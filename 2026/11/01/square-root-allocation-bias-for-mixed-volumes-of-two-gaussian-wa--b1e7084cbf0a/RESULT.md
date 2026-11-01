# Square-root allocation bias for mixed volumes of two Gaussian-walk hulls

## Finding
Let \(p,q\ge 1\) be integers and \(d=p+q\). Consider two independent standard Gaussian random walks in \(\mathbb R^d\), the first observed for \(m\) steps, the second for \(n\) steps, both starting at the origin. Write \(C_m,D_n\) for their respective convex hulls, including the origin. Mixed volume is normalized by \(V_d(K,\ldots,K)=\operatorname{Vol}_d(K)\), and \(C_m[p]\) means \(p\) repeated arguments.

For an integer \(r\ge1\) define
\[
F_r(k)=\sum_{\substack{j_1,\ldots,j_r\ge1\\j_1+\cdots+j_r\le k}}(j_1\cdots j_r)^{-1/2}\quad(k\ge r),\qquad F_r(k)=0\quad(k<r).
\]
The established Gaussian specialization of the independent-walk mixed-volume formula gives
\[
\mathbb E V_d(C_m[p],D_n[q])=\frac{\kappa_d}{(2\pi)^{d/2}}F_p(m)F_q(n),\qquad m\ge p,\ n\ge q,
\]
where \(\kappa_d\) is the Euclidean unit-ball volume. This exact expectation factorization is a **prior result**, not the novelty asserted here.

**Allocation theorem.** Fix a total number of steps \(N\), with \(N\ge p+q\), and maximize the expected mixed volume above over integer \(m\in\{p,\ldots,N-q\}\) and \(n=N-m\). Put
\[
\beta_r=\frac{r\,\zeta(1/2)}{\sqrt\pi}\frac{\Gamma(1+r/2)}{\Gamma((r+1)/2)},\qquad
\alpha_{p,q}=\frac{p\beta_q/\sqrt q-q\beta_p/\sqrt p}{(p+q)^{3/2}}.
\]
For every sequence of maximizing allocations \(m_N\),
\[
\boxed{m_N=\frac{p}{p+q}N+\alpha_{p,q}\sqrt N+O_{p,q}(1).}
\]
Moreover, for all sufficiently large \(N\), the set of maximizers has either one member or two consecutive members. The bias vanishes if and only if \(p=q\), and
\[
\operatorname{sgn}(\alpha_{p,q})=\operatorname{sgn}(q-p).
\]
Thus when the multiplicities differ, the smaller-multiplicity walk optimally receives an unbounded \(\Theta(\sqrt N)\) excess over its naive proportional share. For example, for \((p,q)=(2,1)\),
\[
\alpha_{2,1}=\frac{\zeta(1/2)(\pi-2\sqrt2)}{3\sqrt3\pi}<0.
\]

## Assumptions and scope
The Gaussian increments are mutually independent and identically distributed with covariance \(I_d\); both walks have zero drift. Only the two independent hulls and their repeated mixed volumes are considered. Integers \(p,q\) are fixed while \(N\to\infty\). The finite-budget maximizer need not be unique. The asymptotic \(O_{p,q}(1)\) concerns the **number of steps**, not the expected mixed volume, and the implied constant can depend on both fixed multiplicities.

## Proof
**Step 1: exact expectation (established).** The independent-copy formula of Bolotin--Zaporozhets (2026), Corollary 3.2, expresses the expected mixed volume as a sum over positive block lengths separately constrained by the respective walk horizons. For standard Gaussian increments, a block sum of length \(j\) is \(\sqrt j\) times a standard Gaussian vector. Multilinearity of the determinant and the denominator consisting of all block lengths change each summand into a product of their inverse square roots. The mean absolute determinant of a standard \(d\)-by-\(d\) Gaussian matrix is \(d!\kappa_d/(2\pi)^{d/2}\), cancelling the source's \(d!\) denominator. The two constraints factor the sum into \(F_p(m)F_q(n)\).

**Step 2: controlled coefficient asymptotics.** Set \(A(z)=\operatorname{Li}_{1/2}(z)\). Nonnegative composition sums give the exact generating identity
\[
\sum_{k\ge0}F_r(k)z^k=\frac{A(z)^r}{1-z}.
\]
The standard polylogarithm singular expansion in a slit neighborhood of \(z=1\) begins
\[
A(z)=\sqrt\pi(1-z)^{-1/2}+\zeta(1/2)+O((1-z)^{1/2}).
\]
Indeed the full expansion in powers of \((1-z)^{1/2}\) follows by composing the classical expansion in \(-\log z\) with the analytic map \(-\log z\); transfer of each term gives an expansion with arbitrary inverse-half-integer precision. In particular,
\[
F_r(k)=\frac{\pi^{r/2}}{\Gamma(1+r/2)}k^{r/2}
\left(1+\beta_r k^{-1/2}+O_r(k^{-1})\right).
\]
Termwise expansion to a sufficiently high order also controls the *first and second finite differences of the logarithm*, and yields, as \(k\to\infty\),
\[
D_r(k):=\log F_r(k)-\log F_r(k-1)
=\frac{r}{2k}-\frac{\beta_r}{2k^{3/2}}+O_r(k^{-2}),
\]
\[
D_r(k+1)-D_r(k)=-\frac{r}{2k^2}+O_r(k^{-5/2}).
\]
In particular \(F_r\) is eventually strictly log-concave in the integer step count. The differences written here hold for \(k\ge r+1\); endpoint counts are handled separately.

**Step 3: locate the maximizing allocation.** The leading factor in \(F_p(m)F_q(N-m)\) is proportional to \(m^{p/2}(N-m)^{q/2}\), uniquely maximized on the continuous interval at \(m/N=p/(p+q)\). Uniform leading asymptotics on compact subintervals, and crude estimates \(F_r(k)\le C_r k^{r/2}\) at the two ends, imply that every maximizing sequence satisfies \(m_N/N\to p/(p+q)\).

Write \(s=p/d\), \(m=sN+x\sqrt N\). For \(x\) in bounded intervals, the exact one-step log objective increment is
\[
\begin{aligned}
\Delta_N(m)&=\log\frac{F_p(m+1)F_q(N-m-1)}{F_p(m)F_q(N-m)}\\
&=D_p(m+1)-D_q(N-m)\\
&=-\frac{d^3}{2pq}N^{-3/2}(x-\alpha_{p,q})+O_{p,q}(N^{-2}).
\end{aligned}
\]
For every fixed positive \(\varepsilon\), the analogous expansion with \(m=sN+yN\) is strictly positive for \(y<0\) and strictly negative for \(y>0\), away from \(y=0\). In the intermediate regime \(\sqrt N\ll |m-sN|\ll N\), the leading drift of order \(|m-sN|/N^2\) dominates the error \(O(N^{-3/2})\). Thus first every maximum lies within \(O(\sqrt N)\) of proportional allocation, and then the displayed uniform expansion forces it within a constant number of integers of \(sN+\alpha_{p,q}\sqrt N\). Because \(D_p\) and \(D_q\) are eventually decreasing, \(\Delta_N(m)\) is strictly decreasing throughout a neighborhood containing every maximizer. Its sign can cross zero only once, leaving at most two consecutive maximizers.

**Step 4: strict bias direction.** Put \(h(x)=\Gamma(1+x/2)/(\sqrt x\,\Gamma((x+1)/2))\) for \(x>0\). Digamma differentiation gives
\[
2\frac{d}{dx}\log h(x)=\psi(1+x/2)-\psi((x+1)/2)-\frac1x.
\]
The digamma difference has the positive integral representation
\[
\psi(1+x/2)-\psi((x+1)/2)
=\int_0^\infty\frac{e^{-(x+1)t/2}}{1+e^{-t/2}}\,dt
<\int_0^\infty e^{-xt/2}\,dt=\frac2x.
\]
A sharper elementary comparison uses \(1+e^{-t/2}>2e^{-t/4}\), giving
\[
\psi(1+x/2)-\psi((x+1)/2)
<\frac12\int_0^\infty e^{-(x/2+1/4)t}\,dt
=\frac1{x+1/2}<\frac1x.
\]
Hence \(h\) is strictly decreasing. Since \(\beta_r/r^{3/2}=\zeta(1/2)h(r)/\sqrt\pi\) and \(\zeta(1/2)<0\), the sequence \(\beta_r/r^{3/2}\) is strictly increasing, proving the sign and equality assertions for \(\alpha_{p,q}\).

## Verification
Run `python3 verify_budget.py` from the same directory as this document. The script uses only the Python standard library and computes the composition sums by convolution. It performs 34 independent direct-composition checks for small \(r,k\), tests 24 finite-budget optimizers, and compares the first asymptotic coefficients for four multiplicities. Its success marker is `VERIFICATION_OK`. Floating-point calculations are numerical corroboration only. The proof of the infinite and all-large-\(N\) assertions is Steps 2--4 above, relying on standard complex-analytic singularity transfer.

## Relationship to prior work
Bolotin and Zaporozhets (first publicly posted 2026-10-07) derived the underlying exact expected-mixed-volume identity for arbitrary independent random walks. Their result **implies** the displayed factorized Gaussian expectation after elementary determinant evaluation; no originality is claimed for this identity, the generating series, or standard polylog asymptotics. Their continuous-time Brownian example (Example 3.8) has the exact power-law duration product, for which proportional allocation is optimal; the finite-step theorem above identifies the nonzero discrete correction. The claimed addition is the constrained *integer allocation* theorem, its sharp \(\sqrt N\)-scale bias, universal direction and eventual adjacent-maximizer structure. Randon-Furling and Zaporozhets (2020 preprint, subsequently 2021 publication) study a **single convex hull of multiple walks**, not this mixed-volume two-hull allocation objective. Classical polylog and transfer results underpin the asymptotic analysis. Complete comparison cannot exclude older equivalent allocation results under another terminology.

## Limitations
No uniform statement is asserted when \(p,q\) grow with \(N\), for walks with drift, heavy-tailed increments, non-Gaussian increments, or anisotropic covariance. The result does not provide a closed-form exact maximizing integer for every small budget and does not assert uniqueness in the case of integer ties. Numerical tests cannot establish historical priority or replace the all-\(N\) proof. Independent mathematical validation has not been performed.

## References
- A. Bolotin and D. Zaporozhets, *Expected mixed volumes of convex hulls of random walks and Lévy processes*, arXiv:2610.10228, initial public version October 7, 2026, especially Corollary 3.2. https://arxiv.org/abs/2610.10228
- J. Randon-Furling and D. Zaporozhets, *Convex hulls of several multidimensional Gaussian random walks*, arXiv:2007.02768, July 2020. https://arxiv.org/abs/2007.02768
- NIST Digital Library of Mathematical Functions, §25.12(ii), polylogarithm expansion (formula 25.12.12). https://dlmf.nist.gov/25.12#E12
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Chapter VI, singularity analysis and transfer theorems, Cambridge University Press, 2009. https://ac.cs.princeton.edu/home/
