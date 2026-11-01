"""Exact symbolic verification for four-cell coding of a random W-map."""
import sympy as sp

a, p = sp.symbols('a p', real=True, positive=True)
q = (a-2)/a
z = p*(a-2)/(a-1)
r = sp.factor(z-q)
w = sp.Matrix([[1/a, (a-2)/(2*a), (a-2)/(2*a), 1/a]])
v = sp.Matrix([[1-p+p/(a-1), p*(a-2)/(2*(a-1)), p*(a-2)/(2*(a-1)), 0]])
P = sp.Matrix.vstack(w, v, v, w)
mu = sp.factor(q/(1-z+q))
pi = sp.simplify((1-mu)*w + mu*v)
Pi = sp.ones(4,1)*pi

def zero(M):
    return all(sp.cancel(entry)==0 for entry in M)

assert zero(P*sp.ones(4,1)-sp.ones(4,1))
assert zero(pi*P-pi)
# Direct identification of this stationary density with the original source's four-cell formula.
c = a*(a-1)/(2*(a-1)**2 - p*a*(a-2))
lengths = sp.Matrix([[1/a,(a-2)/(2*a),(a-2)/(2*a),1/a]])
source_heights = sp.Matrix([[c*((a-1)-p*(a-2)),c,c,c*(1-p*(a-2)/(a-1))]])
assert zero(sp.Matrix([[pi[0,j]/lengths[0,j] for j in range(4)]])-source_heights)
assert zero(P**2-Pi-r*(P-Pi))
assert sp.factor(mu*(1-mu)) != 0
pc=sp.factor((a-1)/a)
Pc=sp.simplify(P.subs(p,pc))
pic=sp.simplify(pi.subs(p,pc))
assert sp.simplify(r.subs(p,pc))==0
assert zero(Pc**2-sp.ones(4,1)*pic)
assert not zero(Pc-sp.ones(4,1)*pic)
assert sp.factor(mu.subs(p,pc)-q)==0
assert zero(pic-sp.Matrix([[2*(a-1)/a**2,(a-2)/(2*a),(a-2)/(2*a),2/a**2]]))

# Check branch endpoint images and induced row probabilities at several rational a.
for av in [sp.Rational(5,2), sp.Rational(8,3), sp.Integer(3),sp.Integer(4),sp.Integer(5),sp.Integer(9)]:
    endpoints=[sp.Integer(0),1/av,sp.Rational(1,2),(av-1)/av,sp.Integer(1)]
    def W(x,branch,which):
        if branch in (0,3):
            return 1-av*x if branch==0 else 1-av*(1-x)
        y=x if branch==1 else 1-x
        if which==0:
            return 2*y/(av-2)-2/((av-2)*av)
        return 2*(av-1)*y/(av-2)-2*(av-1)/((av-2)*av)
    for branch in range(4):
        for which in (0,1):
            endpoints_img={sp.simplify(W(endpoints[j],branch,which)) for j in (branch,branch+1)}
            target={sp.Integer(0),sp.Integer(1)} if branch in (0,3) else ({sp.Integer(0),1/av} if which==0 else {sp.Integer(0),(av-1)/av})
            assert endpoints_img == target, (av,branch,which,endpoints_img,target)
    for pv in [sp.Rational(1,5),sp.Rational(1,2),(av-1)/av,sp.Rational(9,10)]:
        Pv=P.subs({a:av,p:pv})
        piv=pi.subs({a:av,p:pv})
        assert zero(piv*Pv-piv)
        assert zero(Pv**2-sp.ones(4,1)*piv-r.subs({a:av,p:pv})*(Pv-sp.ones(4,1)*piv))
        if pv == (av-1)/av:
            assert zero(Pv**2-sp.ones(4,1)*piv)

print('PASS: full symbolic transition identity, stationary probabilities, unique critical curve, branch endpoint images, and 24 rational-parameter cases')
print('critical_parameter:',pc)
print('nontrivial_eigenvalue:',r)
print('stationary_central_probability:',mu)
print('critical_stationary_vector:',pic)
