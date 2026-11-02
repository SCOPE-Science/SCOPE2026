# Nine chores are sharp for EFX–Pareto incompatibility in a four-agent complementary two-type market

## Finding

For the four-agent cost domain with three chore classes \(A,B,C\) of per-agent cost vectors
\[
(r,r,r,r),\qquad(1,1,r,r),\qquad(r,r,1,1),\qquad r>3,
\]
every instance with at most eight chores admits a complete allocation satisfying both envy-freeness up to any own chore (EFX) and Pareto optimality (PO). The count of chores is sharp **within this domain**. At nine chores the multiset of class sizes \((3,3,3)\) fails, by He and Tao's published construction [1]. The contribution here is the universal eight-chore classification, not the nine-chore counterexample.

## Assumptions and scope

There are exactly four agents, indexed \(1,2,3,4\), and \(r\) is an arbitrary real number strictly greater than \(3\). The chores are indivisible and completely allocated. Agents \(1,2\) have identical additive disutilities and agents \(3,4\) have identical additive disutilities. A class-\(A\) chore costs every agent \(r\), a class-\(B\) chore costs agents \(1,2\) exactly \(1\) and agents \(3,4\) exactly \(r\), and a class-\(C\) chore has the reversed costs. Multiplicities \((a,b,c)\) are arbitrary nonnegative integers with \(a+b+c\le8\).

For an allocation \(X=(X_1,X_2,X_3,X_4)\), EFX means \(d_i(X_i\setminus\{g}\})\le d_i(X_j)\) for every ordered pair of agents \((i,j)\) and every \(g\in X_i\). PO means there is no complete allocation \(Y\) such that \(d_i(Y_i)\le d_i(X_i)\) for each agent and strict inequality for at least one.

## Proof

Write an allocation as its four-by-three nonnegative integer incidence matrix, whose column sums are \(a,b,c\). This identifies all allocations modulo permutations of indistinguishable chores. There are \(\binom{a+3}{3}\binom{b+3}{3}\binom{c+3}{3}\) such matrices for a fixed profile; summing over all \(165=\binom{11}{3}\) multiplicity triples with total at most eight gives exactly \(125970=\binom{20}{12}\) matrices.

For any fixed allocation and ordered pair of agents, both sides of each EFX inequality are linear integer-coefficient expressions \(\alpha r+\beta\), each summing costs of at most eight chores. Similarly, for any two allocations, each agent's Pareto-comparison inequality has that form. In every resulting difference, the absolute coefficients of \(r\) and of the constant are at most eight. Therefore all nonconstant signs are fixed between the positive breakpoints \(r>3\) of ratios of integers with numerator and denominator at most eight. Those breakpoints are exactly \(7/2,4,5,6,7,8\). Consequently the entire set of EFX allocations and the PO order are constant on each of the seven open intervals and at each of the six breakpoints.

The accompanying standalone `verify_nine_chores.py` enumerates every incidence matrix and tests the literal EFX inequalities and all possible strict Pareto dominators using exact integers. For the seven open intervals it takes respectively the representatives \(13/4,15/4,9/2,11/2,13/2,15/2,9\); at the six endpoints it tests \(7/2,4,5,6,7,8\). At every one of the thirteen parameter cells and every one of the \(165\) profiles, it confirms existence of at least one EFX and PO allocation. The coefficient argument makes this finite exhaustive test a proof over the continuum \(r>3\), not an extrapolation from samples.

For sharpness, He and Tao [1, Theorem 2] establish that the \((3,3,3)\) instance has no joint EFX+PO allocation whenever \(r>3\). The accompanying verifier also independently checks its thirteen representative parameter cells; the all-real obstruction itself is credited to [1].

## Verification

Run `OPENBLAS_NUM_THREADS=1 python verify_nine_chores.py` with Python 3 and NumPy. The code uses 64-bit integer arithmetic after scaling a rational sample \(r=p/q\) to item costs \(p\) and \(q\), so comparisons are exact; no floating-point tests are performed. It enumerates \(125970\) allocation matrices per cell and checks every potential dominator of every EFX allocation. It prints thirteen positive cell certificates and thirteen nine-chore sharpness checks. The source code itself, not a detached log, is supplied for independent replay.

## Relationship to prior work

He and Tao [1] prove a four-agent, nine-chore bi-valued incompatibility construction for every \(r>3\), and establish broad existence of EFX (without simultaneous PO) in four-agent bi-valued markets. Their result alone does not imply that all smaller profiles in the complete symmetric three-class domain have EFX+PO allocations. The at-most-eight guarantee and the exact finite parameter-cell certificate are the distinct contribution. Previously established EFX results for at most twice the number of agents do not by themselves ensure PO.

## Limitations

The result does **not** assert that nine chores are necessary for EFX–PO incompatibility in unrestricted four-agent bi-valued markets. It does not cover additional chore cost types, unequal group sizes, or \(1<r\le3\). The lower bound is computer-assisted and depends on the exhaustive finite checker; an independent audit has not been conducted. Publicly unindexed prior finite classifications remain possible.

## References

[1] Wentao He and Biaoshuai Tao, *EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence*, arXiv:2606.08872, originally public 2026-06-07, Theorem 2. https://arxiv.org/abs/2606.08872
