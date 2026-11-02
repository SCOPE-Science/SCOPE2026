# Scattered-subsequence universality of paperfolding sixteen-block skeletons

## Finding

For a binary word \(w\), let \(\iota(w)\) be the largest integer \(r\) such that every binary word of length \(r\) occurs as a **scattered subsequence** of \(w\). Let \(\operatorname{SAS}(w)\) denote its set of shortest absent scattered subsequences.

**Theorem.** Put
\[
B(x,y)=1101100\,x\,1100100\,y\qquad(x,y\in\{0,1\}).
\]
For every integer \(q\ge1\), choose arbitrary \(x_1,\ldots,x_q\in\{0,1\}\) and \(y_1,\ldots,y_{q-1}\in\{0,1\}\). Set \(y_q=1\) and
\[
W=B(x_1,y_1)\cdots B(x_q,y_q).
\]
Then
\[
\boxed{\iota(W)=6q,\qquad |\operatorname{SAS}(W)|=2^{q+1}.}
\]
More precisely, there are exactly \(2^q\) distinct binary words of length \(6q\) whose **leftmost greedy subsequence embedding** ends at the final position \(16q\). The shortest absent words are precisely these \(2^q\) words followed by an arbitrary binary letter. This assertion is uniform in all \(2q-1\) free block bits.

**Paperfolding consequence.** Let the regular binary paperfolding sequence in the \(1\)-first convention have \(f(n)=1\) when the odd part of \(n\) is \(1\pmod4\), and \(f(n)=0\) when it is \(3\pmod4\), for \(n\ge1\). Write \(P_k=f(1)\cdots f(2^k)\). For every integer \(k\ge4\),
\[
\boxed{\iota(P_k)=3\cdot2^{k-3},\qquad |\operatorname{SAS}(P_k)|=2^{2^{k-4}+1}.}
\]
Complementing every letter gives the corresponding statement in the opposite paperfolding convention.

## Assumptions and scope

All positions are one-based in the mathematical proof. A scattered subsequence preserves letter order but need not use adjacent positions. Its greedy embedding chooses each matching letter at the earliest available position following the previous match. The endpoint is the position of its final matched letter; for an empty input it is zero. We use an infinite continuation of the specified block skeleton solely to define greedy transitions crossing a block boundary; for every assertion about \(W\), the final endpoint must lie at or before \(16q\). All exponents and counts are exact integers. The theorem applies to every \(q\ge1\) and every allowed assignment of the free bits, not just powers of two.

## Proof

**1. Greedy-transition convention.** For an infinite binary word \(F\) extending the block concatenation, define \(\delta(p,a)\), for \(a\in\{0,1\}\), as the least position \(t>p\) with \(F[t]=a\); extend \(\delta(p,u)\) to words \(u\) by composition from left to right. Whenever both are defined, \(\delta(p,u)\) is nondecreasing in \(p\). A binary word is a subsequence of a finite prefix of length \(N\) if and only if its greedy endpoint is at most \(N\).

**2. Exact six-step local lemma.** Let the infinite continuation be a concatenation of blocks \(B(x_j,y_j)\) with arbitrary bits. Define \(e_0=0\) and, for \(j\ge1\),
\[
e_j=16j+1-y_j.
\]
The previous-block bit \(y_{j-1}\) determines whether \(e_{j-1}=16(j-1)\) or \(16(j-1)+1\). For each \(j\ge1\), among all \(64\) inputs \(u\in\{0,1\}^6\) from start \(e_{j-1}\), precisely two have greedy endpoint \(e_j\), none ends after \(e_j\), and every other endpoint is at most \(16j-2\). Moreover, for \(j\ge2\), every length-six input beginning from position \(16(j-1)-2\) ends at or before \(16j-3\). The same first claim holds for \(j=1\) from the initial position zero.

Here is an exhaustive **finite proof** of this local lemma, reducible to the eight choices of three bits, independently of \(j\). A complete block is \(1101100x1100100y\); only the eighth and sixteenth letters vary, and the next block always begins with \(1\). For the initial state zero, enumerate the \(64\) inputs for each of the four \((x,y)\) choices. Their maximum endpoint is \(16+(1-y)\), reached twice; their second-largest endpoint is \(14\). For the subsequent states, enumerate the eight \((y_{j-1},x_j,y_j)\) possibilities. After shifting the block start to position \(16\), the initial state is either \(16\) or \(17\). The maximum endpoint is \(32+(1-y_j)\), reached twice, while the second-largest is \(30\). Starting instead at position \(14\), the largest endpoint after six letters is \(29\). These assertions hold for each of the eight cases; no more than the previous block's final letter, the current block, and the next block's first letter are ever required. The standalone `checker.py` enumerates each length-six input and verifies all twelve finite cases directly. This is an exhaustive \(4+8\) finite verification of a bounded lemma, **not** extrapolation from finitely many ranks.

For clarity, the normalized local table is

| initial-state class | current \(x\) | current \(y\) | largest endpoint relative to next boundary | number attaining it | largest other endpoint relative to next boundary | maximum from prior low state |
|---|---|---|---:|---:|---:|---:|
| \(16\) or \(17\) | \(0\) or \(1\) | \(0\) | \(+1\) | 2 | \(-2\) | \(-3\) |
| \(16\) or \(17\) | \(0\) or \(1\) | \(1\) | \(0\) | 2 | \(-2\) | \(-3\) |

Both initial-state choices and both eighth-letter choices were exhaustively checked separately, rather than inferred from this compressed display.

**3. Induction over blocks.** Let \(D_j(p)\) be the number of binary length-\(6j\) inputs whose greedy embedding in the continuation ends at \(p\). We claim, for each \(j\ge1\), that \(D_j(e_j)=2^j\), that no state exceeds \(e_j\), and that every other state is at most \(16j-2\). The initial \(j=1\) case is exactly the initial row of the local lemma. Assume this for \(j-1\). Every word reaching the unique extreme endpoint \(e_{j-1}\) has exactly two six-letter extensions reaching \(e_j\). Every other such extension ends by \(16j-2\). All inputs reaching a nonextreme position \(p\le16(j-1)-2\) remain at most \(16j-3\) after another six letters, by the monotonicity of \(\delta\) and the local low-state bound. Thus there is no catch-up from a nonextreme state, and the extreme-path count doubles: \(D_j(e_j)=2D_{j-1}(e_{j-1})=2^j\). This proves the invariant for every \(j\).

**4. Universality and exact missing count.** For the finite word \(W\) with \(y_q=1\), the greedy maximum after \(6q\) input letters is \(e_q=16q\). Hence every length-\(6q\) binary word is a subsequence, so \(\iota(W)\ge6q\). Exactly \(2^q\) words of length \(6q\) end greedily at \(16q\). Every other word of this length ends by \(16q-2\). The last two letters of \(W\) are \(01\), so those other words can each be extended by either alphabet letter and remain subsequences. By contrast, neither extension of any greedily terminal word can be embedded: both possible next symbols lie strictly beyond the end of \(W\). The two families are disjoint and together contain precisely \(2^{q+1}\) absent words of length \(6q+1\). Thus \(\iota(W)=6q\), and these are exactly its shortest absent subsequences.

**5. Paperfolding specialization.** Every contiguous block of sixteen letters of the \(1\)-first regular paperfolding word has the form \(1101100x1100100y\), since the odd-part rule fixes all positions within the block except the eighth and sixteenth. In the prefix of length \(2^k\) with \(k\ge4\), the number of blocks is \(q=2^{k-4}\), and the last bit is \(f(2^k)=1\). Therefore the general theorem applies and gives the displayed dyadic formulas.

## Verification

Run `python3 checker.py` with Python 3. It independently enumerates all sixty-four inputs in each of the four initial and eight transition cases, including maximal and runner-up endpoints and the low-start upper bound. Separately it evaluates the greedy subsequence automaton for paperfolding dyadic prefixes of lengths \(16\) through \(1024\), and exhaustively checks all block assignments up to \(q=5\). The checker prints `ALL CHECKS PASSED`. No external libraries or unavailable files are required.

The all-\(q\) proof depends on the explicitly enumerated *local* lemma plus induction; the finite-rank tests are independent checks, not the reason for universal quantification.

## Relationship to prior work

The paperfolding sequence and its arithmetic/Toeplitz descriptions are classical. Madill and Rampersad analyze **Abelian complexity of contiguous factors** of the paperfolding word, not the exact counts of shortest absent scattered subsequences in its finite dyadic prefixes. Kosche, Koß, Manea and Siemer develop **general absent-subsequence and arch-factorization theory**, including algorithms and extremal constructions; those general statements do not directly state the uniform \(16\)-block theorem or the exact dyadic paperfolding formula. The present claim is restricted to the explicit skeleton and its paperfolding instance, without claiming a new general subsequence-universality algorithm.

## Limitations

The universal skeleton claim requires the exact fixed fourteen-bit positions within each block and the final block letter \(1\). It does not provide a complete description of shortest absent subsequences for arbitrary paperfolding prefix lengths, nor assert the same formulas for arbitrary Toeplitz words. The finite checker is not an independent mathematical review. The historical originality comparison does not exclude unpublished or unindexed results.

## References

- B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856, first publicly available 2012-08-14, https://arxiv.org/abs/1208.2856 .
- M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public preprint 2021-08-31, https://arxiv.org/abs/2108.13968 .
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003 (standard background reference; not used for an unverified theorem statement).
