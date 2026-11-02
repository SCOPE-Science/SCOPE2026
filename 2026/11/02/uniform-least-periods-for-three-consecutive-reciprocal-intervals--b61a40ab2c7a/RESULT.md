# Uniform least periods for three consecutive reciprocal intervals, and a four-interval obstruction

## Finding

For every integer \(n\ge 1\), let \(R_{n+3,n}\) be the interval exchange of \([1/(n+3),1/n)\) obtained by cutting at \(1/(n+2)\) and \(1/(n+1)\) and **reversing the order of the three pieces without reflecting any piece**. Every point, including every included cutting boundary, has exactly the same least period:

\[
P_n=\frac{3(n+1)(n+2)}{2\gcd(n,3)}
=\begin{cases}\frac{(n+1)(n+2)}2,&3\mid n,\\[2pt]
\frac{3(n+1)(n+2)}2,&3\nmid n.
\end{cases}
\]

Thus the least-period distribution, measured in ordinary (unnormalized) Lebesgue length, is supported at \(P_n\) with mass exactly \(3/[n(n+3)]\) and is zero at every other period. The three-piece statement is sharp as a universal single-period property for this reciprocal-reversal family: the four-piece map \(R_{11,7}\) has two least periods, \(373\) and \(694\), on subsets of lengths \(746/27720\) and \(694/27720\), respectively.

## Assumptions and scope

For integers \(m>n\ge1\), the map \(R_{m,n}\) is defined on the half-open interval \([1/m,1/n)\). Its pieces are the consecutive half-open reciprocal intervals \([1/(k+1),1/k)\), for \(n\le k<m\). The map is the unique piecewise translation that arranges the pieces in reverse left-to-right order while preserving orientation inside each piece. Consequently \(R_{m,n}\) is a bijection of this half-open interval. Least period means the smallest **positive** iterate that returns to the same point; no almost-everywhere qualifier is used.

For the three-piece case put \(g=\gcd(n,3)\) and introduce the positive integer scale

\[
D=\frac{n(n+1)(n+2)(n+3)}{2g}.
\]

In the affine coordinate \(u=D(x-1/(n+3))\), the three consecutive piece lengths are the positive integers

\[
a=\frac{n(n+1)}{2g},\qquad b=\frac{n(n+3)}{2g},\qquad c=\frac{(n+2)(n+3)}{2g}.
\]

These expressions are integers for every \(n\ge1\): in each numerator at least one factor is even; if \(g=3\), at least one factor is also divisible by three. Write \(L=a+b+c\), \(s=a+b\), \(t=b+c\), \(S=s+t=L+b\).

## Proof

**Step 1: exact branch action.** In the scaled half-open interval \([0,L)\), reversing the order of the three translated pieces gives

\[
T(u)=\begin{cases}
u+t,&0\le u<a,\\
u+c-a,&a\le u<a+b,\\
u-s,&a+b\le u<L.
\end{cases}
\]

The branches map, respectively, to \([b+c,L)\), \([c,b+c)\), and \([0,c)\); these intervals partition \([0,L)\).

**Step 2: first-return representation.** On the circle of circumference \(S=L+b\), consider the rotation \(Q(u)=u+t\pmod S\). Take the half-open return section \(J=[0,L)\). A point in \([0,a)\) is sent immediately to \([t,L)\subset J\). A point in \([a,a+b)\) is sent into the omitted gap \([L,S)\); its second iterate is \(u+2t-S=u+c-a\in[c,b+c)\subset J\). A point in \([a+b,L)\) returns in one step as \(u+t-S=u-s\in[0,c)\). Therefore the first return of \(Q\) to \(J\) is exactly \(T\), including all half-open boundary conventions.

**Step 3: coprimality and exact period.** Direct calculation gives

\[
s=\frac{n(n+2)}g,\qquad t=\frac{(n+1)(n+3)}g.
\]

Since \(n+2\) is coprime to both \(n+1\) and \(n+3\),

\[
\gcd\!\bigl(n(n+2),(n+1)(n+3)\bigr)
=\gcd(n,n+3)=\gcd(n,3)=g,
\]

hence \(\gcd(s,t)=\gcd(S,t)=1\). Both \(S\) and \(t\) are integers. For every real offset \(0\le r<1\), the orbit of any point \(j+r\) under \(Q\) visits every one of the \(S\) points \(k+r\), for \(0\le k<S\), exactly once before returning. Because the return section \(J=[0,L)\) comprises exactly \(L\) of the \(S\) integer unit cells, this full rotation orbit has precisely \(L\) returns to \(J\). The first-return transformation \(T\) therefore has **exact** least period \(L\) at every point of \(J\). Substitution of the length formulas yields \(L=3(n+1)(n+2)/(2g)\).

**Step 4: period-mass law.** The entire original interval has Lebesgue length \(1/n-1/(n+3)=3/[n(n+3)]\), and by Step 3 every point in it has least period \(P_n\); no other period occurs.

**Step 5: sharp four-piece contrast.** For \(R_{11,7}\), use the integer scale \(D=\operatorname{lcm}(7,8,9,10,11)=27720\). Consecutive reciprocal piece lengths, from left to right, are \(252,308,385,495\), totalling \(1440\); reversing gives integer translations \(1188,628,-65,-945\) on the respective pieces. The resulting permutation of all \(1440\) unit cells has three cycles with (least-index representative, cycle length) equal to \((0,694)\), \((1,373)\), and \((2,373)\). This is a finite exhaustive identity, verified by the standalone exact-integer program `verify_periods.py`. Each real point in a given half-open unit cell follows precisely the corresponding integer-cell itinerary, because all translations are integers. Thus the two periods have \(694\) and \(2\cdot373=746\) cells, respectively. Rescaling by \(D\) gives the asserted Lebesgue lengths, which sum to \(1440/27720=4/77=1/7-1/11\).

## Verification

Run `python3 verify_periods.py` using the standalone Python standard library. It checks the reciprocal rational scaling and full integer-cell permutation for the first \(50\) three-piece cases, including all boundary cells, and exhaustively enumerates the three cycles of the \(1440\)-cell four-piece example. Exact rational arithmetic is used throughout. The proof of the universal three-piece statement is Steps 1–4 and does **not** depend on finite testing; the four-piece enumeration is exhaustive over its finite state space and is independently auditable from the given integer shifts.

## Relationship to prior work

Hooper, Rafi and Randecker defined the family \(R_{m,n}\) in Remark 7 and explicitly asked which pairs have a common least period at every point. Their Proposition 4 proves only periodicity of rational finite-branch exchanges, not uniform least period or its numeric value; their discussion includes examples with multiple periods. The result above supplies a complete infinite three-consecutive-piece subfamily, including an arithmetic modulus-three formula and the exact masses, together with a contrasting four-piece instance.

Cánovas, Linero Bas and Soler López (2022) study period restrictions for interval exchanges with one and two discontinuities. Linero Bas and Soler López (2025) introduce a general Rauzy-induction approach and describe possible period sets for oriented three-piece exchanges. These frameworks are applicable background, but do not in the inspected material identify the reciprocal family \(R_{n+3,n}\), the explicit formula \(P_n\) for **all** \(n\), or the \(R_{11,7}\) two-period masses. This is a source-specific arithmetic resolution, not a claim that the induced-rotation mechanism is itself new.

## Limitations

This is **not** a classification of all pairs \((m,n)\), nor of all rational three-piece interval exchanges. It proves uniform least period for the specified reciprocal-consecutive family, plus one explicit four-piece failure. Nothing is asserted for any change of half-open conventions that changes the map at discontinuity endpoints. Existing general Rauzy-period algorithms may permit an alternative derivation; exhaustive publication-priority validation and independent review remain open.

## References

1. W. P. Hooper, K. Rafi, A. Randecker, *Renormalizing an infinite rational IET*, arXiv:1808.09989v1 (first public 2018-08-29), *Discrete and Continuous Dynamical Systems* 40 (2020), 5105–5116, doi:10.3934/dcds.2020220. See Remark 7 and Proposition 4. https://arxiv.org/abs/1808.09989
2. J. S. Cánovas, A. Linero Bas, G. Soler López, *On Periods of Interval Exchange Transformations*, *Mathematics* 10 (2022), 1487, doi:10.3390/math10091487. https://doi.org/10.3390/math10091487
3. A. Linero Bas, G. Soler López, *New Results on the Computation of Periods of IETs*, *Mathematics* 13 (2025), 3175, doi:10.3390/math13193175. https://doi.org/10.3390/math13193175
