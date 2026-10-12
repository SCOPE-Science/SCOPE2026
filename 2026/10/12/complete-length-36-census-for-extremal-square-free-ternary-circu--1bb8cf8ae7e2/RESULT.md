# Complete length-\(36\) census for extremal square-free ternary circular words
## Finding
For the ternary alphabet \(\{0,1,2\}\), there are exactly \(15\) extremal square-free circular words of length \(36\), where a circular word is identified up to rotation. Under alphabet permutations and reversal, these \(15\) circular words form exactly three orbits, of sizes \(6\), \(6\), and \(3\). Canonical lexicographically least rotation representatives of the three orbits are
\[
\mathtt{010201202101201020121021202101210212},
\]
\[
\mathtt{010201202102010210120102012102010212},
\]
and
\[
\mathtt{010210120102120121020120210201210212}.
\]

Equivalently, among linear representatives of length \(36\), exactly \(540\) are circularly square-free and extremal. Each circular class has exactly \(36\) distinct rotations.

## Assumptions and scope
A finite word is square-free when it has no nonempty factor \(uu\). A circular word represented by \(w\) is square-free when every conjugate of \(w\) is square-free. It is extremal square-free when inserting any letter of the ternary alphabet at any position of the circle produces a circular word containing a square.

Mol and Rampersad proved that an extremal square-free ternary circular word exists exactly for lengths
\[
\{4,6,8,13,15,16,18,20,21,22,23,24,28,30,32,33,34,35,36\}
\cup\{m:m\ge 38\}.
\]
Thus \(36\) is the final sporadic attainable length: \(37\) is excluded, while every length at least \(38\) is attainable. The published result determines existence by length; the claim here classifies all equality objects at that last sporadic boundary.

## Proof
First generate every ternary square-free linear word by prefix extension. A newly created square after appending one letter must be a suffix, so checking all even suffixes is exhaustive. The resulting exact numbers of linear square-free words at lengths \(36\) and \(37\) are respectively
\[
168546\quad\text{and}\quad219516.
\]

For a length-\(n\) word \(w\), test circular square-freeness directly in \(ww\): for each cyclic start and each positive half-length \(h\) with \(2h\le n\), compare the two adjacent length-\(h\) blocks. This leaves exactly
\[
16416
\]
circularly square-free linear representatives at length \(36\), and
\[
18870
\]
at length \(37\).

Extremality was then computed in two independent ways. In the first, the complete length-\(37\) circular-square-free set is stored, and a length-\(36\) candidate is rejected if any of its \(36\cdot3\) insertions belongs to that set. In the second, every insertion is tested directly for circular square-freeness without consulting the stored length-\(37\) set. Both methods return the same set of exactly \(540\) length-\(36\) linear representatives.

A circular square-free word is primitive: if a representative were a nontrivial exact power, it would contain a square. Hence every length-\(36\) circular class has exactly \(36\) rotations, so the \(540\) linear representatives give
\[
540/36=15
\]
circular words.

Finally apply all six alphabet permutations and reversal, canonically reducing each result modulo rotation. The \(15\) classes split into exactly three orbits, with sizes \(6,6,3\), and the representatives displayed above.

## Verification
Compile and run `verify.cpp` with a C++17 compiler, for example:

`c++ -O3 -std=c++17 verify.cpp -o verify && ./verify`

The verifier reconstructs the complete square-free prefix tree through length \(37\), checks the exact circular counts at lengths \(36\) and \(37\), and performs both independent extremality tests. It then verifies primitivity through distinct rotations and recomputes the full action of alphabet permutations and reversal on the \(15\) circular classes.

`certificate.json` records all \(15\) canonical circular representatives and their three symmetry orbits.

## Relationship to prior work
Mol and Rampersad completely determine the attainable lengths of extremal square-free ternary circular words. Their Theorem 1.3 makes \(36\) the last sporadic attainable length before the exceptional nonattainable length \(37\) and the eventual interval beginning at \(38\). In the proof, unattainable small lengths are ruled out by standard backtracking, and for attainable lengths below \(470\) an extremal circular word is found by computer search.

The published theorem is therefore an existence spectrum rather than a boundary census: it does not state how many length-\(36\) extremal circular words exist or classify them under natural symmetries. Searches using the exact length, “extremal square-free circular”, equality/extremizer terminology, and exact representatives did not locate a published \(15\)-class or three-orbit classification.

## Limitations
The result classifies only the last sporadic length \(36\). It does not enumerate extremal circular words at the other attainable lengths or determine asymptotic orbit counts.

The original proof used computer search for finite cases, so unpublished search output from that work could contain the complete length-\(36\) level. No published or indexed equality classification was located.

## References
1. L. Mol and N. Rampersad, “Lengths of extremal square-free ternary words,” arXiv:2001.11763v1, first public version 2020-01-31; Contributions to Discrete Mathematics 16(1), 2021, 8–19, DOI 10.55016/ojs/cdm.v16i1.69831.
