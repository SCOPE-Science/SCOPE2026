# Positive crossing-clique–circular-span covariance in uniform chord diagrams

## Finding
For every integer pair \(n\ge r\ge3\), the count \(T_{r,n}\) of sets of \(r\) mutually crossing chords in a uniform circular chord diagram has **strictly positive covariance** with the total shortest circular chord span \(H_n\). In particular, the triangle count in the chord-intersection graph satisfies
\[
\operatorname{Cov}(H_n,T_{3,n})=
\frac{n^3(n-2)(n-1)^2(3n-7)}{60(2n-5)(2n-3)(2n-1)}.
\]
A finite binomial-sum identity gives the exact covariance for every permitted \(r\), not just for triangles.

## Assumptions and scope
Let \(n\ge r\ge3\) be integers. Choose a perfect matching \(M\) uniformly among the \((2n-1)!!\) matchings of \(2n\) cyclically labeled points \(0,1,\ldots,2n-1\). Draw a chord for each pair. Two chords cross if their endpoints alternate around the circle. Write \(T_{r,n}\) for the number of unordered \(r\)-element sets of chords with every two crossing. For each chord \(\{a,b\}\), define \(w(a,b)=\min(|a-b|,2n-|a-b|)\) and \(H_n=\sum_{\{a,b\}\in M}w(a,b)\). This is a combinatorial *endpoint-step* span, not Euclidean chord length. If the chord-length convention counts interior points of the shorter arc, the sum is \(H_n-n\); its covariance with \(T_{r,n}\) is identical.

Put \(D_{n,r}=\prod_{j=1}^{r-1}(2n-2j-1)\) and \((2r-1)!!=1\cdot3\cdots(2r-1)\). Set \(\binom ab=0\) for \(b>a\) or \(b<0\). The exact formula is
\[
\operatorname{Cov}(H_n,T_{r,n})=
\frac{n}{2n-1}\sum_{d=1}^{2n-1}\min(d,2n-d)
\left[\frac{\binom{n-1}{r}-\binom nr}{(2r-1)!!}
+\frac{\binom{d-1}{r-1}\binom{2n-d-1}{r-1}}{D_{n,r}}\right].
\]
This formula and the strict sign claim hold for *all* \(n\ge r\ge3\).

## Proof
**1. A random marked chord.** Mark a uniformly chosen chord of the matching. Its two endpoints form a uniformly chosen unordered pair, hence we may rotate them to positions \(0,d\), where \(d\) is uniform on \(1,\ldots,2n-1\). Let \(s=d-1\) and \(t=2n-d-1\) be the numbers of endpoints in the two open arcs, and \(k=\min(s,t)\). The chord span is \(w=k+1\), and
\[
\mathbb P(k=j)=\frac2{2n-1}\quad(0\le j\le n-2),\qquad
\mathbb P(k=n-1)=\frac1{2n-1}.
\]
By symmetry of the \(n\) chords, for the marked chord \(e\) we have
\(\operatorname{Cov}(H_n,T_{r,n})=n\operatorname{Cov}(w(e),T_{r,n})\).

**2. Conditional clique counts.** An unordered set of \(r\) chords forms a complete crossing family with probability \(1/(2r-1)!!\): of all pairings on its \(2r\) endpoints, exactly one pairs the alternating endpoint blocks to produce all mutual crossings. Thus
\(\mathbb E T_{r,n}=\binom nr/(2r-1)!!\).
Condition on the marked chord's endpoint pair. The remaining matching is uniform. Cliques not containing the marked chord have expectation \(\binom{n-1}{r}/(2r-1)!!\). For a clique containing it, choose \(r-1\) points on each side (\(\binom{s}{r-1}\binom{t}{r-1}\) choices); exactly one pairing of those \(2r-2\) points creates mutually crossing chords that each cross the marked chord. The probability that these \(r-1\) prescribed pairs occur among the remaining chords is \(1/D_{n,r}\). Therefore
\[
\mathbb E[T_{r,n}\mid e=\{0,d\}]
=\frac{\binom{n-1}{r}}{(2r-1)!!}
+\frac{\binom{s}{r-1}\binom{t}{r-1}}{D_{n,r}}.
\]
Inserting this conditional mean and summing over uniform \(d\) yields the exact covariance sum stated above.

**3. Strict positivity.** Define \(g(k)=\binom{k}{r-1}\binom{2n-2-k}{r-1}\), for integer \(0\le k\le n-1\). It vanishes for \(k<r-1\). When \(r-1\le k\le n-2\), with \(t=2n-2-k\),
\[
\frac{g(k+1)}{g(k)}
=\frac{(k+1)(t-r+1)}{(k-r+2)t}>1,
\]
because the numerator minus denominator is \((r-1)(t-k-1)>0\). Therefore \(g\) is nondecreasing and nonconstant on the support of \(k\), and \(w=k+1\) increases strictly. For independent copies \(K,K'\) of the marked chord's shorter-arc count, the covariance identity
\[
2\operatorname{Cov}(K+1,g(K))
=\mathbb E[(K-K')(g(K)-g(K'))]>0
\]
shows
\(\operatorname{Cov}(H_n,T_{r,n})=(n/D_{n,r})\operatorname{Cov}(K+1,g(K))>0\). This proves the infinite family of strict inequalities, including boundary \(n=r\).

**4. Triangle closed form.** At \(r=3\), \(D_{n,3}=(2n-3)(2n-5)\), and an elementary split of the sum at \(d=n\) gives
\[
\sum_{d=1}^{2n-1}\min(d,2n-d)
\binom{d-1}{2}\binom{2n-d-1}{2}
=\frac{n^2(n-2)(n-1)(11n^2-42n+37)}{60}.
\]
Substitution into the exact formula, using \(\mathbb E H_n=n^3/(2n-1)\), reduces to the displayed rational covariance. Its leading order for fixed triangle size is \(n^4/160\).

## Verification
Run `python3 verify_clique.py` with Python 3 and only the standard library. The verifier independently enumerates all perfect matchings for \(n=3,4,5,6\) (respectively 15, 105, 945, and 10,395) and evaluates all crossing clique counts directly. It verifies agreement with the conditional-moment finite sum and triangle closed form using exact fractions; it also checks those formulas and positivity for all \(3\le r\le n\le64\). Enumeration tests finitely many cases; the preceding monotonicity proof establishes all sizes.

## Relationship to prior work
Acan (2015) studies uniformly random chord diagrams, the distribution of a chord's crossing degree, the clique-number problem and other intersection-graph structure. Its primary 2010 MSC classification is 60C05. The present observable is the *joint* statistic between **total shortest endpoint arc span** and **counts of every fixed-size complete-crossing family**, not the single-chord degree or maximum clique size. Acan and Pittel (2014) analyze the distribution of component size and total pairwise crossings in the sparse-crossing regime; their results do not yield this clique/span mixed moment directly. Kasraoui and Zeng (2006) develop distributions of two-edge crossings, nestings and alignments. Their two-edge results do not determine three-or-more-wise crossing-clique counts. The pairwise crossing-count conditional profile is a separate, stronger previously available calculation for \(r=2\); for that reason \(r=2\) is excluded from the claimed novelty.

## Limitations
This is a statement about uniformly paired labeled circle endpoints and the combinatorial shortest-arc length, not arbitrary random geometric chords sampled by another distribution. It does not assert distributional association or positive regression of the two full statistics, only positive covariance. No asymptotic normality, independence, or independent historical-priority certification is claimed. Older higher-order crossing enumeration might contain an equivalent mixed identity; the literature comparison is not a proof of absolute novelty.

## References
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first version 2015-01-07, https://arxiv.org/abs/1501.01489.
- H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867, first version 2014-06-11, https://arxiv.org/abs/1406.2867.
- A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081, first version 2006-01-04, https://arxiv.org/abs/math/0601081.
