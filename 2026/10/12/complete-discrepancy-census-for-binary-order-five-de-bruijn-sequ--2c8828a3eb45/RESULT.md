# Complete discrepancy census for binary order-five de Bruijn sequences
## Finding
A binary de Bruijn cycle of order \(5\) is a circular binary word of length \(32\) in which every binary word of length \(5\) occurs exactly once. Its discrepancy is the largest absolute difference between the numbers of ones and zeroes in a circular contiguous factor.

There are \(2048\) binary order-\(5\) de Bruijn cycles up to rotation. Their complete discrepancy distribution is
\[
\begin{array}{c|rrrr}
\text{discrepancy}&5&6&7&8\\
\hline
\text{number of cycles}&224&688&912&224.
\end{array}
\]
Thus exactly \(224\), or \(7/64\), attain the minimum discrepancy \(5\).

After quotienting rotations, let bitwise complementation and reversal act on the \(224\) minimum-discrepancy cycles. They form exactly \(60\) symmetry orbits: \(52\) orbits have size \(4\), and \(8\) have size \(2\). The lexicographically least minimum-discrepancy representative is
\[
\mathtt{00000101011001101110100100011111}.
\]

## Assumptions and scope
Cycles are identified only up to cyclic rotation when the count \(2048\) is stated. Complementation and reversal are used only for the secondary symmetry quotient.

For a binary circular word \(w\), discrepancy is
\[
\operatorname{disc}(w)=\max_u\left||u|_1-|u|_0\right|,
\]
where \(u\) ranges over circular contiguous factors. Every binary de Bruijn cycle is balanced, so it contains exactly \(16\) zeroes and \(16\) ones at order \(5\).

The minimum value \(5\) is prior work: Álvarez, Becher, Mereb, Pajor, and Soto proved that the minimum discrepancy of a binary de Bruijn sequence of order \(n\) is exactly \(n\). The new claim is the complete order-\(5\) distribution and the equality-layer symmetry census.

## Proof
There are two independent exhaustive cycle generators.

The first uses the binary de Bruijn graph \(B(2,4)\). Its \(16\) vertices are the length-\(4\) binary words, and its \(32\) directed edges are the length-\(5\) binary words. A binary de Bruijn cycle of order \(5\) is exactly an Eulerian cycle. The edge \(\mathtt{00000}\) occurs uniquely, so fixing it as the first edge removes cyclic-rotation multiplicity. Exhaustive Eulerian backtracking produces \(2048\) cycles, agreeing with the classical count
\[
2^{\,2^{4}-5}=2048.
\]

The second generator starts from the unique length-\(5\) factor \(\mathtt{00000}\). It appends bits while forbidding any repeated length-\(5\) factor and finally requires the last four appended positions to close back to \(\mathtt{0000}\). It independently produces exactly the same \(2048\) canonical cycles.

Encode a one by \(+1\) and a zero by \(-1\). Because the total sum around a de Bruijn cycle is zero, every circular-factor sum is a difference of two cyclic prefix sums. Hence
\[
\operatorname{disc}(w)=\max P-\min P,
\]
where \(P\) ranges over the prefix sums of any linearization of \(w\). Computing this quantity on all \(2048\) cycles gives the histogram
\[
5:224,\qquad 6:688,\qquad 7:912,\qquad 8:224.
\]
A second discrepancy implementation scans every circular factor directly and agrees cycle by cycle.

Finally, complementation and reversal preserve both the de Bruijn property and discrepancy. Canonicalizing every transformed word by its least cyclic rotation partitions the \(224\) minimizers into \(60\) orbits, with orbit-size histogram
\[
2:8,\qquad 4:52.
\]

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently regenerates all cycles by Eulerian-circuit enumeration and by repeated-factor backtracking. It checks that the two complete sets agree and have size \(2048\), and that every generated cycle has all \(32\) distinct length-\(5\) circular factors.

For every cycle, the verifier computes discrepancy both from prefix-sum range and by explicitly scanning every circular factor. It checks the complete four-value histogram and the exact \(224\)-element minimum layer.

The certificate records a digest of the sorted minimizers and all \(60\) symmetry-orbit representatives with their orbit sizes. These are recomputed from scratch during replay.

## Relationship to prior work
Gabric and Sawada introduced a systematic investigation of discrepancy for de Bruijn sequences. They evaluated many named constructions and primitive-polynomial LFSR families, established asymptotically low- and high-discrepancy constructions, and explicitly listed studying the distribution of discrepancy over all de Bruijn sequences as a future direction.

Álvarez, Becher, Mereb, Pajor, and Soto then solved the minimum-value problem for binary de Bruijn sequences: the minimum discrepancy at order \(n\) is exactly \(n\), and their algorithm constructs a sequence attaining it. Their experimental Table 2 records minimum attainable discrepancies for small parameters, including the binary case, but does not enumerate the number of minimizers or the full discrepancy distribution.

The present result supplies that distribution completely at order \(5\). Searches for the exact count \(224\), an order-\(5\) discrepancy census, and minimizer symmetry classes located the minimum-value and construction papers but no published complete order-\(5\) distribution.

## Limitations
This is a finite classification at order \(5\). It gives no formula for the discrepancy distribution at larger orders and does not estimate the asymptotic proportion of minimum-discrepancy cycles.

The number of binary de Bruijn cycles rises doubly exponentially; already at order \(6\) there are \(67{,}108{,}864\) cycles up to rotation, so the exhaustive method used here is not intended as a scalable distribution algorithm.

An unindexed computation associated with earlier experimental work could contain the same order-\(5\) histogram even though the inspected publications do not state it.

## References
1. N. Álvarez, V. Becher, M. Mereb, I. Pajor, and C. M. Soto, “De Bruijn Sequences with Minimum Discrepancy,” arXiv:2407.17367v1, first public version 2024-07-24.
2. D. Gabric and J. Sawada, “Investigating the discrepancy property of de Bruijn sequences,” Discrete Mathematics 345(4) (2022), 112780, DOI 10.1016/j.disc.2021.112780.
3. N. G. de Bruijn, “A combinatorial problem,” Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764.
