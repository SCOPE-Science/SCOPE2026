# Universal log-scale Gaussian correlations of random-point number variance

## Finding

Let \(X_1,X_2,\ldots\) be independent uniform points on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\). Write \(S_N(x,s)=\sum_{j=1}^{N}\mathbf1_{(x,x+s]}(X_j)\) (circular intervals) and
\[
V_N(s)=\int_0^1\bigl(S_N(x,s)-Ns\bigr)^2\,dx.
\]
For every integer \(N\ge2\) and lengths \(s,t\in(0,1)\), put \(u=\min(s,1-s)\), \(v=\min(t,1-t)\), \(a=\min(u,v)\), and \(b=\max(u,v)\). The **exact finite-sample cross-scale covariance** is
\[
\operatorname{Cov}(V_N(s),V_N(t))
=2N(N-1)a^2\left[b(1-b)-\frac a3\right].\tag{1}
\]
In particular it is strictly positive for all interior lengths. This extends the single-length variance identity by identifying dependence *between* different window lengths.

Let \(\varepsilon_N\downarrow0\) be deterministic and satisfy
\[
\frac{\sqrt N\,\varepsilon_N}{\log N}\longrightarrow\infty.\tag{2}
\]
For any fixed real numbers \(h_1,\ldots,h_m\), define, for sufficiently large \(N\),
\[
Z_N(h)=\frac{V_N(\varepsilon_N e^h)-N\varepsilon_Ne^h(1-\varepsilon_Ne^h)}{N\sqrt{4/3}\,(\varepsilon_Ne^h)^{3/2}}.\tag{3}
\]
Then \((Z_N(h_1),\ldots,Z_N(h_m))\) converges in distribution to a centered Gaussian vector with **universal log-scale stationary covariance**
\[
R(h_i-h_j)=\frac32e^{-|h_i-h_j|/2}-\frac12e^{-3|h_i-h_j|/2}.\tag{4}
\]
Equivalently, two shrinking lengths whose ratio tends to \(r\in(0,1]\) have asymptotic correlation \(\tfrac32\sqrt r-\tfrac12r^{3/2}\). The Fourier spectral density corresponding to the covariance convention \(R(h)=(2\pi)^{-1}\int e^{i\omega h}f(\omega)\,d\omega\) is
\[
f(\omega)=\frac{3}{(\omega^2+1/4)(\omega^2+9/4)}.\tag{5}
\]
Thus asymptotic dependence depends only on the ratio of nearby observation scales; scale ratios tending to zero become decorrelated in this limiting Gaussian family.

## Assumptions and scope

The points are independent and exactly uniform on \(\mathbb T\), the sample size \(N\) is deterministic, and circular intervals are used without boundary corrections. Formula (1) holds for all \(N\ge2\) and all \(s,t\in(0,1)\). Formula (4) is finite-dimensional convergence for a fixed finite list of log-lengths; no tightness or convergence in a function space is claimed. The sufficient mesoscopic rate (2) is not asserted to be necessary or optimal. The original scalar number-variance limit theory is assumed only through the standard empirical-process strong approximation, stated explicitly in the proof.

## Proof

**1. Degenerate pair representation.** Let \(L_s(d)=(s-d)_++(s-(1-d))_+\) for \(d\in[0,1]\). The integral, over starting positions of a window, of the event that two prescribed circle points of separation \(d\) both lie in the length-\(s\) window equals \(L_s(d)\). Expanding the square and using \(\int_0^1 L_s(d)\,dd=s^2\) gives exactly
\[
V_N(s)=Ns(1-s)+2\sum_{1\le i<j\le N}K_s(X_i-X_j),\qquad K_s(d)=L_s(d)-s^2.\tag{6}
\]
All differences are taken modulo one. The kernel is conditionally centered: \(\mathbb E[K_s(X_i-X_j)\mid X_i]=0\). Consequently covariance terms corresponding to disjoint unordered pairs or pairs sharing only one index vanish; only identical unordered pairs contribute. Hence
\[
\operatorname{Cov}(V_N(s),V_N(t))=2N(N-1)\int_0^1K_s(d)K_t(d)\,dd.\tag{7}
\]
The identity \(V_N(s)=V_N(1-s)\) follows by complementing and rotating the counting interval. We may therefore assume \(0<s\le t\le1/2\). On this domain the two triangular lobes of each \(L\) are disjoint, and direct integration yields
\[
\int_0^1L_s(d)L_t(d)\,dd=2\int_0^s(s-d)(t-d)\,dd=s^2t-\frac{s^3}{3}.\tag{8}
\]
Subtracting \(s^2t^2\) proves (1). Moreover, \(b(1-b)-a/3\ge b/2-b/3=b/6>0\), proving strict positivity. At \(s=t\le1/2\), (1) reduces to \(\operatorname{Var}(V_N(s))=2N(N-1)(2s^3/3-s^4)\).

**2. A simultaneous Gaussian-bridge representation.** Let \(B\) be a standard Brownian bridge on \([0,1]\), periodically extended, and let \(H_s=\int_0^1(B(x+s)-B(x))^2\,dx\). Represent the bridge through real white noise \(dW\) on the circle: \(B(x+s)-B(x)=\int_0^1(\mathbf1_{(x,x+s]}(y)-s)\,dW(y)\). For \(k\ge1\), set \(A_k=\int_0^1e^{-2\pi iky}\,dW(y)\). The \(A_k\) are independent circular complex Gaussians with \(\mathbb E|A_k|^2=1\), so \(E_k=|A_k|^2\) are independent exponential variables of mean one. Fourier expansion in \(x\) and Parseval give **simultaneously for every specified finite collection of lengths**
\[
H_s=\sum_{k=1}^{\infty}\lambda_k(s)E_k,\qquad
\lambda_k(s)=\frac{2\sin^2(\pi ks)}{\pi^2k^2}.\tag{9}
\]
The key point is that the same \(E_k\) occur at every \(s\); a separate scalar equality in law for each \(s\) would not establish a joint limit. Identity (9) follows first in \(L^1\) by Parseval and then almost surely for each fixed \(s\) by nonnegativity; finite collections share one probability-one event.

By the Gaussian covariance identity for quadratic norms, or by applying (7) to the bridge covariance kernel, one obtains for \(0<s\le t\le1/2\)
\[
\sum_{k\ge1}\lambda_k(s)\lambda_k(t)
=2s^2\left[t(1-t)-s/3\right].\tag{10}
\]
For completeness, the bridge increment covariance kernel is \(K_s(d)\) from (6), and Isserlis' formula gives \(\operatorname{Cov}(H_s,H_t)=2\int_0^1K_s(d)K_t(d)\,dd\); this is exactly the right side of (10). Thus the joint spectral identity is also independently checked by the same geometric integral.

**3. Joint small-window Gaussian limit for the bridge.** Fix positive \(a_1,\ldots,a_m\). Normalize each centered \(H_{a_j\varepsilon}\) by \(\sqrt{4/3}\,(a_j\varepsilon)^{3/2}\). For every fixed vector of coefficients \(q\in\mathbb R^m\), (9) expresses its linear combination as \(\sum_{k\ge1}w_{k,\varepsilon}(E_k-1)\). Since \(\sin^2 z\le z^2\), \(\lambda_k(a_j\varepsilon)\le2a_j^2\varepsilon^2\), uniformly in \(k\). Therefore \(\max_k|w_{k,\varepsilon}|=O_q(\sqrt\varepsilon)\). Equation (10) shows that \(\sum_kw_{k,\varepsilon}^2\) has the finite limit prescribed by (4), so
\[
\sum_k|w_{k,\varepsilon}|^3
\le\max_k|w_{k,\varepsilon}|\sum_kw_{k,\varepsilon}^2\longrightarrow0.\tag{11}
\]
As the centered exponentials have finite third absolute moment, Lyapunov's argument proves a scalar Gaussian limit; if its limiting variance vanishes, use Chebyshev's inequality. Cramér–Wold yields the joint Gaussian limit. For \(a_i\le a_j\), (10), divided by the normalization factors, gives \(\tfrac32\sqrt{a_i/a_j}-\tfrac12(a_i/a_j)^{3/2}\). Taking \(a_j=e^{h_j}\) yields (4).

**4. Transfer to empirical number variance.** The standard Komlós–Major–Tusnády uniform empirical-process coupling, used in the cited 2026 number-variance work, supplies, for each \(N\), a Brownian bridge \(B_N\) for which the uniform discrepancy error \(D_N\) obeys \(\|D_N\|_\infty=O_{\mathbb P}(\log N)\). Crucially this is one common approximation over all interval endpoints, independent of the choice of \(s\). Expanding the squared increment and using Cauchy–Schwarz gives simultaneously for all selected lengths
\[
\left|\frac{V_N(s)}{N}-H_{N,s}\right|
\le\frac{4\|D_N\|_\infty}{\sqrt N}\sqrt{H_{N,s}}
+\frac{4\|D_N\|_\infty^2}{N},\tag{12}
\]
where \(H_{N,s}=\int_0^1(B_N(x+s)-B_N(x))^2\,dx\). The common bridge has the joint distribution in (9). Since \(\mathbb EH_{N,s}=s(1-s)\), the family \(H_{N,s}/s\) is tight for each selected shrinking length by Markov's inequality. Dividing (12) by \(s^{3/2}\) gives an \(O_{\mathbb P}(\log N/(\sqrt N\,s))\) first term and an \(O_{\mathbb P}((\log N)^2/(Ns^{3/2}))\) second term. Both vanish uniformly over the fixed finite choices \(s=\varepsilon_Ne^{h_j}\) under (2), because \((\log N)^2/(Ns^{3/2})=[\log N/(\sqrt N s)]^2\sqrt s\). Slutsky's lemma transfers the joint Gaussian limit from \(H\) to \(V_N/N\).

**5. Spectrum and scale separation.** The function in (4) is even and depends only on the log-length difference. Using \(\int_{\mathbb R}e^{-a|h|}e^{-i\omega h}\,dh=2a/(a^2+\omega^2)\), its Fourier transform equals (5), which is strictly positive. Hence (4) defines a nondegenerate stationary Gaussian family. The limit \(R(h)\to0\) as \(|h|\to\infty\) proves asymptotic decorrelation at separated log-scales within this limiting family. Only finite-dimensional distribution convergence is claimed.

## Verification

A standalone standard-library Python verifier, `verify_multiscale.py`, performs 121 rational geometry comparisons on a grid of lengths, four Fourier-series versus exact-integral comparisons, and nine scale-correlation/spectral checks (134 tests total). Run `python verify_multiscale.py` in the directory containing the extracted file. Every test printed PASS in the accompanying review. These checks detect factors and endpoint mistakes; they do **not** replace the all-length integration, Lyapunov argument, or empirical-process coupling above.

## Relationship to prior work

Aistleitner, Hörmann, and Manskova (2026) establish a precise scalar number-variance law and almost-sure threshold, and give the one-length variance, the Brownian-bridge Fourier weights, and the KMT bound used here. Their scalar theorem does not state the exact cross-length covariance (1) or the joint mesoscopic Gaussian limit with stationary log-scale kernel (4). The contribution is the **simultaneous** Fourier coupling and its explicit cross-scale limit, rather than a new proof of their marginal theorem.

Aistleitner and Yesha (2025) treat deterministic integer-sequence dilations for almost every dilation parameter, not independent uniform points or their joint mesoscopic fluctuations. Heinrich (2017) proves multiscale limits for expanding-window point-process K-statistics; the displayed limit in his principal scaled theorem is proportional to a single Gaussian count fluctuation and is not the fixed-sample, degenerate-pair, log-scale kernel (4). Lang and Marcon (2013) compute multiscale covariances and Gaussian tests for planar Ripley K-statistics on growing squares; this is close in methodology, but has different spatial dimension, point-count law, statistic, and scale regime, and does not state (1) or (4). General U-statistic machinery may offer other proofs; that possibility is not a claim of method novelty.

## Limitations

The Gaussian limit is proven only for fixed finite sets of log-scales, not process-level tightness, maxima of multiscale scans, or empirical confidence bands. Condition (2) is a sufficient KMT-based rate and may be improvable. The exact formula assumes iid uniform locations and circular geometry; neither nonuniform samples nor interacting point processes are covered. A residual literature-priority risk remains from older spatial-statistics work on multiscale K-functions and integrated pair statistics under other normalizations. There is no claim of an independent audit or published priority.

## References

1. C. Aistleitner, S. Hörmann, and M. Manskova, *On the asymptotic behavior of the number variance of random points on the unit torus*, arXiv:2610.11687v1 (first public 2026-10-08), https://arxiv.org/html/2610.11687v1.
2. C. Aistleitner and N. Yesha, *Almost sure asymptotics for the number variance of dilations of integer sequences*, arXiv:2504.00708v1 (2025), https://arxiv.org/html/2504.00708v1.
3. L. Heinrich, *Asymptotic Goodness-of-Fit Tests for Point Processes Based on Scaled Empirical K-Functions*, arXiv:1706.01074 (2017), https://arxiv.org/abs/1706.01074.
4. G. Lang and E. Marcon, *Testing randomness of spatial point patterns with the Ripley statistic*, ESAIM: Probability and Statistics **17** (2013), 767–788, doi:10.1051/ps/2012027, https://numdam.org/articles/10.1051/ps/2012027/.
