# Fixed points positively covary with every higher-order increasing-subsequence count

## Finding
Let \(\pi\) be uniformly distributed over all permutations of \(\{1,\dots,n\}\), with \(n\ge3\). Write \(F(\pi)=\#\{i:\pi(i)=i\}\) for its number of fixed points, and let \(Z_{n,k}(\pi)\) count increasing subsequences of length \(k\), with nonconsecutive positions permitted. For every integer \(3\le k\le n\), set
\[
p_{j,x}=\frac{\binom{x-1}{j-1}\binom{n-x}{k-j}}{\binom nk},
\qquad 1\le j\le k,\quad1\le x\le n,
\]
where \(\binom ab=0\) when \(b<0\) or \(b>a\).

**Theorem.** For every such \(n,k\),
\[
\boxed{\operatorname{Cov}(F,Z_{n,k})
=\frac{\binom nk}{k!}\sum_{j=1}^{k}\left(\sum_{x=1}^{n}p_{j,x}^{2}-\frac1n\right)>0.}
\]
Moreover,
\[
\operatorname{Cov}(F,Z_{n,k})\ge
\frac{\binom nk}{k!}\,\frac{k-1}{n(n-k+1)},
\]
and, for each **fixed** \(k\ge3\) as \(n\to\infty\),
\[
\operatorname{Cov}(F,Z_{n,k})
=\left(\frac{4^{k-1}}{(2k-1)!}-\frac{k}{(k!)^2}\right)n^{k-1}
+O_k(n^{k-2}).
\]
The leading constant is strictly positive; when \(k=3\), it is \(1/20\).

## Assumptions and scope
The probability space is the entire symmetric group \(S_n\) with equal mass \(1/n!\) on each permutation. A subsequence is defined by strictly ordered positions whose associated values are also strictly ordered, not by consecutive positions. Expectations, covariance and asymptotic notation use this unconditioned uniform law. The strict-sign claim covers **all** integer pairs \(n\ge3\), \(3\le k\le n\); no restriction that \(k\) be fixed is needed for the exact formula. Only the final asymptotic statement assumes that \(k\) remains fixed while \(n\) grows. The length-two relation to inversions is deliberately excluded from the claimed novelty scope.

## Proof
**1. Increasing-subsequence size bias.** Every selected set of \(k\) positions has probability \(1/k!\) of being increasing, so \(\mathbb E Z_{n,k}=\binom nk/k!\). Independently choose uniform \(k\)-subsets \(I=\{i_1<\dots<i_k\}\) and \(V=\{v_1<\dots<v_k\}\) of \(\{1,\dots,n\}\). Impose \(\pi(i_j)=v_j\) for each \(j\), and uniformly biject the remaining \(n-k\) positions to the remaining values. The resulting law \(\mu\) satisfies, for every \(\pi\in S_n\),
\[
\mu(\pi)=\frac{Z_{n,k}(\pi)}{n!\,\mathbb E Z_{n,k}}.
\]
Indeed each increasing subsequence in \(\pi\) corresponds to exactly one ordered choice of \((I,V)\), and each prescribed compatible choice admits \((n-k)!\) extensions. Thus, for every statistic \(H\),
\[
\operatorname{Cov}(H,Z_{n,k})=(\mathbb E Z_{n,k})
\bigl(\mathbb E_\mu H-\mathbb E H\bigr).
\]

**2. Fixed points under size bias.** In the forced positions, a fixed point occurs exactly when \(i_j=v_j\). The law of the \(j\)-th smallest element of an independently sampled uniform \(k\)-subset is precisely \(\Pr(i_j=x)=\Pr(v_j=x)=p_{j,x}\). Hence the expected number of forced fixed points equals \(\sum_{j,x}p_{j,x}^{2}\).

If \(k<n\), conditioned on \(I,V\), every unforced position \(t\notin I\) has probability \(1/(n-k)\) to be fixed when \(t\notin V\), and probability zero otherwise. Its expected contribution is therefore
\[
\frac{\mathbb E\#(\{1,\dots,n\}\setminus(I\cup V))}{n-k}
=\frac{n-2k+k^2/n}{n-k}=\frac{n-k}{n},
\]
because \(I,V\) are independent and \(\mathbb E|I\cap V|=k^2/n\). When \(k=n\), no unforced positions exist and this same expression equals zero. Thus
\[
\mathbb E_\mu F=\sum_{j,x}p_{j,x}^{2}+\frac{n-k}{n}.
\]
Since \(\mathbb E F=1\), substituting in the size-bias identity proves the boxed formula.

**3. Strict sign and bound.** For each \(j\), the vector \((p_{j,x})_{x=1}^n\) is a probability distribution, whence \(\sum_x p_{j,x}^{2}\ge1/n\) by Cauchy–Schwarz. The first-order-statistic distribution \((p_{1,x})_x\) vanishes at all \(x>n-k+1\). The support contains exactly \(n-k+1\) points and therefore
\[
\sum_xp_{1,x}^{2}\ge\frac1{n-k+1}.
\]
The other \(k-1\) rows each contribute at least \(1/n\). Consequently the sum in the boxed formula is bounded below by
\[
\frac1{n-k+1}-\frac1n=\frac{k-1}{n(n-k+1)}>0.
\]
This also handles \(k=n\) without taking a limit.

**4. Fixed-length asymptotic.** For fixed \(k\), put
\[
f_j(t)=\frac{k!}{(j-1)!(k-j)!}\,t^{j-1}(1-t)^{k-j},\qquad 0\le t\le1.
\]
Uniformly over \(x=1,\dots,n\), \(np_{j,x}=f_j(x/n)+O_k(n^{-1})\). Therefore Riemann summation gives
\[
\sum_{x=1}^{n}p_{j,x}^2=\frac1n\int_0^1f_j(t)^2\,dt+O_k(n^{-2}).
\]
The beta-integral yields
\[
\int_0^1f_j^2
=\frac{(k!)^2}{(2k-1)!}
\binom{2j-2}{j-1}\binom{2k-2j}{k-j}.
\]
Summing over \(j\) and using the coefficient identity
\[
\sum_{a=0}^{k-1}\binom{2a}{a}\binom{2(k-1-a)}{k-1-a}=4^{k-1}
\]
(the square of \((1-4z)^{-1/2}\)) gives
\[
\sum_{j=1}^k\int_0^1f_j(t)^2\,dt
=\frac{(k!)^2 4^{k-1}}{(2k-1)!}.
\]
The boxed formula and \(\binom nk/k!=n^k/(k!)^2+O_k(n^{k-1})\) now yield the claimed expansion. Strict positivity of its leading coefficient also follows from \(\int_0^1 f_j^2\ge(\int_0^1 f_j)^2=1\), strictly for the nonconstant first-order density when \(k\ge2\).

## Verification
A standalone Python verifier (`verify_covariance.py`) uses integer/fraction arithmetic. It enumerates every permutation for \(3\le n\le8\), independently computes its fixed points and increasing-subsequence counts, and compares the resulting exact covariances with the formula for all \(3\le k\le n\). The exhaustive sample comprises 46,230 permutations. Additional exact checks cover \(3\le n\le150\) and \(3\le k\le\min(n,17)\), together with the coefficient sign for fixed \(3\le k\le12\); 2,242 rational assertions passed. Run `python verify_covariance.py` from the directory containing this file and the verifier. The unrestricted theorem depends on the proof above, not on those finite checks.

## Relationship to prior work
Pinsky (first public arXiv submission 2004) defines \(Z_{n,k}\), computes its mean, and introduces the same increasing-subsequence-biased permutation measure to study variance, limit laws and total-variation approximation. The **measure itself is established prior work**; the claim here is its explicit mixed moment with the fixed-point count, rank-collision formula, strict sign for every length, and fixed-length expansion. Pinsky (2026) treats fixed points together with inversions, equivalent to the **length-two** increasing-subsequence count after subtracting from the total number of pairs; the present result excludes that pair case and treats \(k\ge3\). Earlier studies of increasing-subsequence numbers and conditioned involution longest subsequences do not by themselves imply this unconditional all-length fixed-point covariance identity. No assertion of exhaustive historical priority is made.

## Limitations
Covariance positivity is weaker than positive association, conditional stochastic dominance, or a statement about the longest increasing subsequence; none of these is claimed. The expansion is only for fixed \(k\), not a uniform estimate over growing lengths. The rank-collision evaluation uses the uniform symmetric group and may not extend to permutations with constrained cycle type. A fully independent mathematical audit and exhaustive bibliographic priority verification have not been performed. A possible implicit identity in older general joint generating-function work remains a historical-priority risk.

## References
1. R. G. Pinsky, *Law of large numbers for increasing subsequences of random permutations and an approximation result for the uniform measure*, arXiv:math/0407353, first submitted 21 July 2004. https://arxiv.org/abs/math/0407353 ; full text: https://arxiv.org/pdf/math/0407353.
2. R. G. Pinsky, *The Inversion Statistic in Derangements and in other Permutations with a Prescribed Number of Fixed Points*, Electronic Journal of Combinatorics 33(2) (2026), P2.36, DOI 10.37236/14250. https://doi.org/10.37236/14250.
3. A. Lifschitz and B. Pittel, *The Number of Increasing Subsequences of the Random Permutation*, Journal of Combinatorial Theory, Series A 31 (1981), 1–20. Mentioned as older marginal-subsequence literature; its complete text was not examined here.
