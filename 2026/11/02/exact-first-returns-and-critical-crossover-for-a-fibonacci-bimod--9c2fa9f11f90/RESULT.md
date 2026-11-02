# Exact first returns and critical crossover for a Fibonacci bimodal Markov map

## Finding
For the induced piecewise-affine map \(T_\lambda\) defined below, choose an initial point uniformly from the natural three-cell return region \(B_\lambda=(\lambda^3,1]\). Let \(\tau=\inf\{n\ge 1:T_\lambda^n(x)\in B_\lambda\}\), with \(\tau=\infty\) when no return occurs. For every \(0<\lambda<1\), the defective probability generating function \(F_\lambda(z)=\mathbb E[z^\tau;\tau<\infty]\), initially for \(0\le z\le1\), is
\[
F_\lambda(z)=z(1-\lambda^3)+\lambda^2(1-\lambda^2)z\,\frac{1-\sqrt{1-4\lambda(1-\lambda)z}}{2-\lambda+\lambda\sqrt{1-4\lambda(1-\lambda)z}}.
\]
The square root is the principal branch with value one at zero. Write \(p_n(\lambda)=\Pr(\tau=n)\). Then \(p_1(\lambda)=1-\lambda^3\), and for every integer \(n\ge2\),
\[
p_n(\lambda)=\frac{\lambda^{n+1}(1-\lambda^2)(1-\lambda)^{n-1}}{n-1}\sum_{j=0}^{n-2}(j+1)\binom{2n-j-4}{n-j-2}\lambda^j.
\]
The no-return probability and finite-return mean satisfy
\[
\Pr(\tau=\infty)=\begin{cases}0,&0<\lambda\le1/2,\\ \lambda^2(2\lambda-1)/(1-\lambda+\lambda^2),&1/2<\lambda<1,\end{cases}
\]
\[
\mathbb E\tau=1+\frac{\lambda^3}{(1+\lambda)(1-2\lambda)}\quad(0<\lambda<1/2),\qquad \mathbb E\tau=\infty\quad(\lambda=1/2).
\]
For each fixed \(0<\lambda<1\), the sharp return coefficient asymptotic is
\[
p_n(\lambda)\sim\frac{\lambda(1+\lambda)}{4\sqrt\pi(2-\lambda)^2}\,[4\lambda(1-\lambda)]^n n^{-3/2}.
\]
In particular, at criticality \(p_n(1/2)\sim n^{-3/2}/(12\sqrt\pi)\) and \(\Pr_{1/2}(\tau>n)\sim n^{-1/2}/(6\sqrt\pi)\). The crossover is uniform on the Gaussian parameter scale: for every fixed real \(u\), setting \(\lambda_n=1/2+u/\sqrt n\) gives
\[
\lim_{n\to\infty}n^{3/2}p_n(\lambda_n)=\frac{e^{-4u^2}}{12\sqrt\pi}.
\]
These formulas also hold for the initial distribution obtained by conditioning the finite absolutely continuous invariant probability on \(B_\lambda\), whenever \(0<\lambda<1/2\).

## Assumptions and scope
The interval partition is \(V_i=(\lambda^i,\lambda^{i-1}]\) for integers \(i\ge1\), modulo irrelevant endpoint conventions. On these pieces define
\[
T_\lambda(x)=\begin{cases}
(x-\lambda)/(1-\lambda),&x\in V_1,\\
(x-\lambda^2)/(\lambda(1-\lambda)),&x\in V_2,\\
(x-\lambda^3)/(\lambda^2(1-\lambda)),&x\in V_3,\\
(x-\lambda^4)/(\lambda^2(1-\lambda)),&x\in V_4,\\
(x-\lambda^i)/(\lambda(1-\lambda)),&x\in V_i,\ i\ge5.
\end{cases}
\]
This is the positive-half induced Markov map of Ji and Ma's Fibonacci bimodal construction [1]. Their primary dynamical phase transition is not claimed anew here. Uniform initial measure on \(B_\lambda=V_1\cup V_2\cup V_3\) is normalized ordinary Lebesgue measure. All probabilities and expectation formulas are for that initial distribution; when \(\lambda>1/2\), the unconditioned return-time law is defective.

## Proof
**Exact Markov coding.** Each affine restriction maps its source cell bijectively onto a union of partition cells. The image is \((0,1]\) for \(i\le3\), \((0,\lambda]\) for \(i=4\), and \((0,\lambda^{i-2}]\) for \(i\ge5\). Consequently, normalized Lebesgue measure on a source cell gives a uniform image, and the cell-index process has transition probabilities
\[
P_{ij}=\begin{cases}
(1-\lambda)\lambda^{j-1},&i\le3,\ j\ge1,\\
(1-\lambda)\lambda^{j-2},&i=4,\ j\ge2,\\
(1-\lambda)\lambda^{j-i+1},&i\ge5,\ j\ge i-1,\\
0,&\text{otherwise}.
\end{cases}
\]
The uniformity of conditional future branches follows inductively from linearity of all restrictions. Since rows \(i=1,2,3\) coincide, the return law does not depend on which of these cells initially contains the point or on a mixture of their normalized cell-Lebesgue laws.

**Bulk descent and the exceptional fourth cell.** For \(i\ge5\), every step subtracts one from the index and adds a nonnegative geometric random variable with probability \((1-\lambda)\lambda^k\). Let \(r=r_\lambda(z)\) be the hitting-time PGF of one unit of downcrossing for this skip-free homogeneous walk. The strong Markov property gives
\[
r=\frac{z(1-\lambda)}{1-\lambda r},\qquad
r=\frac{1-\sqrt{1-4\lambda(1-\lambda)z}}{2\lambda}.
\]
The minimal nonnegative solution is selected by \(r(0)=0\). If \(h_i\) is the PGF for the time from cell \(i\ge4\) until reaching \(B_\lambda\), the strong Markov property gives \(h_i=r^{i-4}h_4\) for \(i\ge4\). Cell four jumps to cell two or three with total probability \(1-\lambda^2\), otherwise to \(j\ge4\), giving
\[
h_4=z(1-\lambda^2)+z\sum_{j\ge4}(1-\lambda)\lambda^{j-2}h_j
=\frac{z(1-\lambda^2)}{1-\lambda^2r}.
\]
Starting from any of cells one through three, the first jump returns immediately with probability \(1-\lambda^3\). Summing first jumps into cells \(j\ge4\), whose total weighted hitting PGF is \(\lambda^3rh_4/z\), gives
\[
F_\lambda=z(1-\lambda^3)+\lambda^3rh_4
=z(1-\lambda^3)+\frac{\lambda^3(1-\lambda^2)zr}{1-\lambda^2r}.
\]
Substituting the quadratic solution proves the displayed generating function.

**Coefficient extraction and recurrence.** Since \(r=z(1-\lambda)/(1-\lambda r)\), Lagrange inversion applied to \(r/(1-\lambda^2r)\) gives
\[
[z^{n-1}]\frac{r}{1-\lambda^2r}=
\frac{(1-\lambda)^{n-1}}{n-1}[w^{n-2}]\frac1{(1-\lambda^2w)^2(1-\lambda w)^{n-1}}.
\]
Multiplication of the two binomial series yields the finite coefficient sum. At \(z=1\), the minimal solution of the quadratic is \(r(1)=1\) if \(\lambda\le1/2\) and \(r(1)=(1-\lambda)/\lambda\) if \(\lambda>1/2\). Direct substitution yields the escape formula. For \(\lambda<1/2\), differentiation at \(z=1\) gives \(r'(1)=(1-\lambda)/(1-2\lambda)\) and the stated mean. At \(\lambda=1/2\) the positive return distribution has infinite mean because its coefficient tail has exponent \(3/2\), proved next.

**Sharp singularity and crossover.** Set \(R=4\lambda(1-\lambda)\) and \(s=\sqrt{1-Rz}\). The nontrivial term of the PGF equals \(\lambda^2(1-\lambda^2)z(1-s)/(2-\lambda+\lambda s)\). Its nonanalytic term near \(z=R^{-1}\) is \(-\lambda(1+\lambda)s/[2(2-\lambda)^2]\). The possible denominator pole does not occur in the analytic slit disc: for \(|z|\le R^{-1}\), the power series for \(r\) has nonnegative coefficients and \(|\lambda^2r(z)|\le\lambda^2r(R^{-1})=\lambda/2<1\). Standard square-root coefficient transfer gives the precise coefficient constant displayed above, with relative error \(O(n^{-1})\) for fixed \(\lambda\). On any compact parameter subinterval of \((0,1)\), the singularity expansion and analytic remainder bounds are uniform because \(2-\lambda>1\) and \(\lambda/2<1\). For \(\lambda_n=1/2+u/\sqrt n\), one has \(R(\lambda_n)^n=(1-4u^2/n)^n\to e^{-4u^2}\) and continuity of the prefactor proves the claimed Gaussian crossover. Finally, summing the positive, recurrent critical tail gives \(\Pr(\tau>n)\sim 2\,n^{-1/2}/(12\sqrt\pi)\).

**Finite invariant initial distribution.** When \(0<\lambda<1/2\), Ji and Ma [1] construct a stationary density constant on each \(V_i\). Conditioning on \(B_\lambda\) gives a mixture of uniform distributions over \(V_1,V_2,V_3\). Their three rows of \(P\) are identical, so the full first-return law agrees with that under normalized Lebesgue measure on \(B_\lambda\).

## Verification
The accompanying standalone Python script `checker.py` uses exact rational arithmetic. It independently computes the coefficient law by finite-horizon Markov propagation (120 parameter/horizon identities for five rational parameters) and compares 2,380 exact conditional transition probabilities derived from affine image lengths. It also tests the finite invariant Kac relation and numerically reports, without treating as proof, sample large-horizon asymptotic ratios. Run `python checker.py` with Python 3; no third-party packages are required. All asymptotic, escape, and completeness assertions above are proved by the analytic argument, not by numerical tests.

## Relationship to prior work
Ji and Ma [1] introduce the induced Fibonacci bimodal Markov map, derive its transition mechanism and invariant densities, and prove the conservative/dissipative transition at \(\lambda=1/2\). We credit those foundational results and claim neither that map nor the recurrence threshold as new. The present statement instead gives the explicit all-time return generating function for the natural three-cell base, every finite return coefficient, the exact escape weight and sharp critical/Gaussian crossover constants. The bulk quadratic law is a classical skip-free/Galton–Watson mechanism; for context see [2]. The exceptional fourth-cell boundary correction in the rational expression and its dynamical return interpretation are model-specific. Direct general skip-free results can supply substantial components, so the claim should not be construed as a new random-walk universality principle.

## Limitations
The result concerns the induced map \(T_\lambda\), rather than first returns of the original unimodal/bimodal physical-time system. For \(\lambda>1/2\), the law is defective and the mean formula for recurrent regimes is not asserted. Endpoint choices form Lebesgue-null sets. The result does not classify correlations or the full invariant measure beyond what was previously established. Independently verifying publication priority against all specialised random-walk or inducing literature remains desirable; independent scientific audit is not yet performed.

## References
[1] Haoyang Ji and Wenxiu Ma, *Phase transition for piecewise linear fibonacci bimodal map*, AIMS Mathematics 8 (2023), 8403–8430, https://doi.org/10.3934/math.2023424 (first publicly listed 2023-02-03). Particularly Section 5, the induced Markov map and recurrence classification.

[2] Timo Vilkas, *Left-continuous random walk on Z and the parity of its hitting times*, arXiv:2407.06903v1 (2024), https://arxiv.org/abs/2407.06903. General skip-free walk/branching correspondence; it does not specify the three-cell return distribution for the Ji–Ma map.
