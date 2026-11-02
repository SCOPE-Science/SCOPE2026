# Sharp small-double-cap Slepian conditioning and the parity of the least observable spherical harmonics

## Finding
For the spherical harmonic space \(V_L\) of all degrees up to a fixed integer \(L\ge1\), restriction to two shrinking antipodal polar caps has a sharp smallest concentration eigenvalue. With \(s=\sin^2\Theta\),
\[
\lambda_{\min}(s)=\frac{s^{L+1}}{(L+1)\binom{L}{\lfloor L/2\rfloor}^{2} B(L+1,\tfrac12)}(1+O_L(s)),
\quad \lambda_{\max}(s)=\frac{(L+1)(L+2)}4s+O_L(s^2).
\]
The least eigenspace is **one-dimensional in azimuthal order \(m=0\)** when \(L\) is even and **two-dimensional in azimuthal orders \(m=\pm1\)** when \(L\) is odd, for all sufficiently small positive \(s\). Hence the sharp norm condition number of restriction to the caps is
\[
\kappa_L(s)=(L+1)\binom{L}{\lfloor L/2\rfloor}\sqrt{\frac{(L+2)B(L+1,\tfrac12)}4}\,s^{-L/2}(1+O_L(s)).
\]
These statements determine the least-observable angular symmetry and the exact leading deterioration of inverse recovery.

## Assumptions and scope
The unit sphere \(S^2\) carries its standard surface measure \(d\omega\), of total mass \(4\pi\). \(V_L=\bigoplus_{\ell=0}^L\mathcal H_\ell(S^2)\) has dimension \((L+1)^2\), with the unweighted full-sphere norm. Fix \(L\ge1\) throughout, and let \(E_\Theta\) be the union of polar caps \(0\le\vartheta\le\Theta\) and \(\pi-\Theta\le\vartheta\le\pi\). Set \(s=\sin^2\Theta\in(0,1)\). The positive definite concentration form is \(Q_s(f)=\int_{E_\Theta}|f|^2d\omega\) divided by \(\int_{S^2}|f|^2d\omega\). Its smallest and largest generalized eigenvalues are \(\lambda_{\min}(s)\) and \(\lambda_{\max}(s)\). We write \(B(a,b)=\int_0^1u^{a-1}(1-u)^{b-1}du\). All errors allow constants depending on fixed \(L\).

## Proof
**1. Exact separation.** Rotation about the pole and reflection across the equator commute with both quadratic forms. Fix \(m\in\{0,\ldots,L\}\) and a parity \(\epsilon\in\{0,1\}\) with \(m+\epsilon\le L\). The associated invariant space is, apart from a common angular factor and scalar,
\[
f(\vartheta,\varphi)=e^{im\varphi}(\sin\vartheta)^m(\cos\vartheta)^\epsilon p(\sin^2\vartheta),\quad \deg p\le r=\lfloor(L-m-\epsilon)/2\rfloor.
\]
This follows from the associated Legendre polynomial parity and its full polynomial span across degrees \(m+\epsilon,m+\epsilon+2,\ldots,m+\epsilon+2r\). The ratio of the two quadratic forms, after substituting \(u=\sin^2\vartheta\) on each cap and both hemispheres, **exactly** becomes
\[
R_{m,\epsilon,s}(p)=\frac{\int_0^s u^m(1-u)^{\epsilon-1/2}|p(u)|^2du}{\int_0^1u^m(1-u)^{\epsilon-1/2}|p(u)|^2du}.
\]
The same block occurs for \(m\) and \(-m\) when \(m>0\), giving the precise symmetry multiplicities.

**2. A small-endpoint polynomial lemma.** Let integers \(m,r\ge0\) and \(\beta>-1\) be fixed. The least Rayleigh quotient on polynomials of degree at most \(r\), for weights \(u^m(1-u)^\beta\) on \([0,s]\) versus \([0,1]\), is
\[
\frac{s^{m+2r+1}}{(m+2r+1)\binom{m+2r}{r}^2B(m+2r+1,\beta+1)}(1+O_{m,r,\beta}(s)). \tag{1}
\]
Here is a derivation of the nontrivial leading constant and remainder. Let \(\pi_j^s\) be the monic degree-\(j\) polynomials orthogonal on \([0,s]\) for weight \(u^m(1-u)^\beta\), with local squared norms \(h_j(s)\). Substitute \(u=sv\). Regularity of the rescaled weight, and the nonsingularity of its finite moment matrices, imply that \(s^{-j}\pi_j^s(sv)\) converges coefficientwise with \(O(s)\) error to the unique monic \(v^m\)-orthogonal polynomial
\[
q_j(v)=\frac{P_j^{(0,m)}(2v-1)}{\binom{m+2j}{j}},\qquad \int_0^1v^m|q_j(v)|^2dv=\frac1{(m+2j+1)\binom{m+2j}{j}^2}.
\]
The Jacobi norm is the classical finite polynomial orthogonality identity (also directly checked by the binomial expansion). Thus \(h_j(s)=s^{m+2j+1}[(m+2j+1)\binom{m+2j}{j}^2]^{-1}(1+O(s))\). In the basis \(\pi_0^s,\ldots,\pi_r^s\), the local Gram matrix is diagonal with entries \(h_j\), while the full Gram matrix has entries \(B(m+i+j+1,\beta+1)+O(s)\). The largest eigenvalue of the full matrix conjugated by \(\operatorname{diag}(h_j^{-1/2})\) is its \(r,r\) contribution
\[
\frac{B(m+2r+1,\beta+1)}{h_r(s)}(1+O(s)):
\]
all other diagonal terms are smaller by \(O(s^2)\), and the closest off-diagonal terms by \(O(s)\) relative to that contribution. Taking the reciprocal proves (1), including the relative \(O(s)\) error. When \(r=0\), (1) is the elementary beta-integral expansion.

**3. Selecting the least spherical sector.** Apply (1) with \(\beta=\epsilon-1/2\). The smallest eigenvalue in the \((m,\epsilon)\) block is
\[
\lambda_{m,\epsilon}^{\rm least}(s)=\frac{s^{m+2r+1}}{(m+2r+1)\binom{m+2r}{r}^2B(m+2r+1,\epsilon+1/2)}(1+O_L(s)). \tag{2}
\]
Other eigenvalues of each block have smaller vanishing exponents, as follows from the same local orthogonal-polynomial hierarchy (or finite-dimensional min–max comparison of the graded Gram matrices). We need maximize \(d=m+2r+1\). It is at most \(L+1\), with equality precisely for \(\epsilon=0\), \(m\equiv L\pmod2\) and \(r=(L-m)/2\). In these sectors, the beta factor and \(d\) coincide. The unique largest binomial coefficient \(\binom Lr\) on the admissible side \(0\le r\le\lfloor L/2\rfloor\) occurs at \(r=\lfloor L/2\rfloor\). This gives \(m=0\) for even \(L\), and \(m=1\) for odd \(L\). Finitely many strict comparisons in the leading coefficients, together with (2), give these as the *exact* least sectors for sufficiently small \(s\). In the even case the sector is simple; in the odd case the conjugate \(m=\pm1\) sectors are exactly degenerate and each has a simple least eigenvalue. Equation (2) yields the asserted minimal coefficient.

**4. Largest eigenvalue.** The cap area is \(\pi s+O(s^2)\). The reproducing kernel of \(V_L\), normalized with standard surface measure, satisfies
\[
K_L(n,n)=\frac{(L+1)^2}{4\pi},\qquad K_L(n,-n)=\frac{(-1)^L(L+1)}{4\pi}
\]
by the spherical-harmonic addition theorem and \(\sum_{\ell=0}^L(2\ell+1)(-1)^\ell=(-1)^L(L+1)\). Uniform smoothness on the finite-dimensional unit sphere implies in operator norm
\[
Q_s=\pi s\,[\mathrm{ev}_n^*\mathrm{ev}_n+\mathrm{ev}_{-n}^*\mathrm{ev}_{-n}]+O_L(s^2).
\]
The nonzero eigenvalues of this two-point evaluation Gram matrix are \(\pi s[K_L(n,n)\pm|K_L(n,-n)|]\). Its largest equals \(\frac{(L+1)(L+2)}4s+O_L(s^2)\). Take \(\kappa_L=\sqrt{\lambda_{\max}/\lambda_{\min}}\) to finish.

## Verification
A standalone script `check_caps.py` computes generalized Gram eigenvalues from incomplete beta integrals at 85-digit precision for degrees \(1\le L\le6\), cap parameters \(s\in\{0.01,0.02,0.04\}\), and all azimuthal/parity blocks. It checks dimensions, positive eigenvalues, the predicted least sectors and multiplicities, consistency with both endpoint expansions, and the weighted monic Jacobi norm identity. Execute `python check_caps.py` with `mpmath` installed. These finite tests support the computations but do not establish the all-degree theorem, which follows from the preceding proof.

## Relationship to prior work
Simons and Dahlen's *Spherical Slepian functions and the polar gap in geodesy* (arXiv:math/0603271, 2006), Section 4.2 and Section 5.2, develops the exact double-polar-cap operator and its symmetry blocks and commuting tridiagonal algorithm. The new assertion here is the **fixed-bandwidth, shrinking-cap sharp least eigenvalue**, the cross-sector parity of its minimizer, and the full restriction conditioning constant; the 2006 analysis instead gives a numerical/spectral framework and polar-gap reconstruction. The general spherical Slepian theory of Simons, Dahlen, and Wieczorek (2006) also treats small-domain/high-bandwidth scaling, a distinct joint limit. Xiao and Zhuang's (2023) study of spherical-harmonic function approximation using spherical designs supplies a more recent spherical sampling context, but treats discrete cubature/approximation rather than double-cap smallest-eigenvalue asymptotics. These comparisons do not establish historical novelty conclusively.

## Limitations
The asymptotic is at **fixed** finite \(L\), with \(s\downarrow0\); it makes no uniform claim for \(L\to\infty\), general nonsymmetric masks, nor the spectrum beyond the extremes and the least-eigenspace parity. The two caps are equally sized and precisely antipodal. The numerical experiment tests degrees at most six and is not an infinite-dimensional proof. Historical-priority assessment remains provisional; no independent validation is claimed.

## References
- F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, arXiv:math/0603271v1 (first public 11 March 2006), especially Sections 4.2 and 5.2. https://arxiv.org/pdf/math/0603271
- F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review 48 (2006), 504–536, DOI 10.1137/S0036144504445765.
- Y. Xiao and X. Zhuang, *Spherical Designs for Function Approximation and Beyond*, arXiv:2311.18333v1, posted 30 November 2023, MSC2020 42C05 (first listed). https://arxiv.org/abs/2311.18333
- Classical Jacobi polynomial orthogonality and spherical-harmonic addition theorem (standard identities used with their explicit normalizations above).
