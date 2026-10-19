# Exact hexagon-pair phase retrieval for complex cubic polynomials

## Finding
Let \(r,s>0\), \(\phi,\psi\in\mathbb R\), and define the two hexagonal sampling grids
\[
\mathcal Z=\{r e^{i(\phi+j\pi/3)}:0\le j\le5\}\cup\{s e^{i(\psi+j\pi/3)}:0\le j\le5\}.
\]
For every polynomial \(f(z)=a_0+a_1z+a_2z^2+a_3z^3\) with arbitrary complex coefficients, its twelve intensities \(\{|f(z)|^2:z\in\mathcal Z\}\), indexed by sampling point, determine \(f\) up to one common unimodular scalar **if and only if**
\[
r\ne s\qquad\text{and}\qquad\sin(3(\psi-\phi))\ne0.
\]
The failure of either condition produces inequivalent polynomials with identical measurements. Under the stated nondegeneracy assumptions the real-linear kernel of the associated Hermitian measurement map has dimension exactly four, consists solely of matrices of rank at least three apart from zero, and is described explicitly in the proof. All zero and lower-degree signals are included. The result is a complete criterion for this balanced two-ring twelve-point family, not a claim that twelve measurements is the global phase-retrieval minimum for four complex coefficients.

## Assumptions and scope
Coefficient vectors belong to \(\mathbb C^4\); no genericity, nonvanishing, or normalization assumption is imposed on the coefficients. Distinct positive radii and relative angular staggering are the only sufficient geometric requirements. The data comprise labeled magnitudes at the indicated nodes, not an unlabeled multiset. Phase equivalence means \(g=e^{i\theta}f\) for some real \(\theta\). This result concerns exact noiseless injectivity and the algebraic lifting kernel, not a uniform numerical stability estimate or an explicit nonlinear inversion algorithm.

## Proof
Use the Hermitian lift: let \(v(z)=(1,z,z^2,z^3)^T\), and for Hermitian \(H=(h_{jk})_{0\le j,k\le3}\) put \(F_H(z)=v(z)^*Hv(z)\). If two signals have identical intensities, their difference-of-lifts \(H=xx^*-yy^*\) lies in the measurement kernel and has rank at most two. Conversely, injectivity follows if the Hermitian measurement kernel has no nonzero rank-at-most-two member.

Set \(a=r^2\), \(b=s^2\). On a circle \(|z|=R\), write \(z=Re^{i\theta}\). The angular coefficients at harmonic numbers zero through three are, up to harmless conjugation of the indexing convention,
\[
\begin{aligned}
C_0(R)&=h_{00}+R^2h_{11}+R^4h_{22}+R^6h_{33},\\
C_1(R)&=R(h_{01}+R^2h_{12}+R^4h_{23}),\\
C_2(R)&=R^2(h_{02}+R^2h_{13}),\\
C_3(R)&=R^3h_{03}.
\end{aligned}
\]
Here \(C_0\) is real and the negative harmonics are conjugates. Six-point angular Fourier inversion separates the harmonic classes zero, \(\pm1\), and \(\pm2\). It leaves only the Nyquist harmonic \(3\), whose contribution at the first ring is \(2r^3\operatorname{Re}(e^{3i\phi}h_{03})\) and at the second is \(2s^3\operatorname{Re}(e^{3i\psi}h_{03})\).

Suppose \(a\ne b\) and \(\sin(3(\psi-\phi))\ne0\). Vanishing of all twelve sample values forces \(h_{03}=0\) from the nonsingular two-equation Nyquist system. The two equations \(C_2(r)=C_2(s)=0\) yield \(h_{02}=h_{13}=0\). The two equations for \(C_1\) say that the polynomial \(h_{01}+t h_{12}+t^2h_{23}\) vanishes at \(t=a,b\), so
\[
(h_{01},h_{12},h_{23})=c(ab,-(a+b),1),\qquad c\in\mathbb C.
\]
Finally the real cubic \(q(t)=h_{00}+t h_{11}+t^2h_{22}+t^3h_{33}\) vanishes at \(a,b\), hence
\[
q(t)=(t-a)(t-b)(u+vt),\qquad u,v\in\mathbb R.
\]
Conversely, these conditions make all twelve evaluations vanish. Thus the real kernel has precisely four free parameters: \(u,v,\operatorname{Re}c,\operatorname{Im}c\).

If \(c\ne0\), the kernel matrix is Hermitian tridiagonal, with all three neighboring off-diagonal entries nonzero because \(ab>0\) and \(a+b>0\). Each eigenvalue of such a matrix has a one-dimensional eigenspace: in \((H-\lambda I)w=0\), the first coordinate of a nonzero eigenvector cannot vanish, and each subsequent coordinate is uniquely determined by the preceding two through the nonzero off-diagonal coefficients. Consequently its nullity is at most one and its rank at least three.

If \(c=0\), the matrix is diagonal with entries equal to the four real coefficients of \((t-a)(t-b)(u+vt)\). For a nonzero polynomial in this family, at least three of its four coefficients are nonzero: if only two monomials were present, their quotient would force at most one distinct positive nonzero real root (for a binomial \(A t^m+B t^n\), the equation \(t^{m-n}=-B/A\) has at most one positive solution). Yet the polynomial has the two distinct positive roots \(a,b\). Hence the diagonal matrix again has rank at least three. Therefore no nonzero Hermitian kernel element has rank at most two, proving universal phase retrieval.

Necessity is explicit. If \(r=s\), the polynomials \(f(z)=1\) and \(g(z)=(z/r)^3\) have equal moduli at every sampled point but are not phase equivalent. If \(\sin(3(\psi-\phi))=0\), set \(f(z)=1+i e^{-3i\phi}z^3\) and \(g(z)=1-i e^{-3i\phi}z^3\). At both hexagonal grids, \(e^{-3i\phi}z^3\) is real; thus \(|f|=|g|\) at every node, while the coefficient vectors are not phase equivalent. This proves both directions.

## Verification
The included standalone `VERIFY.py` computes the real-linear rank of the twelve-by-sixteen Hermitian measurement map and checks the predicted four-dimensional nullspace at four nondegenerate choices of radii and offsets. It also tests explicit ambiguity witnesses in five degenerate arrangements, verifies annihilation by each of the four proposed kernel generators, and performs deterministic randomized Hermitian kernel experiments. Running `python VERIFY.py` with NumPy prints `VERIFY_OK 1430 comparisons`. The universal conclusion rests on the preceding analytic rank argument, not the finite tests.

## Relationship to prior work
Pohl, Li and Boche (2017), Section IV and Theorem 7, give universal complex-polynomial phase retrieval from a different allocation: seven boundary samples and five inner-circle samples in the cubic case, via inner–outer factorization. Their theorem does not assert phase retrieval for two equally populated regular hexagons, and its conclusion does not imply the precise relative-angle criterion here. Bodmann and Hammen (2013) give a general twelve-vector polynomial evaluation construction based on two intersecting circles rather than concentric staggered hexagons. Huang (2026) supplies a separate lower bound of eleven universal intensity measurements for arbitrary vectors in \(\mathbb C^4\); that theorem concerns global sample count rather than the present structured design. The present theorem settles the exact geometry of this balanced two-ring family by a direct Hermitian rank argument.

## Limitations
No claim of global twelve-sample optimality is made: general eleven-vector phase-retrieval configurations are known. The result is restricted to cubic polynomials and two equal regular six-point angular grids. No uniform noise-condition-number bound or recovery algorithm is supplied. The full texts of some relevant earlier constructions were not accessible in the current literature comparison; possible unindexed equivalent constructions remain an originality risk. The proof applies unchanged when some coefficients vanish, including the zero polynomial.

## References
1. M. Huang, *Phase Retrieval in \(\mathbb C^4\) Requires Exactly Eleven Measurements*, arXiv:2607.27719, first posted 2026-07-30, https://arxiv.org/abs/2607.27719.
2. V. Pohl, N. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, Sampling Theory and Applications (2017), DOI: 10.1109/SAMPTA.2017.8024411, https://doi.org/10.1109/SAMPTA.2017.8024411.
3. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, first posted 2013-02-22, https://arxiv.org/abs/1302.5487.
4. F. Philipp, *Phase Retrieval from 4N-4 Measurements*, arXiv:1403.4769, first posted 2014-03-19, https://arxiv.org/abs/1403.4769.
