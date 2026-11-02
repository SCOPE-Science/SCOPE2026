# Airy-edge constants for every supercritical coefficient moment of radial finite Blaschke powers

## Finding
For every integer \(m\ge 2\), every strictly increasing tuple \(0<a_1<\cdots<a_m<1\), and every **fixed real exponent \(p>4\)**, set
\[
B(z)=\prod_{j=1}^{m}\frac{z-a_j}{1-a_jz},\qquad B(z)^n=\sum_{k=0}^{\infty}c_{n,k}z^k,
\]
and
\[
U=\sum_{j=1}^{m}\frac{2a_j(1+a_j)}{(1-a_j)^3},\qquad
V=\sum_{j=1}^{m}\frac{2a_j(1-a_j)}{(1+a_j)^3}.
\]
Then the **exact positive leading constant** of the supercritical moment is
\[
\boxed{\lim_{n\to\infty}n^{(p-1)/3}\sum_{k=0}^{\infty}|c_{n,k}|^p
=2^{(p-1)/3}\left(U^{-(p-1)/3}+V^{-(p-1)/3}\right)
\int_{-\infty}^{\infty}|\operatorname{Ai}(s)|^p\,ds.}
\]
The Airy integral is finite and positive for all \(p>4\). The formula handles distinct radial factors and includes arbitrary (fixed) numbers of zeros. It is not a uniform statement when the roots or \(p\) depend on \(n\).

## Assumptions and scope
All zeros are positive real, distinct, strictly inside the unit disk, and fixed as \(n\to\infty\). The exponent \(p\in(4,\infty)\) is finite and fixed. No additional monomial factor is included; a fixed monomial factor would only shift coefficient indices, leaving the moment unchanged. The Taylor coefficients are those of the analytic function \(B^n\). The Airy function has its standard real integral normalization \(\operatorname{Ai}(x)=(2\pi)^{-1}\int_{\mathbb R}^{\mathrm{osc}}e^{i(t^3/3+xt)}dt\).

Write the continuous boundary phase locally as \(B(e^{i\theta})=e^{i\phi(\theta)}\). Then
\[
F(\theta)=\phi'(\theta)=\sum_{j=1}^{m}\frac{1-a_j^2}{1-2a_j\cos\theta+a_j^2}.
\]
Every summand strictly decreases on \((0,\pi)\) and strictly increases on \((\pi,2\pi)\), so the only extremal phase velocities are
\[
\lambda_+=F(0)=\sum_j\frac{1+a_j}{1-a_j},\qquad
\lambda_-=F(\pi)=\sum_j\frac{1-a_j}{1+a_j},\qquad \lambda_-<\lambda_+.
\]
The two nondegenerate folds satisfy \(F''(0)=-U\) and \(F''(\pi)=V\), both nonzero. All other phases are nondegenerate.

## Proof
**Step 1: Fourier representation and two folds.** For integer \(n\ge1\) and \(k\ge0\),
\[
c_{n,k}=\frac1{2\pi}\int_{-\pi}^{\pi}e^{i(n\phi(\theta)-k\theta)}\,d\theta.
\]
The chosen lift can increase by \(2\pi m\), but the integrand is exactly periodic. A direct differentiation of the Poisson factors gives \(F''(0)=-U\), \(F''(\pi)=V\). As \(F\) is strictly monotone on either open semicircle, there are precisely two simple phase stationary points for velocities in \((\lambda_-,\lambda_+)\), coalescing at the two endpoints. There are no other coalescences. In particular the folds are cubic and have the opposite signs indicated above.

**Step 2: uniform Airy profiles.** Define
\[
h_+(n)=\left(\frac2{nU}\right)^{1/3},\quad
h_-(n)=\left(\frac2{nV}\right)^{1/3},\quad
s_+=(k-n\lambda_+)h_+(n),\quad s_-=(n\lambda_--k)h_-(n).
\]
For each fixed \(M<\infty\), uniformly over the integers \(k\) for which \(|s_+|\le M\),
\[
c_{n,k}=e^{in\phi(0)}h_+(n)\bigl(\operatorname{Ai}(s_+)+o_M(1)\bigr).
\]
Similarly, uniformly for \(|s_-|\le M\),
\[
c_{n,k}=e^{i(n\phi(\pi)-k\pi)}h_-(n)\bigl(\operatorname{Ai}(s_-)+o_M(1)\bigr).
\]
To obtain these statements, split the Fourier circle into small neighborhoods of the corresponding fold and their complement. Taylor expansion at zero is
\(\phi(\theta)=\phi(0)+\lambda_+\theta-U\theta^3/6+O(\theta^5)\); at \(\pi\), it is
\(\phi(\pi+t)=\phi(\pi)+\lambda_-t+Vt^3/6+O(t^5)\).
At zero make the orientation-reversing substitution \(\theta=-h_+(n)t\); at \(\pi\) use \(\theta-\pi=h_-(n)t\). The exponent then tends to \(i(t^3/3+s_\pm t)\). For fixed \(M\), the integral outside \(|t|\le L\) is bounded by \(C_M/L^2\) after integration by parts in the cubic scaled phase, provided \(L\) is larger than a constant depending on \(M\). The rest of the original circle has derivative bounded away from zero at the fold velocity and is \(O(n^{-1})\) by periodic integration by parts. First letting \(n\to\infty\) and then \(L\to\infty\) proves both local formulas without using a formal, nonuniform Taylor expansion across the whole contour.

**Step 3: uniform integrable bounds outside the Airy windows.** Let
\(d(k,n)=\min\{k-n\lambda_-,n\lambda_+-k\}\) for an integer \(k\) within the two limiting velocities, and let \(d_{\mathrm{out}}(k,n)\) be its distance to the closed interval \([n\lambda_-,n\lambda_+]\) when outside it. There are constants depending only on the fixed zeros such that
\[
|c_{n,k}|\le C n^{-1/3}\quad\text{when }\min(|k-n\lambda_-|,|k-n\lambda_+|)\le n^{1/3},
\]
\[
|c_{n,k}|\le C(n\,d(k,n))^{-1/4}\quad\text{when }k\in(n\lambda_-,n\lambda_+),\ d(k,n)\ge n^{1/3},
\]
and
\[
|c_{n,k}|\le C/d_{\mathrm{out}}(k,n)\quad\text{when }d_{\mathrm{out}}(k,n)\ge n^{1/3}.
\]
Here is a direct justification of the estimates. Cut the phase domain into fixed small neighborhoods of \(0\) and \(\pi\) and finitely many arcs with \(|F'|\) bounded below. In a fold neighborhood \(|F(\theta)-\lambda_\pm|\asymp|\theta-\theta_\pm|^2\) and \(|F'(\theta)|\asymp|\theta-\theta_\pm|\). At velocity separation \(d/n\ge n^{-2/3}\), split that neighborhood into the two subarcs of length comparable to \(\sqrt{d/n}\) containing potential stationary points and the remaining dyadic annuli. The second-derivative van der Corput estimate on each stationary subarc is \(C(nd)^{-1/4}\), because \(n|F'|\asymp\sqrt{nd}\); first-derivative integration by parts on successive complementary annuli forms a geometric series of no larger order. Finite nonfold arcs obey the usual \(O(n^{-1/2})\) estimate. At separation at most \(n^{1/3}\), the cubic van der Corput bound yields \(Cn^{-1/3}\). Beyond the velocity interval the phase derivative has constant sign and is monotone on each of the two semicircles; the first-derivative estimate is \(C/d_{\mathrm{out}}\). These bounds are uniform in all integers \(k\ge0\) and \(n\ge1\), after adjusting the constant for small \(n\).

**Step 4: pass from local profiles to the global moment.** Fix \(M\ge2\). The upper and lower windows \(|s_+|\le M\) and \(|s_-|\le M\) are disjoint for sufficiently large \(n\). For each window, a Riemann sum with mesh \(h_\pm(n)\) and the corresponding Airy profile from Step 2 yields
\[
\lim_{n\to\infty}n^{(p-1)/3}\sum_{|s_\pm|\le M}|c_{n,k}|^p
=\left(\frac2{U\ \text{or}\ V}\right)^{(p-1)/3}
\int_{-M}^{M}|\operatorname{Ai}(s)|^pds.
\]
The omitted interior coefficients satisfy the quantitative bound
\[
\limsup_{n\to\infty}n^{(p-1)/3}
\sum_{\substack{k\in(n\lambda_-,n\lambda_+)\\|s_-|>M,\ |s_+|>M}}
|c_{n,k}|^p\le C_p M^{1-p/4}.
\]
Indeed, the bulk estimate of Step 3 gives \(n^{-p/4}\sum_{d\gtrsim Mn^{1/3}}d^{-p/4}\), which after multiplication by \(n^{(p-1)/3}\) is \(O(M^{1-p/4})\). The omitted exterior coefficients likewise contribute at most \(C_pM^{1-p}\) after the same normalization. Since \(p>4\), both errors tend to zero as \(M\to\infty\). Finally \(\operatorname{Ai}(s)\) decays exponentially as \(s\to+\infty\), while its oscillatory tail has modulus \(O(|s|^{-1/4})\) as \(s\to-\infty\); hence its \(p\)-moment is finite precisely for \(p>4\). The claimed constant follows.

## Verification
The analytic checks are the exact boundary-velocity identities, the two cubic coefficients, the local Airy integral normalization, and the uniform tail exponent \(1-p/4<0\). For an exact arithmetic example, at \(a_1=1/5\), \(a_2=1/2\) the slopes are \(\lambda_-=1\), \(\lambda_+=9/2\) and the curvatures are \(U=207/16\), \(V=1/3\). At \(p=6\), the predicted normalization is
\[
\lim_{n\to\infty}n^{5/3}\sum_{k\ge0}|c_{n,k}|^6
=2^{5/3}\left((207/16)^{-5/3}+3^{5/3}\right)\int_{\mathbb R}|\operatorname{Ai}(s)|^6ds.
\]
A standalone \(\texttt{check.py}\) computes the curvatures both by exact fractions and boundary differentiation, checks sampled Airy profiles by FFT, and makes finite-size consistency comparisons; it is supplementary and does not prove the limit. Run it in an environment with NumPy and SciPy installed.

## Relationship to prior work
Szehr and Zarouf (first posted 2017-01-09, arXiv:1701.02358) gave the threshold \(p=4\) and sharp **orders of growth** for powers of one Blaschke factor. Borichev, Fouchet, and Zarouf (first posted 2021-07-01, arXiv:2107.00405) gave precise Airy coefficient asymptotics for **one** Blaschke factor, explicitly distinguishing computation of the corresponding \(p\)-norm constants as separate work. Borichev, Fouchet, and Zarouf (first posted 2024-01-31, arXiv:2401.17520) treated sharp **\(\ell^\infty\)** decay for general finite Blaschke products; their finite-product extrema can have higher-order degeneracies. Here fixed strictly aligned positive zeros enforce exactly two cubic folds and yield an **explicit global finite-\(p>4\) norm constant with contributions from both folds**. The nontrivial step beyond coefficientwise asymptotics is uniform control of the entire intervening coefficient range to justify the sum. A literature search and relevant full-text section comparisons found no statement of this multi-zero finite-\(p\) constant; this is not a guarantee of priority, and indirect derivability from general stationary-phase frameworks remains possible. The already recorded \(p=4\) logarithmic constant is a different critical regime and does not imply this Airy \(p>4\) limit.

## Limitations
The result assumes distinct fixed zeros on one ray and fixed finite \(p>4\). It does not cover configurations with nonradial zeros, higher-order stationary points, zeros approaching the circle, uniform root collisions, growing \(p\), the critical exponent \(p=4\), or the endpoint \(p=\infty\). It does not claim that these methods are novel; standard van der Corput, Airy asymptotics and stationary-phase estimates are used. No independent mathematical audit has been performed, and the priority comparison cannot rule out an unlocated equivalent theorem.

## References
1. O. Szehr and R. Zarouf, *\(\ell^p\)-norms of Fourier coefficients of powers of a Blaschke factor*, arXiv:1701.02358, publicly posted 2017-01-09.
2. A. Borichev, K. Fouchet, R. Zarouf, *On the Fourier coefficients of powers of a Blaschke factor and strongly annular functions*, arXiv:2107.00405, publicly posted 2021-07-01.
3. A. Borichev, K. Fouchet, R. Zarouf, *On the Fourier coefficients of powers of a finite Blaschke product*, arXiv:2401.17520, publicly posted 2024-01-31.
