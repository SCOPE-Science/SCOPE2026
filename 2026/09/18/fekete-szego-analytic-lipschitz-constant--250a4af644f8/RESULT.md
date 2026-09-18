# A Fekete–Szegő quantitative strengthening of the analytic Lipschitz metric

## Statement

Let \(\Omega\subset\mathbb C\) be simply connected, and for \(p,q\in\Omega\) define
\[
X_\Omega(p,q)
=
\sup\left\{
|f(p)-f(q)|:
f\in\mathcal O(\Omega),\ \|f'\|_{L^\infty(\Omega)}\le 1
\right\}.
\]
Let \(d_\Omega\) denote the interior path metric. Then
\[
c_0\,d_\Omega(p,q)\le X_\Omega(p,q)\le d_\Omega(p,q)
\qquad (p,q\in\Omega),
\]
where the explicit universal constant
\[
c_0
=
\cos\!\left(
\frac{243}{196}(1+2e^{-4})
\right)
\exp\!\left[
-\frac{18}{7}\sqrt{\sinh(196/81)}
\right]
\]
satisfies
\[
c_0>6.49\times 10^{-4}.
\]

MacMahon's recent theorem proves the same universal bi-Lipschitz comparison with an explicit lower constant about \(1.29\times10^{-42}\). The estimate above improves that explicit constant by more than \(5\times10^{38}\).

The proof also repairs two local slips in the displayed Gaussian-convolution estimate of the source proof: the centered first-order Taylor term has the opposite sign after the substitution \(x=a-s\), and \(\int 8s^2k_\sigma(s)\,ds=8\sigma^2\), not \(4\sigma^2\). At the source choice \(\sigma=1/3\), the corrected error is \(8/9<\pi/3\), so these slips do not invalidate the qualitative theorem or its stated lower constant after the local correction.

## Proof

The upper bound \(X_\Omega\le d_\Omega\) follows immediately by integrating \(f'\) along rectifiable curves. We prove the quantitative lower bound.

Fix \(p,q\in\Omega\). As in the source argument, choose a conformal map
\[
\psi:S\to\Omega,
\qquad
S=\{z\in\mathbb C:|\operatorname{Im}z|<1\},
\]
and real \(a<b\) with \(\psi(a)=p\) and \(\psi(b)=q\). Put
\[
g=\log\psi'=A+iB.
\]
The branch exists because \(\psi'\) has no zeros and \(S\) is simply connected.

### 1. A sharper bound for \(B''\)

For every real \(x\), normalize \(\psi\) on the unit disk centered at \(x\):
\[
\phi_x(\zeta)
=
\frac{\psi(x+\zeta)-\psi(x)}{\psi'(x)}
=
\zeta+a_2\zeta^2+a_3\zeta^3+\cdots .
\]
This is a normalized univalent function on \(\mathbb D\). Hence
\[
g''(x)=6a_3-4a_2^2
=
6\left(a_3-\frac23 a_2^2\right).
\]
The classical sharp Fekete–Szegő inequality
\[
\left|a_3-\mu a_2^2\right|
\le
1+2\exp\!\left(-\frac{2\mu}{1-\mu}\right),
\qquad 0\le\mu<1,
\]
at \(\mu=2/3\) gives
\[
|g''(x)|
\le
M:=6(1+2e^{-4}).
\]
Therefore
\[
|B''(x)|\le M.
\]
The usual Bieberbach estimate \(|a_2|\le2\) also gives
\[
|B'(x)|\le |g'(x)|\le4.
\]

### 2. Gaussian straightening

For \(\sigma>0\), set
\[
k_\sigma(w)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\!\left(-\frac{w^2}{2\sigma^2}\right),
\qquad
G(w)=\int_{\mathbb R}B(x)k_\sigma(w-x)\,dx.
\]
The linear growth of \(B\) makes \(G\) entire. For real \(t\), after writing \(x=t-s\), use the correctly centered Taylor expression
\[
B(t-s)-B(t)+sB'(t).
\]
Since \(\int k_\sigma=1\) and \(\int s\,k_\sigma(s)\,ds=0\),
\[
G(t)-B(t)
=
\int_{\mathbb R}
\bigl(B(t-s)-B(t)+sB'(t)\bigr)k_\sigma(s)\,ds.
\]
Taylor's theorem and the bound for \(B''\) yield
\[
|G(t)-B(t)|
\le
\frac M2\int_{\mathbb R}s^2k_\sigma(s)\,ds
=
\frac M2\sigma^2
=
3(1+2e^{-4})\sigma^2.
\]
Write
\[
E_\sigma:=3(1+2e^{-4})\sigma^2.
\]

### 3. A sharper strip bound for \(\operatorname{Im}G\)

Let \(w=t+ib\in S\). Since \(\int_{\mathbb R}\operatorname{Im}k_\sigma(s+ib)\,ds=0\) and
\(|B(t-s)-B(t)|\le4|s|\),
\[
|\operatorname{Im}G(w)|
\le
4\int_{\mathbb R}|s|\,
|\operatorname{Im}k_\sigma(s+ib)|\,ds.
\]
Put \(r=|b|/\sigma\), and let \(Z\) be a standard real Gaussian. The exact imaginary part of the Gaussian kernel gives
\[
|\operatorname{Im}G(w)|
\le
4\sigma e^{r^2/2}
\mathbb E\!\left[|Z|\,|\sin(rZ)|\right].
\]
By Cauchy–Schwarz,
\[
\mathbb E\!\left[|Z|\,|\sin(rZ)|\right]
\le
\sqrt{\mathbb E Z^2\;\mathbb E\sin^2(rZ)}
=
\sqrt{\frac{1-e^{-2r^2}}2}.
\]
Consequently
\[
|\operatorname{Im}G(w)|
\le
4\sigma\sqrt{\sinh(r^2)}
\le
4\sigma\sqrt{\sinh(\sigma^{-2})}
=:\lambda_\sigma,
\]
because \(|b|<1\).

### 4. Constructing the bounded-derivative analytic function

Assume \(E_\sigma<\pi/2\), and define on \(S\)
\[
h(z)=\psi'(z)e^{-\lambda_\sigma-iG(z)}.
\]
Since \(|\operatorname{Im}G|\le\lambda_\sigma\),
\[
|h(z)|\le|\psi'(z)|.
\]
If
\[
F(w)=\int_a^w h(\zeta)\,d\zeta,
\qquad
f=F\circ\psi^{-1},
\]
then \(f\in\mathcal O(\Omega)\) and \(|f'|\le1\).

On the real axis, \(G\) is real and
\[
|B(t)-G(t)|\le E_\sigma<\frac\pi2.
\]
Hence
\[
\operatorname{Re}h(t)
\ge
\cos(E_\sigma)e^{-\lambda_\sigma}|\psi'(t)|.
\]
Therefore
\[
|f(p)-f(q)|
\ge
\cos(E_\sigma)e^{-\lambda_\sigma}
\int_a^b|\psi'(t)|\,dt
\ge
\cos(E_\sigma)e^{-\lambda_\sigma}d_\Omega(p,q).
\]

Thus every admissible \(\sigma\) gives the universal lower constant
\[
c(\sigma)
=
\cos\!\bigl(3(1+2e^{-4})\sigma^2\bigr)
\exp\!\left[-4\sigma\sqrt{\sinh(\sigma^{-2})}\right].
\]

Taking
\[
\sigma=\frac9{14}
\]
gives
\[
E_\sigma
=
\frac{243}{196}(1+2e^{-4})
<\frac\pi2,
\qquad
\lambda_\sigma
=
\frac{18}{7}\sqrt{\sinh(196/81)},
\]
and hence the stated constant \(c_0>6.49\times10^{-4}\).

## Verification

The exact proof is analytic. The accompanying script evaluates only the final explicit expressions and checks the stated decimal lower bound.

## Originality scope

The recent source establishes the universal comparison \(X_\Omega\asymp d_\Omega\) and supplies the Gaussian-straightening mechanism. The classical Fekete–Szegő inequality is also prior art. The new claim is the quantitative synthesis: replacing the coarse second-derivative estimate by the sharp Fekete–Szegő coefficient bound, sharpening the strip estimate by a Gaussian Cauchy–Schwarz calculation, correcting the centered Taylor calculation, and obtaining the explicit lower constant above.

Searches for the source title and identifier together with Fekete–Szegő, pre-Schwarzian second derivatives, analytic Lipschitz metrics, bounded-derivative holomorphic metrics, and quantitative inner-metric constants located no prior version of this refinement.

## Limitations

No claim is made that \(c_0\) is the optimal universal constant, or even the best constant obtainable from every possible straightening kernel. The choice \(\sigma=9/14\) is a convenient explicit value; numerical optimization within the displayed Gaussian/Fekete–Szegő bound improves it only slightly, to about \(6.494\times10^{-4}\). The argument is restricted to simply connected planar domains, exactly as in the source metric theorem.

## References

1. C. MacMahon, *On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded Derivative*, arXiv:2609.20607v1 (2026).
2. J. H. Choi, Y. C. Kim, T. Sugawa, *A general approach to the Fekete–Szegő problem*, J. Math. Soc. Japan 59 (2007), 707–727, doi:10.2969/jmsj/05930707. The introduction records the classical sharp Fekete–Szegő inequality for normalized univalent functions.
