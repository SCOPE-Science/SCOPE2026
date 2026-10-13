# Convex NVHS*-CD hybridization cannot realize conjugacy on a scalar quadratic under inexact strong Wolfe steps
## Finding
Consider the source method on the one-dimensional positive quadratic
\[
f(x)=\frac{a}{2}x^2,\qquad a>0,
\]
from any \(x_0\ne0\). The source initializes \(g_0=ax_0\) and \(d_0=-g_0\). Put \(\tau=a\alpha_0\) and \(r=1-\tau\), so \(x_1=rx_0\).

For every nonexact strong-Wolfe first step allowed by the source, the coefficient that would enforce the source's stated conjugacy condition lies outside the convex hull of the two coefficients that the method is allowed to combine. More precisely,
\[
\beta_{\rm conj}=-r,\qquad \beta_{\rm CD}=r^2,
\]
and
\[
\beta_{\rm NVHS^*}=
\begin{cases}
0,&r>0,\\
\dfrac{2r^2}{1-r},&r<0.
\end{cases}
\]
Therefore no \(\theta\in[0,1]\) can make \(\beta=(1-\theta)\beta_{\rm NVHS^*}+\theta\beta_{\rm CD}\) satisfy \(d_1^{\mathsf T}y_0=0\) unless \(r=0\). The raw interpolation parameter is in fact
\[
\theta_{\rm raw}=-\frac{1}{|r|}<0.
\]
The clipping rule in the published algorithm consequently chooses \(\theta_0=0\) at every nonterminal scalar quadratic first step, so the advertised hybridization collapses to the NVHS* endpoint and does not realize conjugacy.

## Assumptions and scope
The statement concerns the first update of the published algorithm, with its initialization \(d_0=-g_0\), its strong Wolfe parameters \(0<\delta<\sigma<1/3\), and its published convex-combination/clipping rule. The objective is the scalar strictly convex quadratic above. This is a condition-one positive-curvature model, so no ill-conditioning, nonconvexity, or nonsmoothness is involved.

The exact step \(\tau=1\) is excluded from the nonterminal statement because it gives \(x_1=0\) and \(g_1=0\). An admissible nonexact step always exists: for example \(\tau=1-\sigma/2\).

## Proof
The first step gives
\[
g_0=ax_0,\quad d_0=-ax_0,\quad x_1=(1-\tau)x_0=rx_0,\quad g_1=arx_0,
\]
and
\[
y_0=g_1-g_0=-a\tau x_0,\qquad d_0^{\mathsf T}y_0=a^2\tau x_0^2>0.
\]
The strong-Wolfe curvature inequality becomes
\[
|g_1^{\mathsf T}d_0|\le -\sigma g_0^{\mathsf T}d_0
\quad\Longleftrightarrow\quad |r|\le\sigma.
\]
The Armijo inequality reduces to \(\tau\le2(1-\delta)\). Because \(0<\delta<\sigma<1/3\), one has \(1+\sigma<2(1-\delta)\). Hence the entire interval \(\tau\in[1-\sigma,1+\sigma]\) is strong-Wolfe admissible.

For a generic coefficient \(\beta\), the next direction is \(d_1=-g_1+\beta d_0\). Enforcing \(d_1^{\mathsf T}y_0=0\) therefore requires
\[
\beta_{\rm conj}=\frac{g_1^{\mathsf T}y_0}{d_0^{\mathsf T}y_0}=-r.
\]
The published CD coefficient gives \(\beta_{\rm CD}=r^2\). Substitution in the published NVHS* coefficient gives
\[
\beta_{\rm NVHS^*}=\frac{r(r-|r|)}{\tau}.
\]
If \(r>0\), then \(\beta_{\rm NVHS^*}=0\) while \(\beta_{\rm conj}=-r<0\); the target is below both endpoints. If \(r<0\), put \(s=-r\in(0,\sigma]\). Then
\[
\beta_{\rm CD}=s^2,\qquad
\beta_{\rm NVHS^*}=\frac{2s^2}{1+s},\qquad
\beta_{\rm conj}=s.
\]
Since \(0<s<1\),
\[
s^2<\frac{2s^2}{1+s}<s,
\]
so the target is above both endpoints. Thus the target is outside the convex hull for every \(r\ne0\).

Solving the affine interpolation equation for the unconstrained weight yields \(\theta_{\rm raw}=-1/|r|\) in both sign cases. The source's clipping therefore sets \(\theta_0=0\), proving the stated collapse.

## Verification
The bundled script `artifacts/verify.py` checks the exact formulas with rational arithmetic over representative understeps and oversteps, verifies the strong-Wolfe inequalities, reconstructs the target and endpoint coefficients, and confirms \(\theta_{\rm raw}=-1/|r|\). Its recorded output is `VERIFY_OK`.

The all-parameter conclusion does not depend on the finite replay: it follows from the inequalities in the proof.

## Relationship to prior work
The 2026 primary paper defines the NVHS*-CD convex combination, derives a raw weight from the conjugacy equation, clips that weight to \([0,1]\), and states that the parameter is chosen to satisfy conjugacy. The calculation above shows that, on the canonical scalar positive quadratic, the desired coefficient is never in the permitted convex hull for a nonexact strong-Wolfe step.

Djordjević's 2017 LS-CD convex-combination method uses a related clipping construction. On the same scalar quadratic its LS-CD pair behaves differently: for an overstep, the conjugacy target lies between the LS and CD endpoints. Thus that predecessor does not imply the source-specific conclusion that every nonexact scalar step forces endpoint collapse. The 2025 NPRP-DY convex-combination paper by three of the same authors explicitly notes that its raw weight can leave \([0,1]\) and then clips it, but it uses different endpoint coefficients and does not establish the NVHS*-CD endpoint-order obstruction proved here.

## Limitations
This result isolates the conjugacy mechanism at the first update. It does not claim that the published method loses sufficient descent, that its iterates diverge, or that its global convergence theorem is false. It also does not characterize higher-dimensional trajectories. The obstruction is specifically that a convex combination of the published NVHS* and CD coefficients cannot realize the stated conjugacy target on any nonexact first strong-Wolfe step of the scalar positive quadratic.

## References
1. A. E. Mehamdia, Y. Chaib, T. Bechouat, Z. Raouf, “Another hybrid conjugate gradient method as a convex combination of NVHS* and CD methods,” *Applicationes Mathematicae*, online first, 2026. DOI: 10.4064/am2559-2-2026.
2. S. S. Djordjević, “New hybrid conjugate gradient method as a convex combination of LS and CD methods,” *Filomat* 31 (2017), 1813–1825. DOI: 10.2298/FIL1706813D.
3. M. Abdelhamid, T. Bechouat, Y. Chaib, “A new hybrid conjugate gradient method as a convex combination methods,” *Bulletin of the Transilvania University of Brașov, Series III* 5(67) (2025), 179–192. DOI: 10.31926/BUT.MIF.2025.5.67.2.14.
