# Hyperbolic critical-orbit trichotomy for E_a(z)=(z^2+a)/(z^2-1) over Q_2

## Context

The admitted target asked for a wandering dichotomy for the even bicritical
quadratic rational family E_a(z)=(z^2+a)/(z^2-1) over the 2-adic field Q_2:
either prove no wandering Berkovich Fatou component exists for any admissible
a, or exhibit an explicit wandering disk orbit. While pursuing that target,
the investigation classified every critical orbit uniformly in a. Because the
only possible wild recurrent obstruction lives in critical orbits, this
classification is the critical-orbit half of the dichotomy and an independently
retrievable lemma for non-archimedean dynamics of even bicritical quadratics.

## Definitions

Let Q_2 be the 2-adic field with normalized valuation v_2, |x|_2=2^{-v_2(x)},
and C_2 its completed algebraic closure. For a in Q_2 with a != -1 define
E_a(z)=(z^2+a)/(z^2-1), a degree-2 rational map. In the finite chart
E_a'(z)=-2z(a+1)/(z^2-1)^2, so z=0 is the unique finite critical point when
a != -1; in w=1/z coordinates F_a(w)=(1-w^2)/(1+aw^2) has F_a'(0)=0, so
infinity is the second critical point. Poles are at z=+-1. Write
m=v_2(a), k=v_2(a+1) (finite since a != -1).

## Result

Theorem. For every a in Q_2, a != -1:

1. {1,infinity} is a superattracting 2-cycle: E_a(infinity)=1, E_a(1)=infinity.
2. If v_2(a) <= 0, the critical point 0 lies in the attracting basin of
   {1,infinity}: either the orbit lands on it in finitely many steps
   (postcritically finite cases, e.g. a=1 and a=1/2), or the odd/even tails
   satisfy c_{2n+1} -> 1 and c_{2n} -> infinity 2-adically with the
   valuation doubling recursion t_{n+1}=2d_n-k and growth t_{n+1} >= t_n+2.
3. If m=v_2(a) >= 1, the closed disk B={z:|z|_2 <= 2^{-m}} is invariant,
   E_a contracts B with ratio <= 2^{-m}, and there is a unique attracting
   fixed point gamma in B with |E_a'(gamma)|_2 <= 2^{-(m+1)} attracting 0.
4. If a=0, 0 is a superattracting fixed point.

Corollary. Every E_a is hyperbolic over C_2: both critical points lie in
attracting basins, so no critical point is recurrent and in particular there
is no wild recurrent critical point.

## Proof and evidence

The 2-cycle claim follows from E_a(infinity)=1, E_a(1)=infinity with the
critical point infinity in the cycle, hence multiplier 0. Exact identities
E_a(z)-1=(a+1)/(z^2-1) and
E_a(z)-E_a(w)=(a+1)(w-z)(w+z)/((z^2-1)(w^2-1)) drive everything. Valuation
constraints: m,k cannot both be positive; m<0 gives k=m; m=0 gives a unit
hence k>=1; m>0 gives k=0. A disk lemma gives v_2(z^2-1) >= 3 near z=1 and
exactly 1+t for t=v_2(z-1) >= 2. For m=0, induction on the odd subsequence
preserves d_n=v_2(o_n^2-1)>k so the numerator valuation stays exactly k,
yielding t_{n+1}=2d_n-k and linear-plus growth; the finitely many hits of
+-1 give the PCF captures. For m<0 the same recursion starts after one
step since d_n >= 3 > k=m. For m >= 1, |z^2|_2 < |a|_2 and |z^2-1|_2=1 on B
give invariance and the contraction bound, and Banach's theorem gives gamma;
the multiplier formula gives attraction. Example a=2 has gamma=2 with
multiplier of absolute value 1/4. Exact rational-arithmetic verification in
output/artifacts/critical_orbits.py reproduces doubling patterns
(e.g. a=5: 1,5,11,23), PCF captures, and disk invariance.

## Limitations

This result does not by itself prove branch (A) of the wandering dichotomy
(no wandering Berkovich Fatou component for every a). The implication from
hyperbolicity to no wandering in residue characteristic 2 requires the cited
Rivera-Letelier, Trucco, and Benedetto wild-reduction machinery, which is
invoked but not reproved. What is proved self-containedly is the complete
wild-recurrent-critical-point analysis: no wandering witness of
critical-orbit type exists.

## Reproducibility

Run `python3 output/artifacts/critical_orbits.py` with standard Python 3
(Fraction-based exact arithmetic, no dependencies). It prints orbit
valuations for m<=0 representatives, PCF cases, and m>=1 invariance checks,
ending with ALL_CHECKS_DONE.

## References

- J. Rivera-Letelier, Wild recurrent critical points, arXiv:math/0406417.
- R. L. Benedetto, Wandering domains and nontrivial reduction in
  non-archimedean dynamics, arXiv:math/0312034.
- R. L. Benedetto, Wandering domains in non-archimedean polynomial dynamics.
- Non-archimedean dynamics textbooks for Rivera-Letelier classification and
  Berkovich Fatou theory.
