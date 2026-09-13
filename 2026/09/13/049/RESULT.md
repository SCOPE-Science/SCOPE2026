# Rossi reference CR Yamabe flow: alternative (A) holds with delta = 1/4

## Context

On the Rossi family of CR structures on S^3 = SU(2), the CR Yamabe problem admits a solution for every deformation parameter (Gamara–Yacoub), while the pseudohermitian mass is negative for small nonzero parameters (Cheng–Malchiodi–Yang). Recent work (Afeltra–Pinamonti–Ho, 2026) exhibits, for small Rossi parameters, some initial contact form whose normalized CR Yamabe flow develops a one-bubble concentration regime. The question audited here fixes instead the reference initial data theta0 itself and asks which side of the dichotomy holds: reference convergence (A) or reference bubbling (B).

## Definitions

Let (J_0, theta0) be the standard strictly pseudoconvex structure on S^3 = SU(2) with left-invariant (1,0) field Z_1, conjugate Z_{1bar}, Reeb field T, and dual coframe theta^1, theta^{1bar}, theta0. For constant real t with |t| < 1 define Z_{1,t} = Z_1 + t Z_{1bar}, Z_{1bar,t} = Z_{1bar} + t Z_1, and J_t by H_t^{1,0} = span Z_{1,t}. Theta0 is kept fixed as the background contact form; the unit-volume reference data is the constant multiple hat-theta0 = c theta0 with c = V0^{-1/2}, V0 = integral theta0 wedge dtheta0, t-independent. The normalized CR Yamabe flow is theta(s) = u(s)^2 hat-theta0 with unit-volume constraint integral u(s)^4 dV = 1 and stationary points exactly at constant-Webster-curvature forms.

## Result

With explicit delta = 1/4, for every 0 < |t| < delta the normalized CR Yamabe flow from the fixed reference data exists globally in s >= 0, is stationary theta(s) = theta(0), hence converges smoothly to a constant-Webster-curvature limit. Alternative (B) does not occur: no sequence t_k -> 0 in range develops a one-bubble regime. The deviation satisfies ||u(s)-1||_{C^k} = 0 for all k and s, and curvature is uniformly bounded on [0,infty) x [-delta,delta].

## Proof / evidence

Left-invariance: Z_{1,t}, Z_{1bar,t} have constant coefficients in left-invariant fields, so J_t is left-invariant; theta0 is left-invariant. Hence each SU(2) left translation L_g satisfies L_g^* theta0 = theta0 and dL_g J_t = J_t dL_g, giving a transitive pseudohermitian automorphism group of (J_t, theta0). Dual coframe theta^1_t = (theta^1 - t theta^{1bar})/(1-t^2) (verified symbolically in output/artifacts/verify_coframe.py); then dtheta0 = i theta^1 wedge theta^{1bar} = i(1-t^2) theta^1_t wedge theta^{1bar}_t, so theta0 is compatible with J_t with Levi eigenvalue h_t = 1-t^2 >= 15/16 on |t| <= 1/4, giving uniform strict pseudoconvexity. By naturality of the Tanaka–Webster connection under pseudohermitian maps and transitivity, Webster curvature R_t and torsion are constant functions for each fixed t; equivalently the structure equations have constant coefficients. Volume form theta0 wedge dtheta0 uses only fixed forms, so unit-volume rescaling is a single t-independent constant preserving curvature constancy. Constant-curvature data satisfies F(1,R,bar-R) = 0 in the normalized flow (Ho; Chang–Chiu), so u = 1 is the exact solution; standard short-time existence and uniqueness identifies it as the reference flow, extended globally by continuation. Exclusion of (B) is immediate from stationarity with bounded constant curvature. Scripts verify_coframe.py and uniform_bounds.py re-executed and passing.

## Limitations

Relies on cited standard short-time existence/uniqueness and stationarity of constant-Webster-curvature data on compact strictly pseudoconvex 3-manifolds (Ho 2007; Chang–Chiu 2008/2010); requires t constant and real as in the target; claims no closed-form value of R_t beyond constancy and uniform boundedness; does not address flows from non-reference initial data, where Afeltra-type bubbling occurs.

## Reproducibility

Run python3 output/artifacts/verify_coframe.py and python3 output/artifacts/uniform_bounds.py; check duality M^{-1}, wedge factor 1-t^2, bound 15/16, c^2 volume scaling, and zero flow deviation. Standard flow references supply the PDE background.

## References

Ho, long-time existence of CR Yamabe flow; Ho–Sheng–Wang, convergence under mass positivity; Chang–Chiu, CR Yamabe flow estimates; Gamara–Yacoub, CR Yamabe existence; Cheng–Malchiodi–Yang arXiv:2309.02278, homogeneous Rossi data and R(s); Afeltra–Pinamonti–Ho arXiv:2606.27164, one-bubble non-convergence for some data.
