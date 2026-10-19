# A quartic resonance staircase and an exact Floquet transition in the biquadratic nontwist map

## Finding

Consider the biquadratic nontwist map on the **entire infinite cylinder** \(\mathbb T\times\mathbb R\), where \(\mathbb T=\mathbb R/\mathbb Z\),
\[
M(x,y)=\bigl(x+W(y-b\sin(2\pi x))\pmod 1,\;y-b\sin(2\pi x)\bigr),
\qquad W(y)=a(1-y^2)(1-\epsilon y^2),
\]
with \(0<a\le1\), \(0<b\le1\), and \(\epsilon>0\). A periodic orbit has **constant action** when its \(y\)-coordinate is the same at every state, not merely after one full return. Count primitive period-two orbits up to cyclic exchange.

**Theorem.** Every constant-action primitive period-two orbit, and no other such orbit, is
\[
(0,y)\longleftrightarrow(1/2,y),\qquad W(y)=m+1/2,\quad m\in\mathbb Z.
\]
Each admissible real root \(y\) gives one distinct orbit. In particular there are infinitely many such orbits for every allowed parameter triple, independently of the kick amplitude \(b\).

Put
\[
r_c=\sqrt{\frac{1+\epsilon}{2\epsilon}},\qquad
w_c=-\frac{a(\epsilon-1)^2}{4\epsilon},\qquad
C=2\#\{m\in\mathbb Z:w_c\le m+1/2<a\}
+\mathbf{1}_{\{a\in\mathbb Z+1/2\}}.
\]
The number \(N(R)\) of these primitive period-two orbits with \(|y|\le R\), for **every** \(R\ge r_c\), is exactly
\[
\boxed{N(R)=C+2\left(\left\lfloor W(R)-1/2\right\rfloor
-\left\lfloor w_c-1/2\right\rfloor\right).}
\]
Consequently, including its sharp subleading term,
\[
\boxed{N(R)=2a\epsilon R^4-2a(1+\epsilon)R^2+O_{a,\epsilon}(1)}
\qquad(R\to\infty).
\]
No assertion is made that these are **all** primitive two-cycles of the map; the exhaustive classification is for the natural constant-action class.

For each listed orbit, the derivative of the two-step return has determinant one and trace
\[
\boxed{\tau(y)=2-\bigl(2\pi b W'(y)\bigr)^2},
\qquad W'(y)=2ay\bigl(2\epsilon y^2-(1+\epsilon)\bigr).
\]
It is linearly elliptic when \(0<|2\pi bW'(y)|<2\), spectrally neutral (with double multiplier \(+1\) or \(-1\)) when \(|2\pi bW'(y)|=0\) or \(2\), respectively, and hyperbolic with two negative reciprocal multipliers when \(|2\pi bW'(y)|>2\). There is a unique \(r_h>r_c\) solving \(W'(r_h)=1/(\pi b)\). Among the outer resonances \(|y|>r_c\), the sharp transition is elliptic for \(r_c<|y|<r_h\), parabolic at \(|y|=r_h\) if resonant, and hyperbolic for \(|y|>r_h\).

For each sufficiently large integer \(m\), exactly two orbits in this class arise from \(W(y)=m+1/2\), at the positive and negative outer roots. Their larger-magnitude two-step multiplier has spectral radius
\[
\boxed{\rho_m\sim64\pi^2b^2\sqrt{a\epsilon}\;m^{3/2}}
\qquad(m\to\infty).
\]
Thus the map has a quantitatively unbounded hyperbolic period-two skeleton at arbitrarily large action for **every** positive kick amplitude.

## Assumptions and scope

The angular variable is taken modulo one, while \(y\) ranges over all real values; no unannounced compact action cutoff or zero-winding restriction is imposed. The parameter region is \(0<a\le1\), \(0<b\le1\), \(\epsilon>0\). We count actual cylinder orbits, rather than roots of an unreduced lift, and treat coincident roots only once. A linearly elliptic orbit is not thereby claimed nonlinearly stable or surrounded by invariant curves. The result is about period two with action unchanged at each iterate; other two-cycles, and transport between action levels, are outside the theorem.

## Proof

**1. Exhaustion of the constant-action class.** Let \((x_0,y_0)\mapsto(x_1,y_1)\mapsto(x_0,y_0)\) have primitive period two and \(y_0=y_1=y\). From both action equations and \(b>0\),
\[
\sin(2\pi x_0)=\sin(2\pi x_1)=0.
\]
The two angles therefore belong to \(\{0,1/2\}\) in \(\mathbb T\). Primitivity forces them to be distinct, hence alternate. The angular equation is precisely \(W(y)\equiv 1/2\pmod1\), or \(W(y)=m+1/2\) for one integer \(m\). Conversely, every real root gives the claimed two-cycle since both sine kicks vanish. Distinct roots give disjoint cylinder orbits. This proves the classification without assuming the converse for arbitrary two-cycles.

**2. Exact staircase and boundaries.** For \(s=y^2\ge0\),
\[
W(y)=a\bigl(1-(1+\epsilon)s+\epsilon s^2\bigr).
\]
This convex quadratic has its unique minimum \(w_c\) at \(s=r_c^2\). Thus \(W\) strictly decreases from \(a\) to \(w_c\) as \(|y|\) ranges from zero to \(r_c\), and strictly increases from \(w_c\) to infinity when \(|y|>r_c\). The central interval \([-r_c,r_c]\) contributes exactly two roots for each half-integer in \([w_c,a)\), and one root at \(y=0\) if \(a\) is a half-integer. At the minimum there are exactly two roots \(\pm r_c\), not four. This is exactly the stated number \(C\).

For \(R\ge r_c\), each half-integer level in \((w_c,W(R)]\) supplies exactly one positive and one negative **outer** root with \(r_c<|y|\le R\). The count of integer \(m\) with \(w_c<m+1/2\le W(R)\) is exactly \(\lfloor W(R)-1/2\rfloor-\lfloor w_c-1/2\rfloor\). The strict lower endpoint excludes double counting at \(w_c\), and the closed upper endpoint includes roots on \(|y|=R\). This yields the exact staircase. Since \(2\lfloor u-1/2\rfloor=2u+O(1)\) and \(W(R)=a\epsilon R^4-a(1+\epsilon)R^2+a\), the two-term asymptotic follows with bounded error.

**3. Exact Floquet trace.** On a neighborhood of any listed cycle, write \(q=2\pi b\) and \(w=W'(y)\). At its angle-zero and angle-half states, the one-step Jacobians in \((x,y)\) order are
\[
J_0=\begin{pmatrix}1-qw&w\\-q&1\end{pmatrix},\qquad
J_{1/2}=\begin{pmatrix}1+qw&w\\q&1\end{pmatrix}.
\]
Each has determinant \(1\), and direct multiplication gives
\[
\operatorname{tr}(J_{1/2}J_0)=2-(qw)^2,
\qquad\det(J_{1/2}J_0)=1.
\]
The characteristic equation is \(\lambda^2-\tau(y)\lambda+1=0\). This proves every stated elliptic/neutral/hyperbolic boundary. When \(W'(y)=0\), the two-step Jacobian is the identity (a degenerate neutral case); when \(\lvert2\pi bW'(y)\rvert=2\), its double multiplier is \(-1\). It also establishes the sign of the hyperbolic multipliers. For \(y>r_c\), \(W'(y)>0\) and
\[
W''(y)=2a\bigl(6\epsilon y^2-(1+\epsilon)\bigr)>0.
\]
Hence \(W'\) increases strictly from zero to infinity on the outer positive branch; there is a unique \(r_h>r_c\) with \(W'(r_h)=1/(\pi b)\). Evenness of \(W\) makes \(|W'(-y)|=W'(y)\), giving the sharp outer threshold on both sides.

**4. Growth of hyperbolicity.** For every sufficiently large integer \(m\), the level \(m+1/2\) lies above \(a\) and has exactly two real roots, one of either sign. Let \(y_m>r_c\) be the positive root. Solving the quadratic in \(s=y_m^2\) gives
\[
s_m=\frac{1+\epsilon+\sqrt{(1-\epsilon)^2+4\epsilon(m+1/2)/a}}{2\epsilon},\qquad
y_m\sim\left(\frac{m}{a\epsilon}\right)^{1/4}.
\]
Consequently \(|W'(y_m)|\sim4(a\epsilon)^{1/4}m^{3/4}\). The return trace tends to minus infinity and the spectral radius of its reciprocal real eigenvalues satisfies \(\rho_m\sim(2\pi b W'(y_m))^2=64\pi^2b^2\sqrt{a\epsilon}\,m^{3/2}\). This proves an infinite family of hyperbolic orbits without confusing finite tests with an infinite proof.

## Verification

Run `python3 verify.py` from the same directory. The script uses only the Python standard library and checks exact rational Jacobian traces and determinants, exact resonance levels, endpoint-inclusive staircase counts against independent quadratic-root enumeration, and a nontrivial rationally bounded elliptic-to-hyperbolic example.

For \(a=1/2\), \(\epsilon=2\), and \(b=1/(16\pi)\), one has \(W(y)=y^4-3y^2/2+1/2\). There is one neutral central orbit with identity two-step linearization at \(y=0\), exactly ten elliptic outer orbits (two at each level \(m=0,1,2,3,4\)), and infinitely many hyperbolic outer orbits (two for each \(m\ge5\)). In the closed action strip \(|y|\le2\), exactly \(23\) constant-action primitive two-cycles occur. In this example the outer roots have
\[
y_m^2=\frac{3+\sqrt{9+16m}}4\quad(m\ge0).
\]
The inequalities \(y_4<17/10\) and \(y_5>44/25\), together with strict growth of \(W'\) outside \(r_c\), give \(W'(y_4)<16<W'(y_5)\); the threshold here is \(|W'|=16\). These inequalities are certified by elementary rational squares in the verification script.

## Relationship to prior work

Grime, Roberto, Viana, Elskens and Caldas introduced the biquadratic nontwist map and its symmetry lines, and identified the primary fixed-point resonances and separatrix reconnection scenarios [1]. Their later study investigated breakup of multiple shearless curves and local period-two reconnection numerically [2]. A further study analyzed effective transport barriers and manifold intercrossing [3]. The present statement uses the same unbounded-cylinder map but concerns a different invariant: **the entire constant-action period-two resonance spectrum over all integer angular windings**, an exact action-cutoff counting staircase, and its complete linear stability transition. The symmetry lines and area-preserving Floquet criteria themselves are prior ingredients, not claimed as new. The accessible relevant mathematical sections of [1]–[3] do not establish the exact staircase or the universal hyperbolic tail. This is a best-knowledge literature comparison, not a proof that no equivalent antecedent exists.

## Limitations

The theorem does not classify two-cycles with nonconstant action, higher periods, global attractors, transport rates, existence or breakup of shearless curves, or nonlinear KAM stability of elliptic cycles. The large-action tail may extend beyond the region where the physical derivation from a plasma model is quantitatively accurate; the result remains exact for the published mathematical map on \(\mathbb T\times\mathbb R\). Classical resonance methods might yield related statements in other twist or nontwist systems; an equivalent theorem under another formulation is a residual priority risk. Independent mathematical validation has not been performed.

## References

[1] G. C. Grime, M. Roberto, R. L. Viana, Y. Elskens, I. L. Caldas, “Biquadratic Nontwist Map: a model for shearless bifurcations,” arXiv:2209.07408 (first public version 2022-09-15); *Chaos, Solitons & Fractals* 169 (2023), 113231. DOI: 10.1016/j.chaos.2023.113231. Full text: https://fisica.ufpr.br/viana/artigos/2023/grime2023.pdf.

[2] G. C. Grime et al., “Shearless curve breakup in the biquadratic nontwist map,” arXiv:2305.17538 (2023-05-27). https://arxiv.org/pdf/2305.17538.

[3] G. C. Grime, R. L. Viana, Y. Elskens, I. L. Caldas, “Effective transport barriers in the biquadratic nontwist map,” arXiv:2409.00785 (2024-09-01); *Physical Review E* 111 (2025), 014219. https://arxiv.org/abs/2409.00785.
