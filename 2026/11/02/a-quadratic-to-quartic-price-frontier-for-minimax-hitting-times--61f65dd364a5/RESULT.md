# A quadratic-to-quartic price frontier for minimax hitting times on reversible paths

## Finding

Consider a continuous-time reversible nearest-neighbor Markov chain on the path with vertices \(1,\ldots,n\), where \(n\ge3\). Its stationary probabilities \(\pi_1,\ldots,\pi_n\) are prescribed and strictly positive, with sum one. Independently choose positive edge conductances \(c_1,\ldots,c_{n-1}\); transition rates across edge \(i\leftrightarrow i+1\) are \(c_i/\pi_i\) and \(c_i/\pi_{i+1}\). Edge \(i\) costs \(p_i c_i\), where \(p_i>0\), and the budget is \(B>0\).

Let \(H_{uv}\) denote the expected first time the chain started at \(u\) reaches \(v\), with \(u\ne v\). Put
\[
M_i=\sum_{j=1}^{i}\pi_j,\qquad
 a_i(\lambda)=1-M_i+\lambda(2M_i-1),\qquad
 S(\lambda)=\sum_{i=1}^{n-1}\sqrt{p_i a_i(\lambda)}.
\]
The unique maximizer \(\lambda_*\in[0,1]\) of \(S\) determines the **unique** positive budget-optimal allocation for the worst directional mean hitting time:
\[
\boxed{c_i^*=\frac{B}{S(\lambda_*)}\sqrt{\frac{a_i(\lambda_*)}{p_i}},\qquad
\min_{\substack{c_i>0\\\sum_i p_ic_i\le B}}\max_{u\ne v}H_{uv}=\frac{S(\lambda_*)^2}{B}.}
\]
This is a one-dimensional strictly concave maximization, not merely a necessary optimality condition. The endpoint-versus-balanced cases are explicit: \(\lambda_*=0\) if \(S'(0)\le0\), \(\lambda_*=1\) if \(S'(1)\ge0\), and otherwise it is the unique interior zero of \(S'\). In the interior the two endpoint hitting times are equal. At an endpoint the corresponding travel direction is a worst case.

For the natural **one-price-defect family**, take \(\pi_j=1/n\) and let \(p_i=1\) except for \(p_k=Q\ge1\), with \(n/2<k\le n-1\). Define
\[
A_n=\sum_{i=1}^{n-1}\frac{2i-n}{\sqrt i}<0,\qquad
Q_c(n,k)=\left(1-\frac{A_n\sqrt{k}}{2k-n}\right)^2>1.
\]
For \(1<Q<Q_c(n,k)\) the unique optimal allocation exactly balances \(H_{1n}=H_{n1}\), with \(1/2<\lambda_*<1\). At \(Q=Q_c(n,k)\), \(\lambda_*=1\) and the two endpoint times remain equal. For \(Q>Q_c(n,k)\), \(\lambda_*=1\) and \(H_{1n}>H_{n1}\): the optimum is genuinely controlled by only one direction. At \(Q=1\), \(\lambda_*=1/2\).

The exact frontier has **two asymptotic scales**:
\[
\boxed{\frac{Q_c(n,k_n)}{n^2}\longrightarrow
\frac{4\theta}{9(2\theta-1)^2}}
\quad\text{if}\quad \frac{k_n}{n}\longrightarrow\theta\in(1/2,1],
\]
and, for each fixed integer \(s\ge1\) along even \(n\),
\[
\boxed{\frac{Q_c(n,n/2+s)}{n^4}\longrightarrow\frac1{18s^2}.}
\]
Thus a defect a fixed proportion beyond the midpoint has a quadratic transition price, whereas a defect only finitely many edges beyond the midpoint needs a quartic transition price.

## Assumptions and scope

All \(n\) stationary masses are fixed independently of the conductance decision and satisfy \(\pi_i>0\), \(\sum_i\pi_i=1\). Conductances must be strictly positive to retain irreducibility. Only jumps between neighbors are allowed, and the generator has no other nonzero off-diagonal entries. The budget constraint is \(\sum_i p_i c_i\le B\), with all prices and \(B\) positive; the objective concerns **expected first-hitting times in continuous physical time**, not step counts. The one-price phase theorem assumes a surcharge \(Q\ge1\) and \(k>n/2\); reflection covers \(k<n/2\), while an exact midpoint has no directional asymmetry.

## Proof

**Step 1: exact hitting-time representation.** For the mean time to reach \(n\), write \(h_j=H_{jn}\), with \(h_n=0\), and let \(\delta_j=h_j-h_{j+1}\). The backward generator equation at \(j<n\) is
\[
-c_j\delta_j+c_{j-1}\delta_{j-1}=-\pi_j,
\]
where the second term is absent at \(j=1\). Induction gives \(c_j\delta_j=M_j\), hence
\[
H_{1n}=\sum_{i=1}^{n-1}\frac{M_i}{c_i}.
\]
The reflected recursion gives
\[
H_{n1}=\sum_{i=1}^{n-1}\frac{1-M_i}{c_i}.
\]
The strong Markov property expresses every one-way hitting time between two other vertices as a sum over a proper subinterval of the corresponding positive edge contributions. Therefore, exactly,
\[
\max_{u\ne v}H_{uv}=\max\{H_{1n},H_{n1}\}.
\]
No symmetry of the optimized conductances has been imposed.

**Step 2: a sharp lower bound.** For every \(\lambda\in[0,1]\),
\[
\max\{H_{1n},H_{n1}\}\ge
\lambda H_{1n}+(1-\lambda)H_{n1}
=\sum_{i=1}^{n-1}\frac{a_i(\lambda)}{c_i}.
\]
Weighted Cauchy–Schwarz and the budget yield
\[
\left(\sum_i\sqrt{p_i a_i(\lambda)}\right)^2
\le\left(\sum_i p_i c_i\right)
\left(\sum_i\frac{a_i(\lambda)}{c_i}\right)
\le B\max\{H_{1n},H_{n1}\}.
\]
Equality in the first inequality requires \(c_i\) proportional to \(\sqrt{a_i(\lambda)/p_i}\), and equality in the budget requires full expenditure.

**Step 3: attainability and uniqueness.** Every \(M_i\in(0,1)\), so all \(a_i(\lambda)>0\) on the closed unit interval. Direct differentiation gives
\[
S'(\lambda)=\frac12\sum_i\frac{\sqrt{p_i}(2M_i-1)}{\sqrt{a_i(\lambda)}},\qquad
S''(\lambda)=-\frac14\sum_i\frac{\sqrt{p_i}(2M_i-1)^2}{a_i(\lambda)^{3/2}}<0.
\]
The last inequality is strict for \(n\ge3\), because strictly increasing partial masses cannot all equal \(1/2\). Thus \(S\) has a unique maximizer \(\lambda_*\). Define \(c_i^*\) by the formula in the finding; it is feasible and uses the full budget. At this conductance vector, direct substitution gives
\[
H_{1n}-H_{n1}=\frac{2S(\lambda_*)}{B}S'(\lambda_*).
\]
If \(\lambda_*\) is interior, its derivative vanishes, so both hitting times equal the attained lower bound \(S(\lambda_*)^2/B\). If \(\lambda_*=1\), then \(S'(1)\ge0\), so \(H_{1n}\ge H_{n1}\); the same lower bound is attained by the forward hitting time. The case \(\lambda_*=0\) is analogous, with \(S'(0)\le0\). Consequently the universal lower bound is attained in every case. Each endpoint hitting-time functional is strictly convex in the positive vector \((c_i)\), and their maximum is strictly convex. The minimizing vector is therefore unique, including at the phase boundary.

**Step 4: the exact surcharge transition.** For uniform masses, \(M_i=i/n\). Since \(\sum_i(2i-n)=0\), a single surcharge at \(k>n/2\) gives
\[
S'(1/2)=\frac{(\sqrt Q-1)(2k-n)}{\sqrt2\,n},
\qquad
S'(1)=\frac{A_n+(\sqrt Q-1)(2k-n)/\sqrt k}{2\sqrt n}.
\]
Pairing terms indexed by \(i\) and \(n-i\) in \(A_n\) proves \(A_n<0\): for \(i<n/2\), the pair equals \((2i-n)(i^{-1/2}-(n-i)^{-1/2})<0\). The condition \(S'(1)\ge0\) is therefore equivalent to \(Q\ge Q_c(n,k)\). For \(1<Q<Q_c\), the signs at \(1/2\) and \(1\) are opposite, and strict concavity gives a unique maximizer in between. At equality the endpoint multiplier is \(1\) and the two directions tie; above it the forward direction strictly dominates. This proves every finite-size regime without solving the original multi-variable optimization numerically.

**Step 5: quadratic and quartic scales.** Writing \(x_i=i/n\) gives
\[
\frac{A_n}{n^{3/2}}=\frac1n\sum_{i=1}^{n-1}\frac{2x_i-1}{\sqrt{x_i}}
\longrightarrow\int_0^1\frac{2x-1}{\sqrt{x}}\,dx=-\frac23.
\]
The integrable singularity at zero is harmless: the contribution from \(i\le\varepsilon n\), after absolute normalization, is bounded by a constant times \(\sqrt\varepsilon\); the rest is an ordinary Riemann sum. If \(k_n/n\to\theta>1/2\), then \((2k_n-n)/\sqrt{k_n}\sim\sqrt n(2\theta-1)/\sqrt\theta\), so the exact expression for \(Q_c\) yields the stated quadratic limit. If \(n\) is even and \(k=n/2+s\) for fixed \(s\ge1\), then \((2k-n)/\sqrt k\sim2\sqrt2s/\sqrt n\). Combining this with \(A_n\sim-(2/3)n^{3/2}\) yields the quartic limit \(1/(18s^2)\).

**Exact three-state illustration.** With \(n=3\), \(k=2\), and prices \((1,Q)\), the threshold is exactly \(Q_c=2\). For \(1\le Q\le2\) the two conductances are equal to \(B/(1+Q)\), and the optimal worst hitting time is \((1+Q)/B\). For \(Q\ge2\) the optimum is instead
\[
\frac{(1+\sqrt{2Q})^2}{3B},\qquad
c_1^*=\frac{B}{1+\sqrt{2Q}},\qquad
c_2^*=\frac{B\sqrt{2/Q}}{1+\sqrt{2Q}}.
\]
The formulas agree at \(Q=2\). The fact that the robust optimum ceases to balance the two directions at a finite surcharge is a genuine active-constraint transition.

## Verification

A standalone Python checker, `verify.py`, independently reconstructs first-hitting times by solving absorbing-generator linear systems, checks the closed-form allocation against full nonsymmetric numerical epigraph optimizations, samples heterogeneous stationary distributions and prices, verifies the surcharge regimes, and tests the two asymptotic scales. Running `python verify.py` in an environment with NumPy and SciPy produced:

`PASS: 19538 deterministic finite assertions (not a proof of the universal theorem)`

These are finite tests and do not establish the universal claims. Universal correctness follows from the backward-equation, strict concavity, Cauchy–Schwarz equality, and singular Riemann-sum arguments above. The reproducibility script does not use precomputed expected solutions for the absorbing-generator checks.

## Relationship to prior work

Palacios, Gómez and Del Río (2014) give voltage representations and birth-and-death hitting-time formulas; those are the background for Step 1 and are not claimed as new. Their paper treats hitting-time evaluation rather than joint price-budget optimization with a prescribed stationary distribution. Ghosh, Boyd and Saberi (2006/2008) prove convexity and optimize **total** effective resistance, giving a square-root formula for trees, and mention minimizing the maximum **symmetric** effective resistance as an SDP extension. Here the objective is instead the maximum of two **directed** endpoint first-hitting times; it depends on the prescribed stationary masses and generally differs from maximum effective resistance even on a path. The exact balance-to-one-sided threshold and its quadratic-versus-quartic scaling are not consequences of the stated optimal-total-resistance solution. Aldous and Fill's reversible-chain notes establish hitting- and commute-time theory, not this conductance-cost classification. Berman (1964) supplies an important, substantially broader predecessor for continuous convex activity-time versus resource allocation in critical-path PERT networks. Its abstract describes a parametric convex resource-allocation treatment, so the general minimax/Cauchy–Schwarz optimization mechanism here is not claimed as a new resource-allocation principle. The mathematical contribution assessed here is specifically the Markov-path reduction with fixed stationary masses and, in particular, the exact spatially dependent one-surcharge frontier and its quadratic-to-quartic asymptotic transition. The full Berman paper was not accessible for detailed theorem comparison; a stronger general precedent remains a residual originality risk.

This is a statement comparison, not a claim that keyword searches prove priority. A specialist treatment of robust hitting-time resource allocation or a general PERT time-cost theorem may still overlap the result; independent literature review remains valuable.

## Limitations

The theorem requires a finite *path*, fixed strictly positive stationary masses, continuously adjustable positive conductances, a linear conductance budget, and continuous-time mean hitting times. It makes no assertion for general graphs, discrete-time chains whose stationary law changes with conductances, stationary-target Kemeny time, first-passage tail probabilities, or control constraints on individual jump rates. The one-surcharge closed-form frontier is stated only for prices \(Q\ge1\) and an edge strictly to the right of the midpoint; the general scalar allocation theorem covers all positive price vectors. The finite verification suite cannot rule out a hidden published equivalent.

## References

1. J. L. Palacios, E. Gómez and M. Del Río, *Hitting Times of Walks on Graphs through Voltages*, Journal of Probability (2014), Article 852481, first published 20 May 2014. https://doi.org/10.1155/2014/852481 (open full text: https://onlinelibrary.wiley.com/doi/10.1155/2014/852481).
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66; shorter 2006 conference version. Public full text: https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/ghosh_boyd.pdf.
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapters 3.7 and 4, online manuscript. https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S7.html and https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch4.html.

4. E. B. Berman, *Resource Allocation in a PERT Network Under Continuous Activity Time-Cost Functions*, Management Science 10 (1964), 734–745, published online 1 July 1964. https://doi.org/10.1287/mnsc.10.4.734. Abstract publicly accessible; complete text not inspected.
