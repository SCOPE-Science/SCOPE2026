# Segre-component geometry and exact rank-one Rota–Baxter census for truncated polynomial algebras

## Finding

Let \(k\) be an arbitrary field, \(n\ge4\), and \(A_n=k[t]/(t^n)\). Consider the **reduced algebraic set** \(\mathcal Z_n\subseteq\operatorname{End}_k(A_n)\) of all operators \(R\) with \(\operatorname{rank}R\le1\) obeying the weight-zero Rota–Baxter identity
\[
R(a)R(b)=R(R(a)b+aR(b))\quad\text{for every }a,b\in A_n.
\]
Set \(h=\lceil n/2\rceil\). Then \(\mathcal Z_n\) has exactly \(n-h=\lfloor n/2\rfloor\) geometrically irreducible components, explicitly
\[
\mathcal X_r=\{R:\operatorname{rank}R\le1,\ \operatorname{im}R\subseteq(t^r),\ R((t^r))=0\},\quad h\le r\le n-1.
\]
Each component is a rank-at-most-one determinantal cone in
\(\operatorname{Hom}_k(A_n/(t^r),(t^r))\), of affine dimension \(n-1\). Its projectivization is the Segre variety \(\mathbb P^{r-1}\times\mathbb P^{n-r-1}\). For \(h\le r<s\le n-1\), their intersection is the rank-at-most-one cone in \(\operatorname{Hom}_k(A_n/(t^r),(t^s))\), of dimension \(n-1-(s-r)\). More generally, any nonempty intersection of these components is determined by the smallest and largest indices in the same way.

If \(k=\mathbb F_q\) is an arbitrary finite field, the number of **nonzero** rank-one weight-zero Rota–Baxter operators on \(A_n\) is exactly
\[
\boxed{\lfloor n/2\rfloor q^{n-1}-\frac{q^{\lfloor n/2\rfloor}-1}{q-1}}.
\]
Including the zero operator adds one. The result is characteristic-free, including characteristic two, and holds for all \(n\ge4\) and prime powers \(q\).

## Assumptions and scope

The associative algebra \(A_n\) is unital, commutative and local, with maximal ideal \((t)\). Rank refers to \(k\)-linear rank. The operator variety is considered with its **reduced** algebraic-set structure; no assertion is made about the scheme structure defined by the unreduced Rota–Baxter polynomial equations. For \(0\ne u\in A_n\), \(\nu(u)\) denotes the smallest exponent of \(t\) with nonzero coefficient. Every nonzero rank-one map admits a factorization \(R(a)=\phi(a)u\) with \(u\ne0\) and nonzero \(k\)-linear functional \(\phi\); two such factorizations differ precisely by a scalar rescaling \((u,\phi)\mapsto(cu,c^{-1}\phi)\).

## Proof

**Step 1: the general rank-one criterion.** Substitute \(R(a)=\phi(a)u\) into the defining identity to obtain
\[
\phi(a)\phi(b)u^2=\big(\phi(a)\phi(ub)+\phi(b)\phi(ua)\big)u.
\]
Choose \(a_0\) with \(\phi(a_0)=1\) and put \(a=b=a_0\). This forces \(u^2\in ku\). If \(u\) were a unit, \(u^2=cu\) would force \(u=c\cdot1\), and hence the image would be the scalar line. For a scalar-line rank-one operator \(R(a)=\psi(a)1\), the Rota–Baxter equation reads \(\psi(a)\psi(b)=2\psi(a)\psi(b)\), impossible since \(\psi\ne0\) in any characteristic. Therefore \(u\) is a nonunit and hence nilpotent. From \(u^2\in ku\), nilpotency forces \(u^2=0\).

If \(a\in\ker\phi\), the equation with \(b=a_0\) gives \(\phi(ua)=0\). Thus \(\phi\circ\mu_u\) is a scalar multiple of \(\phi\): \(\phi(ua)=c\phi(a)\). Since multiplication by \(u\) is nilpotent on \(A_n\), the only possible scalar is \(c=0\); consequently \(\phi(uA_n)=0\). Conversely, \(u^2=0\) together with \(\phi(uA_n)=0\) makes both sides of the displayed identity zero. Hence these conditions are necessary and sufficient, with no characteristic hypothesis.

**Step 2: valuation strata.** If \(\nu(u)=r\), then \(uA_n=(t^r)\), and \(u^2=0\) if and only if \(2r\ge n\). Therefore every nonzero solution has \(r\in\{h,\dots,n-1\}\), image contained in \((t^r)\), and functional vanishing on \((t^r)\). Conversely every nonzero rank-one map satisfying the two stated ideal conditions is a solution, since \((t^r)^2=0\) for \(r\ge h\). Thus the reduced solution set is the union of the indicated closed determinantal cones \(\mathcal X_r\).

**Step 3: component structure.** The source \(A_n/(t^r)\) has dimension \(r\) and the target \((t^r)\) has dimension \(n-r\). The affine cone of matrices of rank at most one has dimension \(r+(n-r)-1=n-1\), and is geometrically irreducible because the rank-one locus is the image of a product of affine vector spaces. Projectivizing gives the classical Segre variety. For \(r<s\), simultaneous image containment requires the smaller target \((t^s)\), while annihilation of \((t^r)\) is the stronger kernel condition, giving an \(r\)-by-\((n-s)\) rank-one cone and dimension \(r+(n-s)-1=n-1-(s-r)\). This dimension is strictly below \(n-1\), so none of the cones is contained in another. Each is therefore an irreducible component, with the asserted number and all intersection formulas.

**Step 4: exact finite-field count.** For a fixed allowable valuation \(r\), there are \((q-1)q^{n-r-1}\) choices of \(u\), and \(q^r-1\) nonzero functionals \(\phi\) on \(A_n/(t^r)\). Rescaling gives exactly \(q-1\) representations per distinct nonzero operator. Summing the disjoint valuation strata yields
\[
\sum_{r=h}^{n-1}q^{n-r-1}(q^r-1)
=(n-h)q^{n-1}-\sum_{j=0}^{n-h-1}q^j
=\lfloor n/2\rfloor q^{n-1}-\frac{q^{\lfloor n/2\rfloor}-1}{q-1}.
\]
The valuation of the image generator is intrinsic to an operator, making this sum disjoint. Every claim above follows.

## Verification

The accompanying standalone `verify_rank_one_rb.py` tests the Rota–Baxter identity directly on each ordered pair of polynomial basis elements for **every distinct nonzero rank-one endomorphism** in nine finite configurations: \((q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3)\). The binary, ternary and quadratic-extension-field cases exhaustively cover \(6212\) tested maps, with observed solution counts respectively \(1,3,13,29,2,8,50,3,15\), exactly agreeing with the stated formula (including low-dimensional boundary consistency checks). Reproduce using `python verify_rank_one_rb.py`; it ends with `RANK_ONE_RB_SEGRE_STRATA_OK 9 6212`. These finite checks do not substitute for the characteristic-free proof.

## Relationship to prior work

Guo, Rosenkranz and Zheng's 2014 work on semigroup algebras classifies Rota–Baxter operators for algebras of dimensions two and three, not the growing truncated-power family considered here. Their other 2014 work on ordinary polynomial algebras treats monomial and injective operators, not finite-rank moduli on the quotient algebras \(k[t]/(t^n)\). Yu's monomial-operator classification likewise studies \(k[t]\). More recent work on square-zero truncated polynomial algebras concerns a different family and is not a classification of these rank-one cones for \(n\ge4\). Standard determinantal geometry and the scalar rank-one factorization are used without novelty claims. The new claim concerns their explicit occurrence, intersections and arithmetic census under the Rota–Baxter equations. Publication priority is not certified; an undiscovered general rank-one classification could imply the result.

## Limitations

The conclusion concerns rank **at most one**, with the arithmetic count excluding the zero map. It does not enumerate operators of rank two or greater; it does not identify automorphism-conjugacy classes or the possibly nonreduced defining scheme. The integer bound \(n\ge4\) ensures multiple components; proof and enumeration also provide boundary checks for \(n=2,3\) without attributing independent novelty to them. Neither finite computation nor unsuccessful literature search proves priority or independent validation.

## References

1. L. Guo, M. Rosenkranz and S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702 (first public 2014-02-15), https://arxiv.org/abs/1402.3702.
2. L. Guo, M. Rosenkranz and S. Zheng, *Rota-Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306 (first public 2014-07-20), https://arxiv.org/abs/1407.5306.
3. H. Yu, *Classification of monomial Rota-Baxter operators on k[x]*, arXiv:1503.02606 (2015), https://arxiv.org/abs/1503.02606.
4. *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670 (2026), https://arxiv.org/abs/2605.15670. This last source concerns a square-zero truncation, not the stated general higher-power family.
