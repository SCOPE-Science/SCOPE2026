# Complete census of the first delicate cubefree binary block
## Finding
A binary word is delicate cubefree when it is cubefree and changing any one of its letters creates a cube.

The first three lengths admitting delicate cubefree binary words are the published lengths \(20\), \(21\), and \(22\). Their complete counts are
\[
2,\quad 4,\quad 2.
\]

At length \(20\), the two words are
\[
\mathtt{00101001101001101011},\qquad \mathtt{11010110010110010100}.
\]

At length \(21\), the four words are
\[
\mathtt{001010011010011010110},\quad \mathtt{011010110010110010100},\quad \mathtt{100101001101001101011},\quad \mathtt{110101100101100101001}.
\]

At length \(22\), the two words are
\[
\mathtt{0110101100101100101001},\qquad \mathtt{1001010011010011010110}.
\]

For each of the three lengths, the complete set is one orbit under reversal and binary complementation. The length-\(20\) and length-\(22\) orbits have size \(2\); the length-\(21\) orbit has size \(4\).

## Assumptions and scope
A cube is a nonempty factor \(XXX\). A word is cubefree if it has no cube factor. Delicacy means that every single-position bit flip creates a cube.

The primary source already proves that delicate cubefree binary words exist exactly at lengths \(20,21,22,29,33,34,35\) and every length at least \(38\). The present claim does not change that spectrum; it classifies the entire first consecutive admissible block \(20,21,22\).

## Proof
Cubefreeness is factorial, so exhaustive prefix generation is complete. When one bit is appended to a cubefree prefix, any newly created cube must be a suffix. Testing all suffixes of length \(3h\) is therefore exact.

The complete cubefree counts at lengths \(20,21,22\) are respectively \(5324\), \(7754\), and \(11320\). For every survivor, each position is flipped in turn and the whole mutated word is scanned for a cube. Exactly \(2,4,2\) words pass at the three lengths, and no delicate cubefree word occurs below length \(20\).

A second enumeration engine rescans each whole prefix for cubes instead of using the suffix invariant. It gives exactly the same cubefree levels through length \(22\), and the same delicate sets. Reversal and complementation of one representative at each length generate exactly the corresponding full set.

## Verification
Run `python3 verify.py` beside `certificate.json`. The verifier reconstructs the cubefree prefix tree through length \(22\) by two independent methods, tests every one-bit mutation of every candidate, checks the exact eight listed words, and recomputes their symmetry orbits.

## Relationship to prior work
Przybocki introduced delicacy and proved the complete admissible-length spectrum for delicate cubefree binary words. The proof prints \(\mathtt{00101001101001101011}\) as a length-\(20\) witness. Its morphism has images \(\mathtt{0110101100101100101001}\) and \(\mathtt{1001010011010011010110}\), which are exactly the two length-\(22\) equality cases found here.

The published result is an existence-spectrum theorem. It does not state the number of delicate cubefree words at lengths \(20,21,22\), nor that each boundary layer is one reversal/complement orbit. Exact-string, uniqueness, equality-case, and count-pattern searches located the source but no published complete census.

## Limitations
This classification covers only the first admissible block \(20,21,22\). It does not enumerate the later sporadic lengths or the infinite family beginning at \(38\). Unpublished source-author search output could contain the same small equality sets.

## References
1. B. Przybocki, “Lengths of Irreducible and Delicate Words,” arXiv:2108.06646v1, first public version 2021-08-15; Electronic Journal of Combinatorics 29(3), #P3.7, 2022, DOI 10.37236/10669.
