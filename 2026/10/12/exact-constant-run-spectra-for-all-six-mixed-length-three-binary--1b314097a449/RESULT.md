# Exact constant-run spectra for all six mixed length-three binary block-counting words

## Finding
For a binary word \(w\) of length three containing both symbols, let \(a_w(n)\) be the parity of the number of overlapping occurrences of \(w\) in the usual binary expansion of \(n\), with \(0\) represented by `0` and with no leading zeros. A *maximal constant run* is a maximal interval of consecutive indices on which \(a_w\) is constant. The exact spectra of maximal-run lengths are:

| \(w\) | Every attainable run length | Exceptional origin-only length |
|:--|:--|:--|
| `001` | \(\{1,3,5,6,7,8,9\}\) | \(9\) |
| `110` | \(\{1,3,5,6,7,8\}\) | none |
| `010` | \(\{1,2,4,5,6,7,10\}\) | \(10\) |
| `101` | \(\{1,2,4,5,6,7\}\) | none |
| `011` | \(\{1,2,3,4,5,7,8,11\}\) | \(11\) |
| `100` | \(\{1,2,3,4,5,7,8\}\) | none |

Each origin-only length occurs in precisely the run starting at index \(0\); every other listed length occurs with positive limiting frequency and therefore infinitely often.

More precisely, define \(R_w(s)\) to be the length of the maximal run starting at \(s\) when \(s=0\) or \(a_w(s-1)\ne a_w(s)\), and otherwise leave it undefined. For every positive integer \(\ell\), the limit
\[
\delta_w(\ell)=\lim_{N\to\infty}\frac1N\#\{0\le s<N:R_w(s)=\ell\}
\]
exists. Its complete list of nonzero values is the following. Paired words have identical distributions; all omitted lengths (including the origin-only lengths) have density zero.

| \(w\) | \(\ell=1\) | \(\ell=2\) | \(\ell=3\) | \(\ell=4\) | \(\ell=5\) | \(\ell=6\) | \(\ell=7\) | \(\ell=8\) |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| `001`, `110` | \(3/32\) | \(0\) | \(1/32\) | \(0\) | \(1/32\) | \(1/64\) | \(1/16\) | \(1/64\) |
| `010`, `101` | \(7/32\) | \(13/64\) | \(0\) | \(5/128\) | \(3/128\) | \(1/128\) | \(1/128\) | \(0\) |
| `011`, `100` | \(3/32\) | \(7/64\) | \(3/32\) | \(3/128\) | \(5/128\) | \(0\) | \(1/128\) | \(1/128\) |

Consequently, the limiting densities of run starts in the three respective rows are \(1/4\), \(1/2\), and \(3/8\); in each case \(\sum_{\ell\ge1}\ell\delta_w(\ell)=1\).

## Assumptions and scope
The indexing starts at \(n=0\). No leading zeros are appended to the expansion, and occurrences of the tested length-three pattern overlap normally. These conventions matter at the left endpoint and give the three exceptional origin runs. All six words in the set \(\{001,010,011,100,101,110\}\) are included; the all-zero and all-one length-three patterns are not part of this theorem. Frequencies count *starting indices of maximal runs per integer index*, not frequencies normalized by the number of runs.

## Proof
**1. Binary-carry reduction.** Write \(c_w(v)\) for the parity of occurrences of \(w\) in a finite binary word \(v\), and write \(d_w(n)=a_w(n)\oplus a_w(n+1)\), where \(\oplus\) denotes addition modulo two. For every \(m=n+1\), factor \(m=q2^t\) with \(q\) odd and \(t\ge0\). If \(q\ge5\), put \(P=(q-1)/2\). The two adjacent binary expansions have the exact forms
\[
\operatorname{bin}(m-1)=\operatorname{bin}(P)\,0\,1^t,\qquad
\operatorname{bin}(m)=\operatorname{bin}(P)\,1\,0^t.
\]
Therefore
\[
d_w(m-1)=c_w(\operatorname{bin}(P)\,0\,1^t)\oplus c_w(\operatorname{bin}(P)\,1\,0^t).
\]
All length-three occurrences wholly inside the common prefix cancel. Only its last two digits and the adjoining suffix are relevant; the last two digits are determined by \(q\bmod8\). Since \(w\) contains both binary symbols, a triple wholly inside a constant suffix is never equal to \(w\). Thus the displayed parity difference is unchanged upon increasing \(t\) beyond \(4\). This proves, without an unbounded search, that \(d_w(m-1)\) depends only on \(q\bmod8\) and \(\min(t,4)\) whenever \(q\ge5\).

**2. A finite exact residue certificate.** Define \(F_w(q,t)\) as the parity difference in the preceding display for \(q\ge5\). For each \(r\in\{1,\dots,63\}\) with \(16\nmid r\), set \(t=v_2(r)\) and
\[
T_w(r)=F_w\bigl(16+((r/2^t)\bmod8),t\bigr).
\]
(The argument of \(F_w\) is always odd and at least \(17\).) For \(h\in\{1,3,5,7\}\), set \(E_w(h)=F_w(16+h,4)\). For any \(m\ge129\) with \(16\nmid m\), one has \(d_w(m-1)=T_w(m\bmod64)\). If \(16\mid m\) and its odd part is \(q\ge5\), then \(d_w(m-1)=E_w(q\bmod8)\). When \(q\) is \(1\) or \(3\), \(m\ge129\) implies \(64\mid m\); direct substitution of the binary strings \(1^t\) versus \(10^t\), or \(10\,1^t\) versus \(11\,0^t\), shows the jump is again independent of \(t\ge6\). These two exceptional values are also included in the finite certificate.

At any position \(m\) divisible by \(16\), its residue modulo \(64\) restricts the odd part \(q\bmod8\) exactly as follows:
\[
\begin{array}{c|c}
m\bmod64 &\text{possible residues of }q\bmod8\\\hline
0&1,3,5,7\\
16&1,5\\
32&1,3,5,7\\
48&3,7
\end{array}
\]
Within any \(14\) consecutive values of \(m\), at most one is divisible by \(16\). For each of the \(64\) possible starting phases, insert the fixed bits \(T_w(r)\) at the ordinary positions and each allowable bit \(E_w(h)\) at the sole exceptional position; when that exceptional position is \(0\bmod64\), include the two isolated \(q=1,3\) values as well. The exhaustive rational-integer case analysis in the accompanying `verify.py` establishes the following two exact finite statements: every such \(14\)-bit window whose first bit equals \(1\) has another \(1\) within the next \(8\) positions, and the possible first-return distances are precisely the nonexceptional lengths given in the first table. In particular, *every* run beginning at an index \(s\ge128\) belongs to the listed ordinary spectrum. Direct evaluation of the first \(145\) terms establishes all complete runs starting before \(128\): the only other distances are the origin-only lengths \(9\), \(10\), and \(11\) for the specified three patterns. The terminal run in this finite check starts after index \(127\), so no early run is left unchecked. The two parts together exhaust all nonnegative starting indices.

**3. Exact limiting frequencies.** The two exceptional odd parts \(q=1,3\) occur at positions in the sparse sets \(\{2^t:t\ge0\}\) and \(\{3\cdot2^t:t\ge0\}\), which have natural density zero. Each of the \(64\) starting residues has density \(1/64\). Conditional on a divisible-by-\(16\) position in the window with residue \(0,16,32,48\pmod{64}\), the allowed odd-part residues from the last display occur with respective equal conditional weights \(1/4,1/2,1/4,1/2\). This follows by summing the exact densities of fixed \(2\)-adic valuations and odd parts modulo \(8\). Each phase thus contributes either \(1/64\), or \(1/(64\cdot2)\), or \(1/(64\cdot4)\) to the first-return-distance count. Exhaustive addition of these rational weights in `verify.py` yields exactly the second table. Strict positivity of each displayed entry proves infinite occurrence of each ordinary length. The weighted sum identity follows from the table (or from the partition into runs).

## Verification
Run `python3 verify.py` using only the Python standard library. The verifier constructs both local bit tables from the defining pattern counts, enumerates every one of the \(64\) phase classes and all relevant odd-part residues with exact rational arithmetic, checks the two sparse exceptional cases, tests the first \(145\) symbols, and independently compares direct prefixes of length \(2^{17}\). It reports `VERIFY_OK six_patterns=6 phase_classes=64 odd_residue_cases=all symbolic_window_bound=13 mixed_pattern_critical_boundary=checked direct_n=131072`. The infinite conclusion rests on the proved carry-locality and valuation-density reduction combined with the finite exhaustive certificate, not on long-prefix sampling.

## Relationship to prior work
Abram, Hu, and Li, *Block-counting sequences are not purely morphic* (arXiv:2304.14595; first public 2023-04-28), introduce and analyze the same block-counting family and its morphic and generating-function structure but do not furnish a complete maximal-constant-run spectrum or per-length run-start densities. Konieczny's *Algorithmic classification of noncorrelated binary pattern sequences* (arXiv:1905.03283) treats correlation questions, not this complete joint run-length classification. Li's *On the Orthogonality of Generalized Pattern Sequences* (arXiv:2406.16411) concerns partial-sum orthogonality and uses conventions that must not be silently substituted for the no-leading-zeros convention here. Hendel's *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern* (arXiv:2505.20547) studies the distinct all-one subfamily, not the six mixed patterns. The ordinary runs and rational frequency tables here do not follow from the statements inspected in these sources.

## Limitations
The result is specific to length-three binary patterns containing both digits; it makes no assertion about length-four patterns or general alphabets. The density is over positions starting runs and does not distinguish the symbols of successive runs. Bibliographic comparisons do not exclude an unindexed prior equivalent calculation. Scientific proof and reproducibility checks are presented without any assertion of independent validation.

## References
1. A. Abram, Y. Hu, S. Li, *Block-counting sequences are not purely morphic*, arXiv:2304.14595 (first public 2023-04-28); published in *Advances in Applied Mathematics* 155 (2024), 102673; primary MSC 68R15.
2. J. Konieczny, *Algorithmic classification of noncorrelated binary pattern sequences*, arXiv:1905.03283 (2019).
3. S. Li, *On the Orthogonality of Generalized Pattern Sequences*, arXiv:2406.16411 (2024).
4. R. J. Hendel, *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern*, arXiv:2505.20547 (2025).
