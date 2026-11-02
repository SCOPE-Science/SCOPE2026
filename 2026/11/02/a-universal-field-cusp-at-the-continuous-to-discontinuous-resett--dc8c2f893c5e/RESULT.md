# A universal field cusp at the continuous-to-discontinuous resetting transition

## Finding

For the mean-field resetting-diffusion model of Bertin [1], with resetting rate \(\lambda(x)=\mathbf 1_{\{|x|\geq1\}}\), drift \(h\), and feedback \(D=\alpha\Gamma^\beta\), the exact positive-diffusivity stationary solutions satisfy \(\alpha=A_\beta(D,h)=f(D,h)^\beta/D^{\beta-1}\). For all \(\beta>1\), the zero-field curve has a unique global minimum \(\alpha_c(\beta)\), located at

\[
s_c(\beta)=\frac{\beta-2+\sqrt{\beta^2+4\beta-4}}4,
\qquad D_c(\beta)=s_c(\beta)^2,
\qquad \alpha_c(\beta)=\frac{(\tfrac12+s_c+s_c^2)^\beta}{s_c^{2(\beta-1)}}.
\]

Let \(\epsilon=\beta-1\downarrow0\), and introduce the positive normalized diffusivity \(y=D/\epsilon^2\) and nonnegative normalized field \(z=|h|/\epsilon^{5/2}\). Then the normalized logarithmic stationary curve

\[
G_\epsilon(y,z)=\frac1\epsilon\log\frac{A_{1+\epsilon}(\epsilon^2y,\epsilon^{5/2}z)}{\alpha_c(1+\epsilon)}
\]

converges in \(C^3\) on every compact subset of \((0,\infty)\times[0,\infty)\) to

\[
F(y,z)=2(\sqrt y-1)-\log y-\frac{z^2}{12y^2}.
\]

For \(z>0\), the limiting curve has two stationary turning points precisely when \(0<z<z_*\), one degenerate cubic turning point when \(z=z_*\), and no turning points when \(z>z_*\), where

\[
y_*=\frac{16}{25},\qquad z_*=\sqrt{\frac{1536}{3125}}=0.7010848736066126\ldots.
\]

In particular, for every sufficiently small positive \(\epsilon\), the **exact** stationary equation has a locally unique nondegenerate cusp \((y_\epsilon,z_\epsilon)\) near \((y_*,z_*)\), characterized by \(\partial_yG_\epsilon=\partial_{yy}G_\epsilon=0\). It satisfies

\[
D_{\mathrm{cusp}}=\epsilon^2\left(\frac{16}{25}+o(1)\right),\qquad
|h_{\mathrm{cusp}}|=\epsilon^{5/2}\left(\sqrt{\frac{1536}{3125}}+o(1)\right),
\]

and

\[
\frac{1}{\epsilon}\log\frac{\alpha_{\mathrm{cusp}}}{\alpha_c(1+\epsilon)}
\longrightarrow 2\log\frac54-\frac12=-0.05371289737158049\ldots.
\]

The cusp is generic: at the exact finite-\(\epsilon\) cusp the third diffusivity derivative and the field derivative of the first diffusivity derivative are nonzero. Thus the nearby self-consistency curve has a genuine local one-to-three positive-stationary-root transition as the field and the feedback amplitude vary. This is a statement about **local stationary branches**, not their stability in the full nonlinear evolution.

## Assumptions and scope

Use the normalized model of [1]: each walker has diffusion coefficient \(D>0\), constant drift \(h\in\mathbb R\), instantaneous resetting to the origin at unit rate outside the interval \((-1,1)\), and the self-consistent power-law relation \(D=\alpha\Gamma^\beta\) with \(\alpha>0\) and \(\beta>1\). Here \(\Gamma\) is the ensemble-averaged reset rate. All statements concern positive stationary diffusivities in the infinite-population mean-field stationary equation. They do not require or claim dynamical stability of its solutions. For the cusp, \(\epsilon=\beta-1\) is positive and sufficiently small. Convergence is local in \(y>0\), not uniform all the way to \(D=0\).

The exact source stationary relation \(\Gamma(D,h)=D/f(D,h)\) gives

\[
f(D,h)=D\left[1+\frac{1+(\sqrt{1+4D/h^2}+2D/|h|)\tanh(|h|/(2D))}{|h|[\tanh(|h|/(2D))+\sqrt{1+4D/h^2}]}\right]
\]

when \(h\ne0\), with its continuous value \(f(D,0)=\tfrac12+\sqrt D+D\).

## Proof

**Zero-field minimum.** With \(s=\sqrt D>0\), differentiate \(\log A_\beta(s^2,0)\):

\[
\frac{d}{ds}\log A_\beta(s^2,0)=
\frac{2s^2+(2-\beta)s-(\beta-1)}{s(s^2+s+\tfrac12)}.
\]

The numerator has one strictly positive and one negative root for every \(\beta>1\); hence the positive root \(s_c(\beta)\) is the unique minimum. The curve diverges as \(s\downarrow0\) and \(s\to\infty\), making it global. The explicit formulas follow by solving that quadratic. As \(\epsilon\downarrow0\), \(s_c(1+\epsilon)=\epsilon+O(\epsilon^2)\), and

\[
\log\alpha_c(1+\epsilon)=-\log2+\epsilon(2-\log2-2\log\epsilon)+O(\epsilon^2|\log\epsilon|).
\]

**Uniform joint scaling.** For \(h\ne0\), set \(s=\sqrt D\), \(b=|h|/D\), \(u=s/\sqrt{4+s^2b^2}\), and \(t=\tanh(b/2)\). Algebraically the exact formula becomes the nonsingular representation

\[
f(D,h)=D+\frac{u+(1+2u)t/b}{1+ubt},
\]

where \(t/b=1/2\) at \(b=0\). The functions of \(s,b\) in this representation are smooth near \((0,0)\), and even analytic in \(b\). On any compact set with \(0<y_0\le y\le y_1<\infty\) and \(0\le z\le z_1\), the substitutions \(s=\epsilon\sqrt y\) and \(b=\sqrt\epsilon\,z/y\) give, uniformly with three derivatives in \(y,z\),

\[
f(\epsilon^2y,\epsilon^{5/2}z)=\frac12+\epsilon\left(\sqrt y-\frac{z^2}{24y^2}\right)+O(\epsilon^2).
\]

Taking \((1+\epsilon)\log f-\epsilon\log(\epsilon^2y)\) and subtracting the preceding formula for \(\log\alpha_c\) proves the announced \(C^3\) limit \(G_\epsilon\to F\).

**Limiting fold and cusp.** Direct differentiation gives

\[
F_y=y^{-1/2}-y^{-1}+\frac{z^2}{6y^3}.
\]

Putting \(s=\sqrt y\), its zeros satisfy \(z^2=6s^4(1-s)\), necessarily \(0<s<1\). This right-hand side increases on \((0,4/5)\) and decreases on \((4/5,1)\), with its unique maximum \(1536/3125\). Therefore the turning-point trichotomy holds for every fixed \(z>0\). At \((y_*,z_*)\),

\[
F_y=F_{yy}=0,\quad F_{yyy}=y_*^{-3}>0,\quad F_{yz}=z_*/(3y_*^3)>0.
\]

The Jacobian of the map \((y,z)\mapsto(F_y,F_{yy})\) is invertible there: its determinant is \(-F_{yz}F_{yyy}\ne0\). The parameter-dependent implicit-function theorem, using the established \(C^3\) convergence and the smooth exact formula, yields the unique nearby exact cusp \((y_\epsilon,z_\epsilon)\). Continuity preserves its two nonvanishing derivatives and hence the local cusp unfolding and three-root wedge. Evaluating the limiting height at the cusp gives \(F(y_*,z_*)=2\log(5/4)-1/2\), completing the proof.

## Verification

The accompanying `artifacts/verify.py` evaluates the source's explicit stationary formula and the algebraically nonsingular representation to high precision, checks the zero-field critical quadratic, the limiting cusp's four derivative identities, representative scaling convergence, and exact finite-\(\epsilon\) cusp equations. With mpmath 1.3+, the supplied script completed 43 checks. Its finite tests supplement the analytic local-uniform Taylor and implicit-function arguments; they do not establish uniqueness of remote cusps or global evolution stability.

## Relationship to prior work

Bertin [1, equations (9)–(11), (15)–(17), (23), and (29)] derives the exact stationary self-consistency equation, the zero-field relation, the critical \(\beta=1\) fifth-order field response, and the existence of superlinear-feedback coexistence. The paper presents the superlinear zero-field threshold implicitly and treats general nonzero field via numerical resolution. The present result instead resolves the **coupled singular limit** \(\beta\downarrow1\), \(D\sim(\beta-1)^2\), \(|h|\sim(\beta-1)^{5/2}\), proving the full universal local limiting curve and the exact limiting cusp constants. This is neither the source's zero-field tangency condition alone nor its \(\beta=1\) critical field law alone. The conventional Hébraud–Lequeux model and its mathematical analyses [2,3] address the linear-feedback case and related flow curves rather than this superlinear joint unfolding.

## Limitations

The cusp's uniqueness and the one-to-three branch count are **local** in the scaled positive-diffusivity neighborhood. Additional roots near \(D=0\), global finite-\(\epsilon\) branch topology, stability of the full nonlinear mean-field evolution, finite-population fluctuations, and nonlinear feedback beyond the chosen power law are not resolved. The theorem does not characterize physical hysteresis from stability alone. Literature comparison cannot certify absolute publication priority; an unlocated stronger theorem could subsume the statement.

## References

[1] E. Bertin, *Stochastic resetting of a population of random walks with resetting-rate-dependent diffusivity*, arXiv:2205.00817v1 (first public 2022-05-02), https://arxiv.org/html/2205.00817v1 .

[2] P. Hébraud and F. Lequeux, *Mode-coupling theory for the pasty rheology of soft glassy materials*, Phys. Rev. Lett. 81, 2934 (1998), doi:10.1103/PhysRevLett.81.2934 .

[3] J. Olivier and M. Renardy, *Glass transition seen through asymptotic expansions*, SIAM J. Appl. Math. 71, 1144 (2011), doi:10.1137/100800725 .
