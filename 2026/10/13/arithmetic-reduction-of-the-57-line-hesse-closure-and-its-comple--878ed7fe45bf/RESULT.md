# Arithmetic reduction of the 57-line Hesse closure and its complete \(\mathbb F_7\) plane

## Finding

Let \(\epsilon\) satisfy \(\epsilon^2+\epsilon+1=0\). Let \(\mathcal H_{57}\) be the 57-line Hesse closure of Pokora–Roulleau, defined over \(\mathbb Q(\epsilon)\) by the explicit forms in Section 2 of *Construction of free arrangements using point-line operators* (arXiv:2403.20024). The integral coefficients in the accompanying `verify.py` reproduce those 57 forms, with the nine half-integral forms multiplied by two. For each prime \(p\ge5\), reduce the forms using either root of \(T^2+T+1\) in \(\overline{\mathbb F}_p\), and denote the resulting union of lines by \(\mathcal H_{57,p}\). Every reduced arrangement has 57 distinct geometric lines.

If \(n_m(p)\) denotes the number of distinct geometric points on exactly \(m\) of those lines, the **complete** incidence profile for \(p\ge5\) is:

| Prime | \(n_2\) | \(n_3\) | \(n_4\) | \(n_5\) | \(n_8\) | Total points |
|---|---:|---:|---:|---:|---:|---:|
| \(p\notin\{7,13,19\}\) | 252 | 108 | 72 | 0 | 21 | 453 |
| \(p=7\) | 0 | 0 | 0 | 0 | 57 | 57 |
| \(p=13\) | 36 | 0 | 72 | 54 | 21 | 183 |
| \(p=19\) | 36 | 180 | 72 | 0 | 21 | 309 |

All omitted multiplicities vanish. In particular, the intersection lattice equals that in characteristic zero **if and only if** \(p\notin\{7,13,19\}\) among primes \(p\ge5\).

In characteristic seven, the 57 reduced linear forms give **every** line of \(\mathbb P^2(\mathbb F_7)\). Equivalently, up to a nonzero scalar their product is the Moore determinant
\[
\prod_{\ell\in\mathbb P^{2}(\mathbb F_7)^\vee}\ell(X,Y,Z)
\ \doteq\
\det\begin{pmatrix}
X&Y&Z\\ X^7&Y^7&Z^7\\ X^{49}&Y^{49}&Z^{49}
\end{pmatrix}.
\]
Each of the 57 rational points lies on eight lines of the arrangement.

There is also an exact Frobenius spectrum. For \(p\ge5\) outside the three exceptional primes, the numbers of *individual* \(\mathbb F_p\)-rational lines and of \(\mathbb F_p\)-rational geometric intersection points are respectively
\[
(57,453)\quad\text{if }p\equiv1\pmod 3,
\qquad (13,31)\quad\text{if }p\equiv2\pmod 3.
\]
At \(p=7,13,19\) the corresponding pairs are \((57,57)\), \((57,183)\), and \((57,309)\). Thus, outside finitely many primes, the rational intersection-point counts \(453\) and \(31\) each have natural density \(1/2\). These are **intersection points** of a line arrangement, not all rational points on its union.

## Assumptions and scope

The construction fixes the *integral model given by the 57 explicit Section 2 forms*: this is a statement about its specified reductions, not arbitrary integral models of the complex arrangement. The quadratic equation is separable for every prime \(p\ge5\). When \(p\equiv1\pmod3\), either root is in \(\mathbb F_p\); when \(p\equiv2\pmod3\), the two roots belong to \(\mathbb F_{p^2}\). Conjugating the root permutes the 57 defining lines and therefore does not change any displayed histogram. Characteristics two and three are excluded. No characteristic-positive freeness assertion is made.

## Proof

**(1) Exact generic incidence.** Work in the ring \(R=\mathbb Z[\epsilon]/(\epsilon^2+\epsilon+1)\). Represent \(a+b\epsilon\) as \((a,b)\). The 57 forms in `verify.py` are obtained by reading the source's displayed list and clearing the denominators two. Exact pairwise cross products, normalized projectively over \(\mathbb Q(\epsilon)\), give 453 distinct intersections with multiplicity basket \((n_2,n_3,n_4,n_8)=(252,108,72,21)\). The identity
\[
252\binom22+108\binom32+72\binom42+21\binom82=\binom{57}{2}=1596
\]
checks the complete pair partition. The source already proves this characteristic-zero basket; the independent reconstruction fixes the integral arithmetic model used here.

**(2) The exhaustive determinant obstruction.** For every triple of the 57 coefficient rows, compute its determinant \(d=a+b\epsilon\in R\) and its positive integral norm \(N(d)=a^2-ab+b^2\). Among the \(\binom{57}{3}=29260\) triples, exactly 1572 determinants vanish in \(R\). The remaining 27688 have norms at most 171, and the union of the prime supports of those norms is **exactly** \(\{2,3,7,13,19\}\). The certificate enumerates *all* triples, not a sample; trial division of each positive norm supplies an exhaustive factorization. For a prime outside that set, a nonzero determinant cannot vanish in either residue embedding, while every identically vanishing determinant remains zero. Hence the full rank-three matroid, and thus the intersection lattice, is preserved. In particular the lines remain pairwise distinct.

**(3) All exceptional reductions.** At each of \(p=7,13,19\), both roots of the quadratic are in the prime field. Reducing all 57 rows, normalizing by the first nonzero coefficient, and forming all 1596 pairwise intersections gives 57 distinct lines at each prime and precisely the three exceptional baskets stated above. For each, the weighted count \(\sum_m n_m(p)\binom m2=1596\) is checked directly. At \(p=7\), the 57 normalized coefficient rows coincide with the *entire* set
\[
\{(1,a,b):a,b\in\mathbb F_7\}\cup
\{(0,1,a):a\in\mathbb F_7\}\cup\{(0,0,1)\}.
\]
That is the full dual projective plane, with 57 lines and 57 points, eight lines through each point. The Moore determinant vanishes on every rational line and has the same total degree 57, so its nonzero scalar multiple equals the product of the 57 linear forms.

**(4) Arithmetic descent.** Complex conjugation on \(\mathbb Q(\epsilon)\) acts as \(\epsilon\mapsto-1-\epsilon\). Direct projective normalization of the 57 lines finds 13 fixed lines and 22 exchanged pairs. The 453 normalized intersection points contain exactly 31 fixed points; their fixed-point multiplicities are twelve double, six triple, six quadruple and seven eightfold points. For primes outside the determinant support, the reductions of different points cannot collide because the intersection lattice is preserved. Frobenius acts trivially on \(\mathbb Q(\epsilon)\) when \(p\equiv1\pmod3\), and as the nontrivial conjugation when \(p\equiv2\pmod3\); the asserted rational counts follow. The density statement follows from Dirichlet's theorem on primes in the two reduced residue classes modulo three.

## Verification

Run `python3 verify.py` using the Python standard library. It reads its own complete 57-row input, checks the characteristic-zero basket, conjugation fixed counts, every triple determinant norm and its prime support, all exceptional prime embeddings, selected good-prime checks in both splitting classes, and exhaustive equality of the 57 characteristic-seven line normals with all 57 dual-plane points. It prints `VERIFY_OK` only after every assertion succeeds. In particular this is an exhaustive finite verification of a fixed arithmetic family combined with the general determinant and Frobenius arguments above; computations for a few sample primes are not used as proof for all primes.

## Relationship to prior work

Pokora and Roulleau construct \(\mathcal H_{57}\), prove that it is a rigid free complex arrangement, and give its characteristic-zero multiplicity profile and its 57 line equations (Theorem A and Section 2). Their displayed results do **not** assert the reduction-to-\(\mathbb P^2(\mathbb F_7)\) statement, the complete exceptional-prime set, the characteristic-13/19 profiles or the rational Frobenius spectrum. The classical identity of the Moore determinant with the full finite projective-plane line product is not claimed as new; the point is that this particular characteristic-zero rigid arrangement specializes to that product exactly at seven. No assertion is made of priority over inaccessible or unindexed calculations.

## Limitations

The theorem is about the specified integral model, prime characteristics at least five, and the numbers of intersections and rational points; it does not prove freeness of any reduction. The original complex freeness and rigidity are not new. Arithmetic coincidence with a classical full finite plane may have been noticed in unpublished calculations. The displayed finite proof is reproducible by straightforward enumeration but does not itself establish absence from all literature. Independent examination of the computation and bibliography is still outstanding.

## References

1. P. Pokora and X. Roulleau, *Construction of free arrangements using point-line operators*, arXiv:2403.20024, first public 2024-03-29; see Theorem A and Section 2 (57 defining lines).
2. Standard finite-geometry facts: \(\#\mathbb P^2(\mathbb F_q)=q^2+q+1\), and the Moore determinant is the product (up to scalar) of the \(\mathbb F_q\)-rational lines.
