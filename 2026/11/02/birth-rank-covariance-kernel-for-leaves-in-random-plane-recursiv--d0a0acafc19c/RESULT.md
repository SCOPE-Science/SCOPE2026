# Birth-rank covariance kernel for leaves in random plane recursive trees

## Finding

Let a plane-oriented recursive tree be chosen uniformly from the rooted, ordered, increasing trees with root label \(0\) and nonroot birth labels \(1,\ldots,n\), for any integer \(n\ge1\). Write \(I_{n,i}\) for the indicator that birth-label \(i\) is a leaf at final time \(n\), and set
\[
A_n(s)=\sum_{i=1}^{\lfloor ns\rfloor}I_{n,i},\qquad 0\le s\le1.
\]

For every nonempty subset \(S\subseteq\{1,\ldots,n\}\), the complete leaf-survival probability is
\[
\Pr\{I_{n,i}=1\text{ for all }i\in S\}
=\prod_{t=2}^{n}\left(1-\frac{|S\cap\{1,\ldots,t-1\}|}{2t-1}\right).
\tag{1}
\]
(The empty product is \(1\).) In particular, put
\[
p_{n,i}=\prod_{t=i+1}^{n}\frac{2t-2}{2t-1},\quad
R_{n,j}=\prod_{k=j}^{n-1}\left(1-\frac1{4k^2}\right).
\]
Then, for all \(1\le i<j\le n\),
\[
\Pr(I_{n,i}=1)=p_{n,i},\qquad
\operatorname{Cov}(I_{n,i},I_{n,j})
=p_{n,i}p_{n,j}(R_{n,j}-1).
\tag{2}
\]
The relative covariance is independent of the older birth label \(i\). It is negative for \(j<n\), while \(I_{n,n}=1\) deterministically.

The finite-size covariance profile has a closed scaling limit. For \(0<x<y<1\), any integer sequences with \(i/n\to x\), \(j/n\to y\) satisfy
\[
n\operatorname{Cov}(I_{n,i},I_{n,j})
\longrightarrow -\frac{1-y}{4}\sqrt{\frac{x}{y}}.
\tag{3}
\]
For every fixed \(0\le s\le t\le1\),
\[
\lim_{n\to\infty}\frac{\mathbb E A_n(s)}{n}
=\frac23s^{3/2},\qquad
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(A_n(s),A_n(t))}{n}
=K(s,t)=\frac{s^{3/2}}9(6-3\sqrt t+t^{3/2})-\frac{s^2}{3}.}
\tag{4}
\]
For the reversed order, use symmetry \(K(s,t)=K(t,s)\). The special case \(K(1,1)=1/9\) agrees with the established total-leaf variance asymptotic.

More generally, for bounded Riemann-integrable weights \(f,g:[0,1]\to\mathbb R\), define \(Z_n(f)=\sum_{i=1}^n f(i/n)I_{n,i}\). Then
\[
\begin{aligned}
\lim_{n\to\infty}\frac{\operatorname{Cov}(Z_n(f),Z_n(g))}{n}
={}&\int_0^1f(x)g(x)(\sqrt x-x)\,dx\\
&-\frac14\int_0^1\!\int_0^1 f(x)g(y)(1-\max\{x,y\})
\sqrt{\frac{\min\{x,y\}}{\max\{x,y\}}}\,dx\,dy.
\end{aligned}
\tag{5}
\]
At \(x=y=0\), the integrand of the double integral may be defined arbitrarily, since that point has measure zero. Equation (4) is the case of prefix-indicator weights.

## Assumptions and scope

The tree evolves from a single root. At insertion step \(t\), vertex \(t\) is attached in one of the \(2t-1\) ordered insertion slots, independently uniformly conditional on the current tree. Every completed ordered increasing tree is therefore equally likely. In the equivalent Stirling-permutation representation, inserting vertex \(t\) inserts the adjacent pair \(tt\) in one of \(2t-1\) gaps. A nonroot vertex is a leaf exactly when its two appearances remain adjacent in the final permutation. All limits are as integer \(n\to\infty\); the coordinates \(s,t,x,y\) are deterministic and are not random.

## Proof

**Joint survival.** The newborn pair \(ii\) is adjacent at birth. If a set \(S\) of its members all remain plateaux immediately before insertion \(t\), they correspond to \(|S\cap\{1,\ldots,t-1\}|\) different forbidden gaps, one per surviving pair. There are exactly \(2t-1\) uniformly chosen gaps. A pair once separated can never become adjacent again, since later insertions do not delete letters. Thus multiplying the conditional survival probabilities over insertions gives (1), with no independence assumption between leaf indicators.

**Pair covariance.** Formula (1) for singleton \(\{i\}\) gives \(p_{n,i}\). For \(i<j\), comparing joint survival with the product of marginal survival probabilities cancels the factors through insertion \(j\). At each later insertion \(t\), the remaining ratio is
\[
\frac{1-2/(2t-1)}{(1-1/(2t-1))^2}
=1-\frac1{4(t-1)^2}.
\]
Multiplication over \(t=j+1,\ldots,n\) proves (2), including the endpoint \(j=n\).

**Pointwise age limit.** Since \(\log(1-u)=-u+O(u^2)\) as \(u\to0\), uniformly for \(i/n\) in a compact subinterval of \((0,1]\),
\[
\log p_{n,i}=-\frac12\log(n/i)+o(1),\qquad
n\log R_{n,j}\to-\frac14(1/y-1)
\quad\text{when }j/n\to y>0.
\]
Therefore \(p_{n,i}\to\sqrt x\), \(p_{n,j}\to\sqrt y\), and
\(n(R_{n,j}-1)\to-(1-y)/(4y)\). Inserting these limits into (2) gives (3).

**Control at the lower boundary.** Factorwise,
\[
\frac{2t-2}{2t-1}\le\sqrt{\frac{t-1}{t}},\qquad
p_{n,i}\le\sqrt{i/n}.
\]
For \(2\le j\le n\),
\[
0\le1-R_{n,j}\le\sum_{k=j}^{n-1}\frac1{4k^2}
\le\frac1{4(j-1)}.
\]
Thus \(n|\operatorname{Cov}(I_{n,i},I_{n,j})|\le1/2\) for all \(i<j\). These uniform bounds, plus convergence away from the coordinate axes, justify dominated Riemann-sum limits for all the stated finite-dimensional covariance expressions. Since a Bernoulli indicator has variance \(p_{n,i}(1-p_{n,i})\), its diagonal contribution converges to \(\sqrt x-x\).

**Integration.** For \(0<x<y<1\), put \(k(x,y)=-(1-y)\sqrt{x/y}/4\) and extend symmetrically. For \(0\le s\le t\le1\), the covariance of the two prefix sums, normalized by \(n\), tends to
\[
\int_0^s(\sqrt x-x)\,dx
+2\int_0^s\int_x^s k(x,y)\,dy\,dx
+\int_0^s\int_s^t k(x,y)\,dy\,dx.
\]
Direct elementary integration equals the displayed \(K(s,t)\) in (4). The same diagonal/off-diagonal decomposition with bounded Riemann-integrable test functions gives (5), because the integrands are bounded and the discontinuity sets have measure zero.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently enumerates both all Stirling permutations and all parent arrays weighted by their numbers of plane child orderings for \(n\le7\). It checks their complete leaf-mask distributions; every subset joint-survival probability; every single and pairwise covariance; and the established total leaf mean and variance. It also checks exact product identities and the known leaf variance formula for integer \(n\) through \(40\). Run `python verify.py` in the directory containing this document and the script. Finite enumeration and symbolic rational equality are sanity checks; the preceding proof supplies the all-size justification.

## Relationship to prior work

Janson (2008), following Mahmoud, Smythe and Szymański, establishes the ordered-recursive-tree/Stirling-permutation bijection and exact total leaf moments, including variance \(2(n^2-1)/(9(2n-1))\). Kuba and Panholzer (2005 manuscript/2007 publication) and Zhang (2017 preprint) investigate degrees of individually labeled vertices; Zhang's fixed-label zero-child probability covers the singleton factor of (2). These single-label and aggregate results do not alone supply a two-label covariance or covariance kernel for birth-age cohorts.

Haglund and Visontai (2011 preprint, Theorem 3.3) prove stability of the multiaffine, value-indexed ascent/descent/plateau enumerator of Stirling permutations. Specializing non-plateau variables to \(1\) yields a stable multiaffine generating polynomial for the leaf-label indicators, hence strong Rayleigh negative-dependence consequences. **No general negative-association or pairwise-covariance-sign theorem is claimed as new here.** The asserted quantitative refinement is the exact joint survival factorization, the age-resolved covariance multiplier, and especially the closed limiting cumulative/weighted birth-age covariance kernel. These formulas were not located in the examined primary sources.

## Limitations

The covariance kernel is not a functional central limit theorem and makes no claim of Gaussian process convergence, whole-distribution stochastic ordering, or independence of age strata. The proof concerns uniform *ordered increasing* recursive trees, not uniform-parent recursive trees or unlabelled Catalan plane trees. Historical priority is not guaranteed: other general multivariate stable-polynomial or preferential-attachment treatments may imply the exact quantitative formula implicitly. A 1993 study of leaves in tree branches was identified but its full text was not accessible in this check; branch-age versus birth-age coverage remains a residual literature risk. The result has undergone self-review only, not independent validation.

## References

- Svante Janson, *Plane Recursive Trees, Stirling Permutations and an Urn Model*, arXiv:0803.1129, first arXiv public version 7 March 2008. https://arxiv.org/abs/0803.1129
- J. Haglund and Mirkó Visontai, *Stable Multivariate Eulerian Polynomials and Generalized Stirling Permutations*, preprint dated 5 October 2011, especially Section 3.1 and Theorem 3.3. https://www2.math.upenn.edu/~jhaglund/preprints/es-final.pdf
- Markus Kuba and Alois Panholzer, *On the Degree Distribution of the Nodes in Increasing Trees*, preprint manuscript dated 30 November 2005, and *Journal of Combinatorial Theory, Series A* 114 (2007). https://www.dmg.tuwien.ac.at/kuba/nodedegree3.pdf
- Panpan Zhang, *On Several Properties of Plane-Oriented Recursive Trees*, arXiv:1706.02441, first arXiv version 8 June 2017, especially Section 3. https://arxiv.org/abs/1706.02441
- H. M. Mahmoud, R. T. Smythe and J. Szymański, *On the Structure of Random Plane-Oriented Recursive Trees and Their Branches*, *Random Structures & Algorithms* 4 (1993). https://doi.org/10.1002/rsa.3240040204
