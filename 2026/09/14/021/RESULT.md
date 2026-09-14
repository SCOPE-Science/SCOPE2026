# Universal coupled-SEIR R0 bracketing is false: an exact 2-patch counterexample

## Context

The admitted target asks whether the coupled network reproduction number of an
n-patch SEIR metapopulation is always bracketed by the isolated-patch values,
monotone in a joint movement rate, and convergent to stated small- and
large-coupling limits. Either a Perron-Frobenius proof of the whole package or
an explicit parameter set plus two coupling values with verified spectral radii
violating bracketing or monotonicity counts as a complete target resolution.
This record reports the second alternative: a rigorous disproof of the
universal bracketing claim.

## Definitions

Two patches; infected states ordered (E1,E2,I1,I2). Per-patch parameters:
transmission beta_i, progression sigma_i, recovery gamma_i, background removal
mu_i. Movement generators Q^E,Q^I are Laplacian-type with zero column sums; a
scalar coupling m>=0 scales all off-diagonal exposed and infective movement
rates jointly. New-infection and transition matrices:

F = [[0,D_beta],[0,0]], V(m) = [[V_E(m),0],[-D_sigma,V_I(m)]],

V_E(m) = diag(sigma+mu)+m Q^E, V_I(m) = diag(gamma+mu)+m Q^I.

Each V_E(m),V_I(m) is strictly column diagonally dominant with positive column
sums, hence a nonsingular M-matrix with entrywise-nonnegative inverse. With
H(m) = D_beta V_I(m)^{-1} D_sigma V_E(m)^{-1} >= 0 entrywise,
R0(m) = rho(K(m)) = rho(H(m)), where K(m)=F V(m)^{-1} and rho is spectral
radius. At m=0, H(0)=diag(Riso_1,Riso_2) with
Riso_i = beta_i sigma_i/((sigma_i+mu_i)(gamma_i+mu_i)).

## Result

Universal upper bracketing R0(m) <= max_i Riso_i is false. With

beta=(1,2), sigma=(3,1), mu=(2,2), gamma=(1,1),

E movement 2->1 at rate 3 and I movement 1->2 at rate 3 (opposite directions,
forming a churn cycle), jointly scaled by m, the isolated values are
Riso=(1/5,2/9) with max 2/9 ~= 0.22222, but at m=1

H(1) = [[1/10,1/20],[1/5,19/90]],

rho(H(1)) = (14/45+sqrt(106/2025))/2 ~= 0.26995 > 2/9,

exceeding the isolated maximum by more than 20%. R0 also strictly increases
from m=0 to m=1. Hence the conjunctive universal package (bracketing for every
m plus monotonicity and stated limits) is disproved.

## Proof / evidence

At m=0, V_E(0)=diag(5,3), V_I(0)=diag(3,3), so
H(0)=diag(1*3/(5*3),2*1/(3*3))=diag(1/5,2/9) and R0(0)=2/9.
At m=1: V_E(1)=[[5,-3],[0,6]], V_I(1)=[[6,0],[-3,3]];
V_E(1)^{-1}=[[1/5,1/10],[0,1/6]], V_I(1)^{-1}=[[1/6,0],[1/6,1/3]];
multiplying D_beta V_I^{-1} D_sigma V_E^{-1} gives exactly
H(1)=[[1/10,1/20],[1/5,19/90]]. Trace T=14/45, determinant D=1/90,
discriminant Delta=T^2-4D=106/2025>0, so
rho(H(1))=(T+sqrt(Delta))/2. Since rho(H(1))>2/9 iff sqrt(Delta)>2/15 iff
106/2025>4/225=36/2025 iff 106>36, the violation is an exact integer
inequality. Both Q matrices have zero column sums, so all hypotheses hold.

## Limitations

Disproof of the universal statement only. It does not rule out bracketing
under extra hypotheses (e.g. identical E/I movement patterns, symmetric rates,
or homogeneous progression/recovery). The m->infinity limit is not analyzed
beyond the single violating pair m=0,1.

## Reproducibility

All rational identities are verified by exact Fraction arithmetic in
output/artifacts/verify_counterexample.py, with an independent float
eigendecomposition cross-check (R0(0)=0.22222, R0(1)=0.26995).

## References

- O. Diekmann, J. A. P. Heesterbeek, M. G. Roberts, The construction of
  next-generation matrices for compartmental epidemic models, J. R. Soc.
  Interface 7:873-885 (2010).
- P. van den Driessche, Reproduction numbers of infectious disease models,
  Infect. Dis. Model. 2:288-303 (2017).
- D. Gao, Travel frequency and infectious diseases, SIAM J. Appl. Math.
  79:1581-1606 (2019).
- J. Arino, P. van den Driessche, A multi-city epidemic model, Math. Popul.
  Stud. 10:175-193 (2003).
- L. Meng, W. Zhu, Generalized SEIR epidemic model for COVID-19 in a
  multipatch environment, Discrete Dyn. Nat. Soc. 2021:5401253 (2021).
