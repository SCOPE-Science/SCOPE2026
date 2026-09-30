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

Let sigma_1 >= sigma_2 >= sigma_3 >= 0 be the singular values of F. For
c>0 the distance to the proper-rotation well c SO(3) is the special
orthogonal Procrustes distance

  dist(F,c SO(3))^2 = ||F||_F^2 + 3c^2
      - 2c (sigma_1+sigma_2+s sigma_3),

where s=+1 when det F >= 0 and s=-1 when det F < 0 (at det F=0 the
last singular value is zero). Thus for det F >= 0 this is
sum_i (sigma_i-c)^2, whereas for det F<0 it is
sum_i (sigma_i-c)^2 + 4c sigma_3. This orientation correction is
essential because the wells are SO(3), not O(3).

Put e1=lam-1=0.138720864453374, ea=lam-alpha=-0.111279135546627,
K1=2e1^2, Ka=2ea^2, W(F0)=3ea^2=0.037149138024013.
Axis split: A=diag(a,lam,lam), B=diag(b,lam,lam),
tA+(1-t)B=F0, energy E(t,a)=tW(A)+(1-t)W(B). On the positive
determinant part of this line the well switch xk solves
(x-1)^2+K1=(x-alpha)^2+Ka, giving xk=1.097558271093253.

## Result

Sharp order-one laminate: the interior optimum on the mixed positive-
determinant branch (A in well 1, B in well alpha) satisfies
a-b=1-alpha=-0.25, i.e. a=lam-(1-t)/4, b=lam+t/4 and
d(t)=(a-1)=(b-alpha)=lam-alpha+t/4. Hence
E(t)=d(t)^2+2t e1^2+2(1-t)ea^2=0.0625t^2+c1t+c0.
The stationary point is
t*=0.335349626559518, a*=0.972558271093253,
b*=1.222558271093253, E*=0.030120427271913. Branch validity holds
with margin 0.125 on each side (a*=xk-0.125, b*=xk+0.125).
Since B-A=(b-a)e1 tensor e1, the pair is rank-one compatible and gives
QW(F0)<=E*. Since every polyconvex function is quasiconvex, PW<=QW,
so PW(F0)<=E* as well. The pair also matches the cofactor and determinant
means of F0.

The omitted orientation-reversing part of the axis line cannot improve
this value. Write x=-u<0. If 0<=u<=lam then for either c in {1,alpha}

  dist(diag(-u,lam,lam),c SO(3))^2
    = (u+c)^2 + 2(lam-c)^2,

whose minimum over u is attained at u=0. If u>=lam, the SO(3)
orientation correction is still larger. Consequently every x<0 has
W(diag(x,lam,lam)) >= min{1+2e1^2, alpha^2+2ea^2} > 1.03 >> E*.
Thus all minimizing axis splits lie in the positive-determinant branches
used above.

Two-atom diagonal classification: let F0=tX+(1-t)Y with X,Y diagonal,
matched cofactor means lam^2 I and matched determinant mean lam^3. The
variance identity

t Xi Xj+(1-t) Yi Yj-(tXi+(1-t)Yi)(tXj+(1-t)Yj)
 = t(1-t)(Xi-Yi)(Xj-Yj)

with left side zero forces (Xi-Yi)(Xj-Yj)=0 for every i!=j, so X,Y
differ in at most one coordinate; the determinant constraint is then
automatic. Hence the feasible set is exactly axis rank-one splits. The
negative-coordinate part is excluded by the SO(3) estimate above. The
positive branches have: (1,1) infeasible (mean lam>xk); (2,2) Jensen
floor W(F0)=0.037149138024013; the mixed branches give E*, equal by
label-swap symmetry; the kink-edge minimum is W(F0). Therefore the
two-atom diagonal minors-matched minimum is exactly E*, attained by the
laminate above up to axis permutation and label swap.

Trace obstruction: a zero-energy gradient Young measure would be
supported on SO(3) union alpha SO(3). The determinant-minor constraint
at F0 forces half of its mass on each well. Its average trace is then at
most (3+3alpha)/2=3.375, whereas tr F0=3lam=3.416163. Hence no
zero-energy gradient Young measure has barycenter F0, and QW(F0)>0.

## Proof and evidence

Closed-form positive-axis derivation in artifacts/order1_exact.py;
exhaustive fine-grid confirmation and branch minima in
artifacts/final_verify.py; kink/edge analysis in artifacts/edge_check.py;
36-direction order-one catalog in artifacts/o1_catalog.py; and numerical
two-atom refinements in artifacts/pw_refine.py and artifacts/pw_refine2.py.
The catalog and refinement searches are supporting computation, not proof.
The laminate bound, the SO(3) orientation correction and negative-axis
exclusion, the variance-identity reduction, the branch/edge minima, and
the trace obstruction are analytic.

## Limitations

Not proved: PW(F0)=QW(F0) or any separating gap delta>0. The
classification covers only two-atom diagonal minors-matched competitors;
non-diagonal and n>=3 cases remain open, as does global laminate
optimality among all gradient microstructures. Dual minorant classes stall
well below E*.

## Reproducibility

Pure-Python scripts under artifacts/ reproduce the numerical constants.
The SO(3) orientation correction used in this repaired statement is a
standard special-orthogonal Procrustes calculation and can also be checked
directly from the SVD trace maximization.

## References

P. H. Schoenemann, A generalized solution of the orthogonal Procrustes
problem, Psychometrika 31 (1966), 1-10, DOI 10.1007/BF02289451.
S. Conti and G. Dolzmann, Relaxation of a model energy for the cubic to
tetragonal phase transformation in two dimensions, arXiv:1403.4877.
Dacorogna, Direct Methods in the Calculus of Variations; Mueller,
Variational models for microstructure and phase transitions; Ball-James,
Fine phase mixtures / two-well problem.
