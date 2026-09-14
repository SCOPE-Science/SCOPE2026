# Extremal-process convergence for Weibull branching random walks in an i.i.d. branching environment

## Context

Branching random walk (BRW) extremes fall into universality classes set by the displacement tail.
Light-tailed steps give linear speed with logarithmic correction and a randomly-shifted decorated
Poisson limit; regularly-varying steps obey the one-big-jump principle with a Frechet Cox-cluster
limit. The intermediate stretched-exponential (Weibull) class was resolved in the homogeneous case
by Dyszewski-Gantert (maxima, large deviations, then full extremal point process with a phase
transition at r=2/3). The parallel question for BRW indexed by a supercritical branching process
in an i.i.d. random environment (BPRE) was known only for regularly-varying steps
(Bhattacharya-Palmowski: Frechet limit, scale-decorated limit, time-reversed environment clusters),
whose authors state the light-tailed analog is open. The target here is the Weibull-BPRE case.

## Definitions

Environment Y=(Y_j) i.i.d.; particle in generation j has offspring N with law F_j given Y_j.
m_j=E[N|Y_j], L_n(Y)=sum_{j<n} log m_j, Z_n population, W_n=Z_n exp(-L_n(Y)) -> W.
Assume (E1) E|log m_0|<infty, mu=E log m_0 in (0,infty), P(survival)>0; (E2) Smith-Wilkinson-Tanny
Kesten-Stigum moment E[Z_1 log^+ Z_1/m_0]<infty so W_n->W a.s. and L^1 with {W=0}={extinction}
a.s.; (E3) upsilon(Y^<-)=sum_j exp(-L^<-_j)P(Z^<-_j>0|Y^<-)<infty a.s. Displacements {X_w} i.i.d.
centred, EX=0, EX^2=1, P(X>x)=a(x)exp(-R(x)), R=x^r ell(x), 0<r<1, R' regularly varying of index
r-1 with Dyszewski-Gantert smoothness/moments. V(w)=sum of X along lineage; V_n=sum_{|w|=n}
delta_{V(w)}; M_n=max V(w); T_b shift; S_c scale. d_n(Y) solves R(d_n(Y))=L_n(Y);
a_n(Y)=1/R'(d_n(Y)); Psi_n(z;Y)=inf_{s in [0,1]}{R(d_n+z-nK'(s))+n(sK'(s)-K(s))} with truncated
cumulant K; tau_n(Y) solves Psi_n(tau_n;Y)=L_n(Y), tau_n=nR'(d_n)/2+O(n^{3-2/r});
b_n(Y)=d_n(Y)+tau_n(Y). Y^<- independent copy (time-reversed); upsilon as above; T|Y^<- with
P(T=k|Y^<-)=upsilon^{-1} sum_j exp(-L^<-_j)P(Z^<-_j=k|Y^<-); {iota_k} PPP(a e^{-x}dx).

## Result

Under (E1)-(E3) and (D), annealed and conditional on survival S={W>0},
S_{a_n(Y)^{-1}} T_{-b_n(Y)} V_n => Lambda in M_p (vague), where
Lambda=1_{W>0} sum_k T_k delta_{iota_k-log(upsilon(Y^<-)W)},
with annealed Laplace functional
E exp(-<f,Lambda>)=E[exp{-aW sum_j E^<-[exp(-L^<-_j) int E_{Y^<-}[1-exp(-Z^<-_j f(x))] e^{-x}dx]}].
Hence (M_n-b_n(Y))/a_n(Y) ->d V with P(V<=x|S)=E[exp(-a upsilon(Y^<-)W e^{-x})|W>0],
a Y^<--mixture of Gumbels; k-th order statistics follow as in DG Cor. 3.2.
The full r in (0,1) range is covered including the r=2/3 transition:
tau_n(Y)=o(a_n) for r<2/3, comparable at r=2/3, dominant for r>2/3.
Deterministic centring is impossible: (d_n(Y)-dbar_n)/abar_n has sd sigma sqrt(n)->infty.

## Proof / evidence

Homogeneous precise stretched-exponential large deviations are imported verbatim
(displacement-only); only first-moment bookkeeping changes m^n -> exp(L_n(Y)).
Quenched trimming kills classes A (no big jump), B (>=2 big jumps, needs 2 eps^r>1),
C (intermediate jump) a.s. since L_n(Y)/n->mu; only single big jump D survives.
Deterministic decoupling scales k_n,l_n work a.s.; shared-ancestry events vanish.
For fixed lag j, exp(L_{n-j}(Y)) eta_n^{(j)} ->v a e^{-x}dx, and
Z_{n-j}E_Y[1-exp(-Theta)] -> W exp(-(L_n-L_{n-j})) int E[1-exp(-Z_j f)] eta;
(L_n-L_{n-j}, descendant law) =d (L^<-_j, Z^<-_j) independent of the early bulk by
i.i.d. stationarity, with L^1 convergence of W_{n-j}->W from (E2) and a.s. summable
exp(-L^<-_j) tails giving (9)/(17); upsilon factors cancel to yield (8).
Void probabilities give the maximum; reversal reflects that L_n-L_{n-j} uses the last
j environments. Computation `check_centering.py` (support only) confirms
sd((d_n-dbar)/abar)=1.62,3.68,8.08,17.82 at n=40,200,1000,5000 vs sigma sqrt(n), and
single-jump mechanism at small n.

## Limitations

Annealed convergence conditional on survival; quenched a.s. convergence to a fixed limit
is false (recent environment fluctuates) — only convergence in P_Y-probability to the
Y^<--averaged law. Imports DG precise-LD/cumulant analysis as black box. No local/genealogy
refinements, boundary r->0,1, relaxation of (E2), or convergence rates.

## Reproducibility

Model/assumptions/scales as above; proof follows DG Sections 4-6 with stated substitutions;
artifact `check_centering.py` runs with python3+numpy only.

## References

Dyszewski-Gantert arXiv:2212.06639 (extremal process, stretched exponential, homogeneous);
Dyszewski-Gantert-Hofelsauer AIHP 2023 / ECP 2020 (maximum, large deviations);
Bhattacharya-Palmowski arXiv:2101.05369 / Extremes 2025 (regularly-varying BRW in BPRE);
Gantert 2000 Ann. Probab. (semiexponential maximum).
