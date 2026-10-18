# An exact three-regime correlation reversal in a two-firm equity contagion model

## Finding

A two-firm equity network with threshold-triggered distress costs admits a sharp classification of how integration changes the **effect of shock correlation on the expected number of insolvent firms**. Fix a solvency threshold \(T>0\), a high primitive-asset benchmark \(h>T\), a low benchmark \(0<\ell<T\), a distress cost \(\beta>0\), and a reciprocal equity share \(0\le c<1\). For a single primitive-asset shock, define
\[
A=h-T>0,\qquad B=T-\ell>0,\qquad F(c)=A-(A+B+\beta)c+Bc^2.
\]
The maximal equilibrium has one insolvency when \(c\) lies below the first threshold \(c_*\), two insolvencies on an intermediate interval when this interval exists, and zero insolvencies after the full-solvency threshold. Precisely:

* If \(A\le B\), let \(c_*\in(0,1)\) be the unique root of \(F\). The maximal-equilibrium insolvency count is \(1\) for \(0\le c\le c_*\) and \(2\) for \(c_*<c<1\).
* If \(A>B\), set \(c_{\mathrm{all}}=B/A\) and
\[
\beta_{\mathrm{crit}}=\frac{(A-B)^2(A+B)}{AB}.
\]
When \(\beta>\beta_{\mathrm{crit}}\), the sharp sequence is
\[
 d(c)=\begin{cases}1,&0\le c\le c_*,\\2,&c_*<c<c_{\mathrm{all}},\\0,&c_{\mathrm{all}}\le c<1,\end{cases}
\quad
c_* =\frac{A+B+\beta-\sqrt{(A+B+\beta)^2-4AB}}{2B}.
\]
When \(\beta\le\beta_{\mathrm{crit}}\), the intermediate interval is absent: \(d(c)=1\) for \(c<c_{\mathrm{all}}\) and \(d(c)=0\) for \(c\ge c_{\mathrm{all}}\).

Now let the two primitive-asset shocks be exchangeable Bernoulli indicators with marginal shock probability \(p\in(0,1)\) and joint shock probability \(q\in[\max(0,2p-1),p]\). The exact expected number of insolvent firms at the maximal equilibrium is
\[
\mathbb E[N_{\mathrm{def}}]=2(p-q)d(c)+2q.
\]
Since the shock-indicator correlation is \(\rho=(q-p^2)/(p(1-p))\), the dependence on correlation has the exact slope
\[
\boxed{\frac{\partial\mathbb E[N_{\mathrm{def}}]}{\partial\rho}=2p(1-p)(1-d(c)).}
\]
Consequently, in the three-regime case, this slope changes **zero \(\to\) negative \(\to\) positive** as integration increases. The sign reversal concerns the expected number of defaulted firms at the *maximal static equity valuation equilibrium*, not all risk statistics or dynamical default probabilities.

## Assumptions and scope

The book-value equations, for each specified pair of primitive-asset benchmark values \(a_1,a_2\in\{\ell,h\}\), are
\[
V_1=(1-c)a_1+cV_2-\beta\mathbf 1_{\{V_1<T\}},\qquad
V_2=(1-c)a_2+cV_1-\beta\mathbf 1_{\{V_2<T\}}.
\]
Thus the external primitive-asset component is explicitly \((1-c)a_i\). This normalization keeps the no-shock/no-distress symmetric benchmark value fixed as the equity share \(c\) changes. It is an **assumption of this comparison**, not an identity for all financial cross-ownership settings. A firm exactly at \(T\) is solvent. A *maximal equilibrium* is an equilibrium whose values dominate those of every other equilibrium coordinatewise; the proof below establishes its existence for every shock pattern under consideration. Negative net book valuations are allowed by the general algebraic equations; a positive-valuation interval is given below.

Each firm independently of the equilibrium mechanism receives either the high or low benchmark, with \(a_i=\ell\) if its shock indicator is one and \(a_i=h\) otherwise. Only the two shock indicators' joint law varies; marginal \(p\), primitive-asset benchmarks, threshold, distress cost, and integration \(c\) remain fixed.

## Proof

**1. Exact candidates and their ordering.** Write \(d_i=\mathbf 1_{\{V_i<T\}}\). For any putative default indicators \(d_1,d_2\in\{0,1\}\), the only candidate values are
\[
V_1=\frac{(1-c)a_1+c(1-c)a_2-\beta(d_1+cd_2)}{1-c^2},\qquad
V_2=\frac{(1-c)a_2+c(1-c)a_1-\beta(d_2+cd_1)}{1-c^2}.
\]
The candidate is an equilibrium exactly when its two indicators agree with the strict threshold tests. Since \((I-\begin{psmallmatrix}0&c\\c&0\end{psmallmatrix})^{-1}\) has nonnegative entries, removing any distress indicator weakly raises both values. In particular, any feasible fully solvent candidate dominates every other candidate.

**2. Neither or both shocked.** For \(a_1=a_2=h\), \((h,h)\) is a fully solvent equilibrium and therefore maximal: zero defaults. For \(a_1=a_2=\ell\), a fully solvent candidate is \((\ell,\ell)\), which is infeasible. A candidate with one solvent firm has that firm's value \(\ell-c\beta/(1-c^2)<T\), also infeasible. Thus the unique equilibrium has both in distress and \(V_i=\ell-\beta/(1-c)\), giving two defaults for every \(0\le c<1\).

**3. Exactly one shocked.** By symmetry let \(a_1=\ell\), \(a_2=h\). The fully solvent candidate has
\[
V_1^{00}=\frac{\ell+ch}{1+c},\qquad V_2^{00}=\frac{h+c\ell}{1+c}.
\]
It is feasible exactly when \(A>B\) and \(c\ge B/A\). At and after this threshold it is maximal and produces zero defaults. Before that point the low-benchmark firm cannot be solvent in *any* equilibrium, since distress indicators only decrease its fully solvent candidate value.

The only possible one-default pattern before full solvency is therefore \((d_1,d_2)=(1,0)\). Its higher-benchmark firm's value is
\[
V_2^{10}=\frac{h+c\ell}{1+c}-\frac{c\beta}{1-c^2},
\quad
(1-c^2)(V_2^{10}-T)=F(c).
\]
The low-benchmark firm's value is strictly below \(T\) before \(c_{\mathrm{all}}\), so this candidate is feasible exactly when \(F(c)\ge0\). If it is feasible, it dominates the only remaining possible equilibrium (both distressed), because removing the high firm's distress raises the vector by \(\beta(c,1)/(1-c^2)\). Hence its count is one.

If \(F(c)<0\), the higher firm is insolvent even when it incurs no distress loss, so it is insolvent also in the both-distressed candidate. In that candidate the higher firm's value exceeds the lower firm's by \((1-c)(h-\ell)/(1+c)>0\). Both are thus strictly insolvent, and the both-distressed candidate is the unique feasible equilibrium before full solvency. Its default count is two.

**4. Root location and complete phases.** Since \(F(0)=A>0\), \(F(1)=-\beta<0\), and \(F\) is a strictly convex quadratic with leading coefficient \(B>0\), there is exactly one root \(c_*\in(0,1)\). If \(A\le B\), full solvency is not feasible for any \(c<1\), giving the first case. If \(A>B\), \(c_{\mathrm{all}}=B/A\in(0,1)\), and \(F\) is strictly decreasing on \([0,c_{\mathrm{all}}]\): its derivative satisfies
\[
F'(c)=-(A+B+\beta)+2Bc<-(A+B)+2B=B-A<0.
\]
The root precedes \(c_{\mathrm{all}}\) exactly when \(F(c_{\mathrm{all}})<0\). Multiplication by \(A^2\) gives the equivalent strict inequality
\[
\beta>\frac{(A-B)^2(A+B)}{AB}.
\]
This proves all phase boundaries and their endpoint conventions.

**5. Correlation.** The four mutually exclusive shock cases have probabilities \(1-2p+q,p-q,p-q,q\), respectively. From steps 2–4 their maximal-equilibrium insolvency counts are \(0,d(c),d(c),2\). Taking expectation proves the formula. Since \(q=p^2+\rho p(1-p)\), differentiation on the feasible interior of the dependence interval proves the stated exact slope; at endpoints it is the corresponding one-sided affine slope.

## Verification

For \(T=1\), \(\ell=4/5\), \(h=7/5\), and \(\beta=3/8\), one gets \(A=2/5\), \(B=1/5\), \(\beta_{\mathrm{crit}}=3/10\), \(c_{\mathrm{all}}=1/2\), and
\[
 c_* = \frac{39-\sqrt{1009}}{16}=0.4522024782\ldots.
\]
At \(0\le c\le53/100\), all actual maximal-equilibrium book values are positive for all four shock states. Indeed, the least possible candidate value is bounded below by the both-low, both-distressed value \(4/5-(3/8)/(1-c)\), whose minimum on this interval is \(1/470>0\). [At the endpoint this difference is \(4/5-75/94=1/470\).]

For \(p=1/2\) and correlation \(\rho\in[-1,1]\), the exact expected insolvency count is
\[
\mathbb E[N_{\mathrm{def}}]=\begin{cases}
1,&0\le c\le c_*,\\
3/2-\rho/2,&c_*<c<1/2,\\
1/2+\rho/2,&1/2\le c\le53/100.
\end{cases}
\]
The accompanying `verify.py` checks the four solvency indicators for each candidate using exact rational arithmetic, verifies the symbolic inverse identities and analytically derived thresholds, tests hundreds of other parameter choices, and reconstructs the correlation expectation from the full four-event distribution. It passed 7,659 assertions. These finite checks are additional reproducibility evidence; the exhaustive parameter theorem follows from the proof above.

## Relationship to prior work

The discontinuous equity-value equation and the general enumeration of candidate default configurations are established in Dasaratha, Venkatesh and Vohra (arXiv:2406.12818, Section 2), drawing on Elliott, Golub and Jackson. The present result does not claim novelty for those equations, maximal equilibria, bankruptcy costs, or generic enumeration. Its narrower claim is the **all-parameter two-bank integration threshold**, the exact condition for an intermediate two-default regime, and its explicit trichotomy in the effect of binary shock correlation under the stated external-asset normalization.

The existence of financial contagion regimes in which lower initial shock correlation can increase losses is already known: Petrone and Latora's two-bank analysis demonstrates this in a multi-period probability-of-default model. The present result is not the discovery of that qualitative possibility; its static reciprocal-equity mechanism, closed-form boundary, and zero/negative/positive *three-regime* correlation slope are different quantified statements. Weber and Weske also study nonmonotone integration effects in a broader model, principally using numerical networks rather than this exact two-firm phase law.

These distinctions leave a residual risk that other literature derives the same elementary two-firm threshold as a special case. No uniqueness of publication priority is certified.

## Limitations

This is a static, thresholded book-equity model with proportional external-asset normalization, two symmetric cross-holdings, a common solvency threshold, equal distress penalties, and two-level exchangeable shocks. It does **not** characterize loss quantiles, expected monetary losses, other equilibrium selection conventions, a dynamic debt-clearing mechanism, general multi-firm topology, or empirical bank data. The general equations can admit negative book values; the displayed numerical integration interval does not. Distress costs, risk probabilities, and outside asset responses need independent calibration for applications. The derivative with respect to correlation is a comparative-static result at fixed marginal shock probability, not a causal claim that changing financial correlation by policy has no other effects.

## References

1. K. Dasaratha, S. S. Venkatesh, R. Vohra, *Optimal Bailouts in Diversified Financial Networks*, arXiv:2406.12818v1, first public 18 June 2024. https://arxiv.org/html/2406.12818v1
2. D. Petrone, V. Latora, *A dynamic approach merging network theory and credit risk techniques to assess systemic risk in financial networks*, Scientific Reports 8 (2018), 5561. https://doi.org/10.1038/s41598-018-23689-5
3. S. Weber, K. Weske, *The joint impact of bankruptcy costs, fire sales and cross-holdings on systemic risk in financial networks*, Probability, Uncertainty and Quantitative Risk 2 (2017), 9. https://doi.org/10.1186/s41546-017-0020-9
4. M. Elliott, B. Golub, M. O. Jackson, *Financial Networks and Contagion*, American Economic Review 104 (2014), 3115–3153. https://doi.org/10.1257/aer.104.10.3115
