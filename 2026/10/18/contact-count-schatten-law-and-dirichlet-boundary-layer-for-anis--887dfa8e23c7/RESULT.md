# Contact-count Schatten law and Dirichlet boundary layer for anisotropic Hardy diagonal traces

## Finding
Fix an integer \(d\ge2\). Let \(H^2(\mathbb D^d)\) be the polydisc Hardy Hilbert space with orthonormal monomials \(z^\nu\), \(\nu\in\mathbb N_0^d\). Let \(\mathcal A_d\) be the one-variable reproducing-kernel Hilbert space with kernel \((1-z\overline w)^{-d}\), so that
\[
 \left\|z^n\right\|_{\mathcal A_d}^2=\binom{n+d-1}{d-1}^{-1}.
\]
For \(\mathbf r\in[0,1]^d\), define the anisotropic diagonal trace \(R_{\mathbf r}f(z)=f(r_1z,\ldots,r_dz)\). Put \(u_j=r_j^2\), \(N_n=\binom{n+d-1}{d-1}\), and \(h_n(\mathbf u)=\sum_{|\nu|=n}\prod_j u_j^{\nu_j}\), with \(0^0=1\). Then the eigenvalues of \(R_{\mathbf r}R_{\mathbf r}^*\), in decreasing order and counting multiplicities, are exactly
\[
 \boxed{\sigma_n^2=\frac{h_n(\mathbf u)}{N_n},\qquad n=0,1,2,\ldots.}
\]
These eigenvalues are nonincreasing; they are strictly decreasing whenever at least one radius is below \(1\) and at least one radius is positive, while all radii zero give \((1,0,0,\ldots)\). The corresponding approximation numbers of \(R_{\mathbf r}\) are \(a_{n+1}(R_{\mathbf r})=\sigma_n\), including in the noncompact case.

Let \(k=|\{j:r_j=1\}|\). If \(1\le k<d\), then
\[
 \boxed{\lim_{n\to\infty}n^{(d-k)/2}\sigma_n=\left[\frac{(d-1)!}{(k-1)!}\prod_{j:r_j<1}\frac1{1-r_j^2}\right]^{1/2}=:\sqrt C.}
\]
In this case \(R_{\mathbf r}\) belongs to the Schatten class \(\mathcal S_p\) **exactly** for \(p>2/(d-k)\), for every real \(p>0\), and at the critical exponent \(p_c=2/(d-k)\),
\[
 \sum_{n=1}^{N}\sigma_n^{p_c}\sim C^{1/(d-k)}\log N.
\]
If \(k=0\), the trace belongs to every \(\mathcal S_p\), \(p>0\). More precisely, if \(\rho=\max_j u_j\in(0,1)\) has multiplicity \(\ell\), then
\[
 \sigma_n\sim\left[\frac{(d-1)!}{(\ell-1)!}\prod_{j:u_j<\rho}\frac1{1-u_j/\rho}\right]^{1/2}\rho^{n/2}n^{-(d-\ell)/2}.
\]
If all radii are zero, the trace has rank one. If \(k=d\), it is a noncompact coisometry and every approximation number equals one. In particular, the trace is compact **if and only if** at least one radius is strictly less than one.

There is also an exact critical scaling law as the radii tend to one. For fixed \(\mathbf t=(t_1,\ldots,t_d)\in[0,\infty)^d\), define \(r_j^{(N)}=\exp(-t_j/(2N))\) for integers \(N\ge1\), and let \(\sigma_N(\mathbf r^{(N)})\) be the degree-\(N\) singular value of the corresponding trace. Let \(P\) be uniform on the probability simplex \(\{p_j\ge0,\sum p_j=1\}\), i.e. \(P\sim\operatorname{Dirichlet}(1,\ldots,1)\). With \(\mu(P)=\sum_jt_jP_j\), \(V(P)=\sum_jt_j^2P_j-\mu(P)^2\), and \(\bar t=d^{-1}\sum_jt_j\), put \(\Phi_d(\mathbf t)=\mathbb E e^{-\mu(P)}\). Then
\[
 \boxed{0\le\sigma_N(\mathbf r^{(N)})^2-\Phi_d(\mathbf t)\le \frac1{2N(d+1)}\sum_{j=1}^d(t_j-\bar t)^2.}
\]
The inequalities are strict for nonconstant \(\mathbf t\). Moreover, uniformly when \(\mathbf t\) ranges over any fixed compact subset of \([0,\infty)^d\),
\[
 \boxed{\sigma_N(\mathbf r^{(N)})^2=\Phi_d(\mathbf t)+\frac1{2N}\mathbb E\big[e^{-\mu(P)}V(P)\big]+O_{d,T}(N^{-2}).}
\]
The first-order coefficient is strictly positive exactly when the \(t_j\) are not all equal. For distinct \(t_j\), the limiting profile is explicitly
\[
 \Phi_d(\mathbf t)=(d-1)!\sum_{j=1}^d\frac{e^{-t_j}}{\prod_{h\ne j}(t_h-t_j)},
\]
with its continuous extension defining coincident-parameter values.

## Assumptions and scope
The dimension \(d\) is a fixed integer at least two. Radii may vanish or equal one and may be complex before taking absolute values: arbitrary coordinate phases are absorbed by unitary rotations on the Hardy domain. The target is specifically the RKHS with kernel \((1-z\overline w)^{-d}\), equivalently normalized weighted Bergman \(A^2_{d-2}\). Schatten \(p\) includes quasi-ideal exponents \(0<p<1\). The critical-window parameter vector is fixed as \(N\to\infty\); the stated remainder is uniform on compact parameter sets, not for unbounded moving parameters.

## Proof
**1. Orthogonal degree rows and exact norm.** The normalized output monomial is \(e_n=\sqrt{N_n}z^n\). The image of the unit input basis monomial \(z^\nu\), with \(|\nu|=n\), is \(r^\nu z^n=(r^\nu/\sqrt{N_n})e_n\). Different total degrees have mutually orthogonal images and mutually orthogonal input supports. Thus \(RR^*e_n=(h_n(\mathbf u)/N_n)e_n\). All these coefficients are at most one since each \(u_j\le1\), while the constant function realizes norm one. The degree blocks have rank one, proving the eigenvalue statement. The monotonic ordering below proves the approximation-number assertion, also for the coisometric endpoint.

**2. Ordering by a Dirichlet–multinomial coupling.** Let \(P\sim\operatorname{Dirichlet}(1,\ldots,1)\), and conditionally on \(P\) let \(I_1,I_2,\ldots\) be iid categorical random variables with probabilities \(P_j\). If \(A_{n,j}\) counts occurrences of index \(j\) among \(I_1,\ldots,I_n\), then integrating the multinomial probability over the uniform simplex gives
\[
 \mathbb P(A_n=\nu)=\frac{n!(d-1)!}{(n+d-1)!}=\frac1{N_n}\quad(|\nu|=n).
\]
Consequently \(\sigma_n^2=\mathbb E\prod_j u_j^{A_{n,j}}\). On this coupling the products decrease samplewise in \(n\). If at least one \(u_j<1\), a strict decrease occurs with positive probability while the product remains positive whenever some \(u_h>0\). The all-zero and all-one endpoints follow separately.

**3. Spectral orders and ideal boundary.** The generating function is
\[
 \sum_{n\ge0}h_n(\mathbf u)z^n=\prod_{j=1}^d(1-u_jz)^{-1}.
\]
If \(k\ge1\), factor out \((1-z)^{-k}\). The remaining factor is analytic beyond the unit circle and has value \(\prod_{u_j<1}(1-u_j)^{-1}\) at \(z=1\). Coefficient convolution with \(\binom{n+k-1}{k-1}\) gives \(h_n\sim n^{k-1}\prod_{u_j<1}(1-u_j)^{-1}/(k-1)!\). Since \(N_n\sim n^{d-1}/(d-1)!\), the power law follows. If \(k=0\) and \(\rho>0\), factor the \(\ell\) dominant poles at \(z=1/\rho\) instead; smaller poles yield exactly the displayed exponential-polynomial coefficient. The all-zero case is immediate. The Schatten membership and critical logarithmic sum now follow by the comparison with a power series of exponent \(p(d-k)/2\). Compactness is equivalent to \(\sigma_n\to0\) from this exhaustive classification.

**4. Uniform critical-window inequality.** Apply the same coupling at degree \(N\). Given \(P\), the normalized count vector \(A_N/N\) is the empirical distribution of \(N\) iid draws. Hence with \(X=\sum_j t_jA_{N,j}/N\),
\[
 \sigma_N(\mathbf r^{(N)})^2=\mathbb E e^{-X},\quad
 \mathbb E(X\mid P)=\mu(P),\quad
 \operatorname{Var}(X\mid P)=V(P)/N.
\]
Jensen's inequality gives the nonnegative defect. Taylor's theorem for \(e^{-x}\) on \([0,\infty)\), where its second derivative is at most one, gives \(\mathbb E(e^{-X}\mid P)-e^{-\mu(P)}\le V(P)/(2N)\). Standard Dirichlet moments \(\mathbb EP_j=1/d\), \(\mathbb EP_iP_j=(1+\mathbf1_{i=j})/[d(d+1)]\) imply \(\mathbb EV(P)=\sum_j(t_j-\bar t)^2/(d+1)\). All inequalities are strict for nonconstant parameters because the Dirichlet density is positive on the simplex interior and exponential is strictly convex.

**5. Exact signed first-order correction.** Conditional independence gives the alternative exact identity
\[
 \sigma_N(\mathbf r^{(N)})^2=\mathbb E_P\left(\sum_jP_j e^{-t_j/N}\right)^N.
\]
For \(0\le t_j\le T\), uniformly in all simplex points \(P\), Taylor expansion of the inner logarithm gives
\[
 N\log\left(\sum_jP_j e^{-t_j/N}\right)
 =-\mu(P)+\frac{V(P)}{2N}+O_T(N^{-2}).
\]
Exponentiation and integration prove the uniform \(N^{-2}\) remainder. The expectation of the strictly positive variance weighted by \(e^{-\mu}\) vanishes only when all the \(t_j\) agree. Finally, integrating the simplex exponential (or using the elementary divided-difference identity) gives the closed formula for \(\Phi_d\), with continuous extension through ties.

## Verification
A self-contained Python checker, `checker.py`, independently enumerates low-degree multinomial compositions over rational grids, reconstructs the same exact coefficients from the Newton recurrence for complete homogeneous symmetric polynomials, compares finite Gram-row norms, and numerically probes the dimension-two signed critical-window inequality and first-order coefficient. On the included code the command `python3 checker.py` passed **7,936** finite assertions. The arbitrarily high-degree and continuous-parameter claims rely on the analytical arguments above; finite enumeration cannot certify them alone.

As a concrete nontrivial ideal boundary, with \(d=3\) and \(\mathbf r=(1,1/2,0)\),
\[
 \sigma_n^2=\frac{8\bigl(1-4^{-n-1}\bigr)}{3(n+1)(n+2)},\qquad
 \lim_{n\to\infty}n\sigma_n=\sqrt{8/3}.
\]
This trace belongs to \(\mathcal S_p\) precisely for \(p>1\), not to trace class.

## Relationship to prior work
Ren and Shi proved a diagonal range theorem between mixed-norm spaces and constructed bounded diagonalization/polarization maps; that describes the unweighted restriction's range, not the present anisotropic approximation-number sequence or singular-ideal phase diagram. Bayart and Dorval give mapping/boundedness criteria for composition operators on weighted Bergman spaces of polydiscs, chiefly with same-dimensional symbols, but do not calculate singular values of the present dimension-reducing trace family or its quantitative boundary layer. Kumari, Muthukumar, and Sarkar discuss reproducing-kernel methods and norm estimates for composition operators; this gives context rather than an implicit spectral formula. The coefficient-space singular-value reduction uses standard orthogonal-degree structure; novelty is claimed only for the complete anisotropic/contact-count classification together with the signed uniform Dirichlet crossover, not for the familiar unweighted diagonal map or elementary Dirichlet–multinomial identities themselves.

## Limitations
The calculations address only the special multiplicative coordinate-radius family of diagonal traces, not arbitrary nonlinear restrictions or general polydisc composition symbols. The boundary-layer remainder assumes a fixed dimension and bounded parameters. The findings have not undergone independent mathematical validation or independent priority review. Earlier literature on generalized diagonal mappings, weighted coefficient restriction, or Dirichlet–multinomial interpolation may contain equivalent formulas under different terminology.

## References
1. F. Bayart and A. Dorval, *Composition operators on weighted Bergman spaces of the polydisc*, arXiv:2601.19308v1, first submitted 27 January 2026, especially Introduction and Theorem 2.10.
2. G. Ren and J. Shi, *The diagonal mapping in mixed norm spaces*, Studia Mathematica 163 (2004), 103–117, DOI: 10.4064/sm163-2-1, especially Theorem 1.1 and Section 2.
3. P. Kumari, P. Muthukumar, and J. Sarkar, *New norm estimate for composition operators*, arXiv:2509.14655, original submission September 2025 (consult the arXiv submission record), especially Sections 2 and 4.
