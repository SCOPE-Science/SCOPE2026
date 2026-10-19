# Sharp scarcity of clustered BWT outputs at every fixed sparse binary weight

## Finding
For an integer \(k\ge4\) held fixed, let \(B_k(n)\) be the number of indexed binary words of length \(n\) with exactly \(k\) ones whose circular-rotation Burrows–Wheeler output has fewer than \(2k\) equal-letter runs. There are constants \(c_k,C_k>0\) and \(n_k\) such that for all \(n\ge n_k\),
\[
c_k n^{k-1}\le B_k(n)\le C_k n^{k-1}.
\]
Equivalently, for a uniformly chosen binary word with precisely \(k\) ones,
\[
\Pr\bigl(\operatorname{runs}(\operatorname{BWT}(w))=2k\bigr)
=1-\Theta_k(1/n).
\]
The reciprocal-length error is sharp: there are \(\Theta_k(n^{k-1})\) exceptional words, not merely at most that many. An explicit sufficient condition for the maximal run count is that all \(k\) cyclic zero gaps between successive ones are positive and every two differ by at least two. Conversely, a repeated **largest** gap forces a nonmaximal run count.

## Assumptions and scope
The alphabet is the ordered binary alphabet \(0<1\). For each \(n\ge k+1\), a word is *indexed*: two circular rotations count as different words if they differ as indexed strings. Its BWT output is the last column obtained by lexicographically sorting all \(n\) cyclic rotations (retaining duplicate rotations separately). No terminal marker is inserted. The number of runs is the number of maximal **linear** blocks of identical symbols in that last column, not its cyclic run count. For a nonconstant binary word the BWT starts with \(1\) and ends with \(0\), so its run count is an even integer at most \(2k\). The asymptotic constants may depend on fixed \(k\); no claim of uniformity when \(k\) grows with \(n\) is made.

Choose any marked one and traverse the word cyclically from that position. Write \(g_1,\ldots,g_k\) for the nonnegative counts of zeros between consecutive ones. Thus \(\sum_i g_i=n-k\). The two gap conditions are invariant under changing the marked one.

## Proof
**1. Rotation-order lemma.** A cyclic rotation beginning with \(t\) zeros and then a one precedes every rotation beginning with fewer than \(t\) zeros and follows every rotation beginning with more. The reason is a comparison at the first position where the initial zero counts differ: \(0<1\). Rotations beginning with a one follow all rotations beginning with a zero.

Assume all \(g_i\ge1\). For each gap, exactly one rotation starts at its *first* zero, hence begins with exactly \(g_i\) zeros. Its preceding letter, and therefore its BWT last-column letter, is \(1\). Every other rotation is preceded by \(0\). Hence the \(k\) ones in the BWT correspond precisely to the \(k\) gap-start rotations. If the gaps are pairwise distinct, the unique largest gap-start rotation precedes all other rotations; the BWT begins with \(1\). Its last rotation begins with one, and all runs of ones in the input have length one, so the BWT ends with \(0\).

**2. Separation certificate.** Suppose every two gap lengths differ by at least two. Between gap-start rotations with zero-prefix lengths \(g_i>g_j\), select the rotation beginning at the **second** zero of the longer gap. Its zero-prefix length is exactly \(g_i-1\), which is strictly between \(g_i\) and \(g_j\). It is preceded by \(0\), and the rotation-order lemma places it strictly between the two gap-start rotations. Consequently no two ones in the BWT are consecutive. Since the BWT begins with \(1\) and ends with \(0\), each of its \(k\) ones gives a separate one-run and a following zero-run: exactly \(2k\) runs.

**3. Global upper bound.** For every nonconstant binary input, its longest cyclic zero run starts at a position preceded by \(1\). Those starts are the lexicographically first rotations, so the first BWT symbol is \(1\). Similarly, the longest cyclic one run starts at a position preceded by \(0\); the lexicographically last rotations start there, so the final BWT symbol is \(0\). Each of the \(k\) BWT ones belongs to at most one one-run, and an output beginning with one and ending with zero has an equal number of one-runs and zero-runs. Therefore the total cannot exceed \(2k\).

**4. Upper count for exceptions.** In the gap description, a word fails the sufficient condition only if some \(g_i=0\), or if \(|g_i-g_j|\le1\) for some distinct indices. For fixed \(k\), the number of nonnegative integer solutions to \(\sum_i g_i=n-k\) with one prescribed zero coordinate is \(O_k(n^{k-2})\). With any prescribed relation \(g_i-g_j\in\{-1,0,1\}\), choose the common-size parameter in \(O(n)\) ways and distribute the remainder among \(k-2\) coordinates in \(O_k(n^{k-3})\) ways, again \(O_k(n^{k-2})\). Taking the finite union gives \(O_k(n^{k-2})\) exceptional **marked gap tuples**. There are exactly \(n\) choices of the absolute marked position, and every indexed weight-\(k\) word has exactly \(k\) markings. Thus
\[
B_k(n)=O_k(n^{k-1}).
\]
This does not assume every gap collision actually produces a nonmaximal BWT.

**5. Matching lower count.** Fix two consecutive gap coordinates equal to an integer \(m\) satisfying \(0.36n\le m\le0.38n\). Distribute the remaining \(n-k-2m\) zeros nonnegatively among the other \(k-2\) gaps. For all sufficiently large \(n\), this remainder lies between two positive constant multiples of \(n\) and is **strictly smaller** than \(m\). Consequently the two displayed gaps are tied for the largest gap, and no other gap can attain their size. In the sorted rotation matrix, the very first two rows begin with the maximal \(m\) zeros, both start at the first zero of their corresponding gap, and both are preceded by \(1\). The BWT begins with \(11\), so it has strictly fewer than \(2k\) runs.

There are \(\Theta(n)\) choices for \(m\). For each, the number of ordered nonnegative compositions of the remaining total into \(k-2\) parts is
\[
\binom{n-k-2m+k-3}{k-3}=\Theta_k(n^{k-3}).
\]
Thus \(\Theta_k(n^{k-2})\) marked gap tuples force an exception. As each indexed word can arise from at most \(k\) choices of its marked one, these tuples yield \(\Omega_k(n^{k-1})\) distinct indexed words. Combined with step 4, this proves the theorem.

**6. Normalization.** Exactly \(\binom nk=\Theta_k(n^k)\) indexed words contain \(k\) ones. Dividing the two-sided exceptional count by this total yields the asserted probability law. Since the run deficit is a positive even integer for every exception and is at most \(2k-2\), the expected deficit is also \(\Theta_k(1/n)\).

## Verification
The reproducible standalone `verify.py` computes the cyclic BWT by **directly sorting complete rotations**, without using the proof's zero-prefix comparison algorithm. It checks 190,890 indexed words for every weight \(4\le k\le6\) and length \(k+1\le n\le20\). For each word it checks the output endpoints, even run count and \(2k\) bound; for clean-gap words it checks equality; for words with a repeated largest gap it checks strict inequality. All checks pass. The exact counting proof above, not finite enumeration, establishes the infinite theorem.

## Relationship to prior work
Burrows and Wheeler (1994) introduced the sorted-cyclic-rotation transformation. Mantaci, Restivo, Rosone, Sciortino and Versari (2017) proved general clustering-ratio bounds, including a twofold bound relative to the **input run count**, and constructed special maximally unclustered families. Their result does not compare the BWT run count to the number of ones, and neither its extremal constructions nor its input-run bound implies a high-probability result for uniform fixed-Hamming-weight ensembles. Mantaci and collaborators' separate fixed-point study (2017) treats the equation \(\operatorname{BWT}(w)=w\), not the run-count distribution; only its accessible abstract and introductory material could be checked. The theorem here gives a sharp **enumerative order of rarity** and a deterministic cyclic-gap certificate simultaneously for all fixed weights at least four. No completeness of the literature search or independent priority confirmation is claimed.

## Limitations
Only the original no-sentinel cyclic BWT, binary alphabet, fixed sparse Hamming weight, and linear BWT run count are treated. The theorem gives a sharp asymptotic order, not the exact exceptional polynomial or leading constant for each weight; it does not claim sufficiency is necessity, and does not cover a weight growing with length. It does not establish any numerical bit-compression factor or behavior of alternative BWT variants. Literature-coverage risk remains for unindexed equivalent formulations and the inaccessible full fixed-point article.

## References
1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Digital SRC Research Report 124, dated May 10, 1994, https://www.cs.jhu.edu/~langmea/resources/burrows_wheeler.pdf .
2. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino and L. Versari, *Measuring the clustering effect of BWT via RLE*, Theoretical Computer Science 698 (2017), 79–87, DOI:10.1016/j.tcs.2017.07.015, open postprint https://pages.di.unipi.it/rosone/Papers/MRRSV_TCS2017.pdf .
3. S. Mantaci, A. Restivo, G. Rosone, F. Russo and M. Sciortino, *On Fixed Points of the Burrows-Wheeler Transform*, Fundamenta Informaticae 154 (2017), 277–288, DOI:10.3233/FI-2017-1566, available abstract https://journals.sagepub.com/doi/10.3233/FI-2017-1566 .
