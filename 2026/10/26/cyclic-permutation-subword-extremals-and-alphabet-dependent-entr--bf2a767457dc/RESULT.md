# Cyclic permutation subword extremals and alphabet-dependent entropy bounds

## Finding
For an integer \(q\ge3\), write \(P_q=0\,1\,\cdots\,(q-1)\) for the permutation word on \(\{0,\ldots,q-1\}\), and let \(W_{q,m}=P_q^m\) for \(m\ge1\). An occurrence of a word \(u\) in \(W\) is a strictly increasing sequence of positions spelling \(u\), **not necessarily contiguous**. Put \(\operatorname{maxocc}(W)=\max_u\operatorname{occ}(W,u)\), including the empty word once.

**Exact optimization and classification.** For every \(m\ge1\),
\[
M_q(m):=\operatorname{maxocc}(W_{q,m})
=\max_{0\le r\le m}\binom{m+(q-1)r}{qr}.
\]
For \(m\ge2\), **all** maximizing subsequences are the words \(P_q^r\) attaining the displayed maximum. Their possible exponents comprise one integer or two consecutive integers. (When \(m=1\), every scattered subsequence has exactly one occurrence; the classification of maximizers has this exception.)

**Exact bivariate enumerator.** With \(b_{m,r}=\operatorname{occ}(P_q^m,P_q^r)\), including \(m=r=0\),
\[
\sum_{m,r\ge0} b_{m,r}x^m y^r
=\frac{(1-x)^{q-1}}{(1-x)^q-xy}.
\]

**Alphabet-dependent entropy bound.** Let \(\beta_q>1\) be the unique positive real root of
\[\beta_q^{q}-\beta_q^{q-1}=1.\]
For fixed \(q\), as \(m\to\infty\),
\[
\log_2 M_q(m)=qm\log_2\beta_q-\tfrac12\log_2 m+O_q(1).
\]
In particular, if \(L_q=\lim_{n\to\infty}n^{-1}\min_{W\in\Sigma_q^n}\log_2\operatorname{maxocc}(W)\) denotes the minimal subword-entropy rate (whose existence was proved previously), then
\[
\boxed{L_q\le\log_2\beta_q.}
\]
For \(q=3\), this gives \(L_3\le0.551463089746\ldots\), and \(\log_2\beta_q\) decreases strictly with \(q\). Thus, for **every alphabet size \(q\ge3\)**, this is strictly smaller than the previously available alphabet-independent bound \(\tfrac12\log_2(1+\sqrt2)=0.635776651582\ldots\). The case \(q=2\) recovers the already published alternating-binary family and is **not** asserted as new.

## Assumptions and scope
All alphabets contain \(q\) distinct letters with an explicitly chosen total order, all words are finite, and every occurrence is counted by its increasing index set. Relabeling \(P_q\) by a permutation of the alphabet leaves the theorem unchanged. A binomial coefficient with lower argument larger than upper argument is zero. The classification is for maximizing **targets** within the fixed source \(P_q^m\); it does not claim that \(P_q^m\) minimizes entropy among all source words. The novel range is \(q\ge3\); statements for \(q=2\) are provided only to connect with prior work.

## Proof
**1. Exact occurrence formula for arbitrary targets.** Let \(u=u_1\cdots u_\ell\) be any nonempty target word, with its letters regarded as integers \(0,\ldots,q-1\). Define its weak-descent count
\[\delta(u)=\#\{j:1\le j<\ell,\ u_{j+1}\le u_j\}.\]
A candidate occurrence chooses, for each letter, a copy index \(c_j\in\{1,\ldots,m\}\) of \(P_q\). Because each copy lists every symbol exactly once in increasing order, increasing source positions are equivalent to
\[
c_{j+1}\ge c_j+\mathbf1_{\{u_{j+1}\le u_j\}}.
\]
Subtracting the cumulative number of weak descents from each copy index gives an ordinary weakly increasing sequence \(1\le d_1\le\cdots\le d_\ell\le m-\delta(u)\). This is a bijection, hence the stars-and-bars count is
\[
\operatorname{occ}(P_q^m,u)=
\begin{cases}
\displaystyle\binom{m+\ell-1-\delta(u)}{\ell},&m>\delta(u),\\
0,&m\le\delta(u).
\end{cases}
\tag{1}
\]
For the empty target, the count is one by definition.

**2. Optimization over the target.** Every strictly increasing consecutive segment of a target has at most \(q\) letters. Splitting \(u\) at each weak descent into \(\delta(u)+1\) such segments therefore gives \(\delta(u)\ge\lfloor(\ell-1)/q\rfloor\). Equality is realized by the length-\(\ell\) prefix of \(P_q^\infty\). For fixed target length, formula (1) is nonincreasing in the weak-descent count, so this prefix is optimal.

If \((r-1)q+1\le\ell\le rq\), the minimal weak-descent count is \(r-1\). The resulting maximum \(\binom{m+\ell-r}{\ell}\) is increasing with \(\ell\) whenever \(r<m\), since the ratio at consecutive lengths is \((m+\ell-r+1)/(\ell+1)>1\). When \(r=m\), all such counts are one and hence cannot be globally maximal for \(m\ge2\), since \(\operatorname{occ}(P_q^m,P_q)=m+q-1>1\). Thus any maximizing target for \(m\ge2\) has length divisible by \(q\), say \(qr\), and has exactly \(r-1\) weak descents. It must consist of \(r\) strictly increasing segments of length exactly \(q\); every such segment is necessarily \(P_q\). This proves both the maximum formula and the **exhaustiveness** of its maximizing targets. The case \(m=1\) was stated separately.

**3. Strict log-concavity.** For \(0\le r<m\) set \(b_{m,r}=\binom{m+(q-1)r}{qr}\). Direct factorial cancellation gives
\[
\frac{b_{m,r+1}}{b_{m,r}}=
\frac{m-r}{qr+q}\prod_{j=1}^{q-1}
\frac{m+(q-1)r+j}{qr+j}.
\tag{2}
\]
Each factor is positive and strictly decreasing with \(r\): for the product factors, differentiation of the continuous extension gives a numerator \(-qm-j\), which is negative. Consequently adjacent ratios strictly decrease, so the positive sequence \(b_{m,0},\ldots,b_{m,m}\) is strictly log-concave when \(m\ge2\). Its maximizing exponents are therefore one index or two adjacent indices.

**4. Exact generating function.** Let \(\ell=qr\). Equation (1) gives \(b_{m,r}=\binom{m+(q-1)r}{qr}\). For fixed \(r\), summing over \(m\ge r\) and using the negative-binomial identity yields
\[
\sum_{m\ge0}b_{m,r}x^m=\frac{x^r}{(1-x)^{qr+1}}.
\]
Summing the geometric series over \(r\) proves the claimed rational bivariate enumerator.

**5. Entropy and its sharp logarithmic correction.** Set \(A_q(x)=\sum_{m\ge0}\sum_{r=0}^m b_{m,r}x^m=(1-x)^{q-1}/((1-x)^q-x)\). Its denominator has a unique positive root \(\rho_q\in(0,1)\) satisfying \((1-\rho_q)^q=\rho_q\). No other root has modulus at most \(\rho_q\): for any such root \(z\),
\[
|1-z|^q\ge(1-|z|)^q\ge(1-\rho_q)^q=\rho_q\ge|z|,
\]
and equality forces \(z=\rho_q\). This root is simple, since the denominator's derivative is \(-q(1-x)^{q-1}-1<0\) there; the numerator does not vanish. Partial fractions consequently yield \(\sum_r b_{m,r}=\Theta_q(\rho_q^{-m})\).

For the finer maximum estimate, put \(r=\alpha m+O(1)\). Stirling's formula in the interior of \(0<\alpha<1\) gives
\[
\log b_{m,r}=m\Phi_q(\alpha)-\tfrac12\log m+O_q(1),
\quad
\Phi_q(\alpha)=[1+(q-1)\alpha]\log[1+(q-1)\alpha]
-q\alpha\log(q\alpha)-(1-\alpha)\log(1-\alpha).
\]
The derivative vanishes exactly when \([1+(q-1)\alpha]^{q-1}(1-\alpha)=(q\alpha)^q\). The ratio formula (2) makes the maximizing integer \(r\) differ by \(O_q(1)\) from this unique interior saddle. Writing \(\alpha_q=(1-\rho_q)/(1+(q-1)\rho_q)\), direct substitution proves the saddle equation and \(\Phi_q(\alpha_q)=-\log\rho_q\). Therefore \(\log M_q(m)=-m\log\rho_q-\frac12\log m+O_q(1)\). Since \(1-\rho_q=\beta_q^{-1}\), the root equation implies \(\rho_q=\beta_q^{-q}\), giving exactly the stated asymptotic.

Finally, the earlier existence result for \(L_q\) lets us bound this limit along source lengths \(qm\) by the constructed words \(P_q^m\). For strict improvement, the equation \(\beta_q^{q-1}(\beta_q-1)=1\) shows \(\beta_q\) strictly decreases with \(q\), and at \(q=3\) the bound is \(0.551463\ldots<0.635776\ldots\).

## Verification
Run `python3 verify_cyclic_subseq.py` using Python's standard library. The script independently constructs all scattered-subsequence occurrence counts by position-wise dynamic programming, checks formula (1) for each encountered target, verifies the entire maximizing-target set, checks generating-function coefficients through degree \(36\), and checks strict log-concavity on a wider finite grid. The completed check reports `CYCLIC_PERM_SUBSEQUENCE_PASS full_DP_cases=20 tested_patterns=96595 winning_patterns=76 GF_coefficients=0..36 q=2..5 strict_log_concavity=q2..10,m2..40`. These computations test the derived finite identities; the proof above supplies the statements for all parameters.

## Relationship to prior work
Fang introduced the maximum scattered-subword occurrence and minimal subword-entropy rate; his 2024 proceedings and expanded 2025 article prove the existence of the rate and obtain the universal upper bound \(\frac12\log_2(1+\sqrt2)\). Fang's binary result for \((01)^m\) (Propositions 4.6–4.8 of the expanded article) yields the \(q=2\) instance of our occurrence coefficients and rational generating function, and a general theorem there already implies rationality for **any fixed pair of repeated source and target words**. Neither this rationality nor the binary instance is claimed as new. The contribution here is the exact **all-target** extremal classification for permutation cycles with \(q\ge3\), explicit closed enumerator, strict log-concavity, and a new alphabet-dependent bound improving Fang's stated all-alphabet bound for every \(q\ge3\). Menon and Singh analyze binary *source-word* optimizations for a fixed subsequence and do not imply these fixed-source many-letter classifications. Bukh and Saatashvili (2025) prove new general upper and lower asymptotic bounds for the optimal entropy rate, including sharper large-alphabet growth information using concatenations of *different* permutations. Their results do not classify the maximizers for the fixed source \(P_q^m\) or its exact rational generating function; our explicit bound is **not** asserted to beat their large-alphabet asymptotic bounds.

## Limitations
No optimality is asserted for \(L_q\): the displayed estimate is an upper bound obtained from a particular family of source words, not the exact minimal rate. The minimizing source words for alphabets of size at least three are not classified. Some equivalent treatment of repeated permutation words could exist in older or unindexed generalized binomial-coefficient literature. Later work of Bukh and Saatashvili gives stronger asymptotic information about the optimal entropy rate at large alphabet size, so the constructed-family bound should not be mistaken for a globally best known estimate for all \(q\). The alphabet-size-two case is prior work. Independent mathematical validation has not been performed.

## References
- W. Fang, *Maximal Number of Subword Occurrences in a Word*, arXiv:2406.02971, first public version June 5, 2024; AofA 2024, DOI 10.4230/LIPIcs.AofA.2024.3, esp. Sections 3–4.
- W. Fang, *Maximal number of subword occurrences in a word*, Journal of Experimental Mathematics 1(2), 2025, DOI 10.56994/JXM.001.002.002, esp. Corollary 4.5 and Propositions 4.6–4.8.
- A. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first public version June 13, 2023.
- B. Bukh and A. Saatashvili, *Most frequent subsequences in a word*, arXiv:2509.22619, first public version September 26, 2025, esp. Theorem 2 and Section 4.
