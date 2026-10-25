# The sharp \(\pi/N\) Gaussian covariance transition on discrete circles

## Finding
For an integer \(N\ge3\), let the intrinsic cyclic distance on \(\mathbb Z/N\mathbb Z\) be
\[
d_N(j,k)=\min\{|j-k|,N-|j-k|\}.
\]
For \(c>0\), consider the real symmetric kernel
\[
K_{N,c}(j,k)=\exp\!\left(-\frac{c}{N}d_N(j,k)^2\right).
\]
Then for each fixed \(c>\pi\), this kernel is strictly positive definite for all sufficiently large \(N\). For each fixed \(0<c<\pi\), it has a strictly negative eigenvalue for all sufficiently large \(N\), specifically at character frequency \(k_N=2\lfloor N/4\rfloor\). Thus \(\pi/N\) is the sharp asymptotic scale for the Gaussian coefficient multiplying squared *graph* distance.

There is also a resolved logarithmic transition window. Set
\[
C_*=2\log\!\left(\frac{2}{\tanh(\pi/2)}\right),\qquad
c_N(s)=\pi-\frac{\log N+s}{N}.
\]
For \(N\) divisible by four, let \(\Lambda_{N,N/2}(c)\) be the Nyquist eigenvalue of \(K_{N,c}\). For every fixed real \(s\),
\[
\lim_{\substack{N\to\infty\\4\mid N}}e^{c_N(s)N/4}\Lambda_{N,N/2}(c_N(s))
=2e^{-s/2}-\tanh(\pi/2).
\]
Consequently, for all sufficiently large multiples of four, the Nyquist eigenvalue has at least one zero at a parameter satisfying
\[
c_N=\pi-\frac{\log N+C_*+o(1)}{N}.
\]
This is a local zero-crossing statement, not a claim that all finite-size admissibility sets have a unique threshold.

For \(N\) equally spaced points on the unit circle with genuine arc-distance \(2\pi d_N/N\), the corresponding geometric Gaussian coefficient is \(\lambda=cN/(4\pi^2)\). In these physical units, the asymptotic transition is at \(\lambda/N=1/(4\pi)\).

## Assumptions and scope
The points are all vertices of the undirected cycle and all pairwise distances are shortest-path distances, not Euclidean chordal distances. The integer \(N\) tends to infinity and \(c>0\) is fixed in the first two assertions. The boundary value \(c=\pi\) is not classified. In the logarithmic window, \(N\) is divisible by four and \(s\in\mathbb R\) is fixed. Positive definiteness means nonnegative Hermitian quadratic forms for all complex coefficient vectors; strict positive definiteness means all eigenvalues are positive.

## Proof
**1. Positive Gaussian periodization.** Write \(t=c/N\), \(\theta_k=2\pi k/N\), and let
\[
F_N(j)=e^{-t d_N(j,0)^2},\quad P_N(j)=\sum_{\ell\in\mathbb Z}e^{-t(j+\ell N)^2},\quad E_N(j)=P_N(j)-F_N(j)\ge0.
\]
(The last inequality is pointwise, not a claim about Fourier signs.) Circulant diagonalization gives the eigenvalues \(\Lambda_{N,k}=\sum_{j=0}^{N-1}F_N(j)e^{-i\theta_kj}\). Gaussian Poisson summation gives, **with this unnormalized Fourier convention**, the exact positive series
\[
\widehat P_N(k)
=\sqrt{\frac{\pi N}{c}}
\sum_{\ell\in\mathbb Z}
\exp\!\left[-\frac{\pi^2N}{c}\left(\frac{k}{N}-\ell\right)^2\right],
\quad\Lambda_{N,k}=\widehat P_N(k)-\widehat E_N(k).
\]
For every \(k\), some integer \(\ell\) is at distance at most \(1/2\) from \(k/N\). Therefore
\[
\widehat P_N(k)\ge\sqrt{\frac{\pi N}{c}}\exp\!\left(-\frac{\pi^2N}{4c}\right).
\]

**2. Global bound on the folding defect.** Choose one closest integer representative in every residue class. Every omitted Gaussian image is at absolute distance at least \(N/2\), and, for each representative, at most two omitted images lie in each successive annulus of width \(N\). Consequently, for a constant \(A_c\) depending only on fixed \(c>0\),
\[
\max_k|\widehat E_N(k)|
\le \sum_{j\bmod N} E_N(j)
\le A_c N\exp\!\left(-\frac{cN}{4}\right).
\]
A concrete bound for all sufficiently large \(N\) is obtained from \(2N\sum_{h\ge0}\exp[-cN(h+1/2)^2]\). If \(c>\pi\), the lower bound in Step 1 dominates this defect, since \(c/4>\pi^2/(4c)\). Hence all \(\Lambda_{N,k}>0\) for sufficiently large \(N\).

**3. A negative high-frequency eigenvalue.** For fixed \(0<c<\pi\), choose the *even* integer \(k_N=2\lfloor N/4\rfloor\) and put \(\theta_N=2\pi k_N/N\). Then \(\theta_N\to\pi\), and the positive periodized Gaussian obeys
\[
\widehat P_N(k_N)=O_c\!\left(\sqrt N\,e^{-\pi^2N/(4c)}\right),
\]
where the suppressed factor may depend on \(c\), because \(k_N/N=1/2+O(1/N)\). We now show that \(\widehat E_N(k_N)>0\) and has a slower exponential decay.

If \(N=2m\) is even, center residues at the antipode \(m\). The additional nearest Gaussian image contributes, uniformly for bounded nonnegative offsets \(u\),
\[
e^{-cN/4}e^{-cu-cu^2/N},
\]
with one contribution at \(u=0\) and two at each \(u\ge1\). All other images contribute \(o(e^{-cN/4})\) in total. Since \(k_N\) is even and \(\theta_N\to\pi\), dominated convergence gives
\[
\frac{\widehat E_N(k_N)}{e^{-cN/4}}
\longrightarrow
1+2\sum_{u=1}^{\infty}(-1)^u e^{-cu}
=\tanh(c/2)>0.
\]
If \(N=2m+1\) is odd, put \(\delta_N=\pi-\theta_N=\pi(N-2k_N)/N\), where \(N-2k_N\) equals \(1\) or \(3\). The two antipodal image tails, indexed by \(u=0,1,\ldots,m\), give
\[
\widehat E_N(k_N)
=2e^{-cN/4}\sum_{u=0}^{m}
 e^{-c(u+1/2)}e^{-c(u+1/2)^2/N}
\cos[\theta_N(u+1/2)]+O_c(Ne^{-cN}).
\]
Here \(\cos[(\pi-\delta_N)(u+1/2)]=(-1)^u\sin[\delta_N(u+1/2)]\); the factor \((-1)^{k_N}\) is one. Dividing by \(\delta_N e^{-cN/4}\), using \(|\sin z|\le|z|\), and applying dominated convergence yields
\[
\frac{\widehat E_N(k_N)}{\delta_N e^{-cN/4}}
\longrightarrow
2e^{-c/2}\sum_{u=0}^{\infty}(-1)^u(u+1/2)e^{-cu}
= e^{-c/2}\frac{1-e^{-c}}{(1+e^{-c})^2}>0.
\]
Thus for even \(N\), the defect is positive of order \(e^{-cN/4}\), and for odd \(N\) it is positive of order \(N^{-1}e^{-cN/4}\). Since \(c<\pi\) is equivalent to \(\pi^2/(4c)>c/4\), the exponentially smaller positive term \(\widehat P_N(k_N)\) cannot cancel the defect. Therefore \(\Lambda_{N,k_N}<0\) for all sufficiently large \(N\) in every parity class.

**4. Nyquist logarithmic window.** Let \(4\mid N\), so \(k=N/2\) is even. Uniformly for \(c\) in a fixed compact neighborhood of \(\pi\), the even-case computation refines to
\[
\widehat E_N(N/2)=e^{-cN/4}\bigl[\tanh(c/2)+O(N^{-1})\bigr].
\]
At Nyquist, the two nearest terms in the Poisson series are equal, yielding
\[
\widehat P_N(N/2)
=2\sqrt{\frac{\pi N}{c}}e^{-\pi^2N/(4c)}
\bigl[1+O(e^{-2\pi^2N/c})\bigr].
\]
Take \(c=c_N(s)=\pi-(\log N+s)/N\) with fixed \(s\). Then
\[
2\sqrt{\frac{\pi N}{c}}\exp\!\left[\frac N4\left(c-\frac{\pi^2}{c}\right)\right]
\longrightarrow 2e^{-s/2},
\]
while \(\tanh(c/2)\to\tanh(\pi/2)\). Subtracting gives the asserted limit. It is positive for \(s<C_*\) and negative for \(s>C_*\). Continuity of the eigenvalue in \(c\), followed by bracketing with \(s=C_*\pm\varepsilon\) for every \(\varepsilon>0\), produces a zero \(c_N=\pi-(\log N+C_*+o(1))/N\). No assertion about other roots away from the logarithmic window is needed. \(\square\)

## Verification
The standalone `verify.py` evaluates the exact cycle Fourier sums at high precision; separately evaluates the Gaussian Poisson formula and omitted-image correction; checks positivity of *every* Fourier eigenvalue at selected supercritical values; checks high-frequency negative witnesses in all four congruence classes; and compares the numerically located Nyquist zeros with \(C_*\). The maximum discrepancy in the independent finite Poisson/image identities over the specified tests is less than \(10^{-70}\). These are finite checks and do not replace the analytic asymptotics proved above.

## Relationship to prior work
Feragen--Lauze--Hauberg (2014, arXiv:1411.0296) give geometric obstructions to all-parameter validity of geodesic Gaussian kernels, rather than a scale-dependent theorem for equal cyclic samples. Wood (1995) studies when truncated stationary covariance functions extend to continuous circles, not an asymptotic for the smallest damping that makes a sequence of finite cyclic Gram matrices positive. Da Costa--Mostajeran--Ortega (2023, arXiv:2302.10623, especially Section 4 and the final discussion) prove that no fixed geodesic Gaussian scale works on the *entire* circle and use alternating Fourier modes at increasingly fine even grids. Their fixed-scale asymptotics correspond to \(c\to0\) here; their argument does not state the sharp \(c=\pi\) transition when the scale grows with sample count, nor the \(\log N/N\) correction. The new claim neither contradicts nor strengthens a false finite-\(N\) assertion: positivity holds only at a moving Gaussian scale and only on the sampled grid.

## Limitations
The result is asymptotic as \(N\to\infty\), not an exact positivity threshold for each finite \(N\). The boundary \(c=\pi\) is not settled by the fixed-parameter dichotomy. The logarithmic correction is proved for the Nyquist eigenvalue along \(4\mid N\), not as a globally unique critical value. It does not address nonuniformly spaced circular samples or arbitrary finite graphs. One older closely related source (Wood 1995) was compared by its bibliographic record and abstract, not its inaccessible complete article; this leaves a bounded originality risk.

## References
1. A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, first public arXiv version 2014-11-02, arXiv:1411.0296, https://arxiv.org/abs/1411.0296 .
2. N. Da Costa, C. Mostajeran, J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (2023), https://arxiv.org/html/2302.10623v1 .
3. A. T. A. Wood, *When is a truncated covariance function on the line a covariance function on the circle?*, Statistics & Probability Letters **24** (1995), 157--164, DOI:10.1016/0167-7152(94)00162-2 .
4. I. J. Schoenberg, *Metric Spaces and Positive Definite Functions*, Transactions of the AMS **44** (1938), 522--536.
