# The first odd near-alternating binary Burrows–Wheeler obstruction

## Finding

For a binary necklace \([u]\) of length \(n\), define \(r(u)\) to be the number of **linear** constant-symbol runs in its cyclic-rotation Burrows–Wheeler transform \(\mathrm{BWT}(u)\). Define \(R(n)=\max_{[u]\in\{0,1\}^n/\mathrm{rotation}}r(u)\). For every odd integer \(3\le n\le49\),
\[
R(n)=\begin{cases}n-1,&3\le n\le47,\\46,&n=49.\end{cases}
\]
Exactly \(1128\) necklaces of length \(49\) attain this maximum, all primitive. Hence \(49\) is the first odd length \(n\ge3\) for which the natural ceiling of \(n-1\) BWT runs is unattained. The precise alphabet ordering is \(0<1\), and complements are not identified.

A matching length-\(49\) witness is the primitive necklace with representative `0001000101011011110001101010010011100111110110011`. Its BWT is `1110101011010101010101010101010101010101010101010`, with \(46\) linear runs.

## Assumptions and scope

The BWT is the last column of all \(n\) cyclic rotations sorted lexicographically, including repeated rotations if the source is periodic. Necklace equivalence identifies cyclic rotations, but not symbol complement or reversal. A *primitive* necklace has \(n\) distinct rotations. A linear run is a maximal consecutive equal-letter block within the displayed BWT, not a cyclic run. These conventions matter to the parity bound and counting statement. The claim is restricted to odd \(3\le n\le49\).

## Proof

**1. Single-cycle test and parity.** Given a binary word \(w=w_0\cdots w_{n-1}\), let \(z\) be its number of zeros. Define the stable-rank permutation \(\pi_w\) by scanning positions from left to right: the \(k\)-th zero, counted from \(0\), maps to \(k\), and the \(k\)-th one maps to \(z+k\). The standard BWT permutation criterion (Fici–Gabory–Romana–Sciortino, Lemma 8) says that \(w\) is the BWT of a unique primitive necklace precisely when \(\pi_w\) consists of one cycle of length \(n\). If \(n>1\) and \(w_0=0\), then \(\pi_w(0)=0\); if \(w_{n-1}=1\), then \(\pi_w(n-1)=n-1\). Thus every primitive binary BWT at length greater than one begins in \(1\) and ends in \(0\). Its number of changes is odd, so its number of linear runs is even. In particular, for odd \(n\), it has at most \(n-1\) runs.

**2. Exhaustive parametrization.** If \(w_0=1\) and exactly \(c\) of its \(n-1\) consecutive gaps join equal letters, then \(w\) is uniquely determined by the subset \(E\subseteq\{0,\ldots,n-2\}\) of those gaps. Starting with \(w_0=1\), form \(w_{i+1}=w_i\) for \(i\in E\), and flip the bit otherwise. The number of linear runs is exactly \(n-c\). For odd \(n\), ending in \(0\) requires \(c\) odd. Consequently every possible primitive BWT with \(n-1\) runs corresponds to exactly one one-element set \(E=\{j\}\). Every possible primitive BWT with \(46\) runs at length \(49\) corresponds to exactly one three-element set \(E\subseteq\{0,\ldots,47\}\).

**3. First exceptional length.** The attached `CHECK.py` enumerates all \(n-1\) singleton sets for each odd \(n=3,5,\ldots,49\) and computes the full orbit length of position \(0\) under the explicitly defined permutation. At odd lengths \(3,5,\ldots,47\), respectively, the smallest successful gap indices are

`0,1,2,0,0,1,2,0,1,6,7,7,0,1,10,11,0,1,2,3,13,14,7`.

These \(23\) displayed witnesses are independently reconstructed through their \(n\)-cycles and checked by direct sorting of all source rotations. At \(n=49\), all \(48\) singleton candidates fail. In index order \(j=0,\ldots,47\), the exact lengths of the orbit of \(0\) are

`7 22 15 43 23 35 12 38 20 28 20 28 39 46 32 31 34 46 34 41 25 44 20 35 35 15 44 15 41 15 46 8 31 8 46 8 28 8 28 8 38 8 35 8 43 8 21 8`.

None equals \(49\). Therefore no primitive necklace of length \(49\) has \(48\) runs, and parity gives \(r\le46\).

**4. Sharpness and exact multiplicity.** All candidates for \(46\) runs form the \(\binom{48}{3}=17296\) distinct words indexed by three-element equality sets. The same finite exhaustive algorithm tests their stable-rank cycle lengths, identifying exactly \(1128\) that have a single \(49\)-cycle. It validates the stable-rank permutation independently by stable sorting of positions, and reconstructs each accepted necklace and recomputes its BWT from the lexically sorted rotations. Its first accepted equality set is \(E=\{0,1,8\}\), giving the explicit witness above. By the single-cycle criterion and BWT injectivity on necklaces, these \(1128\) distinct BWT outputs correspond bijectively to \(1128\) primitive necklaces, all attaining \(46\) runs. This proves the count and the lower bound.

**5. Periodic necklaces cannot compete.** Suppose a length-\(n\) word is a proper power of a primitive word of length \(d<n\). In its BWT table every distinct root rotation is repeated consecutively exactly \(n/d\) times. Accordingly \(\mathrm{BWT}(u)\) results from \(\mathrm{BWT}(v)\) by replacing each symbol with \(n/d\) consecutive copies, and its linear run number is at most \(d\). For odd \(n\ge3\), this is strictly smaller than \(n-1\). For \(n=49\), proper primitive-root lengths are only \(1\) and \(7\), giving at most \(7\) runs, below \(46\). Thus the extrema and counts established for primitive necklaces are also the asserted extrema and counts among **all** necklaces.

## Verification

Execute `python3 CHECK.py` with a standard Python 3 interpreter. The complete output is embedded as `CHECKS.txt`. The program enumerates \(\sum_{n\in\{3,5,\ldots,49\}}(n-1)\) singleton candidates and exactly \(17296\) three-equality candidates at length \(49\); it tests each candidate with two explicit stable-rank formulations and recomputes every accepted BWT by sorting all source rotations. Its assertions establish the exact singleton-witness table, the \(48\)-entry nonexistence certificate, the \(1128\) count, and the displayed witness. Because these finite search spaces follow from the bijective gap encoding, no untested candidate remains within the claimed domain. The supplied program is executable and source-readable; the output log alone is not a proof.

## Relationship to prior work

Fici, Gabory, Romana, and Sciortino (first posted 2025-08-28; CPM 2026) show complete absence of clustering for nonbinary alphabets and revisit the binary fully-unclustered even-length Artin connection. Their Lemma 8 supplies the primitive-necklace standard-permutation test used here. Their theorems do not enumerate binary near-alternating length-\(49\) images or establish the first failure of the parity-allowed odd-length maximum. Mantaci, Restivo, Rosone, Sciortino, and Versari (2017) treat the fully-unclustered binary even-length criterion and clustering ratios, not the present odd-length deficit and finite extremizer census. The claim does not assert either of those established results as new.

## Limitations

This establishes a finite first-exception threshold and a complete length-\(49\) extremizer count; it does **not** derive a general formula for subsequent odd lengths, an asymptotic distribution, or Artin-type infinitude. The numerical certificate is an exhaustive finite computation, not a symbolic classification of all larger parameters. The literature comparison is limited to inspected primary texts and available research records; differently phrased or unindexed preexisting tables are a residual originality risk. Independent validation has not been performed.

## References

1. G. Fici, E. Gabory, G. Romana, M. Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879v1 (first public 2025-08-28), published as *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.13, especially Lemma 8 and Sections 1, 5.
2. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, L. Versari, *Measuring the clustering effect of BWT via RLE*, Theoretical Computer Science 698 (2017), 79–87. DOI:10.1016/j.tcs.2017.07.015.
