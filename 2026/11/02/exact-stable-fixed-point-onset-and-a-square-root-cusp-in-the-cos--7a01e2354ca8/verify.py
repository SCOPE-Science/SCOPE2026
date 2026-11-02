"""Independent-of-package numerical checks of exact formulas for the cosine skewed interval map.
Analytic arguments, not finite tests, establish all-parameter completeness.
"""
import mpmath as m
m.mp.dps=60
E=m.e**(-1)
D=m.cos(E)-m.cos(1)
def H(s): return (m.cos(E)-m.cos(m.exp(s-1)))/D
def Hp(s):
    v=m.exp(s-1)
    return v*m.sin(v)/D
def Hpp(s):
    v=m.exp(s-1)
    return (v*m.sin(v)+v*v*m.cos(v))/D
def bisection(f,a,b,iterations=240):
    assert f(a)*f(b)<0,(f(a),f(b))
    for _ in range(iterations):
        c=(a+b)/2
        if f(a)*f(c)<=0: b=c
        else: a=c
    return (a+b)/2
checks=0
def check(c,msg):
    global checks
    if not c: raise AssertionError(msg)
    checks+=1
check(H(0)==0,"H0")
check(abs(H(1)-1)<m.mpf('1e-55'),"H1")
check(Hp(1)>2 and Hp(1)<2+Hp(0),"end-point derivative inequality")
for j in range(201):
    s=m.mpf(j)/200
    check(Hpp(s)>0,"strict convexity")
q=bisection(lambda s:H(s)+s-1,m.mpf('0'),m.mpf('1'))
check(q>m.mpf('0.6'),"right crossing")
check(Hp(q)>1,"right fixed point repelling")
for alpha_text in ['0.01','0.1','0.5','0.8','0.99']:
    alpha=m.mpf(alpha_text)
    st=bisection(lambda s:s*Hp(s)-H(s)-alpha,m.mpf('0'),m.mpf('1'))
    bc=H(st)+(1-st)*Hp(st)
    check(Hp(0)<bc<1,"fold b inside parameter box")
    check(abs(H(st)+alpha-(alpha+bc)*st)<m.mpf('1e-55'),"fold equation")
    check(abs(Hp(st)-alpha-bc)<m.mpf('1e-55'),"tangent equation")
    check(bc>alpha-Hp(0),"stable multiplier lower bound")
    for b in [bc/2, bc*(1-m.mpf('1e-8'))]:
        for j in range(101):
            s=m.mpf(j)/100
            check(H(s)+alpha-(alpha+b)*s>0,"no left fixed below threshold")
    for b in [(bc+1)/2,1-m.mpf('1e-9')]:
        sm=bisection(lambda s:Hp(s)-alpha-b,m.mpf('0'),m.mpf('1'))
        f=lambda s:H(s)+alpha-(alpha+b)*s
        check(f(sm)<0,"fold region reaches negative")
        sl=bisection(f,m.mpf('0'),sm)
        sr=bisection(f,sm,m.mpf('1'))
        check(0<sl<sm<sr<1,"two left fixed points")
        check(abs(f(sl))<m.mpf('1e-55') and abs(f(sr))<m.mpf('1e-55'),"two root equations")
        check(-1<(Hp(sl)-alpha)/b<1,"left fixed attracting")
        check((Hp(sr)-alpha)/b>1,"right of fold repelling")
    for delta in [m.mpf('1e-6'),m.mpf('1e-8')]:
        b=bc+delta
        sm=bisection(lambda s:Hp(s)-alpha-b,m.mpf('0'),m.mpf('1'))
        f=lambda s:H(s)+alpha-(alpha+b)*s
        sl=bisection(f,m.mpf('0'),sm)
        sr=bisection(f,sm,m.mpf('1'))
        C=m.sqrt(2*st/Hpp(st))
        check(abs((sr-sl)/(2*m.sqrt(delta)*C)-1)<m.mpf('0.003'),"square-root position onset")
        M=m.sqrt(2*st*Hpp(st))/bc
        check(abs((((Hp(sr)-alpha)/b)-((Hp(sl)-alpha)/b))/(2*m.sqrt(delta)*M)-1)<m.mpf('0.003'),"square-root multiplier onset")
    s_right=bisection(lambda s:H(s)+(1-bc)*s-1,m.mpf('0'),m.mpf('1'))
    check(s_right>q,"right fixed parameter position")
    check(Hp(s_right)/(1-bc)>1,"right fixed always repelling")
    print('alpha=',alpha_text,'b_critical=',m.nstr(bc,16),'s_critical=',m.nstr(st,16))
print('PASS',checks,'high-precision assertions')
