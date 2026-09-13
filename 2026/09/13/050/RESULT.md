# Quotient Rossi Bubble-Witness Obstruction on the Lens Space L = S^3/Z_2

## Context

The admitted target asks for a two-sided dichotomy on the lens quotient
L = S^3/Gamma, Gamma = {+-I} of order 2, with quotient Rossi CR structures
J_t^quot induced by Z_{1,t} = Z_1 + t conj(Z_1), real |t| < 1:
(A) a strict quotient gap inf Q_t^quot <= Y_{quot,0} - c t^2 witnessed by an
explicit Heisenberg-bubble trial function lifted from S^3, or (B) quotient
rigidity inf Q_t^quot = Y_{quot,0}. This record resolves the fixed-witness
part of (A) negatively and leaves global (B) open.

## Definitions

S^3 carries its standard CR structure with contact form theta_0 held fixed;
only the CR structure deforms. pi: S^3 -> L is the degree-2 covering.
J_0^quot is the standard quotient CR structure; J_t^quot are quotient Rossi
structures. For n = 1 the CR Yamabe quotient is
Q[u] = int(a|nabla_b u|^2 + R u^2)dV / (int u^4 dV)^{1/2} with a = 4, up to a
fixed overall normalization; all ratio arguments are normalization-free.
Y_{quot,0} = inf Q_0^quot on L; Y(S^3) is the standard sphere infimum.
U(r,tau) = ((1+r^2)^2 + tau^2)^{-1/2} is the Heisenberg bubble profile.
A single-ball bubble means a Heisenberg bubble concentrated in one evenly
covered ball of L at fixed scale and cutoff. Descending-mode coupling means
U + e Re[z_1^2] F with fixed amplitude e or fixed ratio alpha = e/t, where
phi = Re(z_1^2) descends to L.

## Result

Theorem (fixed-witness obstruction). On L = S^3/Z_2 with the structures above:
(i) Y_{quot,0} = Y(S^3)/sqrt(2), so Y(S^3) = sqrt(2) Y_{quot,0}, a fractional
distance 1 - 1/sqrt(2) ~ 0.2929 above threshold.
(ii) Any single-ball concentrated Heisenberg-bubble trial function at fixed
scale/cutoff has Q_0^quot -> Y(S^3) in the concentration limit, and Rossi
expansion Q_t^quot = Q_0^quot (1 + 2t^2 + O(t^4)) with no linear term; the bulk
Dirichlet factor is exactly D_t = D_0 (1+t^2)/(1-t^2).
(iii) Hence no fixed trial function of this class -- single-ball bubble at
fixed parameters, or bubble-plus-descending-mode coupling with fixed e or
fixed alpha = e/t -- can satisfy Q_t^quot <= Y_{quot,0} - c t^2 with c > 0 for
small |t|.
(iv) Constants are uniformly strictly stable: the lowest Gamma-descending
eigenfunction phi = Re(z_1^2) has -Delta_b phi = 2 phi with an 8:1 stability
margin, no e.t cross term at (e,t) = (0,0), and positive-definite joint
(e,t) Hessian for small t.

In particular the literal alternative (A) via the stated single-ball bubble
class is impossible. Global rigidity (B) over all trial functions is open.

## Proof and evidence

Covering identity: for u on L with lift tilde u = u o pi, local integrands
agree while volumes double, so numerator doubles and int tilde u^4 = 2 int u^4,
giving Q_{S^3}[tilde u] = sqrt(2) Q_L[u]. Constants lift to constants; the
Jerison-Lee minimizers give Y(S^3) as the universal local lower bound and
constants on L attain Y(S^3)/sqrt(2), proving (i).
Rossi deformation with fixed contact form: with unitary frame
Z_t = (Z_1 + t bar Z_1)/sqrt(1-t^2), Levi factor 1-t^2 and Webster curvature
R_t = 2(1+t^2)/(1-t^2) = 2 + 4t^2 + O(t^4), even in t. For real u,
|Z_t u|^2 = ((1+t^2)|S|^2 + 2t Re[S^2])/(1-t^2) with S = Z_1-part; the cross
term 2t Re[S^2] is the only possible linear decrease. For radial U,
Z_1 U = e^{-i theta} a(r,tau) so (Z_1 U)^2 carries charge e^{-2i theta} with
zero S^1-fiber mean: int Re[(Z_1 U)^2] = 0, giving (ii) and expansion (5).
For V = r^2 cos(2 theta) F, exact differentiation gives
Z_1 V = (e^{i theta} C_1 + e^{-3i theta} C_3)/sqrt(2); then A bar B, Re[A^2],
Re[B^2] all have zero mean and only Re[AB] survives at order t e with
Cauchy-Schwarz bound J^2 <= I_0 I_2, so the second-order bulk plus curvature
form cannot close the O(1) gap at small t. Stability: phi has Dirichlet ratio
2 versus R/8 = 1/4, int (Z_1 phi)^2 = 0 by charge, hence positive joint
Hessian. Numerical certificate output/artifacts/bubble_margin.py reproduces
D_0 ~ 1.2077, int U^4 ~ 2.4667, relative Rossi shifts 0.0202/0.0833/0.1978 at
t = 0.1/0.2/0.3 versus required 0.2929 drop, and S^3 Monte Carlo
(mean phi ~ 6e-4, E[phi^2] ~ 1/6) confirming mode statistics.

## Limitations

Covers single-ball concentrated bubbles at fixed scale/cutoff and stated
descending-mode couplings, not arbitrary multi-bubble or non-concentrating
sequences. The concentrated-bubble limit uses the cited Jerison-Lee blow-up
characterization. Uniform Rossi-family Sobolev constants and bubble-tree
quantization are not established. Global lower bound (B) remains open.

## Reproducibility

Run python3 output/artifacts/bubble_margin.py (numpy only, seed 0); expected
D0 = 1.2077452900790793, L4^4 = 2.466720122734973, margin 0.29289321881345254,
relative shifts and phi statistics as above. Full derivation in DRAFT record.

## References

D. Jerison and J. M. Lee, Extremals for the Sobolev inequality on the
Heisenberg group and the CR Yamabe problem, JAMS 1988; The Yamabe problem on
CR manifolds, J. Differential Geom. 1987. J.-H. Cheng, A. Malchiodi, P. Yang,
On the Sobolev quotient of 3D CR manifolds, Rev. Mat. Iberoam. 2023 (Rossi
spheres, negative mass, non-attainment). C. Afeltra and A. Pinamonti, A CR
structure with blowing up solutions to the CR Yamabe problem, arXiv:2501.08782
(2025). C. Sung and Y. Takeuchi, The CR Yamabe constant and inequivalent CR
structures, Pacific J. Math. 2025. J.-H. Cheng and H.-L. Chiu, Connected sum
of spherical CR manifolds, arXiv:1805.08485.
