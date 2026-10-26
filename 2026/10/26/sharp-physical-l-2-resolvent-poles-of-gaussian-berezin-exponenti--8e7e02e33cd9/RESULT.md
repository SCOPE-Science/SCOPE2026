# Sharp physical-\(L^2\) resolvent poles of Gaussian Berezin exponential-polynomial jets

## Finding
For every integer \(m\ge1\) and all \(\alpha,\beta\in\mathbb C\setminus\{0\}\), let \(\mu(dz)=\pi^{-1}e^{-|z|^2}dA(z)\) and
\[
\mathcal E_m=\{F_R(z)=e^{\alpha z+\beta\bar z}R(z,\bar z): R\in\mathbb C[z,w],\ \deg R\le m\}\subset L^2(\mu).
\]
Restrict Gaussian Berezin convolution \(\mathcal B F(z)=\int_{\mathbb C}F(z+\xi)\,\mu(d\xi)\) to \(\mathcal E_m\), with the **actual inherited** \(L^2(\mu)\) norm. Put \(\lambda=e^{\alpha\beta}\). Then \(\mathcal B_m\) has the single eigenvalue \(\lambda\), and its resolvent satisfies the sharp formula
\[
\boxed{\lim_{\zeta\to\lambda}|\zeta-\lambda|^{m+1}\big\|(\zeta I-\mathcal B_m)^{-1}\big\|_{L^2(\mu)\to L^2(\mu)}=|\lambda|^m\sqrt{m!}\,(|\alpha|^2+|\beta|^2)^{m/2}.}
\]
The limit is finite, nonzero, and independent of the direction of approach. For \(\varepsilon>0\), define the operator-norm pseudospectrum by \(\sigma_\varepsilon(\mathcal B_m)=\{\lambda\}\cup\{\zeta\ne\lambda: \|(\zeta I-\mathcal B_m)^{-1}\|>1/\varepsilon\}\). Its maximal distance from \(\lambda\) is
\[
\bigl(\varepsilon |\lambda|^m\sqrt{m!}(|\alpha|^2+|\beta|^2)^{m/2}\bigr)^{1/(m+1)}(1+o(1))\quad(\varepsilon\downarrow0).
\]
At a nonzero resonance \(\alpha\beta\in2\pi i\mathbb Z\), the spectral point is \(\lambda=1\), and the formula quantifies perturbative instability near a Berezin fixed-point eigenvalue. The exact spectral multiplicities (Jordan block lengths \(1,2,\ldots,m+1\)) are included here to justify the pole order, not claimed as a separate discovery.

## Assumptions and scope
The variables \(z,w\) are independent in polynomial differentiation, and only afterward \(w=\bar z\) is imposed. Total degree of \(R\) is at most \(m\). The given finite-dimensional subspace is a space of measurable functions in physical Gaussian \(L^2\), rather than an abstract coefficient space. Every element is Gaussian-square-integrable because its exponential multiplier is linear in \(z,\bar z\). All norms are inherited \(L^2(\mu)\) norms. The Berezin integral is absolutely convergent for every such symbol. The statement does not assert that Gaussian convolution is bounded on all of \(L^2(\mu)\).

## Proof
**Step 1: Berezin block.** Let \(D=\partial_z\partial_w+\beta\partial_z+\alpha\partial_w\). Gaussian integration, or the elementary moments \(\mathbb E[\xi^j\bar\xi^k]=\delta_{jk}j!\), gives
\[
\mathcal B F_R(z)=\lambda e^{\alpha z+\beta\bar z}\bigl(e^D R\bigr)(z,\bar z),\qquad \lambda=e^{\alpha\beta}.
\]
This is precisely the polynomial transform identity derived in Qin--Liu--Huang, arXiv:2610.22136v1, equation (3.9), with its parameters relabeled. Since \(D\) lowers total degree by at least one, \(D^{m+1}=0\) on \(\mathcal P_m=\{R:\deg R\le m\}\). Accordingly \(N=\lambda(e^D-I)\) is nilpotent of index at most \(m+1\), and \(\mathcal B_m=\lambda I+N\).

**Step 2: exact pole order and leading operator.** Decompose \(D=A+C\), with \(A=\beta\partial_z+\alpha\partial_w\) lowering degree by one and \(C=\partial_z\partial_w\) lowering degree by two. All summands commute. Therefore \(D^m=A^m\) on \(\mathcal P_m\): any mixed expansion term containing \(C\) lowers degree by at least \(m+1\). Since \(e^D-I=D+O(D^2)\) in the finite nilpotent algebra,
\[
N^m=\lambda^m D^m=\lambda^m A^m.
\]
For \(\zeta\ne\lambda\), the exact finite resolvent expansion is
\[
(\zeta I-\mathcal B_m)^{-1}=\sum_{k=0}^{m}\frac{N^k}{(\zeta-\lambda)^{k+1}}.
\]
After multiplying by \((\zeta-\lambda)^{m+1}\), the operator converges in norm to \(N^m\); continuity of operator norm shows the required limit equals \(\|N^m\|\). The leading coefficient is nonzero because \((\alpha,\beta)\ne(0,0)\).

For completeness, \(D:\mathcal P_j\to\mathcal P_{j-1}\) is onto: the highest homogeneous component is acted on by the nonzero constant-coefficient directional derivative \(A\), which is surjective on each pair of consecutive homogeneous degrees; descending-degree corrections remove the lower terms created by \(C\). Thus each power \(D^k\) is onto \(\mathcal P_{m-k}\), and the rank sequence gives one Jordan block of each length \(1,2,\ldots,m+1\). This supplementary algebraic consequence is not the claimed new quantitative result.

**Step 3: exact norm in physical Gaussian space.** Put \(c=\bar\alpha+\beta\) and let \(W\) have density \(\pi^{-1}e^{-|w|^2}\). Completing the square yields
\[
\|F_R\|_{L^2(\mu)}^2=e^{|c|^2}\,\mathbb E|R(c+W,\bar c+\bar W)|^2.
\]
Define the shifted complex Hermite polynomials
\[
H_{jk}^{(c)}(z,w)=\sum_{r=0}^{\min(j,k)}(-1)^r r!\binom jr\binom kr(z-c)^{j-r}(w-\bar c)^{k-r}.
\]
Standard Gaussian moment expansion proves the exact orthogonality relation
\[
\mathbb E\bigl[H_{jk}^{(c)}(c+W,\bar c+\bar W)\overline{H_{\ell t}^{(c)}(c+W,\bar c+\bar W)}\bigr]
=\delta_{j\ell}\delta_{kt}\,j!k!.
\]
The leading homogeneous term of \(H_{jk}^{(c)}\) is \(z^jw^k\), so for an expansion \(R=\sum_{j+k\le m}r_{jk}H_{jk}^{(c)}\), we have
\[
A^m R=m!\sum_{j+k=m}\beta^j\alpha^k r_{jk}.
\]
Thus the exact norm squared of the scalar functional \(R\mapsto A^mR\) on the physical space \(\mathcal E_m\) equals
\[
e^{-|c|^2}\sum_{j+k=m}\frac{(m!)^2|\beta|^{2j}|\alpha|^{2k}}{j!k!}
=e^{-|c|^2}m!(|\alpha|^2+|\beta|^2)^m.
\]
The output symbol for a constant polynomial is \(e^{\alpha z+\beta\bar z}\), with norm \(e^{|c|^2/2}\). The shift factors cancel. Consequently
\[
\|N^m\|=|\lambda|^m\sqrt{m!}(|\alpha|^2+|\beta|^2)^{m/2},
\]
as claimed. An attaining input is obtained by taking the polynomial
\[
R_*(z,w)=\sum_{j=0}^m\binom mj\bar\beta^j\bar\alpha^{m-j}H_{j,m-j}^{(c)}(z,w).
\]
It lies in the highest Gaussian-chaos degree and attains equality in the above coefficient Cauchy--Schwarz estimate. This also proves sharpness of the operator coefficient, not merely an upper bound.

**Step 4: pseudospectral radius.** The finite Laurent series gives uniformly in the complex argument of \(\zeta-\lambda\)
\[
\| (\zeta I-\mathcal B_m)^{-1}\|=C_m|\zeta-\lambda|^{-m-1}(1+O(|\zeta-\lambda|)),
\]
where \(C_m\) is the exact coefficient above. For all sufficiently small \(\varepsilon\), the pseudospectral component near \(\lambda\) is sandwiched between disks of radii \(((1\mp\eta)C_m\varepsilon)^{1/(m+1)}\), for any fixed \(\eta>0\); away from \(\lambda\) the resolvent is bounded. Letting \(\eta\downarrow0\) gives the stated sharp radius asymptotic.

## Verification
The self-contained script `gaussian_berezin_jet_verify.py` uses exact rational arithmetic. It checks the rank of \(D^k\) and the identity \(D^m=A^m\) for degrees \(0\) through \(7\) and three nonzero real parameter pairs, together with the factorial norm identity (516 exact assertions). Independently, it constructs moment Gram matrices for the **physical shifted Gaussian** norm and solves their dual systems for degrees \(0\) through \(4\), at three parameter pairs (15 further exact comparisons). All checks passed. This finite computation supplements the analytic proof for arbitrary degree and complex parameters; it is not an exhaustive proof by enumeration.

## Relationship to prior work
Qin, Liu and Huang derive the Gaussian exponential-polynomial Berezin block identity and use its fixed vectors to correct a commutation characterization. The earlier Bauer--Choe--Koo paper investigates Berezin fixed points using Laplacian eigenfunctions. The qualitative fixed-vector and Jordan-size implications are not asserted to be new here. The distinct contribution is the exact leading **physical \(L^2\)** resolvent norm, including its cancellation of the Gaussian shift, an attaining complex-Hermite vector, and its sharp pseudospectral consequence. These quantitative operator-norm statements do not appear in the inspected 2026 full text. A complete accessible version of the 2015 paper was unavailable; its priority relationship remains a residual uncertainty.

## Limitations
The result concerns finite exponential-polynomial sectors and the inherited physical \(L^2(\mu)\) norm. It does not establish a bound for the full infinite-dimensional Gaussian convolution operator on \(L^2(\mu)\), nor does it characterize perturbations of general Toeplitz operators. The Jordan block sizes follow from already available structure and are supporting context. Publication priority beyond the inspected sources and the available mathematical-index comparisons is not independently established; no independent scientific validation has been performed.

## References
1. J. Qin, Y. Liu, S. Huang, *Commuting Toeplitz operators with harmonic symbols on the Fock space*, arXiv:2610.22136v1 (first posted 15 October 2026), especially §3 and (3.9): https://arxiv.org/html/2610.22136v1.
2. W. Bauer, B. R. Choe, H. Koo, *Commuting Toeplitz operators with pluriharmonic symbols on the Fock space*, Journal of Functional Analysis 268 (2015), 3017–3060, DOI:10.1016/j.jfa.2015.03.003 (abstract and bibliographic record inspected; full text not accessible).
