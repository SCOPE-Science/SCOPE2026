# Binary carries determine the exact energy transition of dyadic Riesz products

## Finding

For every real \(0<a<1\), let \(\mu_a\) be the probability measure on the additive group of dyadic integers \(\mathbb Z_2\) obtained from the Riesz-product martingale
\[
R_N(x)=\prod_{j=1}^{N}\left(1+a\cos\frac{2\pi(x\bmod 2^j)}{2^j}\right).
\]
The normalized Haar measure of \(\mathbb Z_2\) is denoted \(m\), and \(R_0=1\). Define
\[
\theta_a=1+a+\frac{a^2}{2},\quad
\lambda_{\pm}(a)=\frac{\theta_a\pm\sqrt{\theta_a^2-4a}}{2},\quad
A_a=\frac{1+a^2-\lambda_-(a)}{\lambda_+(a)-\lambda_-(a)}.
\]
Then \(1<\lambda_+(a)<2\), \(0<\lambda_-(a)<1\), and \(A_a>0\). The exact finite-level squared norms are
\[
\boxed{\int_{\mathbb Z_2} R_N^2\,dm=A_a\lambda_+(a)^N+(1-A_a)\lambda_-(a)^N\qquad(N\ge0).}
\]
In particular, the natural order-two correlation/energy dimension is
\[
\boxed{D_2(\mu_a)=1-\log_2\lambda_+(a).}
\]
For \(s>0\), put \(I_s(\mu_a)=\iint|x-y|_2^{-s}\,d\mu_a(x)d\mu_a(y)\). This energy is finite **if and only if** \(0<s<D_2(\mu_a)\). In that range, with \(z=2^{s-1}\), it is exactly
\[
\boxed{I_s(\mu_a)=1+(1-2^{-s})\left(\frac{1+(a^2/2-a)z}{1-\theta_a z+az^2}-1\right).}
\]
At the critical exponent \(s_c=D_2(\mu_a)\), the divergence has the sharp pole
\[
\boxed{\lim_{s\uparrow s_c}(s_c-s)I_s(\mu_a)=\frac{(1-2^{-s_c})A_a}{\log 2}.}
\]
Also, defining the natural resolution-\(N\) truncation
\[
I_{s,N}(\mu_a)=\iint\min\{|x-y|_2^{-s},2^{sN}\}\,d\mu_a(x)d\mu_a(y),
\]
with the integrand interpreted as \(2^{sN}\) on the diagonal, one has
\[
\boxed{I_{s_c,N}(\mu_a)=(1-2^{-s_c})A_a N+O_a(1).}
\]
For example, \(a=1/2\) gives \(\lambda_+=1.212695264839553\ldots\) and \(D_2=0.721782935228420\ldots\).

## Assumptions and scope

The additive compact group \(\mathbb Z_2\) carries Haar probability \(m\). Its standard character of conductor \(2^j\) is \(\chi_j(x)=\exp(2\pi i(x\bmod2^j)/2^j)\). The factor at level \(j\) is \(1+a\operatorname{Re}\chi_j\). A cylinder of level \(N\) is a residue class modulo \(2^N\). The limiting positive measure is defined by assigning mass \(2^{-N}R_N(x)\) to each such cylinder; these assignments are consistent. The absolute value is \(|u|_2=2^{-v_2(u)}\) for nonzero \(u\), and \(|0|_2=0\). The result concerns real constant amplitudes and consecutive character conductors; arbitrary complex phases, nonconstant amplitudes and other conductor sequences are not covered. The limiting dimension is a dimension of the **measure**, not of its support.

## Proof

**1. Martingale and cylinders.** Conditional on a residue modulo \(2^{j-1}\), the two lifts modulo \(2^j\) give opposite values of \(\chi_j\). Thus the conditional mean of \(1+a\operatorname{Re}\chi_j\) is \(1\). Since \(0<a<1\), all factors are strictly positive. Consequently, \(R_N\,dm\) is a consistent probability martingale and determines the asserted measure \(\mu_a\).

**2. Exact binary carry matrix.** Write \(S_N=\int R_N^2\,dm\). The square of each factor has the character expansion
\[
(1+a\operatorname{Re}\chi_j)^2
=\sum_{d=-2}^{2}h_d\chi_j^d,
\quad h_0=1+\frac{a^2}{2},\quad h_{\pm1}=a,\quad h_{\pm2}=\frac{a^2}{4}.
\]
Character orthogonality gives
\[
S_N=\sum_{\substack{d_1,\ldots,d_N\in\{-2,-1,0,1,2\}\\
\sum_{j=1}^{N}d_j2^{N-j}\equiv0\ (\mathrm{mod}\ 2^N)}}\prod_{j=1}^{N}h_{d_j}.
\]
Process the digits from \(j=N\) down to \(j=1\). Starting with carry \(c=0\), a new digit \(d\) is admissible precisely when \(d+c\) is even; the next carry is \((d+c)/2\). Carries remain in \(\{-1,0,1\}\), and **every** terminal carry represents a multiple of \(2^N\), so it must be counted. Symmetry makes the weights of the two nonzero carry states equal. If their common weight is \(v_1\) and the zero-carry weight is \(v_0\), the update is exactly
\[
\begin{pmatrix}v_0'\\v_1'\end{pmatrix}
=\underbrace{\begin{pmatrix}1+a^2/2&2a\\a^2/4&a\end{pmatrix}}_{B_a}
\begin{pmatrix}v_0\\v_1\end{pmatrix},
\qquad (v_0,v_1)\big|_{N=0}=(1,0),
\quad S_N=v_0+2v_1.
\]
Thus \(S_N=(1,2)B_a^N(1,0)^\mathsf T\). The matrix has trace \(\theta_a\), determinant \(a\), and distinct positive eigenvalues \(\lambda_\pm\). The characteristic polynomial is negative at \(1\) and positive at \(2\), because its values there are \(-a^2/2\) and \((1-a)(2+a)\), respectively. Hence \(0<\lambda_-<1<\lambda_+<2\). Since \(S_0=1\) and \(S_1=1+a^2\), Cayley--Hamilton gives the displayed exact formula for \(S_N\), with \(A_a>0\) (also immediate from strict Perron--Frobenius positivity).

**3. Cylinder collisions and energy.** Let \(X,Y\) be independent with law \(\mu_a\). From the cylinder masses,
\[
P_N:=\Pr(X\equiv Y\pmod {2^N})=2^{-N}S_N.
\]
Since \(\lambda_+<2\), \(P_N\to0\), so the law is nonatomic. Moreover,
\[
-\frac{\log P_N}{N\log2}\longrightarrow 1-\log_2\lambda_+.
\]
For each pair \(x\ne y\), let \(v=v_2(x-y)\). The elementary identity
\[
2^{sv}=1+\sum_{j=1}^{v}(2^{sj}-2^{s(j-1)})
\]
and Tonelli's theorem imply, with \(z=2^{s-1}\),
\[
I_s(\mu_a)=1+(1-2^{-s})\sum_{N\ge1}z^N S_N.
\]
The nonnegative series converges if and only if \(z\lambda_+<1\), equivalently \(s<s_c\). The sequence \(S_N\) obeys \(S_{N+2}=\theta_a S_{N+1}-a S_N\), so its generating function is
\[
\sum_{N\ge0}S_Nz^N=\frac{1+(a^2/2-a)z}{1-\theta_a z+az^2}.
\]
Substitution yields the exact energy formula, with divergence for \(s\ge s_c\).

**4. Critical behavior.** The spectral decomposition yields
\[
\sum_{N\ge1}z^N S_N
=A_a\frac{\lambda_+z}{1-\lambda_+z}+(1-A_a)\frac{\lambda_-z}{1-\lambda_-z}.
\]
As \(s\uparrow s_c\), the first denominator equals \(1-2^{s-s_c}=(s_c-s)\log2+O((s_c-s)^2)\); the second term stays bounded. This proves the exact pole residue. At \(s=s_c\), the truncated geometric series equals \(A_aN+O_a(1)\), proving the finite-resolution statement.

The boundary cases have the expected limits: at \(a=0\) the measure is Haar and \(S_N=1\); at \(a=1\) the finite densities are \(2^N\) times the indicator of the zero cylinder, giving the point mass at zero and infinite energy for every \(s>0\). These endpoints are not used to infer the open-parameter theorem.

## Verification

The separate standard-library script `check.py` recomputes the exact Fourier zero-coefficient sum using rational arithmetic for \(20\) parameter/level cases and compares it against the carry matrix. It separately computes all \(2^N\) trigonometric cylinder values in \(35\) further cases, checks four subcritical energy sums against the rational generating function, tests the Perron leading term, and verifies both endpoint identities. Run with `python3 check.py`. The finite checks corroborate the algebra; they do not prove the statements for infinitely many levels or all real parameters.

## Relationship to prior work

Liu and Liao, *P-adic s-energy and Fourier dimension* (first public version 2026-09-19, arXiv:2609.22881), prove general energy/Fourier identities and determine Fourier dimension for dyadic Riesz products, including the non-dissociated case. The present claim concerns a **different invariant**: the exact dyadic \(L^2\) collision growth, full subcritical Riesz energy, its critical exponent, and its sharp divergence coefficient for constant amplitudes. The explicit two-state transfer above exploits collisions not represented by an independent-factor product.

Fan and Zhang (2009) calculate energy dimensions for odd-prime \(p\)-adic Riesz products through their dissociated Fourier spectra. Those identities do not directly apply at \(p=2\), where adjacent characters satisfy doubling relations. Zhang's 2009 work treats Riesz products on dyadic integers and their Hausdorff dimension; its detailed manuscript was not accessible for a decisive full-text comparison. It remains possible that an equivalent binary carry calculation occurs there or in unindexed related literature. The current statement is not a claim of unconditional historical priority.

## Limitations

Only real, level-independent \(0<a<1\) and conductors \(2,4,8,\ldots\) are treated. This proves the energy/correlation dimension of \(\mu_a\), not its Hausdorff dimension, Fourier dimension, absolute continuity classification, or exact multifractal spectrum. A specific earlier dyadic Riesz-product manuscript could not be inspected in full, leaving an explicit priority risk.

## References

1. C. Liu and L. Liao, *P-adic s-energy and Fourier dimension*, arXiv:2609.22881 (first public version 2026-09-19), https://arxiv.org/abs/2609.22881.
2. A. Fan and X. Zhang, *Some Properties of Riesz Products on the Ring of p-Adic Integers*, Journal of Fourier Analysis and Applications 15 (2009), 521–552, https://doi.org/10.1007/s00041-009-9059-z.
3. X.-Y. Zhang, *Riesz products on the ring of dyadic integers*, Journal of Mathematical Analysis and Applications 357 (2009), 103–114, https://doi.org/10.1016/j.jmaa.2009.03.067.
