#!/usr/bin/env python3
"""Independent arithmetic checks for a discrete-time SIR peak-day transition.

Standard Python only. The mathematical proof of uniqueness and global peaking
is in RESULT.md; the sampled checks here are not a replacement for that proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction

N = 0

def check(assertion, label):
    global N
    if not assertion:
        raise AssertionError(label)
    N += 1

with localcontext() as ctx:
    ctx.prec = 65
    one = Decimal(1)
    two = Decimal(2)
    half = one / two
    three = Decimal(3)
    four = Decimal(4)
    ln2 = two.ln()

    def F(q):
        kappa = Decimal('4.5') - three*q
        return 18*q - 7 - 12*(q.ln()*kappa).exp()

    def FD(q):
        kappa = Decimal('4.5') - three*q
        p = (q.ln()*kappa).exp()
        return 18-12*p*(kappa/q-three*q.ln())

    def one_pass(q):
        lamb = -four*q.ln()
        S = Decimal(3)/4
        I = one/4
        R = Decimal(0)
        vals = [(S,I,R)]
        for t in range(12):
            new = S * (one - (-lamb*I).exp())
            newS = S-new
            newI = I/2 + new
            newR = R + I/2
            S,I,R = newS,newI,newR
            vals.append((S,I,R))
        return lamb,vals

    # Algebraic rational first two steps at q=1/2.
    S1 = Fraction(3,8)
    I1 = Fraction(1,2)
    S2 = S1*Fraction(1,4)
    I2 = I1/2 + S1-S2
    check(S2 == Fraction(3,32), 'rational S2')
    check(I2 == Fraction(17,32), 'rational I2')
    check(I2 > I1 > Fraction(1,4), 'rational peak day two')
    check(F(half) == half, 'exact F at right endpoint')
    check(F(one/4) < 0, 'negative left endpoint')

    # Rigorous monotonicity argument is analytic in RESULT.md.
    # Check its exact evaluated endpoint lower bound.
    check(Decimal('4.5')*(one-ln2)>0, 'analytic derivative lower bound')
    check(three*ln2/8<half, 'analytic decay inequality')

    low, high = one/4,half
    for step in range(230):
        mid=(low+high)/2
        if F(mid)>0:high=mid
        else:low=mid
        check(F(low)<=0<=F(high),'bracket has correct signs')
    qstar=(low+high)/2
    lambdastar=-four*qstar.ln()
    jump=Decimal(7)/16-three*qstar/8
    S1star=three*qstar/4
    I1star=Decimal(7)/8-three*qstar/4
    S2star=three/4*(qstar.ln()*(Decimal('4.5')-three*qstar)).exp()
    check(abs(F(qstar))<Decimal('1e-58'),'root residual')
    check(abs((S1star-S2star)-jump)<Decimal('1e-58'),'jump two formulas')
    check(abs(jump-I1star/2)<Decimal('1e-58'),'jump equals recovered mass at tie')
    check(Decimal('3.32040')<lambdastar<Decimal('3.32041'),'lambda interval')
    check(Decimal('0.27399')<jump<Decimal('0.27401'),'jump interval')

    for j in range(401):
        q=(one/4)+(one/4)*Decimal(j)/400
        # Necessary inequalities used by proof; independent decimal evaluation.
        check(FD(q)>Decimal('4.5')*(one-ln2)-Decimal('1e-50'), 'derivative bound')
        lamb,states=one_pass(q)
        check(states[1][1]>states[0][1], 'I1>I0')
        check(all(states[t+1][1]<states[t][1] for t in range(2,12)), 'strict post-day-two decay')
        check(lamb*states[2][0]<half,'post-day-two force bound')
        check(all(abs(sum(states[t])-one)<Decimal('1e-59') for t in range(13)), 'mass conservation')
        check((F(q)>0)==(states[2][1]>states[1][1]), 'sign correspondence')
        expected_peak=2 if F(q)>0 else 1
        check(max(range(len(states)),key=lambda idx:states[idx][1])==expected_peak,'global peak on tested horizon')

    # Confirm strict transmission-order reversal at two exact q-values.
    _,first=one_pass(half)
    _,second=one_pass(one/4)
    check(first[2][1]>first[1][1],'weak-transmission later peak')
    check(second[1][1]>second[2][1],'strong-transmission earlier peak')
    check(one-first[2][0]>one-second[1][0],'peak-cumulative reversal')

    print('PASS:',N,'arithmetic assertions')
    print('critical q =',qstar)
    print('critical lambda =',lambdastar)
    print('downward jump =',jump)
    print('left limit =',one-S2star)
    print('right limit =',one-S1star)
