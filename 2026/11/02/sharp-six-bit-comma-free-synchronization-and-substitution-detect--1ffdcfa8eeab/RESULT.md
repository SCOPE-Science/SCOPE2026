# Sharp six-bit comma-free synchronization and substitution-detection tradeoff

## Finding
For the binary alphabet, consider *comma-free* block codes \(C\subseteq\{0,1\}^6\): for every \(u,v,w\in C\) and every shift \(1\le j\le5\), the mixed six-symbol word \(u_{j+1}\cdots u_6v_1\cdots v_j\) must differ from \(w\). The exact largest cardinality is \(9\); exactly \(1972\) labeled nine-word codebooks attain it. When in addition every distinct \(u,v\in C\) has Hamming distance at least \(2\), the sharp maximum is **\(7\)** and there are exactly **\(272\)** labeled seven-word codebooks. Under global bit complementation and reversal, the two sets of maximum codebooks split into \(493\) and \(68\) orbits respectively, all of size four. In particular, all \(1972\) unrestricted nine-word maxima have Hamming minimum distance exactly \(1\).

## Assumptions and scope
Words have exactly six positions, the binary alphabet is labeled, and codebooks are unordered sets of distinct words. The overlap constraint is imposed even when \(u=v\) and even when the forbidden word equals either concatenated word. Hamming distance \(d_H(u,v)\) counts differing positions; \(d_H(C)\ge2\) provides detection of a single substitution *after block boundaries are identified*, not correction or detection of an arbitrary erroneous continuous stream. A symmetry acts simultaneously on every codeword: reversal of position order and/or global exchange of 0 with 1. No arbitrary coordinate permutation is asserted to preserve comma-freeness.

## Proof
**Necklace upper bound.** A word of proper cyclic period cannot belong to any comma-free code, since its own self-concatenation contains it as a shifted window. Two different rotations of a primitive word cannot both belong, by the same self-concatenation argument. The number of primitive binary length-six necklaces is
\[
\frac{2^6-2^3-2^2+2}{6}=9,
\]
where the numerator follows by excluding periods dividing two and three, with inclusion-exclusion for period one. Every comma-free code therefore has at most nine words, selecting at most one representative from each of nine six-word necklaces.

**Exhaustive constrained census.** Enumerate the nine primitive-necklace classes lexicographically. Maintain a partial selected set \(S\) and a forbidden set \(B(S)\) of all mixed six-symbol windows from ordered pairs of words already in \(S\). At a class, either skip it (allowed only when investigating Hamming-distance at least two codes), or insert one of its six representatives \(x\). Insertion is legal precisely when \(x\notin B(S)\), all mixed windows from pairs involving \(x\) avoid every word of \(S\cup\{x\}\), and, in the detection variant, \(d_H(x,s)\ge2\) for every \(s\in S\). Update \(B\) by adjoining those new mixed windows. The invariant that \(B=B(S)\) proves legality of every accepted branch. Every eligible codebook appears on exactly one branch, because its intersection with every necklace is uniquely defined. Thus recursion constitutes an exact finite proof, not statistical sampling.

The exhaustive leaf cardinality table under the additional distance-two condition is:

| Size \(s\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of codebooks | 1 | 54 | 1090 | 8410 | 23892 | 22374 | 5712 | 272 | 0 | 0 |

The unrestricted branch which always selects one representative from each of the nine necklaces has exactly \(1972\) valid leaves. This both attains the necklace bound and counts all unrestricted maximum codebooks. Every full nine-word leaf was separately checked to have Hamming minimum distance exactly one. The distance-two search attains seven and exhausts all eight- or nine-word possibilities. Explicit codebooks are among the inventories:

- Nine-word comma-free: `000001 000101 000111 100001 100101 100111 101001 101011 101111`.
- Seven-word comma-free with \(d_H\ge2\): `000001 000110 011010 011101 110001 110010 111110`.

Finally, for every maximum codebook \(C\), apply the four transformations \(C\), \(\operatorname{reverse}(C)\), \(\operatorname{complement}(C)\), and \(\operatorname{reversecomplement}(C)\). Their direct exact orbit enumeration yields orbit-size histogram \(\{4:1972\}\) and \(\{4:272\}\) for the unrestricted and distance-two maxima. Dividing by four gives \(493\) and \(68\) distinct symmetry orbits. The transformation calculation is part of the independently replayable finite census.

## Verification
Run `python3 verify_comma_free.py` from the folder containing that file and `full_codebooks.tsv` and `detecting_codebooks.tsv`. The script uses only the Python standard library, reconstructs all nine primitive-necklace classes from all 64 binary words, reruns the exhaustive finite branching proof, verifies all leaf totals and symmetry orbits, validates each listed codebook directly against every ordered overlap and Hamming condition, and compares the complete inventories byte-for-byte with the generated ordered lists. The expected terminal status is `VERIFY_OK`. The inventories are complete, not random samples; the program has no user-supplied solver or external data dependency. An alternative independently developed integer-encoding enumerator checked the unrestricted count \(1972\); the independent cross-check does not replace the self-contained exhaustive program.

## Relationship to prior work
Golomb, Gordon and Welch introduced comma-free code bounds and the primitive-necklace obstruction. Tang, Golomb and Graham studied limits for even blocklengths but not a complete six-bit detection-constrained census in the inspected relevant sections. Churchill developed self-reflective and self-swappable constraints, not the Hamming-distance-two requirement; his exact publication date provides a date-verified archived primary source. The present distinction is between a comma-free nine-word optimum and its sharp additional one-bit substitution-detection penalty. The general necklace bound alone does not imply the seven-word maximum or either equality-class census.

## Limitations
The results apply to binary blocks of length exactly six. They do not extrapolate to longer words or arbitrary alphabets, do not provide correction of a substitution, and do not assert stream-level error tolerance without synchronization. Earlier publications not fully available or not indexed could contain an equivalent finite enumeration; independent historical-priority review has not been performed. This is a finite, fully exhaustive mathematical result, not an asymptotic capacity theorem.

## References
1. A. L. Churchill, *Restrictions and Generalizations on Comma-Free Codes*, Electronic Journal of Combinatorics 16 (2009), R25, first published 2009-02-20. https://doi.org/10.37236/114 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i1r25/pdf/ .
2. B. Tang, S. W. Golomb and R. L. Graham, *A New Result on Comma-Free Codes of Even Word-Length*, Canadian Journal of Mathematics 39 (1987), 513–526. https://doi.org/10.4153/CJM-1987-023-7 ; full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/71A7831337DAC1E7D03DF9AE4C096F08/S0008414X0000448Xa.pdf/div-class-title-a-new-result-on-comma-free-codes-of-even-word-length-div.pdf .
3. S. W. Golomb, B. Gordon and L. R. Welch, *Comma-Free Codes*, Canadian Journal of Mathematics 10 (1958), 202–209. https://doi.org/10.4153/CJM-1958-023-9 .
4. J. A. Llewellyn, *Finite State Models in the Study of Comma-Free Codes*, The Computer Journal 26 (1983), 303–308. https://doi.org/10.1093/comjnl/26.4.303 .
