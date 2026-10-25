# Sharp exponent bound for reducible-fiber component groups at \(\chi=3\)

## Finding

Let \(n_1,\ldots,n_s\) be a nonempty finite multiset of integers at least \(2\), and define

\[
\delta=\sum_{i=1}^{s}\frac{\lfloor n_i^2/4\rfloor}{n_i},
\qquad
L=\operatorname{lcm}(n_1,\ldots,n_s).
\]

If \(\delta\le 3\), then

\[
\boxed{L\le 60.}
\]

Equality holds if and only if the multiset is exactly \(\{3,4,5\}\). For a semistable Jacobian elliptic surface \(\pi:X\to\mathbf P^1\) over \(\mathbf C\) with \(\chi(\mathcal O_X)=3\), finite Mordell--Weil group, and reducible fibers \(I_{n_1},\ldots,I_{n_s}\), the polyhedrality condition \(\delta(\pi)\le 3\) therefore bounds the exponent of the product of their component groups by \(60\), because the component group of an \(I_n\) fiber is cyclic of order \(n\). The extremal numerical fiber multiset is \(I_3+I_4+I_5\).

The equality statement concerns the numerical constraint. It does not assert that a surface realizing the extremal multiset exists with all the required geometric properties.

## Assumptions and scope

The numerical claim concerns every finite multiset \(n_i\ge2\) satisfying \(\sum_i\lfloor n_i^2/4\rfloor/n_i\le3\). In the geometric application, the surface is semistable, Jacobian, over \(\mathbf P^1_{\mathbf C}\), has \(\chi(\mathcal O_X)=3\), finite Mordell--Weil group, and only multiplicative reducible fibers \(I_{n_i}\). The condition \(\delta(\pi)\le\chi\) is the published numerical criterion for the rational polyhedral Mori-cone range in this setting.

The invariant is the exponent of the product \(G=\prod_i\mathbf Z/n_i\mathbf Z\), namely the least positive integer annihilating every element of \(G\). This exponent equals \(L=\operatorname{lcm}(n_1,\ldots,n_s)\). The result is not a claim about the order of the product group, nor a classification of actual Mordell--Weil torsion.

## Proof

Put \(c(n)=\lfloor n^2/4\rfloor/n\). For integers \(k\ge1\),

\[
c(2k)=\frac{k}{2},\qquad c(2k+1)=\frac{k(k+1)}{2k+1}.
\]

These formulas give

\[
c(2k+1)-c(2k)=\frac{k}{2(2k+1)}>0,
\qquad
c(2k+2)-c(2k+1)=\frac{k+1}{2(2k+1)}>0.
\]

Thus \(c(n)\) is strictly increasing for \(n\ge2\). Since \(c(13)=42/13>3\), every admissible entry satisfies \(2\le n_i\le12\). Also \(c(n_i)\ge c(2)=1/2\), so \(s\le6\).

It remains a finite exact classification: enumerate all nondecreasing tuples of length \(1\) through \(6\) with entries in \(\{2,3,\ldots,12\}\), retaining exactly those whose rational cost is at most \(3\). Nondecreasing tuples represent each multiset exactly once. The standalone verifier `verification/check_lcm_bound.py` uses rational arithmetic and exhaustive enumeration; it finds exactly \(78\) feasible multisets and a unique maximum of \(L=60\), at \((3,4,5)\). This finite search is exhaustive because the bounds on each entry and on the length were proved above.

The extremizer directly satisfies the constraint:

\[
c(3)+c(4)+c(5)=\frac23+1+\frac65=\frac{43}{15}\le3,
\qquad
\operatorname{lcm}(3,4,5)=60.
\]

Finally, the product of the component groups of the reducible fibers is \(\prod_i\mathbf Z/n_i\mathbf Z\); its exponent is the least common multiple of the cyclic orders. This proves the stated geometric consequence.

## Verification

The included standard-library script `verification/check_lcm_bound.py` was executed. It asserts the monotonicity and cutoff facts, enumerates every feasible multiset with exact `Fraction` arithmetic, and asserts that there are \(78\) feasible multisets and that \((3,4,5)\) is the unique maximizer with least common multiple \(60\). A second independent recursive enumeration produced the same count and unique maximizer. Neither calculation is used to infer an infinite-family statement: the finite bounds reduce the claim to this exhaustive search.

## Relationship to prior work

Laface, Li, and Liu study the Mori cone of Jacobian elliptic surfaces with finite Mordell--Weil group and one reducible fiber. Laface and Li then use

\[
\delta(\pi)=\sum_i\frac{\lfloor n_i^2/4\rfloor}{n_i}
\]

to characterize the polyhedral range for semistable Jacobian elliptic surfaces with several reducible fibers. Their papers also use the sum \(N(\pi)=\sum_i n_i\) for Mori-dream criteria. The inspected statements do not give the exact maximum of the different invariant \(\operatorname{lcm}(n_i)\) under \(\delta\le3\). A bound on \(\sum_i n_i\) alone does not identify the maximum exponent of \(\prod_i\mathbf Z/n_i\mathbf Z\); the numerical extremizer here is \(\{3,4,5\}\).

The full text of the Laface--Li paper was inspected for its definition of \(\delta\), hypotheses, and related numerical criteria. The full text of the earlier Laface--Li--Liu paper was not retrieved; only its arXiv abstract and metadata were available, so priority risk remains for an unstated related observation in that source or elsewhere.

## Limitations

The result is restricted to the first permitted value \(\chi=3\); no formula for the maximum exponent when \(\chi>3\) is claimed. The unique extremal multiset is sharp for the numerical constraint, but geometric realization of \(I_3+I_4+I_5\) by a surface satisfying every stated hypothesis has not been established here. The bound is on the exponent of the product of component groups, not its order and not the exact exponent of the Mordell--Weil torsion subgroup. The earlier paper's full text and unindexed literature remain priority risks.

## References

1. Antonio Laface, Sichen Li, and Jihao Liu, *Mori dream Jacobian elliptic surfaces of Kodaira dimension one*, arXiv:2608.09002v1, first public 2026-08-10. https://arxiv.org/abs/2608.09002
2. Antonio Laface and Sichen Li, *Semiampleness on Jacobian elliptic surfaces of Kodaira dimension one*, arXiv:2609.23306v1, first public 2026-09-20, especially Theorem 1.1 and the definition of \(\delta(\pi)\). https://arxiv.org/abs/2609.23306
