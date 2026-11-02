# Negative dependence and an exact covariance law for component leaves in multinomial Hoppe forests

## Finding

Fix an integer \(d\ge 2\), positive root weights \(\theta_1,\ldots,\theta_d\), and \(\theta=\sum_i\theta_i\). Construct a multinomial Hoppe forest by adding \(n\ge1\) ordinary vertices in order, each attaching to root \(i\) with weight \(\theta_i\), or to each previously arrived ordinary vertex with weight one. Let \(L_i\) be the number of **ordinary**, childless vertices in the component attached to root \(i\); roots themselves are never counted.

**Theorem (negative quadrant dependence and mixed moments).** For any disjoint, nonempty sets of roots \(A,B\), put \(L_A=\sum_{i\in A}L_i\) and \(L_B=\sum_{i\in B}L_i\). For all nondecreasing real-valued functions \(f,g\) on \(\{0,\ldots,n\}\),
\[
\operatorname{Cov}(f(L_A),g(L_B))\le0.
\]
The inequality is strict when both functions are strictly increasing. In particular, \(L_A,L_B\) are negatively quadrant dependent.

For distinct roots \(i,j\), let
\[
\mu_n=\frac{n(n+2\theta-1)}{2(n+\theta-1)},\qquad
J_n=\frac{n(n-1)\bigl(4\theta^2+4(n-1)\theta+n(n-1)-2\bigr)}{4\theta(\theta+1)(\theta+n-2)(\theta+n-1)}\quad(n\ge2),\quad J_1=0.
\]
Then the **exact** finite-size laws are
\[
\mathbb E L_i=\frac{\theta_i}{\theta}\mu_n,\qquad
\mathbb E[L_iL_j]=\theta_i\theta_jJ_n,\qquad
\operatorname{Cov}(L_i,L_j)=\theta_i\theta_j\left(J_n-\frac{\mu_n^2}{\theta^2}\right)<0.
\]
Moreover, with \(P\sim\operatorname{Dirichlet}(\theta_1,\ldots,\theta_d)\), the leaf-proportion vector can be coupled to converge in \(L^2\) to \(P/2\). Consequently,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(L_i,L_j)}{n^2}=-\frac{\theta_i\theta_j}{4\theta^2(\theta+1)},\qquad
\lim_{n\to\infty}\operatorname{Corr}(L_i,L_j)=-\sqrt{\frac{\theta_i\theta_j}{(\theta-\theta_i)(\theta-\theta_j)}}.
\]

## Assumptions and scope

At the moment just before adding ordinary vertex \(t\) (starting with \(t=1\)), the total attachment weight is \(\theta+t-1\). Thus root \(i\) has conditional attachment probability \(\theta_i/(\theta+t-1)\); each ordinary predecessor has probability \(1/(\theta+t-1)\). Every arriving vertex inherits its ancestor root's color. The base state has no ordinary vertices; every root weight is strictly positive. Statements about arbitrary increasing transforms concern *two aggregate component-leaf counts* from disjoint root groups, not the full negative-association property of all individual leaf indicators. All identities hold for every positive real choice of weights and each stated integer \(n\).

## Proof

**1. Color allocation and conditional components.** Let \(N_i\) count ordinary vertices in root \(i\)'s component. Conditional on earlier colors, a new vertex receives color \(i\) with probability \((\theta_i+N_i)/(\theta+t-1)\). Conditional further on color \(i\), its parent is root \(i\) with probability \(\theta_i/(\theta_i+N_i)\), or any existing ordinary vertex of color \(i\) with probability \(1/(\theta_i+N_i)\). Consequently, the color sequence is a Pólya urn; its final size vector has the Dirichlet-multinomial law, and conditional on the color sequence the component trees are independent Hoppe trees of weights \(\theta_i\), run for \(N_i\) arrivals. This conditional law depends on the sequence only through final sizes. Aggregating disjoint root groups preserves the same mechanism, with the grouped weight equal to the sum of member weights, as far as their *total* ordinary-leaf count is concerned.

**2. Negative regression.** Consider two disjoint groups with weights \(a,b>0\) and remaining weight \(c\ge0\). Given that group \(A\) has size \(s\), group \(B\)'s size is beta-binomial with \(n-s\) trials and parameters \((b,c)\) if \(c>0\), and deterministically \(n-s\) if \(c=0\). To see monotonicity, sample a common beta-distributed probability and then an infinite independent Bernoulli sequence: the first \(n-s\) trials generate group \(B\)'s size. Increasing \(s\) removes trials and therefore decreases that size in the usual stochastic order, strictly because \(b>0\). The Hoppe leaf count \(T_m\) itself is nondecreasing in \(m\) under the canonical sequential attachment coupling: the new vertex is initially childless and its parent, if an ordinary leaf, simultaneously ceases to be one. Hence the total leaf count changes by zero or one. Each increment is positive with positive probability, since direct attachment to the positive-weight root creates a new leaf. For nondecreasing \(f,g\), set \(\phi(s)=\mathbb Ef(T_s)\) and \(\psi(t)=\mathbb Eg(T_t)\). Both are nondecreasing; both are strictly increasing when the respective test functions are strictly increasing. By conditional independence of distinct group trees,
\[
\operatorname{Cov}(f(L_A),g(L_B))=\operatorname{Cov}(\phi(N_A),\psi(N_B)).
\]
Because \(\mathbb E[\psi(N_B)\mid N_A=s]\) decreases with \(s\), the last covariance is nonpositive by the covariance identity using two independent copies of \(N_A\). It is strict for strictly increasing \(f,g\): \(N_A\) is nondegenerate when \(n\ge1\), and both opposing regression functions are then strictly monotone. Taking threshold functions proves negative quadrant dependence.

**3. Exact means and mixed moments.** Write \(S_i(t)\) for the color-\(i\) population after \(t\) arrivals. Conditional on the forest at this time, the increments satisfy
\[
\mathbb E[\Delta S_i\mid\mathcal F_t]=\frac{\theta_i+S_i}{\theta+t},\qquad
\mathbb E[\Delta L_i\mid\mathcal F_t]=\frac{\theta_i+S_i-L_i}{\theta+t}.
\]
For different roots, both products \(\Delta S_j\Delta L_i\) and \(\Delta L_i\Delta L_j\) vanish. The Dirichlet-multinomial moments give, for distinct \(i,j\),
\[
\mathbb ES_i(t)=\frac{\theta_i t}{\theta},\qquad
\mathbb E[S_i(t)S_j(t)]=\frac{\theta_i\theta_jt(t-1)}{\theta(\theta+1)}.
\]
Exchangeability of root weights allows us to define scalar moments by \(\mathbb EL_i(t)=\theta_i\mu_t/\theta\), \(\mathbb E[S_j(t)L_i(t)]=\theta_i\theta_jH_t\), and \(\mathbb E[L_i(t)L_j(t)]=\theta_i\theta_jJ_t\), for \(i\ne j\). Expanding products using the increment equations and applying the moments just given yields the deterministic recurrences
\[
\mu_{t+1}=\left(1-\frac1{\theta+t}\right)\mu_t+1,\qquad \mu_0=0,
\]
\[
H_{t+1}=H_t+\frac{\mu_t/\theta+t/\theta+t(t-1)/[\theta(\theta+1)]}{\theta+t},\qquad H_0=0,
\]
\[
J_{t+1}=\left(1-\frac2{\theta+t}\right)J_t+\frac{2\mu_t/\theta+2H_t}{\theta+t},\qquad J_0=0.
\]
Direct substitution and induction give the unique solutions stated for \(\mu_n,J_n\), together with
\[
H_n=\frac{n(n-1)(2\theta+n)}{2\theta(\theta+1)(\theta+n-1)}\quad(n\ge2),\qquad H_0=H_1=0.
\]
Initial cases \(n=0,1\) agree with the definitions. The covariance identity follows by subtracting the product of means. Its **strict negativity** follows independently from Step 2 with identity functions, avoiding any unproved sign manipulation of the displayed rational expression.

**4. Persistent Dirichlet dependence.** For a Hoppe tree of positive root weight \(a\) containing \(m\) ordinary vertices, the same one-step recursion gives
\[
\mathbb ET_m=\frac{m(m+2a-1)}{2(m+a-1)},\qquad \operatorname{Var}(T_m)\le m/4.
\]
The variance bound follows from the conditional variance formula: the expected increment is affine in \(T_m\) with slope \(-1/(a+m)\), and its conditional variance is at most \(1/4\). The mean differs from \(m/2\) by at most \(\max\{1,a\}/2\). Thus, conditional on its component size \(N_i\), the squared error \(\mathbb E[(L_i-N_i/2)^2\mid N_i]\) is bounded by \(N_i/4+O_a(1)\), uniformly in \(N_i\), and hence \((L_i-N_i/2)/n\to0\) in \(L^2\). The Dirichlet-mixture representation of the Pólya urn lets one first sample \(P\) from the indicated Dirichlet law and then sample the colors conditionally iid with probabilities \(P\). It follows that \(N_i/n\to P_i\) in \(L^2\). Therefore \((L_1/n,\ldots,L_d/n)\to P/2\) in \(L^2\) in that coupling. The standard Dirichlet covariance and variance formulas, together with bounded second moments, yield both displayed limits. Since at least two root weights are positive, the limiting individual variances are positive, so the correlation limit is well-defined.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and performs exhaustive, **exact-rational** attachment-sequence enumeration for positive integer and fractional root weights in two-root and three-root models, comparing all component-size probabilities, first and mixed second leaf moments, strict negative covariance, and all nontrivial pairwise leaf-tail inequalities to the theorem. It separately verifies the three rational moment recurrences for several weights through time forty. Run with `python verify.py`. The supplied run produced `PASS assertions= 1001  attachment_histories= 14779`. These finite checks are corroboration; the unrestricted claims rest on the four proof steps above.

## Relationship to prior work

Iksanov, Kabluchko, Marynych and Wachtel (2024, arXiv:2403.16448v1) define the multinomial Hoppe forest, derive its Dirichlet-multinomial component sizes in Proposition 2.8, and provide single-component leaf-count laws in Theorems 2.12 and 2.15. These results are used and **not claimed as new**. The present statement concerns negative regression between aggregate leaf counts of distinct components, explicit **mixed** second moments, and the persistent limiting leaf dependence across components; those are not obtained merely by specifying individual marginals. Mahmoud and Smythe (1991) study leaves of rooted subtrees of recursive trees. Its scanned primary text was not usable for a complete comparison, leaving a residual possibility that certain component covariance cases were previously derived.

## Limitations

This result concerns a fixed number of positively weighted initial roots and their sequential unit-weight recursive attachment trees. It does not prove full negative association of all ordinary-vertex terminal indicators, a Gaussian joint fluctuation theorem, or the same conclusions under preferential attachment with nonconstant ordinary-vertex weights. Prior historical work not fully accessible may contain equivalent special cases. The finite enumerations do not certify the theorem for infinite parameter ranges. Independent mathematical assessment has not been performed.

## References

1. A. Iksanov, Z. Kabluchko, A. Marynych, and V. Wachtel, *Multinomial random combinatorial structures and r-versions of Stirling, Eulerian and Lah numbers*, arXiv:2403.16448v1, first posted 2024-03-25, https://arxiv.org/abs/2403.16448 .
2. H. M. Mahmoud and R. T. Smythe, *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, Annals of Applied Probability (1991), DOI:10.1214/aoap/1177005874. Historical relation unresolved due to inaccessible machine-readable primary text.
