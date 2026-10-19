# Exact camouflage of a hard triadic ecological interaction on an attracting product manifold

## Finding
For every six-tuple of strictly positive parameters \(\alpha,\kappa,\gamma,\delta,b,d\), there is an elementary pair of three-species population models, one purely pairwise and one possessing a genuinely hard triadic interaction, that produce **identical complete, nonconstant, positive periodic abundance trajectories** on a continuum of initial conditions. The full three-dimensional vector fields are different away from a curved invariant surface. In the higher-order model that surface is transversely attracting with a universal exact exponential rate; in the pairwise model it is neutral. A targeted perturbation across the surface separates the mechanisms immediately.

## Assumptions and scope
Work in the strictly positive octant with \(\alpha,\kappa,\gamma,\delta,b,d>0\). Both models share the autonomous base equations
\[
\dot V=V(\alpha-\kappa W),\qquad
\dot W=W(\gamma V-\delta).
\]
The **pairwise** model adds
\[
\dot U=U G(V,W),\qquad G(V,W)=\alpha-\delta+\gamma V-\kappa W.
\]
The **higher-order** model instead adds
\[
\dot U=U\{G(V,W)+bVW-dU\}.
\]
A per-capita growth law is called pairwise when it is affine in the abundances. Thus the first model is generalized Lotka--Volterra (gLV) of pairwise type; the second includes the *hard* third-species term \(bVW\) in the per-capita growth of \(U\), with \(\partial_V\partial_W(\dot U/U)=b>0\). The coefficient \(d>0\) denotes an independent self-limitation of \(U\); the triadic term vanishes whenever either modifier species is absent. No ecological assertion is made that the displayed food-web topology is typical.

Define
\[
\Sigma=\{(U,V,W)>0:U=(b/d)VW\},
\]
which is a two-dimensional surface, not an open set of three-dimensional initial conditions. Fix any initial state on \(\Sigma\) with \((V,W)\ne(\delta/\gamma,\alpha/\kappa)\). The asserted exact observational equivalence means equality of all three abundance coordinates for all forward time *from that same initial state*; it does not claim equality for arbitrary initial states or structural identifiability from multiple designed perturbation experiments.

## Proof
**1. The base flow has a continuum of positive periodic orbits.** The classical first integral is
\[
H(V,W)=\gamma V-\delta\log V+\kappa W-\alpha\log W.
\]
Direct differentiation using the two base equations gives \(\dot H=0\). The Hessian is \(\operatorname{diag}(\delta/V^2,\alpha/W^2)\), so \(H\) is strictly convex with its unique minimum at \((V_*,W_*)=(\delta/\gamma,\alpha/\kappa)\). The function diverges as either coordinate approaches zero or infinity. Every level above the minimum is therefore a compact smooth simple closed oval lacking stationary points; on each such oval the nonzero planar vector field generates a periodic motion of some period \(T>0\). The stationary minimum is explicitly excluded from the nonconstant conclusion.

**2. The two vector fields coincide on an invariant product graph.** Let \(P=VW\). Their common base flow gives
\[
\dot P=P\{(\alpha-\kappa W)+(\gamma V-\delta)\}=P G(V,W).
\]
For the pairwise equation \(U/P\) is conserved, so the graph \(U=(b/d)P\) is invariant. On that same graph the added higher-order contribution equals \(bP-dU=0\), and thus the higher-order \(U\)-equation exactly reduces to the pairwise equation. Local uniqueness and positivity prove that both solutions starting on \(\Sigma\) remain there and agree at every time. The preceding first-integral argument gives uncountably many nonconstant positive periodic base orbits; each uniquely lifts to \(U=(b/d)VW\). The higher-order interaction is not a disguised zero coefficient: \(b>0\) and the per-capita mixed partial derivative equals \(b\) at every point of the positive orthant.

**3. Exact transverse dynamics and all-time relaxation.** Define the dimensionless deviation
\[
S(t)=\frac{bV(t)W(t)}{dU(t)}-1>-1.
\]
Using \(\dot P/P=G\), in the higher-order model
\[
\dot S=(1+S)\{dU-bVW\}=-bVW S.
\]
In the pairwise model the corresponding derivative is zero. Consequently
\[
S(t)=S(0)\exp\!\left(-b\int_0^t V(s)W(s)\,ds\right).
\]
An explicit antiderivative along the common base system follows from
\[
VW=\frac{\alpha}{\kappa}V-\frac{1}{\kappa}\dot V,
\qquad V=\frac{\delta+\frac d{dt}\log W}{\gamma}:
\]
\[
\int_0^t VW\,ds=
\frac{\alpha\delta}{\kappa\gamma}t+
\frac{\alpha}{\kappa\gamma}\log\frac{W(t)}{W(0)}-
\frac{V(t)-V(0)}{\kappa}.
\]
Since all positive nonstationary base trajectories are bounded and periodic, the correction after the linear term is bounded. Thus for \(S(0)\ne0\),
\[
\lim_{t\to\infty}\frac1t\log|S(t)|=-\frac{b\alpha\delta}{\kappa\gamma}.
\]
For a period \(T\), periodicity gives \(\int_0^T VW\,dt=T\alpha\delta/(\kappa\gamma)\). Hence the transverse multiplier of the higher-order orbit is exactly
\[
\rho_{\perp}=\exp\!\left(-\frac{b\alpha\delta}{\kappa\gamma}T\right)<1;
\]
in the pairwise model it equals \(1\). This is normal attraction to the *surface*, not orbital asymptotic stability of any individual closed curve: the base subsystem has a first integral and therefore an independent neutral direction.

**4. A controlled intervention exposes the hidden term.** At the same positive state the difference between per-capita growth rates of \(U\) in the two systems is
\[
\frac{\dot U_{\rm higher}}{U}-\frac{\dot U_{\rm pairwise}}{U}=bVW-dU=-d\bigl(U-(b/d)VW\bigr).
\]
Displacing \(U\) alone by any sufficiently small nonzero \(\varepsilon\), while holding \(V,W\) fixed on a shared orbit, makes this discrepancy \(-d\varepsilon\ne0\). Consequently perfect agreement of unperturbed abundance records does not imply agreement under controlled interventions.

## Verification
The standalone script `verify.py` checks the two invariant-surface identities, the mixed Hessian, conservation of the Lotka--Volterra first integral, the exact differential equation for \(S\), and the derivative of the explicit integral formula using SymPy. SciPy trajectories then check the formula at on-surface and off-surface initial conditions and independently integrate the two models on the shared surface. Run `python verify.py` after installing `requirements.txt`. These finite checks corroborate the algebra but do not replace the analytic periodic-orbit and infinite-time proofs given above.

## Relationship to prior work
Calleja-Solanas and collaborators (arXiv:2605.06301v1) present the substantive ecological identifiability question, including numerically **near-matching** trajectories between higher-order Lotka--Volterra systems and fitted pairwise models; their Results show correlation near \(0.99\) for a three-species example. The construction here is different: it achieves **literal equality for all time** on an explicit positively invariant curved surface, proves an exact continuum of nonconstant orbits, and computes their opposite normal multipliers and an intervention diagnostic. These claims are not consequences of a numerical fit with correlation below one.

Llabrés and collaborators (arXiv:2601.05169v1) investigate reductions of hypergraph social-impact update rules to pairwise representations, not same-coordinate ecological gLV trajectories. Peixoto and collaborators (arXiv:2602.16937v1) analyze representational expressivity of graphs; Lacasa (arXiv:2602.21727v1) discusses graph/nonlinear versus higher-order/linear lifts. Neither provides the displayed all-time three-species Lotka--Volterra construction in the material inspected. Kleinhesselink and collaborators (DOI 10.1111/ele.14022) discuss definitions and detection of hard ecological higher-order interactions. The present calculation uses classical Lotka--Volterra integrability, an elementary invariant graph, and a scalar multiplicative discrepancy equation; **none of those tools separately is asserted to be new**.

## Limitations
The exact correspondence is deliberately non-generic: the initial conditions must satisfy the codimension-one equation defining \(\Sigma\), and the parameters obey the specified matching algebra. It does not extend to open sets of initial states. The planar base cycles are neutrally stable rather than isolated attracting limit cycles; only the transverse direction is attracting in the higher-order system. There is no claim of robustness to parameter errors, measurement noise, stochastic forcing, or universal ecological frequency of this arrangement. The result is a mathematically exact structural counterexample to unconditional identifiability from a single unperturbed all-time trajectory, not a statement that designed perturbations or additional data cannot distinguish mechanisms. The motivating source's supporting material was not independently verified; a broader invariant-manifold observability theorem could subsume a portion of the conclusion.

## References
1. V. Calleja-Solanas, S. Lamata-Otín, C. Gómez-Ambrosi, J. Gómez-Gardeñes, and S. Meloni, *Higher-order interactions in ecology can be hidden in plain sight*, arXiv:2605.06301v1 (first posted 2026-05-07). https://arxiv.org/html/2605.06301v1
2. J. Llabrés, R. Toral, M. San Miguel, and F. Vázquez, *Reducibility of higher-order to pairwise interactions: Social impact models on hypergraphs*, arXiv:2601.05169v1. https://arxiv.org/html/2601.05169v1
3. T. P. Peixoto, L. Peel, T. Gross, and M. De Domenico, *Graphs are maximally expressive for higher-order interactions*, arXiv:2602.16937v1. https://arxiv.org/html/2602.16937v1
4. L. Lacasa, *On the equivalence between nonlinear graph-based dynamics and linear dynamics on higher-order networks*, arXiv:2602.21727v1. https://arxiv.org/html/2602.21727v1
5. E. Kleinhesselink and collaborators, *Detecting and interpreting higher-order interactions in ecological communities*, Ecology Letters (2022), DOI:10.1111/ele.14022. https://onlinelibrary.wiley.com/doi/10.1111/ele.14022
6. P. Yodzis, *The Indeterminacy of Ecological Interactions as Perceived Through Perturbation Experiments*, Ecology 69 (1988), 508–515, DOI:10.2307/1940449 (abstract inspected). https://esajournals.onlinelibrary.wiley.com/doi/10.2307/1940449
