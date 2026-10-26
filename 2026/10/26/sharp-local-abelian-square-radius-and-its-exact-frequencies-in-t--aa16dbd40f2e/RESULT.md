# Sharp local abelian-square radius and its exact frequencies in the Rudin–Shapiro word

## Finding
Let \(r=r_0r_1\cdots\) be the binary Rudin–Shapiro word, indexed from zero, with \(r_n\) the parity of the number of occurrences of `11` in the base-two expansion of \(n\). For each \(i\ge0\), let \(a(i)\) be the least positive integer \(m\) such that the adjacent blocks \(r[i..i+m-1]\) and \(r[i+m..i+2m-1]\) have equal numbers of zeros and ones (an *abelian square* of root length \(m\) at \(i\)).

For every \(i\ge0\), the value \(a(i)\) exists, belongs to \(\{1,2,3,4,8,11,12,13\}\), and is at most \(13\). The bound \(13\) is attained and is sharp. Moreover, the sets \(\{i\ge0:a(i)=m\}\) have natural densities given by the following exact table:

| Minimal root length \(m\) | Density |
| ---: | ---: |
| \(1\) | \(1/2\) |
| \(2\) | \(1/8\) |
| \(3\) | \(9/32\) |
| \(4\) | \(1/32\) |
| \(8\) | \(1/64\) |
| \(11\) | \(1/64\) |
| \(12\) | \(1/64\) |
| \(13\) | \(1/64\) |

In particular, exactly a density \(1/64\) of starting positions require root length \(13\). The two possible length-\(26\) factors that require root length \(13\) are `01000011101111011010001110` and `10111100010000100101110001`. These are factors of the infinite word, not merely observed prefixes.

## Assumptions and scope
The binary word is the one-sided standard Rudin–Shapiro fixed point defined equivalently by the four-symbol substitution \(\rho(0)=01\), \(\rho(1)=02\), \(\rho(2)=31\), \(\rho(3)=32\), starting with \(0\), followed by the letter coding \(\tau(j)=\lfloor j/2\rfloor\). Root length is strictly positive; the two blocks are adjacent, have *exactly* the same length, and need only agree in Parikh counts, not symbol by symbol. Natural density means \(\lim_{N\to\infty}N^{-1}|\{0\le i<N:a(i)=m\}|\).

## Proof
**Complete language certificate.** Let \(u=\rho^\omega(0)\) be the four-letter fixed point. Its complete set of adjacent letter pairs is
\[
S=\{01,02,10,13,20,23,31,32\}.
\]
Indeed, starting from the pair `01` in \(\rho(0)\), close under (i) the pair constituting each substituted letter and (ii) the pair formed by the last letter of \(\rho(a)\) and the first letter of \(\rho(b)\), for each currently present pair \(ab\). The closure stabilizes at exactly \(S\). Every pair produced at a finite closure stage occurs in an iterate of \(0\); no other pair can arise under the substitution. Hence each of the eight pairs occurs in \(u\).

Take any starting position \(i=32j+t\), where \(j\ge0\) and \(0\le t<32\). Since the block length \(26\) does not exceed \(32\), the factor \(r[i..i+25]\) is exactly the length-\(26\) window at offset \(t\) in
\[
\tau\bigl(\rho^5(u_j)\rho^5(u_{j+1})\bigr).
\]
Conversely every choice \(u_ju_{j+1}\in S\) and \(0\le t<32\) occurs at some position. Thus the entire length-\(26\) factor language is given by *exactly* the \(8\cdot32=256\) specified window templates (with possible repetitions). There are \(200\) distinct binary length-\(26\) factors.

For a template window \(w=w_0\cdots w_{25}\), define \(s(0)=0\), \(s(t+1)=s(t)+w_t\). The first abelian-square root length is the least \(m\in\{1,\ldots,13\}\) satisfying
\[
2s(m)=s(2m).
\]
The exhaustive, small integer certificate `templates.csv`, reproduced by `verify.py`, evaluates all \(256\) templates without omitting any source pair or offset. For \(m=1,2,3,4,8,11,12,13\) respectively, the template counts are
\[
128,\ 32,\ 72,\ 8,\ 4,\ 4,\ 4,\ 4;
\]
all other root-length counts are zero. Every template satisfies at least one of these tests. Exactly four templates have minimum \(13\): \((a,b,t)=(1,0,5),(1,3,5),(2,0,5),(2,3,5)\). This proves the global bound, its sharpness, the possible values, and the asserted exceptional factor strings. This is a finite proof of a universal infinite-word assertion because the preceding block decomposition proves template exhaustion.

**Exact densities.** The substitution is primitive: each \(\rho^3(a)\) contains all four source letters, for every \(a\in\{0,1,2,3\}\). The unique invariant letter-frequency vector is \((1/4,1/4,1/4,1/4)\). The adjacent pair frequencies are also uniformly \(1/8\) on \(S\). To see this directly, a substituted adjacent pair begins either inside an image \(\rho(a)\) (even index) or across the images of two adjacent letters \(a,b\) (odd index). The four internal pairs `01`, `02`, `31`, `32` each arise from exactly one source letter, hence have frequency \((1/2)(1/4)=1/8\). Each of the remaining four cross-image pairs `10`, `13`, `20`, `23` has exactly two preimage pairs in \(S\). A constant pair-frequency vector \(1/8\) solves the resulting recurrence for the latter four. The recurrence has a unique solution: its linear part is one half a column-stochastic operator and hence has operator norm at most \(1/2\) on the relevant \(\ell_1\) space. Thus all eight pair frequencies are \(1/8\).

Every length-\(26\) window has a uniquely determined offset modulo \(32\) in the canonical substituted block decomposition. For fixed \((a,b,t)\), its occurrence as an *aligned template* has density \((1/8)(1/32)=1/256\). Summing the eight template-count entries \(128,32,72,8,4,4,4,4\), each divided by \(256\), proves every density in the table. Primitivity guarantees the needed limits exist.

## Verification
Run `python3 verify.py` with `templates.csv` in the same directory (Python 3.9+). The code regenerates all \(256\) templates from the explicit four-letter morphism, independently computes each minimum root length by prefix sums and direct Parikh counts, confirms the exact histogram and all \(200\) distinct factors, and checks the two sharp witnesses. It also generates \(65{,}536\) Rudin–Shapiro bits from the independent binary recurrence \(r_{2n}=r_n\), \(r_{2n+1}=r_n\oplus(n\bmod2)\) and compares the complete observed length-\(26\) factor set to the mathematically exhaustive template set. No external data or third-party packages are needed.

## Relationship to prior work
Schaeffer and Shallit (2015 preprint, 2016 journal publication) investigate several other factor predicates in automatic words, including the Rudin–Shapiro word; their listed classes do not include abelian squares. Lü, Chen, Wen, and Wu (2016) determine properties of Rudin–Shapiro *abelian factor complexity*, which counts Parikh classes of factors of a given length, not whether two *adjacent* factors have identical Parikh vectors at a fixed position. Fici, Mignosi, and Shallit (2017) establish abelian-square-richness results primarily for Thue–Morse and Sturmian words, a different invariant from the minimum root length at each Rudin–Shapiro position. Earlier exact Rudin–Shapiro factor-language calculations have also used the eight-source-pair substitution cover. The present result does not claim that general enumeration mechanism as new: it determines the previously unlisted *minimum adjacent abelian-square root* at every position, its sharp maximum, and its exact natural-density law. These are neither a restatement of global complexity nor a corollary of the cited factor predicates.

## Limitations
This theorem concerns the standard binary Rudin–Shapiro word and *two-block abelian squares* only; it makes no claim for other automatic sequences, higher-order abelian powers, or all abelian-square root lengths that may occur at a position. The integer certificate is complete because of the proven block-template reduction, not because a long finite prefix alone guarantees an infinite assertion. The proposed priority status remains subject to independent scholarly review; an unindexed equivalent formula cannot be ruled out by search alone.

## References
- L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (first submitted 2015-08-09); *Electronic Journal of Combinatorics* 23(1) (2016), P1.25, DOI 10.37236/5752.
- X. Lü, J. Chen, Z. Wen, and W. Wu, *On the abelian complexity of the Rudin–Shapiro sequence*, arXiv:1606.06935 (2016), especially the introduction, Theorem A, and the substitution representation.
- G. Fici, F. Mignosi, and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948 (2017), *Theoretical Computer Science* 684, 29–42, DOI 10.1016/j.tcs.2017.02.012.
