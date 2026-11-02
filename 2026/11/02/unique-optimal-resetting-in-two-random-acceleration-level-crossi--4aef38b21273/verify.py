"""Reproduce the dimensionless crossing-rate calculations. Numerical checks are not an infinite proof."""
import mpmath as mp

mp.mp.dps = 35
C = mp.sqrt(3) / (2 * mp.pi)
A, B = mp.mpf('1.5'), mp.mpf('0.5')


def E(z, mode):
    if mode == 'u':
        return mp.sqrt(3 * mp.pi * z) * mp.erf(mp.sqrt(3 * z))
    return mp.sqrt(mp.pi * z) * mp.erf(mp.sqrt(z))


def H(z, mode):
    return mp.exp(-4*z) + mp.exp(-z if mode == 'u' else -3*z)*E(z,mode)


def G(z, mode):
    if mode == 'u':
        return (mp.mpf(1)/3-z)*mp.exp(-4*z)+(mp.mpf(5)/6-z)*mp.exp(-z)*E(z,mode)
    return (1-3*z)*mp.exp(-4*z)+(mp.mpf(3)/2-3*z)*mp.exp(-3*z)*E(z,mode)


def z_of(t, mode):
    return A/t**3 if mode == 'u' else B/t


def rate(t, mode):
    return C * H(z_of(t,mode),mode)/t


def rate_from_gaussian(t, mode):
    # Compute p_X(level) E[|V| | X=level] without H or G.
    noise=mp.mpf(1)
    initial_velocity, target = (0,1) if mode == 'u' else (1,0)
    mean_x=initial_velocity*t
    vx=t**3/3
    c_vx=t**2/2
    conditional_mean=initial_velocity+c_vx/vx*(target-mean_x)
    conditional_sd=mp.sqrt(t/4)
    p=mp.exp(-(target-mean_x)**2/(2*vx))/mp.sqrt(2*mp.pi*vx)
    abs_mean=(conditional_sd*mp.sqrt(2/mp.pi)*mp.exp(-conditional_mean**2/(2*conditional_sd**2))
              +conditional_mean*mp.erf(conditional_mean/(mp.sqrt(2)*conditional_sd)))
    return p*abs_mean


BREAKS=[0,mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.6'),1,2,4,8,16,32,64,mp.inf]


def stationary(s, mode):
    return C*s*mp.quad(lambda t: mp.exp(-s*t)*H(z_of(t,mode),mode)/t, BREAKS)


def stationary_derivative(s, mode):
    factor=3 if mode == 'u' else 1
    return factor*C*mp.quad(lambda t: mp.exp(-s*t)*G(z_of(t,mode),mode)/t, BREAKS)


def check_mode(mode, expected_z, expected_s, expected_rate):
    z0=mp.findroot(lambda z: G(z,mode),(.8,.83) if mode=='u' else (.4,.45))
    assert abs(z0-mp.mpf(expected_z))<mp.mpf('1e-13')
    t0=(A/z0)**(mp.mpf(1)/3) if mode=='u' else B/z0
    for t in (mp.mpf('.2'),mp.mpf('.75'),mp.mpf('1.1'),mp.mpf('2.4'),mp.mpf('5.5')):
        assert abs(rate(t,mode)-rate_from_gaussian(t,mode))<mp.mpf('1e-29')
    for t in (mp.mpf('.2'),mp.mpf('.7'),mp.mpf('1.1'),mp.mpf('2'),mp.mpf('5')):
        derivative=mp.diff(lambda x: rate(x,mode), t)
        expected=-(3 if mode=='u' else 1)*C*G(z_of(t,mode),mode)/t**2
        assert abs(derivative-expected)<mp.mpf('1e-27')
    for z in (mp.mpf('.05'),mp.mpf('.2'),mp.mpf('.3'),z0/2):
        if z<z0: assert G(z,mode)>0
    for z in (z0+mp.mpf('.01'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5')):
        assert G(z,mode)<0
    s0=mp.findroot(lambda s: stationary_derivative(s,mode),(.50,.54) if mode=='u' else (.48,.53))
    assert abs(s0-mp.mpf(expected_s))<mp.mpf('1e-12')
    assert abs(stationary(s0,mode)-mp.mpf(expected_rate))<mp.mpf('1e-12')
    assert stationary_derivative(s0-mp.mpf('.02'),mode)>0
    assert stationary_derivative(s0+mp.mpf('.02'),mode)<0
    # An independently differentiated integral must agree with the derived signed-kernel integral.
    assert abs(mp.diff(lambda r: stationary(r,mode),s0)-stationary_derivative(s0,mode))<mp.mpf('1e-29')
    return z0,t0,s0,stationary(s0,mode)


if __name__=='__main__':
    out_u=check_mode('u','.8179163359646871669','.5203276894932712149','.1046702621071614738')
    out_v=check_mode('v','.4215836900246711823','.5059430040501757022','.0584658828402267333')
    for mode, values in (('u',out_u),('v',out_v)):
        print(mode, 'peak_z=',mp.nstr(values[0],23),'peak_time=',mp.nstr(values[1],23),
              'opt_dimensionless_r=',mp.nstr(values[2],23),'max_intensity=',mp.nstr(values[3],23))
    print('Reproducibility checks passed. Global one-crossing inequalities require the written proof.')
