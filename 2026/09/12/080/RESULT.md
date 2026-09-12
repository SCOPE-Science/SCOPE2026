# Short-horizon projected-Verlet drift lower bound with work ledger

## Context
Constrained geometric integration of the planar Cartesian double pendulum is a
standard benchmark distinguishing naive projection methods from symplectic
constrained methods (SHAKE/RATTLE). The admitted target asks, for a fixed
short horizon T*=10, whether the projected-Verlet baseline exhibits a
certifiable linear-in-h energy drift bounded below, together with an explicit
projection-work ledger in the Lagrange multipliers, using only short-horizon
trajectory analysis without invoking any long-time RATTLE uniform bound.

## Definitions
- System: planar double pendulum in Cartesian variables, q=(q1,q2) in R^4,
  M=I, U(q)=g(y1+y2), g=9.81, H(q,p)=|p|^2/2+U(q).
- Constraints: g1(q)=|q1|^2-1=0, g2(q)=|q2-q1|^2-1=0, G(q)=Dg(q) (2x4),
  S(q)=G(q)G(q)^T.
- Consistent librational data: g(q)=0, G(q)p=0, parametrized by
  (th1,th2,w1,w2) with H0 in [-12,-8], |wi|<=2.
- Projected-Verlet step of size h: one unconstrained kick-drift-kick with
  constant force a=(0,-g,0,-g), then orthogonal position projection
  (multiplier mu) and momentum projection (multiplier nu) via
  qn-q*+G(qn)^T mu=0, g(qn)=0 and pn=p*-G(qn)^T nu, G(qn)pn=0.
- N=floor(T*/h) with T*=10.

## Result
There exist a nonempty open set U of consistent librational data, c1=100>0,
C0=0, h0=0.01, C1=100 such that for every h in (0,h0] and every initial datum
in U, at N=floor(10/h):
  |H(qN,pN)-H0| >= 100 N h^3 - 0*h^2,
  |H(qN,pN)-H0| <= 100 N max_{k<=N}(|mu_k|+|nu_k|) + 0*h^2.
Witness: anchor zA=(0.840,0.842,1.918,1.782), H0=-10.9445; U is the ball of
radius 0.03 (angles) x 0.06 (velocities) about zA intersected with the
consistent-data manifold. No long-time RATTLE uniform bound is invoked.

## Proof / evidence
1. Exact single-step lemma. Because -gradU is constant, kick-drift-kick
preserves H exactly: with p_half=p-ha/2, q*=q+h p_half, p*=p-ha,
|p*|^2-|p|^2=-2h a.p+h^2|a|^2 and U(q*)-U(q)=h a_U.p_half with a_U=-a, so
H(q*,p*)=H(q,p) to machine precision (~1e-15, verified). Hence the per-step
increment Wk=H(qn,pn)-H(q,p) equals pure projection work.
2. Per-step expansion. With e=(2|v1|^2,2|v2-v1|^2), Ga=G(q)gradU(q),
det S=16(2-c^2)>=16 on the manifold (c=q1.(q2-q1) in [-1,1]), mu=O(h^2),
nu=O(h), kinetic work -f^T S^{-1} f/2 (verified to ~1e-16), potential work
-Ga^T S^{-1} g*, giving Wk=h^2 w(z)+O(h^3) with
w(z)=-(1/2) e^T S^{-1} (e-Ga), uniform on the compact shell. Richardson
validation: W/h^2=-59.95,-62.34,-63.54,-64.14 at h=0.02,0.01,0.005,0.0025,
converging to wdens=-64.74 at the anchor.
3. Short-horizon accumulation. Finite-time Gronwall tracking gives
sup_{k<=N}|zk-z(kh)|=O(h^2) with constant depending only on T*=10, so
D_N=sum Wk satisfies |D_N|~|I|h with I(z0)=int_0^{10} w(z(t))dt.
Exact-flow RK4 quadrature (dt=0.004 vs 0.002, 4-digit agreement) gives
I(zA)=-1719 and I in [-1738,-1628] on axis perturbations of U, all <=-1600.
Since N h^3~10h^2 and |D_N|~1600h, the ratio |D_N|/(N h^3)~|I|/(10h) grows
like 1/h; h=0.01 is the hardest case. Discrete logs confirm:
|D|/(N h^3)=8041 (h=0.01), 20673 (h=0.005) at the anchor; >=18700 on the
U-ball; fresh auditor checks at h=0.007,0.003,0.001 give 13122,41345,152953.
All exceed c1=100 by >=80x. The disproof alternative (uniform O(h^2) cap) is
refuted since |dH|/h^2~8e4-2e5 and grows as h decreases.
4. Ledger. |U-work|<=|gradU||G||mu|, |T-work|<=sup|p||G||nu|; on the shell
|gradU|<=14, |p|<=6, |G|<=4, so L0<=100 suffices; measured C1eff<=0.023
(4000x margin). Take C1=100, C0=0.

## Limitations
The uniform passage from the integral certificate to all h in (0,0.01] uses
standard short-horizon Taylor/Gronwall tracking whose remainder constants are
margin-certified (80x-4000x, two mesh scales, Richardson fits) rather than
enclosed by interval arithmetic. Exact-flow quadrature uses RK4 with mesh
refinement agreement, not validated enclosure. Only the librational regime
H0 in [-12,-8], |w|<=2 is covered. Projection Newton tolerance 1e-14.

## Reproducibility
numpy-only scripts: core.py (step, projections, multipliers, wdens),
run_anchor.py -> table_anchor.json (anchor + U-ball discrete logs),
run_exact.py (exact-flow mean-w), verify_w.py and fitw.py (single-step
density validation). Re-run with python3 run_anchor.py and run_exact.py;
auditor independently reproduced exact preservation, the T-work identity,
the Richardson ladder, and fresh h/U-ball ratios.

## References
- S. Reich, Backward error analysis for numerical integrators (SIAM JNA 1999):
  near-conservation upper bounds for (unconstrained) symplectic methods.
- B. Moore & S. Reich, Backward error analysis for multi-symplectic methods:
  modified conservation laws to higher order.
- M. West, Variational Integrators (thesis): SHAKE/RATTLE constrained
  variational equivalence, symplectic-on-manifold property.
- B. Leimkuhler et al., Symplectic numerical integrators in constrained
  Hamiltonian systems: RATTLE symplecticity and time reversibility.
- F. Vesely, Of pendulums, polymers, and robots: Cartesian-constraint
  computational mechanics survey.
