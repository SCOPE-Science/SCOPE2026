# Scientific review of Frobenius-orbit rank spectra

## Correctness — PASS

The claim is exact for all finite abelian groups, all automorphisms, and all prime-power coefficient fields of characteristic coprime to the group order. Its key premise, the Fourier product identity, follows directly by evaluating a character on \(\varphi(x)+(1-\varphi)y\) and agrees with Ta, arXiv:2610.20306v1, Proposition 5.1. Fourier transforms commute with Frobenius on the coefficients. Each orbit of size \(d\) in the image of the dual displacement map has \(fd\) preimage coordinates. Zero/nonzero assignments on those fibers yield the left rank increments of \(d\), while evaluation on image coordinates yields right rank increments of \(fd\). The product enumerators and the exact ordered zero-product count follow by counting disjoint Frobenius-stable blocks. Matrix ranks do not change under scalar extension. Every executable check in `verify.py` finishes with `VERIFY_OK`. Computations are finite tests; the general theorem is justified by the proof, not extrapolation. The coprimality hypothesis is necessary for this Fourier argument.

## Originality — PASS, with residual priority risk

The original results of Bardakov–Passi–Singh (arXiv:2001.06843) concern existence of zero divisors over ordered settings and special idempotents. Elhamdadi–Ta–Virgin (arXiv:2609.03799v1, Theorem 3.2) and Ta (arXiv:2610.20306v1, Proposition 5.1) already establish the foundational Fourier product law; this law is credited, not claimed. Ta's principal zero-divisor theorem concerns non-inert medial quandles, and its finite Alexander discussion concerns augmentation/idempotents rather than a complete finite-field rank census. Churchill et al. (arXiv:2608.09149v1, Section 6) examine zero-divisor graphs for specific *extended* quandle rings, not uniform spectra in the original algebras. Direct comparisons against related available results on idempotents, square-zero subspaces, and two-sided ideals find no statement implying both rank distributions and the ordered zero-product formula. The four comparisons in `AUDIT.json` detail the exact novelty boundary. A general algebraic Fourier-counting theorem or inaccessible literature could still implicitly subsume this result, so independent priority verification remains open.

## Value — PASS

A complete multiplication-rank distribution and zero-product probability are natural structural statistics of a finite nonassociative algebra. This theorem computes both orientations simultaneously throughout an entire infinite class without assuming the latin property or a splitting field, and reduces all arithmetic to the displacement subgroup and Frobenius orders. The asymmetry is substantive: the nonlatin left rank is at most \(|(1-\varphi)A|\), while the right rank can reach \(|A|\). The explicit noncyclic example \(C_3\times C_3\), with one fixed and one inverted coordinate, has left ranks \(0,1,2,3\) but right ranks \(0,3,6,9\). The result classifies the precise invariant rather than merely observing that zero divisors exist. It does not claim algebra isomorphism, a modular-characteristic extension, or an application theorem.

## Remaining limitations and checks

The coefficient characteristic must be coprime to \(|A|\), and the result includes zero as an allowed pair factor. Finite examples were fully enumerated only at feasible orders; arbitrary cases are covered by a proof. Previously available results using general character theory might imply some aspects, and independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
