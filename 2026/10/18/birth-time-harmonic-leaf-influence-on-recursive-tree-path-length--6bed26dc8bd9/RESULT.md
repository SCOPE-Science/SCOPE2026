# Birth-time harmonic leaf influence on recursive-tree path length

## Finding
For each integer \(n\ge2\), grow a uniform random recursive tree by attaching each vertex \(t=2,\ldots,n\) independently to a uniform parent in \(\{1,\ldots,t-1\}\). Let \(D_t\) be the distance of vertex \(t\) from root \(1\), let \(P_n=\sum_{t=1}^{n}D_t\) be total path length, and let \(I_{n,j}\) indicate that vertex \(j\) has no children in the completed tree. Let \(L_n=\sum_{j=2}^n I_{n,j}\) be the number of leaves and \(H_k=\sum_{s=1}^k 1/s\), with \(H_0=0\).

**Theorem (birth-time leaf influence).** For every \(n\ge2\) and \(2\le j\le n\),
\[
\Pr(I_{n,j}=1)=\frac{j-1}{n-1},\qquad
\mathbb E[P_n\mid I_{n,j}=1]-\mathbb EP_n=H_{j-1}-H_{n-1},
\]
\[
\operatorname{Cov}(P_n,I_{n,j})
=\frac{j-1}{n-1}(H_{j-1}-H_{n-1}).
\]
It follows, without an asymptotic approximation, that
\[
\operatorname{Cov}(P_n,L_n)=-\frac{n-2}{4}.
\]
For \(n\ge3\), every label \(2\le j<n\) has strictly negative individual covariance; the last vertex is deterministically a leaf and has zero covariance. For \(n\ge4\), the finite profile is strictly discretely convex when plotted against \(j-1\). For any sequence \(j_n/n\to u\in(0,1]\), its covariance converges to \(u\log u\) (with \(1\log1=0\)); the minimum over birth labels tends to \(-1/e\), attained at labels satisfying \(j_n/n\to e^{-1}\). For \(n=2\), all covariances vanish.

Using established marginal-variance limits, the finite negative covariance gives
\[
\operatorname{Corr}(P_n,L_n)
\sim-\frac{\sqrt3}{2\sqrt{2-\pi^2/6}}\,n^{-1/2}.
\]
This correlation conclusion is restricted to \(n\to\infty\), with \(n\ge3\) so the leaf-count variance is positive.

## Assumptions and scope
All results concern *uniform* increasing recursive trees on fixed birth labels, not arbitrary unlabeled rooted trees, degree-proportional attachment, or an independent leaf process. A leaf means outdegree zero; when \(n\ge2\), root \(1\) is not a leaf. There is no randomness in the birth labels. The conditional expectations are defined because every event \(I_{n,j}=1\) has positive probability. The covariance is ordinary centered covariance under the joint law of all parent selections.

## Proof
Write \(A_t\) for the parent of vertex \(t\). The variables \(A_t\), for \(2\le t\le n\), are independent and \(A_t\) is uniform on \(\{1,\ldots,t-1\}\). For fixed \(j\ge2\), the leaf event is the intersection \(A_t\ne j\) over \(j<t\le n\). Its probability telescopes:
\[
\Pr(I_{n,j}=1)=\prod_{t=j+1}^{n}\frac{t-2}{t-1}
=\frac{j-1}{n-1}.
\]
The empty product when \(j=n\) is one. Crucially, conditional on this event, the pre-\(j\) tree is unchanged, while the later parent variables remain mutually independent, each uniform among the \(t-2\) earlier vertices other than \(j\).

The elementary recursive-depth expectation is \(\mathbb E D_t=H_{t-1}\), obtained from \(D_t=1+D_{A_t}\) by induction, and therefore
\[
\mathbb EP_t=t(H_t-1)=tH_{t-1}-(t-1).
\]
Write \(m_t=\mathbb E[P_t\mid I_{n,j}=1]\) for \(t\ge j\) and \(a=\mathbb E[D_j\mid I_{n,j}=1]=H_{j-1}\). Since \(D_j\) depends only on earlier parent variables, this conditioning does not change its mean. For \(t>j\), conditional independence of \(A_t\) gives the exact recurrence
\[
 m_t=\frac{t-1}{t-2}m_{t-1}+1-\frac{a}{t-2}.
\]
Dividing by \(t-1\) and telescoping from \(j+1\) to \(n\), using \(m_j=jH_{j-1}-(j-1)\) and
\[
\sum_{t=j+1}^{n}\frac1{(t-1)(t-2)}
=\frac1{j-1}-\frac1{n-1},
\]
gives
\[
 m_n=(n-1)(H_{n-1}-1)+H_{j-1}
=\mathbb EP_n+H_{j-1}-H_{n-1}.
\]
This also covers \(j=n\), where the recurrence has no steps. Multiplying the conditional mean shift by the event probability proves the individual covariance formula.

Summing it over all leaf indicators and reversing a finite sum gives the exact global identity:
\[
\begin{aligned}
\operatorname{Cov}(P_n,L_n)
&=-\frac1{n-1}\sum_{k=1}^{n-1}k\sum_{t=k+1}^{n-1}\frac1t\\
&=-\frac1{2(n-1)}\sum_{t=2}^{n-1}(t-1)
=-\frac{n-2}{4}.
\end{aligned}
\]
Define \(w_k=k(H_k-H_{n-1})/(n-1)\) for \(1\le k\le n-1\). Its adjacent difference equals
\[
 w_{k+1}-w_k=\frac{1+H_k-H_{n-1}}{n-1},
\]
and successive adjacent differences increase strictly because \(H_{k+1}>H_k\). Thus the profile is discretely strictly convex. For \(k/(n-1)\to u\in(0,1]\), harmonic-sum comparison with the logarithm gives \(w_k\to u\log u\). The same bound at \(u=0\), since \(x|\log x|\to0\), controls endpoint subsequences; the finite minimizing fraction therefore tends to the unique minimizer \(e^{-1}\) of \(u\log u\) on \([0,1]\), and its covariance tends to \(-1/e\).

The variance \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\) is the classical Eulerian leaf-count variance. The established path-length result \(\operatorname{Var}(P_n)/n^2\to 2-\pi^2/6>0\) then gives the displayed correlation asymptotic by division. These marginal-variance statements are not claimed as new.

## Verification
The included standalone `verify.py` requires only Python's standard library. It exhaustively enumerates all \((n-1)!\) recursive trees for each \(2\le n\le9\), computes total depths, leaf counts and every label-specific leaf indicator, and verifies the stated exact probabilities, conditional shifts, and covariance identities with rational arithmetic. It also checks strict discrete convexity for \(3\le n<500\) and numerically probes the position of the minimum at larger sizes. Executed locally, it passed 640 assertions. Exact finite enumeration checks consistency only; the proof above handles every \(n\) and \(j\).

## Relationship to prior work
Dobrow and Fill's *Total Path Length for Random Recursive Trees* establishes path-length mean, limit, and variance information; its accessible full manuscript was checked for leaf-specific results, with no occurrence of a leaf-statistic treatment found. Zhang's *On the number of leaves in a random recursive tree* establishes marginal leaf-count asymptotics, but its full text was not accessible during this comparison. Janson treats asymptotic degree profiles in recursive trees. Lundblad and Wagner (2026) give a multivariate generating-function framework for total path length, external path length and the total number of leaves. Their unlabeled aggregate framework could in principle produce the aggregate covariance by further differentiation, but does not track the birth label and does not present the stated conditional harmonic influence profile. The label-resolved conditional theorem and its age localization, rather than the separate known marginals, are the proposed addition.

## Limitations
The result is an exact first/second-moment and conditional-mean statement, not a stochastic domination or joint central limit theorem. The profile concerns zero outdegree at a *specified* birth label and does not claim analogous formulas for other attachment rules. An earlier exact but differently indexed generating-function computation might imply the aggregate covariance; the broader priority of the label-resolved statement is not independently certified. Complete inspection of some pertinent historical source texts remains an access limitation.

## References
1. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333. DOI: 10.1017/S0963548399003855. Accessible text: https://paperzz.com/doc/6944038/total-path-length-for-random-recursive-trees
2. Y. Zhang, *On the number of leaves in a random recursive tree*, Brazilian Journal of Probability and Statistics 29 (2015), 897–908. DOI: 10.1214/14-BJPS252.
3. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83. DOI: 10.1002/rsa.20046.
4. J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, LIPIcs 381, Article 2 (2026). DOI: 10.4230/LIPIcs.AofA.2026.2. https://drops.dagstuhl.de/storage/00lipics/lipics-vol381-aofa2026/LIPIcs.AofA.2026.2/LIPIcs.AofA.2026.2.pdf
