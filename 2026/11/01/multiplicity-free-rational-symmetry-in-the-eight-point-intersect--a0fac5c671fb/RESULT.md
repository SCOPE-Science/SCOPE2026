# Multiplicity-free rational symmetry in the eight-point intersecting-triple complex

## Finding

Let \(X\) be the simplicial complex whose vertices are the \(56\) three-element subsets of \([8]\) and whose simplices are collections of pairwise-intersecting triples. Equivalently, \(X=\operatorname{Ind}(\operatorname{KG}(8,3))\) in the conventional notation in which the Kneser graph has ground-set size first. The symmetric group \(\mathfrak S_8\) acts by permuting the ground points. Its complete reduced rational homology representation is

\[
\widetilde H_6(X;\mathbb Q)\cong S^{(8)}\oplus S^{(7,1)}\oplus S^{(5,3)}\oplus S^{(4,4)}\oplus S^{(4,3,1)}\oplus S^{(3,2,2,1)}\oplus S^{(2,2,2,2)}\oplus S^{(2,2,2,1,1)}\oplus S^{(1,1,1,1,1,1,1,1)},
\]

\[
\widetilde H_9(X;\mathbb Q)\cong S^{(3,1,1,1,1,1)}\oplus S^{(2,1,1,1,1,1,1)},
\]

and all other reduced rational homology groups vanish. Here \(S^\lambda\) denotes the irreducible rational Specht module indexed by the partition \(\lambda\) of eight. Both nonzero modules are multiplicity-free, of dimensions \(233\) and \(28\) respectively. In particular, degree six contains exactly one invariant rational class and exactly one copy of the alternating-sign representation, whereas degree nine contains no invariant class.

## Assumptions and scope

The ground set has exactly eight elements. Three-subsets are vertices of the complex, not points of the underlying space. Homology is reduced, with coefficients in \(\mathbb Q\), and the \(\mathfrak S_8\) action is the natural coordinate action. The convention \(\operatorname{KG}(8,3)\) agrees with \(\operatorname{KG}(3,2)\) in Feng's convention, which lists the triple size first and the excess ground points second. The only previously known homological input used is the rational Betti-number theorem for these intersecting-triple complexes: \(\widetilde\beta_6=233\), \(\widetilde\beta_9=28\), and zero elsewhere.

## Proof

**1. Identify the ninth-homology representation.** For any six-subset \(S\subset[8]\), the induced subcomplex on triples contained in \(S\) is the boundary of the ten-dimensional cross-polytope: its twenty triples occur in ten complementary pairs. Write \(z_S\) for its oriented fundamental nine-cycle. Feng and Wang's cross-polytopal-generator theorem proves that the \(\binom86=28\) classes \([z_S]\) are linearly independent: each has a top simplex that is maximal in the full complex, with support exactly \(S\), and that simplex appears in no other \(z_T\). Feng's rational Betti-number theorem gives dimension exactly \(28\), hence they are a basis.

The stabilizer \(\mathfrak S_6\times\mathfrak S_2\) of a particular six-subset acts on its sphere generator through \(\operatorname{sgn}_{\mathfrak S_6}\boxtimes\mathbf1\). To verify the sign, a single transposition of two of the six ground points permutes the ten complementary-pair axes with fifteen inversions and six antipodal flips. Its orientation determinant is therefore \((-1)^{15+6}=-1\). Every transposition has the same sign, so the full stabilizer action is the indicated one-dimensional character. Consequently

\[
\widetilde H_9(X;\mathbb Q)\cong\operatorname{Ind}_{\mathfrak S_6\times\mathfrak S_2}^{\mathfrak S_8}(\operatorname{sgn}_6\boxtimes\mathbf1).
\]

Pieri's rule gives exactly the two stated hook Specht modules. For a permutation \(g\) with cycle lengths \(\mu_1,\ldots,\mu_t\), its character is the coefficient

\[
\chi_9(g)=[u^6]\prod_{j=1}^{t}\bigl(1+(-1)^{\mu_j-1}u^{\mu_j}\bigr).
\]

This follows by choosing stable six-subsets as unions of cycles and weighting each by the sign of the induced permutation on that subset.

**2. Determine the virtual difference using fixed simplices.** Let \(\mathcal T=\binom{[8]}3\). For \(g\in\mathfrak S_8\), partition \(\mathcal T\) into \(g\)-orbits. Discard an orbit if it contains two disjoint triples. Form a conflict graph \(D_g\) on the remaining orbits, joining two orbits whenever a triple in one is disjoint from a triple in the other. A simplex of \(X\) is \(g\)-invariant exactly when it is a union of an independent family of vertices of \(D_g\).

If an invariant simplex is a union of \(j\) triple-orbits containing \(r\) triples in total, the orientation sign of \(g\) on it is \((-1)^{r-j}\), whereas its ordinary Lefschetz degree sign is \((-1)^{r-1}\). Their product is \((-1)^{j-1}\). Including the augmentation term, the reduced Lefschetz number therefore equals

\[
\widetilde L(g)=-I(D_g;-1),\qquad I(D_g;z)=\sum_{J\subseteq V(D_g)\atop J\ \mathrm{independent}}z^{|J|}.
\]

Only degrees six and nine support rational homology, so \(\chi_6(g)-\chi_9(g)=\widetilde L(g)\). This formula involves no undetermined homology matrices.

**3. Exact class calculation and irreducible decomposition.** The executable verifier constructs the \(22\) conjugacy-class representatives of \(\mathfrak S_8\). For every class it constructs the orbits of the \(56\) triples, discards internally conflicting orbits, constructs \(D_g\), and evaluates its independence polynomial at minus one. With any vertex \(v\), the exact recursion is

\[
I(D;-1)=I(D-v;-1)-I(D-N[v];-1),\qquad I(\varnothing;-1)=1.
\]

The resulting reduced Lefschetz values, indexed by cycle type, are:

| Cycle type | Reduced Lefschetz number |
| --- | ---: |
| \((8)\) | -1 |
| \((7,1)\) | 2 |
| \((6,2)\) | 2 |
| \((6,1,1)\) | 2 |
| \((5,3)\) | 1 |
| \((5,2,1)\) | -1 |
| \((5,1,1,1)\) | -5 |
| \((4,4)\) | 1 |
| \((4,3,1)\) | 0 |
| \((4,2,2)\) | -3 |
| \((4,2,1,1)\) | 3 |
| \((4,1,1,1,1)\) | 9 |
| \((3,3,2)\) | -2 |
| \((3,3,1,1)\) | 10 |
| \((3,2,2,1)\) | 2 |
| \((3,2,1,1,1)\) | 4 |
| \((3,1,1,1,1,1)\) | -14 |
| \((2,2,2,2)\) | 5 |
| \((2,2,2,1,1)\) | -1 |
| \((2,2,1,1,1,1)\) | 17 |
| \((2,1,1,1,1,1,1)\) | 19 |
| \((1,1,1,1,1,1,1,1)\) | 205 |

Combining these values with the degree-nine character yields the degree-six character on every class. For each partition \(\lambda\vdash8\), its multiplicity is computed by the exact class inner product

\[
m_\lambda=\sum_{\mu\vdash8}\frac{\chi_6(\mu)\chi^\lambda(\mu)}{z_\mu},\qquad z_\mu=\prod_{j\ge1}j^{m_j}m_j!.
\]

The Specht characters \(\chi^\lambda\) are evaluated by Murnaghan–Nakayama removal of connected border strips. Precisely nine multiplicities equal one, for the nine partitions in the first displayed formula; all remaining multiplicities are zero. The sum of their hook-length dimensions is \(1+7+28+14+70+70+14+28+1=233\). The ninth-degree constituents have dimensions \(21+7=28\), consistent with the independent rank theorem. This completes the rational representation classification.

## Verification

Run `python3 verify.py` with Python 3.10 or newer. It uses only the standard library and independently enumerates all \(22\) conjugacy types, all \(56\) triple-vertices and their orbit-conflict graphs. It checks character-table orthogonality using exact rational arithmetic, the degree-six and degree-nine irreducible multiplicities, both Betti dimensions, and the stabilizer transposition's cross-polytope orientation. All recursion, signs, conjugacy classes, and multiplicity calculations are finite and exhaustive. The input ranks and independence of the six-set sphere classes are established by the cited published theorems, not by the finite verifier.

## Relationship to prior work

Feng and Wang (2024), Theorem 10, construct and prove independence of the embedded cross-polytope nine-dimensional cycles and give lower bounds; they do not identify the degree-six \(\mathfrak S_8\) representation. Feng (2026), Theorem 18, proves rational homology concentration and all Betti numbers for triple Kneser complexes; it does not give an equivariant Specht decomposition. Together these theorems supply the ranks and top-degree basis used here, but not the newly computed degree-six character. The preceding seven-point representation computation applies to a different ground-set size and has no implication fixing the eight-point decomposition. The exact signed Lefschetz enumeration distinguishes this result from nearby stable-Kneser and Kneser-neighborhood complexes, which are different simplicial objects.

## Limitations

This theorem is for the eight-point complex and rational coefficients. It neither proves integral torsion-freeness nor determines homotopy type or the degree-six representation for arbitrary larger ground sets. The finite computations are exact, but independent external mathematical validation has not been performed. Equivalence to an unindexed older calculation remains an originality risk.

## References

1. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394, first publicly submitted 2026-10-12; Theorem 18 and Section 7. https://arxiv.org/abs/2610.17394
2. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first publicly submitted 2024-04-16; Theorem 10 and its proof. https://arxiv.org/abs/2404.10566
3. B. Sagan, *The Symmetric Group*, second edition, Springer, 2001; standard Murnaghan–Nakayama rule, Pieri rule, and Specht orthogonality.
