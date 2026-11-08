# Independent mathematical audit

## correctness

PASS

A six-bit comma-free code can contain only primitive cyclic words and at most one representative from each primitive length-six necklace; Möbius inclusion-exclusion gives exactly nine classes. A complete canonical DFS branches through the six representatives (and a skip branch under distance >=2), rejecting words whose ordered cross-boundary 1..5 shifted windows enter the codebook. This is exhaustive, with no probabilistic solver. Independently written compact-bitmask C++ enumerator reconstructed 1,972 nine-word unrestricted codebooks and 272 seven-word Hamming-distance-two codebooks, counted all detector sizes (1,54,1090,8410,23892,22374,5712,272), checked all nine-word solutions have minimum Hamming distance 1, and verified four-element reversal/complement orbits: 493 and 68. Source Python and C++ verifiers, including full listed inventory references, were inspected. Strictly length 6 finite census; no stream-error correction inference.

## originality

PASS

The classical primitive-necklace upper bound and comma-free definitions are due to Golomb–Gordon–Welch; even-length restrictions to Tang–Golomb–Graham and reversal-related closure analyses to Churchill. The intersection with Hamming distance >=2 and full exact numerical optimal/equality census were not found in the material actually inspected. Qualified due to inaccessible early papers and possible historical finite-state tabulations.

## value

PASS

A natural framing-plus-substitution detection design problem has a sharp finite capacity loss 9 to 7 and complete extrema and symmetry classes; a definite unknown finite invariant can be valuable without a general asymptotic capacity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
