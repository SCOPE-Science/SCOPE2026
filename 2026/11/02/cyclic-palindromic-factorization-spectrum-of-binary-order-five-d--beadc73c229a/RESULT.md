# Cyclic palindromic factorization spectrum of binary order-five de Bruijn cycles

## Finding

Let \(\mathcal B_5\) be the set of binary de Bruijn cycles of order five, considered modulo rotation. Each member has length \(32\) and contains each binary word of length five exactly once as a circular factor. For a nonempty linear word \(u\), let \(\operatorname{PL}(u)\) denote the least number of nonempty contiguous palindromes whose concatenation is \(u\). For the \(r\)-th rotation \(\rho_r(W)\), define

\[
P_{\min}(W)=\min_{0\le r<32}\operatorname{PL}(\rho_r(W)),\qquad
P_{\max}(W)=\max_{0\le r<32}\operatorname{PL}(\rho_r(W)).
\]

**Theorem (complete order-five spectrum).** There are exactly \(2048\) cycles in \(\mathcal B_5\). Their optimal circular palindromic factorization lengths have the following exact distribution:

| \(P_{\min}\) | Number of cycles |
|---:|---:|
| 4 | 48 |
| 5 | 534 |
| 6 | 942 |
| 7 | 416 |
| 8 | 106 |
| 9 | 2 |

In particular, every order-five cycle admits a cut into at most nine nonempty palindrome blocks, this is sharp for exactly two cycles, and no such cycle admits a cut into three or fewer palindrome blocks. The two cycles with \(P_{\min}=9\) have canonical rotations

- `00000100111010100011011111001011`
- `00000110100111110110001010111001`

and are exchanged by reversing or complementing the cyclic word.

The **full rooted spectrum** of the \(65{,}536=2048\cdot32\) linear rotations is:

| \(\operatorname{PL}(\rho_r(W))\) | Number of rooted words |
|---:|---:|
| 4 | 384 |
| 5 | 3554 |
| 6 | 18266 |
| 7 | 29118 |
| 8 | 12138 |
| 9 | 2030 |
| 10 | 46 |

The complete **joint distribution** of optimal and worst-root factorization lengths is:

| \(P_{\min}\) | \(P_{\max}\) | Number of cycles |
|---:|---:|---:|
| 4 | 7 | 48 |
| 5 | 7 | 120 |
| 5 | 8 | 350 |
| 5 | 9 | 64 |
| 6 | 7 | 118 |
| 6 | 8 | 742 |
| 6 | 9 | 74 |
| 6 | 10 | 8 |
| 7 | 8 | 254 |
| 7 | 9 | 154 |
| 7 | 10 | 8 |
| 8 | 9 | 92 |
| 8 | 10 | 14 |
| 9 | 10 | 2 |

These are exact integer identities, not statistical estimates.

## Assumptions and scope

Symbols are the literal ordered binary alphabet \(\{0,1\}\). A cyclic word is counted once up to rotation but not up to reversal or bit complement. Every root is a complete, non-wrapping length-\(32\) traversal; palindrome blocks are ordinary contiguous *linear* factors of that root. The circular optimum is obtained by placing the cut at a block boundary, hence equals \(P_{\min}\). No palindrome may be empty. The source order and the cycle order are fixed at five.

## Proof

**1. Exhaustive feedback-table parameterization.** Regard a circular order-five window as a five-bit state \(a s\), with leading bit \(a\in\{0,1\}\) and four-bit suffix \(s\). Its successor under a cyclic shift has the form \(s f(a,s)\). In any de Bruijn cycle, these successors form a permutation on all \(32\) five-bit states. The two states \(0s\) and \(1s\) therefore have distinct successors \(s0\) and \(s1\), so their appended bits are complementary. Consequently there is a unique binary table \(g:\{0,1\}^4\to\{0,1\}\) with

\[
f(a,s)=a\oplus g(s),\qquad T_g(as)=s\,(a\oplus g(s)).
\]

Conversely \(T_g\) is a permutation for every one of the \(2^{16}\) choices of \(g\), and if the orbit of `00000` consists of all \(32\) states, then the leading state bits along that orbit give a de Bruijn cycle. Every order-five cycle contains `00000` at a unique circular position, so this is a one-to-one parameterization of cycles by the tables whose orbit is full. Testing all tables returns exactly \(2048\) accepted tables.

**2. Independent completeness control.** A de Bruijn cycle is equivalently an Euler tour of the order-four directed binary de Bruijn graph. Its \(16\) vertices are four-bit words and its \(32\) edges are five-bit words. Fix the edge `00000` first, then recursively traverse each remaining edge at most once and accept only tours returning to vertex `0000` after all edges have been used. This independent procedure returns the same \(2048\) canonically rooted strings, with no duplicates. The equality of the two sets verifies completeness independently of the feedback-table construction.

**3. Exact factorization recurrence.** For any fixed rooted word \(u=u_0\cdots u_{31}\), let \(d(0)=0\). For every \(1\le j\le32\), set

\[
d(j)=1+\min\{d(i):0\le i<j,\ u_i\cdots u_{j-1}\text{ is a palindrome}\}.
\]

Every admissible factorization of the prefix ending at \(j\) has a final palindromic factor beginning at some \(i\); removing that last factor yields a factorization of the preceding prefix. Conversely, appending any palindromic factor to an optimal prefix gives an admissible factorization. Induction on \(j\) thus proves \(d(j)=\operatorname{PL}(u_0\cdots u_{j-1})\). A separate implementation derives palindromic intervals by expanding around all centers of \(WW\), then solves the shortest-path problem between successive cut positions within each interval of length \(32\). These two algorithms agree for every root of every cycle.

**4. Finite certificate and reduction to the tables.** The attached pure-Python program `verify_circular_pal_lengths.py` implements both enumeration methods and both palindromic-length methods, independently compares their outputs for every one of the \(2048\) cycles and its \(32\) roots, and checks each integer in all three tables above. The attached C++17 program `verify_circular_pal_lengths.cpp` separately enumerates the Euler tours and computes interval dynamic programming, and verifies the same tables. Both programs terminate after finite bounded loops; successful replay of both returns `VERIFY_OK`. In particular the entries for \(P_{\min}=4\) and \(P_{\min}=9\) provide, respectively, sharp attainability and sharp nonexistence beyond the claimed boundaries. The two exact extremal strings are explicitly checked. No untested extrapolation beyond order five is used.

For a concrete four-block witness, the canonical cycle `00000100110110001110010111110101`, cut after its sixth bit, is

`001101100 | 01110 | 01011111010 | 1000001`.

All four displayed blocks are palindromes. For a nine-block witness, the first extremal representative above can be split as

`000 | 00100 | 11 | 10101 | 000 | 11 | 0111110 | 010 | 11`.

The global lower bound of nine for each of the two extremal cycles and the universal lower bound of four are guaranteed by exhaustive testing of every one of their possible cuts, not merely by these witnesses.

## Verification

Run `python3 verify_circular_pal_lengths.py`. It exhausts all \(65{,}536\) feedback tables, independently enumerates rooted Euler tours, checks every five-bit factor and compares two methods for each palindromic length. It then checks the expected spectra, joint counts and extremal representatives. Independently compile with `c++ -O2 -std=c++17 verify_circular_pal_lengths.cpp -o verify_pal`, then run `./verify_pal`. Both programs were executed successfully and reported `VERIFY_OK`. The C++ program makes no use of the Python program or data files. Their integer assertions and their covering enumeration logic, rather than a saved log, are the finite proof certificates.

## Relationship to prior work

Frid, Puzynina and Zamboni [1] define palindromic length and study bounded palindromic factorizations in infinite words. Fici, Gagie, Kärkkäinen and Kempa [2] give general algorithms for minimizing the number of palindromic factors of a linear word, including the same defining dynamic-programming recurrence, but no de Bruijn-cycle classification. Anisiu, Anisiu and Kása [3] investigate palindromic factors and palindromic-factor counts with de Bruijn constructions; counting the occurrences or distinct palindromes is different from minimizing the number of blocks in an exact factorization. The present tables concern the order-five family across all rotations. Their exhaustive computation uses established elementary definitions and algorithms; no novelty is claimed for the general dynamic programming, Euler construction or feedback encoding.

## Limitations

The exact extrema, representatives and spectra are established only for the binary order-five family. No formula for other orders, larger alphabets, or other types of factorization is proved. The enumeration is a finite computational proof with complete executable source, not a closed-form structural characterization of the individual nonextremal classes. Priority relative to unindexed historical tables or inaccessible secondary sources has not been ruled out; independent mathematical audit has not been performed.

## References

1. A. E. Frid, S. Puzynina and L. Q. Zamboni, *On minimal factorizations of words as products of palindromes*, first posted 23 October 2012, arXiv:1210.6179, https://arxiv.org/abs/1210.6179.
2. G. Fici, T. Gagie, J. Kärkkäinen and D. Kempa, *A Subquadratic Algorithm for Minimum Palindromic Factorization*, first posted 10 March 2014, arXiv:1403.2431, https://arxiv.org/abs/1403.2431.
3. M.-C. Anisiu, V. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Mathematics and Applications 17 (2006), 183–195, https://ictp.acad.ro/properties-of-palindromes-in-finite-words/.
