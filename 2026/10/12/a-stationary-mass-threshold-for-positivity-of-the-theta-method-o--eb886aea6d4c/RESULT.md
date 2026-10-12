# A stationary-mass threshold for positivity of the theta method on heterogeneous directed cycles

## Finding

For an arbitrary irreducible one-way rate cycle, the ordinary \(\theta\)-method has a **sharp threshold determined solely by the smallest stationary probability** for remaining stochastic at every stepsize. This is substantially different from a uniform positivity restriction based on the fastest transition rate.

Let \(n\ge3\) and \(\lambda_1,\ldots,\lambda_n>0\). In the column-vector convention, consider a clockwise continuous-time Markov generator \(Q\) with
\[
 Q_{jj}=-\lambda_j,\qquad Q_{j+1,j}=\lambda_j
 \quad(j\text{ cyclically modulo }n),
\]
and all other entries zero. In particular \(\mathbf 1^{\mathsf T}Q=0\). Define
\[
 s_j=\lambda_j^{-1},\qquad S=\sum_{j=1}^{n}s_j,\qquad
 \pi_j=\frac{s_j}{S},\qquad
 \theta_c=1-\pi_{\min}=1-\frac{\min_j s_j}{S}.
\]
For \(0\le\theta\le1\) and \(h>0\), write
\[
 T_{\theta,h}=(I-\theta hQ)^{-1}(I+(1-\theta)hQ).
\]
Then the following are necessary and sufficient for \(T_{\theta,h}\) to be entrywise nonnegative (and hence column-stochastic):

1. If \(\theta=0\), precisely \(h\le \lambda_{\max}^{-1}\).
2. If \(0<\theta<\theta_c\), precisely \(0<h\le h_c(\theta)\), where \(h_c(\theta)\) is the **unique** positive solution of
\[
 \frac{1-\dfrac{\theta h\lambda_{\max}}{1+\theta h\lambda_{\max}}}
 {1-\prod_{j=1}^{n}\dfrac{\theta h\lambda_j}{1+\theta h\lambda_j}}
 =1-\theta.
\]
At equality, exactly the diagonal entries belonging to fastest-rate states vanish; the other entries are nonnegative, and every off-diagonal entry is strictly positive.
3. If \(\theta_c\le\theta\le1\), then \(T_{\theta,h}\) is **strictly positive and column-stochastic for every finite \(h>0\)**.

The finite cutoff diverges at the critical parameter. Let \(U=\sum_j s_j^2\), choose any fastest-rate state and write \(s_*=\min_j s_j\). The positive coefficient
\[
 K=\pi_{\min}\left(\frac{S^2+U}{2S}-s_*\right)>0
\]
satisfies
\[
 \lim_{\theta\uparrow\theta_c}(\theta_c-\theta)h_c(\theta)
 =\frac{K}{\theta_c}.
\]
For equal rates \(\lambda_j=\lambda\), the unconditional-positivity boundary is exactly \(\theta_c=1-1/n\) and the coefficient simplifies to
\[
 \lim_{\theta\uparrow\theta_c}(\theta_c-\theta)h_c(\theta)
 =\frac{1}{2\lambda}.
\]
Consequently, the standard Crank–Nicolson choice \(\theta=1/2\) always has a **finite** positivity cutoff for these directed cycles with \(n\ge3\), despite its scalar stability properties.

## Assumptions and scope

States are indexed cyclically. All rates are strictly positive, the number of states is finite and at least three, all matrix inequalities are entrywise, and computations use real exact-arithmetic matrix functions. For every positive stepsize and \(\theta>0\), the matrix \(I-\theta hQ\) is nonsingular. The threshold concerns one complete time step with an arbitrary nonnegative initial probability column vector, not positivity for a selected initial condition. The term stochastic means nonnegative entries with each column summing to one. The stationary vector \(\pi\) above is uniquely determined by \(Q\pi=0\) and \(\sum_j\pi_j=1\).

## Proof

**Resolvent and cyclic factorization.** Put \(a=\theta h>0\), \(q_j=a\lambda_j/(1+a\lambda_j)\), and \(P=\prod_{j=1}^{n}q_j\). Let \(E\) denote the one-position cyclic forward permutation and \(D_q=\operatorname{diag}(q_j)\). Direct multiplication gives
\[
 I-aQ=(I-ED_q)\operatorname{diag}(1+a\lambda_j).
\]
Since \((ED_q)^n=PI\) and \(0<P<1\), its inverse is
\[
 R_a:=(I-aQ)^{-1}
 =\operatorname{diag}\bigl((1+a\lambda_j)^{-1}\bigr)
 \frac{\sum_{k=0}^{n-1}(ED_q)^k}{1-P}.
\]
Every entry of \(R_a\) is strictly positive: for each ordered state pair, exactly one of the \(n\) cyclic shifts carries a strictly positive contribution. The diagonal is
\[
 F_j(a):=(R_a)_{jj}=\frac{1-q_j}{1-P}.
\]
Because \(\mathbf1^{\mathsf T}Q=0\), we also have \(\mathbf1^{\mathsf T}R_a=\mathbf1^{\mathsf T}\). Rewriting the \(\theta\)-step gives the exact identity
\[
 T_{\theta,h}=\frac{R_a-(1-\theta)I}{\theta}.
\]
Thus all off-diagonal entries are strictly positive, column sums are exactly one, and nonnegativity is **equivalent** to \(F_j(a)\ge1-\theta\) for every \(j\).

**Fastest-rate reduction.** The denominator of \(F_j(a)\) does not depend on \(j\). Since \(1-q_j=1/(1+a\lambda_j)\), its minimum occurs exactly at states attaining \(\lambda_{\max}\). It therefore suffices to test the scalar function \(F_*(a)\) for one such state.

**Strict monotonicity and limit.** For every \(j\), differentiation yields
\[
 a\frac{d}{da}\log F_j(a)
 =-q_j+\frac{P}{1-P}\sum_{k=1}^n(1-q_k).
\]
It is strictly negative. Indeed, setting \(B=\prod_{k\ne j}q_k\), the inequality is equivalent to
\[
 B\left(1+\sum_{k\ne j}(1-q_k)\right)<1.
\]
This follows from
\[
 B^{-1}=\prod_{k\ne j}\frac1{q_k}
 >1+\sum_{k\ne j}(1-q_k),
\]
because every factor \(q_k^{-1}=1+(1-q_k)/q_k\) strictly exceeds \(1+(1-q_k)\), and multiplying positive factors expands to at least one plus their individual increments. The set \(k\ne j\) is nonempty. Hence \(F_j\) is strictly decreasing. As \(a\downarrow0\), \(F_j(a)\to1\). As \(a\to\infty\), use \(1-q_j=s_j/a+O(a^{-2})\) and \(1-P=S/a+O(a^{-2})\) to conclude \(F_j(a)\to\pi_j\). The limit is approached strictly from above at every finite \(a\).

**Positivity classification.** For \(0<\theta<1\), compare the horizontal level \(1-\theta\) with \(\pi_{\min}\). If \(1-\theta>\pi_{\min}\), continuity and strict monotonicity yield one and only one intersection, with nonnegativity precisely below it. If \(1-\theta\le\pi_{\min}\), strict approach from above makes every finite step positive. The case \(\theta=1\) follows from \(T_{1,h}=R_h>0\). At \(\theta=0\), the explicit matrix \(I+hQ\) is nonnegative precisely when all diagonal entries \(1-h\lambda_j\) are nonnegative. All endpoint and equality assertions follow, including coincident fastest-rate states.

**Sharp critical scaling.** Set \(U=\sum_j s_j^2\). As \(a\to\infty\),
\[
 1-q_j=\frac{s_j}{a}-\frac{s_j^2}{a^2}+O(a^{-3}),
\qquad
 1-P=\frac{S}{a}-\frac{S^2+U}{2a^2}+O(a^{-3}).
\]
Consequently,
\[
 F_*(a)=\pi_{\min}+\frac{K}{a}+O(a^{-2}),
\qquad
 K=\pi_{\min}\left(\frac{S^2+U}{2S}-s_*\right).
\]
The coefficient is strictly positive: by \(S>s_*\) and the inequalities \(S^2+U>2Ss_*\), or alternatively by expanding \(S^2+U-2Ss_*\) into positive contributions from rates other than the fastest one. Taking \(a=\theta h_c(\theta)\) and using \(F_*(a)=1-\theta=\pi_{\min}+(\theta_c-\theta)\) shows that \(a\to\infty\) and \((\theta_c-\theta)a\to K\). Since \(\theta\to\theta_c>0\), this proves the scaling. When every rate is \(\lambda\), substitution of \(S=n/\lambda\) and \(U=n/\lambda^2\) gives \(K/\theta_c=1/(2\lambda)\).

**Exact three-state example.** For \((\lambda_1,\lambda_2,\lambda_3)=(1,2,6)\) the stationary masses are \((3/5,3/10,1/10)\), so \(\theta_c=9/10\). With \(a=h/2\) at \(\theta=1/2\),
\[
 F_*(a)=\frac{1+3a+2a^2}{1+9a+20a^2}.
\]
The required inequality \(F_*(a)\ge1/2\) is exactly \(1-3a-16a^2\ge0\). Therefore the nonnegative-step interval is
\[
 0<h\le\frac{\sqrt{73}-3}{16}.
\]
This example has no symmetry or equal-rate assumption.

## Verification

The accompanying standalone checker uses rational matrix inversion and multiplication rather than floating-point signs. It reconstructs \(Q\), \(R_a\), and \(T_{\theta,h}\) across dimensions \(2\) through \(6\), including nonuniform rates, checks stochastic column sums, all off-diagonal signs, the precise diagonal-resolvent identity and the sharp finite-horizon test, and verifies strict resolvent monotonicity at rational pairs and the heterogeneous three-state example. A successful execution prints `VERIFY_OK 5346 exact rational transition matrices, 297 strict diagonal-resolvent comparisons, heterogeneous critical example`. This **finite reproducibility check does not replace** the arbitrary-real-parameter monotonicity, sharp cutoff, or asymptotic proofs given above.

## Relationship to prior work

Horváth's 2004-online Runge–Kutta positivity study proves sharp step restrictions on broad positive-IVP classes and analyzes positively invariant regions, without stating the all-rate directed-cycle classification above. Horváth, Song, and Terlaky give a general framework for invariant-set discretizations. Higueras and Roldán analyze sharp positivity restrictions for the \(\theta\)- and Crank–Nicolson schemes on symmetric Dirichlet heat grids. These are related numerical-positivity problems but do not imply the exact heterogeneous, nonreversible cycle formula, the boundary \(1-\pi_{\min}\), or its critical divergence.

Related published work on the \([2/2]\) Padé Markov-positivity barrier concerns a fourth-order two-stage Gauss map, not this one-stage \(\theta\) map. Work on backward-Euler-filtered Crank–Nicolson on periodic heat lattices uses a different, composite stability function and symmetric spatial generator. Earlier two-state rational-map formulas and general \(\theta\)-resolvent diagonal tests provide useful background, but they do not by themselves determine the all-rate cyclic threshold in any number of states. No claim is made that resolvent positivity, the \(\theta\)-scheme, or the small-step sign test is new.

## Limitations

The global stationary-mass criterion uses an **irreducible, one-directional rate cycle**; it is not claimed for arbitrary finite Markov generators or for reversible birth–death chains. It is a one-step exact-arithmetic result, not a claim of second-order accuracy for \(\theta\ne1/2\), stage positivity, embeddability as a continuous-time Markov transition, or error bounds. Very large positive steps can approximate a stochastic projector while poorly resolving transients. Only the leading asymptotic for the finite cutoff near the threshold is proved, not a complete higher-order expansion. A precise historical equivalent in less searchable classical positivity literature remains a residual originality possibility; the supplied source comparisons cannot certify uniqueness in all literature.

## References

1. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* **53** (2005), 341–356, first available online 27 October 2004; DOI: 10.1016/j.apnum.2004.08.026.
2. Z. Horváth, Y. Song, T. Terlaky, “Invariance Preserving Discretization Methods of Dynamical Systems,” arXiv:1607.01106, 2016.
3. I. Higueras, T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066, 2023.
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” 2026; https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
5. “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” 2026; https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac.
