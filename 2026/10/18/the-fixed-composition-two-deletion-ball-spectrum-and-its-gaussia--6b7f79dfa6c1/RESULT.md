# The fixed-composition two-deletion-ball spectrum and its Gaussian limit

## Finding
Let \(n\ge2\), \(0\le k\le n\), and choose a binary word \(W_{n,k}\) uniformly from the \(\binom nk\) length-\(n\) words containing exactly \(k\) ones. Let \(B(w)\) be the number of **distinct** length-\(n-2\) words obtainable by deleting exactly two positions from \(w\); different deletion masks yielding the same word count once. The following one theorem determines the complete conditional distribution, its exact mean, and its nondegenerate Gaussian limit.

Put \(u_0=z\), \(u_1=xz\), and define the formal Laurent series (in \(t\), with coefficients formal in \(z,x\))
\[
H_b=\frac{u_b}{t}+\frac{u_b^2}{1-u_b},\qquad
J_b=\frac{u_b}{t^2}+\frac{u_b^2}{1-u_b}\quad(b\in\{0,1\}).
\]
For each integer \(r\ge2\) and \(b\in\{0,1\}\), write \(b_i=b\oplus((i-1)\bmod2)\) for \(1\le i\le r\), where \(\oplus\) is binary exclusive-or, and put
\[
\mathcal F(z,x,t)=t\left(\frac{z^2}{1-z}+\frac{x^2z^2}{1-xz}\right)
+\sum_{r\ge2}t^{\binom{r+1}{2}}
 \sum_{b=0}^1 H_{b_1}H_{b_r}\prod_{i=2}^{r-1}J_{b_i}.
\]
The sum is well-defined coefficientwise in \(z\): a term with \(r\) runs has length at least \(r\). Every coefficient \([z^nx^kt^d]\mathcal F\) is a nonnegative integer and
\[
\boxed{\#\{w\in\{0,1\}^n:|w|_1=k,\ B(w)=d\}=[z^nx^kt^d]\mathcal F(z,x,t)}
\qquad(n\ge2,\ 0\le k\le n,\ d\ge1).
\]
Thus the probability generating polynomial is \([z^nx^k]\mathcal F/\binom nk\). In particular the exact mean is
\[
\boxed{\mathbb E B(W_{n,k})
=1+\frac{3(n-2)k(n-k)+2k(k-1)(n-k)(n-k-1)}{n(n-1)}}
\quad(n\ge2).
\]
If \(k=k_n\) and \(k_n/n\to\alpha\in(0,1)\), then
\[
\boxed{\frac{B(W_{n,k_n})-\mathbb E B(W_{n,k_n})}{n^{3/2}}
\ \Longrightarrow\ \mathcal N\!\left(0,16\alpha^4(1-\alpha)^4\right)}.
\]
This is the fixed-composition (rather than independent-symbol) law; the limit has strictly positive variance for every interior limiting composition.

## Assumptions and scope
Words are **linear**, not circular, over the ordered binary alphabet \(\{0,1\}\). An exact two-deletion ball is a set of distinct descendants, not a multiset of deletion-position pairs and not a fixed-length Levenshtein ball. The input distribution samples without replacement from a fixed composition; endpoints \(k=0,n\) are included in the exact formulas but excluded from the Gaussian limit. The theorem concerns all integers \(n\ge2\), and the limit assumes only \(k_n/n\to\alpha\in(0,1)\).

## Proof
**Canonical masks and the per-word formula.** For any fixed output word \(v\) that is a subsequence of a source \(w\), greedily embed \(v\) into \(w\) by always choosing the leftmost available matching position. This gives exactly one *canonical* kept-position set for each distinct output; hence deleting the complementary positions gives exactly one canonical two-deletion mask for each distinct two-deletion descendant.

Write \(X_i=\mathbf 1\{w_i\ne w_{i+1}\}\) for \(1\le i\le n-1\), and \(T=\sum_{i=1}^{n-1}X_i\). For a mask deleting positions \(i<j\) with \(j\ge i+2\), the greedy mask condition is that each deleted symbol immediately before a retained position differs from that next retained symbol: \(X_i=1\), and either \(j=n\) or \(X_j=1\). For adjacent deleted positions \(i,i+1<n\), both deleted symbols must differ from the next retained symbol at \(i+2\). On a binary alphabet this is equivalent to \((1-X_i)X_{i+1}=1\). The mask deleting the last two positions is always canonical. These conditions are necessary and sufficient, including at both boundaries.

Counting the three disjoint kinds of masks therefore gives
\[
\begin{aligned}
B(w)&=1+\sum_{i=1}^{n-2}X_i
 +\sum_{i=1}^{n-2}(1-X_i)X_{i+1}
 +\sum_{\substack{1\le i<j\le n-1\\j\ge i+2}}X_iX_j\\
&=\boxed{\binom{T+2}{2}-X_1-X_{n-1}
-2\sum_{i=1}^{n-2}X_iX_{i+1}}.
\end{aligned}
\]
For \(n=2\) both sums with upper limit \(n-2\) are empty, and \(X_1\) appears twice in the endpoint correction. This still gives the unique empty descendant. Let \(R=T+1\) be the number of constant runs, \(E=X_1+X_{n-1}\) the number of singleton endpoint runs (counting both ends of a two-run word), and \(I=\sum_{i=1}^{n-2}X_iX_{i+1}\) the number of singleton interior runs. Equivalently,
\[
B(w)=\binom{R+1}{2}-E-2I.
\]
This is the classical deterministic double-deletion run identity, reconstructed here from greedy subsequence embeddings rather than treated as a black box.

**Entire fixed-composition spectrum.** A binary word is uniquely determined by its first symbol \(b\) and a composition of \(n\) into \(r\) positive run lengths. The symbols of its runs alternate. If \(r=1\), only the two constant words arise and, at length at least two, both have \(B=1\); their total generating contribution is the first term in \(\mathcal F\).

For \(r\ge2\), a run of symbol \(b\) and length one contributes \(u_b\); one of length at least two contributes \(u_b^2/(1-u_b)\). A singleton endpoint run lowers \(B\) by one, while a singleton interior run lowers it by two. Thus an endpoint contributes \(H_b\), an interior run contributes \(J_b\), and the baseline \(\binom{r+1}{2}\) contributes \(t^{\binom{r+1}{2}}\). Summing over initial symbols and the number of runs gives exactly \(\mathcal F\). Its \(x\)-exponent counts ones, its \(z\)-exponent counts length, and its \(t\)-exponent is exactly \(B\), proving the coefficient identity and its probability normalization. Although intermediate factors contain negative powers of \(t\), every complete word contributes a positive exponent by the already-proved cardinality formula.

**Exact conditional mean.** Write \(a=n-k\). For any specified consecutive coordinate pair in a uniformly shuffled fixed-content word,
\[
q=\mathbb P(X_i=1)=\frac{2ka}{n(n-1)},\qquad
h=\mathbb P(X_i=X_{i+1}=1)=\frac{ka}{n(n-1)}.
\]
For four distinct coordinates (two disjoint transition tests), when \(n\ge4\),
\[
p_4=\mathbb P(X_i=X_j=1)
=\frac{4k(k-1)a(a-1)}{n(n-1)(n-2)(n-3)}\qquad(j\ge i+2).
\]
There are \(\binom{n-2}{2}\) disjoint transition-test pairs, \(n-2\) eligible single transitions with a deletion at the right endpoint, and \(n-2\) neighboring pairs of transitions. Taking expectations in the first canonical-mask sum above yields
\[
\mathbb E B=1+(n-2)q+(n-2)(q-h)+\binom{n-2}{2}p_4.
\]
Substitution and cancellation give the boxed exact formula. For \(n=2,3\), the four-coordinate term does not exist and is zero; direct evaluation of the same canonical-mask sum gives exactly the displayed formula, so no undefined falling-factorial probability is used.

**Gaussian limit under fixed content.** For \(0<k<n\), the classical fixed-composition run count has the following explicit enumeration (use the convention \(\binom ab=0\) when \(b<0\) or \(b>a\)):
\[
\begin{aligned}
\#\{w:|w|_1=k,\ R(w)=2j\}&=2\binom{k-1}{j-1}\binom{a-1}{j-1},\\
\#\{w:|w|_1=k,\ R(w)=2j+1\}&=\binom{k-1}{j}\binom{a-1}{j-1}+\binom{k-1}{j-1}\binom{a-1}{j}.
\end{aligned}
\]
This follows by composing the \(k\) ones and \(a\) zeros into alternating positive-length runs. Stirling's local Gaussian approximation to these binomial coefficients gives the standard fixed-composition runs central limit theorem whenever \(k/n\to\alpha\in(0,1)\). The exact first two moments, obtainable directly by the transition probabilities above, are
\[
\mu_n=\mathbb ET=\frac{2ka}{n},\qquad
\operatorname{Var}(T)=\frac{2ka(2ka-n)}{n^2(n-1)}.
\]
Consequently
\[
\frac{T-\mu_n}{\sqrt n}\Longrightarrow\mathcal N\!\left(0,4\alpha^2(1-\alpha)^2\right).
\]
The local statistic \(I=\sum_iX_iX_{i+1}\) has \(\operatorname{Var}(I)=O(n)\) in this fixed-content regime: intersecting triples contribute only \(O(n)\) covariance pairs, and any disjoint triples have covariance \(O(1/n)\) by the six-coordinate sampling-without-replacement formula, uniformly when the composition ratios stay in a compact subinterval of \((0,1)\). Also \(E=X_1+X_{n-1}=O(1)\). Expand the established polynomial formula about \(\mu_n\):
\[
B-\mathbb EB=\mu_n(T-\mu_n)
 +\tfrac12\big((T-\mu_n)^2-\operatorname{Var}(T)\big)
 +\tfrac32(T-\mu_n)-2(I-\mathbb EI)-(E-\mathbb EE).
\]
Since \(T-\mu_n=O_{\mathbb P}(\sqrt n)\), every term after the first is \(o_{\mathbb P}(n^{3/2})\), whereas \(\mu_n/n\to2\alpha(1-\alpha)\). Slutsky's theorem and the run-count limit yield the boxed Gaussian limit with variance \(16\alpha^4(1-\alpha)^4\). This completes the proof.

## Verification
`verify.py` directly enumerates every binary word of lengths \(2\) through \(13\), constructs its distinct two-deletion outputs, and compares the resulting cardinality with the independently derived transition formula. It separately expands the alternating-run products by integer dynamic programming, comparing the **entire** histogram at every weight through length \(13\). The exact histogram mass and the rational mean are further checked for every weight through length \(18\). There are \(16{,}380\) directly enumerated source words across lengths \(2\) through \(13\). These finite computations do not prove the all-length theorem; the preceding canonical-mask, run-product, and asymptotic arguments do.

As an illustrative complete conditional spectrum at \(n=6,\ k=3\), the possible ball sizes and their multiplicities are \(3\mapsto2,5\mapsto4,6\mapsto2,7\mapsto4,8\mapsto2,9\mapsto4,11\mapsto2\), summing to \(\binom63=20\).

## Relationship to prior work
The run identity underlying the proof is already known from Swart and Ferreira's exact double-deletion enumeration and is **not** claimed as new. Liron and Langberg analyzed extremal descendant counts at specified run counts. Atashpendar and collaborators studied embedding-weight distributions and entropy across supersequences, with explicit attention to Hamming weight; that is a different direction of conditioning and does not give the complete distribution of distinct *descendants across fixed-content sources* established here. Wang and Wang analyze the distribution/concentration of radius-one **fixed-length Levenshtein balls**, which permit a deletion and reinsertion and differ from exact two-deletion descendant sets.

A separately published exact variance formula for the size of the binary two-deletion descendant set concerns the **unconditioned** uniform binary source, as does an accessible more general complete-law claim for independent uniform finite-alphabet symbols. Mixing over all Hamming weights loses the marked composition variable and does not recover the conditional coefficient array or its composition-dependent Gaussian scale. This theorem provides all fixed-weight histograms and a sharp Gaussian law at every positive limiting density, rather than restating the known run formula or the unconditioned law. The recorded originality comparisons leave a residual possibility of an equivalent conditional enumeration in differently indexed literature.

## Limitations
The statement is restricted to binary words and exactly two deletions. The product is an explicit coefficient formula rather than a single simplified rational function in the three variables; its run-number sum is finite for every fixed length. The Gaussian conclusion does not cover extremely sparse or extremely dense compositions where \(k/n\to0\) or \(1\). Neither exact fixed-content variance at finite length nor a quantitative normal-approximation rate is claimed. Completeness of a bibliographic search cannot be proved from indexed sources; a differently named prior conditional formula might exist.

## References
1. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” *IEEE Transactions on Information Theory* 49(1) (2003), 269–273, DOI:10.1109/TIT.2002.806155.
2. Y. Liron and M. Langberg, “A characterization of the number of subsequences obtained via the deletion channel,” arXiv:1202.1644 (first posted 2012-02-08).
3. A. Atashpendar et al., “From Clustering Supersequences to Entropy Minimizing Subsequences for Single and Double Deletions,” arXiv:1802.00703 (first posted 2018-02-02).
4. G. Wang and Q. Wang, “On the Size Distribution of Levenshtein Balls with Radius One,” arXiv:2204.02201 (first posted 2022-04-05; the preprint is about fixed-length Levenshtein balls).
5. V. L. P. Pham, K. Goyal, and H. M. Kiah, “Sequence Reconstruction Problem for Deletion Channels: A Complete Asymptotic Solution,” arXiv:2111.04255 (first posted 2021-11-08).
6. “Exact variance of binary two-deletion sphere size,” publicly accessible research result (unconditioned binary-source variance); cited here solely for comparison of theorem scope.
