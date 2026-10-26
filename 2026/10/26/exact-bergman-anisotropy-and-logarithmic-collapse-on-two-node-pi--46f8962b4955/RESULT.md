# Exact Bergman anisotropy and logarithmic collapse on two-node Pick bodies

## Finding
For each \(0<\rho<1\), put \(q=\rho^2\) and consider the two-point Nevanlinna–Pick interpolation domain
\[
D_\rho=\left\{(u,v)\in\mathbb D^2:\left|\frac{u-v}{1-\bar u v}\right|<\rho\right\}.
\]
With standard, unnormalized Euclidean volume \(dA(u)dA(v)\), let \(K_\rho\) be its Bergman kernel and \(g_\rho=\partial\bar\partial\log K_\rho(z,z)\) its Bergman metric. Define the positive integrals
\[
J_k(q)=\int_0^1 \frac{t^k(1-t)^2}{(1-qt)^2}\,dt\quad(k=0,1),\qquad
\Lambda(q)=\frac{J_0(q)}{4J_1(q)-J_0(q)}.
\]
**Theorem.** For every \(a\in\mathbb D\), the vectors \(e_+=(1,1)/\sqrt2\) and \(e_-=(1,-1)/\sqrt2\) are mutually orthogonal eigenvectors of \(g_\rho\) at \((a,a)\), with exact eigenvalues
\[
g_\rho((a,a))[e_+]=\frac{2}{(1-|a|^2)^2},\qquad
g_\rho((a,a))[e_-]=\frac{2\Lambda(q)}{(1-|a|^2)^2}.
\]
The diagonal kernel itself is
\[
K_\rho((a,a),(a,a))=\frac{1}{\pi^2qJ_0(q)(1-|a|^2)^4}.
\]
The transverse-to-tangential eigenvalue ratio \(\Lambda(q)\) is strictly decreasing on \((0,1)\), satisfies \(\Lambda(q)>1\), and has two sharp limiting laws:
\[
\Lambda(q)=\frac{10}{3q}+O(1)\quad(q\downarrow0),\qquad
\Lambda(q)=1+4(1-q)\log\frac1{1-q}+O(1-q)\quad(q\uparrow1).
\]
Thus the intrinsic anisotropy of the two-node interpolation domain collapses to the bidisk value with a logarithmic, rather than linear, first-order correction.

## Assumptions and scope
The two source interpolation nodes are distinct points of the unit disk at pseudohyperbolic distance \(\rho\). By the two-node Nevanlinna–Pick criterion their admissible target-value pairs form the closure of \(D_\rho\); here only its open interior is used. The complex dimension is two. The metric follows the normalization \(g_{j\bar k}=\partial_{z_j}\partial_{\bar z_k}\log K(z,z)\), without a factor of two. No weighted measure or arbitrary multipoint domain is considered. Every estimate is uniform in fixed \(a\) because the \(a\)-dependence is explicitly factored out.

## Proof
**1. Slice volume and moments.** The inequality defining \(D_\rho\), solved for \(v\) at fixed \(u\), is an ordinary disk of center and radius
\[
c_q(u)=\frac{(1-q)u}{1-q|u|^2},\qquad
R_q(u)=\frac{\sqrt q(1-|u|^2)}{1-q|u|^2}.
\]
Consequently Fubini's theorem and polar integration give the domain volume \(V=\pi^2qJ_0(q)\) and the second moment \(I_u=\int_{D_\rho}|u|^2dV=\pi^2qJ_1(q)\). All integrals are finite because \(D_\rho\subset\mathbb D^2\).

**2. Kernel on the diagonal.** This is a bounded balanced domain: simultaneous multiplication by a scalar of modulus at most one is a disk self-map and hence decreases pseudohyperbolic distance. Simultaneous rotation symmetry makes the constant functions orthogonal to all nonconstant homogeneous Taylor terms. Averaging any holomorphic square-integrable function over rotations shows its integral is \(V\) times its value at the origin; equality in the evaluation bound is achieved by constants. Thus \(K_\rho(0,0)=V^{-1}\).
For \(a\in\mathbb D\), simultaneous disk Möbius maps in the two coordinates are biholomorphic automorphisms of \(D_\rho\), carrying \((a,a)\) to \((0,0)\). The absolute square of their complex Jacobian at \((a,a)\) is \((1-|a|^2)^{-4}\). Kernel covariance gives exactly \(K_\rho((a,a),(a,a))=V^{-1}(1-|a|^2)^{-4}\).

**3. Recover the degree-one Gram matrix.** Put \(s(u,v)=u+v\), \(d(u,v)=u-v\), with squared norms \(I_s,I_d\). Their mutual inner product vanishes by interchange symmetry; they are orthogonal to degree-zero and to degrees greater than one by common rotations. The degree-one part of the Bergman kernel, evaluated at \((a,a)\), contributes \(4|a|^2/I_s\). Comparison with the coefficient \(4|a|^2/V\) in the preceding exact diagonal formula forces \(I_s=V\). Interchange symmetry also gives \(\int|u|^2=\int|v|^2=I_u\), so the parallelogram identity yields
\[
I_d=4I_u-I_s=\pi^2q(4J_1(q)-J_0(q))>0.
\]
At the origin the Hessian of \(\log K\) equals \(V\) times the Hermitian matrix of its degree-one kernel, because its first derivatives vanish. Accordingly the unit directions \(e_+,e_-\) have metric squares \(2V/I_s=2\) and \(2V/I_d=2\Lambda(q)\), respectively. Möbius invariance transfers these values to \((a,a)\), multiplying them by \((1-|a|^2)^{-2}\). This proves both exact eigenvalues and the absence of a cross term.

**4. Strict monotonicity and endpoint laws.** Let \(W_q(t)=(1-t)^2/(1-qt)^2\) and normalize it to a probability density \(W_q/J_0\) on \((0,1)\). Writing \(M(q)=J_1(q)/J_0(q)\), differentiation under the integral gives
\[
M'(q)=\operatorname{Cov}_{W_q/J_0}\!\left(t,\frac{2t}{1-qt}\right)>0,
\]
since both arguments are strictly increasing on an interval carrying nonzero density. Thus \(\Lambda(q)=1/(4M(q)-1)\) strictly decreases. Dominated convergence yields \(M(0)=1/4\) and \(M(1^-)=1/2\), establishing \(\Lambda>1\).
At the small parameter endpoint, direct Taylor integration gives
\[
J_0(q)=\frac13+\frac q6+O(q^2),\qquad J_1(q)=\frac1{12}+\frac q{15}+O(q^2),\qquad M(q)=\frac14+\frac{3q}{40}+O(q^2).
\]
It follows that \(\Lambda(q)=10/(3q)+O(1)\). At the other endpoint put \(\varepsilon=1-q\) and integrate the same rational weight, or equivalently use the exact logarithmic forms
\[
J_0(q)=\frac{-q^2+2q+2(1-q)\log(1-q)}{q^3},\quad
J_1(q)=\frac{(q^2-4q+3)\log(1-q)-\tfrac52q^2+3q}{q^4}.
\]
These give \(J_0=1+2\varepsilon\log\varepsilon+O(\varepsilon)\), \(J_1=1/2+2\varepsilon\log\varepsilon+O(\varepsilon)\), and hence \(M=1/2+\varepsilon\log\varepsilon+O(\varepsilon)\). Taking the reciprocal \(\Lambda=1/(4M-1)\) yields the stated sharp logarithmic law. All error terms follow from these elementary exact identities. \(\square\)

## Verification
The accompanying `check.py` evaluates the defining integrals and their closed forms at six interior parameters with high precision, checks the exact variance identity, and independently computes both asymptotic leading coefficients with symbolic limits; it prints `CHECK_OK`. The proof itself consists of the exact slice formula, Hilbert-space degree-one orthogonality, covariance and endpoint expansions; no finite test is treated as a proof of an infinite claim.

## Relationship to prior work
The two-value Pick positivity criterion and the realization of Pick bodies are classical. Biswas, *On interpolation in Carathéodory hyperbolic domains*, arXiv:2602.00882v1 (2026-01-31), studies interpolation bodies and matrix realizations. The subsequent *On the automorphisms of Pick bodies*, arXiv:2610.28972v1 (2026-10-20), determines global automorphism groups; its focus is the symmetry group rather than the Bergman metric. Neither inspected full article develops Bergman-kernel normalization, the diagonal Bergman eigenspectrum, or the sharp logarithmic anisotropy law. The new statement concerns intrinsic analytic geometry of this same natural interpolation domain, rather than a fresh Pick feasibility criterion.

## Limitations
Only the two-node disk Pick bodies and points on the diagonal are covered. No formula is claimed for the full off-diagonal Bergman kernel, metric away from the diagonal, higher-node interpolation bodies, or any uniform curvature estimate. Existing or unindexed earlier kernel computations, particularly older Pick-body literature not obtained in full, may contain equivalent statements; a separate independent priority assessment remains outstanding.

## References
1. A. Biswas, *On interpolation in Carathéodory hyperbolic domains*, arXiv:2602.00882v1, first posted 2026-01-31, https://arxiv.org/abs/2602.00882.
2. A. Biswas, *On the automorphisms of Pick bodies*, arXiv:2610.28972v1, posted 2026-10-20, https://arxiv.org/abs/2610.28972. Used only for comparison; not as the motivating first-publication date.
3. B. Cole, K. Lewis and J. Wermer, *A Characterization of Pick Bodies*, Journal of the London Mathematical Society 48 (1993), 316–326, DOI:10.1112/jlms/s2-48.2.316. Historical background; the full article was not retrieved.
