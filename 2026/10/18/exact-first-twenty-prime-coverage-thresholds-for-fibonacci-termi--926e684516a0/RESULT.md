# Exact first-twenty prime coverage thresholds for Fibonacci terminal blocks

## Finding
For ordinary Fibonacci numbers \(F_1=F_2=1\), \(F_{k+2}=F_{k+1}+F_k\), use the unique Zeckendorf representation \(n=\sum_{k\ge2}a_kF_k\) with nonconsecutive ones, \(a_1=0\). Decompose its coefficient string from the small-weight end into **semi-proper blocks** `S=(0)` and `D=(0,1)` (the same block convention as Chang--Verwee). A terminal block word is any finite concatenation of `S` and `D`; its total digit length is \(m=\#S+2\#D\). Let \(\mathcal W_m\) be all such words of total digit length \(m\), and define its **prime coverage threshold**
\[
 C_m=\min\left\{X\in\mathbb Z_{\ge2}:\ \forall B\in\mathcal W_m\ \exists\ p\le X\text{ prime with }\text{the terminal block sequence of }p\text{ begins with }B\right\}.
\]
Every \(C_m\) exists by the fixed-terminal-block prime theorem of Chang--Verwee. The following is a complete exact census for \(1\le m\le20\). The final column identifies the single word first seen at the threshold; here `D` means `(0,1)` and `S` means `(0)`.

| \(m\) | admissible terminal words | least covering prime \(C_m\) | last new block |
|---:|---:|---:|---|
| 1 | 1 | 2 | `S` |
| 2 | 2 | 17 | `D` |
| 3 | 3 | 19 | `DS` |
| 4 | 5 | 43 | `DSS` |
| 5 | 8 | 103 | `DSSS` |
| 6 | 13 | 179 | `DSSSS` |
| 7 | 21 | 277 | `SDSDS` |
| 8 | 34 | 1009 | `DSSSSD` |
| 9 | 55 | 1033 | `DDDSD` |
| 10 | 89 | 5573 | `SDDSDSS` |
| 11 | 144 | 5573 | `SDDSDSSS` |
| 12 | 233 | 11777 | `DSSSSDDD` |
| 13 | 377 | 31907 | `DSSSSSSDSSS` |
| 14 | 610 | 45979 | `DSSSSDDDD` |
| 15 | 987 | 86837 | `SDSSSDSSSDD` |
| 16 | 1597 | 165887 | `SSDDSSSDSSDS` |
| 17 | 2584 | 386329 | `DDSSDSSSDSSSS` |
| 18 | 4181 | 797287 | `DDSSSSDSSSDSSS` |
| 19 | 6765 | 1115701 | `SSSDDDSSDSDSSS` |
| 20 | 10946 | 1803947 | `DSSDSSSSDSDSSSSS` |

In particular, all \(10,946\) admissible total-length-\(20\) words occur among the primes up to \(1,803,947\), but at least one is absent among smaller primes. The last newly covered word is `DSSDSSSSDSDSSSSS`, first represented by the prime \(1,803,947\). This is an exact finite benchmark; no unproved formula for larger lengths is asserted.

## Assumptions and scope
All integers and primes are ordinary positive integers. The Fibonacci indexing has \(F_1=F_2=1\), with the coefficient of \(F_1\) fixed to zero. Terminal classes are defined by the canonical infinite block expansion, with trailing zero blocks; thus the classification applies to every integer, including values whose finite representation ends before digit position \(m\). Coverage at length \(m\) means *every* concatenation of full blocks of total digit length \(m\), not every unconstrained binary bit string of length \(m\). A word beginning with the next block `D` cannot be truncated in the middle of that block. The claim covers exactly the twenty lengths stated.

## Proof
Let \(w_m=|\mathcal W_m|\). Splitting a word according to its first block gives \(w_0=1\), \(w_1=1\), \(w_m=w_{m-1}+w_{m-2}\) for \(m\ge2\); hence \(w_m=F_{m+1}\). In particular \(w_{20}=10,946\).

For every prime not exceeding the largest candidate bound \(1,803,947\), obtain the canonical Fibonacci digits by descending greedy subtraction from the largest Fibonacci weight. A digit \(a_k=1\) forbids \(a_{k+1}=1\). Parse the digit string from \(a_1=0\): whenever a zero is followed by one, consume `(0,1)` as `D`; otherwise consume the single digit zero as `S`. This is the semi-proper block grammar; the only possible nonzero digit is the second digit of a `D`. At each completed block boundary with total length \(m\le20\), record the prime if it is the first with that exact prefix. The algorithm does not prematurely record a prefix ending inside a `D`.

A complete Eratosthenes sieve supplies **every prime** up to \(1,803,947\). The provided program maintains a dictionary containing the least encountered prime for each terminal word at each length. Its output verifies, for every \(1\le m\le20\), that the dictionary has exactly \(F_{m+1}\) keys and that its largest recorded least prime equals the \(C_m\) in the table. No primes are skipped, and no admissible terminal word is omitted by the independently proved Fibonacci word count. For any threshold value \(C_m\), a particular recorded word first occurs at the indicated prime and does not occur at any smaller prime, proving the necessary lower bound. The completed dictionary proves the matching upper bound. Thus all table entries are exact, rather than experimental estimates.

## Verification
Run `python3 verify.py` using only the Python standard library. The checker recomputes the prime sieve, digit expansions, complete dictionaries and twenty maxima. Its expected concluding line is `VERIFY_OK`. The run enumerated all primes up to \(1,803,947\), including \(135,340\) primes through the terminal witness, and checked all \(10,946\) length-20 classes. A separate finite-word recurrence check for lengths through \(20\) matches the dictionary sizes. Computations use integer arithmetic except for no essential step; no floating point is needed.

## Relationship to prior work
Chang and Verwee, *Terminal Blocks of Primes in Pisot Numeration Systems*, arXiv:2610.10026v1 (2026-10-07), Theorem 1.6, establish the fixed-word prime asymptotic, and Section 9.2 poses the problem of uniformity over growing terminal lengths. Their theory ensures eventual coverage at each fixed length, but does not list these precise finite thresholds. Chang, *Terminal digits under Zeckendorf expansion* (2025), introduced the terminal-prime question. The present finding gives an exact, independently reproducible finite coverage frontier; it does **not** establish the shrinking-cylinder asymptotic asked in the cited open problem. No covering exact table was identified in searched mathematical records or accessible prior research claims.

## Limitations
The cutoff \(m\le20\) is a finite benchmark and does not imply asymptotic growth of \(C_m\). The exact certificate uses a complete finite sieve; it is not a formal machine-checked proof or an independent audit. An earlier unpublished computation or an exact table indexed differently remains a residual originality risk. The prime coverage function is motivated by the cited quantitative terminal-block question, but its precise finite values do not by themselves resolve that question.

## References
1. S. Chang and J. Verwee, *Terminal Blocks of Primes in Pisot Numeration Systems*, arXiv:2610.10026v1 (2026-10-07), Theorem 1.6 and Section 9.2, https://arxiv.org/html/2610.10026v1.
2. S. Chang, *Terminal digits under Zeckendorf expansion*, Mathematical Communications **30** (2025), 221–229.
