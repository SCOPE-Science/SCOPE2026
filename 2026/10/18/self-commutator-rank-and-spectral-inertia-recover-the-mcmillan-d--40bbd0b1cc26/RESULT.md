# Self-commutator rank and spectral inertia recover the McMillan degree of stable causal convolution

## Finding
For every minimal real scalar state-space realization of dimension \(d\ge1\) with a Hurwitz matrix, the finite-interval causal convolution operator has a self-commutator of **rank exactly \(2d\)** and **inertia exactly \((d,d)\)**. Its \(d\) positive eigenvalues are computed from one \(d\)-by-\(d\) positive-definite matrix formed from controllability and parity-resolved observability Gramians; its \(d\) negative eigenvalues are their opposites. This includes repeated poles and damped oscillatory kernels, not only sums of distinct real exponentials.

More precisely, let \(A\in\mathbb R^{d\times d}\), \(b,c\in\mathbb R^d\), with \(\operatorname{Re}\sigma(A)<0\), \((A,b)\) controllable and \((c^{\mathsf T},A)\) observable. Put
\[
 k(t)=c^{\mathsf T}e^{At}b,\qquad (Tf)(x)=\int_0^x k(x-y)f(y)\,dy
\]
on \(L^2(0,1;\mathbb C)\), and \(K=TT^*-T^*T\). Define the positive controllability Gramian
\[
 P=\int_0^\infty e^{At}bb^{\mathsf T}e^{A^{\mathsf T}t}\,dt,
\]
the map \((Uv)(x)=c^{\mathsf T}e^{Ax}v\), reflection \((Rf)(x)=f(1-x)\), and \(G=U^*U\), \(H=U^*RU\). Then the symmetric matrices \(G+H\) and \(G-H\) are positive definite. Write
\[
 B=(G+H)^{1/2}P(G-H)P(G+H)^{1/2}.
\]
If \(\eta_1,\ldots,\eta_d\) are the strictly positive eigenvalues of \(B\), counted with multiplicity, **the entire nonzero spectrum** of \(K\) is
\[
 \sigma(K)\setminus\{0\}=\{+\sqrt{\eta_j},-\sqrt{\eta_j}:1\le j\le d\},
\]
with multiplicities. In particular \(\operatorname{tr}K=0\), neither \(T\) nor \(T^*\) is hyponormal, and
\[
 \|K\|_{\mathcal S_1}=2\operatorname{tr}(B^{1/2}),\qquad
 \prod_{j=1}^d\sqrt{\eta_j}=\det(P)\sqrt{\det(G+H)\det(G-H)}.
\]

## Assumptions and scope
The scalar kernel is real-valued, with **a minimal realization** \((A,b,c^{\mathsf T})\) of dimension \(d\) and strictly stable poles. Minimality means exactly the rank-\(d\) Kalman controllability and observability tests. The Hilbert space is complex \(L^2(0,1)\); a real kernel acts complex-linearly. No positivity of \(k\) is assumed. The result is not a classification of arbitrary \(L^2\) convolution kernels, unstable realizations, or multichannel input/output systems. The finite interval can equivalently be any positive length by rescaling the integrals.

The degree \(d\) is the McMillan degree of the strictly proper transfer function \(c^{\mathsf T}(sI-A)^{-1}b\). Therefore the operator-theoretic rank invariant \(\operatorname{rank}(TT^*-T^*T)/2\) retrieves that degree exactly under the stated assumptions.

## Proof
**1. Exact kernel cancellation.** Stability yields the unique symmetric positive definite solution \(P\) of the Lyapunov equation \(AP+PA^{\mathsf T}=-bb^{\mathsf T}\). Set \(W(t)=\int_0^t e^{As}bb^{\mathsf T}e^{A^{\mathsf T}s}\,ds=P-e^{At}Pe^{A^{\mathsf T}t}\). For \(x\ge y\), direct integration gives
\[
 (TT^*)(x,y)=c^{\mathsf T}e^{A(x-y)}W(y)c,
 \quad (T^*T)(x,y)=c^{\mathsf T}W(1-x)e^{A^{\mathsf T}(x-y)}c.
\]
The terms containing \(P\) cancel because they are equal real scalars. The other terms give, by symmetry for all \(x,y\),
\[
 K(x,y)=c^{\mathsf T}e^{A(1-x)}Pe^{A^{\mathsf T}(1-y)}c
 -c^{\mathsf T}e^{Ax}Pe^{A^{\mathsf T}y}c.
\]
Hence \(K=RUPU^*R-UPU^*\). This identity is an equality of Hilbert--Schmidt kernels and bounded integral operators, not merely a formal calculation.

**2. Rank and inertia without genericity assumptions.** Controllability implies \(P>0\). Observability implies \(U:\mathbb C^d\to L^2(0,1)\) is injective: if \(Uv=0\), analyticity gives \(c^{\mathsf T}A^jv=0\) for \(0\le j<d\), hence \(v=0\). The ranges of \(U\) and \(RU\) intersect trivially. Indeed, every \(Uv\) solves \(p(D)f=0\) with \(p(z)=\det(zI-A)\), while every \(RUv\) solves \(p(-D)f=0\). The polynomials \(p(z)\) and \(p(-z)\) are coprime because all roots of \(p\) have strictly negative real part. Bezout's identity for differential operators implies a common solution must vanish. Thus \([RU,U]\) has full column rank \(2d\). The displayed factorization is a congruence of \(\operatorname{diag}(P,-P)\) by a full-column-rank map. Sylvester's inertia law on its finite-dimensional range gives exactly \(d\) positive and \(d\) negative eigenvalues and rank \(2d\).

**3. Parity reduction and complete nonzero spectrum.** The reflection satisfies \(RKR=-K\). Define \(U_+=(U+RU)/\sqrt2\) and \(U_-=(U-RU)/\sqrt2\). Their ranges lie in the orthogonal even and odd reflection subspaces. By the preceding intersection argument, both are injective. Their Gramians are
\[
 U_+^*U_+=G+H,\qquad U_-^*U_-=G-H,
\]
and therefore strictly positive. Expanding the factors gives
\[
 K=-U_+PU_-^*-U_-PU_+^*.
\]
After orthonormalizing the two finite-dimensional parity subspaces, the only nonzero block is \(-(G+H)^{1/2}P(G-H)^{1/2}\) and its adjoint. Its singular values are the positive eigenvalues \(\sqrt{\eta_j}\) above. The symmetry, trace-norm, and product formula follow by linear algebra. The zero eigenspace is infinite dimensional because \(K\) has finite rank in infinite-dimensional \(L^2\).

**4. Single-pole illustration and zero-decay boundary.** For \(k(t)=\gamma e^{-at}\) with \(a>0\) and nonzero real \(\gamma\), \(d=1\), and the two eigenvalues are exactly
\[
 \pm\frac{\gamma^2e^{-a}}{2a}
 \sqrt{\left(\frac{\sinh a}{a}\right)^2-1}.
\]
As \(a\downarrow0\), they tend to \(\pm\gamma^2/(2\sqrt3)\), matching the classical Volterra self-commutator \(\gamma^2(x+y-1)\). The limit is explanatory; the theorem assumes \(a>0\).

## Verification
The standalone `check.py` computes four minimal stable examples: a single real pole, distinct real poles, a repeated real pole with a Jordan block, and a real realization of a conjugate pole pair. It checks the Lyapunov equation, minimality, pointwise integral-kernel identity against independent scalar quadratures, positivity of the parity Gramians, finite-section rank/inertia and eigenvalue symmetry, and the reduced determinant identity. It separately approximates the original triangular convolution and checks convergence to the finite-rank kernel. All four examples passed. Numerical finite sections support the formulas but are not relied upon to establish the infinite-dimensional result. Dependencies: Python, NumPy, SciPy. Run `python check.py` from the directory containing this file.

## Relationship to prior work
Potts (2012 thesis, publicly deposited 2013-05-20) studies cyclicity, convolution powers and the commutant of Volterra convolution operators; the accessible thesis does not supply the self-commutator inertia or McMillan-degree formula. Andersson and Carlsson (2015) study finite-rank truncated correlation and convolution operators; the full accessible companion arXiv paper `1506.05566` states their exponential-polynomial rank characterization. Here \(T\) itself is generally infinite rank and the claim concerns \(TT^*-T^*T\), its signed eigenvalues and its finite-horizon controllability/observability reduction. Classical finite-rank Hankel and system-Gramian facts supply tools but do not, in the inspected material, state this combined invariant and spectral identity. No general historical priority guarantee is asserted.

## Limitations
The proof needs a Hurwitz **minimal real scalar** realization; it does not cover arbitrary unstable systems, discrete-time kernels, matrix-valued kernels, or a converse from finite commutator rank to rationality of an arbitrary impulse response. The exact eigenvalues are given by a positive \(d\)-dimensional Gram matrix, not elementary scalar closed forms for arbitrary \(d\). The bibliographic comparison has residual risk, especially the complete text of Andersson--Carlsson's 2015 original paper, which was inaccessible through available institutional access; its accessible author companion was reviewed instead. Independent validation has not been performed.

## References
- T. Potts, *Properties of Convolution Operators on \(L^p(0,1)\)*, University of York PhD thesis (2012), publicly deposited 2013-05-20. https://etheses.whiterose.ac.uk/id/eprint/3917/.
- F. Andersson and M. Carlsson, *On General Domain Truncated Correlation and Convolution Operators with Finite Rank*, Integral Equations and Operator Theory 82 (2015), 339--370. DOI 10.1007/s00020-015-2217-6.
- F. Andersson and M. Carlsson, *On the Kronecker and Carathéodory--Fejér theorems in several variables*, arXiv:1506.05566 (2015); accessible author's companion elaborating the earlier finite-rank results.
- J. A. Ball and A. C. M. Ran, *Optimal Hankel Norm Model Reductions and Wiener--Hopf Factorization I: The Canonical Case*, SIAM Journal on Control and Optimization 25 (1987), 362--382, DOI 10.1137/0325022 (background on rational realizations and Gramians).
