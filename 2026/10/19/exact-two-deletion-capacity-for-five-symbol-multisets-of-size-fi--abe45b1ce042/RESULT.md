# Exact two-deletion capacity for five-symbol multisets of size five

## Finding

The exact optimum for two deletions from an unordered multiset of cardinality five on a five-symbol labeled alphabet is
\[
S_5(5,2)=10.
\]
This is equivalent to the nonnegative-integer constant-weight code parameter \(A(5,6,5)=10\), where the coordinates are unbounded nonnegative integers, the coordinate sum is five, and the minimum \(\ell_1\)-distance is six. It does **not** concern ordinary ordered five-letter deletion codes or binary constant-weight codes.

An attaining code consists of the five pure vectors \(5e_i\), for \(i\in\{0,1,2,3,4\}\), and the five cyclic rotations of \((2,2,0,1,0)\).

## Assumptions and scope

Let
\[
X=\bigl\{x=(x_0,\ldots,x_4)\in\mathbb Z_{\geq0}^{5}:\sum_{i=0}^{4}x_i=5\bigr\}.
\]
The coordinate \(x_i\) is the multiplicity of symbol \(i\), not its position in a sequence. For \(x,y\in X\), write
\[
m(x,y)=\sum_{i=0}^{4}\min(x_i,y_i),\qquad d(x,y)=5-m(x,y)=\tfrac12\|x-y\|_1.
\]
Exact two-deletion output sets are disjoint if and only if any two different codewords have \(m(x,y)\leq2\), equivalently \(d(x,y)\geq3\). The ambient space has \(\binom94=126\) vectors. The theorem concerns precisely these parameters; it does not assert a formula at other alphabet sizes, multiset lengths, or deletion radii.

## Proof

**Attainment.** Take the five vectors \(5e_i\) and the cyclic shifts of
\[
(2,2,0,1,0),\ (0,2,2,0,1),\ (1,0,2,2,0),\ (0,1,0,2,2),\ (2,0,1,0,2).
\]
The latter five vectors are distinct and have pairwise intersection multiplicity exactly \(2\). Their individual coordinates never exceed two, so they meet each pure vector in multiplicity at most two. Distinct pure vectors meet in multiplicity zero. Thus this ten-element family corrects two deletions.

**Forbidden-pair cliques.** Call \(K\subseteq X\) a *conflict clique* if \(m(x,y)\geq3\) for any two distinct \(x,y\in K\). A two-deletion-correcting code contains at most one member of each conflict clique. Define the following indexed families, with indices \(i,j\in\{0,\ldots,4\}\):
\[
A_i=\{x\in X:x_i\geq3\},\qquad
B_{ij}=\{x\in X:x_i\geq2,\ x_j\geq1\}\quad (i\ne j).
\]
Each is a conflict clique, since its defining common coordinate multiplicity is at least three. There are five indexed \(A\)-cliques and twenty indexed \(B\)-cliques. Each has fifteen elements: subtract the required multiplicities and distribute the remaining two tokens among five coordinates, giving \(\binom64=15\).

For each ordered pair of distinct indices \((i,j)\), let \(R_{ij}(x)\) be the three coordinates of \(x\) not indexed by \(i,j\), sorted in nonincreasing order. Define \(C_{ij}\subset X\) by requiring \((x_i,x_j;R_{ij}(x))\) to equal one of these six profiles, listed here with their respective numbers of realizations:

| Pattern | \((x_i,x_j;R_{ij}(x))\) | Members |
|---|---|---:|
| I | \((0,1;(2,1,1))\) | 3 |
| II | \((0,2;(1,1,1))\) | 1 |
| III | \((0,2;(2,1,0))\) | 6 |
| IV | \((0,3;(1,1,0))\) | 3 |
| V | \((1,1;(1,1,1))\) | 1 |
| VI | \((1,2;(1,1,0))\) | 3 |

Thus every \(C_{ij}\) has exactly seventeen members. To check it is a conflict clique, consider any two *distinct* vectors in its six cases. The following table gives the minimum possible common multiplicity \(m(x,y)\) for each pair of cases, obtained by the three-coordinate permutations explicitly specified above. A dash means that the case contains just one vector, so no distinct same-case pair exists.

| Case | I | II | III | IV | V | VI |
|---|---:|---:|---:|---:|---:|---:|
| I | 4 | 4 | 3 | 3 | 4 | 3 |
| II | 4 | — | 4 | 4 | 4 | 4 |
| III | 3 | 4 | 3 | 3 | 3 | 3 |
| IV | 3 | 4 | 3 | 4 | 3 | 3 |
| V | 4 | 4 | 3 | 3 | — | 4 |
| VI | 3 | 4 | 3 | 3 | 4 | 4 |

All defined entries are at least three. The enumerated cases have sizes only \(3,1,6,3,1,3\), making the table an exhaustive, short finite proof; the accompanying standard-library program reconstructs all case pairs directly. There are twenty indexed \(C\)-cliques.

**Fractional clique certificate.** For each vector \(x\), let \(a(x)\), \(b(x)\), \(c(x)\) count its memberships in the indexed \(A\)-, \(B\)-, and \(C\)-cliques. All vectors with the same sorted multiplicity type have the same three incidence counts, computed directly from the preceding definitions:

| Sorted multiplicity type | Number of vectors | \(a\) | \(b\) | \(c\) |
|---|---:|---:|---:|---:|
| \((5,0,0,0,0)\) | 5 | 1 | 0 | 0 |
| \((4,1,0,0,0)\) | 20 | 1 | 1 | 0 |
| \((3,2,0,0,0)\) | 20 | 1 | 2 | 0 |
| \((3,1,1,0,0)\) | 30 | 1 | 2 | 2 |
| \((2,2,1,0,0)\) | 30 | 0 | 4 | 4 |
| \((2,1,1,1,0)\) | 20 | 0 | 3 | 7 |
| \((1,1,1,1,1)\) | 1 | 0 | 0 | 20 |

For each row of this complete partition of \(X\), the displayed counts satisfy
\[
a(x)+\frac{3}{16}b(x)+\frac1{16}c(x)\geq1.\]
Assign weight \(1\) to each \(A_i\), weight \(3/16\) to each \(B_{ij}\), and weight \(1/16\) to each \(C_{ij}\). The sum of all forty-five clique weights is
\[
5+20\cdot\frac3{16}+20\cdot\frac1{16}=10.
\]
For any code \(\mathcal D\subset X\) satisfying the required distance condition, each clique contains at most one member of \(\mathcal D\). Therefore,
\[
|\mathcal D|\leq\sum_{x\in\mathcal D}\left(a(x)+\frac{3b(x)+c(x)}{16}\right)
=\sum_K w_K|\mathcal D\cap K|\leq\sum_Kw_K=10.
\]
Combined with the displayed ten-word construction, this proves the claimed exact optimum.

## Verification

Run `python3 verify.py` using Python's standard library. The checker independently generates all \(126\) profiles, constructs all \(45\) indexed cliques from their definitions, checks every pair in every clique for common multiplicity at least three, checks all seven incidence types, verifies each fractional covering inequality as an exact rational comparison, sums the clique weights to ten, and tests all \(45\) pairs among the ten constructed codewords. The output is `VERIFY_OK profiles=126 cliques=45 patterns=7 bound=10 witness=10`.

The upper bound is a finite mathematical certificate: validity follows from the explicitly specified cliques, their complete case table, and the weighted-count argument. The checker verifies the finite case table but does not replace that argument.

## Relationship to prior work

Kreindel, Barouch Essayag, and Zabokritskiy's 2026 work defines \(S_q(n,t)\) and studies the \(t=n-3\) regime with general upper bounds; its Section 4.4 does not give the exact value at \((q,n,t)=(5,5,2)\). Their subsequent work establishes deletion-ball geometry and general volume bounds rather than this particular equality. Chen, Ma, and Zhang investigate the equivalent constant-weight nonnegative-integer \(\ell_1\) formulation and provide exact arbitrary-nonnegative-coordinate results for weights at most four, but this code has weight five. Kovačević and Tan establish the general multiset coding framework and bounds, not the displayed forty-five-clique sharp certificate.

No claim is made that the multiset model, constant-weight metric equivalence, or the established general bounds are new.

## Limitations

This is a single exact finite parameter; it is not a general formula for arbitrary multiset sizes or deletion radii. The proof does not classify all optimal ten-word codes. Finite-case verification is exhaustive for the stated parameter only. An earlier unindexed calculation or alternative formulation of the same equality could exist; the documented literature comparison does not establish absolute novelty. Independent mathematical audit has not yet been performed.

## References

1. A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, version 2 (2026), especially Sections 4.4–5 and Theorem 13.
2. T. Chen, Y. Ma, and X. Zhang, *Optimal Codes with Small Constant Weight in the \(\ell_1\)-Metric*, arXiv:2003.00483, version 2 (2020), especially Sections II–III.
3. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (2016/2018), Sections III–V.
4. A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026), Sections 3–5.
