# Inner-derivation rank polynomials of unicyclic height-two incidence algebras

## Finding
Let \(P\) be a finite connected height-two poset whose undirected comparability graph \(G\) is simple and unicyclic. Its unique cycle has even length \(\ell\ge4\). Set \(m=|E(G)|\) and \(t=m-\ell\). For any finite field \(k=\mathbf F_q\), let \(A=I(P,k)\) be its incidence algebra. For \(a\in A\), write \(\operatorname{ad}_a(x)=ax-xa\), and define the element-indexed rank polynomial
\[
R_{G,q}(z)=\sum_{a\in A}z^{\operatorname{rank}_k(\operatorname{ad}_a)}.
\]
Put \(U_q(z)=1+(q^2-1)z\). Then
\[
\boxed{R_{G,q}(z)=U_q(z)^t\left(U_q(z)^\ell+(q-1)(1-z)^\ell+q(q-1)^\ell z^{\ell-1}(1-z)\right).}
\]
The center of \(A\) consists precisely of its scalar identities. Consequently, the polynomial counting **distinct inner derivations** once each is \(R_{G,q}(z)/q\). In particular, their rank-one multiplicity is
\[
\boxed{[z]\frac{R_{G,q}(z)}q=m(q^2-1)-q(q-1)\ell,}
\]
so the rank spectrum, together with \(m\) and \(q\), recovers the exact length \(\ell\) of the unique cycle. Moreover, the number of ordered commuting pairs of elements of \(A\) is
\[
\boxed{q^m\left((q^2+q-1)^m+(q+1)(q-1)^{\ell+1}(q^2+q-1)^t\right).}
\]
All assertions hold in every characteristic and for every prime power \(q\).

## Assumptions and scope
A height-two poset here consists of two antichains \(L\) and \(H\), with comparabilities only from \(L\) to \(H\); every graph edge \(\{u,v\}\) is identified with exactly one relation \(u<v\), where \(u\in L\) and \(v\in H\). Thus its undirected comparability graph is bipartite. Connectedness and unicyclicity imply \(|V(G)|=|E(G)|=m\). The incidence-algebra basis comprises \(e_{vv}\) for \(v\in V(G)\) and \(e_{uv}\) for \((u,v)\in E(G)\), so \(\dim_k A=2m\). There are no additional transitive relations of length two, and the span of off-diagonal basis units is square-zero. Rank always means rank of an endomorphism of the full \(2m\)-dimensional vector space \(A\), not the rank of the matrix representing \(a\) itself.

## Proof
Write \(a=\sum_v\lambda_v e_{vv}+\sum_{u<v}b_{uv}e_{uv}\) and \(x=\sum_v\xi_v e_{vv}+\sum_{u<v}y_{uv}e_{uv}\). Matrix-unit multiplication in \(I(P,k)\) gives zero diagonal entries of \(\operatorname{ad}_a(x)\) and, for each edge \(u<v\), the exact coefficient
\[
(\operatorname{ad}_a(x))_{uv}=(\lambda_u-\lambda_v)y_{uv}+b_{uv}(\xi_v-\xi_u). \tag{1}
\]
For edges with \(\lambda_u\ne\lambda_v\), the unique variable \(y_{uv}\) makes that output row independent of all other rows. On the remaining edges, those with \(b_{uv}=0\) contribute zero and those with \(b_{uv}\ne0\) form a nonzero-weighted oriented graph-incidence matrix on the diagonal variables \(\xi_v\). Its row rank is the size of any maximal forest of its support: it has one dependence for each independent cycle. This holds over every field, including characteristic two, because the nullspace consists exactly of functions constant on each support component.

The support graph of the latter rows is a subgraph of a unicyclic graph. Except in one circumstance it is a forest: its unique cycle appears only when every cycle vertex has the same value \(\lambda_v\) and each coefficient \(b_{uv}\) on the cycle is nonzero. Therefore, define a *formal active-edge count* by assigning weight \(z\) to an edge whenever either its endpoint labels differ or its labels agree but its off-diagonal coefficient is nonzero. By (1), the true adjoint rank equals this active-edge count except in the exceptional full-cycle situation, when it is exactly one smaller.

For an edge whose two endpoint labels agree, summing over the \(q\) choices of its coefficient gives the weight \(a(z)=1+(q-1)z\); for differing endpoint labels, it gives \(b(z)=qz\). Root each tree attached to the unique cycle. For a fixed label at a parent vertex, summing over the label at each child yields \(a(z)+(q-1)b(z)=U_q(z)\), independently of the parent. All \(t\) tree edges therefore give the common factor \(U_q(z)^t\).

For the \(\ell\)-cycle, the transfer matrix indexed by field elements has diagonal entries \(a(z)\) and off-diagonal entries \(b(z)\). It equals \((a-b)I+bJ\); its eigenvalues over the rational function field in \(z\) are \(a+(q-1)b=U_q(z)\) once and \(a-b=1-z\) with multiplicity \(q-1\). Consequently, the formal active-edge polynomial on the cycle is
\[
\operatorname{tr}(T^\ell)=U_q(z)^\ell+(q-1)(1-z)^\ell. \tag{2}
\]
There are exactly \(q(q-1)^\ell\) cycle label-and-coefficient assignments in the exceptional full-cycle case: choose a common label and a nonzero coefficient on each cycle edge. Their formal weight is \(z^\ell\) but their actual rank contributes \(z^{\ell-1}\). After multiplying by the independent tree factor, the correction is \(q(q-1)^\ell z^{\ell-1}(1-z)U_q(z)^t\). Adding this to (2) proves the boxed rank formula.

If \(\operatorname{ad}_a=0\), equation (1) first forces \(\lambda_u=\lambda_v\) on every edge and then forces \(b_{uv}=0\) on every edge. Connectedness makes all labels equal, hence \(Z(A)=k\,1\), so every distinct inner derivation has exactly \(q\) representatives \(a\). Because \(\ell\ge4\), the correction contributes no linear term. Extracting the coefficient of \(z\) gives \([z]R=q m(q^2-1)-q^2(q-1)\ell\), hence the stated cycle-length recovery.

For fixed \(a\), the centralizer \(\ker\operatorname{ad}_a\) has \(q^{2m-\operatorname{rank}(\operatorname{ad}_a)}\) elements. The number of ordered commuting pairs therefore equals \(q^{2m}R_{G,q}(1/q)\). Substitution and simplification give the final displayed formula.

## Verification
The companion standalone `check_rank.py` constructs matrix-unit multiplication directly, computes \(\operatorname{ad}_a\) for every algebra element, and performs modular Gaussian elimination. The script independently expands the claimed polynomial using integer coefficients. Exhaustive tests pass for the four-cycle with zero or one pendant edge over \(\mathbf F_2\) and \(\mathbf F_3\), and for a four-cycle with a length-two pendant path and a six-cycle over \(\mathbf F_2\). It also checks the zero- and rank-one counts, total number of elements, and the commuting-pair formula in each case. For a four-cycle over \(\mathbf F_2\), the element-indexed ranks \(0,1,2,3,4\) occur with multiplicities \(2,8,60,106,80\); for a six-cycle over \(\mathbf F_2\), the multiplicities are \(2,12,150,520,1230,1454,728\). Run with `python3 check_rank.py`. The all-parameter assertion follows from the proof, not from finite enumeration.

## Relationship to prior work
General decompositions of derivations of incidence algebras, including inner and additive summands, are established in the literature. Krylov and Tuganbaev's *Incidence Rings: Automorphisms and Derivations* (arXiv:2305.02984, first posted 2023-05-04) studies these modules and derives cycle-space dimension formulas (especially Theorem 19.2), but the inspected portions do not provide the rank-by-rank distribution of the individual maps \(\operatorname{ad}_a\). Fornaroli and Khrypchenko's *Skew derivations of incidence algebras* (arXiv:2307.08439, first posted 2023-07-17) characterizes and decomposes skew derivations, including the ordinary case, but likewise does not supply this enumerator in the inspected material. The cycle-space rank used in existing structural descriptions is different from the variable rank of \(\operatorname{ad}_a:A\to A\).

The polynomial's ingredients are elementary graph-incidence rank and a coloring transfer matrix; these standard ingredients are not claimed as new. The asserted contribution is their exact incidence-algebra adjoint-rank refinement for every unicyclic height-two poset, with recovery of the unique cycle length and an exact commuting-pair count.

## Limitations
The theorem concerns *inner* derivations only; it does not classify outer derivations or their ranks. The poset must have height two, be connected, and have a simple unicyclic comparability graph. Graphs with two or more independent cycles require additional dependency bookkeeping. The literature search did not exclude all equivalent formulations under graph-Potts, radical-square-zero algebra, or finite-ring centralizer terminology. Certain related publisher texts were available only as abstracts, so originality beyond the inspected primary full texts remains provisional pending independent review.

## References
1. P. Krylov and A. Tuganbaev, *Incidence Rings: Automorphisms and Derivations*, arXiv:2305.02984 (first public version 2023-05-04), https://arxiv.org/abs/2305.02984.
2. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439 (first public version 2023-07-17), https://arxiv.org/abs/2307.08439.
3. É. Z. Fornaroli and R. E. M. Pezzott, *Additive derivations of incidence algebras*, *Communications in Algebra* 49 (2021), 1816–1828; first published online 2020-12-09, https://doi.org/10.1080/00927872.2020.1854775 (abstract checked; full text unavailable in this review).
4. P. Krylov and A. Tuganbaev, *Derivations of Incidence Algebras*, *Mathematics* 12 (2024), 999, https://doi.org/10.3390/math12070999 (abstract checked; same-topic later exposition).
