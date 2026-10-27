"""Independent finite checks of circle-projection Gram spectra and geometry."""
import math
import numpy as np


def spectrum(phi, n):
    B = np.column_stack([np.cos(n * phi), np.sin(n * phi)])
    eig_numeric = np.linalg.eigvalsh(B.T @ B)
    phasor = abs(sum(np.exp(2j * n * phi)))
    eig_predicted = np.array([(len(phi)-phasor)/2, (len(phi)+phasor)/2])
    return eig_numeric, eig_predicted


def distance_mod_one(x):
    return abs(x - round(x))


def check():
    angles_list = [
        np.array([0., math.pi * (math.sqrt(5)-1)/2]),
        np.array([.31, .31 + math.pi*math.sqrt(2)/2, .31 + math.pi*math.sqrt(3)/5]),
        np.array([0., math.pi*math.sqrt(2)/2, math.pi*math.sqrt(3)/3, math.pi*math.sqrt(5)/5, math.pi*math.sqrt(7)/7]),
    ]
    max_eig_error=0.
    all_count=0
    min_ratio=math.inf
    max_ratio=0.
    for angles in angles_list:
        k=len(angles)
        for n in range(1,151):
            observed,predicted=spectrum(angles,n)
            max_eig_error=max(max_eig_error,float(np.max(np.abs(observed-predicted))))
            d=max(distance_mod_one(n*(angle-angles[0])/math.pi) for angle in angles[1:])
            assert observed[0]+1e-10>=4*d*d/k
            assert observed[0]<=4*math.pi**2*(k-1)*d*d+1e-10
            ratio=observed[0]/d**2
            min_ratio=min(min_ratio,ratio)
            max_ratio=max(max_ratio,ratio)
            all_count+=1
    assert max_eig_error<1e-12
    # Direct projected density and Chebyshev isometry verification.
    angles=np.array([.29,1.17,2.45]); k=len(angles)
    coefficients_cos=np.array([.45, -.23, .18, -.32, .12, .07])
    coefficients_sin=np.array([.12, .34, -.17, .24, .11, -.25])
    constant=.31
    t=(np.arange(16384)+.5)*math.pi/16384
    total_numerical=0.
    for phi in angles:
        theta_plus=phi+t; theta_minus=phi-t
        f_plus=constant+sum(math.sqrt(2)*(coefficients_cos[n-1]*np.cos(n*theta_plus)+coefficients_sin[n-1]*np.sin(n*theta_plus)) for n in range(1,7))
        f_minus=constant+sum(math.sqrt(2)*(coefficients_cos[n-1]*np.cos(n*theta_minus)+coefficients_sin[n-1]*np.sin(n*theta_minus)) for n in range(1,7))
        q=.5*(f_plus+f_minus)
        total_numerical+=float(np.mean(q*q))
    total_exact=k*constant**2+sum(sum((coefficients_cos[n-1]*np.cos(n*angles)+coefficients_sin[n-1]*np.sin(n*angles))**2) for n in range(1,7))
    assert abs(total_exact-total_numerical)<1e-12
    # Rank failure for rationally related directions.
    for n in [7,14,21,35,49]:
        eig,pred=spectrum(np.array([0,math.pi/7]),n)
        assert eig[0]<1e-12
    # Dirichlet subsequence test for one quadratic irrational angle.
    beta=(math.sqrt(5)-1)/2
    best=[]
    for n in range(1,20001):
        dist=distance_mod_one(n*beta)
        if not best or dist<best[-1][1]:
            best.append((n,dist))
    assert len(best)>12
    worst_q_dist=max(n*d for n,d in best[3:])
    print('Gram samples:',all_count)
    print('max numerical-vs-exact eigenvalue error:',f'{max_eig_error:.3e}')
    print('minimum and maximum eigenvalue-to-torus-gap-square ratios:',f'{min_ratio:.7f}',f'{max_ratio:.7f}')
    print('pushforward arcsine energy error:',f'{abs(total_exact-total_numerical):.3e}')
    print('rational view kernel checked at 5 frequencies')
    print('quadratic irrational record approximant count:',len(best))
    print('largest record q-times-gap after initial records:',f'{worst_q_dist:.7f}')
    print('PASS')


if __name__ == '__main__':
    check()
