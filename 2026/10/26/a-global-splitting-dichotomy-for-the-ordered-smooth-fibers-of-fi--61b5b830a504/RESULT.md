# A global splitting dichotomy for the ordered smooth fibers of five Fano quiver-moduli series

## Finding
Let \(X_k^{\boldsymbol n}(Q)\), \(k\geq2\), be any of the five smooth Fano families constructed from framed extended Dynkin quivers by Belmans and Reineke (arXiv:2610.22203v1, Theorem B), with forgetful morphism \(p_k:X_k^{\boldsymbol n}(Q)\to\operatorname{Sym}^k\mathbb P^1\). Write \(t=|Q_0|-2\in\{0,1,2,3\}\), let \(P_t\subset\mathbb P^1\) be the exceptional parameter set of cardinality \(t\), and put
\[
S_t=\mathbb P^1\setminus P_t,\qquad U_k=\{(z_1,\ldots,z_k)\in S_t^k:z_i\ne z_j\text{ for }i\ne j\},\qquad B_k=U_k/\mathfrak S_k.
\]
Then \(U_k\to B_k\subset\operatorname{Sym}^k\mathbb P^1\) is finite étale, and the ordered pullback of \(p_k^{-1}(B_k)\) is a Zariski-locally trivial \((\mathbb P^1)^k\)-bundle. More precisely, for a rank-two bundle \(E\) on \(S_t\), it has the **global** presentation
\[
p_k^{-1}(B_k)\times_{B_k}U_k\ \cong\ \prod_{i=1}^k{}_{U_k}\mathbb P(\operatorname{pr}_i^*E).
\]
The projective-bundle types of \(E\) are exactly:

| Fano family | \(t\) | \(\mathbb P(E)\) over \(S_t\) |
| --- | ---: | --- |
| \(\widetilde A_1(a)\) | 0 | \(\mathbb P(\mathcal O^{\oplus2})\) |
| \(\widetilde A_1(b)\) | 0 | \(\mathbb P(\mathcal O\oplus\mathcal O(1))\) |
| \(\widetilde A_2\) | 1 | \(\mathbb P(\mathcal O_{S_1}^{\oplus2})\) |
| \(\widetilde A_3\) | 2 | \(\mathbb P(\mathcal O_{S_2}^{\oplus2})\) |
| \(\widetilde D_4\) | 3 | \(\mathbb P(\mathcal O_{S_3}^{\oplus2})\) |

Here the displayed identifications can be noncanonical, and \(\mathbb P(E)\) denotes the bundle of one-dimensional quotients (equivalently lines after duality). Consequently, in **four of the five infinite series**, the ordered pullback is the trivial product \(U_k\times(\mathbb P^1)^k\). In the remaining \(\widetilde A_1(b)\) series it is **nontrivial for every \(k\ge2\)**, even after ordering all the distinct stable factors. The intrinsic permutation monodromy of the \(k\) fiber rulings on \(B_k\) is the full symmetric group \(\mathfrak S_k\) in every series.

## Assumptions and scope
Everything is over \(\mathbb C\). The five framings are exactly \(2\boldsymbol j\), \(\boldsymbol i+\boldsymbol j\), \(\boldsymbol j+\boldsymbol k\), \(\boldsymbol j+\boldsymbol k\), and \(\boldsymbol j\), respectively, in Table 1 of the cited paper, with \(\boldsymbol n\cdot\delta=2\). The locus \(B_k\) consists of unordered configurations of pairwise distinct stable representations of indivisible imaginary-root dimension \(\delta\), excluding the \(t\) exceptional regular parameters. No description of singular fibers, special strata, or the entire discriminant is asserted for \(k>2\).

## Proof
**1. Universal framing bundle.** For the stable \(\delta\)-representations over \(S_t\), indivisibility of \(\delta\) allows a universal family \((V_i)_{i\in Q_0}\), up to common line-bundle tensoring. Its rank-two framing bundle is \(E=\bigoplus_i V_i^{\oplus n_i}\), because \(\sum_i n_i\delta_i=2\). The projectivization is independent of the common tensor twist. Distinct stable \(\delta\)-representations \(V_z,V_w\) have no nonzero homomorphisms between them. Since the path algebra is hereditary and \(\langle\delta,\delta\rangle=0\), they also have \(\operatorname{Ext}^1(V_z,V_w)=0\). Thus the underlying representation over \(U_k\) is their direct sum without cross-extension parameters. Frame stability requires a nonzero framing component in every stable summand; quotienting by its scalar automorphism yields exactly \(\prod_i\mathbb P(\operatorname{pr}_i^*E)\). The fiberwise construction commutes with base change and is an isomorphism of relative moduli problems, so it provides the asserted global isomorphism, not merely an equality of geometric fibers.

**2. Triviality in four cases.** For \(t\ge1\), \(S_t\) is an affine line with finitely many points removed; its coordinate ring is a localization of \(\mathbb C[z]\), hence a principal ideal domain. All algebraic vector bundles on \(S_t\) are trivial, so \(E\cong\mathcal O_{S_t}^{\oplus2}\). For \(t=0\) the quiver is the two-arrow Kronecker quiver. Its universal stable \((1,1)\)-representation over \(\mathbb P^1\) has vertex line bundles differing by \(\mathcal O(1)\) (up to common twist and orientation). Framing \(2\boldsymbol j\) uses two copies of the **same** vertex line bundle, so its projectivization is trivial. Framing \(\boldsymbol i+\boldsymbol j\) uses one copy of **each**, so \(\mathbb P(E)\cong\mathbb P(\mathcal O\oplus\mathcal O(1))\), the first Hirzebruch surface over \(\mathbb P^1\).

**3. Integral obstruction in the fifth case.** For \(t=0\), \(U_k=F_k(\mathbb P^1)=(\mathbb P^1)^k\setminus\bigcup_{i<j}\Delta_{ij}\). Restriction of divisor classes from the smooth compactification gives
\[
\operatorname{Pic}(U_k)\cong\mathbb Z^k/\langle e_i+e_j:1\le i<j\le k\rangle.
\]
Here \(e_i\) denotes the restriction of \(\operatorname{pr}_i^*\mathcal O(1)\), since \([\Delta_{ij}]=e_i+e_j\). For \(k=2\) this quotient is \(\mathbb Z\), and \(e_i\) is primitive. For all \(k\ge3\), the relations identify all the \(e_i\) up to a common element of exact order two: \(\operatorname{Pic}(U_k)\cong\mathbb Z/2\mathbb Z\), and each \(e_i\) is its nonzero element. Exactness is seen by mapping every \(e_i\) to \(1\pmod2\). In either case \(e_i\notin2\operatorname{Pic}(U_k)\). If \(\mathbb P(\mathcal O\oplus\operatorname{pr}_i^*\mathcal O(1))\) were a trivial projective-line bundle, its underlying rank-two vector bundle would be \(L^{\oplus2}\) for some line bundle \(L\) (the kernels of \(\mathrm{GL}_2\to\mathrm{PGL}_2\) are scalars). Taking determinants would force \(e_i=2c_1(L)\), impossible. Thus every factor is nontrivial. Any trivialization of their product as a \((\mathbb P^1)^k\)-bundle would induce, after a fixed permutation of the fiber factors on connected \(U_k\), a trivialization of every factor, since \(\operatorname{Aut}((\mathbb P^1)^k)=\mathrm{PGL}_2^k\rtimes\mathfrak S_k\). Hence the whole pulled-back bundle is nontrivial.

**4. Permutation monodromy.** The ordered configuration space \(U_k\) is irreducible and the finite étale cover \(U_k\to B_k\) has deck group \(\mathfrak S_k\). Its descent permutes the distinct summands and the corresponding \(k\) relative rulings. Consequently the action on the fiber-ruling set has full image \(\mathfrak S_k\).

## Verification
The Picard-group presentation was independently reduced to Smith normal form for \(2\le k\le8\), yielding one free generator at \(k=2\) and a single order-two invariant factor at each \(k\ge3\). The universal computation in the proof does not depend on this finite check. A bundled script reconstructs the integer relation matrix and repeats those exact Smith-normal-form checks. The Kronecker vertex-line twist and the distinct-summand extension vanishing are proved independently from the explicit two-arrow universal family and the hereditary Euler identity; the results of the cited paper are used to fix the five families and their forgetful maps.

## Relationship to prior work
Belmans and Reineke, arXiv:2610.22203v1, Theorems A–B and Proposition 11, establish flatness, the general geometric fiber, and a local-quiver description of each Luna-stratum fiber. Proposition 24 gives the \(k=2\) discriminant. Their Section 6.1 also identifies the \(k=1\) Kronecker surfaces as \(\mathbb P^1\times\mathbb P^1\) and the one-point blowup of \(\mathbb P^2\). Those conclusions are prior work, not new results here. The added statement identifies the **global** ordered-cover family for every \(k\ge2\), distinguishes the single genuinely twisted series via a computable Picard obstruction, and determines the full ruling-permutation monodromy. Their earlier arXiv:2607.12895 studies a related \(\widetilde D_4\) fourfold; no priority is asserted for already known individual fourfold fibers or degenerations.

## Limitations
Only the distinct stable-root locus is analyzed; the theorem does not classify the full discriminant, singular fibers, Brauer class over the unordered base, or birational equivalences of the compact Fano varieties. All five fibers are abstractly products of projective lines at a generic point, so the detected obstruction is to **global bundle trivialization**, not to local triviality or geometric rationality. A complete text comparison with the earlier July fourfold paper could not be completed; the related known \(\widetilde D_4\) model may contain an implicit special-case construction. Historical priority of the uniform splitting dichotomy is therefore not independently certified.

## References
1. Pieter Belmans and Markus Reineke, *Series of Fano quiver moduli from extended Dynkin quivers*, arXiv:2610.22203v1, 15 October 2026, https://arxiv.org/html/2610.22203v1 (Theorems A–B, Proposition 11, Proposition 24, Sections 3 and 6).
2. Pieter Belmans and Markus Reineke, *Fano 4-fold quiver moduli from subspace quivers*, arXiv:2607.12895v1, 14 July 2026, https://arxiv.org/abs/2607.12895 (related prior fourfold geometry).
3. The standard divisor-localization exact sequence for smooth varieties and the classical description of the projective-frame automorphism group are used in the proof above.
