# First differing optimal circular attractors among binary de Bruijn cycles of power-of-two order

## Finding
A **circular string attractor** of a cyclic word is a set of positions such that every nonempty circular factor has at least one occurrence intersecting the set. Its minimum cardinality is denoted \(\gamma_{\mathrm{circ}}\). A binary de Bruijn cycle of order \(k\) contains every binary word of length \(k\) exactly once as a circular factor; its length is \(2^k\).

**Theorem.** At orders \(k=1,2,4\), every binary de Bruijn cycle has the information-theoretically minimal circular attractor size \(\lceil 2^k/k\rceil\). At order \(k=8\), this is no longer uniform: there are explicit binary de Bruijn cycles \(U,V\), both of length \(256\), satisfying
\[
\gamma_{\mathrm{circ}}(U)=32,\qquad \gamma_{\mathrm{circ}}(V)=33.
\]
Thus \(8\) is the first power-of-two order at which binary de Bruijn cycles with the same alphabet and order have different optimal circular attractor sizes, and the length-eight-window covering bound can be strict.

The cycles are specified in hexadecimal (exactly \(64\) hex digits, preserving leading zero bits to form length \(256\) words; position \(0\) is the leftmost bit):

- \(U\): `59a674386baa7f818d8939eb07cc2821376d4792d15bc5f652af72e3bf488c80`
- \(V\): `614087653eb755de5c70d3637fb6bdc98ac17c488fce9667a139a92a2d190780`

The witness sets, with zero-based indices modulo \(256\), are
\[
P_U=\{3+8j:0\le j<32\},\quad
P_V=\{7+8j:0\le j<32\}\cup\{40\}.
\]

## Assumptions and scope
All positions and occurrences are cyclic, and every circular factor is taken with length between \(1\) and the cycle length inclusive. A factor starting at position \(i\), of length \(t\), occupies residues \(i,i+1,\ldots,i+t-1\) modulo the cycle length. A set is an attractor if **each distinct factor** has **some** occurrence meeting that set; the same occurrence need not be used for other factors. This is the circular analogue of the string-attractor definition of Mantaci et al. and is different from the sharp \(k\)-attractor, which only requires factors of length exactly \(k\).

Only the power-of-two orders \(1,2,4,8\) are compared, not all orders below \(8\). The theorem does not assert the worst possible circular-attractor size among all order-eight cycles, nor an analogous infinite-family separation.

## Proof
**General lower bound.** An order-\(k\) de Bruijn cycle contains \(2^k\) distinct length-\(k\) circular factors, each with exactly one starting position. One selected position lies in exactly \(k\) of their occurrences. Hence every attractor contains at least \(\lceil 2^k/k\rceil\) positions.

**Rigidity at equality.** Suppose \(k\mid2^k\) and an attractor has exactly \(2^k/k\) positions. Its selected positions cover all \(2^k\) unique \(k\)-factor occurrences with total capacity exactly \(2^k\), so no \(k\)-factor occurrence contains two selected positions. The cyclic distance between consecutive selected positions must therefore be at least \(k\). These distances sum to \(2^k\), so they are all exactly \(k\). Consequently, every attractor meeting the lower bound is one of the \(k\) residue-class sets \(\{r+kj\}\), where \(0\le r<k\).

**The two order-eight certificates.** Directly taking all \(256\) cyclic length-eight windows of each displayed word gives all \(256\) distinct binary eight-letter words; hence both are de Bruijn cycles. For \(U\), the residue-class set \(P_U\) covers every circular factor of lengths \(1\) through \(8\). It also covers all longer factors: any occurrence of a longer factor contains an occurrence of a length-eight factor, and every such length-eight window meets \(P_U\). Therefore \(\gamma_{\mathrm{circ}}(U)=32\).

For \(V\), every one of the eight possible residue-class sets of size \(32\) fails. The following table supplies a missed length-seven factor, with its **two and only two** starting positions, for each residue \(r\). Neither of the two cyclic intervals meets any position congruent to \(r\) modulo \(8\).

| Residue \(r\) | Missed seven-bit factor | Both starts (zero-based) |
|---:|:---:|:---:|
| 0 | `0000111` | 17, 241 |
| 1 | `1000010` | 2, 194 |
| 2 | `0000101` | 3, 139 |
| 3 | `0011011` | 84, 92 |
| 4 | `0001000` | 13, 157 |
| 5 | `1101100` | 22, 86 |
| 6 | `1011111` | 95, 143 |
| 7 | `1011011` | 40, 104 |

This proves \(\gamma_{\mathrm{circ}}(V)>32\). To attain \(33\), take all positions congruent to \(7\) modulo \(8\), and add position \(40\). Exhaustively checking circular factors of lengths \(1\) through \(7\) shows that the residue-seven set alone misses exactly the factor `1011011`, and that the added position meets its occurrence starting at \(40\). Every length-eight window already meets the residue-seven set, so every factor of length at least eight is covered. Thus \(\gamma_{\mathrm{circ}}(V)=33\).

**Lower power-of-two orders.** At \(k=1\) the unique binary cycle has both letters and needs both positions. At \(k=2\), the unique binary cycle is a rotation of `0011` and has a two-position attractor. For \(k=4\), the following exhaustive finite enumeration proves the assertion. Each de Bruijn necklace has exactly one occurrence of `0000` and exactly eight ones. Rotate its unique occurrence of `0000` to the start, then enumerate the \(\binom{12}{8}=495\) possible placements of the eight ones in the remaining twelve positions. Exactly sixteen pass the condition that all sixteen circular four-bit windows are distinct. For each of those sixteen, at least one of the four residue-class sets modulo four covers every factor of lengths \(1\) through \(4\). Their numbers of valid residue classes have histogram \(2\mapsto4\), \(3\mapsto8\), \(4\mapsto4\). The witness condition extends automatically to factors longer than four. Together with the lower bound, all order-four cycles have optimum four. These steps are reproduced exhaustively by the enclosed standalone verifier, with the full finite domain and checks explicit in its loops.

## Verification
Run `python3 verify.py` beside this file. The script uses the standard library alone, expands the exact hexadecimal inputs to \(256\) bits, tests all \(256\) cyclic eight-bit windows, checks every distinct factor of lengths \(1\) through \(8\) against each claimed attractor, and checks each of the eight obstruction rows including the exact two occurrence starts. It also enumerates all \(495\) canonical balanced order-four candidates, selects the \(16\) de Bruijn cycles, and checks their residue-class attractors. `verification_output.txt` contains the reproduced output. Every finite assertion used above is tested on the same explicit witness data; no random sampling enters the proof.

## Relationship to prior work
Mantaci, Restivo, Romana, Rosone, and Sciortino (2021) introduced circular string attractors and established general asymptotic bounds for attractors of de Bruijn words, particularly their linearizations. Their Proposition 41 does not give exact circular minima for specific order-eight necklaces. Whittington (2024), Section 5, explicitly distinguishes sharp attractors from attractors covering shorter factors, and asks how optimal attractors vary with the chosen de Bruijn sequence; its theorem for prime-order Lyndon cycles does not cover the composite order eight. Béal, Crochemore, and Romana (first posted September 10, 2025) give checking and greedy-generation algorithms and report an attractor of size \(33\) for a particular **linear** binary de Bruijn word of order eight. That is an algorithmic output and does not establish either of the two exact **circular** optima exhibited here, nor a strict separation between them. The present claim concerns the circular quantity and distinguishes an optimality proof from a greedy output.

## Limitations
The lower-bound obstruction is finite, at a fixed order and binary alphabet. It does not prove that some linear unfolding requires more than the natural rounded linear-window bound, nor answer Whittington's broader existence conjecture for a suitably chosen de Bruijn sequence. There is no claim of asymptotic separation. Exhaustive verification at orders one, two, and four proves the stated bounded comparison, not a theorem about arbitrary lower orders. Earlier unindexed or differently formulated statements about circular \(k\)-attractors could affect priority; independent scientific review remains outstanding.

## References
1. M.-P. Béal, M. Crochemore, G. Romana, *Checking and producing word attractors*, arXiv:2509.08503, initially posted 2025-09-10, revised 2026-10-09. https://arxiv.org/html/2509.08503v2
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science (2021). https://doi.org/10.1016/j.tcs.2020.11.006 ; open manuscript https://arpi.unipi.it/bitstream/11568/1062328/1/MRRRS_TCS2021.pdf
3. P. Whittington, *Online String Attractors*, arXiv:2407.15599, 2024-07-22. https://arxiv.org/pdf/2407.15599
