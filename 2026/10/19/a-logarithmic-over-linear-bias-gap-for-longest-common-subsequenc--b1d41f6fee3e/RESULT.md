# A logarithmic-over-linear bias gap for longest common subsequences of many random words

## Finding

Let \(q\ge 2\) be fixed and \(p_1>p_2\ge\cdots\ge p_q>0\), with \(\sum_{i=1}^q p_i=1\). For every \(d\ge2\), let \(\gamma_{\mathbf p,d}\) be the limiting expected longest-common-subsequence length per source symbol among \(d\) independent length-\(n\) words sampled letterwise from \(\mathbf p\), as \(n\to\infty\). Put \(\Delta=p_2^{-1}-p_1^{-1}>0\). Then

\[
0\le\gamma_{\mathbf p,d}-p_1,\qquad
\limsup_{d\to\infty}\frac{d}{\log d}(\gamma_{\mathbf p,d}-p_1)
\le\frac{1-p_1}{2\Delta}.
\]

In particular, the excess is \(O_{\mathbf p}((\log d)/d)\), and is \(o(d^{-1/2})\) for every fixed positive distribution with a uniquely most probable letter. The following finite-\(d\) variational upper bound holds. For \(t>0\) put

\[
M_i(t)=\frac{p_i}{p_i+e^t-1},\qquad
S_d(t)=\sum_{i=1}^q M_i(t)^d.
\]

For any \(t>0\) with \(S_d(t)<1\),

\[
\gamma_{\mathbf p,d}\le \frac{dt}{-\log S_d(t)}.
\]

The theorem gives an upper bound, not a matching asymptotic equivalent for the excess.

## Assumptions and scope

All probabilities are fixed as \(d\to\infty\); in particular \(\Delta>0\) is fixed and the finite alphabet has no zero-probability letters. Each of the \(d\) words has the same length \(n\) and all letters, across words and positions, are independent. For words \(x^{(1)},\ldots,x^{(d)}\), \(\operatorname{LCS}\) denotes the maximum length of a word that is an order-preserving subsequence of every input word, without any requirement of contiguous occurrences. The logarithm is natural.

For each fixed \(d\), the expected LCS length \(a_n\) is superadditive in \(n\): concatenating the longest common subsequences of the first \(n\) and final \(m\) blocks gives a common subsequence of length at least their sum, pointwise. Independence and stationarity yield \(a_{n+m}\ge a_n+a_m\); therefore Fekete's lemma, with \(0\le a_n\le n\), gives the limit \(\gamma_{\mathbf p,d}=\lim_{n\to\infty}a_n/n\).

## Proof

**1. Embedding-time law.** Fix any target word \(w=w_1\cdots w_\ell\). Scan an infinite i.i.d. source from left to right and greedily locate successive letters of \(w\). The number \(T_w\) of inspected source symbols until the target has been embedded equals a sum of independent geometric waiting times, one for each target letter. A geometric random variable \(G_i\) supported on \(1,2,\ldots\), with success probability \(p_i\), satisfies

\[
\mathbb E[e^{-tG_i}]
=\sum_{h\ge1}p_i(1-p_i)^{h-1}e^{-th}
=\frac{p_i}{p_i+e^t-1}=M_i(t).
\]

Consequently, by Markov's inequality applied to \(e^{-tT_w}\), for every \(t>0\),

\[
\Pr\{w\text{ is a subsequence of an independent length-}n\text{ source}\}
=\Pr\{T_w\le n\}
\le e^{tn}\prod_{j=1}^{\ell}M_{w_j}(t).
\]

**2. Union bound and finite-rate inequality.** Independence across the \(d\) source words raises the last probability bound to the \(d\)-th power. If their LCS length is at least \(\ell\), at least one of the \(q^\ell\) possible target words is embedded in all of them. Summing the bounds over these targets factorizes exactly:

\[
\Pr\{\operatorname{LCS}\ge\ell\}
\le e^{dtn}\sum_{w\in\{1,\ldots,q\}^{\ell}}\prod_{j=1}^{\ell}M_{w_j}(t)^d
=e^{dtn}S_d(t)^\ell.
\]

If \(S_d(t)<1\) and \(\alpha>dt/(-\log S_d(t))\), set \(\ell=\lceil\alpha n\rceil\). The right-hand side decays exponentially in \(n\). Since the LCS is between zero and \(n\), its expected normalized length has limit at most \(\alpha\). Letting \(\alpha\) decrease proves \(\gamma_{\mathbf p,d}\le dt/(-\log S_d(t))\).

**3. Unique dominant letter and the asymptotic scale.** Write \(\Lambda_i(t)=-\log M_i(t)\). Taylor expansion as \(t\downarrow0\), with fixed \(\mathbf p\), gives

\[
\Lambda_i(t)=\frac{t}{p_i}-\frac{1-p_i}{2p_i^2}t^2+O_{\mathbf p}(t^3),\qquad
\Lambda_i(t)-\Lambda_1(t)
=\left(\frac1{p_i}-\frac1{p_1}\right)t+O_{\mathbf p}(t^2).
\]

Take \(t_d=(\log d)/(d\Delta)\) for integers \(d\ge2\). For each \(i\ge2\), \(p_i^{-1}-p_1^{-1}\ge\Delta\), hence

\[
\exp\{-d(\Lambda_i(t_d)-\Lambda_1(t_d))\}
=d^{-(p_i^{-1}-p_1^{-1})/\Delta}(1+o(1))
=O_{\mathbf p}(d^{-1}).
\]

The finite sum of these terms is \(O_{\mathbf p}(1/d)\). Therefore

\[
-\log S_d(t_d)
=d\Lambda_1(t_d)
-\log\left(1+\sum_{i=2}^q e^{-d(\Lambda_i(t_d)-\Lambda_1(t_d))}\right)
=d\Lambda_1(t_d)+O_{\mathbf p}(d^{-1}).
\]

This is positive for all sufficiently large \(d\), since \(d\Lambda_1(t_d)\) grows proportionally to \(\log d\). Dividing by \(d\), expanding the reciprocal, and substituting the second-order Taylor series gives

\[
\frac{dt_d}{-\log S_d(t_d)}
=\frac{t_d}{\Lambda_1(t_d)+O_{\mathbf p}(d^{-2})}
=p_1+\frac{1-p_1}{2}t_d
+O_{\mathbf p}\left(t_d^2+\frac1{d\log d}\right).
\]

Since \(t_d=(\log d)/(d\Delta)\), the claimed limsup upper coefficient follows.

**4. Lower baseline.** In each source word, take the subsequence comprising only the most likely letter. Its common length is the minimum of the \(d\) counts of that letter. For fixed \(d\), the strong law of large numbers shows that this minimum divided by \(n\) tends to \(p_1\) almost surely. The ratio is bounded by one, so bounded convergence shows \(\gamma_{\mathbf p,d}\ge p_1\). This completes the proof.

## Verification

The accompanying standalone `check_candidate.py` uses exhaustive exact-rational enumeration of binary source words through length six to test the geometric embedding inequality for all targets through length four at three positive Laplace parameters. It separately exhausts all pairs of binary words of lengths two through five, verifies the exact longest-common-subsequence event probabilities, and compares them with the stated union bound. Additional floating-point tests evaluate the finite-rate expression for three strict-bias laws and four growing numbers of strings. All assertions pass in the recorded output. Such experiments verify finite instances only; the asymptotic conclusion follows from the preceding proof, not from extrapolation.

## Relationship to prior work

Li, Ren, and Wen study the uniformly sampled \(q\)-ary multiword LCS constant. In particular, their binary law has an excess above \(1/2\) of order \(d^{-1/2}\). The present strict-bias result concerns a different distribution class and establishes a smaller upper scale, \((\log d)/d\), using a target-dependent geometric waiting-time transform. Nikolić and collaborators investigate algorithms for LCS instances with nonuniform letter probabilities and derive finite-instance embedding recurrences, rather than an asymptotic many-string constant or a strict-bias rate. Existing bounds on random-substring complexity and on subsequence universality concern different invariants. This contrast does not exclude an equivalent result in less accessible literature.

## Limitations

The leading coefficient above is an **upper envelope**, not a proved exact coefficient. No matching lower order for the excess is established, and the result does not apply when two or more alphabet letters tie for maximum probability, when alphabet size or letter probabilities vary with \(d\), or to non-i.i.d. sources. No independent audit has been performed.

## References

1. Ray Li, William Ren, and Yiran Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings*, arXiv:2504.10425, first posted 2025-04-14; *Bulletin of the Australian Mathematical Society* 114 (2026), 197–209. https://arxiv.org/abs/2504.10425 ; https://doi.org/10.1017/S000497272610104X .
2. Bojan Nikolić, Aleksandar Kartelj, Marko Đukanović, Milana Grbić, Christian Blum, and Günther Raidl, *Solving the Longest Common Subsequence Problem Concerning Non-Uniform Distributions of Letters in Input Strings*, *Mathematics* 9 (2021), article 1515. https://doi.org/10.3390/math9131515 .
3. George S. Lueker, *Improved Bounds on the Average Length of Longest Common Subsequences*, *Journal of the ACM* 56 (2009), article 17. https://doi.org/10.1145/1516512.1516519 .
