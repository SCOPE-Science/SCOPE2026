# Exact squeezing value at the origin of the type-4 decoupled model

## Context

The squeezing function $s_D(p)$ of a bounded domain $D \subset \mathbb{C}^n$ measures
how large a centered ball can be inscribed in a normalized injective holomorphic
image of $D$ in the unit ball. Deng–Guan–Zhang introduced the invariant and
proved holomorphic homogeneous regularity equals a positive lower bound, with
uniform gaps for convex/strongly pseudoconvex cases, but no uniform bound
depending only on D'Angelo type for finite-type domains in $\mathbb{C}^2$ and no
exact value for the decoupled Thullen model. Boundary-limit theorems
(Joo–Kim; Ninh Van Thu et al.) show squeezing tending to 1 forces strong
pseudoconvexity — the opposite direction from an interior exact value. Exact
ordinary-squeezing computations exist only for annuli (Ng–Tang–Tsai;
Gumenyuk–Roth) and bounded symmetric domains (Bharali–Borah–Gorai extending
Kubota); general-ellipsoid results give only one-sided/local bounds near
$(P,r)$-extreme points (Van Thu et al.), and Gupta–Pant compute generalized
squeezing of the ball in the opposite direction. The domain
$E_2 = \{(z_1,z_2) : |z_1|^2 + |z_2|^4 < 1\}$ is the smallest non-strictly
pseudoconvex decoupled finite-type model (D'Angelo type 4), the natural first
calibration endpoint for any type-dependent gap $c(m)$.

## Definitions

- Squeezing function: $s_D(p) = \sup\{r \in (0,1] : \exists\ \text{injective
  holomorphic } f : D \to B^2,\ f(p) = 0,\ B(0,r) \subset f(D)\}$,
  $B^2$ the unit ball in $\mathbb{C}^2$.
- $E_2 = E = \{\rho < 1\}$, $\rho(z) = |z_1|^2 + |z_2|^4$.
- Kobayashi infinitesimal metric $K_D$; Minkowski functional
  $m(z) = \inf\{t > 0 : z/t \in E\}$ of $E$.

## Result

**Theorem.** For $E_2 = \{(z_1,z_2) \in \mathbb{C}^2 : |z_1|^2 + |z_2|^4 < 1\}$,
$$s_{E_2}(0) = \frac{2}{\sqrt{5}} \approx 0.894427191.$$

**Corollary.** $s_{E_2}(0) \neq 1/\sqrt{2}$: the map $L(z) = 2z/\sqrt{5}$ is
admissible with radius $2/\sqrt{5} > 1/\sqrt{2}$.

Domain data (all elementary): $E$ is bounded, open, balanced, complete
Reinhardt, contains $B^2$ (if $|z_1|^2+|z_2|^2<1$ then $|z_2|\le 1$ so
$|z_2|^4\le|z_2|^2$); smooth boundary ($\nabla\rho = 0$ only at $0 \notin
\partial E$); convex hence pseudoconvex (real Hessian $\mathrm{diag}(2,2,H_2)$,
$H_2 = 4sI + 8vv^T$, eigenvalues $4s, 12s \ge 0$); D'Angelo type exactly 4
($\Gamma(\zeta) = (1,\zeta)$ gives contact 4; Levi form
$|v_1|^2 + 4|p_2|^2|v_2|^2$ positive off $\{z_1 = 0\}$; at
$p = (e^{i\theta},0)$ tangential condition forces $v_1 = 0$, and for regular
$\gamma$ with $\gamma_1 = e^{i\theta} + b\zeta^2 + c\zeta^3 + \cdots$,
$\gamma_2 = v_2\zeta + \cdots$, $f = \rho\circ\gamma - 1$ has contact 2 if
$b \neq 0$, 3 if $b = 0, c \neq 0$, exactly 4 if $b = c = 0$ since the
$\zeta^2\bar\zeta^2$ coefficient $K = |v_2|^4 > 0$ is nonzero; non-tangential
curves have contact 1).

## Proof / evidence

Lower bound $s_E(0) \ge 2/\sqrt{5}$: put $t = 2/\sqrt{5}$, $L(z) = tz$.
For $(z_1,z_2) \in E$ with $x = |z_1|^2$, $y = |z_2|^2$ ($x + y^2 < 1$):
$|Lz|^2 = t^2(x+y) = t^2(x + y^2 + y - y^2) < t^2(1 + 1/4) = 1$ since
$y - y^2 \le 1/4$. So $L : E \to B^2$ is injective holomorphic, $L(0) = 0$,
and $L(B^2) = B(0,t) \subset L(E)$ because $B^2 \subset E$. Sharp for scalar
maps since $\sup_E |z|^2 = \max_{x+y^2\le 1}(x+y) = 5/4$ at $(x,y) = (3/4,1/2)$,
i.e. $(|z_1|,|z_2|) = (\sqrt{3}/2, 1/\sqrt{2}) \in \partial E$ mapping to
$\partial B^2$.

Balanced reduction (Lemma R): $K_E(0,v) = m(v)$ and $E = \{m < 1\}$ — ($\le$)
via discs $\zeta \mapsto \zeta v/(m(v)+\delta)$; ($\ge$) via a Hahn–Banach
complex-linear $\ell$ with $\ell(v) = m(v)$, $|\ell| \le m < 1$ on $E$, and
Schwarz applied to $\ell \circ \varphi$. Since $f : E \to f(E)$ is
biholomorphic, $K_{f(E)}(0,Av) = m(v)$ with $A = df_0$. Metric-decreasing
under $B(0,r) \subset f(E) \subset B^2$ gives
$|Av| = K_{B^2}(0,Av) \le m(v) \le K_{B(0,r)}(0,Av) = |Av|/r$, so
$A(E) \subset B^2$ and $B(0,r) \subset A(E)$; $A$ contains a ball so is an
isomorphism. Hence $s_E(0) \le s^{\mathrm{lin}}$.

Linear optimum (Lemma M): $s^{\mathrm{lin}} = 2/\sqrt{5}$. Writing
$M = A^*A$ with entries $(p,q,c)$: phases give
$r(A)^2 = \min_{x^2+y^4=1}(px^2+qy^2-2|c|xy)$ and
$A(E) \subset B^2 \iff \max_{x^2+y^4<1}(px^2+qy^2+2|c|xy) \le 1$; increasing
$|c|$ decreases radius and tightens the constraint, so the optimum is
diagonal $M = \mathrm{diag}(a^2,b^2)$. For $D = \mathrm{diag}(a,b)$,
$B(0,r) \subset D(E) \iff r \le \min(a,b)$ (via convex
$h(s) = s/a^2 + (r^2-s)^2/b^4$, $h'' > 0$). Outer constraint
$\max_{u\in[0,1]} g(u) \le 1$, $g(u) = a^2(1-u^2) + b^2u$ concave; if
$a = b = t$, $\max g = 5t^2/4$ at $u = 1/2$ so $t \le 2/\sqrt{5}$; if
$a \ge b$ (resp. $b \ge a$), $g(1/2) \ge 5b^2/4$ (resp. $5a^2/4$) so
$\min \le 2/\sqrt{5}$. Attained by $(2/\sqrt{5})I$.

Assembly: lower bound plus Lemmas R+M give equality.

## Limitations

Value proved at the origin only; no claim about $\inf_{E_2} s$ or any uniform
$c(m)$. Type computation is order-of-contact bookkeeping. Corroborating
script replays achiever identities and a linear-matrix sweep but the proof is
analytic and does not depend on numerics.

## Reproducibility

Definitions, both extremal embeddings, and all calculus steps are checkable
from this record. Corroboration: `artifacts/scaling_check.py`
(stdlib-only; run `python3 artifacts/scaling_check.py`; 53 checks
ALL CHECKS PASSED), replaying $B^2 \subset E_2$, envelope $5/4$, saturator,
convexity Hessian, diagonal envelope, and a 1500-sample linear-matrix sweep.

## References

- F. Deng, Q. Guan, L. Zhang, On some properties of squeezing functions of
  bounded domains, https://arxiv.org/abs/1109.3920
- H. Joo, Y. Kim, On boundary points at which the squeezing function tends
  to one, https://arxiv.org/abs/1611.08356
- N. Van Thu, N. T. K. Son, C. Van Tiep, Boundary behavior near a global
  extreme point, https://arxiv.org/abs/2005.00977
- N. Van Thu, N. T. L. Huong, N. Q. Dieu, Boundary behaviour near linearly
  convex points, https://arxiv.org/abs/2209.14168
- G. Bharali, D. Borah, S. Gorai, The squeezing function: exact computations,
  optimal estimates, and a new application, https://arxiv.org/abs/2305.11145
- P. Gumenyuk, O. Roth, On the squeezing function for finitely connected
  planar domains, https://arxiv.org/abs/2011.13734
- N. Gupta, S. K. Pant, A note on squeezing function and its
  generalizations, https://arxiv.org/abs/2211.14971
