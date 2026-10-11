# Sharp finite convexification thresholds for every skeleton of a simplex

## Finding

Let \(\Delta=\operatorname{conv}\{v_0,\ldots,v_d\}\subset\mathbb R^d\) be any nondegenerate simplex with integer \(d\ge2\). For integer \(1\le r<d\), its closed \(r\)-skeleton \(S_r\) is the union of all faces spanned by at most \(r+1\) vertices. For every positive integer \(k\), define the equal-weight Minkowski average

\[
M_k(S_r)=\left\{\frac{x_1+\cdots+x_k}{k}:x_1,\ldots,x_k\in S_r\right\}.
\]

**Theorem (complete sharp phase diagram).** For all such \(d,r,k\),

\[
M_k(S_r)=\Delta\quad\Longleftrightarrow\quad kr\ge d.
\]

In particular, the least number of summands is exactly \(\lceil d/r\rceil\). The statement is affine invariant; it is valid for every simplex shape, without general-position restrictions beyond affine independence of its vertices. Below threshold the failure occurs at points arbitrarily close to every vertex, even with all barycentric coordinates strictly positive.

## Assumptions and scope

A point belongs to \(S_r\) precisely when its unique nonnegative barycentric vector has at most \(r+1\) nonzero coordinates. Minkowski averages use **exactly** \(k\) summands, each in the same fixed skeleton, with equal coefficient \(1/k\). Faces and their boundaries are included. There is no rationality assumption on barycentric coordinates. The vertices of \(\Delta\) are affinely independent; dimensions \(d\ge2\), skeleton orders \(1\le r\le d-1\), and positive integer \(k\) are quantified universally.

## Proof

**Lemma (exact sparse splitting).** Let integers \(k\ge1\) and \(r\ge1\) be given. Suppose \(m\le kr+1\) and nonnegative real numbers \(w_1,\ldots,w_m\) satisfy \(\sum_iw_i=k\). There exist \(k\) nonnegative vectors \(z^{(1)},\ldots,z^{(k)}\), each with coordinate sum one and support cardinality at most \(r+1\), such that \(\sum_{t=1}^k z^{(t)}_i=w_i\) for every \(i\).

*Proof of lemma.* Pad the list with zeros to exactly \(kr+1\) entries and induct on \(k\). The case \(k=1\) is immediate: there are \(r+1\) entries summing to one. For \(k\ge2\), arrange entries in nonincreasing order \(a_1\ge\cdots\ge a_{kr+1}\ge0\). The final block of \(r\) entries sums to at most \(rk/(kr+1)<1\); hence some consecutive block of \(r\) entries has sum at most one. Let \(i\) be the *first* starting position with

\[
S=a_i+\cdots+a_{i+r-1}\le1.
\]

If \(i>1\), the preceding length-\(r\) block has sum strictly greater than one, and therefore \(S+a_{i-1}>1\); choose the extra entry \(a_j=a_{i-1}\). If \(i=1\), the \(r+1\) largest entries sum at least \((r+1)k/(kr+1)>1\), because \(k>1\); choose \(j=r+1\). In both cases \(j\) lies outside the block and \(a_j\ge1-S\). Define one probability row by taking all \(r\) entries in this block in full and the mass \(1-S\) from entry \(j\), and zero elsewhere. It sums to one, is supported on at most \(r+1\) entries, and does not exceed the available coordinate masses. Delete the \(r\) now-exhausted positions and reduce entry \(j\) by \(1-S\). The remaining \((k-1)r+1\) nonnegative entries sum to \(k-1\). The induction hypothesis applies. Undoing permutations and discarding the padded zero positions gives the stated decomposition. \(\square\)

**Sufficiency.** Take any \(x\in\Delta\) with barycentric coordinates \(\lambda_0,\ldots,\lambda_d\ge0\), \(\sum_i\lambda_i=1\). Assume \(kr\ge d\), so \(d+1\le kr+1\). Apply the lemma to \(w_i=k\lambda_i\) with \(m=d+1\). For each resulting probability row, let \(x_t=\sum_i z_i^{(t)}v_i\). Its support contains at most \(r+1\) vertices, hence \(x_t\in S_r\); and \(\frac1k\sum_t x_t=x\). Therefore \(\Delta\subseteq M_k(S_r)\). The opposite inclusion follows from the convexity of \(\Delta\).

**Necessity.** Suppose \(kr<d\). Choose \(0<\varepsilon<1/k\) and the interior point with barycentric coordinates

\[
(1-\varepsilon,\varepsilon/d,\ldots,\varepsilon/d).
\]

If it were the average of \(k\) points in \(S_r\), the sum of all \(k\) summands' barycentric masses outside vertex \(v_0\) would equal \(k\varepsilon<1\). Consequently no summand can have zero barycentric mass at \(v_0\): such a summand would contribute exactly one to that sum. Each summand therefore has positive mass at \(v_0\) and at no more than \(r\) other vertices. Across all \(k\) summands, at most \(kr<d\) of the other \(d\) coordinates could be positive, contradicting that every one equals \(\varepsilon/d>0\) in the target sum. Thus \(M_k(S_r)\ne\Delta\), and sending \(\varepsilon\downarrow0\) gives witnesses arbitrarily close to \(v_0\). \(\square\)

## Verification

The self-contained accompanying `verify.py` implements the lemma with exact rational arithmetic and checks every row's unit mass, support bound, coordinate-wise reconstruction, and the sharpness witness inequalities. Run from the extracted package's directory with `python verify.py`; its deterministic seeded suite reports `VERIFY_OK 4410 exact rational decompositions; sharpness inequalities checked`. The tests cover dimensions \(2\) through \(21\), all allowed skeleton dimensions, and three values of \(k\) at or above the sharp threshold. This finite test is supplementary: the induction and barycentric contradiction supply the all-dimensional proof.

## Relationship to prior work

Fradelizi, Madiman, Marsiglietti, and Zvavitch initiated systematic study of equal-weight Minkowski averages, proving rates and monotonicity statements for several measures of nonconvexity, including eventual Hausdorff-distance decay. Their general theorems do not themselves assert an exact finite threshold for a specified simplex skeleton. Their extended treatment likewise studies Hausdorff nonconvexity and volume deficit, rather than the present all-point exact skeleton decomposition. Here the objective is exact equality of sets, not an asymptotic distance bound or a volume-monotonicity assertion.

The classical Shapley–Folkman–Starr convergence theorem assures Hausdorff convergence for compact sets, but gives no finite equality threshold for this particular family. The statement is also distinct from geometric Minkowski sums of *convex* faces, whose face-count descriptions have a different domain: here each summand ranges over a **nonconvex union of faces**. The sharpness uses a near-vertex all-positive barycentric target, not a volume estimate. A later sharp Hausdorff threshold theorem, arXiv:2606.10815v1, establishes positive contraction at a dimension-dependent step for arbitrary compact sets; its accessible abstract does not state exact equality for simplex skeleta, and its inaccessible full text is an acknowledged historical-overlap risk.

## Limitations

The theorem concerns skeleta of genuine simplices, not arbitrary polytopal complexes or arbitrary compact sets. Its exact finite saturation does not establish general monotonicity of volume deficit or Hausdorff distance for Minkowski averages. The algebraic splitting lemma is proven here, but equivalent classical formulations in sparse transport or finite convexification may exist; no exhaustive historical originality guarantee is claimed. The supplementary finite verifier does not constitute independent certification.

## References

1. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *Do Minkowski averages get progressively more convex?*, arXiv:1512.03718v1, first publicly posted 2015-12-05. https://arxiv.org/abs/1512.03718 .
2. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486v3 (later comprehensive treatment). https://arxiv.org/abs/1704.05486 .
3. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1 (2026). Abstract consulted; full text unavailable. https://arxiv.org/abs/2606.10815 .
4. Komei Fukuda, Christophe Weibel, *f-Vectors of Minkowski Additions of Convex Polytopes*, Discrete & Computational Geometry 37 (2007), 503–516, DOI:10.1007/s00454-007-1310-2. Distinguished by convex summand assumption.
