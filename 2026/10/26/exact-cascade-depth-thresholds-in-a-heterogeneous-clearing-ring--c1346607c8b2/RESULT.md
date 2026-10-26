# Exact cascade-depth thresholds in a heterogeneous clearing ring

## Finding

For the Eisenberg–Noe clearing model on a directed \(n\)-bank ring with unit nominal liabilities, edge shares \(0<\lambda_i<1\), and strictly positive baseline slacks \(s_i=x_i+\lambda_{i-1}-1\), a single shock \(\sigma\) to bank \(0\) has exact cascade thresholds \(\tau_0=s_0\) and \(\tau_k=s_0+\sum_{j=1}^{k}\frac{s_j}{\prod_{i=0}^{j-1}\lambda_i}\) for \(1\le k\le n-1\): exactly \(k+1\) consecutive banks default when \(\tau_k<\sigma\le\tau_{k+1}\) for \(0\le k\le n-2\), and all \(n\) default when \(\sigma>\tau_{n-1}\), subject to \(0\le\sigma\le x_0\).

## Assumptions and scope

Let \(n\ge2\), with bank indices taken modulo \(n\). Every bank has nominal liabilities of one unit. Bank \(i\) owes share \(\lambda_i\in(0,1)\) to bank \(i+1\), and the remaining share \(1-\lambda_i\) to creditors outside the ring. Its nonnegative operating resources before the shock are \(x_i\). Define its baseline slack by

\[
s_i=x_i+\lambda_{i-1}-1.
\]

Assume \(s_i>0\) for every bank, so the unshocked clearing vector is full payment at every bank. A shock of size \(\sigma\) subtracts from \(x_0\) only; the admissible range is \(0\le\sigma\le x_0\). A bank defaults exactly when its payment is strictly below one. Thresholds exceeding \(x_0\) are formal boundaries but cannot be reached by this single-bank shock.

## Proof

The clearing equations are

\[
p_i=\min\{1,\ x_i-\sigma\mathbf 1_{i=0}+\lambda_{i-1}p_{i-1}\}.
\]

Set \(d_i=1-p_i\). The deficit equations become

\[
d_0=\max\{0,\sigma-s_0+\lambda_{n-1}d_{n-1}\},\qquad
 d_i=\max\{0,\lambda_{i-1}d_{i-1}-s_i\}\quad(1\le i<n).
\]

The right-hand side is a contraction on \([0,1]^n\) in the sup norm, with Lipschitz constant at most \(\max_i\lambda_i<1\). Hence the clearing vector is unique. Since every \(s_i>0\), a zero deficit at a bank \(i\ge1\) forces the next deficit to be zero. Thus, before the cascade closes around the ring, the default set is a consecutive prefix beginning at bank \(0\).

At the threshold for bank \(k\) to default, \(d_k=0\). Back-substitution through the recurrence gives

\[
d_0=\sum_{j=1}^{k}\frac{s_j}{\prod_{i=0}^{j-1}\lambda_i}.
\]

At this boundary \(d_{n-1}=0\), whether the cascade stops before bank \(n-1\) or bank \(n-1\) itself is at its boundary. The first equation then gives \(d_0=\sigma-s_0\), yielding the stated \(\tau_k\). Moreover,

\[
\tau_k-\tau_{k-1}=\frac{s_k}{\prod_{i=0}^{k-1}\lambda_i}>0,
\]

so the thresholds are strictly increasing. It follows that exactly banks \(0,\ldots,k\) default on \((\tau_k,\tau_{k+1}]\) for \(k<n-1\).

For \(\sigma>\tau_{n-1}\), the all-default linear branch has a unique solution because \(\prod_i\lambda_i<1\). Its deficit derivatives with respect to \(\sigma\) are

\[
\frac{\partial d_0}{\partial\sigma}=\frac{1}{1-\prod_{i=0}^{n-1}\lambda_i},\qquad
\frac{\partial d_i}{\partial\sigma}=\frac{\prod_{j=0}^{i-1}\lambda_j}{1-\prod_{j=0}^{n-1}\lambda_j}\quad(1\le i<n).
\]

All are positive. At \(\tau_{n-1}\), the first \(n-1\) deficits are positive and the last is zero; immediately above it every deficit is positive. This proves the full-cascade assertion. The shock bound \(\sigma\le x_0\) only removes any threshold intervals lying beyond the admissible range.

## Verification

An exact-rational check is included in `verify.py`. For \(n=4\), take \((\lambda_0,\lambda_1,\lambda_2,\lambda_3)=(1/2,2/3,3/4,1/3)\) and \((s_0,s_1,s_2,s_3)=(1/10,1/20,1/20,1/100)\). The thresholds are exactly \((1/10,1/5,7/20,39/100)\), while \(x_0=23/30\). At \(\sigma=9/25\), the clearing payments are \((37/50,23/25,299/300,1)\), so exactly three banks default. At \(\sigma=2/5\), the payments are \((769/1100,1979/2200,811/825,1097/1100)\), so all four default. The script checks the clearing equations with rational arithmetic; it is an example check, not a substitute for the proof above.

## Relationship to prior work

The 2001 Eisenberg–Noe paper defines the general proportional-clearing vector and a sequential-default algorithm. The 2001 paper gives the fixed-point equations and default-wave interpretation, but does not state this explicit threshold sequence for a heterogeneous unilateral ring. A 2022 study of ring interbank networks reports first and extreme final thresholds in a loss-flow/loss-given-default model and states that intermediate ring thresholds are not analytically characterized in that setting. That model is not identical to the proportional-payment model treated here, so the present formula is not asserted to solve its threshold problem. The contribution is the closed-form sequence for a single localized shock in the stated clearing model, not a new general clearing framework.

## Limitations

The result assumes one localized shock, unit nominal liabilities, a unilateral directed ring, positive baseline slacks, and no bankruptcy costs, fire-sale losses, or liquidity feedback. It does not classify multiple simultaneous shocks or bilateral rings. If a threshold exceeds \(x_0\), the corresponding cascade depth is unreachable under the admissible shock range. The exact-rational example verifies the arithmetic only; no empirical calibration or independent audit is claimed.

## References

1. Eisenberg, L., and Noe, T. H. (2001). “Systemic Risk in Financial Systems.” *Management Science* 47(2), 236–249. DOI: 10.1287/mnsc.47.2.236.9835.
2. Eboli, M., Ozel, B., Teglio, A., et al. (2022). “Connectivity, centralisation and ‘robustness-yet-fragility’ of interbank networks.” *Annals of Finance* 19, 169–200. DOI: 10.1007/s10436-022-00416-9.
3. Eboli, M. (2019). “A flow network analysis of direct balance-sheet contagion in financial networks.” *Journal of Economic Dynamics and Control* 103, 205–233. DOI: 10.1016/j.jedc.2019.04.007.
