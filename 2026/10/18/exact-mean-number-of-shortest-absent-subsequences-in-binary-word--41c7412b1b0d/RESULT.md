# Exact mean number of shortest absent subsequences in binary words

## Finding
Fix the binary ambient alphabet \(\Sigma=\{0,1\}\). For a finite word \(w\in\Sigma^*\), a *subsequence* preserves relative order but need not be contiguous. Let \(s(w)\) count the distinct shortest binary words that are **not** subsequences of \(w\). This definition uses the fixed ambient alphabet even for constant and empty source words.

For every integer \(n\ge0\), set
\[
A_n=\sum_{w\in\Sigma^n}s(w).
\]
Then
\[
\boxed{\sum_{n\ge0}A_nz^n=\frac{2}{1-z-3z^2+z^3}.}
\]
In particular, \(A_0=2\), \(A_1=2\), \(A_2=8\), and for every \(n\ge3\),
\[
\boxed{A_n=A_{n-1}+3A_{n-2}-A_{n-3}.}
\]
The first sixteen totals, for lengths zero through fifteen, are
\[
2,\ 2,\ 8,\ 12,\ 34,\ 62,\ 152,\ 304,\ 698,\ 1458,\ 3248,\ 6924,\ 15210,\ 32734,\ 71440,\ 154432.
\]
If \(W_n\) is uniformly distributed on \(\Sigma^n\), then \(\mathbb E[s(W_n)]=A_n/2^n\). Let \(\rho=2.170086486626\ldots\) be the largest real root of \(r^3-r^2-3r+1=0\). With
\[
C=\frac{2\rho^3}{\rho^2+6\rho-3}=1.3876004818\ldots,
\]
we have the sharp asymptotic
\[
\boxed{\mathbb E[s(W_n)]=C\left(\frac{\rho}{2}\right)^n+O(0.741^n).}
\]
Thus the mean number of **shortest** missing scattered patterns grows exponentially, at base \(\rho/2=1.0850432433\ldots\), even though the shortest absent length itself grows only linearly on average.

## Assumptions and scope
The word length \(n\) is any nonnegative integer. A target is counted once, regardless of how many position selections would realize it. At length zero, both binary words of length one are shortest absent, so \(s(\varepsilon)=2\). For a constant nonempty word, exactly the other letter is a shortest absent subsequence, so \(s(w)=1\).

Define the *arch count* \(\iota(w)\) by repeatedly consuming the shortest current prefix that contains both binary letters, and stopping when the remainder is constant or empty. The standard arch-factorization theorem identifies \(\iota(w)\) with the subsequence-universality index: all binary words of length \(\iota(w)\) occur as scattered subsequences, and at least one word of length \(\iota(w)+1\) does not. Consequently all shortest absent subsequences have exactly length \(\iota(w)+1\).

## Proof
**1. A random target converts an absent-word count to a weighted probability.** Let \(W\) be an independent fair-bit word of length \(n\). Independently choose an infinite sequence \(U\) of fair bits, and greedily match the longest possible prefix of \(U\) against successive letters of \(W\). Let \(J\) be the number of matched target letters, and let \(K=\iota(W)\) be the number of completed binary arches.

Since every binary target word of length \(K\) embeds in \(W\), the greedy matcher always finds at least \(K\) target letters: \(J\ge K\). The first \(K+1\) bits of \(U\) form a shortest absent subsequence exactly when \(J=K\). Conditional on \(W=w\), this event has probability \(s(w)/2^{K+1}\). Hence, for every \(n\ge0\),
\[
\mathbb E[s(W)]=2\,\mathbb E_{W,U}\!\left[2^K\,\mathbf1_{\{J=K\}}\right].\tag{1}
\]
This also holds when \(K=0\).

**2. A weighted three-phase process.** Process source letters one at a time and let \(h=J-K\) be the nonnegative *surplus*. Record one of three phases: \(F\), when a new arch has not yet seen any letter; \(M\), when an arch has seen a letter \(c\) and the pending target bit equals \(c\); and \(N\), when the pending target bit differs from \(c\). At a matched target bit, the next target bit is freshly independent and fair.

Multiply each transition probability by \(2\) whenever it completes an arch; the product of transition weights along a path is its original probability times \(2^K\). The entire transition table is

| Phase transition | Change in surplus \(h\) | Weighted probability |
| --- | ---: | ---: |
| \(F\to M\) | \(+1\) | \(1/4\) |
| \(F\to N\), source matches target | \(+1\) | \(1/4\) |
| \(F\to N\), source misses target | \(0\) | \(1/2\) |
| \(M\to F\), arch completed | \(-1\) | \(1\) |
| \(M\to M\) | \(+1\) | \(1/4\) |
| \(M\to N\) | \(+1\) | \(1/4\) |
| \(N\to F\), arch completed | \(0\) | \(1\) |
| \(N\to N\) | \(0\) | \(1/2\) |

For example, \(M\to F\) requires the next source letter to differ from \(c\), so it has ordinary probability \(1/2\) and gains the arch-completion factor \(2\), giving weight one. Every row's weights sum to either \(1\) (from \(F\)) or \(3/2\) (from \(M,N\)), as permitted for the tilted measure.

**3. Exact zero-surplus paths.** The only step decreasing \(h\) is \(M\to F\), and every entry to phase \(M\) comes from either \(F\to M\) or \(M\to M\), each increasing \(h\) by one. Therefore the surplus measured at successive visits to \(F\) or \(N\) never decreases. A path that starts at \((F,0)\) and finishes with surplus zero cannot contain any positive-surplus transition other than a two-step excursion
\[
F\longrightarrow M\longrightarrow F
\]
with its immediate compensating decrease. In particular, no such path can finish in \(M\). All admissible zero-surplus paths are thus described by the following *exact* two-state weighted transitions:
\[
F\xrightarrow[\text{one letter}]{1/2}N,\qquad
N\xrightarrow[\text{one letter}]{1/2}N,\qquad
N\xrightarrow[\text{one letter}]{1}F,\qquad
F\xrightarrow[\text{two letters}]{1/4}F.
\]
The last arrow represents the indivisible \(F\to M\to F\) excursion. The claim is bijective: conversely, all paths in this reduced system keep surplus zero at the selected state boundaries and therefore contribute to (1).

**4. Exact generating function.** Let \(f(z)\) and \(g(z)\) be the generating functions for weighted zero-surplus paths beginning in \(F\) and \(N\), respectively, with either ending state permitted and the empty path counted with weight one. First-step decomposition gives
\[
f(z)=1+\frac z2g(z)+\frac{z^2}{4}f(z),\qquad
g(z)=1+\frac z2g(z)+zf(z).
\]
Eliminating \(g\) yields
\[
f(z)=\frac{1}{1-z/2-3z^2/4+z^3/8}.
\]
By (1), \(2[z^n]f(z)\) is the average \(\mathbb E[s(W_n)]\). Multiplying this coefficient by \(2^n\) gives \(A_n\), hence
\[
\sum_{n\ge0}A_nz^n=2f(2z)=\frac{2}{1-z-3z^2+z^3},
\]
as asserted.

**5. Leading asymptotic and controlled remainder.** The denominator has three distinct real reciprocal roots. The roots of its characteristic polynomial \(r^3-r^2-3r+1\) are approximately \(2.17008649\), \(-1.48119430\), and \(0.31110782\). Partial fractions therefore give
\[
A_n=C\rho^n+O(1.482^n),\qquad
C=\frac{2\rho^3}{\rho^2+6\rho-3},
\]
with the displayed explicit positive leading constant. Division by \(2^n\) yields the stated expected-value formula and its \(O(0.741^n)\) remainder. These arguments hold for all integer lengths, without extrapolation from samples.

## Verification
The standalone `verify.py` enumerates all \(2^n\) binary words for each \(0\le n\le14\) and computes their shortest absent subsequences directly from the definition, independently of arch counting. It also checks the greedy arch index against the minimal-absence length, compares exact total counts against the cubic recurrence, and checks two independent weighted recurrences—the full three-phase surplus process and its zero-surplus two-state reduction—against the claimed rational generating function for all \(0\le n\le100\). Run `python3 verify.py` with Python 3 (standard library only). The observed success marker is `ALL_CHECKS_PASS direct_all_words_n=0..14 recurrence_n=0..100 three_state_n=0..100 safe_paths_n=0..100`.

The enumerations and coefficient checks test boundary conventions and finite consequences; the all-length conclusion follows from the preceding probabilistic-path bijection and algebraic calculation.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer, *Absent Subsequences in Words* (arXiv:2108.13968, first public 2021-08-31), establish the arch-factorization and shortest-absent-subsequence setting used here. Their inspected treatment provides structural descriptions and algorithms for a given word, not the present average over every binary word of each length. Fleischmann et al., *m-Nearly k-Universal Words — Investigating Simon Congruence* (arXiv:2202.07981, 2022), examine words with specified numbers of missing length-\(k\) subsequences but do not provide the all-length expected shortest-absence count derived here. Related results on the distribution of the binary universality index and on fixed-length maximal shortest-absent counts supply different marginals or extremal values and do not imply the present weighted average: the count \(s(w)\) is not determined by \(\iota(w)\). For example, \(s(0011)=1\) but \(s(0111)=2\), while both words have universality index one.

Biers-Ariel, Godbole, and Kelley, *Expected number of distinct subsequences in random strings* (arXiv:1704.08661), study **present** subsequences of arbitrary lengths rather than the shortest **absent** ones. These distinctions were checked by comparing mathematical quantities, not merely article titles. An equivalent expression under a different decomposition in less accessible literature remains possible.

## Limitations
This theorem assumes a fixed fair binary source and counts only distinct shortest *absent scattered subsequences*. It does not determine the full distribution or variance of this random count, minimal absent subsequences of all lengths, nonuniform sources, or alphabets of size greater than two. The derivation itself does not establish that no earlier author obtained an equivalent generating function; the originality assessment is limited by searchable and inspected literature. No independent audit or external mathematical validation is asserted.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, 31 August 2021, https://arxiv.org/abs/2108.13968 ; subsequent *Fundamenta Informaticae* 189 (2023), 199–240.
2. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1, 16 February 2022, https://arxiv.org/abs/2202.07981.
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *α-β-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v1, 25 June 2023, https://arxiv.org/abs/2306.14192.
4. N. Biers-Ariel, A. P. Godbole, S. Kelley, *Expected Number of Distinct Subsequences in Random Strings*, arXiv:1704.08661v1, 27 April 2017, https://arxiv.org/abs/1704.08661.
