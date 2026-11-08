# A factor-\(n\) crossing–nesting contrast for the total circular span of random chords

## Finding

For every integer \(n\ge2\), choose a perfect matching of the cyclically ordered set \(\{1,\ldots,2n\}\) uniformly. Let \(S_n\) be the sum, over all matched edges, of the number of vertices in the shorter of the two open circular arcs cut out by the edge. Let \(X_n\) and \(N_n\) be the numbers of unordered pairs of matched edges that respectively cross and nest in the *fixed linear order* \(1<\cdots<2n\) (for nesting, \(a<c<d<b\)). Then

\[
\operatorname{Cov}(S_n,X_n)=\frac{n^3(n-1)^2}{6(2n-3)(2n-1)},\qquad
\operatorname{Cov}(S_n,N_n)=-\frac{n^2(n-1)^2}{6(2n-3)(2n-1)}.
\]

In particular \(\operatorname{Cov}(S_n,X_n)=-n\operatorname{Cov}(S_n,N_n)\) although \(X_n\) and \(N_n\) have **identical marginal laws**. More sharply,

\[
\lim_{n\to\infty}\operatorname{Corr}(S_n,X_n)=\frac{\sqrt{15}}4,
\qquad
\lim_{n\to\infty}n\operatorname{Corr}(S_n,N_n)=-\frac{\sqrt{15}}4.
\]

The new contribution is the nesting–span relationship and the resulting asymmetric comparison; the crossing–span covariance separately follows from existing marked-chord crossing regressions.

## Assumptions and scope

All \((2n-1)!!\) perfect matchings of the labeled \(2n\) endpoints are equiprobable. For an edge \(e=(i,j)\) with \(i<j\), set
\[
\ell(e)=\min\{j-i-1,\,2n-j+i-1\},\qquad S_n=\sum_{e\in M}\ell(e).
\]
Crossing pairs have endpoint pattern \(a<c<b<d\); nested pairs have endpoint pattern \(a<c<d<b\), where \((a,b)\) and \((c,d)\) are matched edges. This nesting convention uses the specified linear cut; the circular span itself does not depend on that cut. All covariance and correlation statements are for \(n\ge2\), when the relevant variances are positive.

## Proof

**1. Edge conditioning.** Let \(e=(i,j)\) be a prescribed edge. The probability that \(e\in M\) is \(1/(2n-1)\). Conditionally on its presence, the other \(n-1\) edges are uniformly matched. Consequently their internal expected crossing and nesting counts are both \((n-1)(n-2)/6\). For the pairs containing \(e\), set \(d=j-i\). Each prescribed second edge on the remaining endpoints occurs with conditional probability \(1/(2n-3)\). There are \((d-1)(2n-d-1)\) crossing possibilities. A nesting with \(e\) outer has both endpoints in \((i,j)\), giving \(\binom{d-1}{2}\) possibilities; a nesting with \(e\) inner joins a point before \(i\) to a point after \(j\), giving \((i-1)(2n-j)\) possibilities. Thus
\[
\begin{aligned}
\mathbb E[X_n\mid e\in M]&=\frac{(n-1)(n-2)}6+\frac{(d-1)(2n-d-1)}{2n-3},\\
\mathbb E[N_n\mid e\in M]&=\frac{(n-1)(n-2)}6+
 \frac{\binom{d-1}{2}+(i-1)(2n-j)}{2n-3}.
\end{aligned}
\]
Both unconditional expectations are \(n(n-1)/6\). By expanding the weighted sum \(S_n\) over candidate edges and using conditional expectation, the mixed covariances are determined by the three deterministic sums \(W,U_X,U_N\) below.

**2. Exact finite sums.** Write \(L_d=\min\{d-1,2n-d-1\}\). Elementary arithmetic-progression sums, split at \(d=n\), give
\[
\begin{aligned}
W&=\sum_{1\le i<j\le2n}\ell(i,j)
 =\sum_{d=1}^{2n-1}(2n-d)L_d=n(n-1)^2,\\
U_X&=\sum_{i<j}\ell(i,j)(j-i-1)(2n-j+i-1)
 =\frac{n(n-1)^2(5n^2-10n+6)}6,\\
U_N&=\sum_{i<j}\ell(i,j)\left[\binom{j-i-1}{2}+(i-1)(2n-j)\right]
 =\frac{n(n-2)(n-1)^2(4n-3)}6.
\end{aligned}
\]
For reproducibility, the last sum reduces to the one-variable sum
\[
\sum_{d=1}^{2n-1}L_d\left[(2n-d)\binom{d-1}{2}+\binom{2n-d}{3}\right],
\]
since \(\sum_{i=1}^{2n-d}(i-1)(2n-d-i)=\binom{2n-d}{3}\). The corresponding sum for \(U_X\) has summand \((2n-d)L_d(d-1)(2n-d-1)\). Each displayed equality follows by substituting \(L_d=d-1\) for \(d\le n\), and \(L_d=2n-d-1\) for \(d>n\), and summing polynomials. As \(\mathbb E S_n=W/(2n-1)\), the conditional identities give
\[
\operatorname{Cov}(S_n,T_n)=
\frac{U_T}{(2n-1)(2n-3)}
-\frac{(n-1)W}{3(2n-1)},\qquad T\in\{X,N\}.
\]
Substitution yields exactly the two claimed covariances. This proves their signs and the factor-\(n\) contrast for **all** \(n\ge2\), independently of asymptotics.

**3. Variances and correlations.** The mean and variance of total span are
\[
\mathbb E S_n=\frac{n(n-1)^2}{2n-1},\qquad
\operatorname{Var}(S_n)=\frac{2n^2(n-1)^2(n^2-n+1)}{3(2n-3)(2n-1)^2}.
\]
To see the variance, the deterministic sum of span weights of all candidate edges incident to any fixed endpoint is \(R=(n-1)^2\). The sum of squared weights over all candidate edges is
\(W_2=n(n-1)(2n^2-4n+3)/3\). Two distinct prescribed disjoint edges co-occur with probability \(1/[(2n-1)(2n-3)]\), and two edges sharing an endpoint cannot co-occur. Therefore
\[
\mathbb E S_n^2=\frac{W_2}{2n-1}
+\frac{W^2+W_2-2nR^2}{(2n-1)(2n-3)},
\]
which gives the stated variance after subtracting the squared mean.

The classical crossing-pair variance is
\[
\operatorname{Var}(X_n)=\frac{n(n-1)(n+3)}{45}.
\]
For completeness, it can be reconstructed by expressing \(X_n\) as a sum of crossing indicators over four-subsets of endpoints. For \(n\ge4\), the total numbers of **ordered** compatible distinct indicator pairs supported on six and eight specified endpoints are respectively \(12\) and \(70\). Thus
\[
\mathbb E[X_n(X_n-1)]=
\frac{12\binom{2n}{6}}{(2n-1)(2n-3)(2n-5)}+
\frac{70\binom{2n}{8}}{(2n-1)(2n-3)(2n-5)(2n-7)}.
\]
Together with \(\mathbb E X_n=n(n-1)/6\), this simplifies to the displayed variance. The cases \(n=2,3\) are direct. The classical crossing–nesting involution of Kasraoui–Zeng exchanges the **counts of crossing and nesting pairs**, showing \(\operatorname{Var}(N_n)=\operatorname{Var}(X_n)\). Divide the covariances by these positive standard deviations. The exact ratio of correlations is \(-n\); inserting the variance formulas and retaining leading powers yields the two limits in the finding.

## Verification

The accompanying standalone `verify.py` performs independent exhaustive enumeration of every matching for \(2\le n\le7\), comparing exact rational means, variances and both covariances against the theorem, and separately evaluates the deterministic conditional-edge and second-moment sums for all \(2\le n\le200\). There are 850 exact assertions in the verifier; its completed output is recorded in `VERIFICATION.md`. The executable checks are finite corroboration; the all-size assertion follows from the displayed conditional-expectation and polynomial-summation argument, not from enumeration.

## Relationship to prior work

Acan (2015, preprint v1) defines precisely the same circular chord length and analyzes crossing-degree distributions conditional on this length. A marked-chord crossing regression already yields the positive crossing–span covariance by aggregation; it is **not separately asserted as novel**. Kasraoui and Zeng (2006) give a type-preserving involution exchanging crossing and nesting **pair counts**, and their theorem supplies marginal equidistribution. That involution does not preserve the nonlinear *shorter-circular-arc* sum \(S_n\); in particular marginal symmetry alone cannot imply the new negative nesting–span covariance or the exact factor-\(n\) contrast. Paguyo (2021) gives later limit-theorem context for crossings. Acan's earlier accessible dissertation (2013), chapter 3, gives degree and conditional-length calculations rather than this mixed nesting statistic. The formulas use classical counting, but the conditional inner/outer nesting balance and its asymptotic disparity are additional information.

## Limitations

The nesting statistic is based on the chosen linear cut through the circle, unlike the circular span. Changing the cut changes individual nesting counts, though cyclic averaging of the uniform ensemble leaves the theorem unaffected. The finding is an exact second-moment comparison, not a joint limit theorem or stochastic ordering. Earlier general multivariate generating functions or unpublished weighted enumerations might imply the result implicitly; historical priority beyond the inspected literature is not guaranteed. No independent audit has been performed.

## References

- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 7 January 2015, https://arxiv.org/abs/1501.01489.
- A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081v1, 4 January 2006, https://arxiv.org/abs/math/0601081; Electron. J. Combin. 13 (2006), R33.
- H. Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, Ohio State University dissertation (2013), https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1373310487&disposition=inline.
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, 2 April 2021, https://arxiv.org/abs/2104.01134.
