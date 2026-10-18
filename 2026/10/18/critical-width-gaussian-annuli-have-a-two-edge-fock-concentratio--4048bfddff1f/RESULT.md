# Critical-width Gaussian annuli have a two-edge Fock concentration spectrum

## Finding

Let \(\mathcal F^2\) be the complex Bargmann–Fock Hilbert space with norm
\[\|f\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).\]
Fix real \(a<b\). For all sufficiently large real \(R\), put \(A_R=R+a\sqrt R\), \(B_R=R+b\sqrt R\), and \(\Omega_R=\{z\in\mathbb C:A_R<|z|^2<B_R\}\). Let \(C_R=P_{\mathcal F^2}M_{\mathbf1_{\Omega_R}}\vert_{\mathcal F^2}\), with its eigenvalues counted with multiplicity in decreasing order \(\lambda_1^{\downarrow}(R)\ge\lambda_2^{\downarrow}(R)\ge\cdots>0\). Define \(w=b-a\), \(m=(a+b)/2\), let \(\Phi\) and \(\phi\) be the standard normal CDF and density, and let \(G(t)=t\Phi(t)+\phi(t)\).

**Theorem (critical annular spectral filling).** For every \(c>0\), with \(N_R=\lfloor c\sqrt R\rfloor\),
\[
\sup_{\substack{u_1,\ldots,u_{N_R}\in\mathcal F^2\\\langle u_j,u_k\rangle=\delta_{jk}}}
\sum_{j=1}^{N_R}\frac1\pi\int_{\Omega_R}|u_j(z)|^2e^{-|z|^2}\,dA(z)
=\sqrt R\,Q(c,w)+O_{a,b,c}(1),
\]
where the error is absolute and
\[
Q(c,w)=\int_{-c/2}^{c/2}\!\bigl[\Phi(w/2-y)-\Phi(-w/2-y)\bigr]dy
=2\left[G\left(\frac{w+c}{2}\right)-G\left(\frac{w-c}{2}\right)\right]-c.
\]
For every fixed \(c>0\), the ordered eigenvalues satisfy
\[
\lim_{R\to\infty}\lambda_{\lfloor c\sqrt R\rfloor}^{\downarrow}(R)
=\Phi\left(\frac{w+c}{2}\right)-\Phi\left(\frac{c-w}{2}\right)=\frac{\partial Q}{\partial c}(c,w),
\]
and the top eigenvalue tends to \(2\Phi(w/2)-1\). The limiting profile is independent of the annulus center parameter \(m\). For all \(c,w>0\),
\[0<Q(c,w)<\min\{c,w\}.\]
Thus neither the occupation bound \(N_R\) nor the geometric trace bound \(\operatorname{Tr}C_R=w\sqrt R\) is asymptotically attained at this critical width.

At every finite \(R\) with \(0<A_R<B_R\), an optimizing \(N\)-dimensional subspace for any integer \(N\ge1\) may be chosen as the span of **\(N\) consecutive monomials**. Its central degree is asymptotic to \(R+m\sqrt R\) when \(N=\lfloor c\sqrt R\rfloor\); more precisely, the first degree is \(R+(m-c/2)\sqrt R+o(\sqrt R)\). No uniqueness of every maximizing subspace is claimed when eigenvalues tie.

## Assumptions and scope

The operator is the positive bounded compact Toeplitz concentration operator of a circular annulus in the one-complex-dimensional Fock space. The parameters \(a<b\) and \(c>0\) are fixed as \(R\to\infty\); no assumption of radiality is made on the competing orthonormal functions. The width in squared radius is \((b-a)\sqrt R\), corresponding to a *fixed nonzero physical radial thickness* asymptotically. This is a boundary-dominated, non-van-Hove regime, not a homothetic dilation of an annulus with fixed inner/outer-radius ratio. The implicit constants may depend on the fixed parameters.

## Proof

**1. Exact diagonalization and optimality for unrestricted families.** The monomials \(e_k(z)=z^k/\sqrt{k!}\), \(k\ge0\), form an orthonormal basis of \(\mathcal F^2\). Rotation invariance makes \(C_R\) diagonal with eigenvalues
\[
\tau_k(R)=\frac1{k!}\int_{A_R}^{B_R}t^ke^{-t}\,dt
=\mathbb P\{A_R\le X_{k+1}\le B_R\},
\]
where \(X_{k+1}\) is a sum of \(k+1\) independent mean-one exponential random variables. Since \(\Omega_R\) has finite area, \(C_R\) is positive trace class; summing over monomials gives \(\sum_{k\ge0}\tau_k(R)=B_R-A_R=w\sqrt R\). For any orthonormal family, the Ky Fan principle bounds its total concentration by the sum of the \(N\) largest eigenvalues, with equality for corresponding eigenvectors. This step includes arbitrary complex, nonradial competitors.

**2. Exact finite annulus unimodality and consecutive-block maximizers.** Integration by parts gives, for any \(0<A<B\),
\[
\tau_{k+1}-\tau_k=\frac{A^{k+1}e^{-A}-B^{k+1}e^{-B}}{(k+1)!}.
\]
Writing \(L(A,B)=(B-A)/\log(B/A)\), this difference is positive when \(k+1<L(A,B)\), negative when \(k+1>L(A,B)\), and zero only at equality. Hence the positive sequence tends to zero and is unimodal (with at most a two-term plateau). A selection of its \(N\) largest entries can always be taken at consecutive indices. This proves the finite-dimensional optimizer assertion, independently of any asymptotic approximation.

For the moving annulus,
\[
L(A_R,B_R)=R+m\sqrt R+O_{a,b}(1),
\]
by Taylor expansion of the logarithm. Therefore a modal index is \(R+m\sqrt R+O_{a,b}(1)\). Each maximizing consecutive block must contain a modal index: a block strictly to either side increases its sum by sliding one step toward the mode.

**3. Uniform critical Gaussian approximation.** Put \(k=R+x\sqrt R\), with \(x\) in any fixed compact real interval and \(k\) a nonnegative integer. The Berry–Esseen bound applied to the \(k+1\) exponential summands, together with the expansion of their mean and standard deviation, yields, uniformly on such compact sets,
\[
\tau_k(R)=f_{a,b}(x)+O_{a,b,K}(R^{-1/2}),\qquad
f_{a,b}(x)=\Phi(b-x)-\Phi(a-x).
\]
The function \(f_{a,b}(m+y)=\Phi(w/2-y)-\Phi(-w/2-y)\) is even in \(y\), strictly positive, and strictly decreasing for \(y>0\). Indeed its derivative is \(\phi(w/2+y)-\phi(w/2-y)<0\) for \(y>0\), \(w>0\). This also proves its maximum is \(2\Phi(w/2)-1<1\).

**4. Sharp finite-rank filling limit and a uniform absolute remainder.** Let \(N_R=\lfloor c\sqrt R\rfloor\). By step 2 an optimal block of indices contains a modal index; hence all its scaled indices \((k-R)/\sqrt R\) remain in a compact set depending on \(a,b,c\). Step 3 applies uniformly to each of its \(N_R\) entries. The associated Riemann sum differs by \(O_{a,b,c}(1)\) from
\[\sqrt R\int_t^{t+c}f_{a,b}(x)\,dx,\]
where \(t\) is its scaled starting point. Since \(f_{a,b}\) is strictly symmetric-unimodal about \(m\), this integral is uniquely maximized by \(t=m-c/2\). Taking a consecutive block with starting index closest to \(R+(m-c/2)\sqrt R\) yields the lower bound \(\sqrt R Q(c,w)-O(1)\), and comparing the optimal block with the continuous maximum yields the upper bound \(\sqrt R Q(c,w)+O(1)\). The unique integral maximizer and compactness of scaled optimal starting indices also prove the asserted \(o(\sqrt R)\) centering.

**5. Sorted eigenvalue law.** For fixed \(R\), the maximal partial sums \(S_R(N)=\sum_{j=1}^N\lambda_j^{\downarrow}(R)\) are concave in integer \(N\). Step 4 gives \(R^{-1/2}S_R(\lfloor c\sqrt R\rfloor)\to Q(c,w)\) for every \(c>0\). Sandwiching the discrete slopes near \(c\) between left and right secant slopes over a fixed \(\varepsilon\)-interval, then letting \(\varepsilon\downarrow0\), shows \(\lambda_{\lfloor c\sqrt R\rfloor}^{\downarrow}(R)\to\partial_cQ(c,w)\). Direct differentiation of the displayed closed form yields the CDF difference in the theorem. The maximal eigenvalue limit follows instead from step 3 near the modal index and the monotonicity from step 2.

**6. Exact closed form and strict loss.** Let \(G'=\Phi\). Integrating the CDF differences in step 3 yields the displayed expression for \(Q\). Since \(0<f_{a,b}(x)<1\) for all finite real \(x\), \(0<Q(c,w)<c\). Moreover
\[Q(c,w)=\int_{-w/2}^{w/2}[\Phi(c/2-y)-\Phi(-c/2-y)]\,dy<w.\]
The equality of the two integral representations follows by Fubini applied to a Gaussian convolution of intervals. Together they give the strict \(\min\{c,w\}\) gap. This completes the proof.

## Verification

A standalone checker, `check.py`, reproduces finite annular eigenvalues by incomplete gamma functions, verifies the exact adjacent-gap formula and the consecutive-block property on representative finite examples, and compares the computed optimal spectral partial sums and threshold eigenvalues against \(Q(c,w)\) and \(\partial_cQ(c,w)\) at increasing \(R\). These finite numerical checks are diagnostic only; the infinite-parameter theorem is proved by the preceding spectral and probabilistic arguments. Run `python3 check.py` with Python 3 and SciPy installed.

## Relationship to prior work

Halvdansson's 2025 study of Gaussian time-frequency localization establishes an error-function plunge law for **homothetic annuli with fixed ratio of inner and outer radii** (Proposition 2.4). Its fixed-ratio assumption and proof estimates do not control the present critical family, whose annular thickness remains comparable to the Gaussian boundary smoothing length. The limiting spectral shape here is a two-edge CDF *difference*, not the single-front erfc profile of the separated-edge setting.

Nicola, Riccardi, and Tilli's 2025 work determines isoperimetric extremizers for the *sum of the largest finitely many* Fock Toeplitz eigenvalues over radial domains and records the gamma-integral eigenvalues for radial symbols. Those results do not specify the sorted spectral or optimal collective-concentration limits when a given annulus moves outward while its radial thickness stays fixed and the rank grows at the matching \(\sqrt R\) scale.

Alvarez, Camper, and Mitkovski's 2026 spectral-filling work develops general orthonormal occupancy bounds and effective-dimension asymptotics for sufficiently regular expanding sets. Their van-Hove boundary-leakage hypothesis does not apply to these critical annuli, whose boundary and area have the same growth order. The theorem provides the exact sharp limit in that excluded boundary-dominated regime. All three connections use established Fock diagonalization and Ky Fan principles; these are not originality claims.

## Limitations

Only Gaussian-window, one-complex-dimensional Fock concentration on exactly centered circular annuli is treated; translation of a complete annulus changes neither spectrum nor result. No general noncircular-domain universality, higher-dimensional classification, or fixed-ratio annulus expansion is proved. The parameters \(a,b,c\) must remain fixed; no joint uniform estimate as \(w\to0\), \(w\to\infty\), or \(c\to\infty\) is asserted. Finite numerical checks do not independently certify the analytic argument. While reviewed relevant literature does not state the present critical double-scaling law, alternative semiclassical boundary-spectral formulations remain a priority risk and independent mathematical assessment has not been performed.

## References

1. S. Halvdansson, *Empirical plunge profiles of time-frequency localization operators*, arXiv:2502.11805v1, February 17, 2025. In particular Proposition 2.4 and its proof. https://arxiv.org/abs/2502.11805
2. F. Nicola, F. Riccardi, and P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069v1, March 10, 2025; SIAM J. Math. Anal. 58 (2026), 3898–3920. https://arxiv.org/abs/2503.07069
3. T. Alvarez, T. Camper, and M. Mitkovski, *Orthogonality, Spectral Filling, and Uncertainty*, arXiv:2610.02484v1 (2026). Relevant results: Theorem 2.2 and Section 5.1. https://arxiv.org/abs/2610.02484
4. The classical Berry–Esseen inequality for sums of independent identically distributed random variables with finite third absolute moment; used solely to justify the uniform \(O(R^{-1/2})\) gamma-to-Gaussian approximation in step 3.
