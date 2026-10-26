# Sharp \(q\)-numerical annuli and boundary-attainment thresholds for antilinear isometries

## Finding

Let \(H\) be a complex Hilbert space of dimension at least two, with inner product linear in its first variable. Suppose \(A:H\to H\) is conjugate-linear and has a constant nonzero norm on the unit sphere:
\[
\|Ax\|=\sigma\|x\|\quad(x\in H),\qquad \sigma>0.
\]
The map need not be onto. Write \(w(A)=\sup_{\|x\|=1}|\langle Ax,x\rangle|\), \(\alpha=w(A)/\sigma\in[0,1]\), \(\beta=\sqrt{1-\alpha^2}\), \(r=|q|\in[0,1]\), and \(s=\sqrt{1-r^2}\). Define
\[
W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]

**Exact outer radius, all dimensions.** The supremum of \(|z|\) for \(z\in W_q(A)\) is
\[
R=\sigma\begin{cases}1,&0\le r\le\alpha,\\ \alpha r+\beta\sqrt{1-r^2},&\alpha\le r\le1.\end{cases}
\]
Thus there is a sharp norm plateau up to \(r=\alpha\), followed by an explicit angular-decay branch.

**Complete planar classification.** If \(\dim_{\mathbb C}H=2\), the entire range is the closed annulus (including circle- and disk-degenerate cases)
\[
W_q(A)=\{z\in\mathbb C:\ L\le|z|\le R\},\qquad
L=\sigma\max\{0,\beta\sqrt{1-r^2}-\alpha r\}.
\]
Its central hole exists exactly when \(r<\beta\) and closes at the sharp threshold \(r=\beta\). For \(0<\alpha<1\), \(L=\sigma(\beta-r)/\alpha+O((\beta-r)^2)\) as \(r\uparrow\beta\). At \(\alpha=0\), closure instead follows \(L=\sigma\sqrt{1-r^2}\sim\sigma\sqrt{2(1-r)}\) as \(r\uparrow1\). Every \(\alpha\in[0,1]\) occurs for an explicit two-dimensional antiunitary.

**Higher-dimensional closure criterion.** If \(\dim_{\mathbb C}H\ge3\), then
\[
W_q(A)=\{z:|z|<R\}\ \text{or}\ \{z:|z|\le R\}.
\]
Precisely, the second (closed) alternative holds if and only if \(r<\alpha\) or the numerical-radius supremum \(w(A)\) is attained by a unit vector. When \(R=0\), the range is \(\{0\}\), necessarily closed. In particular every finite-dimensional example has a closed disk. A concrete infinite-dimensional antiunitary below exhibits the open-disk alternative for every \(r\ge\alpha\).

## Assumptions and scope

The Hilbert space may be nonseparable; \(A\) is a bounded conjugate-linear scaled isometry, not necessarily an involution or a surjective antiunitary. Complex \(q\) is allowed, and all radii depend only on \(|q|\). The cases \(q=0\), \(|q|=1\), \(w(A)=0\), and \(w(A)=\sigma\) are included. The theorem is not asserted for general antilinear operators lacking the constant-norm condition. The displayed bounds are exact, not estimates.

## Proof

**1. Values of the diagonal overlap.** On any two-dimensional complex subspace, \(x\mapsto\langle Ax,x\rangle\) is conjugate-homogeneous of degree two. After conjugating the coordinates, it is a homogeneous complex quadratic polynomial in two variables, which has a nonzero isotropic vector over \(\mathbb C\); the identically zero polynomial poses no difficulty. Consequently a unit vector \(x_0\) satisfies \(\langle Ax_0,x_0\rangle=0\). The unit sphere of any complex Hilbert space is path connected, and the continuous real map \(x\mapsto|\langle Ax,x\rangle|\) therefore takes every value in \([0,w(A))\), as well as \(w(A)\) exactly when the latter supremum is attained. Note that \(w(A)\le\sigma\).

**2. A universal one-variable envelope.** Fix a unit \(x\), write \(t=|\langle Ax,x\rangle|\), and let \(u\perp x\) have norm one. Every admissible \(y\) can be written as
\[
y=\overline q\,x+s u,
\]
including \(s=0\). Orthogonal decomposition gives \(\|P_{x^\perp}Ax\|=\sqrt{\sigma^2-t^2}\). Cauchy--Schwarz thus yields
\[
|\langle Ax,y\rangle|\le r t+s\sqrt{\sigma^2-t^2}=:f(t).
\]
When the orthogonal component is nonzero, choose \(u\) parallel to that component with the phase aligning the two scalar summands. When it vanishes, the same equality follows immediately. Hence the estimate is pointwise sharp for each \(t\) and every dimension at least two.

The function \(f(t)\) is the scalar product of \((r,s)\) with a point on the radius-\(\sigma\) semicircle; its unconstrained maximum on \([0,\sigma]\) occurs at \(t=r\sigma\) and equals \(\sigma\). If \(r\le\alpha\) this position belongs to the closure of the allowed interval \([0,w(A)]\), and the resulting supremum equals \(\sigma\). If \(r>\alpha\), \(f\) is strictly increasing up to \(w(A)\), so the supremum is \(f(w(A))=\sigma(\alpha r+\beta s)\). This proves the outer formula, with equality at \(r=\alpha\).

**3. The exact inner radius in complex dimension two.** In this dimension \(x^\perp\) is one-dimensional. As the phase of \(u\) varies, the attainable moduli for fixed \(t\) are precisely
\[
\big[\,|r t-s\sqrt{\sigma^2-t^2}|,\ r t+s\sqrt{\sigma^2-t^2}\,\big].
\]
Let \(g(t)=rt-s\sqrt{\sigma^2-t^2}\), which is nondecreasing on \([0,w(A)]\). If \(g(w(A))<0\), the smallest modulus is \(-g(w(A))=\sigma(\beta s-\alpha r)\). Otherwise the unique zero of \(g\) is available (or an endpoint), and the smallest modulus is zero. This gives \(L=\sigma\max\{0,\beta s-\alpha r\}\). The constrained unit-pair space is path connected: for \(s>0\) identify it with the unitary two-frame space, and for \(s=0\) with the unit sphere. A common rotation \((x,y)\mapsto(e^{i\theta}x,e^{i\theta}y)\) preserves \(q\) and rotates \(\langle Ax,y\rangle\) by \(e^{-2i\theta}\). Thus the compact image is rotationally symmetric, connected, and attains both extremal moduli; it is exactly the claimed closed annulus.

The hole inequality \(\beta s>\alpha r\), with nonnegative terms, is equivalent after squaring to \(\beta^2>r^2\). The boundary expansions follow by differentiating \(\beta\sqrt{1-r^2}-\alpha r\); at \(r=\beta\) and \(0<\alpha<1\), the left derivative is \(-1/\alpha\). For realization, take standard coordinate conjugation \(C\) on \(\mathbb C^2\), \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and \(A=(\alpha I+\beta J)C\). The real matrix \(\alpha I+\beta J\) is orthogonal, and \(\langle Ax,x\rangle=\alpha(\overline{x_1}^2+\overline{x_2}^2)\), so \(A\) is antiunitary with \(w(A)=\alpha\).

**4. Higher dimensions and boundary attainment.** Given an isotropic unit vector \(x_0\), choose a unit \(u\perp x_0,Ax_0\), possible when \(\dim_{\mathbb C}H\ge3\). Then \(y=\overline q\,x_0+s u\) yields \(\langle Ax_0,y\rangle=0\). The constraint space of unit pairs is path connected (the Stiefel two-frame space when \(s>0\)), and its image is rotationally symmetric by the preceding phase calculation. Hence every radius strictly below the supremum \(R\) occurs.

To characterize the boundary, first suppose \(r<\alpha\). The maximizing overlap \(t=r\sigma<w(A)\) occurs for an actual unit vector, so \(R\) is attained. For \(r\ge\alpha\), the maximum of \(f(t)\) on the allowed interval is reached only when \(t=w(A)\): at equality \(r=\alpha\) it is the unique maximizer \(t=r\sigma\), and when \(r>\alpha\) the function is strictly increasing on \([0,w(A)]\) (with the endpoint \(r=1\) immediate). Therefore \(R\) is attained exactly if \(w(A)\) is attained. Circular symmetry then includes the entire boundary or excludes it entirely. If \(R=0\), necessarily \(w(A)=0\) and \(r=1\), so this endpoint is attained automatically.

**5. A nonattaining antiunitary example.** Fix \(a\in(0,1)\), choose \(0<a_n<a\) increasing to \(a\), let \(H=\bigoplus_{n\ge1}\mathbb C^2\), and define
\[
A=\bigoplus_{n\ge1}(a_nI+\sqrt{1-a_n^2}\,J)C.
\]
Every block is antiunitary, hence their orthogonal sum is an antiunitary. As computed in step 3, \(w(A|_{\mathbb C^2_n})=a_n\), so \(w(A)=a\). For every unit \(x=(x_n)\),
\[
|\langle Ax,x\rangle|\le\sum_n a_n\|x_n\|^2<a\sum_n\|x_n\|^2=a;
\]
the strict inequality holds because at least one block has nonzero mass. The outer boundary is therefore absent for \(r\ge a\), while for \(r<a\) the maximizing overlap \(t=r\) exists and the closed unit disk is attained. This realizes the infinite-dimensional open/closed transition.

## Verification

Execute `python verification/check.py` with Python 3 and NumPy. It checks rational boundary identities and samples constrained pairs for 30 pairs of \(\alpha\) and \(r\), using ten thousand unit vectors per pair. All sampled values stay inside the proposed annuli, and the observed extrema approach the exact radii within a stated numerical tolerance. This is a finite consistency check, not an infinite-dimensional proof; the argument above proves the exact identities and endpoint statements.

## Relationship to prior work

Majumdar and Müller, arXiv:2610.16823v1 (first public October 12, 2026), Section 6, Proposition 6.2 and Theorem 6.6, established the disk geometry of the antilinear \(q\)-range in dimension at least three. Their Remark 6.7 states the two-dimensional annulus geometry, and Example 6.3 exhibits a special central hole. Those results are the qualitative starting point. They do not give the current explicit two-radius formula in terms of \(w(A)\) and \(\sigma\), the two parameter thresholds, or the sharp higher-dimensional outer-boundary attainment criterion. Kołaczek and Müller (2024) characterized ordinary antilinear numerical-range disks, corresponding to \(r=1\), and do not supply the all-\(q\) annular result. Classical \(q\)-numerical-range papers for complex-linear matrices do not cover the conjugate-linear family. Jia and Liu (2025) provide an ordinary numerical-range characterization; their full text was not accessible for a complete priority check.

## Limitations

This result concerns scaled antilinear isometries only; it does not determine radii for general antilinear operators of nonconstant norm. Dimension two is essential for a positive inner radius. The phase transitions describe geometry, not spectral inclusions or operator-ideal estimates. Publication priority may be affected by unindexed literature or inaccessible older full texts, particularly Jia--Liu (2025), although the accessible abstract discusses ordinary rather than \(q\)-numerical ranges. Independent expert review has not been performed.

## References

1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (public October 12, 2026), Section 6, especially Proposition 6.2, Example 6.3, Theorem 6.6 and Remark 6.7. https://arxiv.org/abs/2610.16823
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96, article 17 (2024), DOI:10.1007/s00020-024-02768-5. https://doi.org/10.1007/s00020-024-02768-5
3. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347 (2025). https://arxiv.org/abs/2508.04347
4. B. Jia and T. Liu, *A characterization of numerical ranges for antilinear operators*, Canadian Mathematical Bulletin (online April 14, 2025), DOI:10.4153/S000843952500044X. https://doi.org/10.4153/S000843952500044X
5. M.-T. Chien and H. Nakazato, *The q-numerical ranges of normal operators*, Linear and Multilinear Algebra 53 (2005), 393--416; complex-linear theory, DOI:10.1080/03081080500156888.
