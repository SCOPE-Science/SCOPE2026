# Square-marked census and finite-basis density for commutative three-nilpotent semigroups

## Finding

Fix an integer \(n\geq 3\). Let \(\mathcal C_n\) be the set of all **commutative associative multiplication tables on one fixed labelled set of size \(n\)** with a zero \(0\), with every triple product equal to \(0\), and with at least one nonzero double product. Thus the nilpotency index is exactly three. For \(S\in\mathcal C_n\), set
\[
\nu(S)=|\{a\in S:a^2\ne0\}|,\qquad
L_n(z)=\sum_{S\in\mathcal C_n}z^{\nu(S)}.
\]
Writing \(k=n-1-m\), the **complete labelled square-count distribution** is
\[
\boxed{L_n(z)=n\sum_{m=1}^{n-2}\binom{n-1}{m}
\sum_{j=0}^{k}(-1)^j\binom{k}{j}
(k+1-j)^{\binom m2}\bigl(1+(k-j)z\bigr)^m.}\tag{1}
\]

There is also an **exact isomorphism-class square-count distribution**. Let \(U_n(z)\) be the sum of \(z^{\nu(S)}\) over the isomorphism classes in \(\mathcal C_n\). For a partition \(\lambda\vdash m\), let \(\pi_\lambda\) have cycle type \(\lambda\); let \(D_\lambda\) and \(E_\lambda\) be the multisets of orbit lengths of its action on, respectively, diagonal unordered pairs \(\{a,a\}\) and off-diagonal unordered pairs \(\{a,b\}\). For \(\mu=(\mu_1,\ldots,\mu_t)\vdash k\), and \(J\subseteq\{1,\ldots,t\}\), put
\[
H_{\mu,J}(\ell)=\sum_{i\notin J,\,\mu_i\mid\ell}\mu_i,
\qquad Z_\lambda=\prod_{r\ge1}r^{a_r}a_r!
\quad(a_r=|\{i:\lambda_i=r\}|).
\]
Then an explicit Burnside formula, involving only integer partitions, is
\[
\boxed{U_n(z)=\sum_{m=1}^{n-2}\ \sum_{\lambda\vdash m}\ \sum_{\mu\vdash n-1-m}
\frac{1}{Z_\lambda Z_\mu}\sum_{J\subseteq[t]}(-1)^{|J|}
\prod_{\ell\in E_\lambda}(1+H_{\mu,J}(\ell))
\prod_{\ell\in D_\lambda}\bigl(1+H_{\mu,J}(\ell)z^\ell\bigr).}\tag{2}
\]
Products over empty orbit collections equal one. Formula (2) is manifestly computationally finite and returns a polynomial with nonnegative integer coefficients, even though its individual Burnside summands can be rational.

For the **full power semiring** \(\mathcal P(S)\) (all subsets, including the empty set, with union and setwise product, in the constant-free semiring signature), the finite-basis criterion of Wang--Yin--Wang says that, for these semigroups,
\[
\mathcal P(S)\text{ has a finite equational basis}\quad\Longleftrightarrow\quad\nu(S)>0.
\]
Consequently, the exact counts for labelled objects are \(L_n(1)-L_n(0)\) (finitely based) and \(L_n(0)\) (not finitely based); the corresponding isomorphism-class counts are \(U_n(1)-U_n(0)\) and \(U_n(0)\).

If a multiplication table is chosen uniformly from \(\mathcal C_n\), the **nonfinite-basis probability** \(\delta_n=L_n(0)/L_n(1)\) satisfies, for every \(n\ge4\),
\[
\boxed{0\le\delta_n\le
\max\left\{2^{-(n-2)/2},\ (n/2)^{-\sqrt n}\right\}.}\tag{3}
\]
In particular \(\delta_n=\exp(-\Omega(\sqrt n\log n))\), so the proportion with finitely based full power semirings tends to one faster than any inverse power of \(n\). The probability is **conditional on commutative nilpotency index exactly three**, not on the set of all finite semigroups.

## Assumptions and scope

All objects are finite, binary multiplication is commutative and associative, the zero is absorbing, every triple product is zero, and at least one double product is nonzero. The counts in (1) use a fixed labelled underlying set; (2) counts isomorphism classes. No identity element is assumed. The statistic \(\nu\) counts elements whose individual squares are nonzero, **not** the number of distinct nonzero square values. For a formal factor with exponent zero, the usual empty-function convention \(0^0=1\) applies.

## Proof

**Canonical decomposition.** Since \(S^3=\{0\}\) and \(S^2\ne\{0\}\), write \(A=S\setminus S^2\) and \(B=S^2\setminus\{0\}\), of sizes \(m\ge1\) and \(k\ge1\), with \(m+k+1=n\). Every product with a factor in \(B\) vanishes. Indeed, \(B\subset S^2\) and \(S^3=\{0\}\). Thus multiplication is uniquely specified by a symmetric map
\[
f:\operatorname{Sym}^2(A)\longrightarrow B\cup\{0\}
\]
whose image contains every member of \(B\). Conversely, every such map gives a commutative associative three-nilpotent semigroup with exactly the displayed \(A\) and \(B\). The sets \(A,B\) and \(0\) are intrinsic, so no table is counted twice. Since every square of a member of \(B\cup\{0\}\) is zero, \(\nu(S)\) is exactly the number of diagonal arguments \(\{a,a\}\) to which \(f\) assigns a nonzero value.

**Labelled generating polynomial.** Choose the zero in \(n\) ways, then \(A\) among the remaining elements in \(\binom{n-1}{m}\) ways. With \(k\) named nonzero product values, exclusion of a given set of \(j\) values leaves \(k+1-j\) possible images for each of the \(\binom m2\) off-diagonal arguments. For each of the \(m\) diagonal arguments the weighted choice sum is \(1+(k-j)z\): zero has weight one and each nonzero value has weight \(z\). Inclusion--exclusion over the \(k\) required nonzero product values gives exactly (1). This is valid even when the off-diagonal argument set is empty.

**Isomorphism-class polynomial.** Once \(m,k\) are fixed, all isomorphisms are given by independent permutations \(\pi\in\mathfrak S_m\) of \(A\) and \(\sigma\in\mathfrak S_k\) of \(B\), while fixing the zero. A symmetric multiplication table \(f\) is fixed precisely when \(f(\pi u)=\sigma f(u)\) for every unordered pair \(u\). If \(u\) lies in a \(\pi\)-orbit of length \(\ell\), its image is determined by one color fixed by \(\sigma^\ell\). For a permutation \(\sigma\) of cycle type \(\mu\), allowing the zero plus the cycles of \(\sigma\) not in \(J\) gives exactly \(1+H_{\mu,J}(\ell)\) choices. Each off-diagonal orbit therefore supplies this unweighted factor; each diagonal orbit supplies \(1+H_{\mu,J}(\ell)z^\ell\), since a nonzero choice makes all \(\ell\) corresponding diagonal squares nonzero. An equivariant image contains either all or none of each cycle of \(\sigma\), so inclusion--exclusion over missing **cycles** (not individual points) forces surjectivity onto \(B\). The displayed product is the resulting fixed-table polynomial. Burnside's lemma and the fact that a permutation class of cycle type \(\lambda\) occupies the fraction \(1/Z_\lambda\) of \(\mathfrak S_m\) give (2). The argument works for arbitrary \(n\).

**Finite-basis interpretation and density.** The cited commutative nilpotent criterion has nilpotency index \(d=3\) here; its requirement \(a^{d-1}\ne0\) is exactly \(\nu(S)>0\). Fix one pair \((m,k)\) in the labelled sum. A multiplication table with \(\nu=0\) must use all \(k\) nonzero product values on its off-diagonal arguments. For every such fixed off-diagonal table there are exactly \((k+1)^m\) admissible diagonal completions, only one of which has all diagonal values zero. Other off-diagonal tables can contribute admissible completions but none with \(\nu=0\). Consequently, in each nonempty \((m,k)\) stratum, the fraction with \(\nu=0\) is at most \((k+1)^{-m}\). If that fraction is nonzero, then all \(k\) nonzero colors occur off-diagonal, so \(k\le\binom m2\).

When \(k<n/2\), the identity \(m=n-1-k\) gives \(m>(n-2)/2\), and the fraction is at most \(2^{-(n-2)/2}\). When \(k\ge n/2\), the necessary inequality \(k\le m(m-1)/2\) gives \(m>\sqrt n\), and the fraction is at most \((n/2)^{-\sqrt n}\). Taking the weighted average over all strata proves (3). Both bounds decay faster than every power of \(n^{-1}\), establishing the asserted density rate.

## Verification

The accompanying `verify.py` is a standalone Python 3 program using only the standard library. It independently generates symmetric multiplication tables in all fifteen \((m,k)\) strata for \(3\le n\le7\), compares their full square distributions with (1), and checks total labelled counts for \(3\le n\le11\) against the published complete census. It independently enumerates orbits under generator and nonzero-product relabeling for \(3\le n\le6\) and compares them to (2); total isomorphism-class counts for \(3\le n\le9\) agree with the earlier census. Integer checks of the two density-bound cases are also included. All finite calculations supplement the unrestricted counting and Burnside proofs.

For illustration, the numbers (not finitely based, finitely based) among labelled tables are \((12,72)\) for \(n=4\), \((140,1480)\) for \(n=5\), and \((4661707146390,11938155261366960)\) for \(n=10\). Among isomorphism classes they are \((1,4)\) for \(n=4\), \((3,20)\) for \(n=5\), \((12,143)\) for \(n=6\), and \((555,79442)\) for \(n=8\).

## Relationship to prior work

Distler--Mitchell (2012), Theorem 1(ii) and Theorem 5, give **unmarked** labelled and isomorphism-class censuses for all commutative three-nilpotent semigroups. Dolinka--FitzGerald--Mitchell (first public version 2024), Sections 2--3 and 7, develop the partial-partition construction and unmarked orbit analysis. Wang--Yin--Wang (arXiv version of October 1, 2026), Corollary 1.2, proves the complete finite-basis criterion for full power semirings of finite commutative nilpotent semigroups. The present statement combines these two lines of motivation but provides the square-marked enumeration, its isomorphism refinement, and a quantitative conditional density theorem; it does not claim the underlying three-nilpotent presentations, the unmarked totals, or the finite-basis criterion as new.

## Limitations

The result does not enumerate up to equivalence of semiring varieties, does not assert that all non-isomorphic semigroups have non-isomorphic power semirings, and does not address arbitrary noncommutative semigroups or nilpotency index greater than three. The density bound is an explicit upper bound, not a claimed sharp asymptotic equivalent. Bibliographic uncertainty remains concerning equivalent square-marked orbit enumerations in unindexed literature. Independent mathematical review has not been performed.

## References

1. Lili Wang, Qingrui Yin, Aifa Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, arXiv:2610.01329v1, 2026-10-01, especially Corollary 1.2. https://arxiv.org/abs/2610.01329
2. Andreas Distler, J. D. Mitchell, *The Number of Nilpotent Semigroups of Degree 3*, Electronic Journal of Combinatorics 19(2), P51 (2012), Theorems 1 and 5. https://doi.org/10.37236/2441
3. Igor Dolinka, D. G. FitzGerald, James D. Mitchell, *Semirigidity and the enumeration of nilpotent semigroups of index three*, arXiv:2411.00466, initially 2024-11-01, Sections 2, 3, and 7. https://arxiv.org/abs/2411.00466
