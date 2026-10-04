# Exact three-frequency Fourier projection norm on every cyclic group
## Finding
For every integer \(N\ge3\), let \(P_N\) be the Fourier projection on functions on \(\mathbb Z_N\), with normalized counting measure, onto any three consecutive characters. Modulation reduces the frequency set to \(\{-1},0,1\}\). Its convolution kernel is
\[
K_N(k)=1+2\cos\!\left(\frac{2\pi k}N\right),\qquad k\in\mathbb Z_N.
\]
The exact endpoint operator norm is
\[
\|P_N\|_{\ell^\infty\to\ell^\infty}=\|P_N\|_{\ell^1\to\ell^1}=\Lambda_N
=\frac1N\sum_{k=0}^{N-1}\left|1+2\cos\!\left(\frac{2\pi k}N\right)\right|.
\]
Writing \(N=3m+r\), with \(r\in\{0,1,2\}\), this average has the closed form
\[
\Lambda_N=
\begin{cases}
\displaystyle \frac13+\frac{2\sqrt3}N\cot\!\left(\frac\pi N\right),&r=0,\\[2mm]
\displaystyle \frac{m+1+4\,\sin(m\pi/N)/\sin(\pi/N)}N,&r=1,\\[2mm]
\displaystyle \frac{m+4\,\sin((m+1)\pi/N)/\sin(\pi/N)}N,&r=2.
\end{cases}
\]
Consequently
\[
\Lambda_N\longrightarrow \frac13+\frac{2\sqrt3}\pi,
\]
the continuous-torus \(L^1\) norm of \(1+2\cos(2\pi x)\).

## Assumptions and scope
The group is \(\mathbb Z_N\) with normalized counting measure \(N^{-1}\sum_x\). The Fourier projection is onto a set \(\{a-1},a,a+1\}\subset\widehat{\mathbb Z_N}\); for \(N=3\) this is the whole dual group and the formula gives \(\Lambda_3=1\). For \(N\ge4\) the three characters are distinct. Translation of the frequency set only modulates the kernel, so its absolute values and the endpoint operator norms are unchanged.

The statement is an exact finite-group result. It does not assert a formula for projections onto four or more consecutive characters, nor for interior \(\ell^p\)-operator norms.

## Proof
For the centered frequency set \(\{-1},0,1\}\), Fourier inversion gives
\[
(P_Nf)(x)=\frac1N\sum_{y\in\mathbb Z_N}K_N(y)f(x-y),
\qquad
K_N(y)=1+2\cos\!\left(\frac{2\pi y}N\right).
\]
Hence Young's inequality gives \(\|P_N\|_{\ell^\infty\to\ell^\infty}\le N^{-1}\sum_y|K_N(y)|\). Equality holds by choosing \(f(-y)\) to have the sign of \(K_N(y)\) at all nonzero kernel values and evaluating at \(x=0\). By finite-dimensional duality, the same number is the \(\ell^1\to\ell^1\) norm.

It remains to evaluate the absolute sum. Put \(\alpha=\pi/N\). Since \(1+2\cos(2\pi k/N)<0\) exactly when \(N/3<k<2N/3\), let \(I_N\) be the corresponding integer interval. The ordinary kernel sum is
\[
\sum_{k=0}^{N-1}K_N(k)=N,
\]
so if \(S_N=\sum_{k\in I_N}K_N(k)\), then
\[
\sum_{k=0}^{N-1}|K_N(k)|=N-2S_N.
\]
For consecutive integers \(a\le b\),
\[
\sum_{k=a}^b\cos(2k\alpha)
=\frac{\sin((b-a+1)\alpha)\cos((a+b)\alpha)}{\sin\alpha}.
\]
In all three residue classes below, the relevant endpoints satisfy \(a+b=N\), so \(\cos((a+b)\alpha)=\cos\pi=-1\).

If \(N=3m\), then \(I_N=\{m+1,\ldots,2m-1\}\), hence
\[
S_N=(m-1)-\frac{2\sin((m-1)\alpha)}{\sin\alpha}
=m-\sqrt3\cot\alpha.
\]
Therefore \(N-2S_N=m+2\sqrt3\cot\alpha\), giving the first formula.

If \(N=3m+1\), then \(I_N=\{m+1,\ldots,2m\}\), so
\[
S_N=m-\frac{2\sin(m\alpha)}{\sin\alpha},
\]
and therefore
\[
N-2S_N=m+1+\frac{4\sin(m\alpha)}{\sin\alpha}.
\]
This is the second formula.

If \(N=3m+2\), then \(I_N=\{m+1,\ldots,2m+1\}\), so
\[
S_N=m+1-\frac{2\sin((m+1)\alpha)}{\sin\alpha},
\]
and hence
\[
N-2S_N=m+\frac{4\sin((m+1)\alpha)}{\sin\alpha}.
\]
This gives the third formula.

Finally, either the closed forms or the Riemann-sum interpretation yield
\[
\lim_{N\to\infty}\Lambda_N=\int_0^1|1+2\cos(2\pi x)|\,dx.
\]
The integrand changes sign at \(x=1/3\) and \(x=2/3\), and direct integration gives
\[
\int_0^1|1+2\cos(2\pi x)|\,dx
=\frac13+\frac{2\sqrt3}\pi.
\]

## Verification
The accompanying `verify.py` independently evaluates the sampled absolute sum and the residue-class closed form for every \(3\le N\le5000\). It also checks the predicted negative-index interval and the continuous limiting constant numerically at large \(N\). The analytic proof above, not this finite calculation, establishes the theorem for all \(N\).

## Relationship to prior work
Anderson, Ash, Jones, Rider and Saffari treat idempotent trigonometric polynomials on the continuous torus. Their arXiv paper defines the Dirichlet kernel as a basic idempotent and studies continuous \(L^p\) concentration and continuous Dirichlet-kernel norm asymptotics. The inspected full text does not state the finite cyclic sampled endpoint projection norm or the three residue-class formula proved here.

Gilbert and Rzeszotnik determine \(L^p\)-to-\(L^q\) norms of the full Fourier transform on finite abelian groups. A spectral projection onto three prescribed characters is a different operator: its endpoint norm is the normalized \(\ell^1\) norm of a particular idempotent convolution kernel, and the cited full-transform norm theorem does not imply the displayed finite-grid evaluation.

Targeted searches for finite cyclic Lebesgue constants, sampled three-term Dirichlet-kernel norms, and three-consecutive-frequency projection norms did not locate a statement implying the formula above. This is evidence for, not a proof of, originality.

## Limitations
The result concerns only three consecutive characters and endpoint \(\ell^1\) and \(\ell^\infty\) norms. No claim is made for longer Dirichlet projections or for \(1<p<\infty\). A residual originality risk remains that the same elementary finite trigonometric sum appears in older approximation-theory or numerical Fourier literature under different terminology.

## References
1. B. Anderson, J. Marshall Ash, R. Jones, D. G. Rider, B. Saffari, “Exponential sums with coefficients 0 or 1 and concentrated \(L^p\) norms,” arXiv:0705.0636v1, first posted 2007-05-04; published in *Annales de l'Institut Fourier* 57 (2007). Primary MSC 42A05.
2. J. Gilbert, Z. Rzeszotnik, “The norm of the Fourier transform on finite abelian groups,” *Annales de l'Institut Fourier* 60 (2010), 1317–1346, DOI 10.5802/aif.2556.
