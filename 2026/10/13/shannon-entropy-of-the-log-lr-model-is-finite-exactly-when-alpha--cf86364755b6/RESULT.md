# Shannon entropy of the Log-LR model is finite exactly when \(\alpha>1\)
## Finding
For the logarithmic Lomax–Rayleigh model with parameters \(\alpha,\beta,\lambda>0\), let
\[
F_R(x)=1-\exp\!\left(-\frac{x^2}{2\lambda^2}\right)
\]
be the Rayleigh baseline CDF and
\[
G(x)=\left(\frac{\beta}{\beta-\log F_R(x)}\right)^\alpha
\]
be the Log-LR CDF.

Define the monotone transform
\[
T=-\log F_R(X).
\]
Then \(T\) is exactly Lomax with shape \(\alpha\) and scale \(\beta\):
\[
\Pr(T>t)=\left(\frac{\beta}{\beta+t}\right)^\alpha,
\qquad t>0.
\]
Consequently the differential Shannon entropy of \(X\) is finite exactly in the regime
\[
\boxed{\alpha>1}.
\]
For every \(0<\alpha\le1\),
\[
\boxed{H(X)=-\infty}.
\]

This is an integrability boundary absent from the published entropy discussion. The source writes the entropy as a sum of expectations and says those expectations are evaluated numerically, but for \(0<\alpha\le1\) some displayed expectations are not finite and the Shannon entropy itself has the extended value \(-\infty\).

When \(\alpha>1\), two of the source's expectations are explicit:
\[
\mathbb E[\log F_R(X)]
=-\frac{\beta}{\alpha-1},
\]
and, with \(\eta(X)=\beta-\log F_R(X)\),
\[
\mathbb E[\log \eta(X)]
=\log\beta+\frac1\alpha.
\]
Thus the published entropy expression simplifies to
\[
H(X)
=
\log\!\left(\frac{\beta\lambda^2}{\alpha}\right)
+1+\frac1\alpha
-\mathbb E[\log X]
+\frac{\mathbb E[X^2]}{2\lambda^2}
-\frac{\beta}{\alpha-1},
\qquad \alpha>1.
\]

## Assumptions and scope
The parameters satisfy \(\alpha,\beta,\lambda>0\), and logarithms are natural. Differential entropy is interpreted in the standard extended-real sense
\[
H(X)=-\int_0^\infty g(x)\log g(x)\,dx.
\]
The finding classifies finiteness of this integral. It does not assert an elementary closed form for the remaining finite expectations when \(\alpha>1\).

The conclusion \(H(X)=-\infty\) for \(0<\alpha\le1\) is not obtained by subtracting divergent terms in the source's entropy decomposition. It is derived directly from a one-to-one change of variables and the asymptotics of the Jacobian.

## Proof
For \(t>0\), because \(F_R\) is strictly increasing,
\[
\begin{aligned}
\Pr(T>t)
&=\Pr\{-\log F_R(X)>t\}\\
&=\Pr\{F_R(X)<e^{-t}\}\\
&=G\!\left(F_R^{-1}(e^{-t})\right)\\
&=\left(\frac{\beta}{\beta+t}\right)^\alpha.
\end{aligned}
\]
Hence \(T\) has Lomax density
\[
f_T(t)=\frac{\alpha\beta^\alpha}{(\beta+t)^{\alpha+1}},
\qquad t>0.
\]
Its differential entropy is finite for every \(\alpha,\beta>0\) and equals
\[
H(T)=\log\!\left(\frac{\beta}{\alpha}\right)+1+\frac1\alpha.
\]

Solving \(t=-\log F_R(x)\) for \(x\) gives
\[
x(t)=\lambda\sqrt{-2\log(1-e^{-t})}.
\]
The absolute Jacobian is
\[
J(t)=\left|\frac{dx}{dt}\right|
=
\frac{\lambda}{(e^t-1)\sqrt{-2\log(1-e^{-t})}}.
\]
For a smooth one-to-one transformation, entropy changes by the expected log-Jacobian, interpreted by truncation when necessary:
\[
H(X)=H(T)+\mathbb E[\log J(T)].
\]

As \(t\to\infty\),
\[
-\log(1-e^{-t})=e^{-t}(1+o(1)),
\]
so
\[
J(t)=\frac{\lambda}{\sqrt2}e^{-t/2}(1+o(1))
\]
and therefore
\[
\log J(t)
=-\frac t2+\log\!\left(\frac{\lambda}{\sqrt2}\right)+o(1).
\]
At the other endpoint, as \(t\downarrow0\),
\[
J(t)
\sim
\frac{\lambda}{t\sqrt{2\log(1/t)}},
\]
so
\[
\log J(t)
=-\log t-\frac12\log\!\bigl(2\log(1/t)\bigr)+O(1).
\]
Because the Lomax density is bounded near \(0\), the positive part of \(\log J(T)\) is integrable there. In the right tail, the negative part is asymptotic to \(T/2\). Thus
\[
\mathbb E[\log J(T)]>-\infty
\]
if and only if \(\mathbb E[T]<\infty\). For a Lomax variable this is equivalent to \(\alpha>1\), with
\[
\mathbb E[T]=\frac{\beta}{\alpha-1}.
\]
Therefore \(H(X)\) is finite exactly when \(\alpha>1\), and equals \(-\infty\) for \(0<\alpha\le1\).

Finally,
\[
\log F_R(X)=-T,
\]
so for \(\alpha>1\),
\[
\mathbb E[\log F_R(X)]=-\frac{\beta}{\alpha-1}.
\]
Also let
\[
U=\frac{\beta}{\beta+T}.
\]
Then \(\Pr(U\le u)=u^\alpha\) on \((0,1)\), so \(U\) has Beta\((\alpha,1)\) density. Since \(\beta+T=\beta/U\),
\[
\mathbb E[\log(\beta+T)]
=\log\beta-\mathbb E[\log U]
=\log\beta+\frac1\alpha.
\]
This yields the stated simplification of the source's entropy formula.

## Verification
The included checker performs four independent consistency tests from the exact formulas:

1. it checks the transformation identity between the Log-LR CDF and the Lomax survival at several \(t\)-values;
2. it verifies numerically that \(\log J(t)/t\to-1/2\);
3. for \(\alpha>1\), it numerically integrates the Lomax density to reproduce \(\mathbb E[T]=\beta/(\alpha-1)\) and \(\mathbb E[\log(\beta+T)]=\log\beta+1/\alpha\);
4. for \(\alpha\le1\), it verifies that increasingly large truncated log-Jacobian expectations move downward consistently with the analytic divergence.

The numerical calculations are checks only. The finiteness classification is proved by the exact transformation and endpoint estimates above.

## Relationship to prior work
Alomari's 2026 paper defines the Log-LR model, writes the Shannon entropy as a sum of expectations, and states that the expectations involved do not admit tractable closed forms and are evaluated numerically. It does not state a parameter restriction for entropy finiteness.

Sapkota, Kumar, Gemeay, Bakr, Balogun, and Muse introduced the underlying Lomax-G generator in 2023, with general CDF
\[
G(x)=\beta^\alpha[\beta-\log B(x)]^{-\alpha}.
\]
That generator immediately makes \(-\log B(X)\) a Lomax variable, but the inspected paper develops a different inverse-exponential-power specialization and does not state the Log-LR Shannon-entropy boundary proved here.

Focused literature searches were performed using the target DOI, the Log-LR name, Shannon-entropy finiteness, the transformed Lomax variable, and the threshold \(\alpha=1\). No published correction or equivalent model-specific theorem was located.

## Limitations
The finding does not provide an elementary closed form for the finite entropy when \(\alpha>1\). It classifies existence and evaluates two expectations that the source leaves numerical.

No claim is made about Rényi or Tsallis entropy for the Log-LR model; those require separate integrability analysis.

A later or unindexed note could contain the same observation under the general Lomax-G transformation. The literature comparison therefore supports originality but does not constitute a proof of bibliographic uniqueness.

## References
1. H. M. Alomari, “A new logarithmic Lomax–Rayleigh distribution: properties, simulation, and applications,” AIMS Mathematics 11 (2026), 19593–19632. DOI: 10.3934/math.2026796.
2. L. P. Sapkota, V. Kumar, A. M. Gemeay, M. E. Bakr, O. S. Balogun, and A. H. Muse, “New Lomax-G family of distributions: Statistical properties and applications,” AIP Advances 13 (2023), 095128. DOI: 10.1063/5.0171949.
