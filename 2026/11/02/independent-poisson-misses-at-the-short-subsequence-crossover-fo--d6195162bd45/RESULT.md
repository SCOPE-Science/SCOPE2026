# Independent Poisson misses at the short-subsequence crossover for many random binary strings

## Finding
Fix an integer \(r\ge1\). Let \(X^{(1)},\ldots,X^{(d_n)}\) be independent uniformly random binary words, each of length \(n\), and set
\[
a_{n,r}=2^{-n}\sum_{j=0}^{r-1}\binom nj.
\]
Assume that \(n\to\infty\) and the positive integers \(d_n\) satisfy \(d_n a_{n,r}\to\lambda\in(0,\infty)\). For every \(u\in\{0,1\}^r\), denote by \(Z_{n,u}\) the number of these \(d_n\) words that do **not** contain \(u\) as a scattered subsequence. Then
\[
(Z_{n,u}:u\in\{0,1\}^r)\ \xrightarrow{d}\ (P_u:u\in\{0,1\}^r),
\]
where the \(2^r\) variables \(P_u\) are mutually independent \(\operatorname{Poisson}(\lambda)\) variables.

In particular, if \(K_{n,r}\) denotes the number of distinct length-\(r\) binary words occurring as subsequences of **every** input string, then
\[
K_{n,r}\ \xrightarrow{d}\ \operatorname{Binomial}(2^r,e^{-\lambda}).
\]
For the common-subsequence maximum \(L_n=\operatorname{LCS}(X^{(1)},\ldots,X^{(d_n)})\), this yields the two-point law
\[
\begin{aligned}
\lim_{n\to\infty}\Pr(L_n=r)&=1-(1-e^{-\lambda})^{2^r},\\
\lim_{n\to\infty}\Pr(L_n=r-1)&=(1-e^{-\lambda})^{2^r},\\
\lim_{n\to\infty}\Pr(L_n\notin\{r-1,r\})&=0.
\end{aligned}
\]
The zero-length empty subsequence is allowed. The theorem concerns a simultaneous limit in both input length and number of inputs, not the fixed-number-of-inputs Chvátal–Sankoff constants.

## Assumptions and scope
All alphabets are the fixed labeled binary alphabet \(\{0,1\}\); a subsequence preserves the order of retained positions but need not be contiguous. The pattern length \(r\) is fixed before letting \(n\) tend to infinity. Every input string has length exactly \(n\), and all coordinates and strings are mutually independent and equiprobable. The integer sequence \(d_n\) need not have a prescribed rounding convention; only the displayed scaling assumption is used. Because \(a_{n,r}\to0\), this assumption entails \(d_n\to\infty\).

The crossover is at \(d_n\) of order \(2^n/n^{r-1}\). Lattice effects in \(n\) mean that a statement solely in terms of a real-valued inversion of \(d_n\) needs additional rounding conventions; the exact scaling above avoids that ambiguity.

## Proof
**1. One-pattern avoidance probability.** For any fixed pattern \(u=u_1\cdots u_r\), greedily match its symbols, advancing the matched-prefix index by one whenever the next random input symbol equals the next required pattern symbol. At each input position the advance indicator, conditional on the past, is an independent fair Bernoulli event. Thus the number of advances before time \(n\), up to absorption at \(r\), is governed by a \(\operatorname{Binomial}(n,1/2)\) count. The pattern is absent precisely when fewer than \(r\) advances occur. Consequently,
\[
\Pr(u\not\sqsubseteq X^{(1)})=a_{n,r}
\]
for every \(u\) and every \(n\ge r\). In particular, \(a_{n,r}\sim 2^{-n}n^{r-1}/(r-1)!\).

**2. The pair-avoidance lemma.** For fixed distinct binary patterns \(u,v\) of common length \(r\ge2\), the number of length-\(n\) words avoiding **both** as subsequences is \(O_r((n+1)^{r-2})\). To prove this, run the two greedy matchers together. As long as both patterns remain unmatched, the automaton states \((i,j)\) satisfy \(0\le i,j<r\). Each input bit either increments at least one coordinate (a *progress* move) or leaves both unchanged (a *loop*). A loop can occur only if the next desired symbols \(u_{i+1}\) and \(v_{j+1}\) are equal; in that case the opposite input letter loops and the other input letter increments **both** coordinates. All progress moves increase \(i+j\), so there are at most \(2r-2\) of them before absorption.

Any live automaton path visits at most \(r-1\) distinct loop-capable states when \(u\ne v\). Indeed, moving away from each loop-capable state increments both coordinates. If there were \(r\) such states, the first would have to be \((0,0)\), subsequent ones would have to be \((1,1),\ldots,(r-1,r-1)\), and all these states would require \(u_t=v_t\) for every \(t\); this contradicts \(u\ne v\). There are only finitely many progress-move skeletons, with number bounded in terms of \(r\). For one skeleton with \(m\le r-1\) loop-capable states, the loop repetitions are an ordered weak composition of the remaining input length into at most \(m\) parts and admit \(O_r((n+1)^{m-1})\) assignments; if \(m=0\), there can be no loops. Summing the finite skeletons proves the claimed bound. For \(r=1\), two different length-one patterns cannot both be absent when \(n\ge1\).

Therefore for distinct \(u,v\),
\[
\Pr(u,v\not\sqsubseteq X^{(1)})=O_r\bigl(2^{-n}(n+1)^{r-2}\bigr)=o(a_{n,r}),
\]
with the probability identically zero in the \(r=1\) case.

**3. Independent Poisson limit.** For each input word put \(B_i=\{u\in\{0,1\}^r:u\not\sqsubseteq X^{(i)}\}\). There are finitely many patterns, and the preceding lemma with the union bound gives
\[
\Pr(|B_i|\ge2)=O_r(2^{-n}(n+1)^{r-2})=o(a_{n,r}).
\]
For fixed \(t_u\in[0,1]\), the single-row multivariate probability generating function is
\[
\mathbb E\prod_u t_u^{\mathbf1_{\{u\in B_i\}}}
=1+a_{n,r}\sum_u(t_u-1)+o(a_{n,r}).
\]
The error estimate follows by expanding the product: all terms involving two or more different missed patterns are bounded by \(O_r(\Pr(|B_i|\ge2))\). Independence of input rows raises the last expression to the power \(d_n\), yielding
\[
\lim_{n\to\infty}\mathbb E\prod_u t_u^{Z_{n,u}}
=\exp\biggl(\lambda\sum_u(t_u-1)\biggr),
\]
the probability generating function of independent \(\operatorname{Poisson}(\lambda)\) coordinates. This proves joint weak convergence. The event \(Z_{n,u}=0\) says that \(u\) occurs in every input word. Thus the zero-coordinate count converges to \(\operatorname{Binomial}(2^r,e^{-\lambda})\), proving the claim for \(K_{n,r}\).

**4. Maximum length.** There exists a common subsequence of length \(r\) exactly when \(K_{n,r}>0\). Moreover, for every \(r\ge2\), a union bound gives
\[
\Pr(\exists\text{ a length-}\!(r-1)\text{ pattern absent from some input})
\le 2^{r-1}d_n a_{n,r-1}\longrightarrow0,
\]
since \(a_{n,r-1}/a_{n,r}\to0\). For \(r=1\), length zero is automatically common. Conversely, the expected number of length-\((r+1)\) patterns common to all inputs is at most
\[
2^{r+1}(1-a_{n,r+1})^{d_n}\le 2^{r+1}e^{-d_na_{n,r+1}}\longrightarrow0,
\]
because \(a_{n,r+1}/a_{n,r}\sim n/r\to\infty\). Markov's inequality thus excludes common subsequences of length \(r+1\) or greater with probability tending to one. Combining this sandwich with the limiting law of \(K_{n,r}\) proves the two-point LCS distribution. \(\square\)

## Verification
Two standalone exact-arithmetic programs and their recorded outputs are provided. `verify_greedy.py` independently computes one- and two-pattern avoidance counts by automaton state propagation and, for short inputs, by direct binary-word enumeration. It checks every pattern of length \(1\) through \(4\), all unordered pattern pairs, and all relevant input lengths through \(12\); it also records larger-length pair maxima through \(20\). `verify_critical.py` enumerates exact per-string sets of contained subsequences by a different state representation and uses inclusion–exclusion to obtain exact finite-length probabilities that at least one length-\(r\) pattern is common to all \(d\) inputs. It compares those probabilities with the theorem's asymptotic expression for several \(r\) and \(n\). These computations corroborate the arguments but do not replace the all-\(n\) proof.

To reproduce: run `python3 verify_greedy.py` and `python3 verify_critical.py`. Both programs use only the Python standard library. The outputs are in `verify_greedy_output.txt` and `verify_critical_output.txt`.

## Relationship to prior work
Li, Ren, and Wen [1] study the generalized Chvátal–Sankoff constants, taking a length-normalized limit for a fixed number of random input words before investigating how the number of words affects that constant. Their primary MSC classification is 68R15. The theorem above instead keeps the requested common-subsequence length fixed while the number of random strings grows exponentially in the input length; it determines the complete finite-size transition law, including joint multiplicities of missed patterns. The same greedy-match mechanism is relevant, but the fixed-number asymptotic bounds neither state nor imply the independent rare-pattern Poisson limit.

Heineman and coauthors [2] improve numerical lower bounds on generalized Chvátal–Sankoff constants using a different asymptotic order of limits. Related work on scattered-subsequence universality and shortest absent subsequences of **one** word studies the set of patterns contained within one input, not its intersection across an exponentially growing independent sample. In particular, a known exact distribution for the universality index of a single binary word does not imply the joint law of all individual length-\(r\) pattern misses across many words. An older probabilistic formulation could conceivably be equivalent; priority remains subject to outside verification.

## Limitations
The theorem fixes the binary alphabet and the positive pattern length \(r\); it does not establish a uniform result when \(r\) grows with \(n\), for dependent or nonuniform sources, or for larger alphabets. The result is a distributional limit, not an exact finite-\(n\) independence assertion. Numerical convergence may be slow for moderate \(n\), especially at larger fixed \(r\). The proof provides the asymptotic two-point law, not an estimate for the normalized Chvátal–Sankoff constant at fixed \(d\). Literature comparisons cannot exclude every unpublished or differently stated precursor.

## References
1. Ray Li, William Ren, Yiran Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings*, arXiv:2504.10425, first submitted 2025-04-14; *Bulletin of the Australian Mathematical Society* (2026), DOI:10.1017/S000497272610104X. https://arxiv.org/abs/2504.10425
2. George T. Heineman, Chase Miller, Daniel Reichman, Andrew Salls, Gábor Sárközy, Duncan Soiffer, *Improved Lower Bounds on the Expected Length of Longest Common Subsequences*, arXiv:2407.10925v1, 2024-07-15. https://arxiv.org/abs/2407.10925
