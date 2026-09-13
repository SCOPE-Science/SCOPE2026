# Sharp hydrostatic-midpoint laminate and two-atom diagonal polyconvex classification

## Context

Let alpha=1.25, K=SO(3) union alpha SO(3), W(F)=dist(F,K)^2, and
F0=lam I_3 with lam^3=(1+alpha^3)/2=1.4765625, lam=1.138720864453374.
Denote by PW the polyconvex envelope (supremum of polyconvex functions
below W, i.e. convex functions of (F,cof F,det F)) and by QW the
quasiconvex envelope. The admitted target S2 asks whether
PW(F0)=QW(F0) with an explicit minors-supported lower bound saturated
by a laminate, or a certified gap. The full equality remains open; this
record states the sharp proved intermediate finding that any eventual
resolution must respect.

## Definitions

Singular-value formula: for singular values nu_1,nu_2,nu_3,
W(F)=min{(nu_1-1)^2+(nu_2-1)^2+(nu_3-1)^2,
(nu_1-alpha)^2+(nu_2-alpha)^2+(nu_3-alpha)^2}.
Put e1=lam-1=0.138720864453374, ea=lam-alpha=-0.111279135546627,
K1=2e1^2, Ka=2ea^2, W(F0)=3ea^2=0.037149138024013.
Axis split: A=diag(a,lam,lam), B=diag(b,lam,lam),
tA+(1-t)B=F0, energy E(t,a)=tW(A)+(1-t)W(B).
True line kink xk solves (x-1)^2+K1=(x-alpha)^2+Ka,
xk=1.097558271093253.

## Result

Sharp order-one laminate: the interior optimum on the mixed branch
(A in well 1, B in well alpha) satisfies a-b=1-alpha=-0.25, i.e.
a=lam-(1-t)/4, b=lam+t/4, d(t)=(a-1)=(b-alpha)=A0+t/4 with
A0=lam-1.25, E(t)=d(t)^2+2t e1^2+2(1-t)ea^2=0.0625t^2+c1t+c0.
Stationary point t*=0.335349626559518 in (0,1),
a*=0.972558271093253, b*=1.222558271093253,
E*=0.030120427271913. Branch validity holds with margin 0.125 each
side (a*=xk-0.125, b*=xk+0.125). Rank-one compatibility
B-A=(b-a)e1 tensor e1 gives QW(F0)<=E*. The pair is minors-matched
(mean cof=lam^2 I, mean det=lam^3), so PW(F0)<=E* too.

Two-atom diagonal classification: let F0=tX+(1-t)Y with X,Y diagonal,
matched cofactor means lam^2 I and matched determinant mean lam^3.
The variance identity
tXiXj+(1-t)YiYj-(tXi+(1-t)Yi)(tXj+(1-t)Yj)=t(1-t)(Xi-Yi)(Xj-Yj)
with LHS=0 forces dEi dEj=0 for all three pairs, so X,Y differ in at
most one coordinate; the determinant constraint is then automatic.
Hence the feasible set is exactly axis rank-one splits. Branch minima:
(1,1) infeasible (mean lam>xk); (2,2) Jensen floor W0=0.037149138024013
(margin 0.0070287108 over E*); (1,2) and (2,1) give E*, equal by
label-swap symmetry; kink-edge minimum is W0 at t=0. Therefore the
two-atom diagonal polyconvex minimum equals E*, attained at the above
laminate up to axis permutation/label swap.

Trace obstruction: average-trace capacity of K is (3+3alpha)/2=3.375
< 3lam=3.416163=tr F0, so with determinant-mean constraint any
zero-energy gradient Young measure is impossible; QW(F0)>0.

## Proof and evidence

Closed-form derivation in output/artifacts/order1_exact.py; exhaustive
fine-grid confirmation (min 0.030120441975) and branch minima in
output/artifacts/final_verify.py; true-kink/edge analysis with margins
in output/artifacts/edge_check.py; 36-direction order-one catalog in
output/artifacts/o1_catalog.py (minimum E* only at axis stretches);
MU-ramp two-atom refinement converging to E* with penalty 5.6e-17 in
output/artifacts/pw_refine.py and pw_refine2.py. Catalog and stability
searches are conjecture support, not proof; the laminate bounds,
variance-identity reduction, branch/edge minima, and obstruction are
proved.

## Limitations

Not proved: PW(F0)=QW(F0) or any separating gap delta>0. The
classification covers only two-atom diagonal minors-matched
competitors; non-diagonal and n>=3 cases remain open, as does global
laminate optimality among all gradient microstructures. Dual minorant
classes stall at 0.003-0.011 versus E*=0.0301.

## Reproducibility

Pure-Python stdlib scripts listed above reproduce all constants from
first principles; run e.g. `python3 output/artifacts/order1_exact.py`
and `python3 output/artifacts/edge_check.py`.

## References

Conti-Dolzmann, Relaxation of a model energy for the cubic to
tetragonal phase transformation in two dimensions, arXiv:1403.4877
(nearest prior 2D tetragonal relaxation; 3D case stated open therein);
Dacorogna, Direct Methods in the Calculus of Variations; Mueller,
Variational models for microstructure and phase transitions;
Ball-James, Fine phase mixtures / two-well problem.
