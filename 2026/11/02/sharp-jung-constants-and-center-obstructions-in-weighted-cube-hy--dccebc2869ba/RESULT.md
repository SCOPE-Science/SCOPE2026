# Sharp Jung constants and center obstructions in weighted cube hyperplanes

## Finding

Let \(n\ge2\), let \(w=(w_1,\ldots,w_n)\in\mathbb R^n\setminus\{0\}\), and equip the real hyperplane
\[
H_w=\left\{x\in\mathbb R^n:\sum_{i=1}^n w_i x_i=0\right\}
\]
with the inherited maximum norm. Put \(W=\sum_i|w_i|\) and \(\alpha=\max_i|w_i|/W\). For a bounded set \(A\subset H_w\) of positive diameter \(D(A)\), write \(r_{H_w}(A)=\inf_{c\in H_w}\sup_{a\in A}\|a-c\|_\infty\). Define the radius-to-diameter Jung constant, with **no factor of two**, by
\[
J_{\mathrm{rad}}(H_w)=\sup_{A\subset H_w,\,0<D(A)<\infty}\frac{r_{H_w}(A)}{D(A)}.
\]
Then
\[
\boxed{J_{\mathrm{rad}}(H_w)=\max\left\{\frac12,1-\alpha\right\}.}
\]
The supremum is attained by a set of at most \(n\) points for every coefficient vector, including ones with zero entries.

Consequently \(J_{\mathrm{rad}}(H_w)=1/2\) exactly when \(2\max_i|w_i|\ge W\); in that regime the hyperplane is explicitly isometric to \(\ell_\infty^{n-1}\). For \(n\ge3\), \(J_{\mathrm{rad}}(H_w)\le(n-1)/n\), with equality exactly when all \(|w_i|\) are equal and nonzero. For \(n=2\), every such hyperplane has Jung constant \(1/2\).

A stronger setwise result determines the radius and every center. After changing coordinate signs, one can assume the coefficients \(b_i=|w_i|\ge0\). For any nonempty bounded \(A\subset H_b\), set \(M_i=\sup_{a\in A}a_i\), \(m_i=\inf_{a\in A}a_i\), and \(D=\max_i(M_i-m_i)\). Then
\[
\boxed{r_{H_b}(A)=\max\left\{\frac D2,\frac{\sum_i b_i M_i}{W},-\frac{\sum_i b_i m_i}{W}\right\}.}
\]
The complete set of optimal centers is the intersection of \(H_b\) with the coordinate box \(\prod_i[M_i-r_{H_b}(A),\,m_i+r_{H_b}(A)]\).

## Assumptions and scope

All scalars, coefficients, and coordinates are real. The norm is \(\|x\|_\infty=\max_i|x_i|\), and centers are required to lie in the same hyperplane as the data. Arbitrary nonempty bounded sets are allowed; finite-dimensionality ensures the exact center box is nonempty. A change of signs of coordinates is a linear isometry carrying \(H_w\) onto \(H_b\), so the following proof assumes \(b_i\ge0\) without loss. The positive number \(W\) excludes only the zero functional.

## Proof

**1. Exact finite-dimensional center feasibility.** For any \(r\ge0\), the constraints \(\|a-c\|_\infty\le r\) for all \(a\in A\) are equivalent to the coordinate restrictions
\[
M_i-r\le c_i\le m_i+r\quad(1\le i\le n).
\]
These intervals are all nonempty precisely when \(r\ge D/2\). As \(b_i\ge0\), their weighted sums fill the entire interval
\[
\left[\sum_i b_i(M_i-r),\;\sum_i b_i(m_i+r)\right].
\]
Thus some admissible center satisfies \(\sum_i b_ic_i=0\) if and only if, in addition,
\[
r\ge \frac{\sum_i b_iM_i}{W},\qquad
r\ge-\frac{\sum_i b_im_i}{W}.
\]
Taking the least such \(r\) proves the setwise radius formula and, at that radius, the asserted full center set. The derivation uses coordinate extrema rather than finite enumeration, so it applies to every bounded \(A\).

**2. Dimension-free coefficient upper bound.** Fix an index \(j\) with \(b_j=\max_i b_i>0\). Choose points \(a^{(k)}\in A\) whose \(j\)-th coordinates tend to \(M_j\). Because \(\sum_i b_i a_i^{(k)}=0\),
\[
\sum_i b_iM_i=\sum_i b_i(M_i-a_i^{(k)})
\le (W-b_j)D+b_j(M_j-a_j^{(k)}).
\]
Letting \(k\to\infty\) gives \(\sum_i b_iM_i\le(W-b_j)D\). Similarly, selecting a sequence of points whose \(j\)-th coordinates tend to \(m_j\), one obtains
\[
-\sum_i b_i m_i=\sum_i b_i(a_i^{(k)}-m_i)\le (W-b_j)D+o(1).
\]
By Step 1,
\[
r_{H_b}(A)\le D\max\{1/2,(W-b_j)/W\}.
\]
This holds simultaneously for every bounded set, giving the claimed upper estimate.

**3. A single sharp witness family.** For the maximizing \(j\) put
\[
q^{(i)}=e_i-\frac{b_i}{b_j}e_j\qquad(i\ne j),\qquad
A_\star=\{0\}\cup\{q^{(i)}:i\ne j\}.
\]
Each vector lies in \(H_b\). As \(0\le b_i/b_j\le1\), pairwise maximum-norm distances within this \(n\)-point set are at most \(1\), and \(\|q^{(i)}\|_\infty=1\). Thus \(D(A_\star)=1\). Its maxima satisfy \(M_j=0\) and \(M_i=1\) for \(i\ne j\), whence
\[
\sum_i b_iM_i=W-b_j.
\]
Step 1 gives \(r_{H_b}(A_\star)\ge(W-b_j)/W\), and every non-singleton metric set also has radius at least half its diameter by the triangle inequality. Together with Step 2 this yields exact equality and finite attainment. Undo the coordinate sign changes for an explicit witness in \(H_w\).

**4. Structural regimes and equality.** If \(b_j\ge W/2\), solving the defining equation for the \(j\)-th coordinate gives
\[
y_j=-\frac1{b_j}\sum_{i\ne j}b_i y_i,
\qquad |y_j|\le\frac{W-b_j}{b_j}\max_{i\ne j}|y_i|\le\max_{i\ne j}|y_i|.
\]
Hence deleting the \(j\)-th coordinate is an onto linear isometry from \(H_b\) to \(\ell_\infty^{n-1}\). The displayed norm formula also shows necessity of this condition for \(J_{\mathrm{rad}}=1/2\).

Finally \(\max_i b_i\ge W/n\). When \(n\ge3\), \((n-1)/n>1/2\), and equality in the resulting Jung upper bound forces \(b_j=W/n\), which holds exactly when every \(b_i=W/n>0\). When \(n=2\), automatically \(b_j\ge W/2\). These observations complete the classification. \(\square\)

## Verification

The exact-arithmetic companion `verification/check_exact.py` checks the center-interval formula, the explicit extremizing sets and the universal coefficient bound on 52,800 cases spanning dimensions 2–9, including zero coefficients. The separate `verification/check_lp.py` computes least-radius centers independently by linear programming with signed coefficients; 1,200 comparisons passed against the closed formula. Reproduce with `python verification/check_exact.py` (standard library) and optionally `python verification/check_lp.py` (SciPy). Tests corroborate the theorem; the proof above establishes all coefficients, dimensions, and bounded sets.

## Relationship to prior work

The classical Jung constant is often normalized as \(2r/D\); in that convention every value reported here must be multiplied by two. Amir (1985) develops the general Jung framework and a broad structural theory. Kobos (arXiv:1411.6214v1) establishes conditions for equality in Bohnenblust's hyperplane **projection** constant; that is a different optimization, over linear retractions onto a hyperplane. The present problem optimizes centers of arbitrary subsets **inside** that hyperplane, and its coefficient-dependent formula does not follow merely by matching the equal-weight extremal value. Veselý (2002) addresses existence of Chebyshev centers in hyperplanes of \(c_0\); the finite-dimensional weighted radius formula is not stated in the inspected relevant theorem. Castillo and Papini (2024) study general finite Jung constants, not the inspected coefficient-specific classification. The inaccessible full text of Franchetti (1977), which relates Jung and projection constants, leaves a possibility of older implicit coverage; no claim of a comprehensive literature exclusion is made.

## Limitations

No claim is made for complex scalars, infinite-dimensional hyperplanes, other ambient norms, general higher-codimensional subspaces or optimal centers under nonlinear constraints. The theorem measures radius over subsets using **centers in the subspace**, not ambient cube centers. Connections to classical projection constants are contextual and do not assert equality of those invariants. The literature comparison is necessarily limited where older full texts could not be obtained.

## References

1. D. Amir, “On Jung's constant and related constants in normed linear spaces,” *Pacific Journal of Mathematics* 118 (1985), 1–19. https://msp.org/pjm/1985/118-1/pjm-v118-n1-p01-s.pdf
2. T. Kobos, “Hyperplanes of finite-dimensional normed spaces with the maximal relative projection constant,” arXiv:1411.6214v1 (23 November 2014); *Bull. Aust. Math. Soc.* 91 (2015), 447–463. https://arxiv.org/abs/1411.6214
3. L. Veselý, “Chebyshev centers in hyperplanes of \(c_0\),” *Czechoslovak Mathematical Journal* 52 (2002), 721–729. http://dml.cz/dmlcz/127758
4. J. M. F. Castillo and P. L. Papini, “The finite Jung constant in Banach spaces,” *Banach J. Math. Anal.* 18 (2024), article 32. https://doi.org/10.1007/s43037-024-00341-1
5. C. Franchetti, “Relationship between the Jung constant and a certain projection constant in Banach spaces,” *Ann. Univ. Ferrara* 23 (1977), 39–44. (Full text not accessed.)
6. J. M. Bayod and M. C. Masa, “Chebyshev coefficients for \(L_1\)-preduals and for spaces with the extension property,” *Publicacions Matemàtiques* 34 (1990), 341–347. (Only indexed introductory material accessed.)
