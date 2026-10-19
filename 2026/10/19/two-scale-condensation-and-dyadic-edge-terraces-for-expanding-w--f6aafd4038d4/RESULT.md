# Two-scale condensation and dyadic edge terraces for expanding W maps

## Finding
Let \(\mu_a=h_a\,dx\) be the unique absolutely continuous invariant probability measure of the four-branch expanding W map specified below, and let \(c=1/2\). As \(a\downarrow0\), the height-normalized critical layer has a macroscopic profile on the \(a\)-scale,
\[
a h_a(c+at)\longrightarrow \frac23\mathbf 1_{(-1/4,1/4)}(t).
\]
At its **left edge**, a second, finer scale has a nontrivial exact limit:
\[
 a h_a(c-a/4-a^2u)\longrightarrow
 H(u):=\frac43\sum_{j=2}^{\infty}2^{-j}\mathbf 1_{\{u<q_j\}},\qquad q_j=\frac{2^{j-1}-1}{4}.
\]
Both convergences hold in \(L^1\) on every compact interval. Pointwise convergence holds at every point away from the indicated jump locations. In particular, \(H\) takes successive heights \(2/3,1/3,1/6,1/12,\ldots\) across the thresholds \(1/4,3/4,7/4,15/4,\ldots\). At the **right edge** there is no corresponding terrace sequence:
\[
 a h_a(c+a/4+a^2v)\longrightarrow\frac23\mathbf1_{\{v<0\}},\qquad v\ne0.
\]
Finally, for arbitrary positive radii \(r_a\to0\) satisfying \(r_a/a\to\ell\in[0,\infty]\), the exact shrinking-window limit is
\[
\lim_{a\downarrow0}\mu_a([c-r_a,c+r_a])=\min\{4\ell/3,\,1/3\},
\]
where the value at \(\ell=\infty\) is defined to be \(1/3\). Thus the previously established singular mass \(1/3\) comes from a flat width-\(a/2\) core with an infinitely stepped, much finer left boundary.

## Assumptions and scope
For \(0<a<1\), define the continuous, four-branch map \(W_a:[0,1]\to[0,1]\) by
\[
W_a(x)=\begin{cases}
1-4x,&0\le x<1/4,\\
(2+a)(x-1/4),&1/4\le x<1/2,\\
1/2+a/4-(2+a)(x-1/2),&1/2\le x<3/4,\\
4(x-3/4),&3/4\le x\le1.
\end{cases}
\]
Only the limit \(a\downarrow0\) is considered. Existence, uniqueness and exactness of the absolutely continuous invariant probability measure \(\mu_a\) are established in Li–Góra–Boyarsky–Proppe–Eslami [1]; the exact invariant-density series and weak convergence there are used as explicit input. Densities are understood up to Lebesgue-null modifications; pointwise statements use their canonical step-series representatives. At \(u=q_j\) and \(v=0\), no pointwise boundary value is asserted. The limiting step function is locally integrable but not integrable over all \(\mathbb R\), because \(H(u)=2/3\) to the left; only local \(L^1\) convergence is claimed.

## Proof
Write \(m=2+a\) and \(z_j=W_a^{\circ j}(c)\). Let \(\beta_j\) be the signed slope product along the one-sided critical orbit, with \(\beta_1=m\). Define \(\chi_j(x)=\mathbf1_{[0,z_j]}(x)\) if \(\beta_j>0\), and \(\chi_j(x)=\mathbf1_{[z_j,1]}(x)\) otherwise. Lemma 3.1 of [1], with its explicit normalization in Sections 3.3–3.5, gives the invariant density as
\[
 h_a=\frac{f_a}{Z_a},\quad f_a(x)=1+2A_a g_a(x),\quad
 g_a(x)=\sum_{j\ge1}\frac{\chi_j(x)}{|\beta_j|},\quad
 A_a=(1-2S_a)^{-1},\quad Z_a=\int_0^1f_a(x)\,dx,
\]
where \(S_a\) is the exact branch-orientation sum appearing in Lemma 3.2 of [1]. In particular, the normalization bounds proved there imply
\[
\frac{Z_a}{a}\longrightarrow-\frac32.
\]
That statement concerns the signed, non-normalized density \(f_a\); both \(f_a\) and \(Z_a\) are negative for sufficiently small positive \(a\). It is not an assumption that the density itself is negative.

Set \(k(a)=\min\{j\ge1:z_j\le1/4\}\). The critical-orbit calculation in [1, Eq. (3.2) and Lemma 3.3] gives \(k(a)\to\infty\) and, for \(2\le j\le k(a)\),
\[
 \beta_j=-m^j,\qquad z_j=c-\frac{a(1+a m^{j-1})}{4(1+a)},\qquad z_1=c+a/4,\quad\beta_1=m.
\]
For these terms, every \(j\le k(a)\) contributes \(m^{-j}\) to \(S_a\). Since every global branch has absolute slope at least \(m\),
\[
 \sum_{j=1}^{k(a)}m^{-j}\le S_a\le\sum_{j=1}^{\infty}m^{-j}=\frac1{1+a}.
\]
Therefore \(S_a\to1\) and \(A_a\to-1\). Also, for any fixed integer \(N\), the remaining critical-orbit tail is uniformly bounded in both the density and its orientation sum:
\[
 \sum_{j>N}|\beta_j|^{-1}\le\frac{m^{-N}}{m-1}.
\]
Consequently pointwise limits of \(g_a\) can be computed term by term, and \(g_a\) is bounded by \(1/(1+a)\) globally. Since \(a/Z_a\to-2/3\) and \(A_a\to-1\), this also bounds \(a h_a\) uniformly on all observation scales used below.

**First scale.** Put \(x=c+at\). For every fixed \(t\ne\pm1/4\), the first term tends to \(\tfrac12\mathbf1_{\{t<1/4\}}\). The \(j\)-th term for fixed \(j\ge2\) tends to \(2^{-j}\mathbf1_{\{t>-1/4\}}\), as the corresponding endpoint has \((z_j-c)/a\to-1/4\) and negative cumulative slope. Thus
\[
 g_a(c+at)\to\frac12\mathbf1_{\{t<1/4\}}+\frac12\mathbf1_{\{t>-1/4\}},
\]
so \(f_a\to-1\) for \(-1/4<t<1/4\) and \(f_a\to0\) outside its closure. Multiplication by \(a/Z_a\to-2/3\) proves the first formula. The uniform majorant gives local \(L^1\) convergence by dominated convergence.

**Finer left edge.** Put \(x=c-a/4-a^2u\). The first term tends to \(1/2\), while, for fixed \(j\ge2\), the exact orbit identity gives
\[
 \frac{c-a/4-z_j}{a^2}=\frac{m^{j-1}-1}{4(1+a)}\longrightarrow q_j.
\]
Since the \(j\)-th critical slope is negative, \(\chi_j(c-a/4-a^2u)\to\mathbf1_{\{u<q_j\}}\) whenever \(u\ne q_j\). Therefore
\[
 g_a(c-a/4-a^2u)\to\frac12+\sum_{j=2}^\infty2^{-j}\mathbf1_{\{u<q_j\}}.
\]
After the \(1+2A_ag_a\) cancellation and normalization, the claimed \(H(u)\) follows. The same dominating bound proves convergence in local \(L^1\), even across the countably many jumps. The thresholds are strictly increasing and the sum of successive geometric tails gives the heights displayed in the finding.

**Right edge.** Put \(x=c+a/4+a^2v\). For fixed nonzero \(v\), the first indicator tends to \(\mathbf1_{\{v<0\}}\). For every fixed \(j\ge2\) the orbit point remains to the left of \(c\), so its indicator tends to one. Hence \(g_a\to\frac12\mathbf1_{\{v<0\}}+\frac12\), giving the stated step after normalization. Local \(L^1\) convergence follows identically.

**Shrinking windows.** When \(\ell<\infty\), change variables \(x=c+at\) and use the first-scale local \(L^1\) convergence, with moving interval endpoints \(\pm r_a/a\), to obtain \(\int_{-\ell}^{\ell}(2/3)\mathbf1_{[-1/4,1/4]}(t)\,dt=\min\{4\ell/3,1/3\}\). If \(r_a/a\to\infty\), the previous calculation gives a \(\liminf\) of at least \(1/3\) by comparing with \([c-La,c+La]\) for any fixed \(L>1/4\). The weak-* limit in Theorem 2.1 of [1], \(\mu_a\Rightarrow(2/3)\mu_0+(1/3)\delta_c\), where \(\mu_0\) has an absolutely continuous density, gives for any \(\delta>0\) an eventual upper bound through the fixed closed window \([c-\delta,c+\delta]\). By the Portmanteau inequality and then \(\delta\downarrow0\), the \(\limsup\) is at most \(1/3\). The window theorem follows. \(\square\)

## Verification
The accompanying standalone `CHECKER.py` uses exact rational arithmetic for the branch orbit, signed cumulative derivatives and finite density series. Its discarded tail has the rigorous enclosure \(\sum_{j>N}|\beta_j|^{-1}\le m^{-N}/(m-1)\), so the printed enclosures for sample densities and window masses are certified finite-parameter bounds, not floating-point trajectory guesses. It tests \(a=1/100,1/1000,1/10000\), several shrinking-window radii, and seven sample positions across the second-scale staircase. Running the bundled checker gave `VERIFY_OK`. No finite checker is used as proof of any asymptotic: every limit follows from the density series, slope bounds and normalization in the preceding argument.

## Relationship to prior work
Li, Góra, Boyarsky, Proppe and Eslami [1] introduced this exact family, its invariant-series representation, and the weak-* limit with atomic mass \(1/3\). Those results are indispensable premises, not new claims here. Li [2] studied weak limits for a broader W-like family and likewise established qualitative stability/instability regimes. The present finding resolves the *microscopic shape* of that atom, including the \(a^2\)-scale asymmetric dyadic left-edge staircase and sharp right edge, and determines every shrinking centered window's mass. Neither inspected prior source states those multiscale asymptotics; their exact series representations make the calculations accessible, so independent priority verification remains important.

## Limitations
The results are confined to this particular W family as \(a\downarrow0\) and its canonical invariant density. No claim is made about uniform convergence at jump points, global \(L^1(\mathbb R)\) convergence after blow-up, arbitrary noncentered windows, other perturbations of Keller's map or rates of error. The original density representation and weak-* limit are credited to [1]. Existing published formulas may implicitly imply some components of the asymptotics without having identified the two-scale edge mechanism; this is a residual priority risk. Independent mathematical review has not been performed.

## References
[1] Z. Li, P. Góra, A. Boyarsky, H. Proppe and P. Eslami, *A Family of Piecewise Expanding Maps Having Singular Measure as a Limit of ACIMs*, Ergodic Theory and Dynamical Systems, doi:10.1017/S0143385711000836. Author-hosted complete manuscript: https://warwick.ac.uk/fac/sci/maths/people/staff/eslami/wmaps2.pdf . Relevant locations: Eq. (2.1), Theorem 2.1, Lemmas 3.1–3.3, Sections 3.3–3.5.

[2] Z. Li, *W-like maps with various instabilities of ACIMs*, arXiv:1109.5199v1 (public posting 2011-09-23). https://arxiv.org/abs/1109.5199 . Relevant locations: introduction and statements of weak-limit regimes.
