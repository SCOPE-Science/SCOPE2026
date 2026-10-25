# Exact variance inflation and Gaussian coordinate-sum limits of homogeneous chainlink polytopes

## Finding
For real numbers \(a>0\), \(0<\ell\le a/2\), and every integer \(s\ge3\), let \(X^{(s)}\) be uniformly distributed with respect to ordinary \(s\)-dimensional Lebesgue measure on
\[
\mathcal C_s(a,\ell)=\{x\in[0,a]^s:\ x_i-x_{i+1}\le a-\ell\text{ for }i=1,\dots,s,\ x_{s+1}=x_1\},
\]
and set \(S_s=\sum_{i=1}^sX^{(s)}_i\). Put
\[
\Delta=\sqrt{a^2-2\ell^2},\qquad \rho=\frac{a-\Delta}{a+\Delta},\qquad
\varepsilon=\frac{\ell^2(a^2-\ell^2)}{6\Delta(a+\Delta)}.
\]
Then \(0<\rho<1\), \(\varepsilon>0\), and the following **exact finite-dimensional** mean and variance hold:
\[
\mathbb E S_s=\frac{sa}{2},\qquad
\boxed{\operatorname{Var}(S_s)=s\left[\frac{a^2}{12}+\varepsilon\frac{1-\rho^{s-1}}{1+\rho^s}\right].}
\]
In particular \(\operatorname{Var}(S_s)>sa^2/12\): the total-coordinate variance is strictly larger than in the corresponding unconditioned cube. At fixed \(a,\ell\), variance per coordinate increases **strictly** in the integer dimension \(s\ge3\), converging exponentially to
\[
\boxed{\sigma^2=\frac{a^2}{12}+\frac{\ell^2(a^2-\ell^2)}{6\sqrt{a^2-2\ell^2}\,(a+\sqrt{a^2-2\ell^2})}.}
\]
Moreover,
\[
\boxed{\frac{S_s-sa/2}{\sqrt{s}}\ \Longrightarrow\ N(0,\sigma^2)}\qquad(s\longrightarrow\infty).
\]
There is also an exact all-parameter moment-generating function and a full large-deviation principle, specified below.

## Assumptions and scope
All coordinates use the **original** Euclidean coordinates of \(\mathcal C_s(a,\ell)\), not an affine or lattice normalization. Boundary points of the inequalities have zero volume and do not affect the uniform distribution. The number of coordinates \(s\) tends to infinity with \(a,\ell\) fixed for the limit theorem. The endpoint \(\ell=a/2\) is included, while \(\ell=0\) is excluded from the strict inequalities (and may be recovered by continuity as the cube). The first public source defining these polytopes is the 15 November 2022 version of Kantarcı Oğuz--Özel--Ravichandran, arXiv:2211.08382v1.

For each real \(t\), define by continuous extension at \(t=0\)
\[
b(t)=\int_0^a e^{tx}\,dx=\begin{cases}(e^{at}-1)/t,&t\ne0,\\ a,&t=0,\end{cases}
\]
\[
d(t)=e^{at}\int_{u,v\ge0,\,u+v<\ell} e^{t(v-u)}\,du\,dv
=\begin{cases}e^{at}(\cosh(\ell t)-1)/t^2,&t\ne0,\\ \ell^2/2,&t=0.\end{cases}
\]
Let \(\lambda_\pm(t)=(b(t)\pm\sqrt{b(t)^2-4d(t)})/2\). Then \(0<\lambda_-(t)<\lambda_+(t)\) for every real \(t\), and
\[
\boxed{\mathbb E e^{tS_s}=\frac{\lambda_+(t)^s+\lambda_-(t)^s}{\lambda_+(0)^s+\lambda_-(0)^s}.}
\]
The distributions of \(S_s\) and \(sa-S_s\) agree. Moreover \(S_s/s\) satisfies the full large-deviation principle with speed \(s\) and good rate function
\[
I(x)=\sup_{t\in\mathbb R}\left\{tx-\Lambda(t)\right\},\qquad
\Lambda(t)=\log\!\left(\frac{\lambda_+(t)}{\lambda_+(0)}\right).
\]
This is a statement about the Lebesgue-volume distribution of a canonical linear functional; it does **not** claim a general central limit theorem for arbitrary nonhomogeneous chainlink parameters.

## Proof
**1. Weighted inclusion--exclusion.** Within \([0,a]^s\), let \(E_i=\{x_i-x_{i+1}>a-\ell\}\). If both \(E_i\) and \(E_{i+1}\) occur, then \(x_{i+1}<\ell\) and \(x_{i+1}>a-\ell\), impossible for \(2\ell\le a\). Hence the only nonzero intersections of forbidden events are indexed by matchings of the cycle \(C_s\), including the \(s=3\) case.

For an isolated vertex, the weighted integral is \(b(t)\). For one forbidden edge, write \(x_i=a-u\), \(x_{i+1}=v\) with \(u,v\ge0\), \(u+v<\ell\); its weighted integral is \(d(t)\), obtained by direct integration. Therefore the unnormalized exponential-volume transform equals
\[
Z_s(t)=\int_{\mathcal C_s(a,\ell)}e^{t\sum_i x_i}\,dx
=\sum_{M\text{ matching in }C_s}(-1)^{|M|}b(t)^{s-2|M|}d(t)^{|M|}.
\]
The standard cycle-matching recurrence, or direct multiplication of the transfer matrix
\[
T(t)=\begin{pmatrix}b(t)&-d(t)\\1&0\end{pmatrix},
\]
gives \(Z_s(t)=\operatorname{tr}(T(t)^s)=\lambda_+(t)^s+\lambda_-(t)^s\). This weighted identity extends the **unweighted** cycle-matching volume identity of Proposition 6.8 in the motivating paper; that prior volume identity is not new.

**2. Real analytic eigenvalues.** For real \(t\ne0\),
\[
\frac{d(t)}{b(t)^2}=\frac12\left[\frac{\sinh(\ell t/2)}{\sinh(a t/2)}\right]^2\le\frac{\ell^2}{2a^2}\le\frac18,
\]
and the inequality extends continuously to zero. Thus the discriminant is strictly positive and both roots are positive, with a strict leading root. All expressions are real analytic in \(t\). Write
\[
B(t)=e^{-at/2}b(t)=\frac{2\sinh(at/2)}t,\qquad
D(t)=e^{-at}d(t)=\frac{\cosh(\ell t)-1}{t^2},
\]
\[
L_\pm(t)=e^{-at/2}\lambda_\pm(t)=\frac{B(t)\pm\sqrt{B(t)^2-4D(t)}}2.
\]
Both \(L_\pm\) are positive and even. Consequently \(Z_s(t)=e^{sat/2}(L_+(t)^s+L_-(t)^s)\), proving \(Z_s(-t)=e^{-sat}Z_s(t)\), centered distributional symmetry, and the exact mean.

**3. Exact variance.** Expansions at zero are
\[
B(t)=a+\frac{a^3t^2}{24}+O(t^4),\qquad
D(t)=\frac{\ell^2}{2}+\frac{\ell^4t^2}{24}+O(t^4).
\]
With \(\rho=L_-(0)/L_+(0)\), differentiating the logarithm of the centered transform twice gives
\[
\frac{\operatorname{Var}(S_s)}s
=\frac{v_++\rho^sv_-}{1+\rho^s},
\quad
v_+=\frac{a^2}{12}+\varepsilon,
\quad
v_-=\frac{a^2}{12}-\frac{\varepsilon}{\rho}.
\]
Algebra yields the displayed finite formula. Since \(0<\rho<1\), the excess \(\varepsilon(1-\rho^{s-1})/(1+\rho^s)\) is strictly positive and increases strictly with \(s\); it tends to \(\varepsilon\) at an exponential rate. No finite enumeration is used to assert this all-dimensional identity.

**4. Gaussian limit.** The moment-generating function of \((S_s-sa/2)/\sqrt s\) is
\[
\frac{L_+(t/\sqrt{s})^s+L_-(t/\sqrt{s})^s}{L_+(0)^s+L_-(0)^s}.
\]
Near zero, \(\log L_+(u)=\log L_+(0)+\sigma^2u^2/2+O(u^4)\). Uniformly in a fixed neighborhood of zero, \(L_-/L_+<1\), so the second eigenvalue's contribution decays exponentially in \(s\). The displayed transform converges to \(e^{\sigma^2t^2/2}\) on an interval about zero; the moment-generating-function convergence theorem proves the asserted central limit theorem.

**5. Large deviations.** For each real \(t\), the exact transform implies \(\lim_{s\to\infty}s^{-1}\log\mathbb E e^{tS_s}=\Lambda(t)\). This limit is finite and differentiable on all of \(\mathbb R\), with \(\Lambda'(t)\to0\) as \(t\to-\infty\), and \(\Lambda'(t)\to a\) as \(t\to+\infty\), using \(\lambda_+(t)\sim b(t)\) at both ends. Convexity and analyticity, combined with \(\Lambda''(0)=\sigma^2>0\), imply strict convexity and exposed interior slopes. Since \(S_s/s\in[0,a]\), exponential tightness is immediate. The differentiable Gärtner--Ellis theorem yields the full stated good rate function, infinite off \([0,a]\).

## Verification
The self-contained Python file `check_chainlink.py` enumerates cycle matchings exactly through \(s=10\), independently integrates centered second moments of each inclusion--exclusion block using rational arithmetic, and compares against the eigenvalue formula. It also evaluates weighted three-coordinate integrals by independent Gaussian quadrature and uses conditional-cube Monte Carlo as a diagnostic. Execute `python check_chainlink.py` with NumPy installed. Its expected successful summary is `CHECK_OK matching_counts=32 exact_rational_moments=32 tilted_quadrature=3 monte_carlo=750000`. For example, at \(a=1,\ell=1/2,s=3\), the volume is \(5/8\) and exact variance is \(13/40\), versus \(1/4\) in the cube. Finite checks do not prove the limiting theorem, which follows analytically above.

## Relationship to prior work
Kantarcı Oğuz, Özel, and Ravichandran defined chainlink polytopes, proved complementary-section Ehrhart equivalence, and established an **unweighted** matching/transfer-matrix volume formula (arXiv:2211.08382v1, Definition in §1 and Proposition 6.8). The present result uses that exact structural starting point but adds the nonzero exponential tilt, the full exact finite variance, a strict variance-inflation and dimension-monotonicity law, and the Gaussian and large-deviation limits for the homogeneous dimension-growing family. It does not claim the unweighted volume formula or matching interpretation to be new. Kantarcı Oğuz and Ravichandran (arXiv:2112.00518v1) concern discrete rank-polynomial symmetry and unimodality of fence posets, not the continuous coordinate-sum volume distribution. General finite-state transfer-matrix probability theory supplies methodology but not the displayed chainlink-specific variance coefficient or its sign. A mathematically equivalent formula could exist under another finite-range-gas terminology; exhaustive bibliographic uniqueness is not asserted.

## Limitations
The variance comparison is for the sum of **all** canonical coordinates; it is not a claim that every individual coordinate has increased variance, nor a statement about Euclidean directional widths. The variance formula requires homogeneous side lengths and \(0<\ell\le a/2\), and the central limit theorem keeps these parameters fixed as the dimension grows. The LDP describes \(S_s/s\) and does not imply a local central limit theorem for infinitesimal slab volumes. Numerical checks cover finitely many sizes and do not substitute for the proof. Independent mathematical validation has not been performed.

## References
1. E. Kantarcı Oğuz, C. Y. Özel, and M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (first public 2022-11-15), especially §§1 and 6, Proposition 6.8. https://arxiv.org/abs/2211.08382
2. E. Kantarcı Oğuz and M. Ravichandran, *Rank Polynomials of Fence Posets are Unimodal*, arXiv:2112.00518v1 (2021), especially the circular-fence rank-symmetry results. https://arxiv.org/abs/2112.00518
3. A. Dembo and O. Zeitouni, *Large Deviations Techniques and Applications*, second edition, Springer, 1998: differentiable Gärtner--Ellis theorem (general probability background).
