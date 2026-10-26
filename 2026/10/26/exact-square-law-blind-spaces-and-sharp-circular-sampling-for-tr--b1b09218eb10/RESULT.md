# Exact square-law blind spaces and sharp circular sampling for truncated Hermite characteristic functions

## Finding
Fix an integer \(N\geq 0\), and let \(\mathcal H_N=\operatorname{span}\{|0\rangle,\ldots,|N\rangle\}\) be the first \(N+1\) normalized oscillator Hermite levels. For a Hermitian operator \(\rho\) on \(\mathcal H_N\), define its symmetric Weyl characteristic function
\[
\chi_\rho(z)=\operatorname{Tr}\bigl(\rho D(z)\bigr),\qquad D(z)=\exp(za^\dagger-\overline z a),\qquad z\in\mathbb C,
\]
where \(D(z)\) is the infinite-oscillator displacement operator, restricted in its matrix elements to \(\mathcal H_N\). Let \(r_1,\ldots,r_K>0\) be pairwise distinct radii, with \(K\geq0\). Assume \(\operatorname{Tr}\rho=1\) is known, and observe the complex functions \(\theta\mapsto\chi_\rho(r_j e^{i\theta})\) for all \(j\).

**Exact rank theorem.** On the real vector space of traceless Hermitian perturbations, the real dimension of the blind space is
\[
\boxed{\dim_{\mathbb R}\ker\mathcal M_{N,K}=\bigl(N+1-\min(K,N)\bigr)^2-1.}
\]
It is independent of the numerical values of all the pairwise distinct, positive radii. In particular, every choice of \(N\) distinct positive radii distinguishes all trace-one Hermitian matrices and density matrices, while any \(K<N\) fails even on strictly positive density matrices. The minimal radial sampling count is exactly \(N\) (zero for \(N=0\)).

Each continuous circular trace is a trigonometric polynomial of degree at most \(N\). For \(N\geq1\), its complete content can be recovered from the \(N+1\) complex samples at angles \(\theta_j=\pi j/(N+1)\), \(0\leq j\leq N\), using the relation \(\chi_\rho(-z)=\overline{\chi_\rho(z)}\); and no smaller number of arbitrary complex evaluations can determine every possible circular trace at a prescribed positive radius. Thus \(N(N+1)\) explicitly placed complex evaluations on the \(N\) circles suffice for complete density-matrix recovery. This does not claim global minimality of the total number of point evaluations among other sampling geometries.

## Assumptions and scope
The trace is known exactly, measurements are complex (both real and imaginary components), every selected radius is positive, and repeated radii count only once. The oscillator scale uses the standard annihilation and creation operators satisfying \([a,a^\dagger]=1\). The matrix elements of the full displacement operator are used; exponentiating the finite truncation of \(a\) instead would define a different measurement model. Measurements are noise-free. Positivity is used only to show that every nonzero traceless blind direction produces two genuinely different density matrices, not in the rank calculation.

## Proof
The Weyl factorization
\[
D(z)=e^{-|z|^2/2}e^{za^\dagger}e^{-\overline z a}
\]
gives, for integers \(m\geq0\) and \(0\leq n\leq N-m\),
\[
\langle n+m|D(z)|n\rangle=e^{-|z|^2/2}\sqrt{\frac{n!}{(n+m)!}}\,z^m L_n^{(m)}(|z|^2),
\]
where \(L_n^{(m)}\) is the generalized Laguerre polynomial. The lower triangular matrix entries are determined by \(D(-z)=D(z)^\dagger\). For each positive harmonic index \(m\), the angular Fourier coefficient of \(e^{r^2/2}\chi_\rho(re^{i\theta})\), after division by \(r^m\), is therefore the evaluation at \(x=r^2\) of the polynomial
\[
P_m(x)=\sum_{n=0}^{N-m}\rho_{n,n+m}\sqrt{\frac{n!}{(n+m)!}}L_n^{(m)}(x).
\]
For \(m=0\), the same formula is \(P_0(x)=\sum_{n=0}^N\rho_{nn}L_n(x)\), and \(P_0(0)=\operatorname{Tr}\rho\) because \(L_n(0)=1\). Each family \(L_0^{(m)},\ldots,L_{N-m}^{(m)}\) is a basis of the complex polynomials of degree at most \(N-m\), since its degrees are strictly increasing with nonzero leading coefficients. Hermiticity makes \(P_0\) real and determines the negative angular harmonics from the positive ones by \(\chi(-z)=\overline{\chi(z)}\). Conversely every such collection of real \(P_0\) and complex \(P_m\) arises from a unique Hermitian matrix.

Set \(Q(x)=\prod_{j=1}^K(x-r_j^2)\), with \(Q=1\) for \(K=0\). A traceless Hermitian matrix is invisible on every circle exactly when
\[
P_0(x)=xQ(x)R_0(x),\qquad P_m(x)=Q(x)R_m(x)\quad(1\leq m\leq N),
\]
with the evident interpretation that a polynomial must vanish identically if its degree bound is exceeded. For \(K\leq N\), the allowed real polynomial \(R_0\) has dimension \(N-K\), and the allowed complex \(R_m\) has dimension \(\max(N-m+1-K,0)\). Consequently the real blind dimension is
\[
(N-K)+2\sum_{m=1}^{N}\max(N-m+1-K,0)
=(N-K)(N-K+2)=(N+1-K)^2-1.
\]
For \(K\geq N\), all these polynomials vanish, giving dimension zero. This proves the formula.

A constructive inverse when \(K=N\) follows the same proof. Take the angular Fourier coefficients on each ring, divide out the known nonzero factors \(e^{-r_j^2/2}r_j^m\), interpolate each \(P_m\) from its \(N\) positive nodes (only \(N-m+1\) are required for \(m\ge1\)), and interpolate \(P_0\) from those nodes plus the known value \(P_0(0)=1\). Finally convert from the generalized Laguerre basis back to matrix entries. This is an explicit finite linear algorithm; no positivity-constrained optimization is needed for noiseless exact data.

If \(K<N\), choose any nonzero traceless Hermitian blind matrix \(H\). For \(\varepsilon>0\) sufficiently small, \(\rho_\pm=(N+1)^{-1}I\pm\varepsilon H\) are distinct positive definite density matrices with identical samples. At \(K=N\), the vanishing polynomial argument reconstructs all matrix entries uniquely, so the radial threshold is necessary and sufficient even among positive states.

For the angular assertion, a circular trace has frequencies only \(-N,\ldots,N\). Knowing it at \(N+1\) equally spaced angles on a half-circle and using \(\chi(-z)=\overline{\chi(z)}\) supplies its values on the full equispaced \(2N+2\)-point circle, where discrete Fourier interpolation uniquely determines all the permitted Fourier modes. For \(N\geq1\), the possible circular traces at a fixed positive radius have real affine dimension exactly \(2N+1\): the constant harmonic varies by a traceless diagonal perturbation, and each nonzero harmonic varies independently as one complex parameter. Each complex evaluation contributes at most two real linear observations, so fewer than \(N+1\) evaluations cannot recover every circular trace. This proves sharpness in the stated per-circle sense.

## Verification
The accompanying executable checker \(verify.py\) checks the exact Laguerre evaluation-block ranks in 72 rational-radius cases with cutoffs \(0\leq N\leq7\), constructs two distinct positive states with identical two-circle data at cutoff \(N=3\), compares 45 displacement matrix elements against independent Hermite-function quadrature (largest absolute discrepancy approximately \(5.58\times10^{-16}\)), and checks recovery of a full circular trace from half-circle samples. Reproduce with \(python\ verify.py\), with the dependencies in \(requirements.txt\). All universal statements above follow from the polynomial argument, not from finite numerical experiments.

## Relationship to prior work
Laabs, Eppich, and Weber (2002) reconstruct Hermite–Gaussian modal content from the ambiguity function using a full phase-space decomposition. Li and coauthors (2013) explicitly contrast that global integral with finite-propagation-plane intensity methods; the latter measure different data. Flühmann and Home (2019) measure complex Weyl characteristic-function samples and discuss optimizing measurement locations; their inspected article uses two-dimensional grids rather than proving the exact concentric-circle nullity law. The standard displacement/Laguerre matrix-element identity is not claimed as new. The contribution here is the universal sharp radial threshold, exact square-law nullity for every number of distinct circles, and rigorous finite half-circle angular sampling for this observation model.

## Limitations
No claim is made about optimal noise conditioning, robustness when radii coalesce, loss of phase, errors in trace normalization, infinite Fock cutoffs, or uniqueness from fewer circles for a restricted class of rank-one pure states. Experimental access to the complex characteristic function is assumed, not derived. The closest 2002 modal-decomposition paper could not be inspected beyond its accessible publisher preview because the complete text was not available; an older equivalent finite-ring theorem remains a literature-priority risk. The originality assessment is not independent publication certification.

## References
1. H. Laabs, B. Eppich, H. Weber, *Modal decomposition of partially coherent beams using the ambiguity function*, J. Opt. Soc. Am. A **19** (2002), 497–504, DOI: 10.1364/JOSAA.19.000497; first verified publication 2002-03-01.
2. Y. Li, J. Guo, L. Liu, T. Wang, J. Shao, *Linear equations method for modal decomposition using intensity information*, J. Opt. Soc. Am. A **30** (2013), 2502–2509, DOI: 10.1364/JOSAA.30.002502; accessible publisher preview includes introduction and method contrast.
3. C. Flühmann, J. P. Home, *Direct characteristic-function tomography of quantum states of the trapped-ion motional oscillator*, arXiv:1907.06478 (first posted 2019-07-15); full accessible article at https://arxiv.org/abs/1907.06478.
