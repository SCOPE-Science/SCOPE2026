# Exact common divisibility of Stern values at binary-palindromic indices

## Finding

Let Stern's diatomic sequence be defined by \(s(0)=0\), \(s(1)=1\), and, for integers \(n\ge1\),
\[
s(2n)=s(n),\qquad s(2n+1)=s(n)+s(n+1).
\]
For each integer \(\ell\ge1\), let \(\mathcal P_\ell\) consist of the integers whose canonical base-two representations are palindromes of exactly \(\ell\) digits, and define
\[
G(\ell)=\gcd\{s(n):n\in\mathcal P_\ell\}.
\]
Then
\[
(G(1),G(2),G(3),G(4),G(5),G(6),G(7))=(1,2,3,4,1,6,1),
\]
and, for **every** integer \(\ell\ge8\),
\[
\boxed{G(\ell)=\begin{cases}1,&\ell\text{ odd},\\2,&\ell\text{ even}.\end{cases}}
\]
Thus the exact common divisor stabilizes to a parity law, with genuine exceptional common divisors at lengths three, four, and six.

## Assumptions and scope

The binary expansion of every index is canonical, begins with digit one, and has no leading zeros. The gcd is positive; repeated values in the indexing set do not affect it. All statements concern every length in the indicated range, not a sample of indices or an asymptotic density. The index set has \(2^{\lceil\ell/2\rceil-1}\) elements.

## Proof

**Binary transfer recurrence.** Put \(v(n)=(s(n),s(n+1))^{\mathsf T}\) for positive integers \(n\). The defining recurrence yields
\[
v(2n)=M_0v(n),\quad v(2n+1)=M_1v(n),\qquad
M_0=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
M_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Start from \(v(1)=(1,1)^{\mathsf T}\), and apply these matrices to the succeeding bits in left-to-right order. In particular,
\[
M_0^t=\begin{pmatrix}1&0\\t&1\end{pmatrix}\qquad(t\in\mathbb Z_{\ge0}).
\]

**Four uniform palindrome witnesses.** Fix \(\ell\ge8\), and write \(t=\ell-8\). For each of the following four-bit words \(P\), form the length-\(\ell\) palindrome \(w=P0^t\operatorname{rev}(P)\). Matrix multiplication as above gives the exact values:

| First four bits \(P\) | \(s([w]_2)\) |
| --- | --- |
| `1000` | \(t+8=\ell\) |
| `1100` | \(4t+20=4\ell-12\) |
| `1010` | \(9t+30=9\ell-42\) |
| `1001` | \(16t+24=16\ell-104\) |

For reproducibility, each row can be checked by first applying its three nonleading prefix bits to \((1,1)^{\mathsf T}\), then \(M_0^t\), then the four reversed prefix bits. The first component is exactly the displayed linear polynomial. Because all four are members of the gcd's defining family,
\[
G(\ell)\mid\gcd(\ell,4\ell-12,9\ell-42,16\ell-104)
=\gcd(\ell,12,42,104)=\gcd(\ell,2).
\]
This proves \(G(\ell)=1\) for odd \(\ell\ge8\) and \(G(\ell)\in\{1,2\}\) for even \(\ell\ge8\).

**The parity obstruction at even lengths.** The recurrence also gives
\[
s(n)\equiv0\pmod2\quad\Longleftrightarrow\quad n\equiv0\pmod3
\qquad(n\in\mathbb Z_{\ge0}).
\]
Indeed the indicator of being nonzero modulo three has initial values zero at zero and one at one; checking residues modulo three shows it obeys both Stern recurrences modulo two, so induction proves the equivalence. For even \(\ell\), every \(\ell\)-bit binary palindrome represents an integer divisible by three: modulo three, \(2\equiv-1\), and digits at mirrored positions cancel in pairs. Hence every member of \(\{s(n):n\in\mathcal P_\ell\}\) is even. This forces \(G(\ell)=2\) for all even \(\ell\ge8\).

**All short lengths.** Direct use of the defining recurrence on every binary palindrome of each short length gives, in ascending index order, the following complete lists of Stern values:

| \(\ell\) | Values \(s(n)\) | Gcd |
| --- | --- | --- |
| 1 | \(1\) | \(1\) |
| 2 | \(2\) | \(2\) |
| 3 | \(3,3\) | \(3\) |
| 4 | \(4,4\) | \(4\) |
| 5 | \(5,8,8,5\) | \(1\) |
| 6 | \(6,12,12,6\) | \(6\) |
| 7 | \(7,15,21,16,16,21,15,7\) | \(1\) |

The table is exhaustive because the first \(\lceil\ell/2\rceil\) bits, starting with one, uniquely determine a binary palindrome. Combining it with the four-witness argument and parity obstruction completes the proof for all positive lengths.

## Verification

Run the accompanying self-contained Python program using `python verify.py` (Python 3 standard library only). It independently constructs all canonical binary palindromes of lengths one through twenty-two, computes each Stern value by a bit-by-bit transfer algorithm, and verifies every claimed gcd. It also checks symbolic affine transfer coefficients for all four witness families and their values at six middle-block lengths. The complete short-length value lists can be reproduced from the same recurrence. Computation confirms finite cases; the infinite statement is established by the proof above.

## Relationship to prior work

Coons and Shallit, *A Pattern Sequence Approach to Stern's Sequence* (first public arXiv version 30 April 2011), provide digit-pattern expansions and Stern identities. De Luca and De Luca, *Sturmian words and the Stern sequence* (arXiv 15 October 2014), give word representations, reversal symmetry (Proposition 5.4), a continuant representation (Proposition 6.3), and full-level value-distribution results (Section 9). These supply related methods for individual Stern values and whole levels. The invariant here instead takes the gcd over **the binary-palindromic subset at each fixed bit length**; the four uniform witnesses, exact exceptional lengths, and this gcd classification were not located in those inspected results. OEIS A002487 documents Stern's original sequence, properties, and related tables, rather than this palindromic-index gcd sequence. A search not finding a theorem is not itself proof of novelty.

## Limitations

The theorem concerns binary-palindromic indices only, and does not classify value distributions, sums, or common divisors for non-palindromic fixed-length subsets, nor establish analogous laws in other bases or for generalized Stern recurrences. The short-length enumerations are exact, but computational verification through length twenty-two does not replace the proof for unbounded length. The literature comparison cannot exclude an unindexed earlier equivalent formulation; an independent audit has not been performed.

## References

1. M. Coons and J. Shallit, *A Pattern Sequence Approach to Stern's Sequence*, arXiv:1105.0086v1 (30 April 2011); updated v2 (6 July 2011). https://arxiv.org/abs/1105.0086
2. A. de Luca and A. De Luca, *Sturmian words and the Stern sequence*, arXiv:1410.4085v1 (15 October 2014). https://arxiv.org/abs/1410.4085
3. *The On-Line Encyclopedia of Integer Sequences*, A002487, Stern's diatomic sequence. https://oeis.org/A002487
