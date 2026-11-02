# Exact four-runs-per-level law for the binary Cantor word under the Burrows–Wheeler transform

## Finding

Define the finite binary Cantor words by \(C_0=1\) and \(C_{k+1}=\mu(C_k)\), where \(\mu(1)=101\) and \(\mu(0)=000\). List every cyclic rotation of \(C_k\) in nondecreasing lexicographic order with \(0<1\), taking its preceding character to form the circular Burrows–Wheeler transform \(\operatorname{BWT}(C_k)\). Let \(r(u)\) count maximal nonempty constant-letter runs in a finite word \(u\).

**Theorem.** For every integer \(k\ge2\),
\[
r(\operatorname{BWT}(C_k))=4k.
\]
The exceptional initial values are \(r(\operatorname{BWT}(C_0))=1\) and \(r(\operatorname{BWT}(C_1))=2\). Moreover, grouping zero-initial rotations by their exact number \(t\ge1\) of initial zeros, the corresponding contiguous BWT segment is entirely zero unless \(t=3^a\) for some \(0\le a<k\); for \(t=3^a\), it is exactly
\[
1^{\,2^{k-a-1}-1}0^{\,2^{k-a-1}-1}1,
\]
with zero-length powers omitted. The segment of one-initial rotations is \(0^A1\,0^B\) for positive integers \(A,B\) when \(k\ge2\). Consequently the exact linear run count is logarithmic in the input length \(|C_k|=3^k\), whereas \(r(C_k)=2^{k+1}-1\) for \(k\ge1\).

## Assumptions and scope

The binary alphabet is ordered \(0<1\). Rotations are indexed by positions even for periodic words; the output preceding character is the symbol immediately before the rotation start, with indices reduced modulo the word length. There is no terminal sentinel. A run is a maximal equal-character block in this **linear** BWT output, without identifying its endpoints. Only the specified Cantor morphism and its finite iterates are claimed; no analogous identity is asserted for arbitrary nonprimitive morphisms.

## Proof

**1. Exact cyclic zero gaps.** Let \(N=2^k\). The positions of the ones in \(C_k\), indexed from zero in increasing order, are the \(N\) length-\(k\) base-three integers with digits in \(\{0,2\}\), ordered by their associated length-\(k\) binary integers. Write their positions as \(p_0<\cdots<p_{N-1}\), and let \(g_j\) count zeros strictly after the \(j\)-th one and before the next one, cyclically. For \(0\le j<N-1\), incrementing the binary selector \(j\) replaces exactly \(a=\nu_2(j+1)\) trailing binary ones, giving
\[
p_{j+1}-p_j=3^a+1,\qquad g_j=3^{\nu_2(j+1)}.
\]
The word starts and ends with one, hence \(g_{N-1}=0\). In particular each positive gap is a power of three, and the unique maximal gap is \(3^{k-1}\). The unique maximal gap also implies the cyclic word is primitive for \(k\ge1\), so its rotations are distinct.

**2. Decomposition by the number of leading zeros.** Fix an integer \(t\ge1\). A cyclic rotation begins with exactly \(t\) zeros followed by one at the \(j\)-th marked position if and only if \(g_{j-1}\ge t\). Its preceding BWT character equals one precisely when \(g_{j-1}=t\); otherwise that preceding character is zero. (Subscripts of \(g\) are taken modulo \(N\).) Every zero-starting rotation occurs in exactly one such group. Lexicographic order sorts the groups in decreasing \(t\), since \(0^{t+1}1\) precedes \(0^t1\). Because every positive gap is a power of three, a group with non-power \(t\) contributes only zeros.

**3. The exact nontrivial group.** Put \(t=3^a\), where \(0\le a<k\). The allowed next-marker indices are exactly
\[
j=2^a q,\quad 1\le q\le 2^{k-a}-1.
\]
Set \(H=2^{k-a-1}\), so \(q\) ranges from \(1\) through \(2H-1\). The gap just before this marker has length \(3^a\) exactly if \(q\) is odd; thus its preceding BWT character is one for odd \(q\), zero for even \(q\).

For each allowed \(q\), the successive gaps after its marker at offsets \(0,1,\ldots,2^a-2\) equal \(3^{\nu_2(h+1)}\), independently of \(q\). The first possibly distinguishing gap, at offset \(h=2^a-1\), equals \(3^{a+\nu_2(q+1)}\) for \(q<2H-1\). For the terminal \(q=2H-1\), this gap instead equals zero, since it is \(g_{N-1}\). Comparison of rotations with the same initial \(t\) is therefore settled by this first differing gap: a larger zero gap produces a lexicographically smaller rotation. It follows that all nonterminal odd \(q\) precede all even \(q\), which in turn precede the terminal odd \(q=2H-1\). The potential differences within one of these three sets do not matter for the preceding BWT character, which is constant on each set. There are \(H-1\) nonterminal odd indices, \(H-1\) even indices, and one terminal odd index. Their BWT block is exactly
\[
1^{H-1}0^{H-1}1.
\]
This remains valid for \(H=1\), where the two empty blocks disappear.

**4. One-initial rotations.** Every marked one starts a one-initial rotation. Its preceding BWT character is one only for the marker \(j=0\), because \(g_{N-1}=0\), and is otherwise zero. For \(k\ge2\), the rotation starting at marker \(j=1\) precedes marker \(j=0\), since \(g_1=3>g_0=1\), while the rotation at marker \(j=N-1\) follows it, since \(g_{N-1}=0<g_0=1\). Hence the BWT one-initial group has form \(0^A1\,0^B\) with \(A,B\ge1\).

**5. Count runs.** In decreasing order of initial zero count, the group \(t=3^{k-1}\) supplies one run of ones, and every power group with \(0\le a<k-1\) supplies two runs of ones, separated by a nonempty zero segment. Between consecutive power groups \(3^{a+1}\) and \(3^a\) are non-power values of \(t\) with nonempty all-zero groups whenever \(a\ge0\) and \(a+1\le k-1\): for example \(t=2\cdot3^a\) is admissible because the maximal gap \(3^{a+1}\) is present. Therefore the ones-runs from neighboring power groups never merge. After the final \(t=1\) group, the one-initial block begins with zeros; it contributes exactly one additional ones-run. The BWT begins with one (the maximal-gap group) and ends with zero (the one-initial block). There are therefore exactly
\[
1+2(k-1)+1=2k
\]
ones-runs and equally many zeros-runs, proving \(r(\operatorname{BWT}(C_k))=4k\). Finally, direct substitution shows that the number of ordinary runs in \(C_k\) is \(2^{k+1}-1\) for \(k\ge1\): its \(2^k\) ones are isolated by positive gaps except for the two endpoint ones, giving \(2^k\) one-runs and \(2^k-1\) zero-runs. The small cases \(k=0,1\) follow by inspection. \(\square\)

## Verification

The accompanying standalone Python file `checker.py` independently builds the Cantor iterates, sorts cyclic rotations using a doubling method, counts BWT runs, and checks the predicted segments by exact leading-zero groups. It performs direct literal sorting as an independent second implementation on the smaller instances. The finite tests confirm the asserted identity through \(k=9\), but the proof above, not extrapolation, establishes all \(k\ge2\). A unique maximal cyclic zero gap guarantees that tied rotations do not affect the claimed sorting convention.

## Relationship to prior work

Lü, Chen, Guo and Wen (2016) analyze permutation complexity of the Cantor-like sequence generated by this morphism; permutation complexity is not the run count of its cyclic Burrows–Wheeler transform. Brlek and collaborators (2019) analyze the transform of several classes of morphic words, notably Thue–Morse and Fibonacci-related words. Frosini and collaborators (2022) **already prove logarithmic upper and lower bounds** on the number of BWT equal-letter runs of broad classes of growing nonprimitive binary morphisms; this covers the order of growth here. Accordingly, logarithmic growth alone is **not** claimed as a new result. The additional finding here is the **exact coefficient and exact ordered block decomposition** for each Cantor iterate. Fici and collaborators (2023) investigate when morphisms preserve or change BWT-run counts in arbitrary inputs, without supplying this particular exact sequence-specific decomposition in the inspected material.

## Limitations

This proof is for the fixed morphism \(1\mapsto101,\ 0\mapsto000\), circular (sentinel-free) BWT, and the binary alphabet order \(0<1\). No claim is made about all Cantor-like morphisms, a terminal-symbol BWT, minimum-string attractors, or independently verified historical priority. While the relevant full texts on morphic BWT runs were inspected, an equivalent result under other terminology remains a literature risk. The complete full text of the 2016 permutation-complexity paper was not available; its accessible abstract and sections address a different invariant.

## References

1. X.-T. Lü, J. Chen, Y.-J. Guo, and Z.-X. Wen, “On the permutation complexity of the Cantor-like sequences,” *Theoretical Computer Science* 616 (2016), 100–110. DOI: `10.1016/j.tcs.2015.12.022`. Public source date independently documented as 2016-01-21.
2. S. Brlek, A. Frosini, I. Mancini, E. Pergola, and S. Rinaldi, “Burrows-Wheeler transform of words defined by morphisms,” *Combinatorics on Words* (2019). DOI: `10.1007/978-3-030-25005-8_32`. Author full-text version: `https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf`.
3. A. Frosini, I. Mancini, S. Rinaldi, and collaborators, “Logarithmic equal-letter runs for BWT of purely morphic words” (2022). arXiv: `2202.02609`, `https://arxiv.org/abs/2202.02609`.
4. G. Fici, G. Romana, M. Sciortino, and C. Urbina, “On the Impact of Morphisms on BWT-Runs,” *CPM* (2023). DOI: `10.4230/LIPIcs.CPM.2023.10`.
