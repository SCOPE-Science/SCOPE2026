# Sharp Gaussian deficit fluctuations for fixed-round walks on growing complete graphs

## Finding

Fix an integer \(q\ge2\). At stage \(i=1,2,\ldots,n\), a new labeled vertex \(i\) is introduced and a walker makes \(q\) transitions on the complete graph on \(\{1,\ldots,i\}\), with transition probabilities \(1/i\) to every vertex, including the present one. Let \(U_n\) be the number of vertices never visited after stage \(n\), and let \(\mu_n=\mathbb E U_n\). An observation of vertex 1 before the stages is immaterial because the first stage visits it with certainty.

**Theorem.** For every fixed integer \(q\ge2\):

1. The finite-size mean and conditional regression are exactly
   \[
   \mu_n=\frac1{n^q}\sum_{j=0}^{n-1}j^q,\qquad
   \mathbb E[U_n-\mu_n\mid\mathcal F_m]
   =\left(\frac mn\right)^q(U_m-\mu_m),\quad 1\le m\le n,
   \]
   where \(\mathcal F_m\) contains all transitions through stage \(m\). Consequently
   \[
   \operatorname{Cov}(U_m,U_n)
   =\left(\frac mn\right)^q\operatorname{Var}(U_m).
   \]
2. Write \(\sigma_q^2=q^2/((q+1)^2(2q+1))\). Then
   \[
   \frac{\operatorname{Var}(U_n)}n\longrightarrow\sigma_q^2>0,
   \qquad
   \frac{U_n-\mu_n}{\sqrt n}\ \Longrightarrow\ N(0,\sigma_q^2).
   \]
   In particular, \(\mu_n=n/(q+1)-1/2+O_q(n^{-1})\), so the same normal limit holds with centering by \(n/(q+1)\). If \(m/n\to\lambda\in(0,1]\), the correlation of \(U_m\) and \(U_n\) tends to \(\lambda^{q+1/2}\).
3. For all integers \(n\ge1\) and all real \(t>0\),
   \[
   \mathbb P(|U_n-\mu_n|\ge t)
   \le 2\exp\left(-\frac{2t^2}{qn}\right).
   \]
4. At \(q=2\), the finite-size variance has the exact factorization, for all \(n\ge2\),
   \[
   \operatorname{Var}(U_n)
   =\frac{(n+1)(2n-1)(2n+1)(4n-5)}{180n^2(n-1)}.
   \]

The Gaussian law, sharp asymptotic variance constant, exact time regression, and finite-size two-round variance together describe fluctuation behavior not provided by mean estimates for this model.

## Assumptions and scope

The transitions are independent uniform draws at each stage, including self-transitions. The stage duration \(q\) is constant and is fixed as \(n\to\infty\). For \(q\) that changes with \(n\), only the displayed finite-size identities and concentration inequality are asserted, not the Gaussian or variance limits. The model is a growing complete graph, not an arbitrary evolving network. The one-round model \(q=1\) is an Eulerian/subexcedant-function case already studied in classical combinatorics and is *not* advanced here as a novel limit theorem.

## Proof

**1. Exact recursion and mean.** At the beginning of stage \(i\), exactly \(R_i=U_{i-1}+1\) of the \(i\) available labels are unseen. Let \(B_i\) be the number of distinct formerly unseen labels hit in the \(q\) independent stage-\(i\) draws. Then
\[
U_i=U_{i-1}+1-B_i.
\]
Given \(\mathcal F_{i-1}\), a fixed unseen label is missed by all stage draws with probability \(a_i=(1-1/i)^q\). Consequently
\[
\mathbb E[U_i\mid\mathcal F_{i-1}]
=a_i(U_{i-1}+1),\qquad
\mu_i=a_i(\mu_{i-1}+1),\quad \mu_0=0.
\]
The telescoping product \(\prod_{s=j}^n a_s=((j-1)/n)^q\) gives the asserted exact mean. Put \(Z_i=U_i-\mu_i\) and \(\xi_i=U_i-\mathbb E[U_i\mid\mathcal F_{i-1}]\); then \(Z_i=a_i Z_{i-1}+\xi_i\). Since \(\prod_{s=i+1}^n a_s=(i/n)^q\),
\[
Z_n=\sum_{i=1}^n\left(\frac in\right)^q\xi_i.
\]
Each \(\xi_i\) is a martingale difference satisfying \(|\xi_i|\le q\). Conditioning the recursion at any earlier stage \(m\) proves the exact conditional regression; multiplying by \(Z_m\) and averaging proves the temporal covariance formula.

**2. Conditional fluctuation calculation.** Set \(r=U_{i-1}+1\), \(p_i=1-(1-1/i)^q\), and \(b_i=(1-2/i)^q-(1-1/i)^{2q}\) for \(i\ge2\). Indicator inclusion-exclusion gives
\[
\mathbb E[\xi_i^2\mid\mathcal F_{i-1}]
=\operatorname{Var}(B_i\mid\mathcal F_{i-1})
=r p_i(1-p_i)+r(r-1)b_i.
\]
For fixed \(q\), uniformly as \(i\to\infty\),
\[
p_i=\frac qi+O_q(i^{-2}),\qquad
b_i=-\frac q{i^2}+O_q(i^{-3}).
\]
The recurrence for \(Z_i\), orthogonality of martingale differences, and \(|\xi_i|\le q\) imply \(\mathbb E Z_i^2\le q^2 i\). Together with the exact mean asymptotic, this gives \(U_i/i\to1/(q+1)\) in \(L^2\). Thus the conditional variance above converges in probability to
\[
v_q=q\frac1{q+1}\left(1-\frac1{q+1}\right)=\frac{q^2}{(q+1)^2}.
\]
It is bounded by \(q^2\), so its expectations converge to the same constant.

**3. Sharp variance and central limit.** Orthogonality in the weighted martingale representation gives
\[
\operatorname{Var}(U_n)
=\sum_{i=1}^n\left(\frac in\right)^{2q}\mathbb E\xi_i^2.
\]
A bounded weighted Cesàro argument yields
\[
\frac1n\operatorname{Var}(U_n)
\longrightarrow v_q\int_0^1 s^{2q}\,ds
=\frac{q^2}{(q+1)^2(2q+1)}.
\]
For the triangular martingale-difference array \(n^{-1/2}(i/n)^q\xi_i\), each term has magnitude at most \(q/\sqrt n\), so the conditional Lindeberg condition is automatic. Its predictable quadratic variation converges in probability to the same constant: split the weighted sum at \(\varepsilon n\), use the uniform bound \(q^2\) on the initial piece, and use the \(L^2\) convergence of \(U_{i-1}/i\) on the remainder. The martingale central limit theorem therefore establishes the stated Gaussian convergence. The correlation limit follows from the exact temporal covariance relation and the variance asymptotic.

**4. Concentration.** View \(U_n\) as a function of the \(qn\) independent stage draws. Changing one draw removes at most one previously observed label and adds at most one newly observed label, so the *number* of unseen labels changes by at most one. The bounded-differences inequality with \(qn\) Lipschitz constants each equal to one gives the exponential bound.

**5. Two-round finite variance.** Let \(I_j\) indicate that label \(j\) remains unvisited. For \(1\le i<j\le n\), the triangular draw structure gives
\[
\mathbb E I_j=\left(\frac{j-1}{n}\right)^q,\qquad
\mathbb E(I_iI_j)=\left(\frac{(i-1)(j-2)}{n(n-1)}\right)^q.
\]
For \(q=2\), sum the diagonal and off-diagonal terms in \(\operatorname{Var}(\sum_j I_j)\). The resulting power sums simplify exactly to the displayed rational factorization. A second independent derivation is the stage-count Markov transition used by the attached checker.

## Verification

Run `python3 checker.py` in a directory containing the accompanying standalone Python file. It uses only the standard library and reports 961 exact rational tests, comparing (a) a Markov-state recurrence with the joint-inclusion variance, (b) the full two-round finite-size variance, and (c) direct enumeration of trajectories at small sizes. Finite computations check the algebra but do **not** establish the infinite Gaussian limit; the latter uses the explicitly verified hypotheses of the martingale central limit theorem in Proof 3.

## Relationship to prior work

Kijima, Shimizu and Shiraga introduced the growing-graph random walk and determined the first-order expected number of unvisited vertices for constant duration, among broader regimes. Their preprint (arXiv:2008.10837, first publicly posted 2020-08-25), full version and concluding remarks do not establish this constant-duration Gaussian fluctuation law or its sharp variance constant; the authors explicitly identified concentration as a direction for future work. The complete-graph case here has a uniform self-loop transition matrix, as in their model.

The \(q=1\) model is also a uniform subexcedant function. Classical results (Dumont; discussed by Visontai) already give its Eulerian count distribution; Beyene and coauthors describe the exact correspondence between the image set of a subexcedant function and weak-excedance positions of a permutation. Thus the one-round case and its simple consequences are existing mathematics, not a novelty claim. The result here concerns **every fixed \(q\ge2\)** and in particular its Gaussian fluctuations and sharp temporal covariance. General coupon-collection limit results with a fixed pool of types do not directly supply the growing-support calculation.

## Limitations

The theorem does not cover noncomplete networks, nonuniform transition probabilities, random durations, or durations increasing with size. Its central limit theorem has no explicit Berry--Esseen rate. All novelty judgments are literature-limited and subject to independent historical review. The finite checker supplies no independent infinite-dimensional proof or external certification.

## References

1. S. Kijima, N. Shimizu, and T. Shiraga, *How Many Vertices Does a Random Walk Miss in a Network with Moderately Increasing the Number of Vertices?*, arXiv:2008.10837 (first posted 2020-08-25), https://arxiv.org/abs/2008.10837; *Mathematics of Operations Research* (2025), https://doi.org/10.1287/moor.2023.0060.
2. F. Beyene, R. Mantaci, J. Backelin, and S. A. Fufa, *Set Partitions and Other Bell Number Enumerated Objects*, *Journal of Integer Sequences* 26 (2023), Article 23.1.8, https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.pdf.
3. M. Visontai, *Some Remarks on the Joint Distribution of Descents and Inverse Descents*, *Electronic Journal of Combinatorics* 20(1) (2013), P52, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p52/pdf/.
4. H. M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, *Advances in Applied Probability* 44 (2012), 429–451, https://doi.org/10.1239/aap/1339878719.
5. P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press (1980), ISBN 0-12-319350-8.
6. C. McDiarmid, *Centering Sequences with Bounded Differences*, *Combinatorics, Probability and Computing* 6 (1997), 79–86, https://doi.org/10.1017/S0963548396002854.
