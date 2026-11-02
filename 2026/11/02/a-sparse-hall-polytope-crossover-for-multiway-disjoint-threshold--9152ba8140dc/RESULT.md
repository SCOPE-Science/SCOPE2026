# A sparse Hall-polytope crossover for multiway disjoint threshold testimony

## Finding

**Theorem (sparse multiway disjoint-testimony crossover).** Fix an integer \(r\ge2\) and real offsets \(a_1,\ldots,a_r\). For each \(n\), let \(p_n\in(0,1)\), with \(p_n\to0\) and \(n p_n\to\infty\), and put
\[
s_n=\sqrt{n p_n(1-p_n)},\qquad
k_{n,i}=\left\lceil n p_n-a_i s_n\right\rceil,\qquad
\tau_n=\frac{n p_n^2}{s_n}.
\]
For sufficiently large \(n\), all thresholds lie between \(1\) and \(n\). Independently draw \(r\) Bernoulli-\(p_n\) subsets \(S_1,\ldots,S_r\) of \(\{1,\ldots,n\}\). A disjoint testimony is a choice of mutually disjoint subsets \(W_i\subseteq S_i\) with \(\lvert W_i\rvert=k_{n,i}\). Define the **product-space testimony defect**
\[
D_n=\prod_{i=1}^r\Pr\{\operatorname{Bin}(n,p_n)\ge k_{n,i}\}
-\Pr\{\text{a disjoint testimony exists}\}.
\]
The quantity \(D_n\) is nonnegative. This product-space defect is distinct from the diagonal BK gap evaluated on a single configuration.

If \(\tau_n\to\tau\in[0,\infty)\), then
\[
D_n\longrightarrow F_{r,\boldsymbol a}(\tau),
\]
where, for independent standard normals \(Z_1,\ldots,Z_r\) and \(E_i=Z_i+a_i\),
\[
F_{r,\boldsymbol a}(\tau)=
\Pr\left\{E_i\ge0\ \text{for every }i,\quad
\exists J\subseteq\{1,\ldots,r\},\ \lvert J\rvert\ge2:
\sum_{i\in J} E_i<\binom{\lvert J\rvert}{2}\tau\right\}.
\]
Equivalently, with \(E_{(1)}\le\cdots\le E_{(r)}\) denoting their order statistics, the probability of successful testimony tends to
\[
\Pr\left\{E_i\ge0\ \forall i,\ \sum_{i=1}^j E_{(i)}\ge\binom j2\tau\text{ for }j=2,\ldots,r\right\}.
\]
If instead \(\tau_n\to\infty\), then \(D_n\to\prod_{i=1}^r\Phi(a_i)\). The function \(F_{r,\boldsymbol a}\) is continuous and strictly increasing on \([0,\infty)\), equals zero at zero, and approaches \(\prod_i\Phi(a_i)\) at infinity. Its small- and large-parameter laws are
\[
F_{r,\boldsymbol a}(\tau)=
\frac{\tau^2}{2}\sum_{i<j}\phi(a_i)\phi(a_j)
\prod_{h\ne i,j}\Phi(a_h)+O(\tau^3)
\qquad(\tau\downarrow0),
\]
\[
\prod_i\Phi(a_i)-F_{r,\boldsymbol a}(\tau)
\sim\overline\Phi\left(\frac{\binom r2\tau-\sum_i a_i}{\sqrt r}\right)
\qquad(\tau\to\infty).
\]
Here \(\Phi\) and \(\phi\) are the standard normal distribution and density, and \(\overline\Phi=1-\Phi\). In particular the three regimes \(p_n\ll n^{-1/3}\), \(p_n\asymp n^{-1/3}\), and \(p_n\gg n^{-1/3}\) correspond to zero, partial, and complete limiting collision defect. If \(p_n\sim\gamma n^{-1/3}\), then \(\tau_n\to\gamma^{3/2}\).

For \(r=2\) and \(a_1=a_2=0\), the crossover is the elementary Gaussian integral
\[
F_{2,(0,0)}(\tau)=\int_0^\tau\phi(u)\bigl[\Phi(\tau-u)-\tfrac12\bigr]\,du,
\quad F_{2,(0,0)}(1)=0.0677300307008491\ldots .
\]

## Assumptions and scope

The number of events \(r\ge2\) and offsets \(a_i\in\mathbb R\) are **fixed** as \(n\to\infty\). The bit arrays are independent across events and coordinates, and all share \(p_n\). The thresholds may be different across events. No symmetry of the \(a_i\) is assumed. The assertions about \(\tau\to0\) or \(\tau\to\infty\) are limits of the explicit Gaussian crossover function, except for the separately stated direct \(\tau_n\to\infty\) result. The proof does not assert a joint rate uniform in \(r\) or a growing number of events.

## Proof

**1. Exact certificate geometry (capacitated Hall condition).** Set \(N_i=\lvert S_i\rvert\). Each threshold event has a witness consisting of \(k_{n,i}\) open coordinates. Replace event \(i\) by \(k_{n,i}\) distinct demand clones, all adjacent to coordinates in \(S_i\). A matching of every clone to a distinct coordinate is exactly a disjoint testimony. The ordinary Hall marriage theorem, applied to this finite bipartite graph, says that such a matching exists if and only if
\[
\left\lvert\bigcup_{i\in J}S_i\right\rvert
\ge\sum_{i\in J}k_{n,i}
\quad\text{for every nonempty }J\subseteq\{1,\ldots,r\}.
\tag{1}
\]
Indeed, necessity is immediate. For sufficiency, the neighbor set of any selection of clones from an index set \(J\) contains the union of the supports of all indices represented; (1) for that exact \(J\) bounds its size below by all clones of those indices, and hence by the selected number.

**2. Centered binomial fluctuations.** Write
\[
A_{i,n}=\frac{N_i-k_{n,i}}{s_n}.
\]
Since \(n p_n(1-p_n)\to\infty\), the triangular-array binomial central limit theorem and the ceiling error \(O(s_n^{-1})\) yield
\[
(A_{1,n},\ldots,A_{r,n})\ \Rightarrow\ (E_1,\ldots,E_r),
\qquad E_i\sim N(a_i,1)\text{ independently}.
\tag{2}
\]
For a set \(J\) of size \(j\), let the duplicate count be
\[
B_{J,n}=\sum_{i\in J}N_i-
\left\lvert\bigcup_{i\in J}S_i\right\rvert.
\]
At each coordinate its contribution is \(L-\mathbf1_{\{L>0\}}\), where \(L\sim\operatorname{Bin}(j,p_n)\). Hence
\[
\mathbb E B_{J,n}=n\{j p_n-1+(1-p_n)^j\}
=\binom j2 n p_n^2+O_r(n p_n^3).
\tag{3}
\]
Moreover, each summand is bounded by \(r\) and vanishes unless at least two events contain that coordinate. Thus
\[
\operatorname{Var}(B_{J,n})=O_r(n p_n^2).
\tag{4}
\]
For bounded \(\tau_n\), (3) divided by \(s_n\) has error \(O_r(\tau_n p_n)=o(1)\), while by (4) its standard deviation divided by \(s_n\) is \(O_r(\sqrt{p_n/(1-p_n)})=o(1)\). Therefore, jointly over the finitely many subsets,
\[
\frac{B_{J,n}}{s_n}-\binom j2\tau_n\ \xrightarrow{\Pr}\ 0.
\tag{5}
\]
By the identity \(\lvert\cup_{i\in J}S_i\rvert-\sum_{i\in J}k_{n,i}=\sum_{i\in J}(N_i-k_{n,i})-B_{J,n}\), Hall's condition (1) is equivalent to
\[
\sum_{i\in J}A_{i,n}\ge B_{J,n}/s_n\quad\forall J\ne\varnothing.
\tag{6}
\]
The limiting Gaussian vector assigns zero probability to every equality boundary \(\sum_{i\in J}E_i=\binom j2\tau\). Equations (2), (5), (6) and the portmanteau theorem give the joint subset-inequality limit and the claimed formula for \(F_{r,\boldsymbol a}(\tau)\).

**3. Divergent collisions.** If \(\tau_n\to\infty\), take two distinct indices \(i,j\). Their intersection size \(B_{\{i,j\},n}=\lvert S_i\cap S_j\rvert\) is \(\operatorname{Bin}(n,p_n^2)\), with mean \(\tau_n s_n\) and variance no greater than \(n p_n^2\). Chebyshev's inequality gives \(B_{\{i,j\},n}/s_n\to\infty\) in probability, while (2) makes \(A_{i,n}+A_{j,n}\) tight. Thus the pair constraint in (6) fails with probability tending to one. The marginal all-pass probability tends to \(\prod_i\Phi(a_i)\) by independence, proving the infinite-parameter assertion.

**4. Geometry of the Gaussian crossover.** On the positive orthant \(E_i\ge0\), the subsets of size \(j\) having the smallest sums are the \(j\) smallest coordinates. Consequently the Hall region is an intersection of the finitely many half-spaces in the stated order-statistic formula. As \(\tau\) increases, these constraints tighten monotonically. The Gaussian joint density is strictly positive throughout the orthant, so the defect strictly increases: for any \(0\le\tau_1<\tau_2\), choose two positive coordinates whose sum lies strictly between \(\tau_1\) and \(\tau_2\), with all other coordinates sufficiently large to make every other Hall constraint inactive. This produces an open region of positive Gaussian measure in the increment. Continuity follows because each boundary is a Gaussian-null hyperplane. At zero the orthant is automatically feasible, and as \(\tau\to\infty\) its feasible probability decreases to zero.

**5. Small-parameter law.** For each pair \(i,j\), a violated pair constraint within the orthant is \(E_i,E_j\ge0\) and \(E_i+E_j<\tau\). Integrating the smooth positive Gaussian density over this triangle gives
\[
\Pr\{E_i,E_j\ge0,E_i+E_j<\tau\}
=\frac{\tau^2}{2}\phi(a_i)\phi(a_j)+O(\tau^3).
\tag{7}
\]
Multiplying by the independent nonnegativity probabilities of the other coordinates gives the displayed pair contribution. A violated constraint of cardinality at least three requires all of its coordinates to be in \([0,O_r(\tau)]\) and has probability \(O(\tau^3)\). Intersections of distinct pair violations likewise involve at least three small coordinates (or four for disjoint pairs), and have probability \(O(\tau^3)\). Inclusion–exclusion over a fixed finite family therefore gives the claimed universal quadratic onset.

**6. Large-parameter Gaussian tail.** Let \(S=\sum_i E_i\), \(C=\binom r2\), and \(m=\sum_i a_i\). Feasibility implies \(S\ge C\tau\), and \(S\sim N(m,r)\), yielding
\[
\Pr\{\text{feasible}\}\le \overline\Phi((C\tau-m)/\sqrt r).
\]
For a proper subset \(J\) of size \(j<r\), conditional on \(S=s\), its sum has Gaussian mean \(j s/r+O_{\boldsymbol a}(1)\) and bounded variance \(j(1-j/r)\). Uniformly for \(s\ge C\tau\), this conditional mean exceeds \(\binom j2\tau\) by at least \(j(r-j)\tau/2+O(1)\). The same estimate for singleton constraints follows by taking \(j=1\). Gaussian tail bounds imply that, conditional on \(S\ge C\tau\), the probability that any proper Hall constraint fails tends to zero. Therefore feasibility is asymptotically equivalent to \(S\ge C\tau\), establishing the displayed large-parameter asymptotic. For two zero offsets, integration on \(0\le E_1,E_2\), \(E_1+E_2<\tau\) gives the stated one-dimensional integral.

## Verification

The standalone `verify.py` checks the capacitated Hall equivalence exhaustively against a separate brute-force matching implementation for seven small parameter configurations, computes exact rational finite-size defects under Bernoulli parameter \(2/5\), and evaluates the two-event Gaussian integral. It also compares finite multinomial simulations against the Gaussian polytope at the critical scale, with a deterministic seed and stated tolerances. Run `python verify.py` with NumPy installed. The captured output is `verification_output.txt`. Finite enumeration and Monte Carlo are corroborative only; the proof of every asymptotic assertion is the analytic argument above.

## Relationship to prior work

Pierre Tesio, *How much do increasing events occur disjointly?* (arXiv:2610.32658v1, first public 2026-10-23), provides quantitative BK-gap lower bounds and an exact two-support criterion for equal threshold events in its Section 6, explicitly **with fixed bias**. This result instead evaluates the full product-space defect in a sparse triangular array, includes arbitrary fixed numbers of independently sampled configurations and individually shifted thresholds, identifies the critical exponent \(1/3\), and obtains a complete Gaussian Hall-polytope crossover and both endpoint laws. Raphaël Cerf and Pierre Tesio, *The case of equality in BK* (arXiv:2607.02272, first public 2026-07-02), develops the two-event product-space disjoint-testimony formalism and strengthened BK inequality. The present theorem **does not claim** to extend the classical BK inequality itself, and does not claim the Hall criterion or Gaussian central limit theorem are new.

## Limitations

The theorem assumes fixed \(r\), independent uniform Bernoulli coordinates, and thresholds within the binomial central-limit window. No claim is made for correlated configurations, heterogeneously biased coordinates, increasing \(r\), local limit error rates, or a finite-\(n\) closed form for the multiway defect. The limit for \(\tau_n\to\infty\) and the large-parameter asymptotic of \(F\) are distinct statements. Originality comparisons relied on the identified open-access primary results and mathematical-record searches; publication-priority verification remains independent and may uncover a more general previously known theorem.

## References

1. P. Tesio, *How much do increasing events occur disjointly?*, arXiv:2610.32658v1 (2026-10-23), https://arxiv.org/html/2610.32658v1, especially Section 6 and equations (6.1)–(6.3).
2. R. Cerf and P. Tesio, *The case of equality in BK*, arXiv:2607.02272 (2026-07-02), https://arxiv.org/abs/2607.02272, especially Definition 1.4 and Theorem 1.5.
3. P. Hall, *On representatives of subsets*, Journal of the London Mathematical Society 10 (1935), 26–30 (Hall's marriage theorem).
