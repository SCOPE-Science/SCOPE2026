import math

def yroot(n,t):
    if t == 0.0:
        return 0.0
    disc=(1+t*t)**2+4*(n*n-1)*t*t
    return (math.sqrt(disc)-(1+t*t))/(2*(n+1)*t)

def check(n,t):
    y=yroot(n,t)
    p=(n+1)*t*y*y+(1+t*t)*y-(n-1)*t
    den=n*(1-y*y)-(t+y)**2
    tp=t-(1-t*t)*(t+y)/den
    if not (-1 < y < 1):
        raise AssertionError((n,t,'root range',y))
    if abs(p) > 1e-11:
        raise AssertionError((n,t,'stationarity',p))
    if abs(tp) > 1e-11:
        raise AssertionError((n,t,'next center',tp))
    # Directly replay the exact algebraic relation used in the proof.
    numerator=t*den-(1-t*t)*(t+y)
    if abs(numerator+p) > 2e-12:
        raise AssertionError((n,t,'identity',numerator+p))

for n in (2,3,5,10):
    for t in (-0.9,-0.5,-0.1,0.1,0.5,0.9):
        check(n,t)
print('VERIFY_OK')
