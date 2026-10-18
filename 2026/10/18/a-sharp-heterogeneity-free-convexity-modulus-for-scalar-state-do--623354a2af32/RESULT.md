# A sharp heterogeneity-free convexity modulus for scalar-state domain-randomized LQR

## Finding

Consider any finite weighted family of discrete-time scalar-state systems, all controlled by one common multi-input static gain. On the nonempty common stabilization region, their stationary sample-average linear-quadratic cost is globally **strongly convex without any bound on plant heterogeneity**. More precisely, for the positive-definite weighted input-cost matrix \(\overline R\) specified below,
\[
\nabla^2F(k)\succeq\frac12\overline R\quad\text{for every jointly stabilizing }k.
\]
The numerical factor \(1/2\) is the **largest universal factor** valid for arbitrary scalar-state plant parameters and positive state penalties. There is one global minimizer, and the entire jointly stabilizing region satisfies the corresponding quantitative Polyak–Łojasiewicz inequality. This supplies a verifiable landscape condition for a meaningful subclass of domain-randomized LQR, rather than assuming gradient dominance or small inter-plant variation.

## Assumptions and scope

Fix integers \(d\ge1\) and \(M\ge1\). For \(j=1,\ldots,M\), let \(a_j\in\mathbb R\), \(b_j\in\mathbb R^d\), \(q_j>0\), \(R_j\in\mathbb R^{d\times d}\) symmetric positive definite, \(\nu_j>0\), and \(\omega_j>0\) with \(\sum_j\omega_j=1\). In system \(j\), use the static law \(u_t=kx_t\) for a common \(k\in\mathbb R^d\):
\[
 x_{t+1}=(a_j+b_j^\mathsf Tk)x_t+w_t,\qquad
 \mathbb E w_t=0,\quad \mathbb E w_t^2=\nu_j,
\]
where disturbances are temporally independent, centered, and independent of the current state. The stage cost is \(q_jx_t^2+u_t^\mathsf TR_ju_t\). For a stabilizing gain the stationary cost equals \(\nu_j(q_j+k^\mathsf TR_jk)/[1-(a_j+b_j^\mathsf Tk)^2]\). Define
\[
\mathcal S=\{k\in\mathbb R^d:|a_j+b_j^\mathsf Tk|<1\ \text{for all }j\},
\quad\overline R=\sum_{j=1}^M\omega_j\nu_jR_j,
\]
\[
F(k)=\sum_{j=1}^M\omega_j\nu_j
\frac{q_j+k^\mathsf TR_jk}{1-(a_j+b_j^\mathsf Tk)^2}
\quad(k\in\mathcal S).
\]
Assume \(\mathcal S\ne\varnothing\). No closeness, common-input matrix, or small-heterogeneity assumption is made. The claim concerns the exact stationary sample-average cost, not a fixed-policy Bellman surrogate.

Then \(\mathcal S\) is open and convex, \(F\) is twice continuously differentiable and has a unique minimizer \(k_*\in\mathcal S\), and
\[
\nabla^2F(k)\succeq\frac12\overline R,
\quad F(k)-F(k_*)\ge\frac14(k-k_*)^\mathsf T\overline R(k-k_*),
\]
\[
\frac12\|\nabla F(k)\|_2^2\ge
\frac{\lambda_{\min}(\overline R)}2\bigl(F(k)-F(k_*)\bigr),
\quad k\in\mathcal S.
\]
The Hessian constant is sharp over this class even with just one system and one actuator.

## Proof

**Stationary cost and geometry.** With \(y_j=a_j+b_j^\mathsf Tk\in(-1,1)\), the stationary variance solves \(s=y_j^2s+\nu_j\), giving \(s=\nu_j/(1-y_j^2)\) and the displayed cost. Each stability restriction is an open affine slab. Hence their intersection \(\mathcal S\) is open and convex.

**A pointwise sharp Hessian inequality.** Work first with one system and omit its index and weight. Put \(y=a+b^\mathsf Tk\), \(Q=q+k^\mathsf TRk\), and \(g(y)=(1-y^2)^{-1}\). For any direction \(v\in\mathbb R^d\), set \(z=v^\mathsf TRv>0\) for \(v\ne0\), \(u=k^\mathsf TRv\), and \(h=b^\mathsf Tv\). Twice differentiating the scalar function \(J(k)=Qg(y)\) gives the exact identity
\[
D^2J(k)[v,v]=2zg(y)+4ug'(y)h+Qg''(y)h^2.
\]
Here \(Q>0\), \(g''(y)=2(1+3y^2)/(1-y^2)^3>0\), and Cauchy–Schwarz in the \(R\)-inner product gives \(u^2\le z k^\mathsf TRk\le zQ\). Completing the square in \(h\) therefore yields
\[
D^2J(k)[v,v]\ge 2zg(y)-\frac{4u^2g'(y)^2}{Qg''(y)}
\ge z\left(2g(y)-\frac{4g'(y)^2}{g''(y)}\right)
=\frac{2z}{1+3y^2}\ge\frac z2.
\]
The first inequality holds for the actual \(h\), without assuming that \(h\) can vary independently of \(u\). Summing after multiplying by \(\omega_j\nu_j>0\) proves \(\nabla^2F(k)\succeq\overline R/2\) for every \(k\in\mathcal S\).

**Existence, uniqueness, and gradient dominance.** Since every denominator is at most one, \(F(k)\ge k^\mathsf T\overline Rk\), which is coercive as \(\|k\|\to\infty\). If a bounded sequence in \(\mathcal S\) approaches a boundary point, at least one denominator tends to zero while its numerator stays at least \(q_j>0\), so \(F(k)\to\infty\). Thus a sublevel set below any finite level is compact and contained in \(\mathcal S\); the minimum is attained in \(\mathcal S\), and strict convexity makes it unique. Integrating the Hessian bound along segments in \(\mathcal S\) gives strong convexity with Euclidean modulus \(\mu=\lambda_{\min}(\overline R)/2\) and the stated quadratic-growth bound. At the interior minimizer \(\nabla F(k_*)=0\). Strong convexity, with the comparison point \(k_*\), yields
\[
F(k)-F(k_*)\le\nabla F(k)^\mathsf T(k-k_*)-\frac\mu2\|k-k_*\|_2^2
\le\frac{\|\nabla F(k)\|_2^2}{2\mu}.
\]
This is precisely the stated Polyak–Łojasiewicz inequality.

**Sharpness.** Let \(d=M=1\), \(R=\omega=\nu=b=1\). For \(0<y<1\), define
\[
a_y=\frac{y(3+y^2)}{1+3y^2},\qquad
k_y=y-a_y,\qquad q_y=(1-y)^4>0.
\]
The closed-loop pole is \(a_y+k_y=y\in(-1,1)\). Direct differentiation of \(J_y(k)=(q_y+k^2)/[1-(a_y+k)^2]\), evaluated at \(k=k_y\), gives
\[
J_y''(k_y)=\frac{2}{1+3y^2}+
\frac{2(1-y)^4(1+3y^2)}{(1-y^2)^3}.
\]
As \(y\uparrow1\), the first term approaches \(1/2\) and the second tends to zero. Hence no uniform matrix-Hessian coefficient strictly larger than \(1/2\) can hold even when the state cost is strictly positive.

## Verification

The standalone script `verify.py` checks the rational curvature identity and the sharpness limit by symbolic algebra; it also checks the exact directional Hessian identity against central differences and the bound in randomized multi-actuator examples. Reproduce with `python verify.py` (requires Python, SymPy, and NumPy). These tests provide finite corroboration; the proof above, not computation, establishes the quantified assertions.

## Relationship to prior work

Pasdar and Adib Yaghmaie (2026, arXiv:2609.04794v1) analyze policy iteration for the sample-average domain-randomized LQR objective and explicitly impose an additional gradient-dominance assumption to derive a linear rate; their discussion addresses moderate heterogeneity. The present theorem proves a globally quantitative landscape property directly for **scalar-state, any finite number of heterogeneous plants and any input dimension**. It does not establish their algorithm's other technical convergence assumptions.

Fujinami, Lee, Matni and Pappas (2025, arXiv:2503.24371v1) obtain policy-gradient convergence for domain-randomized LQR subject to a system-heterogeneity condition; those sufficient hypotheses do not state this sharp scalar-state Hessian bound. Pasdar and Adib Yaghmaie's earlier SDP formulation (ECC 2026) treats a lifted and locally linearized semidefinite optimization problem, rather than the global Hessian of the native common-feedback cost. Rodriguez-Gil and Uribe (2026, arXiv:2604.22138v1) prove strong convexity of a **fixed-policy Bellman surrogate** for scalar ReLU-controlled LQR, a different function from the native domain-randomized feedback objective treated here. Standard quadratic-over-linear convexity ideas support the underlying derivation but alone do not supply a cited sharp \(1/2\) DR-LQR modulus.

## Limitations

Only one-dimensional **state** dynamics are covered; the number of actuators may be arbitrary. A common simultaneously stabilizing linear feedback is assumed to exist. Strict positivity of each \(q_j\) is used for the boundary coercivity argument, and \(R_j\succ0\) for global coercivity. The proof does not establish convexity for multidimensional-state LQR, switched systems, robust min–max objectives, or neural-network parameterizations. The sharp constant is universal, not necessarily the best bound for a fixed prescribed plant family. A possible uncatalogued prior formulation of the same scalar-state curvature inequality remains a bibliographic risk.

## References

- Abbas Pasdar and Farnaz Adib Yaghmaie, *Policy Iteration for Domain Randomized Linear Quadratic Systems*, arXiv:2609.04794v1, first released 2026-09-04. https://arxiv.org/abs/2609.04794
- Tesshu Fujinami, Bruce D. Lee, Nikolai Matni, and George J. Pappas, *Policy Gradient for LQR with Domain Randomization*, arXiv:2503.24371v1, 2025. https://arxiv.org/abs/2503.24371
- Abbas Pasdar and Farnaz Adib Yaghmaie, *Semidefinite Programming for Domain Randomization in LQR*, European Control Conference, 2026. https://learn2decide-a022b0.gitlab-pages.liu.se/assets/pdf/sdp-domain-randomization-lqr.pdf
- Jhojan A. Rodriguez-Gil and César A. Uribe, *Global Convergence of Policy Gradient Methods for ReLU Controllers in Linear Quadratic Regulation*, arXiv:2604.22138v1, 2026. https://arxiv.org/abs/2604.22138
- Maryam Fazel, Rong Ge, Sham M. Kakade, and Mehran Mesbahi, *Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator*, ICML 2018. https://proceedings.mlr.press/v80/fazel18a.html
