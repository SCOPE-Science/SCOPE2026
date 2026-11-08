# A logarithmic assortativity bias and two independent fluctuation scales in soft two-community attachment

## Finding

Let a connected graph initially consist of one type-A and one type-B vertex joined by an edge. For each integer \(i\ge 1\), add one vertex, independently of previous arrivals assigning its type A or B with probability \(1/2\) each. Given an arriving vertex of type \(u\), choose its parent among all existing vertices with weight \(1-q\) for the same type and \(q\) for the opposite type, with one edge attached to the chosen parent. Here \(q\in(0,1)\) is fixed. This is the two-type symmetric, degree-exponent-zero specialization of the soft attachment model described in [1].

Let \(Y_i\) indicate that new edge \(i\) joins opposite types, let \(C_n=\sum_{i=1}^nY_i\), let \(\mathcal F_i\) contain the first \(i\) additions, and set the predictable compensator \(A_n=\sum_{i=1}^n\mathbb E(Y_i\mid\mathcal F_{i-1})\). Put
\[
a=1-2q,\qquad b=2q(1-q)(1-2q).
\]
Then, for every fixed \(q\in(0,1)\):

1. Almost surely, \(\displaystyle (A_n-nq)/\log n\longrightarrow b\); moreover \(\displaystyle\mathbb EC_n=nq+b\log n+O_q(1)\).
2. If \(q\ne1/2\), then
\[
\left(\frac{C_n-A_n}{\sqrt n},\frac{A_n-\mathbb EA_n}{\sqrt{\log n}}\right)
\ \Rightarrow\ \left(\sqrt{q(1-q)}Z_1,2bZ_2\right),
\]
where \(Z_1,Z_2\) are independent standard Gaussian variables. For all \(q\in(0,1)\), \((C_n-nq)/\sqrt n\Rightarrow\mathcal N(0,q(1-q))\).
3. If \(q=1/2\), \(C_n\) is exactly \(\operatorname{Bin}(n,1/2)\), and \(A_n=n/2\) deterministically. More generally, in the *hard* community-choice attachment model [1] with the same balanced arrivals and cross-type choice probability \(q\), \(C_n\) is exactly \(\operatorname{Bin}(n,q)\) for each \(n\). The logarithmic term and its fluctuations are therefore genuine effects of soft rather than hard attachment.

In particular, \(q=1/4\) gives \(\mathbb EC_n=n/4+(3/16)\log n+O(1)\), whereas \(q=3/4\) gives \(\mathbb EC_n=3n/4-(3/16)\log n+O(1)\). The sign reversal is exact for all fixed \(q\) on either side of \(1/2\).

## Assumptions and scope

The degree exponent is exactly \(\gamma=0\); the arriving types are independent fair coins; the two affinity weights are symmetric and fixed; both initial types are present. The initial edge is not included in \(C_n\). No claim is made for unequal type-arrival probabilities, positive degree exponent, time-varying affinities, or a growing number of types. The random compensator \(A_n\) is computed before each new type is sampled and before its attachment is made.

Write \(\xi_i=1\) for an A arrival and \(\xi_i=-1\) for a B arrival, \(S_j=\sum_{i=1}^j\xi_i\), and \(y_j=S_j/(j+2)\). At time \(i\) the population before addition has \(i+1\) vertices and type imbalance \(S_{i-1}\). Define \(T_n=\sum_{j=0}^{n-1}y_j^2\). The exact predictor identity is
\[
\mathbb E(Y_i\mid\mathcal F_{i-1})=f_q(y_{i-1}),\qquad
 f_q(y)=\frac{q(1+a y^2)}{1-a^2y^2}
 =q+\frac{b y^2}{1-a^2y^2}.
\]
As \(|a|<1\), all denominators are strictly positive on \([-1,1]\).

## Proof

**1. Conditional probabilities and finite remainder.** Before arrival, let the existing type counts be \(N_A,N_B\), \(N=N_A+N_B\), and \(y=(N_A-N_B)/N\). Conditional on an A arrival, the chance of a cross-type edge is \(q(1-y)/(1+a y)\); conditional on a B arrival it is \(q(1+y)/(1-a y)\). Averaging equally and simplifying gives \(f_q\). Thus
\[
A_n=nq+bT_n+R_n,\qquad
R_n=ba^2\sum_{j=0}^{n-1}\frac{y_j^4}{1-a^2y_j^2}.
\]
For a simple symmetric random walk, \(\mathbb E S_j^4=3j^2-2j\) and \(\mathbb E S_j^8=O(j^4)\). Because \(|a|<1\), \(\sum_j\mathbb Ey_j^4<\infty\) and \(\sum_j\|y_j^4\|_2<\infty\). Consequently \(R_n\) converges almost surely and in \(L^2\) to a finite random variable. Its mean remains bounded uniformly in \(n\).

**2. First- and second-order imbalance asymptotics.** Since \(S_j\) is a centered simple random walk,
\[
\mathbb ET_n=\sum_{j=0}^{n-1}\frac{j}{(j+2)^2}=\log n+O(1).
\]
For \(0\le i\le j\), independence of increments and \(S_j=S_i+(S_j-S_i)\) give
\[
\operatorname{Cov}(S_i^2,S_j^2)=\operatorname{Var}(S_i^2)=2i(i-1).
\]
It follows by summation that
\[
\begin{aligned}
\operatorname{Var}(T_n)
&=2\sum_{j=0}^{n-1}\frac{j(j-1)}{(j+2)^4}
+4\sum_{0\le i<j<n}\frac{i(i-1)}{(i+2)^2(j+2)^2}\\
&=4\log n+O(1).
\end{aligned}
\]
Chebyshev's inequality along \(n_m=\lfloor e^{m^2}\rfloor\), Borel–Cantelli, and monotonicity of \(T_n\) prove \(T_n/\log n\to1\) almost surely (the ratio of successive subsequence logarithms tends to one). This and Step 1 prove the almost-sure drift and mean assertions.

For its fluctuations, the identity \(S_j^2-j=2\sum_{k=1}^j S_{k-1}\xi_k\) gives
\[
T_n-\mathbb ET_n=2\sum_{k=1}^{n-1}S_{k-1}\xi_k\sum_{j=k}^{n-1}(j+2)^{-2}
=2L_n+O_{\mathsf P}(1),
\]
where \(L_n=\sum_{k=1}^{n-1}S_{k-1}\xi_k/(k+2)\). Indeed the difference of the inner sum from \((k+2)^{-1}-(n+2)^{-1}\) is \(O(k^{-2})\), whose contribution has bounded second moment by martingale orthogonality; the terminal \(n^{-1}\) term is \(O_{\mathsf P}(1)\). The predictable bracket of \(L_n\) is \(\sum_{k<n}S_{k-1}^2/(k+2)^2\sim\log n\) almost surely by the preceding imbalance law and a summable denominator shift. Every martingale increment of \(L_n\) has magnitude at most one. The bounded-increment martingale central limit theorem yields
\[
\frac{T_n-\mathbb ET_n}{\sqrt{\log n}}\Rightarrow\mathcal N(0,4).
\]
The convergent \(R_n\) may be subtracted or added without changing this limit; hence \((A_n-\mathbb EA_n)/\sqrt{\log n}\Rightarrow\mathcal N(0,4b^2)\).

**3. Edge-count martingale and joint independence.** Define \(M_n=C_n-A_n\). Its differences are bounded, with predictable variance \(f_q(y_{i-1})(1-f_q(y_{i-1}))\). Since \(y_j\to0\) almost surely by the strong law, its bracket divided by \(n\) tends to \(q(1-q)\). The martingale central limit theorem yields \(M_n/\sqrt n\Rightarrow\mathcal N(0,q(1-q))\).

For joint convergence with \(L_n\), conditional on the old graph the incoming sign \(\xi_i\) satisfies
\[
\operatorname{Cov}(Y_i,\xi_i\mid\mathcal F_{i-1})=
-\frac{2q(1-q)y_{i-1}}{1-a^2y_{i-1}^2}.
\]
Therefore the off-diagonal predictable bracket of \(M_n/\sqrt n\) and \(L_n/\sqrt{\log n}\) has absolute value at most
\[
\frac{K_q}{\sqrt{n\log n}}\sum_{i=1}^n y_{i-1}^2
=O_{\mathsf P}\!\left(\sqrt{\frac{\log n}{n}}\right)\to0.
\]
The two-dimensional bounded-jump martingale central limit theorem consequently gives independent Gaussian limits. Step 2 transfers the second coordinate from \(L_n\) to \(A_n\). Finally \(A_n-nq=O_{\mathsf P}(\log n)\), which is negligible at scale \(\sqrt n\), proving the ordinary central limit theorem for \(C_n\). In the hard model, independent cross-community choices are Bernoulli \(q\) at every step, proving the exact binomial assertion.

## Verification

Run `python3 check.py` with the Python standard library. It performs 15,432 exact-rational assertions: conditional probability identities over multiple nondegenerate affinities and all feasible imbalances up to population size 30; exact dynamic-programming enumeration of cross-edge counts; and finite simple-walk quadratic-functional expectations, variances and covariance identities. It reports `PASS 15432 exact-rational assertions`. These finite calculations check coefficients, boundary conventions and formulas only; they do not prove the almost-sure or weak limits, which follow from the analytic argument above.

## Relationship to prior work

Ben-Hamou, Broutin and Cazaux [1] define both hard and soft two-community attachment, study degree frequencies and their limiting fixed points, and explicitly include \(\gamma=0\). The present claim concerns the *cross-community edge process* and its second-order predictable structure, not the degree-frequency limit. Bhamidi, Fan, Fraiman and Nobel [2] previously formulated community-weighted recursive trees (which include the zero-degree-exponent affinity rule) and obtained limiting degree distributions; this model formulation and its first-order analysis are prior art, not new here. Antunes, Banerjee, Bhamidi and Pipiras [3] treat the encompassing attribute-kernel model, including the zero-degree-exponent specialization, and analyze homophily-related first-order network observables and local limits; those results do not supply the stated second-order cross-edge count or predictable-compensator laws. The model itself and martingale central limit methodology are not claimed as new. The claimed contribution is the explicit logarithmic bias, its sharp sign reversal, and the joint, separated, independent fluctuation laws. Literature searches did not identify a theorem already implying this precise assertion; unidentified equivalent results remain possible.

## Limitations

The result does not extend the new theorem to \(\gamma>0\), asymmetric arrival probabilities, or unequal within-community affinity parameters. The compensator's mesoscopic fluctuations have order \(\sqrt{\log n}\), which are masked by the \(\sqrt n\) fluctuations of the raw cross-edge count. The result provides weak convergence, not a Berry–Esseen rate or finite-sample confidence intervals. Independent peer assessment and definitive historical-priority validation have not been performed.

## References

[1] A. Ben-Hamou, N. Broutin and C. Cazaux, *Sublinear multi-type preferential attachment*, arXiv:2611.06904v1 (first public 2026-11-04), https://arxiv.org/html/2611.06904v1 .

[2] S. Bhamidi, R. Fan, N. Fraiman and A. Nobel, *Community modulated recursive trees and population dependent branching processes*, arXiv:2004.02697 (first public 2020-04-06), https://arxiv.org/abs/2004.02697 .

[3] N. Antunes, S. Banerjee, S. Bhamidi and V. Pipiras, *Attribute network models, stochastic approximation, and network sampling and ranking algorithms*, arXiv:2304.08565 (2023), https://arxiv.org/abs/2304.08565 .
