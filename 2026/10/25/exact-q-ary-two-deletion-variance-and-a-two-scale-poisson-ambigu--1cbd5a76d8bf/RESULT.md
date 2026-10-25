# Exact q-ary two-deletion variance and a two-scale Poisson ambiguity transition
## Finding
Let \(X\) be uniformly distributed on words of length \(n\ge2\) over an alphabet of \(q\ge2\) letters, and let \(B_{n,q}(X)\) be the number of **distinct** length-\(n-2\) outputs obtainable by exactly two deletions. Put \(m=n-1\) and \(p=1-1/q\). Then
\[
\mathbb E B_{n,q}=\binom m2p^2+m-\frac{m-1}{q},
\]
and the exact variance for **every** \(q,n\) is
\[
\boxed{\operatorname{Var}(B_{n,q})=
\binom m2p^2(1-p^2)+6\binom m3p^3(1-p)
+\frac{(m-1)p(q-2)}{q^2}.}
\]
When the alphabet grows with the word length, with \(n/q_n\to\theta\in(0,\infty)\), the deletion-volume deficit has a **two-scale joint limit**. Set
\[
H_n=\binom n2-B_{n,q_n}(X),\qquad
Z_n=\sum_{i=1}^{n-1}\mathbf1\{X_i=X_{i+1}\}.
\]
If \(P_1,P_2\) are independent Poisson variables of mean \(\theta\), then
\[
\boxed{\left(\frac{H_n}{n},\ H_n-nZ_n\right)
\ \Longrightarrow\ \left(P_1,\ P_2-\frac{P_1(P_1+3)}2\right).}
\]
Moreover, for \(n\ge3\), the probability of the largest possible volume is exactly
\[
\Pr\left(B_{n,q}=\binom n2\right)
=\left(1-\frac1q\right)\left(1-\frac2q\right)^{n-2}.
\]
Consequently this probability converges to \(e^{-2\theta}\) in the same growing-alphabet regime. The maximum-volume probability tends to one if \(n/q_n\to0\), and to zero if \(n/q_n\to\infty\) (with \(n\ge3\)).

## Assumptions and scope
A deletion is the removal of one position, with order preserved; duplicate resulting strings are counted only once. Alphabet symbols are independent and exactly uniform. The finite-\(q\) formulas hold for all integers \(n,q\ge2\), even if \(q\) depends on \(n\). The Poisson law assumes \(n/q_n\to\theta\) with strictly positive finite \(\theta\); it is a joint weak limit of random vectors, not a pointwise identity or a claim for fixed \(q\).

For a fixed word \(x\), define the unequal-neighbor count and distance-two equality count
\[
K(x)=\sum_{i=1}^{n-1}\mathbf1\{x_i\ne x_{i+1}\},\qquad
J(x)=\sum_{i=1}^{n-2}\mathbf1\{x_i=x_{i+2}\}.
\]
Their local relationship with double deletion, valid for every alphabet, is
\[
\boxed{|\mathcal D_2(x)|=\binom{K(x)}2+n-1-J(x).}\tag{1}
\]
Here \(\binom a b=0\) when \(a<b\), and empty sums are zero.

## Proof
**1. Exact local identity.** Every distinct length-\(n-2\) subsequence has exactly one *greedy embedding*: scan \(x\) from left to right and select the earliest available occurrence of each next output letter. Write \(a<b\) for its two omitted positions. Set \(u_i=\mathbf1\{x_i\ne x_{i+1}\}\), \(1\le i\le n-1\), and \(j_i=\mathbf1\{x_i=x_{i+2}\}\), \(1\le i\le n-2\). The greedy rule partitions possible omitted positions into four disjoint cases:

(i) \(a<b\le n-1\), \(b\ge a+2\): the necessary and sufficient conditions are \(u_a=u_b=1\), giving \(\binom K2-\sum_{i=1}^{n-2}u_i u_{i+1}\).

(ii) \(a\le n-2\), \(b=n\): condition \(u_a=1\), giving \(K-u_{n-1}\).

(iii) \(a\le n-2\), \(b=a+1\): both omitted letters must differ from the next retained symbol, giving \(\sum_{i=1}^{n-2}u_{i+1}(1-j_i)\).

(iv) \((a,b)=(n-1,n)\): always one choice.

For each \(i\le n-2\), the elementary three-letter identity
\[
u_i(1-u_{i+1})+u_{i+1}(1-j_i)=1-j_i
\]
follows directly by distinguishing \(x_i=x_{i+2}\) from \(x_i\ne x_{i+2}\). Summing the four contributions therefore gives \(\binom K2+1+\sum_{i=1}^{n-2}(1-j_i)\), establishing (1).

**2. Exact first and second moments.** For independent uniform letters, the \(m=n-1\) neighbor-inequality indicators \(u_i\) are independent Bernoulli variables with success probability \(p\): reveal \(X_1\), then its independent uniform successive group differences after identifying the alphabet with \(\mathbb Z/q\mathbb Z\). Thus \(K\sim\mathrm{Binomial}(m,p)\). The \(m-1\) distance-two equality indicators \(j_i\) are also jointly independent Bernoulli with probability \(1/q\): the edges \((i,i+2)\) form the disjoint union of two paths, and independent uniform vertex labels yield independent edge equalities on any forest. Hence
\[
\mathbb EJ=\frac{m-1}{q},\qquad
\operatorname{Var}(J)=\frac{(m-1)p}{q}.
\]
The binomial factorial-moment identities, separating pairs of two-edge subsets according to whether they share one position, give
\[
\operatorname{Var}\!\left(\binom K2\right)
=\binom m2p^2(1-p^2)+6\binom m3p^3(1-p).
\]
To compute the covariance with \(J\), observe that every \(j_i\) is uncorrelated with each single \(u_r\). The only quadratic \(u_r u_s\) that has nonzero covariance with \(j_i\) is \((r,s)=(i,i+1)\):
\[
\operatorname{Cov}(u_i u_{i+1},j_i)
=\Pr(j_i=u_i=u_{i+1}=1)-p^2/q
=p/q-p^2/q=p/q^2.
\]
Therefore \(\operatorname{Cov}(\binom K2,J)=(m-1)p/q^2\). Combining this with (1), \(\operatorname{Var}(\binom K2-J)\) gives the asserted variance and its mean. The case \(n=2\) also follows directly: every output is the empty word and both formulas yield zero variance.

**3. Deficit identity and its limit.** Put
\[
Z_n=\sum_{i=1}^{n-1}\mathbf1\{X_i=X_{i+1}\}=m-K,\qquad
J_n=\sum_{i=1}^{n-2}\mathbf1\{X_i=X_{i+2}\}.
\]
Substituting \(K=m-Z_n\) into (1) yields the exact integer identity
\[
H_n=nZ_n-\frac{Z_n(Z_n+3)}2+J_n.\tag{2}
\]
For fixed nonnegative integers \(a,b\), consider the joint factorial moment \(\mathbb E[(Z_n)_a(J_n)_b]\). It is a sum over ordered choices of \(a\) distinct distance-one edges and \(b\) distinct distance-two edges among the positions \(1,\ldots,n\). The choices whose \(a+b\) edges have mutually disjoint endpoints number \(n^{a+b}(1+o(1))\), and each has probability \(q_n^{-(a+b)}\). Any remaining choice contains a connected component with at least two edges and hence at least three distinct vertices. Because every edge length is one or two, the number of embeddings of any fixed nontrivial connected edge pattern is \(O(n)\); the probability that all its endpoint-equality requirements hold is exactly \(q_n^{-(v-1)}\) for a component with \(v\) vertices, whether or not it contains a cycle. Thus each such component contributes \(O(n/q_n^{v-1})=o(1)\), and the remaining isolated-edge components contribute bounded factors. Consequently
\[
\mathbb E[(Z_n)_a(J_n)_b]\longrightarrow\theta^{a+b}.
\]
These are precisely the joint factorial moments of two independent Poisson variables of mean \(\theta\); the standard factorial-moment characterization establishes \((Z_n,J_n)\Rightarrow(P_1,P_2)\). Applying (2), tightness of \(Z_n\), and the continuous mapping theorem proves the two-scale joint law.

**4. Full-volume threshold.** For \(n\ge3\), formula (2) is nonnegative and vanishes exactly when \(Z_n=J_n=0\), since \(Z_n\ge1\) gives \(nZ_n-Z_n(Z_n+3)/2\ge n-2>0\) for all \(1\le Z_n\le n-1\). Thus a center has the maximum \(\binom n2\) distinct descendants exactly when its adjacent letters and its distance-two letters always differ. Counting such words gives \(q(q-1)(q-2)^{n-2}\), and division by \(q^n\) yields the exact probability. Its exponential limit follows from \(n/q_n\to\theta\).

## Verification
The accompanying standalone `verify.py` uses independent direct deletion-output enumeration, compares it with (1) for all \(39{,}669\) inspected words, and computes exact rational first and second moments for alphabets of sizes \(2,3,4,5\). It checks the maximum-volume frequency for every tested \(n\ge3\). The recorded output ends with `VERIFY_OK`. These finite computations corroborate the combinatorial identity and moment algebra; the infinite Poisson limit follows from the factorial-moment argument, not finite simulation.

## Relationship to prior work
Wang, Li, and Fu (first posted 2026-09-15) analyze \(q\)-ary deletion-ball *intersections between two centers*, and also provide general extremal ball facts. Their arguments do not establish the random-single-center variance or growing-alphabet two-scale deficit law. The binary exact variance \((n-1)(n-2)(2n-3)/32\) was established in an earlier publicly archived mathematical manuscript (2026-10-04) using a binary run formula attributed to Swart and Ferreira. Substitution \(q=2\) into the present variance gives exactly that known result, which is **not claimed as novel**. The additional contribution here is the finite \(q\)-ary formula for every \(q\ge3\), and particularly the independent-Poisson two-scale transition as \(q\) grows with \(n\). Biers-Ariel, Godbole, and Kelley study expected *total* distinct-subsequence counts and certain alphabet extensions, not the variance or joint Poisson scaling of the exactly-two-deletion sphere.

## Limitations
The theorem concerns deletion of exactly two symbols from uniformly random words and does not establish distributions for higher deletion radii, nonuniform source laws, or the fixed-alphabet central limit behavior. The two-scale limit assumes \(n/q_n\) converges to a positive finite constant. The locally exact formula may be derivable from established subsequence enumeration identities, and an unindexed prior derivation of the \(q\)-ary variance or two-scale limit cannot be excluded. Independent external mathematical validation has not been performed.

## References
1. Xiang Wang, Han Li, Fang-Wei Fu, “On Sequence Reconstruction Problem for q-ary Deletion Channels,” arXiv:2609.16837, first public 2026-09-15, https://arxiv.org/abs/2609.16837.
2. “Exact variance of binary two-deletion sphere size,” public mathematical record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc.
3. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” IEEE Transactions on Information Theory 49(1) (2003), 269–273, DOI 10.1109/TIT.2002.806155.
4. Y. Biers-Ariel, A. Godbole, E. Kelley, “Expected Number of Distinct Subsequences in Randomly Generated Binary Strings,” DMTCS 19(2) (2018), https://arxiv.org/abs/1704.08661.
5. Andrew D. Lin, “Lower Bounds for all List-Decodable Deletion Codes,” arXiv:2609.26650, first public 2026-09-22, https://arxiv.org/abs/2609.26650.
