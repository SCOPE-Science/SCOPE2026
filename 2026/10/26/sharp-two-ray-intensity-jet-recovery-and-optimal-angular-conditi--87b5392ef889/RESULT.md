# Sharp two-ray intensity-jet recovery and optimal angular conditioning for polynomials

## Finding
For every integer \(N\ge1\), exactly \(2N\) real intensity-Taylor coefficients—one coefficient of each order \(1,\ldots,N\) along each of two lines—recover every normalized complex polynomial of degree at most \(N\) whenever their angle avoids a finite set of rational resonances. The resulting map is a real triangular polynomial automorphism with constant Jacobian determinant. Its **best possible local Euclidean conditioning at the constant polynomial** occurs exactly at the primitive angles \(\theta=p\pi/(N+1)\), with sharp smallest singular value
\[
2\sqrt{1-\cos(\pi/(N+1))}.
\]
This quantifies a finite-dimensional effect not implied merely by qualitative uniqueness for entire functions on irrationally separated lines: rational angles can be optimally conditioned for any prescribed finite polynomial degree.

## Assumptions and scope
Fix an integer \(N\ge1\). Write \(a_0=1\) and
\[
p(z)=1+\sum_{j=1}^{N}a_jz^j,\qquad a_j\in\mathbb C.
\]
For each \(\varphi\in\{0,\theta\}\), with \(0<\theta<\pi\), let
\[
I_{k,\varphi}(a)=[t^k]\,|p(te^{i\varphi})|^2,\qquad 1\le k\le N,
\]
where \([t^k]\) denotes the coefficient of a **real-variable** polynomial in \(t\). Set \(\Phi_\theta(a)=(I_{1,0},I_{1,\theta},\ldots,I_{N,0},I_{N,\theta})\in\mathbb R^{2N}\), and give input coefficients the Euclidean norm \(\sum_j|a_j|^2\) and output jets their unweighted Euclidean norm. Here the constant value \(p(0)=1\) fixes the unavoidable global phase and amplitude; no unnormalized-polynomial conclusion is asserted for this \(2N\)-component map.

**Theorem.** The following are equivalent: (i) \(\sin(k\theta)\ne0\) for every \(1\le k\le N\); (ii) \(\Phi_\theta\) is injective; (iii) \(\Phi_\theta\) is a global polynomial bijection with polynomial inverse. Under these conditions its real Jacobian determinant, at every input, is
\[
\det D\Phi_\theta=(-4)^N\prod_{k=1}^{N}\sin(k\theta).
\]
The singular values at \(a=0\) are exactly \(2\sqrt{1\pm|\cos(k\theta)|}\) for \(1\le k\le N\). The largest possible smallest singular value over \(0<\theta<\pi\) is
\[
2\sqrt{1-\cos(\pi/(N+1))},
\]
with **all** maximizing angles precisely \(\theta=p\pi/(N+1)\) for \(1\le p\le N\), \(\gcd(p,N+1)=1\). At every maximizing angle,
\[
|\det D\Phi_\theta|=2^N(N+1).
\]
At a resonant angle, there exist two nonidentical normalized polynomials whose entire intensities agree on both lines.

## Proof
**1. Triangular identity and reconstruction.** For \(1\le k\le N\), expanding the product gives
\[
I_{k,\varphi}=\sum_{j=0}^{k}a_j\overline{a_{k-j}}e^{i(2j-k)\varphi}
=2\operatorname{Re}(a_ke^{ik\varphi})+B_{k,\varphi},
\]
with
\[
B_{k,\varphi}=\sum_{j=1}^{k-1}a_j\overline{a_{k-j}}e^{i(2j-k)\varphi}\in\mathbb R.
\]
Consequently, once the previous coefficients have been recovered, put \(b_0=(I_{k,0}-B_{k,0})/2\) and \(b_\theta=(I_{k,\theta}-B_{k,\theta})/2\). Writing \(a_k=x_k+iy_k\) gives \(x_k=b_0\) and
\[
y_k=\frac{b_0\cos(k\theta)-b_\theta}{\sin(k\theta)}.
\]
This is a polynomial recursion for each fixed nonresonant \(\theta\). It produces a unique preimage of *every* real jet-data vector; the inverse is polynomial (with fixed angle-dependent real constants). Thus (i) implies (iii), and (iii) implies (ii).

If \(\sin(k\theta)=0\) for some \(1\le k\le N\), then \(p_\pm(z)=1\pm iz^k\) satisfy
\[
|p_\pm(t)|^2=|p_\pm(te^{i\theta})|^2=1+t^{2k}\quad(t\in\mathbb R),
\]
yet \(p_+\ne p_-\), proving failure of injectivity, even with all orders of intensity data.

**2. Exact constant Jacobian.** Order inputs in real blocks \((\operatorname{Re}a_k,\operatorname{Im}a_k)\) and outputs as the paired jets above. The derivative is block lower triangular. Its diagonal \(2\times2\) blocks are independent of \(a\):
\[
M_k=2\begin{pmatrix}1&0\\\cos(k\theta)&-\sin(k\theta)\end{pmatrix},\qquad\det M_k=-4\sin(k\theta).
\]
Multiplying these diagonal determinants proves the displayed formula everywhere in coefficient space.

**3. Singular values at the constant polynomial.** At \(a=0\), every lower off-diagonal Jacobian block vanishes because the terms \(B_{k,\varphi}\) are quadratic in coefficients. Thus \(D\Phi_\theta(0)=\bigoplus_{k=1}^{N}M_k\). For each \(k\), the two eigenvalues of \(M_kM_k^{\mathsf T}\) are \(4(1\pm|\cos(k\theta)|)\). Hence
\[
\sigma_{\min}(D\Phi_\theta(0))=2\sqrt{1-\max_{1\le k\le N}|\cos(k\theta)|}.
\]
This statement is local **only at** \(p=1\); for other polynomials, the off-diagonal Jacobian blocks generally affect singular values.

**4. Sharp optimal-angle classification.** Put \(\alpha=\theta/\pi\). On the unit circle \(\mathbb R/\mathbb Z\), consider the \(N+1\) points \(0,\alpha,\ldots,N\alpha\). Some neighboring pair has circular gap at most \(1/(N+1)\). Its difference corresponds to \(k\alpha\) for an integer \(1\le k\le N\), and thus
\[
\min_{1\le k\le N}\|k\alpha\|_{\mathbb R/\mathbb Z}\le\frac1{N+1}.
\]
As \(|\cos(k\theta)|=\cos(\pi\|k\alpha\|_{\mathbb R/\mathbb Z})\), this proves the claimed upper bound. Equality forces all \(N+1\) circular gaps to equal \(1/(N+1)\), so the point set is the uniform \((N+1)\)-grid and \(\alpha=p/(N+1)\) with \(\gcd(p,N+1)=1\). Conversely those primitive fractions generate the uniform grid, giving equality. Finally, the classical sine product can be obtained by taking absolute values in
\[
\prod_{k=1}^{N}(1-e^{2\pi ik/(N+1)})=N+1,
\]
which yields \(\prod_{k=1}^{N}|\sin(kp\pi/(N+1))|=(N+1)/2^N\) for all primitive \(p\). Substitution into the determinant formula gives \(2^N(N+1)\).

## Verification
The attached standalone `checker.py` implements the coefficient formula, the triangular inverse, the exact block singular values, a dense finite angular comparison, and explicit resonant ambiguities. Its deterministic run passed 48,078 checks, including exact-formula numerical comparisons for all \(1\le N\le18\) and an angular grid for \(1\le N\le12\). These finite tests check algebra and normalization only; the statements for every \(N\) and every angle follow from the proof, not from enumeration.

## Relationship to prior work
Perez, arXiv:2009.02061, proves phase uniqueness of general holomorphic functions on two segments meeting at irrational multiples of \(\pi\), using reflected Taylor information. Chalendar–Partington, arXiv:2403.16255, gives a related proof and rational-angle ambiguities. Wellershoff, arXiv:2202.03733, classifies full-line magnitude ambiguities of finite-order entire functions, including rational angles. Liehr, arXiv:2308.05722, studies rigidity and nonuniqueness for arithmetic families of sampling lines. These broader *full-modulus* uniqueness or ambiguity classifications do not state the finite-order **intensity-jet polynomial automorphism**, its constant Jacobian, or the exact optimum and uniqueness classification for its Euclidean local conditioning. They do motivate the angular resonance problem; no novelty is claimed for irrational-angle uniqueness itself or for the classical circular pigeonhole lemma separately.

## Limitations
The source polynomial must have known nonzero value normalized to \(1\) at the intersection. The data consist of exact intensity Taylor coefficients, not finitely many noisy point samples or integrals along rays. Optimality concerns the Euclidean differential at \(p=1\); it does not imply a global uniform inverse-Lipschitz estimate over unbounded coefficient space. The normalization of coefficient jets is part of the problem: other physical noise metrics may favor different angles. Historical-priority review remains incomplete, and independent validation has not been performed.

## References
1. R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061 (first public 2020-09-04).
2. M. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733 (first public 2022-02-08).
3. L. Liehr, *Arithmetic Progressions and Holomorphic Phase Retrieval*, arXiv:2308.05722 (first public 2023-08-10).
4. I. Chalendar and J. R. Partington, *Phase Retrieval on Circles and Lines*, arXiv:2403.16255 (first public 2024-03-24).
