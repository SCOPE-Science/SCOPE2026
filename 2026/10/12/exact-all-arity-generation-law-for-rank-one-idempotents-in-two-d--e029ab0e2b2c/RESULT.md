# Exact all-arity generation law for rank-one idempotents in two-dimensional matrix algebras

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), and
\[
\mathcal P_q=\{P\in M_2(k):P^2=P,\ \operatorname{rank}P=1\}.
\]
For each integer \(r\ge1\), the exact number of ordered tuples \((P_1,\ldots,P_r)\in\mathcal P_q^r\) that generate \(M_2(k)\) as a unital \(k\)-algebra is
\[
\boxed{G_r(q)=[q(q+1)]^r-(q+1)(2q)^r+\binom{q+1}{2}2^r.}
\]
A tuple generates the full matrix algebra **if and only if** its projectors have no common invariant one-dimensional \(k\)-subspace. In particular, the smallest possible size of a generating tuple chosen entirely from \(\mathcal P_q\) is three when \(q=2\) and two when \(q>2\). More precisely, \(G_2(2)=0\), \(G_3(2)=48\), and for \(q>2\), \(G_2(q)=q(q+1)(q-1)(q-2)>0\).

## Assumptions and scope
All fields here are finite, of arbitrary characteristic. Algebra generation is **unital** and over the specified ground field: the smallest unital \(k\)-subalgebra containing the given tuple must be the entire \(M_2(k)\). Every projector is nontrivial, i.e. has rank exactly one; the zero and identity idempotents are excluded. Ordered tuples may repeat entries. There is no assertion about matrices of larger size or about tuples with unrestricted ranks. For \(r=0\), the displayed formula is not valid because the empty tuple has no projector whose invariant lines control inclusion-exclusion.

## Proof
Let \(V=k^2\). A rank-one idempotent \(P\) is uniquely specified by an ordered decomposition \(V=L\oplus K\) into distinct one-dimensional subspaces: \(P\) projects to its image \(L\) along its kernel \(K\). These are exactly the two invariant lines of \(P\), because its eigenvalues are the distinct scalars zero and one, even in characteristic two. The projective line \(\mathbb P^1(k)\) contains \(v=q+1\) points, so \(|\mathcal P_q|=v(v-1)=q(q+1)\). In combinatorial terms, its members are **oriented edges** of the complete graph on \(v\) projective points, with the two invariant lines as endpoints.

We next prove the generation criterion, including the case where no pair of the tuple generates. If a line is invariant under all \(P_i\), each \(P_i\) lies in its proper stabilizer subalgebra, so the tuple cannot generate \(M_2(k)\). Conversely, suppose there is no common invariant line. Choose a basis adapted to \(P_1\), so \(P_1=E_{11}\). Write the other projectors as matrices \(Q_i=(q_{ab}^{(i)})\). Since the first coordinate line is not invariant under every projector, there is an index \(i\) with \(q_{21}^{(i)}\ne0\); since the second coordinate line is not invariant under every projector, there is an index \(j\) with \(q_{12}^{(j)}\ne0\). The generated algebra contains
\[
(1-P_1)Q_iP_1=q_{21}^{(i)}E_{21},\qquad P_1Q_j(1-P_1)=q_{12}^{(j)}E_{12}.
\]
It contains \(E_{11}=P_1\) and \(E_{22}=1-P_1\) as well. Division by the two nonzero field scalars therefore yields all four matrix units, proving full generation. The two off-diagonal witnesses need not be the same projector.

Count non-generating ordered \(r\)-tuples using inclusion-exclusion on their **common invariant lines**. There are \(v(v-1)\) choices per tuple entry. For each fixed projective point \(L\), exactly \(2(v-1)\) oriented edges contain \(L\); hence \([2(v-1)]^r\) tuples have \(L\) invariant for every entry. For distinct points \(L,K\), exactly two oriented edges have both as endpoints, giving \(2^r\) tuples. Because \(r\ge1\) and any projector has exactly two invariant lines, no three distinct projective points can all be common invariant lines. Inclusion-exclusion is therefore exact after the two-point term:
\[
\#\{\text{non-generating tuples}\}
=v[2(v-1)]^r-\binom v2 2^r.
\]
Subtracting this expression from \([v(v-1)]^r\) and substituting \(v=q+1\) proves the formula. Its specialization at \(r=2\) factors as \(q(q+1)(q-1)(q-2)\). At \(q=2\) this vanishes but the \(r=3\) formula gives \(48>0\); at every \(q>2\), the \(r=2\) value is positive. One projector never generates a noncommutative algebra, which establishes the asserted minimal tuple sizes.

## Verification
The companion standalone script `verify.py` constructs every rank-one idempotent explicitly from its image/kernel lines, then independently tests whether each tuple generates the whole matrix algebra by closing its linear span under right multiplication by the chosen idempotents. It also tests the common-line criterion without using that criterion to compute the closure. Its finite-field arithmetic includes \(\mathbb F_4\) represented by the irreducible polynomial \(z^2+z+1\) over \(\mathbb F_2\). Run with `python verify.py` (Python 3, standard library only).

Exact exhaustive agreement between the formula, the common-line test and matrix-algebra closure was observed in the following cases, reported as \((q,r;\text{total tuples},\text{generating tuples})\): \((2,1;6,0)\), \((2,2;36,0)\), \((2,3;216,48)\), \((2,4;1296,576)\), \((3,2;144,24)\), \((3,3;1728,912)\), \((4,2;400,120)\), \((4,3;8000,5520)\), \((5,2;900,360)\), \((7,2;3136,1680)\). The test ends with `VERIFY_OK`.

## Relationship to prior work
Petrenko and Sidki's 2005 public preprint studies generation of full matrix rings by pairs of arbitrary matrices, including an algebraic characterization and asymptotic density results. Crestani's 2012 work investigates covering and pairwise generation of matrix rings. Sercombe and Shalev's 2020 preprint gives asymptotic results for randomly generating finite associative algebras, including conditioning on a fixed characteristic polynomial or on rank. Here the characteristic polynomial of each projector is \(t(t-1)\), a highly constrained instance of their fixed-polynomial setting. The result here is an **exact all-arity** probability/count for these specific generators, not a general random-generation estimate or a claim about arbitrary matrix pairs. The projective-edge interpretation also detects the exceptional binary necessity of three idempotent generators. Bibliographic priority for this exact restricted formula has not been independently certified.

## Limitations
The proof establishes the displayed formula over all finite fields and for all positive tuple lengths; the exhaustive computational checks cover only the explicitly named small fields and lengths. The article by Crestani was accessible by abstract/metadata but not in full text during this comparison; an equivalent enumeration there or in other work remains a residual originality risk. The result does not characterize generating tuples of higher-dimensional matrix algebras, tuples containing idempotents of arbitrary ranks, or arbitrary generators of the given characteristic polynomial in larger dimensions.

## References
1. B. V. Petrenko and S. N. Sidki, *On pairs of matrices generating matrix rings and their presentations*, arXiv:math/0512186, first publicly posted 9 December 2005; subsequently *Journal of Algebra* **310** (2007), 15–40. https://arxiv.org/abs/math/0512186
2. E. Crestani, *Sets of Elements that Pairwise Generate a Matrix Ring*, *Communications in Algebra* **40** (2012), 1570–1575. https://doi.org/10.1080/00927872.2010.544275
3. D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115, first publicly posted 2 September 2020; *Journal of the London Mathematical Society* (2024). https://arxiv.org/abs/2009.01115
