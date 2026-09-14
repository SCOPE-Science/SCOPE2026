# Goh Abnormal Endpoints in the Free Carnot Group F_{3,3}: Explicit Codimension-2 Container and Exact Codimension 7

## Context

Let F_{3,3} be the free Carnot group of rank 3 and step 3 with left-invariant rank-3
distribution D. Its Lie algebra is f = V_1 (+) V_2 (+) V_3 with dimensions (3,3,8),
so dim F_{3,3} = 14. The sub-Riemannian Sard program asks whether the abnormal set
(the critical values of the endpoint map End: L^2([0,1],R^3) -> F_{3,3}) lies in a
proper algebraic subvariety and of which codimension. Prior work established only
existence: Le Donne-Montgomery-Ottazzi-Pansu-Vittone proved the Algebraic Sard
property for free rank-3 step-3 groups (some unspecified proper container), and
Le Donne-Leonardi-Monti-Vittone classified abnormal/Goh curves via extremal
polynomials without giving F_{3,3}-specific explicit equations or a closure
dimension. No prior source recorded explicit containing equations or the exact
dimension for the Goh part of the abnormal set in F_{3,3}.

## Definitions

A horizontal curve is singular (abnormal) if it is a critical point of End. It
satisfies the Goh condition identically if all brackets [X_i,X_j] pair to zero
against the abnormal covector for all t. Let S denote the set of endpoints of all
nontrivial singular horizontal curves satisfying the Goh condition identically.
Use exponential coordinates (x,y,z) in R^3 x R^3 x R^8, where x is on V_1,
y=(a,b,c) is on ([x_1,x_2],[x_1,x_3],[x_2,x_3]), and (z_1,z_2) is on
([x_1,[x_1,x_2]],[x_1,[x_1,x_3]]). Define
Q(x,y) = x_1 c - x_2 b + x_3 a,  E_1(y,z) = -a z_2 + b z_1.

## Result

1. S is contained in the proper real-algebraic subvariety V(Q,E_1), which has
   codimension exactly 2 (smooth of codimension 2 at an exhibited point with
   independent gradients).
2. The Zariski closure of S is irreducible of dimension 7, hence codimension
   exactly 7. The smallest codimension of a containing proper algebraic
   subvariety actually attained (by the closure itself) is 7; the codimension-2
   container above is valid but not optimal.
3. The bound is realized by genuine Goh abnormal curves: the straight kernel
   line gamma(t)=exp(t x_2) ending at q_1=(0,1,0;0;0), and kernel-plane square
   loops attaining pure second-layer points.

## Proof / Evidence

Left-trivialized Pontryagin equations: a Goh lift has h_2 = 0 on V_2 and constant
covector (0,0,xi_3) with xi_3 != 0 (else the lift is trivial). Writing
M(xi_3)(v,Y) = xi_3([v,Y]) as a 3x3 matrix, Jacobi gives [x_1,y_{23}]=f_4-f_6, and
M = 0 forces xi_3 = 0; hence rank M >= 1 for every nonzero xi_3. Controls must lie
in K = ker M(xi_3), and conversely every K-horizontal curve with constant lift
(0,0,xi_3) satisfies adjoint, maximization, Goh, and singularity (via the
annihilator pairing phi(t) = xi_3(eta_3(t)) with dphi/dt = 0 for every control
variation). Rank-1 kernels are 2-planes; every line kernel sits inside a rank-1
2-plane kernel by GL(3)-transitivity, so S equals the union of the 5-dimensional
Carnot subgroups H_K (Lie algebra K (+) Lambda^2 K (+) [K,Lambda^2 K]) over all
2-planes K in Gr(2,3).

On H_K, x in K and y in Lambda^2 K give x wedge y = 0, i.e. Q = 0. For E_1, in the
dense chart K(s,t) = span{x_1+s x_3, x_2+t x_3} one computes
Z_1 = [A_1,Y], Z_2 = [A_2,Y] explicitly and substitutes a general chart point into
E_1, obtaining 0 identically; since vanishing on H_K is Zariski-closed in K, it
extends to all of Gr(2,3), and GL(3)-equivariance extends it to S. Independently
recomputed symbolically on chart, off-chart, and generic planes. The incidence
{(K,p): p in H_K} is a rank-5 bundle over Gr(2,3) = P^2, hence 7-dimensional
irreducible; its polynomial image has closure of dimension exactly 7 because the
chart map R^7 -> R^14 has Jacobian rank 7 at (0,0,0,0,1,0,0) and the counted
directions are attained by genuine Goh curves. V(Q,E_1) is smooth of codimension 2
at (x=0,y=(1,1,0),z_8=1) with dQ = -dx_2+dx_3 and dE_1 = dz_1-dz_2 independent.

## Limitations

Specific to F_{3,3} with the free left-invariant structure; no claim for other
ranks, steps, or non-free quotients. The codimension-7 statement concerns the
Zariski closure of S. Abnormality is proved via the left-trivialized maximum
principle annihilator, not a full coordinate Jacobian of End. Non-Goh abnormal
curves (e.g. the diagonalizable-A examples spanning V_1) are outside S and not
covered by these equations.

## Reproducibility

inputs/artifacts/verify_f33_goh.py (symbolic chart identities, Jacobian rank 7,
smooth-point check, M(f_1^*) rank-1 computation; ALL CHECKS PASSED) and
inputs/artifacts/discover.py (9-dimensional nullspace of vanishing bilinear
(y,z)-forms containing E_1) reproduce the computational steps. All structural
arguments (kernel characterization, wedge vanishing, bundle dimension) are proved
by hand; computation verifies only polynomial identities and ranks.

## References

- L. Rifford, E. Trelat and A. Agrachev circle of Sard-problem literature; in
  particular Le Donne-Montgomery-Ottazzi-Pansu-Vittone, Sard property for the
  endpoint map on some Carnot groups (arXiv:1503.03610), Thm 1.2(2).
- Le Donne-Leonardi-Monti-Vittone, Extremal curves in nilpotent Lie groups
  (arXiv:1207.3985), abnormal/Goh variety classification.
- Tan-Yang, Subriemannian geodesics of Carnot groups of step 3; Boarotto-Vittone
  codimension>=1 sub-analytic bound for rank-3 step-3.
