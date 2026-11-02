# Scientific review

## Correctness — PASS

The claim fixes labelled vertices and unlabelled factors. The least-uncovered-edge exact-cover recursion covers every matching partition exactly once; two perfect matchings of \(K_8\) have only cycle types \(8\) and \(4+4\), so the precise switch condition is complete. The independently normalized edge-colouring program confirms the same \(6{,}240\) objects and \(17{,}640\) legal edges using a different enumeration and local switching implementation. The first checker performs BFS from every vertex in the \(5{,}280\)-state component. The second checks six full vertex-relabeling orbits and their representative eccentricities. All claimed counts and distances are exact, with no inference from a sample. The commuting-involution argument establishes that degree \(21\) is equivalent to affine translation structure.

## Originality — PASS, subject to historical-priority risk

The central comparator is Kaski–de Souza Medeiros–Östergård–Wanless (2014), *Switching in One-Factorisations of Complete Graphs*, DOI 10.37236/3606. Its inspected §§3, 4, 6 and 8 concern **isomorphism-class switching graphs**, including the six-type \(K_8\) quotient, its perfect-factorization isolated class, and the general parity obstruction. The labelled \(6{,}240\)-state graph is not that six-state quotient. Quotient connectivity cannot imply connectedness of a labelled covering graph, and quotient distance bounds do not imply the radius nine, diameter eleven, six labelled eccentricity classes, or affine-center characterization. Those are the claims assessed as new. Earlier known counts and the perfect-factorization isolation criterion are explicitly credited.

Searches included the exact combined metrics ("K8" "5280" switching one-factorizations; "one-factorizations" "6240" "960" switching), labelled distance synonyms, symmetric unipotent Latin-square intercalate switching, and the inspected 2014 primary PDF. No equivalent stronger statement was located. One independently posted labelled count, without switching metrics, was also found. Historical originality cannot be certified absolutely, and older unpublished or differently indexed computations remain a residual risk.

## Value — PASS

Local intercalate switching is a standard natural operation on one-factorizations, with direct significance for converting round-robin schedules while preserving all players' labels and changing only two rounds locally. The classical quotient result does not determine whether actual labelled schedules can be connected at all. This result settles that reachability question for all nonperfect schedules, gives the sharp maximum travel cost of eleven trades, and identifies every best-positioned schedule as an affine \(\mathbb F_2^3\) construction. The commuting-involution characterization supplies a structural reason for the exceptional centers, rather than merely an enumerative label. This is a complete finite structural benchmark, not a universal result.

## Closest literature and limits

The 2014 paper's definitions, parity, perfect obstructions and six-isomorphism-class graph are prior. The exact labelled metric and centers were not found there, after inspecting the relevant full-text sections and figure/table. The 2007 design textbook records the six isomorphism types and \(6{,}240\) labelled factorizations; these data are not claimed as new. A differently indexed historical calculation may exist; no independent referee or formal certification has assessed this finite computation. Verification programs and complete reproduction conditions accompany the result.

Self-review: passed. Independent audit: not yet performed.
