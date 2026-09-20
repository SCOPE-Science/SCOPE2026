# Endpoint weighted extension for monomial finite-type curves

## Result

Let
\[
\gamma_k(t)=(t,t^k),\qquad 0\le t\le1,\qquad k\ge3
\]
with real \(k\), let \(\mathrm d\sigma\) be arc length on \(\Gamma_k=\gamma_k([0,1])\), and define
\[
E_{\gamma_k}f(x)=\int_{\Gamma_k} f(\xi)e^{2\pi i x\cdot\xi}\,\mathrm d\sigma(\xi).
\]
For \(R\ge1\), put
\[
\tau_R(t)=R^{-1/2}(t+R^{-1/k})^{(k-2)/2}
\]
and use Vergara's monomial normal-direction energy
\[
\mathcal E_{R,k}(f)
=\iint_{[0,1]^2}
\frac{|f(u)|^2|f(v)|^2}
{|\mathcal N_k(u)-\mathcal N_k(v)|+\tau_R((u+v)/2)}
\,\mathrm d\sigma(u)\mathrm d\sigma(v).
\]
Here \(f(u)\) abbreviates \(f(\gamma_k(u))\).

Set
\[
\beta_k=\frac{k-1}{k}.
\]
Then for every \(R\ge1\), every \(x_0\in\mathbb R^2\), and every \(f\in L^2(\mathrm d\sigma)\),
\[
\boxed{
\int_{\mathbb R^2}|E_{\gamma_k}f(x)|^4
\left(1+\frac{|x-x_0|}{R}\right)^{-\beta_k}\,\mathrm dx
\lesssim_k \mathcal E_{R,k}(f).
}
\tag{1}
\]

Vergara proved the same estimate for every exponent \(\iota>\beta_k\), and proved that a uniform estimate of this form fails for every \(\iota<\beta_k\). Consequently the sharp monomial threshold, including the previously open endpoint, is
\[
\boxed{\iota\ge\frac{k-1}{k}.}
\]

The endpoint is not obtained by summing the ball estimates across spatial annuli. At the critical exponent that argument produces a logarithmically divergent geometric series. Instead, (1) follows from a one-dimensional positive Fourier kernel after Plancherel in the linear coordinate. The terminal cutoff \(\tau_R\) emerges directly from a Schur estimate for that kernel.

## Proof

It is enough to prove the estimate for bounded \(f\); truncation preserving the phase of \(f\), followed by Fatou and monotone convergence on the energy, gives the general case. Translation of \(x_0\) is absorbed by multiplying \(f(\gamma_k(t))\) by the unimodular factor \(e^{2\pi i x_0\cdot\gamma_k(t)}\), so assume \(x_0=0\).

Write \(x=(y,z)\). Since \(|(y,z)|\ge |z|\),
\[
\left(1+\frac{|(y,z)|}{R}\right)^{-\beta_k}
\le
w_R(z):=\left(1+\frac{|z|}{R}\right)^{-\beta_k}.
\tag{2}
\]
The loss of the horizontal decay in (2) is compensated exactly by Plancherel.

### 1. Squaring the extension and Plancherel in the linear coordinate

Let
\[
a_k(t)=|\gamma_k'(t)|=\sqrt{1+k^2t^{2k-2}},\qquad
g(t)=f(\gamma_k(t))a_k(t).
\]
Then \(a_k\asymp_k1\) and
\[
E_{\gamma_k}f(y,z)=\int_0^1 g(t)e^{2\pi i(yt+zt^k)}\,\mathrm dt.
\]
For \(0<s<2\), set
\[
D_s=[\max(0,s-1),\min(1,s)],
\]
\[
F_s(t)=g(t)g(s-t),\qquad
\Phi_s(t)=t^k+(s-t)^k.
\]
Then
\[
(E_{\gamma_k}f(y,z))^2
=
\int_0^2 e^{2\pi iys}
\left(\int_{D_s}F_s(t)e^{2\pi iz\Phi_s(t)}\,\mathrm dt\right)\mathrm ds.
\]
Plancherel in \(y\) gives
\[
\int_{\mathbb R}|E_{\gamma_k}f(y,z)|^4\,\mathrm dy
=
\int_0^2
\left|\int_{D_s}F_s(t)e^{2\pi iz\Phi_s(t)}\,\mathrm dt\right|^2\mathrm ds.
\tag{3}
\]

### 2. The endpoint Fourier kernel

For \(0<\beta<1\),
\[
(1+|z|/R)^{-\beta}
=
\frac1{\Gamma(\beta)}
\int_0^\infty e^{-q}q^{\beta-1}e^{-q|z|/R}\,\mathrm dq.
\tag{4}
\]
The Fourier transform of \(e^{-a|z|}\), in the convention used here, is
\[
\int_{\mathbb R}e^{-a|z|}e^{2\pi iz\xi}\,\mathrm dz
=
\frac{2a}{a^2+4\pi^2\xi^2}.
\]
Thus (4), first for each exponential weight and then by Tonelli, associates to \(w_R\) the positive even kernel
\[
K_R(\xi)
=
\frac{2R}{\Gamma(\beta)}
\int_0^\infty
\frac{e^{-q}q^\beta}{q^2+(2\pi R\xi)^2}\,\mathrm dq
=R K_1(R\xi),
\qquad \xi\ne0.
\tag{5}
\]
At \(\xi=0\) the expression is singular, but the singularity below is locally integrable. With \(\beta=\beta_k=1-1/k\), splitting the integral in (5) at \(q\asymp |\xi|\) gives
\[
K_1(\xi)\lesssim_k
\begin{cases}
|\xi|^{-1/k},&0<|\xi|\le1,\\
|\xi|^{-2},&|\xi|\ge1.
\end{cases}
\tag{6}
\]
Moreover \(K_1(|\xi|)\) is decreasing in \(|\xi|\).

For
\[
H_s(z)=\int_{D_s}F_s(t)e^{2\pi iz\Phi_s(t)}\,\mathrm dt,
\]
apply the Fourier identity to each exponential in (4), take absolute values, and then integrate in \(q\). This yields
\[
\int_{\mathbb R}|H_s(z)|^2w_R(z)\,\mathrm dz
\le
\iint_{D_s^2}|F_s(t)||F_s(u)|
K_R(\Phi_s(t)-\Phi_s(u))\,\mathrm dt\mathrm du.
\tag{7}
\]

### 3. A Schur row bound at the terminal scale

We prove, uniformly for \(0<s<2\) and \(t\in D_s\),
\[
\boxed{
\int_{D_s}K_R(\Phi_s(t)-\Phi_s(u))\,\mathrm du
\lesssim_k
\frac1{|t^{k-1}-(s-t)^{k-1}|+\tau_R(s/2)}.
}
\tag{8}
\]

Put \(c=s/2\), \(x=|t-c|\), and \(y=|u-c|\). The interval \(D_s\) is symmetric about \(c\), and its half-length is at most \(c\). Taylor's formula, or differentiation with respect to \(x^2\), gives the uniform power-curve geometry
\[
|\Phi_s(t)-\Phi_s(u)|
\asymp_k s^{k-2}|x^2-y^2|,
\tag{9}
\]
while the mean value theorem gives
\[
|t^{k-1}-(s-t)^{k-1}|
\asymp_k s^{k-2}x.
\tag{10}
\]
These estimates remain valid for \(1<s<2\), where the symmetric interval is shorter.

Let \(a=R^{-1/k}\).

#### Flat regime: \(s\le a\)

Write \(t=sp\), \(u=sq\), and
\[
\psi(r)=r^k+(1-r)^k.
\]
Then \(Q:=Rs^k\le1\), and by (6),
\[
\begin{aligned}
\int_{D_s}K_R(\Phi_s(t)-\Phi_s(u))\,\mathrm du
&\lesssim_k sR Q^{-1/k}
\int_0^1|\psi(p)-\psi(q)|^{-1/k}\,\mathrm dq\\
&\lesssim_k R^{1-1/k}.
\end{aligned}
\tag{11}
\]
The last integral is bounded uniformly in \(p\). Indeed, away from \(p=1/2\) the zeros are simple; at \(p=1/2\), the phase has a quadratic minimum, and the worst singularity is \(|q-1/2|^{-2/k}\), integrable because \(k>2\).

In this regime
\[
|t^{k-1}-(s-t)^{k-1}|\lesssim R^{-(k-1)/k},
\]
and
\[
\tau_R(s/2)\asymp_k R^{-(k-1)/k}.
\]
Thus (11) is exactly (8).

#### Curved regime: \(s\ge a\)

Put
\[
C_s=s^{k-2},\qquad h=(RC_s)^{-1/2}.
\]
Since \(Rs^k\ge1\), one has \(h\le s\). By (9), positivity and monotonicity of the kernel, and extension of the \(y\)-integration to \([0,\infty)\),
\[
\int_{D_s}K_R(\Phi_s(t)-\Phi_s(u))\,\mathrm du
\lesssim_k
\sqrt{\frac R{C_s}}\,J_k(x/h),
\tag{12}
\]
where
\[
J_k(A)=\int_0^\infty K_1(|A^2-Y^2|)\,\mathrm dY.
\]
The kernel bounds (6) imply
\[
\boxed{J_k(A)\lesssim_k(1+A)^{-1}.}
\tag{13}
\]
For \(A\le2\), the local singularity is bounded by
\(|A^2-Y^2|^{-1/k}\); after splitting at \(Y\asymp A\), uniform integrability follows from \(2/k<1\), and the tail is \(O(Y^{-4})\). For \(A\ge2\), split into
\(|Y-A|\le A^{-1}\),
\(A^{-1}<|Y-A|\le A/2\), and the complement. The first part is \(O(A^{-1})\) by the \(|\xi|^{-1/k}\) bound, the second is \(O(A^{-1})\) by the \(|\xi|^{-2}\) bound and \(|A^2-Y^2|\asymp A|A-Y|\), and the complement is \(O(A^{-3})\).

Combining (12) and (13),
\[
\int_{D_s}K_R(\Phi_s(t)-\Phi_s(u))\,\mathrm du
\lesssim_k
\frac1{C_s(x+h)}
=
\frac1{C_sx+\sqrt{C_s/R}}.
\tag{14}
\]
Since \(s\ge R^{-1/k}\),
\[
\sqrt{C_s/R}
=R^{-1/2}s^{(k-2)/2}
\asymp_k \tau_R(s/2).
\tag{15}
\]
Equations (10), (14), and (15) prove (8).

### 4. Completion of the endpoint estimate

By symmetry of the kernel and \(2ab\le a^2+b^2\), (7) and (8) give
\[
\int_{\mathbb R}|H_s(z)|^2w_R(z)\,\mathrm dz
\lesssim_k
\int_{D_s}
\frac{|F_s(t)|^2}
{|t^{k-1}-(s-t)^{k-1}|+\tau_R(s/2)}\,\mathrm dt.
\tag{16}
\]
Integrate (16) in \(s\), use (3), and change variables \(v=s-t\). Since \(a_k\asymp_k1\),
\[
\begin{aligned}
&\int_{\mathbb R^2}|E_{\gamma_k}f(y,z)|^4w_R(z)\,\mathrm dy\mathrm dz\\
&\qquad\lesssim_k
\iint_{[0,1]^2}
\frac{|f(t)|^2|f(v)|^2}
{|t^{k-1}-v^{k-1}|+\tau_R((t+v)/2)}
\,\mathrm d\sigma(t)\mathrm d\sigma(v).
\end{aligned}
\tag{17}
\]
Vergara's normal-parameter comparison states that
\[
|\mathcal N_k(t)-\mathcal N_k(v)|\asymp_k|t^{k-1}-v^{k-1}|.
\tag{18}
\]
Hence the right-hand side of (17) is \(\lesssim_k\mathcal E_{R,k}(f)\). Combining this with (2) proves (1).

## Why the endpoint changes the threshold theorem

Vergara's Corollary 4.8 obtains the weighted estimate for
\(\iota>(k-1)/k\) by decomposing physical space into dyadic annuli, applying the ball estimate at radius \(2^jR\), and using
\[
\mathcal E_{2^jR,k}(f)\lesssim_k2^{j(k-1)/k}\mathcal E_{R,k}(f).
\]
At \(\iota=(k-1)/k\), that method sums constants over all annuli and therefore cannot decide the endpoint. The proof above does not compare different radii. It retains the oscillation in the vertical variable, where the critical spatial weight has a positive Fourier kernel whose singularity is precisely mild enough to be Schur-integrable against the quadratic two-point phase. This recovers the terminal angular cutoff without a logarithmic loss.

## Relation to prior work and originality

Vergara's arXiv:2609.20643v1, submitted 17 September 2026, proves the monomial direct theorem for every real \(k\ge3\), gives the explicit terminal scale \(\tau_R\), proves the weighted estimate for \(\iota>(k-1)/k\), proves failure below \((k-1)/k\), and explicitly states both in the introduction and at the end of Section 4.4 that the endpoint remains open.

Primary theorem statements were also checked in Bulj--Inami--Shiraki's 2026 reverse square-function paper for power curves and Schippa's 2024 generalized square-function paper. Their results concern reverse square functions, Strichartz/local-smoothing consequences, and adapted frequency decompositions, not the endpoint normal-direction-energy inequality above. Bennett--Gutiérrez--Nakamura--Oliveira's 2025 phase-space weighted-extension results were also checked at the theorem level; they concern Sobolev--Stein/Mizohata--Takeuchi inequalities under a different geometric framework and do not state (1).

Searches for the source identifier, the exact endpoint exponent, monomial/power-curve weighted extension, finite-type endpoint estimates, and equivalent normal-direction-energy formulations did not locate an earlier result implying (1). The originality claim is therefore to the best of our knowledge, not a claim of exhaustive literature coverage.

## Limitations

- The theorem settles the endpoint only for the monomial model \(\gamma_k(t)=(t,t^k)\). It does not settle Vergara's broader endpoint problem for arbitrary fixed finite-type convex curves.
- The proof uses the globally linear first coordinate and the explicit power-law two-point phase. No invariant version of the Schur argument for a general finite-type curve is claimed.
- The implicit constant is not optimized.
- No Lorentz-space endpoint, weak-type refinement, extremizer classification, or stability theorem is claimed.
- The direct source is very recent. A contemporaneous result not yet indexed by the searches performed could overlap this endpoint statement.
- No inaccessible paper was identified as especially likely to contain this exact normal-direction-energy endpoint. Some related literature was checked at theorem or abstract level rather than exhaustively line by line.

## References

1. V. Vergara, *Normal-Direction Energy and Fourier Restriction for Convex Planar Curves*, arXiv:2609.20643v1 (2026). https://arxiv.org/abs/2609.20643
2. A. Bulj, K. Inami, and S. Shiraki, *Reverse square function estimates for degenerate curves and its applications*, arXiv:2602.03167 (2026). https://arxiv.org/abs/2602.03167
3. R. Schippa, *Generalized square function estimates for curves and their conical extensions*, arXiv:2408.07248 (2024). https://arxiv.org/abs/2408.07248
4. J. Bennett, S. Gutiérrez, S. Nakamura, and I. Oliveira, *A phase-space approach to weighted Fourier extension inequalities*, Forum Math. Sigma 13 (2025), e181. https://doi.org/10.1017/fms.2025.10127
5. A. Bulj and S. Shiraki, *Fourier extension estimates on a strip in R^2*, arXiv:2508.20463 (2025). https://arxiv.org/abs/2508.20463
