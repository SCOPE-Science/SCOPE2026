# Critical-value rigidity and an indifferent obstruction for G_c(z)=(z^2+c)/(cz+1) over Q2

## Context

The admitted target asked for a uniform wandering dichotomy for the marked-fixed-point quadratic rational family G_c(z)=(z^2+c)/(cz+1) over Q2 (c != 0,-1): either prove no wandering Berkovich Fatou component exists for every admissible c, or exhibit one explicit wandering component with disjointness and Julia-witness verification. Both branches proved blocked: the odd-c regime has genuinely bad reduction (degree drops 2 to 1 mod 2 with the pole inside the hole disk), and certified disk searches returned only preperiodic attractor-bound orbits. The finding reported here is the strongest proved byproduct of that target work: exact critical-value identities constraining every future attack, plus a certified structural obstruction at the bad-reduction stress case c0=-5.

## Definitions

Let |.|_2 be normalized with |2|_2=1/2 and v=v_2. For c in Q2, c != 0,-1, G_c(z)=(z^2+c)/(cz+1) has degree 2, fixes infinity with multiplier c and fixes z=1 with multiplier (2-c)/(c+1). For c != 1 there is a third finite fixed point z3=c/(1-c). Finite critical points are the two distinct roots r1,r2 of c*z^2+2*z-c^2=0 with sum -2/c and product -c; critical values are vi=G_c(ri).

## Result

Lemma 1 (orbit identities). For all admissible c,z1,z2: G_c(z1)-G_c(z2)=(z1-z2)((z1+z2)+c*z1*z2-c^2)/((cz1+1)(cz2+1)); G_c(z)-c=z(z-c^2)/(cz+1); and for c != 1, G_c(z)-z3=(z-z3)(z+c)/(cz+1).

Lemma 2 (critical-value rigidity). Whenever c^3+1 != 0, v1+v2=-4/c^2 and v1*v2=-4/c. Lemma 4: the only c in Q2 with c^3=-1 is the excluded c=-1 (since c^2-c+1=0 has discriminant -3=5 mod 8, a nonsquare in Q2). Corollary 3: for odd c (v(c)=0) both critical values have valuation exactly 1. For v(c)=m>=1 the critical-value valuations are {2-2m,m} if distinct.

Lemma 5 (bad reduction). For odd c the integral model reduces mod 2 with degree drop 2->1 and hole at z=1; G_c(1+2t)-1=2t(2+2t-c)/((c+1)+2ct) with numerator cofactor a unit and denominator even; the pole p=-1/c lies in D(1,1/2). If v(c)=0 and v(z)<0 then v(G_c(z))=v(z) exactly, so negative-valuation tails are exactly stable.

Theorem (c0=-5 obstruction). For G_{-5}: fixed points 1 (multiplier -7/4, repelling), z3=-5/6 (multiplier -35/31, indifferent), infinity (multiplier -5, indifferent). The Q2-irrational period-2 cycle z^2+z+1=0 has exact multiplier 19/31 (indifferent). The genuine period-3 points (certified Newton polygon, valuations {1,1,0,0,0,0}, nonzero pole/fixed/separability resultants) lie in valuations {0,1}. Both critical points lie in Q2 (discriminant -124=4*(-31), -31=1 mod 8) with distinct forward valuation traces stabilizing at -1 (at 2-adic distance 2^-3 from z3) and -2. Hence no cycle of period <=3 is attracting and neither critical orbit lands on one: no proof of the no-wandering branch can proceed via a low-period uniform-hyperbolicity shortcut at c0=-5.

## Proof and evidence

All identities are polynomial identities over Z[c,z] verified by expansion; the critical-value formulas follow by symmetric elimination using r1+r2=-2/c and r1r2=-c. The period-2 multiplier follows from the exact reduction N(w)=7w-20 on w^2+w+1=0 giving products 589 and 31, hence 589/31^2=19/31, cross-checked by an independent Sylvester-determinant computation (589). Period-3 genuineness follows from exact divisions with remainder 0 plus six nonzero resultants (three pole levels, two fixed factors, separability). Critical traces use a bit-by-bit Hensel lift of sqrt(-31) to 2^200 (residue 0) with valuation-aware (unit,shift) arithmetic at 200-bit cap (all shifts <=2, swap-checked). The single script output/artifacts/certify.py re-verifies every fact with exact integer/Fraction arithmetic and reports ALL_PASS True.

## Limitations

Proves neither branch of the wandering dichotomy: no wandering Fatou component is exhibited and no uniform no-wandering theorem is proved. Non-absorption is proved only for periods <=3 at c0=-5; higher-period attractors are not excluded. The r_a tail near the indifferent point z3 is an observation, not a Siegel-type claim. Whether c0=-5 carries a wandering component remains open conjecture.

## Reproducibility

Run python3 output/artifacts/certify.py (no external dependencies); it re-verifies the difference identity, the 2-cycle reduction and multiplier with Sylvester cross-check, both polynomial divisions, the Newton lower hull, all six genuineness resultants, the Hensel lift, and both critical-orbit traces, writing output/artifacts/emergent_cert.json.

## References

Rivera-Letelier, Irrational Fatou components in non-Archimedean dynamics, arXiv:2505.09383 (2026). Benedetto, papers and thesis on p-adic dynamics (Amherst page), including Wandering domains and nontrivial reduction (Illinois J. Math. 49, 2005) and Components and periodic points (Proc. LMS 84, 2002). Ramadas-Silversmith, Equations at infinity for critical-orbit-relation families, arXiv:2008.10095. Ingram, Critical orbits of polynomials with a periodic point of specified multiplier, arXiv:1706.05352. Benedetto-DeMarco-type M2 bifurcation literature for equivalent-formulation comparison.
