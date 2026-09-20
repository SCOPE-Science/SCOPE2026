# Exact delay-distribution law for two-coordinate randomized Gauss-Seidel

## Statement

Let
\[
A=\begin{pmatrix}a&c\\ c&d\end{pmatrix}\succ0,\qquad Ax^\star=b,
\]
and write the error in diagonally scaled coordinates
\[
y_1^k=\sqrt a\,(x_1^k-x_1^\star),\qquad
y_2^k=\sqrt d\,(x_2^k-x_2^\star),\qquad
r=\frac{|c|}{\sqrt{ad}}\in[0,1).
\]
At each update choose \(I_k\in\{1,2\}\) uniformly and independently. Let the
delay \(D_k\) be i.i.d., independent of the coordinate choices and past
iterates, with finite support \(\{0,\ldots,\tau\}\) and probabilities
\(\pi_j=\Pr(D_k=j)\). The selected coordinate is overwritten by its exact
Gauss-Seidel component equation using the stale value of the other coordinate:
\[
\begin{array}{ll}
I_k=1:&y_1^{k+1}=-\rho\,y_2^{k-D_k},\quad y_2^{k+1}=y_2^k,\\[2mm]
I_k=2:&y_2^{k+1}=-\rho\,y_1^{k-D_k},\quad y_1^{k+1}=y_1^k,
\end{array}
\]
where \(\rho=c/\sqrt{ad}\), so \(\rho^2=r^2\). A fixed finite initial history
is used for negative indices.

Define the diagonally scaled mean-square error
\[
S_k=\mathbb E\!\left[(y_1^k)^2+(y_2^k)^2\right]
=\mathbb E\!\left[a(x_1^k-x_1^\star)^2+d(x_2^k-x_2^\star)^2\right].
\]

Then the second moment closes exactly to the scalar recurrence
\[
\boxed{\quad
S_{k+1}=\frac12S_k+\frac{r^2}{2}\sum_{j=0}^{\tau}\pi_jS_{k-j}.
\quad} \tag{1}
\]

For \(0<r<1\), its asymptotic factor is the unique \(q\in(1/2,1)\) satisfying
\[
\boxed{\quad 2q-1=r^2\,\mathbb E[q^{-D}]
=r^2\sum_{j=0}^{\tau}\pi_jq^{-j}. \quad} \tag{2}
\]
Equivalently, if \(\tau\) is the largest delay with positive probability,
\(q\) is the Perron root of
\[
2q^{\tau+1}-q^\tau-r^2\sum_{j=0}^{\tau}\pi_jq^{\tau-j}=0. \tag{3}
\]
Thus \(S_k^{1/k}\to q\), and for every nonzero positive initial history
\(S_{k+1}/S_k\to q\). For \(r=0\), \(S_{k+1}=S_k/2\).

The exact law yields the following consequences.

1. **Stochastic ordering of delays.** If \(D'\) first-order stochastically
   dominates \(D\), then \(q(D')\ge q(D)\). If \(D'\) dominates \(D\) in
   convex order, the same conclusion holds. Hence, at fixed mean delay,
   greater delay variability worsens the exact asymptotic factor.

2. **Extremal bounded delay laws at fixed mean.** Among integer-valued laws
   supported on \(\{0,\ldots,\tau\}\) with mean \(\mu\), the largest factor is
   attained by the endpoint law
   \[
   \Pr(D=\tau)=\mu/\tau,\qquad \Pr(D=0)=1-\mu/\tau.
   \]
   The smallest factor is attained by the distribution supported on
   \(\lfloor\mu\rfloor,\lceil\mu\rceil\) with the prescribed mean
   (deterministic when \(\mu\) is an integer).

3. **Deterministic delay.** For \(D\equiv\tau\),
   \[
   q^\tau(2q-1)=r^2.
   \]
   The factor is strictly increasing with \(\tau\) when \(0<r<1\), and
   \[
   \tau(1-q)\longrightarrow-\log(r^2)\qquad(\tau\to\infty).
   \]

4. **Near-singular normalized system.** Put
   \(\delta=1-r^2\), \(\mu=\mathbb E D\), and
   \(m_2^+=\mathbb E[D(D+1)]\). For fixed finite delay law,
   \[
   q=1-\frac{\delta}{\mu+2}
   +\left[
       \frac{m_2^+}{2(\mu+2)^3}
       -\frac{\mu}{(\mu+2)^2}
     \right]\delta^2
   +O(\delta^3). \tag{4}
   \]
   Thus the mean delay controls the first-order slowdown, while at fixed mean
   the delay variance first appears at second order. For the diagonally
   normalized matrix
   \(\begin{psmallmatrix}1&\rho\\ \rho&1\end{psmallmatrix}\),
   whose spectral condition number is
   \(\kappa=(1+r)/(1-r)\),
   \[
   1-q\sim\frac{4}{(\mu+2)\kappa}\qquad(\kappa\to\infty).
   \]
   Relative to zero staleness, the leading iteration-count penalty is
   \(1+\mu/2\).

The exact quantity in (1)--(4) is the diagonal-scaled mean-square error, not
the \(A\)-energy itself. Since all norms are equivalent in this fixed
two-dimensional SPD setting, the factor still gives a concrete convergence
benchmark, but no exact \(A\)-energy recurrence is claimed.

## Proof

Condition on the complete history before update \(k\) and on \(D_k=j\).
If coordinate 1 is selected, the next squared scaled norm is
\[
r^2(y_2^{k-j})^2+(y_2^k)^2.
\]
If coordinate 2 is selected, it is
\[
r^2(y_1^{k-j})^2+(y_1^k)^2.
\]
Averaging the two equiprobable choices gives
\[
\frac12\bigl((y_1^k)^2+(y_2^k)^2\bigr)
+\frac{r^2}{2}\bigl((y_1^{k-j})^2+(y_2^{k-j})^2\bigr).
\]
Averaging over the independent delay and then over the past proves (1).

For \(0<r<1\), define
\[
F_D(q)=2q-1-r^2\mathbb E[q^{-D}].
\]
On \(q>0\),
\[
F_D'(q)=2+r^2\mathbb E[Dq^{-D-1}]>0.
\]
Moreover \(F_D(1/2)<0\) and \(F_D(1)=1-r^2>0\), so (2) has exactly one root
in \((1/2,1)\). The companion matrix of (1) is nonnegative and, after removing
unused trailing delays, primitive because the coefficient of \(S_k\) is
positive and the maximal-delay coefficient is positive. Perron-Frobenius
therefore identifies the unique positive root with the spectral radius and
gives the asserted asymptotics.

For \(q\in(0,1)\), the function \(j\mapsto q^{-j}\) is increasing and strictly
convex. First-order stochastic dominance or convex dominance therefore
increases \(\mathbb E[q^{-D}]\) pointwise in \(q\). Since every \(F_D\) is
strictly increasing, its zero moves to the right. The extremal fixed-mean
claims follow from the standard chord bound for a convex function on
\([0,\tau]\) and, for integer support, from concentration on the two adjacent
integers around the mean.

For \(D\equiv\tau\), (2) becomes \(q^\tau(2q-1)=r^2\). Increasing \(\tau\)
reduces the left side at fixed \(q<1\), so the root increases. As
\(\tau\to\infty\), the root tends to 1; taking logarithms gives
\[
\tau\log q+\log(2q-1)=\log r^2,
\]
hence \(\tau(1-q)\to-\log r^2\).

Finally, set \(q=1-a\delta+b\delta^2+O(\delta^3)\) in (2), with
\(r^2=1-\delta\). Expanding
\[
\mathbb E[q^{-D}]
=1+\mu a\delta+
\left[-\mu b+\frac{a^2}{2}\mathbb E[D(D+1)]\right]\delta^2
+O(\delta^3)
\]
and matching coefficients gives
\[
a=\frac1{\mu+2},\qquad
b=\frac{m_2^+}{2(\mu+2)^3}-\frac{\mu}{(\mu+2)^2},
\]
which proves (4) and the condition-number form.

## Numerical check

For \(r=0.8\), equation (2) gives

| delay law | mean delay | exact factor \(q\) |
|---|---:|---:|
| \(D=0\) | 0 | 0.820000000000 |
| \(D=1\) | 1 | 0.868465843843 |
| \(\Pr(D=0)=\Pr(D=2)=1/2\) | 1 | 0.870934950214 |
| \(D=2\) | 2 | 0.897375730150 |

The equal-mean comparison illustrates the convex-order statement. The compact
verification script in `artifacts/verify_delay_rate.py` solves (2) by bisection
and independently iterates (1).

## Relation to prior literature

Chazan and Miranker introduced chaotic relaxation and convergence conditions
for asynchronous linear iterations. Beidas and Papavassilopoulos developed a
general stochastic-delay model and gave second-moment and mean convergence
conditions. Moga and Dubois then used state augmentation to study convergence
rates for two-variable asynchronous linear iterations with stochastic delays;
their analytical model follows the expected trajectory and, in its displayed
two-variable specialization, treats zero/one communication delays. Verkama
studied random coordinate relaxation of fixed-point iterations. Avron,
Druinsky and Gupta established linear convergence-rate guarantees for
randomized asynchronous SPD linear solvers. Peng, Xu, Yan and Yin developed
delay-statistics-dependent asynchronous coordinate-update guarantees,
including unbounded-delay models.

Those works supply the surrounding general theory. The contribution here is
the exact scalar **second-moment** closure for the two-coordinate randomized
Gauss-Seidel benchmark with an arbitrary bounded i.i.d. delay law, together
with the resulting distribution-ordering theorem, fixed-mean extremizers,
large-delay asymptotic and near-singular expansion. Searches did not locate
these formulas or consequences stated in that form.

A directly relevant recent preprint by Carson and Ma studies asynchronous
Jacobi and randomized Gauss-Seidel for SPD systems and gives general linear
convergence bounds depending on maximum communication delay and communication
structure. Its abstract was inspected, but its full text was not inspected;
consequently, possible overlap beyond the abstract remains a material
originality uncertainty.

## References

- D. Chazan and W. L. Miranker, *Chaotic relaxation*, Linear Algebra and its
  Applications 2 (1969), 199--222.
  https://research.ibm.com/publications/chaotic-relaxation
- B. F. Beidas and G. P. Papavassilopoulos, *Convergence analysis of
  asynchronous linear iterations with stochastic delays*, Parallel Computing
  19 (1993), 281--302.
  https://doi.org/10.1016/0167-8191(93)90038-M
- A. C. Moga and M. Dubois, *Performance of Asynchronous Linear Iterations with
  Random Delays*, USC CENG Technical Report 95-06 (1995).
  https://ceng.usc.edu/techreports/1995/Dubois%20CENG%2095-06.pdf
- M. Verkama, *Random Relaxation of Fixed-Point Iteration*, SIAM Journal on
  Scientific Computing 17 (1996), 906--912.
  https://doi.org/10.1137/0917058
- H. Avron, A. Druinsky and A. Gupta, *Revisiting Asynchronous Linear Solvers:
  Provable Convergence Rate through Randomization*, Journal of the ACM 62
  (2015), Article 51.
  https://doi.org/10.1145/2814566
- Z. Peng, Y. Xu, M. Yan and W. Yin, *On the Convergence of Asynchronous
  Parallel Iteration with Unbounded Delays*, Journal of the Operations
  Research Society of China 7 (2019), 5--42.
  https://doi.org/10.1007/s40305-017-0183-1
- E. Carson and Y. Ma, *Asynchronous Jacobi and randomized Gauss--Seidel
  methods in shared and distributed memory: A unified convergence-rate
  analysis*, arXiv:2609.15605 (2026).
  https://arxiv.org/abs/2609.15605

## Limitations

The theorem is deliberately a two-coordinate benchmark with uniform coordinate
selection, exact component overwrites, and i.i.d. bounded delays independent
of the iterate history. It does not cover correlated delays, inconsistent
multi-coordinate reads, unequal coordinate probabilities, relaxation
parameters, or dimensions above two. The exact recurrence is for a
diagonal-scaled mean-square norm. The full text of Beidas--Papavassilopoulos
(1993) was not inspected in this review, so a specialized corollary hidden
there remains an originality risk. The full text of the directly relevant
Carson--Ma preprint arXiv:2609.15605 was also not inspected; only its abstract
was checked, leaving a contemporaneous-overlap risk.

Same-model review: passed. Independent audit: not yet performed.
