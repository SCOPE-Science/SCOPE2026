# Expected scattered-palindrome complexity of random double-occurrence words

## Finding

Consider a uniformly random word \(W_q\) on a labeled alphabet of \(q\ge1\) symbols, with every symbol occurring **exactly twice**. Let \(P(W_q)\) count distinct nonempty palindromic scattered subsequences, counting identical subsequence strings only once. Then
\[
\boxed{\mathbb E P(W_q)=\sum_{m=1}^q\binom qm\frac{2m}{(2m-1)!!},}
\]
where \((2m-1)!!=1\cdot3\cdots(2m-1)\). Moreover,
\[
\boxed{\mathbb E P(W_q)\sim e^{-1/4}\sqrt{2q}\,\sinh(\sqrt{2q})
\sim\frac{e^{-1/4}}2\sqrt{2q}\,e^{\sqrt{2q}}.}
\]
Thus the typical first moment has stretched-exponential growth, markedly smaller than the exponential sharp maximum for the same family.

## Assumptions and scope

All \((2q)!/2^q\) labeled linear words with multiplicity exactly two per symbol are equally likely; words are not quotiented by rotation or reversal. Subsequences select strictly increasing positions, and the counted objects are distinct resulting palindromic strings, not embeddings. The alphabet is fixed and labeled, though the expected value is invariant under renaming. The result covers every positive integer \(q\).

## Proof

### Counting palindromes on a fixed support

For nonempty symbol set \(S\) with \(|S|=m\), deleting letters outside \(S\) produces a uniform double-occurrence word \(U\) on \(S\): symmetry of uniform multiset permutations makes each of the \(N_m=(2m)!/2^m\) possible restricted words equally likely. A palindromic subsequence that uses all \(m\) labels must use every label twice except possibly one central label appearing once. Therefore it is either (i) an even palindrome of length \(2m\), equal to the entire restricted word, or (ii) an odd palindrome of length \(2m-1\), obtained by deleting precisely one occurrence of its center from the restricted word.

There are exactly \(m!\) possible even palindromic restricted words: choose the first half as a permutation and the second half as its reversal. There are also exactly \(m!\) **possible odd full-support palindrome strings** of length \(2m-1\): choose the center label in \(m\) ways and choose the permutation of the other \(m-1\) labels occupying the left half. For each such palindrome string, there are exactly \(2m-1\) distinct restricted words that contain it as a subsequence: insert the missing second occurrence of its central label into one of the \(2m\) gaps; the two gaps adjacent to the existing central letter give the same resulting word, and all other insertions are distinct. Conversely every restricted word containing that palindrome is obtained by one of these insertions.

Double counting the pairs consisting of a restricted word and one of its **distinct** full-support palindromic subsequences yields
\[
\mathbb E\bigl|\mathcal P_S(U)\bigr|
=\frac{m!+(2m-1)m!}{(2m)!/2^m}
=\frac{2m}{(2m-1)!!}.
\]
Linear expectation over the \(\binom qm\) possible supports of size \(m\) proves the exact finite formula, without any independence assumption between supports.

### Stretched-exponential asymptotics

Let \(\lambda=\sqrt{2q}\), define \(a_{q,m}=(2q)^m/(2m-1)!\) for \(m\ge1\), and put
\[
T_q=\sum_{m\ge1}a_{q,m}=\lambda\sinh\lambda.
\]
Write \(M_q\) for the positive-integer random variable with \(\Pr(M_q=m)=a_{q,m}/T_q\). Its probability generating function is
\[
\mathbb E[t^{M_q}]=\frac{\sqrt{2qt}\sinh(\sqrt{2qt})}{\lambda\sinh\lambda}.
\]
Differentiating at \(t=1\) gives
\[
\mathbb E[M_q]=\frac12+\frac\lambda2\coth\lambda,
\qquad
\operatorname{Var}(M_q)=\frac\lambda4\coth\lambda-\frac{\lambda^2}4\operatorname{csch}^2\lambda.
\]
Therefore \(M_q/\sqrt q\to1/\sqrt2\) in probability, by Chebyshev's inequality.

Put \(R_{q,m}=\prod_{j=0}^{m-1}(1-j/q)\) when \(1\le m\le q\), and \(R_{q,m}=0\) for \(m>q\). The exact finite sum is
\[
\mathbb E P(W_q)=\sum_{m\ge1}a_{q,m}R_{q,m}
=T_q\,\mathbb E[R_{q,M_q}].
\]
For \(m=O(\sqrt q)\), uniformly over \(m/\sqrt q\) in compact subsets of \((0,\infty)\), expansion of \(\log(1-j/q)\) yields
\[
\log R_{q,m}=-\frac{m(m-1)}{2q}+O\!\left(\frac{m^3}{q^2}\right).
\]
Since \(M_q/\sqrt q\to1/\sqrt2\), it follows that \(R_{q,M_q}\to e^{-1/4}\) in probability. The variables satisfy \(0\le R_{q,M_q}\le1\), so their expectations also converge to \(e^{-1/4}\). This proves the first asymptotic equivalence. Finally \(\sinh\lambda\sim e^\lambda/2\), proving the second.

## Verification

The standalone `verification/check_random_double_occurrence_mean.py` constructs all first-appearance-normalized double-occurrence words for \(1\le q\le5\) and independently enumerates their distinct palindromic scattered subsequences via positional masks. Exact rational sample means equal the theoretical values: \(2,16/3,52/5,1856/105,5240/189\), with complete sample sizes \(1,3,15,105,945\). It additionally computes exact finite-sum ratios to the asymptotic approximation for larger sizes, checking their convergence numerically. The proof above, not finite extrapolation, establishes the theorem for unbounded \(q\).

## Relationship to prior work

Cruz et al. study the structure of double-occurrence words through repeat/return insertions and label-renaming equivalence. Müllner and Ryzhikov study lengths of palindromic subsequences, rather than expected numbers of **distinct** palindromic subsequence strings. The standard single-input counting problem computes the statistic of an individual word. The known sharp maximum for double-occurrence words does not determine this uniform random-word expectation: the present average is a different invariant and has a smaller, stretched-exponential growth scale.

## Limitations

The result addresses the first moment under the precise uniform multiset-permutation distribution, not variance, concentration, higher moments, alternate symbol multiplicities, or circular words. Asymptotic equivalence concerns \(q\to\infty\), with a proven limit and no claimed uniform finite-\(q\) relative error estimate. Scientific novelty may still be limited by inaccessible or unindexed equivalent results; independent audit has not been performed.

## References

1. D. A. Cruz, M. M. Ferrari, N. Jonoska, L. Nabergall, M. Saito, *Insertions Yielding Equivalent Double Occurrence Words*, arXiv:1811.11739, first submitted 2018-11-28. https://arxiv.org/abs/1811.11739
2. C. Müllner, A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first submitted 2019-01-22. https://arxiv.org/abs/1901.07502
3. *Count Different Palindromic Subsequences*, problem 730. https://leetcode.com/problems/count-different-palindromic-subsequences/
