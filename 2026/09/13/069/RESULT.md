# Threshold bifurcation for f_t = A_b o S_t: exact neutral fixed point and rigorous upper bound t_c <= (sqrt(3)-1)/(4*pi)

## Context

The admitted target asks whether Anosov maps f_t = A_b o S_t on T^3, with A_b the toral automorphism induced by [[3,1,0],[1,1,1],[0,1,1]] and S_t(x) = (x_1+2t sin(2pi x_2), x_2+2t sin(2pi x_3), x_3) mod 1, admit uniform exponential mixing constants over all Anosov parameters t < t_c, or instead exhibit quantitative critical slowing as t approaches the Anosov threshold t_c from below. The threshold t_c = sup{tau in (0,1] : f_s Anosov for all s in [0,tau)} is positive by openness of the Anosov property. The submitted finding advances the target by producing the first rigorous quantitative upper bound on t_c with an explicit bifurcation mechanism.

## Definitions

Let T^3 = R^3/Z^3 with Lebesgue measure m. S_t is triangular with Jacobian determinant 1, hence Lebesgue-preserving; A_b has determinant -1, so each f_t = A_b o S_t preserves m. A_b is symmetric with eigenvalues approximately -0.1700865, 1.6888922, 3.4811943, so f_0 = A_b is volume-preserving Anosov with dim E^u = 2, dim E^s = 1. (These correct the approximate moduli 4.330, 1.798, 0.128 stated in the topic text.) Let p2 = (1/2, 0, 1/2) and t* = (sqrt(3)-1)/(4pi) ~ 0.0582548.

## Result

Theorem. (a) f_t(p2) = p2 for every t in [0,1]. (b) Df_t(p2) = A_b [[1,s,0],[0,1,-s],[0,0,1]] with s = 4 pi t, and det(Df_t(p2)-I) = s^2+2s-2, vanishing exactly at s* = sqrt(3)-1, i.e. t = t*, transversely with derivative 2 sqrt(3). (c) At t*, spec(Df_{t*}(p2)) = {1, 2+sqrt(5), 2-sqrt(5)} ~ {1, 4.236068, -0.236068}; the eigenvalue 1 is simple. Hence f_{t*} is not Anosov. (d) Consequently t_c <= t* ~ 0.05825. (e) The weak unstable multiplier mu(t) with mu(0) ~ 1.689 and mu(t*) = 1 satisfies d mu/dt|_{t*} = -2 pi sqrt(3) ~ -10.88, approaching 1 linearly from above (tracked: 1.4409 at t=0.02, 1.2047 at t=0.04, 1.0911 at t=0.05, 1.0006 at t=0.0582).

## Proof / Evidence

(a) sin(2pi*0)=0 and sin(2pi/2)=sin(pi)=0 give S_t(p2)=p2; A_b p2 = (3/2,1,1/2) = p2+(1,1,0) is p2 mod 1. (b) DS_t(x) = [[1,4pit cos(2pi x_2),0],[0,1,4pit cos(2pi x_3)],[0,0,1]]; at p2 the cosines are (1,-1), giving the displayed product with s=4pit. Then M(s)-I = [[2,3s+1,-s],[1,s,1-s],[0,1,-s]] whose determinant expands symbolically to s^2+2s-2 with roots -1+-sqrt(3); only s*=sqrt(3)-1 lies in [0,4pi]. Transversality: d/ds = 2(s+1) = 2 sqrt(3) at s*. (c) The characteristic polynomial -lam^3+5 lam^2+(s^2+2s-5) lam-1 specializes via s^2+2s=2 to -(lam-1)(lam^2-4lam-1), giving the stated spectrum with the other two multipliers off the unit circle. (d) Every fixed point of an Anosov diffeomorphism is hyperbolic; the eigenvalue-1 fixed point p2 at t* rules out Anosov there, and the sup definition of t_c yields t_c<=t*. (e) Exact left/right nullvectors of M(s*)-I give d mu/ds = (u' M' v)/(u' v) = -sqrt(3)/2 with M'(s) = [[0,3,-1],[0,1,-1],[0,0,-1]]; multiplying by ds/dt=4pi gives -2 pi sqrt(3). All identities were independently re-derived by symbolic computation; the script output/artifacts/bifurc.py reproduces them and the eigenvalue tracking.

## Limitations

This result proves the upper bound t_c<=t* and the exact mechanism. It does not prove t_c=t* (Anosov persistence on all of [0,t*) would need a separate cone certificate; a first constant-Lorentz-cone attempt certified the stable direction but not the unstable one) and does not prove non-uniformity of mixing rates. The inequality rho_opt(t)>=1/mu(t), hence rho_opt->1 as t->t_c^-, is stated as conjecture, not theorem.

## Reproducibility

Run `python3 output/artifacts/bifurc.py` (requires sympy, numpy). It prints A_b symmetry and determinant, det(M-I) and roots for all four shear-cosine classes, the characteristic polynomial, eigenvalue tracking for 0<=t<=t*, fixed-point residue checks, and the slope -2 pi sqrt(3).

## References

Inputs: topic.json (target definition), DRAFT.md (theorem and proof), research_report.json (EMERGENT_FINDING claim), target_exit.json (route assessment), artifacts/bifurc.py (verification script); STANDARD.md sky-survey-admission-depth-gate-v12; independent sympy/numpy re-derivation; scope_literature_search fused results (generic Anosov surveys only, no covering prior work).
