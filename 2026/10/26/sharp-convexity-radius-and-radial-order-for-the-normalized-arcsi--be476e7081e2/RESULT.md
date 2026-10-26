# Sharp convexity radius and radial order for the normalized-arcsine starlike class

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(c=2/\pi\), and \(\Phi(w)=1+c\arcsin w\), with the principal branch. Define the normalized Ma--Minda class \(\mathcal S^*_{\mathrm{arc}}\) by \(f(0)=0\), \(f'(0)=1\), and \(zf'(z)/f(z)=\Phi(\omega(z))\) for a holomorphic Schwarz function \(\omega:\mathbb D\to\mathbb D\) with \(\omega(0)=0\).

Put \(D(r)=1-c\arcsin r\) and
\[
\beta(r)=D(r)-\frac{cr}{\sqrt{1-r^2}D(r)}.
\]
For every \(0\le r\le 11/20\),
\[
\inf_{f\in\mathcal S^*_{\mathrm{arc}}}\ \min_{|z|=r}\operatorname{Re}\left(1+\frac{zf''(z)}{f'(z)}\right)=\beta(r).
\]
The **sharp radius of convexity** of the entire class is the unique \(R\in(1/2,11/20)\) such that
\[
\sqrt{1-R^2}\left(1-\frac2\pi\arcsin R\right)^2=\frac{2R}{\pi}.
\]
Numerically \(R=0.538585996535\ldots\). The same normalized function
\[
f_*(z)=z\exp\left[-\frac2\pi\int_0^z\frac{\arcsin t}{t}\,dt\right]
\]
attains the displayed lower bound at each positive real \(z=r\) in the stated range and witnesses sharp failure of convexity beyond \(R\).

## Assumptions and scope
All functions are holomorphic in \(\mathbb D\) and normalized at the origin. The principal arcsine has the Taylor series with positive real coefficients. Every \(f\) in this class is starlike and univalent, since \(\operatorname{Re}\Phi(\omega)>0\); consequently \(f'\) never vanishes. The order formula is claimed only for \(r\le11/20\); the convexity-radius statement is global.

## Proof
Write \(p(z)=zf'(z)/f(z)=\Phi(\omega(z))\). Differentiation gives the exact identity
\[
1+\frac{zf''(z)}{f'(z)}=\Phi(\omega(z))+z\omega'(z)\frac{\Phi'(\omega(z))}{\Phi(\omega(z))}.
\]
Fix \(|z|=r\le11/20\) and let \(t=|\omega(z)|\le r\). The Schwarz lemma and the Schwarz--Pick inequality applied to \(\omega(z)/z\), with removable value at the origin, give the Dieudonne estimate
\[
|z\omega'(z)-\omega(z)|\le\frac{r^2-t^2}{1-r^2},\qquad
|z\omega'(z)|\le B_r(t):=t+\frac{r^2-t^2}{1-r^2}.
\]
Since all Maclaurin coefficients of \(\arcsin w\) are nonnegative, \(\operatorname{Re}\arcsin w\ge-\arcsin|w|\). Therefore \(\operatorname{Re}\Phi(w)\ge D(t)>0\) and \(|\Phi(w)|\ge D(t)\). Also
\[
|\Phi'(w)|=\frac c{|\sqrt{1-w^2}|}\le\frac c{\sqrt{1-t^2}}.
\]
Hence
\[
\operatorname{Re}\left(1+\frac{zf''}{f'}\right)\ge
D(t)-\frac{cB_r(t)}{\sqrt{1-t^2}D(t)}.
\]
To optimize this bound in \(0\le t\le r\), put \(A(t)=\arcsin t\), \(S(t)=\sqrt{1-t^2}\), and \(F_r(t)=A(t)+B_r(t)/(S(t)D(t))\). An exact differentiation yields
\[
S(t)D(t)F_r'(t)=D(t)+1-\frac{2t}{1-r^2}
+B_r(t)\left(\frac{t}{1-t^2}+\frac{c}{S(t)D(t)}\right).
\]
All factors in the last parenthesis are nonnegative. For \(t\le r\le11/20\), \(\arcsin(11/20)<\pi/5\) because \(\sin(\pi/5)>11/20\); thus \(D(t)>3/5\). Moreover
\[
1-\frac{2t}{1-r^2}\ge1-\frac{440}{279}=-\frac{161}{279},
\]
so \(S(t)D(t)F_r'(t)>3/5-161/279=32/1395>0\). Thus \(F_r\) increases and the lower bound is smallest at \(t=r\), where it equals \(\beta(r)\).

For the extremizer \(f_*\), \(zf_*'(z)/f_*(z)=\Phi(-z)\). At real \(z=r\), all preceding inequalities become equalities (\(\omega(z)=-z\)), proving the claimed exact radial order for every radius through \(11/20\).

The function \(D(r)\) decreases strictly and \(r/(\sqrt{1-r^2}D(r))\) increases strictly, hence \(\beta\) decreases strictly. At \(r=1/2\), \(\beta(1/2)=2/3-\sqrt3/\pi>0\). At \(r=11/20\), using \(\pi<22/7\), \(\arcsin r>r+r^3/6=27731/48000\), and \(\sqrt{1-r^2}<21/25\), we have
\[
D(r)<30353/48000,\qquad
\sqrt{1-r^2}D(r)^2<\frac{21}{25}\left(\frac{30353}{48000}\right)^2<\frac7{20}<cr.
\]
Thus \(\beta(11/20)<0\) and there is a unique \(R\in(1/2,11/20)\) where \(\beta(R)=0\). The characterization of convex univalent mappings by \(\operatorname{Re}(1+zf''/f')>0\) proves convexity on every \(|z|<R\). For every larger radius, \(f_*\) has a point with negative real convexity expression just to the right of \(R\), so no larger universal radius is possible.

## Verification
The bundled `verify.py` checks the exact rational comparison at \(11/20\), signs at the bracket endpoints, monotonicity numerically on a grid as a *supplementary* check, and determines the root by bisection. The actual theorem is established by the preceding analytic inequalities; the finite numerical grid is not part of the proof.

## Relationship to prior work
Panja, Banerjee and Majumder (arXiv:2609.20288v1, 2026) introduced the same normalized-arcsine Ma--Minda class and established coefficient, logarithmic-coefficient and Hankel-determinant estimates. Their theorems do not state the class-wide sharp convexity radius or its exact radial order. Closely related work on the arcsine target concerns its image geometry and strong-starlikeness sector, not the convexity criterion involving \(f''/f'\). Sharp convexity-radius results for other Ma--Minda targets use distinct subordinations and have no direct implication for the displayed arcsine identity.

## Limitations
The full radial-order formula has been proved only through \(r=11/20\), although this range contains the exact convexity radius. No assertion is made about the full radial extremal profile beyond that range, about uniform convexity or about a unique equality mapping. Priority is limited by indexed/published searches and examination of the motivating full text; an unindexed general radius theorem might imply the result. No independent audit has been performed.

## References
1. S. Panja, A. Banerjee, S. Majumder, *Coefficient estimates and Hankel determinant for the class of leaf shaped starlike function*, arXiv:2609.20288v1 (2026), https://arxiv.org/pdf/2609.20288.
2. E. Dieudonne, classical Schwarz--Pick derivative estimate for disk self-maps fixing the origin (used here through the elementary Schwarz--Pick consequence explicitly derived in the proof).
3. R. M. Ali, N. Jain, V. Ravichandran, *On the radius constants for classes of analytic functions*, arXiv:1207.4529 (2012), https://arxiv.org/abs/1207.4529 (general contextual radius problems, not an equivalent arcsine theorem).
