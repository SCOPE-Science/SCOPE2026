# Parity bifurcation of majority recurrence on complements of cycles

## Finding
For each integer \(n\ge5\), label the vertices of the cycle \(C_n\) by residues \(i\in\mathbb Z/n\mathbb Z\). On its complement \(G_n=\overline{C_n}\), perform synchronous binary majority voting with ties retained. Write \(F_n\) for one update, \(Q_n=\#\{x:F_nx=x\}\), and \(P_n=\#\{x:F_n^2x=x\}\).

For **odd** \(n\ge5\), every configuration reaches a fixed point in at most two updates, and
\[
Q_n=P_n=2n+2.
\]
For **even** \(n=2m\ge6\), put
\[
H_m=\sum_{r=1}^{\lfloor m/2\rfloor}\frac{2m}{r}\binom{m-r-1}{r-1}^{\!2}.
\]
Then
\[
Q_{2m}=4,\qquad P_{2m}=H_m+4m+4,\qquad
\#\{\text{primitive two-cycles}\}=\frac{H_m}{2}+2m.
\]
Every eventual period is one or two. The **odd/even contrast** is qualitative: odd-size complements have only \(2n+2\) recurrent configurations, whereas even-size complements have exponentially many; the exponential growth of \(H_m\) is an *already known combinatorial asymptotic* (Munarini and Zagaglia Salvi, 2003), applied here to the graph-dynamical classification.

## Assumptions and scope
All graphs are loopless, finite and labelled. For a binary word \(x=(x_i)_{i\bmod n}\), let \(T(x)=\sum_i x_i\) and \(s_i=x_{i-1}+x_i+x_{i+1}\). Since \(i\) has every vertex except \(i-1,i,i+1\) as a neighbour, the number of neighbouring ones is \(T-s_i\). The update adopts one precisely when \(2(T-s_i)>n-3\), adopts zero when the inequality is reversed, and retains \(x_i\) on equality.

A **singleton run** is a cyclic occurrence of \(010\) or \(101\). A **balanced** word has the same number of zeros and ones; a **checkerboard** has alternating bits at every edge. A **single-run** word has exactly one cyclic block of ones and one cyclic block of zeros. All recurrent counts concern labelled configurations, not rotation classes or attraction-basin sizes. The theorem does not assert an even-size sharp convergence-time bound.

## Proof
**1. Strict outer layers.** When \(n=2m+1\) is odd, the neighbourhood degree is \(2m-2\). If \(T\le m-1\), the only exceptional case \(T=m-1\) can give a tie at a triple of zeros, where the central opinion is zero; hence the entire next configuration is zero. Complementing bits gives that \(T\ge m+2\) moves entirely to one. For \(T=m\), the next state has a one exactly at the centre of a cyclic \(000\) triple or at a singleton one. If the configuration has \(r\) runs of ones, let \(U\) be the number of these runs of length one and \(Z\) the number of centres of \(000\). Then \(T(F_nx)=U+Z\). There are \(m+1\) zeros distributed among \(r\) zero-runs, and at least one zero-run has length at least two, so \(Z\le m-r\). If \(r<m\), at least one one-run has length at least two, whence \(U\le r-1\) and \(T(F_nx)\le m-1\); the *following* step is consensus zero. If \(r=m\), all the ones are isolated and the zero-run lengths are \(2,1,\ldots,1\). The word is fixed. There are exactly \(n\) such words (choose the unique double-zero gap); their complements yield another \(n\) fixed words in layer \(T=m+1\), and the two consensus states are also fixed. Thus odd \(n\) has precisely \(2n+2\) fixed states, with global first-entry time at most two and no two-cycles. The bound is attained: a word with \(m\) consecutive ones and \(m+1\) consecutive zeros first moves to a nonzero state of weight \(m-1\), and then to zero.

**2. The two flanking layers for even size.** Let \(n=2m\ge6\); degree \(2m-3\) is odd and no tie is possible. We have consensus zero after one update when \(T\le m-2\), and consensus one when \(T\ge m+2\). At \(T=m-1\), the new one sites are exactly the centres of \(000\). As there are \(m+1\) zeros, their number is at most \(m-1\), with equality exactly if all \(m+1\) zeros form one cyclic run. In that equality case the \(m-1\) ones also form one cyclic run, and the next configuration translates that run by \(m\) positions. Another update translates back, producing a primitive two-cycle. Otherwise the next state has at most \(m-2\) ones and collapses to consensus. Complementation gives the same classification for \(T=m+1\), with a single run of \(m+1\) ones. Each flanking layer contributes \(n\) recurrent labelled words; together they contribute \(n\) distinct two-cycles.

**3. The balanced even layer.** If \(T=m\), the complement-cycle update is exactly \(F_nx=\overline{M_nx}\), where \(M_n\) is the ordinary three-site majority rule on the original cycle. A periodic complement-cycle trajectory entering either flanking layer can never return to weight \(m\); hence a recurrent balanced trajectory stays balanced and there \(F_n^2=M_n^2\) (majority commutes with complementation). In three-site majority, any pair of adjacent equal opinions remains permanently fixed. Starting at any such pair, inspect its adjacent site: if it has the same opinion it is fixed, and if not, it either belongs to another permanently fixed equal pair or flips to the boundary pair's opinion and becomes fixed after one update. Iterating around the finite cycle shows that every noncheckerboard configuration eventually becomes a majority fixed point. A recurrent point of \(M_n^2\) is therefore either a majority fixed word, characterized by absence of singleton runs, or one of the two checkerboards. Every balanced majority fixed word is exchanged with its complement by \(F_n\); the two checkerboards are fixed by \(F_n\). No further balanced periodic words are possible.

**4. Counting balanced words.** A balanced no-singleton word has an equal positive number \(r\) of zero-runs and one-runs, each of length at least two. The ordered lengths of each colour are compositions of \(m\) into \(r\) parts of size at least two, counted by \(\binom{m-r-1}{r-1}\). Choose the starting site of a distinguished one-run in \(2m\) ways and divide by \(r\) possible distinguished one-runs. Summing yields \(H_m\). The balanced recurrent layer has \(H_m+2\) words (including the two checkerboards), the flanking layers have \(2n\) words, and the two consensus configurations add two: \(P_{2m}=H_m+2n+4=H_m+4m+4\). Its fixed words are exactly the two consensuses and two checkerboards, so \(Q_{2m}=4\). The number of unordered two-cycles is \((P_{2m}-Q_{2m})/2=H_m/2+n\).

## Verification
The standalone `verify.py` constructs neighbourhoods directly in \(G_n\), not through the weight reduction. For each integer \(5\le n\le18\), it tests all \(2^n\) initial states, checks equality of the proved structural recurrent set with \(\{x:F_n^2x=x\}\), and checks the independent fixed-point and two-cycle counts. The complete output is included as `verify_output.txt`. In particular the recurrent counts for \(n=5,6,7,8,9,10,11,12\) are \(12,22,16,32,20,54,24,98\). These finite tests corroborate, but do not replace, the all-size proof.

## Relationship to prior work
The general period-at-most-two property of symmetric threshold dynamics was established by Goles and Olivos (1980), and is discussed in Benjamini–Chan–O'Donnell–Tamuz–Tan (2014). Kaaser–Mallmann-Trenn–Natale (2015) analyze voting time and graph modules, not exact recurrence on complements of cycles. The central circular no-zigzag sequence \(H_m\), including its enumeration and asymptotics, was already worked out by Munarini and Zagaglia Salvi (2003), and is indexed as OEIS A263656; no originality is claimed for that sequence or its known asymptotics. The claim here is the **new dynamical link**: a parity-dependent classification of all period-one/two states on the fixed natural graph family \(\overline{C_n}\), including the odd-size two-update collapse and the additional off-balance travelling two-cycles of even sizes.

## Limitations
This is a classification for simple complements of ordinary cycles with \(n\ge5\) only. It does not give even-size basin sizes, full transient-depth distributions, or a new enumeration of the previously known no-zigzag words. The available published-record searches and primary sources do not rule out an unindexed earlier dynamical classification; the originality assessment is bounded rather than a proof of global priority. No independent mathematical audit has been performed.

## References
1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” first public preprint 2014-05-11, https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, “On the Voting Time of the Deterministic Majority Process,” first public preprint 2015-08-14, https://arxiv.org/abs/1508.03519.
4. E. Munarini and N. Zagaglia Salvi, “Circular Binary Strings without Zigzags,” *Integers* **3** (2003), A19, publicly dated 2003-12-11; author-provided full text https://www.researchgate.net/publication/228396896_Circular_binary_strings_without_zigzags.
5. OEIS A263656, “Number of length-\(2n\) central circular binary strings without zigzags,” https://oeis.org/A263656.
