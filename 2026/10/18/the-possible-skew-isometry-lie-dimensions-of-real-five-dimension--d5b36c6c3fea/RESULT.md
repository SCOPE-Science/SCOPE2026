# The possible skew-isometry Lie dimensions of real five-dimensional Banach spaces

## Finding

For a real Banach space \(X\) of dimension five, define its skew-isometry Lie algebra by
\[
\mathcal Z(X)=\{T\in\mathcal L(X):\exp(tT)\in\operatorname{Iso}(X)\text{ for all }t\in\mathbb R\},
\]
where \(\operatorname{Iso}(X)\) is the group of surjective real-linear isometries. The exact attainable set is
\[
\left\{\dim_{\mathbb R}\mathcal Z(X):\dim_{\mathbb R}X=5\right\}=\{0,1,2,3,4,6,10\}.
\]
In particular, dimension five is impossible. The result answers the five-dimensional instance of the possible-Lie-dimensions problem stated in Kadets, Martín and Payá [2, Problem 28] and reiterated in [3, Problem 1.3.7].

## Assumptions and scope

All spaces and operators are **real** and the ambient dimension is exactly five. Lie dimension means real vector-space dimension, not the cardinality or number of components of the isometry group. Finite dimensionality ensures \(\mathcal Z(X)\) is the Lie algebra of a compact matrix group. For an \(\ell_1\)-sum of Euclidean spaces, write
\[
X(d_1,\ldots,d_m)=\left(\bigoplus_{j=1}^{m}\ell_2^{d_j}(\mathbb R)\right)_{\ell_1},
\qquad \|(x_j)_j\|=\sum_j\|x_j\|_2,
\]
with each \(d_j\) a positive integer and \(\sum_jd_j=5\).

## Proof

**Step 1: orthogonal reduction.** The group \(G=\operatorname{Iso}(X)\) is norm-closed and bounded in the finite-dimensional real vector space \(\mathcal L(X)\): a norm-limit of surjective isometries is norm-preserving, hence injective and therefore surjective. Thus \(G\) is compact. Averaging any Euclidean inner product over \(G\) produces a \(G\)-invariant inner product. Relative to an orthonormal basis for it, the identity component \(G^0\) embeds in \(\operatorname{SO}(5)\) and \(\mathcal Z(X)=\operatorname{Lie}(G^0)\) embeds as a **compact** real Lie subalgebra of \(\mathfrak{so}(5)\).

**Step 2: at most two commuting directions.** Every commuting family of real skew-symmetric \(5\times5\) matrices is simultaneously orthogonally block diagonalizable into at most two rotating real planes and a fixed real line. Indeed, complex simultaneous unitary diagonalization of commuting normal matrices, followed by pairing complex-conjugate eigenspaces, gives this real decomposition. On each rotating plane every skew-symmetric matrix acts by one scalar times the standard quarter-turn. Thus every abelian Lie subalgebra of \(\mathfrak{so}(5)\) has real dimension at most two.

**Step 3: exclusion of Lie dimension five.** Suppose \(\dim\mathcal Z(X)=5\), and put \(\mathfrak g=\mathcal Z(X)\). Compact Lie-algebra structure gives a direct sum \(\mathfrak g=\mathfrak z\oplus\mathfrak s\) of its center and a compact semisimple ideal. A compact simple real Lie algebra of dimension at most five is necessarily \(\mathfrak{su}(2)\), of dimension three: in the root-system classification, a rank-one compact simple algebra has dimension three, whereas a rank-at-least-two simple algebra has at least three positive roots and dimension at least eight. Two nonzero compact simple ideals already contribute at least six dimensions. Therefore \(\mathfrak s\) is either zero or \(\mathfrak{su}(2)\). In the first case, \(\mathfrak g\) is a five-dimensional abelian algebra. In the second, \(\mathfrak g\cong\mathfrak{su}(2)\oplus\mathbb R^2\), containing an abelian subalgebra of dimension three (a one-dimensional Cartan subalgebra of \(\mathfrak{su}(2)\) plus the center). Each case contradicts Step 2. Hence \(5\) cannot occur.

**Step 4: exclusion of the larger missing dimensions.** Rosenthal's theorem [1, Theorem 3(a)] says that for a real normed space of dimension \(n\ge2\), if its skew-isometry Lie dimension exceeds \((n-1)(n-2)/2\), the space is Euclidean and its Lie dimension equals \(n(n-1)/2\). Taking \(n=5\), the threshold is six and the Euclidean dimension is ten. Thus \(7\), \(8\), and \(9\) are impossible; \(\dim\mathcal Z(X)\le6\) unless \(\dim\mathcal Z(X)=10\).

**Step 5: every remaining value is attained.** For any composition \((d_1,\ldots,d_m)\) of five, the extreme points of the unit ball of \(X(d_1,\ldots,d_m)\) are precisely the unit vectors supported in exactly one Euclidean summand: support in two summands gives a nontrivial convex decomposition, while strict convexity of each Euclidean unit ball proves the converse. Each sphere of a block of dimension at least two is a connected component of this extreme-point set, and each one-dimensional block contributes two isolated points. A connected family of linear isometries starting at the identity preserves each such component and therefore every Euclidean summand. On the summands the maps are orthogonal, and connectedness fixes orientation. Conversely, independent special-orthogonal block rotations preserve the \(\ell_1\)-sum norm. Consequently
\[
\operatorname{Iso}\big(X(d_1,\ldots,d_m)\big)^0
=\prod_j\operatorname{SO}(d_j),\qquad
\dim\mathcal Z\big(X(d_1,\ldots,d_m)\big)
=\sum_j\frac{d_j(d_j-1)}2.
\]
Here \(\operatorname{SO}(1)\) is the trivial group. The following witnesses exhaust all permissible dimensions:

| Lie dimension | Euclidean block dimensions \((d_j)\) |
| --- | --- |
| \(0\) | \((1,1,1,1,1)\) |
| \(1\) | \((2,1,1,1)\) |
| \(2\) | \((2,2,1)\) |
| \(3\) | \((3,1,1)\) |
| \(4\) | \((3,2)\) |
| \(6\) | \((4,1)\) |
| \(10\) | \((5)\) |

The exclusions and explicit constructions give equality of the claimed sets.

## Verification

The proof separates the only new obstruction, Lie dimension five, from the previously known Rosenthal upper-range obstruction. The commuting-subalgebra bound is verified directly by simultaneous skew-symmetric block diagonalization. The compact-Lie-algebra case split is exhaustive at dimension five by the small-rank root-system dimension bound. Each witness is verified from its extreme-point geometry, not inferred from mere inclusion of rotations; the identity-component equality eliminates possible additional continuous isometries. The seven dimension sums are, respectively, \(0\), \(1\), \(1+1=2\), \(3\), \(3+1=4\), \(6\), and \(10\). There are no numerical experiments, large finite searches, or external computational certificates on which the infinite quantifiers depend.

## Relationship to prior work

Rosenthal [1, Theorem 3] supplies the sharp Hilbertian gap above dimension six and classifies Lie structures through ambient dimension four; the relevant published result does **not** identify all seven realized values in ambient dimension five. Kadets, Martín and Payá [2, Section 5, Problem 28] explicitly pose the five-dimensional classification after stating Rosenthal's theorem, and Martín [3, Section 1.3.1, Problem 1.3.7] repeats it. The missing dimension-five obstruction is supplied here by coupling the maximal abelian dimension two in \(\mathfrak{so}(5)\) with the low-dimensional compact-Lie-algebra decomposition, and sufficiency is established uniformly by the extreme-point geometry of explicit \(\ell_1\)-sums. General compact Lie theory independently constrains possible subgroups of \(\operatorname{SO}(5)\); by itself it does not assert which such subgroup dimensions are attained by full isometry groups of real normed spaces.

## Limitations

This is a complete **dimension spectrum**, not a classification of all norms or all isometry Lie algebras in dimension five. It relies on standard compact Lie-algebra structure and Rosenthal's proven gap theorem. A literature search is not a proof that no later, differently worded treatment exists; independent bibliographic and mathematical audit remains unperformed. The result does not assert an analogous list in other ambient dimensions or over complex scalars.

## References

[1] H. P. Rosenthal, *Functional Hilbertian Sums*, Pacific Journal of Mathematics **124** (1986), 417–467, especially Theorem 3 and the section 'Lie-classification of spaces of low dimension' (pp. 443–445). https://msp.org/pjm/1986/124-2/pjm-v124-n2-p11-p.pdf

[2] V. Kadets, M. Martín and R. Payá, *Recent progress and open questions on the numerical index of Banach spaces*, arXiv:math/0605781v1 (first public posting 31 May 2006), especially Section 5 and Problem 28. https://arxiv.org/abs/math/0605781

[3] M. Martín, *Numerical range of operators, numerical index of Banach spaces, lush spaces, and Slicely Countably Determined Banach spaces*, lecture notes (2009), especially Section 1.3.1 and Problem 1.3.7. https://www.ugr.es/~mmartins/material/2009-india-notes(links).pdf
