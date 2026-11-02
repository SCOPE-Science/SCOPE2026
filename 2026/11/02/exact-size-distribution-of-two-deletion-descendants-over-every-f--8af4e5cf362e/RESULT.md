# Exact size distribution of two-deletion descendants over every finite alphabet

## Finding

Let \(q\ge2\) and \(n\ge2\) be integers, and let \(D_2(w)\) be the set of **distinct** length-\(n-2\) subsequences obtainable by deleting exactly two positions from \(w\in\{0,\ldots,q-1\}^n\). The polynomial
\[
F_{q,n}(z)=\sum_{w\in\{0,\ldots,q-1\}^n}z^{|D_2(w)|}
\]
is given by the explicit finite formula below. Consequently it provides, for every alphabet, block length, and integer \(j\), the exact number \([z^j]F_{q,n}(z)\) of source words with precisely \(j\) distinct two-deletion descendants.

Put \(m=n-1\) and, for \(0<s<m\), define
\[
H_m(s,b,c)=
\begin{cases}
2\binom{s-1}{b-1}\binom{m-s-1}{c-1},&b=c,\\
\binom{s-1}{b-1}\binom{m-s-1}{c-1},&|b-c|=1,\\
0,&\text{otherwise},
\end{cases}
\]
where \(1\le b\le s\) and \(1\le c\le m-s\). Then
\[
\boxed{\begin{aligned}
F_{q,n}(z)={}&qz
+q(q-1)z^{\binom{m+1}{2}}(q-2+z^{-1})^{m-1}\\
&+q\sum_{s=1}^{m-1}\sum_{b=1}^{s}\sum_{c=1}^{m-s}
H_m(s,b,c)(q-1)^b z^{\binom{s+1}{2}+c}
(q-2+z^{-1})^{s-b}.
\end{aligned}}
\]
All apparently negative powers cancel in the displayed finite expression; it is a polynomial with nonnegative integer coefficients, including for \(q=2\). Empty sums vanish.

For a uniformly random \(q\)-ary word \(W\), put \(p=(q-1)/q\). Its moments obey
\[
\mathbb E|D_2(W)|=mp+\binom m2p^2+\frac1q,
\]
and, for \(n\ge3\),
\[
\boxed{\operatorname{Var}(|D_2(W)|)=
\frac{p(1-p)(m-1)}2
\left(2m^2p^2-3mp^2+mp+4p-2\right).}
\]
For \(n=2\) the variance is zero. In particular, the leading asymptotic variance at fixed \(q\) is \(p^3(1-p)n^3+O_q(n^2)\). At \(q=2\) the variance formula reduces to the previously known \(m(m-1)(2m-1)/32\); novelty is claimed for the complete all-alphabet distribution, not for that previously known binary variance.

## Assumptions and scope

The alphabet is the labeled finite set \(\{0,1,\ldots,q-1\}\), with \(q\ge2\). Deletion is exactly twice, positions are ordered, and two deletion patterns producing the same output count only once. All statements hold for every integer \(n\ge2\) without asymptotic or prime-power restrictions. The random word has independent, uniformly distributed symbols. Coefficients count labeled words, not symmetry classes of words.

## Proof

**1. Unique canonical deletion pairs.** Let \(w=w_1\cdots w_n\), and write \(X_i=\mathbf1_{\{w_i\ne w_{i+1}\}}\) for \(1\le i\le m\), \(S=\sum_{i=1}^m X_i\), and \(J=\sum_{i=1}^{m-1}X_iX_{i+1}\). For each distinct output \(y\in D_2(w)\), use its unique greedy, leftmost embedding in \(w\), and write \(i<j\) for the two omitted positions. The greedy property characterizes admissible pairs as follows.

If \(j=n\), either \(i=n-1\), or \(i<n-1\) and \(w_i\ne w_{i+1}\). This contributes \(1+S-X_m\) pairs. If \(j<n\) and \(j\ge i+2\), both \(w_i\ne w_{i+1}\) and \(w_j\ne w_{j+1}\) must hold, and conversely suffice. These contribute \(\binom S2-J\). If \(j=i+1<n\), the conditions are \(w_{i+1}\ne w_{i+2}\) and \(w_i\ne w_{i+2}\). Put
\[
E=\#\{i:1\le i\le m-1,\;w_i=w_{i+2}\ne w_{i+1}\}.
\]
This last case contributes \(S-X_1-E\). Since distinct greedy embeddings give distinct outputs, summing yields
\[
|D_2(w)|=\binom S2+2S+1-X_1-X_m-J-E.
\]
If \(K\) is the number of maximal zero-runs in the indicator word \(X_1\cdots X_m\), direct counting gives \(K=1+S-X_1-X_m-J\); hence
\[
\boxed{|D_2(w)|=\binom{S+1}{2}+K-E.}\tag{1}
\]
This proves the crucial deterministic identity without extrapolating from finite samples.

**2. Count the boundary patterns and inverse pairs.** Regard the alphabet as the additive cyclic group of size \(q\), and define increments \(d_i=w_{i+1}-w_i\pmod q\). A word is uniquely specified by its first symbol (\(q\) possibilities) and the \(m\) increments. We have \(X_i=1\) precisely when \(d_i\ne0\), and the length-three pattern counted by \(E\) occurs precisely when two consecutive nonzero increments satisfy \(d_{i+1}=-d_i\).

Fix a binary boundary pattern with \(s\) ones, \(b\) one-runs and \(c\) zero-runs. It has \(s-b\) consecutive pairs of nonzero increments. Each of its \(b\) one-runs has \(q-1\) choices for the first nonzero increment. For each of the other \(s-b\) increments, exactly one nonzero value is the negative of the preceding increment (weight \(z^{-1}\) in (1)), while the other \(q-2\) choices have weight one. Thus all assignments of symbols for this fixed pattern contribute
\[
q(q-1)^b z^{\binom{s+1}{2}+c}(q-2+z^{-1})^{s-b}.
\]
If \(0<s<m\), the one-run lengths and zero-run lengths have \(\binom{s-1}{b-1}\binom{m-s-1}{c-1}\) possible ordered compositions. Their types must alternate, giving two orders for \(b=c\), one for \(|b-c|=1\), and none otherwise. This is exactly \(H_m\). The all-zero boundary pattern has weight \(qz\). The all-one pattern has \(b=1,c=0\), giving the second term of the formula. Summing proves the exact polynomial for all \(q,n\).

**3. First and second moments.** For uniform \(W\), the increments \(d_i\) are independent uniform values, so the boundary indicators \(X_i\) are independent Bernoulli variables of parameter \(p\). Conditional on the indicators, the \(E\)-count is binomial with \(J\) trials and success probability \(1/(q-1)\): within a block of nonzero increments choose the first value freely, and each subsequent reversal/nonreversal choice has respectively one or \(q-2\) possibilities. This argument also shows conditional independence of the reversal flags.

The mean follows from \(\mathbb E\binom{S+1}{2}=mp+\binom m2p^2\), \(\mathbb E K=(1-p)+(m-1)p(1-p)\), and \(\mathbb E E=(m-1)p(1-p)\).

For the variance put \(T=X_1+X_m\) and \(f(S)=(S^2+3S)/2\). Formula (1) gives
\[
\mathbb E[|D_2(W)|\mid X]=f(S)+1-T-p^{-1}J,
\qquad
\operatorname{Var}(|D_2(W)|\mid X)=\frac{q-2}{(q-1)^2}J.
\]
For \(m\ge2\), the elementary independent-indicator calculations needed for total variance are
\[
\begin{aligned}
\mathbb E J&=(m-1)p^2,\\
\operatorname{Var}(J)&=(m-1)p^2(1-p^2)+2(m-2)p^3(1-p),\\
\operatorname{Var}(T)&=2p(1-p),\\
\operatorname{Cov}(T,J)&=2p^2(1-p),\\
\operatorname{Cov}(f(S),T)&=2(m-1)p^2(1-p)+4p(1-p),\\
\operatorname{Cov}(f(S),J)&=(m-1)p^2\bigl(5+(2m-8)p-(2m-3)p^2\bigr),\\
\operatorname{Var}(f(S))&=\frac{m(m-1)p^2}{2}\bigl(1+2(m-2)p-(2m-3)p^2\bigr)\\
&\quad+4mp(1-p)+4m(m-1)p^2(1-p).
\end{aligned}
\]
To check these identities, expand powers of \(S\) in falling factorials; for example \(\mathbb E(S)_a=(m)_a p^a\), and adjacent terms in \(J\) share one indicator while nonadjacent terms are independent. Substituting into
\[
\begin{aligned}
\operatorname{Var}(|D_2(W)|)
={}&\operatorname{Var}(f(S))+\operatorname{Var}(T)+p^{-2}\operatorname{Var}(J)\\
&-2\operatorname{Cov}(f(S),T)-2p^{-1}\operatorname{Cov}(f(S),J)\\
&+2p^{-1}\operatorname{Cov}(T,J)+\frac{q-2}{(q-1)^2}\mathbb EJ
\end{aligned}
\]
and simplifying yields the announced closed expression. The \(n=2\) case is immediate because every output is empty.

## Verification

The independent Python verifier `check.py` computes descendant sets directly for all words in 33 complete parameter families, then compares the entire resulting histogram to the run-composition formula. It also compares all local canonical-pair counts to direct descendant-set sizes and evaluates the predicted exact rational mean and variance. It verified 281,783 source words, plus 429 further parameter pairs checked algebraically from the enumerator (alphabet sizes 2 through 12 and lengths 2 through 40). Output and code are included as standalone artifacts. The finite checks are corroboration; the preceding three-step argument proves the theorem for all parameters.

## Relationship to prior work

Li, Wang and Fu (arXiv:2601.06493, first submitted January 10, 2026) study the numbers of subsequences of individual nonbinary strings, including extremal bounds at a prescribed number of runs. Their accessible full HTML text does not provide the ensemble-wide polynomial that counts *all* words by two-deletion descendant count. Mercier, Khabbazian and Bhargava (2008) develop general formulas for the number of subsequences of a specified input string; their full paper was not available for verification, and potential overlap with its uninspected body remains a priority risk. The known binary variance \(m(m-1)(2m-1)/32\) is already recorded in the public finding `2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc`. Our claimed contribution is the complete histogram for arbitrary \(q\ge2\), with a new all-alphabet variance specialization, rather than rediscovery of the binary variance. Wang and Wang (arXiv:2204.02201) study concentration of *fixed-length Levenshtein* balls, a distinct channel and object.

## Limitations

No uniqueness or priority is established merely by unsuccessful searches. The 2008 per-input subsequence paper and some other non-open sources could not be compared in full. The result concerns a uniform independent source, exactly two deletions, and the distinct-output-set size, not the number of deletion patterns, the multi-deletion law for \(t\ge3\), or unequal symbol probabilities. The finite verification is not a substitute for the proof. No independent external mathematical audit has been performed.

## References

1. Han Li, Xiang Wang, Fang-Wei Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493v2, https://arxiv.org/html/2601.06493v2 (first public version January 10, 2026).
2. H. Mercier, M. Khabbazian, V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, IEEE Transactions on Information Theory 54 (2008), 3279–3285, https://doi.org/10.1109/TIT.2008.924730 (full text not inspected).
3. Geyang Wang and Qi Wang, *On the Size Distribution of Levenshtein Balls with Radius One*, arXiv:2204.02201, https://arxiv.org/abs/2204.02201 (different fixed-length metric).
4. *Exact variance of binary two-deletion sphere size*, published published-finding corpus record `2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc.
