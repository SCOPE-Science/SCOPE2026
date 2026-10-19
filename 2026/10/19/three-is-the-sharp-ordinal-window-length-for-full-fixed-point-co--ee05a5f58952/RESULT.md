# Three is the sharp ordinal-window length for full fixed-point covariance rank

## Finding

Let \(\pi\) be uniformly distributed over the permutations of \(\{1,\ldots,n\}\), with \(n\ge2\). Write \(F_j=\mathbf 1\{\pi(j)=j\}\). For \(1\le k\le n\), let \(X_{i,\sigma}\) indicate that the consecutive window \(\pi(i),\ldots,\pi(i+k-1)\) has relative-order pattern \(\sigma\in S_k\), where \(1\le i\le n-k+1\).

The entire cross-covariance matrix \(M_{n,k}=(\operatorname{Cov}(X_{i,\sigma},F_j))_{(i,\sigma),j}\), with \((n-k+1)k!\) rows and \(n\) columns, has the exact entries
\[
\boxed{\operatorname{Cov}(X_{i,\sigma},F_j)=
\begin{cases}
\dfrac{1}{n}\left[\dfrac{\binom{j-1}{\sigma(j-i+1)-1}\binom{n-j}{k-\sigma(j-i+1)}}{(n-1)_{\underline{k-1}}}-\dfrac1{k!}\right],& i\le j<i+k,\\[9pt]
0,&j\notin\{i,\ldots,i+k-1\}.
\end{cases}}
\]
Here \((z)_{\underline r}=z(z-1)\cdots(z-r+1)\) with \((z)_{\underline0}=1\), and the binomial coefficient is zero if its lower index is outside the permitted range. This formula applies for every stated \(n,k,i,\sigma,j\), including \(k=1\).

The exact rank classification is
\[
\boxed{\operatorname{rank}M_{n,k}=
\begin{cases}
0,&k=1,\\
n-1,&k=2,\\
n,&3\le k\le n.
\end{cases}}
\]
Thus a complete array of consecutive two-position order comparisons leaves one linear fixed-point direction invisible in covariance, whereas three-position order patterns already detect every nonzero linear combination of the fixed-point indicators. More precisely, for \(k\ge3\), if \(\operatorname{Cov}(X_{i,\sigma},\sum_j a_jF_j)=0\) for every \(i,\sigma\), then all \(a_j=0\). This *linear covariance detection* does not mean samplewise recovery or probabilistic independence.

## Assumptions and scope

The distribution is uniform on the full symmetric group, and all indices and values use the same labels \(1,\ldots,n\). The pattern \(\sigma(t)\) is the rank (starting at one) of the entry in relative window position \(t\). Both the window start and the fixed-point position are retained. No asymptotic limit is taken. The rank is over the real numbers (equivalently, the rationals).

The \(k=2\) covariance entries coincide with the earlier position-resolved fixed-point/descent result and are included to identify the sharp minimal window. The new structural assertion is the all-length kernel together with full column rank as soon as \(k=3\).

## Proof

**1. Exact local covariance.** Each specified length-\(k\) relative order pattern has probability \(1/k!\), and \(\Pr(F_j=1)=1/n\). If position \(j\) lies outside the window, conditioning on \(\pi(j)=j\) leaves the ordering of the window's \(k\) distinct entries uniform, so its conditional pattern probability remains \(1/k!\), proving zero covariance.

Suppose \(j=i+t-1\) and \(r=\sigma(t)\). Conditional on \(F_j=1\), all injections of the remaining \(k-1\) window positions into \(\{1,\ldots,n\}\setminus\{j\}\) are equally likely. For pattern \(\sigma\) there must be exactly \(r-1\) smaller and \(k-r\) larger values among these positions. Choose the smaller set in \(\binom{j-1}{r-1}\) ways and the larger set in \(\binom{n-j}{k-r}\) ways. Once these sets are chosen, the strict ordering prescribed by \(\sigma\) determines a *unique* assignment of the remaining values to the window positions. Consequently,
\[
\Pr(X_{i,\sigma}=1\mid F_j=1)
=\frac{\binom{j-1}{r-1}\binom{n-j}{k-r}}{(n-1)_{\underline{k-1}}}.
\]
Multiplying the difference from \(1/k!\) by \(1/n\) proves the stated formula. The absence of extra factorial factors in its numerator is essential: a fixed pattern specifies a unique order of each chosen set.

**2. Rank at length one and two.** For \(k=1\), every pattern indicator is identically one, so the matrix is zero. For \(k=2\), the two patterns are complements, and the rows for ordinary descent at position \(i\) have only two potentially nonzero entries,
\[
M_{n,2}^{\mathrm{des}}(i,i)=\frac{2i-n-1}{2n(n-1)},\qquad
M_{n,2}^{\mathrm{des}}(i,i+1)=\frac{n-2i-1}{2n(n-1)}.
\]
These \(n-1\) rows are linearly independent. Indeed, in a linear dependence, the first column forces the coefficient of row one to vanish, and subsequent columns force all coefficients to the left of the sole possible zero of \(2i-n-1\) to vanish. The last column similarly forces the last-row coefficient to vanish, and backward propagation forces all coefficients to the right of the sole possible zero of \(n-2i-1\) to vanish. For even \(n\) neither entry vanishes; for odd \(n\) the two possible zeros occur at consecutive row indices \((n+1)/2\) and \((n-1)/2\), so the two propagations cover every row. Hence the rank is \(n-1\), also for \(n=2\).

**3. A three-position window has full local rank.** Fix \(n\ge3\), and fix three consecutive positions \(j,j+1,j+2\), with \(1\le j\le n-2\). Restrict the six covariance rows for its six relative-order patterns to these three fixed-point columns. Multiplication by the nonzero common factor \(n(n-1)(n-2)\) does not change rank. Define
\[
\phi_h(r)=\frac{\binom{h-1}{r-1}\binom{n-h}{3-r}}{(n-1)(n-2)}-\frac16,
\qquad r\in\{1,2,3\}.
\]
Let \(a,b,c\) be coefficients annihilating the six pattern rows. Subtract the equations for patterns \(123\) and \(213\) and then for patterns \(231\) and \(321\). The third relative position has the same rank in each comparison. Hence
\[
a\,[\phi_j(1)-\phi_j(2)]=b\,[\phi_{j+1}(1)-\phi_{j+1}(2)],
\]
\[
a\,[\phi_j(2)-\phi_j(3)]=b\,[\phi_{j+1}(2)-\phi_{j+1}(3)].
\]
Writing \(D=(n-1)(n-2)\), the two rank-difference components satisfy
\[
2D\,(\phi_h(1)-\phi_h(2))=(n-h)(n-3h+1),
\]
\[
2D\,(\phi_h(2)-\phi_h(3))=(h-1)(2n-3h+2).
\]
The determinant of the corresponding two-component vectors at \(h=j\) and \(h=j+1\) equals
\[
2(n-2)\bigl(3j^2-3jn+n^2-1\bigr).
\]
It is strictly positive, because the bracket equals \(3(j-n/2)^2+n^2/4-1>0\) for \(n\ge3\). Therefore \(a=b=0\). At least one of \(\phi_{j+2}(1),\phi_{j+2}(2),\phi_{j+2}(3)\) is nonzero: otherwise its two displayed rank differences would both vanish, which is impossible at an interior index, and at the endpoints one component is explicitly nonzero. The six equations then imply \(c=0\). Thus the local six-by-three block has rank three.

**4. Global rank at length three.** If an \(n\)-vector is annihilated by every covariance row of \(M_{n,3}\), then Step 3 forces its restriction to every triple of consecutive coordinates to be zero. These triples cover all \(n\) coordinates, so the vector vanishes. Therefore \(\operatorname{rank}M_{n,3}=n\).

**5. All longer windows.** For any \(k\ge3\), every triple of consecutive positions can be included in at least one length-\(k\) consecutive window. Within that window, the indicator of any prescribed three-position relative-order pattern is the sum of the indicators of precisely those \(k\)-patterns that restrict to the chosen three-pattern. Covariance is linear, so every row of \(M_{n,3}\) belongs to the row span of \(M_{n,k}\). The latter consequently has rank at least \(n\) and at most \(n\), giving exact rank \(n\). This completes the proof.

## Verification

Run `python verify_patterns.py` with Python 3. The standard-library-only checker enumerates every permutation of sizes \(2\) through \(8\) and tests all \(482,297\) position/pattern/fixed-point covariance cells against the combinatorial formula using exact rational arithmetic. It separately performs \(41\) exact rank calculations for sizes up to \(12\), and \(124,251\) integer determinant comparisons for \(3\le n\le500\). All passed in the recorded execution. The unbounded theorem is established by Steps 1–5, not by this finite enumeration.

## Relationship to prior work

Diaconis, Evans, and Graham (2013) study unseparated consecutive-value pairs and the random fixed-point set in a uniform permutation, including a full distributional equivalence for those different observables. That theorem does not describe ordinal patterns jointly with labeled fixed-point indicators.

Désarménien and Wachs (1993) refine descent-set enumeration by the *number* of fixed points. Their Theorem 5.1 and Section 6 do not retain the fixed-point position, and hence do not imply the present position-by-pattern matrix or its sharp rank change. Eriksen, Freij, and Wästlund (2008) similarly study derangement restrictions and descent classes. Janson, Nakamura, and Zeilberger (2013) analyze counts of (not necessarily consecutive) permutation patterns and their joint asymptotic laws; the displayed covariance with positional fixed points is not one of their observables.

The closest directly comparable published calculation, “Boundary localization of fixed-point–descent dependence in a uniform permutation” (public note, 2026), already gives the \(k=2\) coordinate law. It does not yield the \(k\ge3\) rank theorem merely by linear recombination: a length-three pattern involves the *joint* outcomes of two adjacent comparisons, whereas the earlier result records only their separate first-order covariances. The \(k=2\) part here is included solely to locate the sharp boundary, not claimed as new.

## Limitations

Full column rank is a second-moment, linear-algebraic property, not an ability to recover fixed points from one observed window-pattern vector or a statement of independence. The result requires a uniform permutation. It does not determine higher-order joint distributions, sampling errors, or quantitative conditioning of the full-rank matrices. Earlier refined pattern enumerations could contain an implicit equivalent of the rank classification; the available comparisons do not independently certify first priority.

## References

1. P. Diaconis, S. N. Evans, and R. Graham, “Unseparated pairs and fixed points in random permutations,” Berkeley Statistics Technical Report 822, dated 2013-08-01; arXiv:1308.5459, first submitted 2013-08-25. Primary MSC 60C05.
2. J. Désarménien and M. L. Wachs, “Descent Classes of Permutations with a Given Number of Fixed Points,” *Journal of Combinatorial Theory, Series A* 64 (1993), 311–328, DOI: 10.1016/0097-3165(93)90100-M.
3. N. Eriksen, R. Freij, and J. Wästlund, “Enumeration of derangements with descents in prescribed positions,” arXiv:0811.1925 (2008), *Electronic Journal of Combinatorics* 16 (2009), R32.
4. S. Janson, B. Nakamura, and D. Zeilberger, “On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns,” arXiv:1312.3955 (2013).
5. “Boundary localization of fixed-point–descent dependence in a uniform permutation,” public mathematical note, 2026-10-04, record identifier 6e228e1e9495.
