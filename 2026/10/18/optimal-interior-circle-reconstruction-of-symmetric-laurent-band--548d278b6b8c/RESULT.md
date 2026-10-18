# Optimal interior-circle reconstruction of symmetric Laurent bands in annular Bergman spaces

## Finding

Fix real radii \(0<a<b\) and an integer \(N\ge1\). On the annulus \(A=\{z:a<|z|<b\}\), equip the analytic Laurent band \(V_N=\operatorname{span}\{z^j:-N\le j\le N\}\) with its probability-normalized area Bergman norm. Restrict to the circle \(|z|=r\), with probability-normalized angular measure. Define the strictly positive radial moments
\[
m_j=\frac{2}{b^2-a^2}\int_a^b t^{2j+1}\,dt \qquad(-N\le j\le N).
\]
The squared singular values of circle restriction are exactly \(\lambda_j(r)=r^{2j}/m_j\). The *same unique radius* simultaneously maximizes the smallest singular value and minimizes the spectral condition number:
\[
\boxed{r_N=\left(\frac{m_N}{m_{-N}}\right)^{1/(4N)}\in(a,b).}
\]
At this radius the sharp inverse norm and sharp condition number are
\[
\boxed{\|T_{N,r_N}^{-1}\|=(m_Nm_{-N})^{1/4}},\qquad
\boxed{\kappa_N^2=\max_{-N\le j\le N}\frac{m_N^{(j+N)/(2N)}m_{-N}^{(N-j)/(2N)}}{m_j}.}
\]
The square of the condition number is thus the largest discrete multiplicative interpolation gap for the strictly log-convex moment sequence. For every fixed annulus, as \(N\to\infty\),
\[
r_N=\sqrt{ab}\left(1+\frac{\log(b/a)}{2N}+O_{a,b}(N^{-2})\right),\qquad
\boxed{\kappa_N\sim\frac{(b/a)^{N/2}}{\sqrt{2N\log(b/a)}}.}
\]
For all sufficiently large \(N\), the maximal squared singular value at \(r_N\) is uniquely the \(j=-1\) level, while the minimum is attained at the two extreme Laurent exponents \(j=\pm N\). Hence the sharp exponential instability and its complete leading constant are determined, not only its exponential rate.

## Assumptions and scope

Here \(d\mu_A(z)=dx\,dy/[\pi(b^2-a^2)]\) and \(d\mu_r(\theta)=d\theta/(2\pi)\). The restriction \(T_{N,r}:V_N\to L^2(\mathbb T,d\mu_r)\) is \((T_{N,r}f)(\theta)=f(re^{i\theta})\). Singular values refer to the Bergman Hilbert norm on the domain and the angular \(L^2\) norm on the target; the condition number uses its \((2N+1)\)-dimensional range. For \(j=-1\) the continuous extension of the moment formula is \(m_{-1}=2\log(b/a)/(b^2-a^2)\); otherwise
\[
m_j=\frac{b^{2j+2}-a^{2j+2}}{(j+1)(b^2-a^2)}.
\]
There is no claim that arbitrary, unbandlimited analytic functions can be stably reconstructed from this measurement. The optimized quantity is the relative spectral condition number as well as the absolute inverse norm, with both norms normalized exactly as above.

## Proof

**Step 1: Diagonalization and recovery.** Angular orthogonality gives \(\|\sum_{j=-N}^N c_jz^j\|_{A}^2=\sum_jm_j|c_j|^2\). Thus \(z^j/\sqrt{m_j}\) is an orthonormal basis in the domain, while \(e^{ij\theta}\) is orthonormal in the target. Each basis vector maps to \((r^j/\sqrt{m_j})e^{ij\theta}\), proving the singular spectrum. If measured Fourier coefficients are \(d_j\), the exact inverse on the range is
\[
(T_{N,r}^{-1}g)(z)=\sum_{j=-N}^Nd_j(z/r)^j,\quad g(\theta)=\sum_{j=-N}^Nd_je^{ij\theta}.
\]

**Step 2: Extreme exponents control the least singular value.** For a general positive radial measure with at least two distinct radii, let \(m(s)=\int t^{2s}\,d\nu(t)\). The logarithmic moment function \(F(s)=\log m(s)\) satisfies \(F''(s)=4\operatorname{Var}_{\nu_s}(\log t)>0\), where \(d\nu_s\propto t^{2s}d\nu\). In particular \(j\mapsto\log\lambda_j(r)=2j\log r-F(j)\) is strictly concave. Its minimum on the integer interval \([-N,N]\) is therefore at one of the two endpoints, so
\[
\sigma_{\min}(r)^2=\min\left\{\frac{r^{-2N}}{m_{-N}},\frac{r^{2N}}{m_N}\right\}.
\]
The first expression strictly decreases with \(r\), and the second strictly increases. Their unique crossing is \(r_N\), which therefore uniquely maximizes the least singular value. The crossing lies strictly inside \((a,b)\), because \(m_N/m_{-N}\) is the weighted mean of \(t^{4N}\), with positive weights \(t^{-2N}d\nu(t)\), and hence lies strictly between \(a^{4N}\) and \(b^{4N}\).

**Step 3: The same unique radius optimizes conditioning.** For \(r<r_N\) the minimum is \(r^{2N}/m_N\), so the squared condition number is
\[
\kappa(r)^2=\max_{-N\le j<N}\frac{m_N}{m_j}\,r^{2(j-N)}.
\]
Each displayed term is strictly decreasing in \(r\), and thus so is their finite maximum. For \(r>r_N\), the minimum is \(r^{-2N}/m_{-N}\), and
\[
\kappa(r)^2=\max_{-N<j\le N}\frac{m_{-N}}{m_j}\,r^{2(j+N)},
\]
which is strictly increasing. Therefore \(r_N\) is the unique minimum of the condition number as well. Substitute \(r_N^{2j}=(m_N/m_{-N})^{j/(2N)}\) and divide by the common minimum \((m_Nm_{-N})^{-1/2}\) to obtain the stated exact formula. Strict log-convexity implies that for \(N\ge2\) each interior index gives a larger squared singular value than the coincident two endpoints; for \(N=1\), \(j=0\) is the strict maximum.

**Step 4: Sharp fixed-annulus asymptotics.** For \(N\ge2\), direct integration yields
\[
\frac{m_N}{m_{-N}}=(ab)^{2N}\left(\frac ba\right)^2\frac{N-1}{N+1}\frac{1-(a/b)^{2N+2}}{1-(a/b)^{2N-2}}.
\]
Taking logarithms gives the claimed expansion for \(r_N\). Also
\[
\sqrt{m_Nm_{-N}}\sim\frac{ab}{b^2-a^2}\frac{(b/a)^N}{N}.
\]
Put \(c=\sqrt{ab}\) and \(h=\frac12\log(b/a)>0\). For each integer \(j\),
\[
\lambda_j(c)=\frac{(j+1)\sinh(2h)}{\sinh(2(j+1)h)},
\]
with the continuous value \(\lambda_{-1}(c)=\sinh(2h)/(2h)\). Because \(\sinh x/x>1\) for \(x\ne0\), the \(j=-1\) value is strictly greater than every other \(\lambda_j(c)\). Since \(\log(r_N/c)\to0\), every fixed \(\lambda_j(r_N)\) converges to \(\lambda_j(c)\). Moreover, for any fixed \(|\log(r_N/c)|<h/4\), the expression \(\lambda_j(r_N)=\lambda_j(c)\exp(2j\log(r_N/c))\) is bounded uniformly by \(C_h(|j|+1)e^{-h|j|}\) outside a bounded range of indices; this follows from the exponential lower bound on \(|\sinh(2(j+1)h)|\). Thus the unique maximum is eventually \(j=-1\). It follows that
\[
\max_j\lambda_j(r_N)\longrightarrow\frac{\sinh(2h)}{2h}=\frac{b^2-a^2}{2ab\log(b/a)}.
\]
Multiplying this limit by \(\sqrt{m_Nm_{-N}}\), which is the reciprocal of the optimal smallest squared singular value, gives \(\kappa_N^2\sim(b/a)^N/[2N\log(b/a)]\), as claimed.

**Step 5: Structural generality.** Steps 1–3, including uniqueness of the common optimizer and the exact multiplicative moment-gap formula, continue to hold for any probability radial distribution supported on at least two radii in a compact positive interval, with its corresponding strictly positive moments. Step 4 and its constants apply specifically to normalized annular area measure.

## Verification

The included standalone `verify_annulus.py` reproduces the exact moment and spectral formulas for rational radii, checks the endpoint balancing and the predicted minimality against independently chosen radii, checks the general log-convexity inequality, and tests asymptotic ratios for increasing \(N\). Numerical tests only corroborate the formulas; Steps 1–5 give the proof for every permitted annulus and integer cutoff. All analytic normalizations and endpoints are explicit.

## Relationship to prior work

Douglas and Kim (2009) study reducing subspaces and Laurent-basis weighted shifts on the Bergman annulus. Their analytic setup supplies the natural two-sided Laurent space, but their main classification does not optimize circle restriction, reconstruct Fourier data, or identify a cutoff-dependent condition number. Błocki's 2011 annulus Bergman-kernel lecture uses the same orthogonal Laurent structure for reproducing kernels, not the present minimax radius. Trefethen's 2020 analytic-continuation analysis describes annular ill-conditioning and Hadamard three-circle estimates for bounded analytic functions, rather than the exact singular spectrum and optimized Hilbert inverse of a symmetric finite Laurent band. A related harmonic Bergman trace result controls the *upper* trace norm for nonnegative disk Fourier degrees, not the two-sided annular *lower* singular value or jointly optimal conditioning. The moment/log-convexity principle is classical; the claim is the assembled sharp finite-band optimum, its identical minimax criteria, and its explicit prefactor, not invention of moment convexity itself.

## Limitations

The result is for one complete angular measurement circle with uniform angular sampling measure and symmetric frequency cutoff; it does not optimize multiple circles, discrete angular nodes, nonlinear reconstruction, or nonuniform frequency bands. The leading asymptotics hold for a fixed strictly positive-width annulus and do not claim uniformity as \(b/a\downarrow1\). Literature comparisons cannot exclude an unidentified general radial Hilbert sampling theorem from implying the same answer. No independent audit has been performed.

## References

1. R. G. Douglas and Y.-S. Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794v1 (first public version 2009-02-11), https://arxiv.org/abs/0902.1794 .
2. Z. Błocki, *Bergman Kernel in the Annulus*, lecture material from the 2011 Tambara workshop, https://gamma.im.uj.edu.pl/~blocki/events/tambara-lect.pdf .
3. L. N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*, 2020, https://ora.ox.ac.uk/objects/uuid:0e4de186-e63c-4ec3-bc1c-4b6af4fe012b .
