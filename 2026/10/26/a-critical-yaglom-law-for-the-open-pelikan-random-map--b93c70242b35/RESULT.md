# The total-variation Yaglom limit on the critical line of the open Pelikan map

## Finding

Fix \(0<\varepsilon<1\), put \(a=2-\varepsilon\), and take \(p=4/(4+a^2)\), \(q=1-p\). Start the open Pelikan random map with the uniform distribution on the top dyadic cell \(I_0=[1/2,1)\). Conditional on survival to time \(n\), the cell law converges in total variation to
\[
 u_k=\frac{\varepsilon}{4}\sum_{j=0}^k2^{-j}(a/2)^{k-j},\qquad k\ge0.
\]
The conditioned interval law converges in total variation to the density equal to \(u_k/|I_k|\) on \(I_k=[2^{-k-1},2^{-k})\). The conclusion concerns the distribution at time \(n\), not a time average along surviving trajectories. The critical survival asymptotic is used as an input, and the quasi-stationary law itself is not claimed as new.

## Assumptions and scope

The map choices are independent across time and independent of the initial point. With probability \(q\) apply \(x\mapsto x/2\); with probability \(p\) apply \(x\mapsto 2x\) for \(0\le x<1/2\), send \(x\) to the cemetery for \(1/2\le x<(1+\varepsilon)/2\), and apply \(x\mapsto (2x-1-\varepsilon)/(1-\varepsilon)\) for \((1+\varepsilon)/2\le x<1\). The cemetery is absorbing. Let \(\tau\) be the first killing time. All limits are for each fixed opening parameter; no endpoint-uniformity or claim for arbitrary interval initial laws is made.

## Proof

Let \(m_{n,k}=\Pr(\tau>n, X_n\in I_k)\), \(m_{n,-1}=0\), and \(S_n=\Pr(\tau>n)\). Each branch that survives sends a uniform measure on its source interval to a uniform measure on its image. For the expanding branch on \(I_0\), a fraction \(1-\varepsilon\) survives, with uniform image on \([0,1)\). Induction and linearity thus give uniformity within each occupied cell and the exact recursion
\[
 m_{n+1,k}=p m_{n,k+1}+q m_{n,k-1}+p(1-\varepsilon)2^{-k-1}m_{n,0},\qquad k\ge0.
\]
The mass loss identity is \(S_n-S_{n+1}=p\varepsilon m_{n,0}\). In particular the substochastic chain here has exactly the kernel of the critical survival theorem in [2]. The cell law at time zero is \(\delta_0\), which has every required exponential moment, so that theorem gives \(S_n\sim C\lambda^n/\sqrt n\) with \(C>0\), \(\lambda=ap=2\sqrt{pq}\). Only \(r_n=S_{n+1}/S_n\to\lambda\) is needed below.

Set \(v_{n,k}=m_{n,k}/S_n\). The mass loss identity gives
\[
 v_{n,0}=\frac{1-r_n}{p\varepsilon}\longrightarrow \frac{1-\lambda}{p\varepsilon}=\frac{\varepsilon}{4},
\]
where \(1-\lambda=p\varepsilon^2/4\). For fixed \(k\ge0\), the exact recursion rearranges to
\[
 v_{n,k+1}=\frac{r_n v_{n+1,k}-qv_{n,k-1}}{p}-(1-\varepsilon)2^{-k-1}v_{n,0}.
\]
With \(v_{n,-1}=0\), this proves by induction that all fixed-cell limits \(u_k\) exist. They satisfy \(u_{-1}=0\), \(u_0=\varepsilon/4\) and the same recursion with \(r_n\) replaced by \(\lambda\) and the \(v\)'s replaced by \(u\)'s. Consequently the formal generating series \(U(w)=\sum_{k\ge0}u_kw^k\) satisfies
\[
 (1-aw+a^2w^2/4)U(w)
 =u_0\left(1-\frac{(a-1)w}{2-w}\right)
 =u_0\frac{2-aw}{2-w}.
\]
Thus \(U(w)=\varepsilon/[(2-w)(2-aw)]\), which proves the stated formula by multiplying geometric series. Since \(1<a<2\), the series converges at \(w=1\) and \(U(1)=1\). For any finite set of cells, the sum of absolute mass differences tends to zero; outside the set it is bounded by the sum of the two tail masses. Because the limiting law has total mass one, the finite set can be chosen to make the limiting tail arbitrarily small. This proves total-variation convergence. The conditional and limiting interval laws have the same normalized uniform density within each cell, so their total-variation distance is exactly the cell-law distance.

## Verification

The companion `check.py` and its recorded output provide finite consistency checks of the transition and renewal formulas and numerical corroboration of the limiting weights. The proof above uses the exact transition, the survival ratio from [2], and normalization of the limiting probability law; no finite test substitutes for these steps.

## Relationship to prior work

Brevitt and Klages [1, §2.2] give the open-map chain and identify the critical collision between the return pole and the branch point. Their quasi-stationary formulas [1, §3] already yield the displayed \(u\) on the critical line. The critical survival theorem [2] explicitly specializes to a start in the top cell and gives the sharp amplitude. Knowledge of a quasi-stationary law does not itself show convergence to it from a different initial distribution. The distinct assertion here is critical conditioned-time convergence in total variation from that starting cell, proved by passing the survival ratio through the exact state-by-state balance equations and showing that their limit loses no probability mass.

## References

1. S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084v1, https://arxiv.org/html/2607.19084v1 .
2. *Critical survival amplitudes for the open Pelikan random map*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-critical-survival-amplitudes-for-the-open-pelikan-random-map--e1c961378cda .
