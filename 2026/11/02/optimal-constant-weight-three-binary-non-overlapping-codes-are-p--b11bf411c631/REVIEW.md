# Scientific review

## Correctness — PASS

The exact domain is binary fixed blocklength \(n\ge3\), Hamming weight exactly three, with every proper prefix-suffix comparison required for any ordered pair, including identical words. The upper bound follows from the established fact that a non-overlapping code contains only primitive words and cannot contain two cyclic shifts from the same orbit. All nonprimitive words of weight three are explicitly classified by the exponent dividing three. The construction is verified symbolically in two exhaustive cases: a suffix beginning at its second one has two ones and is too long to avoid all three target-prefix ones; a suffix beginning at its third one has one one and is long enough to contain two target-prefix ones. A suffix beginning with zero cannot match a codeword prefix. The arithmetic count is exact for each residue modulo three. The independent finite implementations exercise literal overlaps and primitive-orbit equality but are not taken as an infinite proof.

## Originality — PASS (best-knowledge, with residual risk)

The closest known covering statement is the primitive cyclic-shift orbit upper bound for constrained non-overlapping codes (Stanovnik–Moškon–Mraz, Proposition 5, arXiv:2410.18458v1). It can yield the upper bound after restricting content, but not its attainment: selecting arbitrary necklace representatives does not give a non-overlapping code. Their source's main theorems concern near-half balance and run-length constraints, with exact searches for small instances, rather than the stated all-length weight-three saturation. The earlier general maximal-code structure (Stanovnik–Moškon–Mraz, doi:10.1007/s10623-023-01344-z), variable-length bounds (Wang–Wang, arXiv:2402.18896v1), and fixed-density necklace listing (Ruskey–Sawada, doi:10.1137/S0097539798344112) likewise do not assert the cross-bifix-free primitive transversal. Published-result searches for fixed-weight-three sparse non-overlapping or cross-bifix-free codes did not identify an equivalent all-length theorem. An equivalent implicit specialization within older constructions cannot be ruled out completely.

## Mathematical value — PASS

The sparse three-pulse restriction is a natural constant-composition synchronization constraint. The theorem matches a structural upper bound for every blocklength and provides a direct encoder description, a complete primitive orbit transversal, and the exact capacity \(M_3(n)\) without optimization. The distinction between a necklace packing bound and simultaneous prefix-suffix feasibility supplies the substantive content. The result is not a renaming of the generic orbit inequality: the attaining construction and its proof are independently necessary.

## Evidence and limitations

The complete combinatorial proof is in RESULT.md and the bounded literal verification is reproducible with verify.py. Checked primary works are listed in RESULT.md. The theorem does not address other weights, stronger distance constraints, or error correction; priority against an undiscovered or implicit weight-three specialization remains a scholarly risk. No independent validation has been undertaken.

Self-review: passed. Independent audit: not yet performed.
