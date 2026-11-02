# Complete dyadic maximizer fibers for cototient iteration through the first three-unit jump

## Finding

Let \(\varphi\) denote Euler's totient and define the cototient iteration height
\[
C(1)=0,\qquad C(n)=1+C(n-\varphi(n))\quad(n\ge2).
\]
For \(1\le k\le19\), let \(I_k=\{n:2^{k-1}<n\le2^k\}\),
\(M_k=\max_{n\in I_k}C(n)\), and
\(E_k=\{n\in I_k:C(n)=M_k\}\).

**Exact finite classification.** The companion file `MAXIMIZERS.json` explicitly lists **every member of \(E_k\)** for each of the 19 intervals. There are exactly 123 maximizers counted across those intervals (with multiplicity across intervals impossible). In particular
\[
(M_{18},|E_{18}|)=(30,44),\qquad
(M_{19},E_{19})=(33,\{462210\}).
\]
Thus the first height jump of at least three is accompanied by a sharp change from 44 maximizing arguments to a single maximizing argument. The following table is a human-readable summary of the full listed fibers.

| \(k\) | \(M_k\) | \(|E_k|\) | \(\min E_k\) |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 1 | 4 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 4 | 10 |
| 5 | 6 | 1 | 30 |
| 6 | 7 | 5 | 42 |
| 7 | 9 | 2 | 114 |
| 8 | 10 | 9 | 186 |
| 9 | 12 | 4 | 390 |
| 10 | 14 | 2 | 798 |
| 11 | 16 | 2 | 1950 |
| 12 | 18 | 1 | 4074 |
| 13 | 20 | 2 | 7770 |
| 14 | 22 | 3 | 15810 |
| 15 | 24 | 6 | 30702 |
| 16 | 26 | 15 | 53130 |
| 17 | 28 | 18 | 105090 |
| 18 | 30 | 44 | 206910 |
| 19 | 33 | 1 | 462210 |

The complete sets, not merely their cardinalities, are certified in the companion JSON file. This is a finite theorem only for \(1\le k\le19\); no assertion about the behavior for higher scales is made.

## Proof and full-domain certificate

For each \(n\ge2\), \(1\le n-\varphi(n)<n\), so the recurrence for \(C\) is well founded and can be evaluated by induction in increasing \(n\). Two arithmetically distinct exact totient constructions provide independent checks of every input through \(N=2^{19}=524288\).

The first method initializes \(\varphi_A(n)=n\) and, when the sieve finds a prime \(p\), updates each positive multiple \(m\) by
\(\varphi_A(m)\leftarrow\varphi_A(m)-\varphi_A(m)/p\). Each prime dividing \(m\) contributes exactly its Euler factor \(1-1/p\), so the resulting array is Euler's totient. The primality test \(\varphi_A(p)=p\) before processing \(p\) is valid because all smaller primes have already acted on their multiples.

The second method independently constructs the smallest prime factor \(p\) of each composite and uses \(m=n/p\) and
\[
\varphi_B(n)=\begin{cases}
 p\varphi_B(m)&\text{if }p\mid m,\\
 (p-1)\varphi_B(m)&\text{if }p\nmid m,
\end{cases}
\quad \varphi_B(1)=1.
\]
This is the usual prime-power formula together with multiplicativity. Both arrays agree at each input \(1\le n\le N\); computing the height recurrence independently from each produces the same full array. For each \(I_k\), the verifier then takes the exact maximum and lists all integers attaining it, comparing each complete list, in order, with `MAXIMIZERS.json`. It separately checks the displayed 19 maxima, first three-unit jump, the 44 versus one extremizer counts at the last two scales, and a direct length-33 trajectory from 462210 to 1.

The certificate is exhaustive because it visits all integers from 2 through 524288 and no sampled subrange or probabilistic step is used. The code is short, uses only Python's standard library, and performs bounded integer operations. Execute `python3 verify.py` from the directory containing both `verify.py` and `MAXIMIZERS.json` to reproduce all data. The proof of the sieve and recurrence identities above explains why a successful finite computation establishes this finite classification; the program's success alone does not establish priority or a theorem for infinitely many scales.

## Previously known numerical threshold and what is added here

The **first three-unit jump, its index \(k=19\), the heights 30 and 33, and the least height-33 integer 462210 are already derivable from the earlier public OEIS table A098197**; they are **not claimed as original discoveries**. That table lists the least starting integer whose cototient trajectory has exactly \(r\) distinct entries including 0. For \(n\ge1\), that trajectory contains \(C(n)+2\) entries. Consequently its entry at index \(h+2\) is the least integer attaining height \(h\). For example, the entries at indices 32, 33, 34, 35, 36 are respectively 206910, 278850, 361410, 462210, 688722, corresponding to first heights 30 through 34. From the complete listed first-hit values, the running maximum through \(2^k\) increases at every \(k\le19\); its new maximum is therefore attained in the newest dyadic interval. This recovers the known maxima and their first three-unit jump.

**The contribution isolated here is different:** the complete argmax fibers \(E_k\), including every maximizing argument and all fiber cardinalities through the first exceptional scale. A least-first-hit table cannot by itself determine how many other integers attain the same height, or which they are. OEIS A071575 records the individual height sequence and a table of the first 10,000 arguments; that listing does not supply the complete 19-scale argmax classification. The primary 2023 paper of Ellis, Shi, Thanatipanonda and Tu defines the same height and proves in Theorem 4.8 that the heights at even positions in each dyadic interval form a consecutive set, but it does not determine the complete maximizing fibers. These are comparisons of statements, not claims that a failed web search proves global novelty.

## Scope and limits

The scope is the natural initial dyadic region through the first jump of size three in \(M_k\). The complete extremal-position classification at that boundary distinguishes an isolated maximizer at scale 19 from the 44-way tie at scale 18, and provides an exact benchmark for further studies of this arithmetic dynamical system. It does not prove an asymptotic growth law or a structural classification for all \(k\). Any unindexed full-height database or previously unpublished exhaustive census remains a priority risk. Neither a numerical certificate nor independent re-enumeration supplies external expert certification.

## References

1. Labos Elemer et al., OEIS A098197, *Smallest number with a prescribed cototient-trajectory length* (entry dated September 16, 2004; current table includes indices 1–40), https://oeis.org/A098197 and https://oeis.org/A098197/b098197.txt.
2. Benoit Cloitre et al., OEIS A071575, *Number of iterations of cototient(n) needed to reach 1*, https://oeis.org/A071575.
3. P. Ellis, J. Shi, T. A. Thanatipanonda, A. Tu, *Two Games on Arithmetic Functions: SALIQUANT and NONTOTIENT*, Discrete Mathematics Letters 12 (2023), 209–216, arXiv:2309.01231, especially Section 4 and Theorem 4.8, https://arxiv.org/pdf/2309.01231.
