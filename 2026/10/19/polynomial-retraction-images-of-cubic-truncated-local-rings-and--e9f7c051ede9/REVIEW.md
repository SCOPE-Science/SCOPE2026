# Review: Polynomial retraction images of cubic truncated local rings

## Correctness — PASS

The stated ring is the equal-characteristic chain ring \(R=\mathbb F_q[t]/(t^3)\), and the objects counted are distinct polynomial functions under composition. Hasse--Taylor expansion yields local jets \((s,r)\mapsto(u+\alpha s,w+vs+\beta s^2+\alpha r)\). The derivative coefficient \(\alpha\) is forced to \(0\) or \(1\) for a fixed fiber of an idempotent, yielding only constant or identity functions there. The CRT for \((X-a)^3\) justifies independent gluing. All factors of the exact formula account for disjoint residue fibers; boundary cases \(q=2\), rank one and full rank are handled. Exact finite checks over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) agree; infinite validity follows from the symbolic proof rather than enumeration.

## Originality — PASS within examined coverage

Al-Maktry (arXiv:2002.01304v1) and Al-Ezeh--Al-Maktry--Frisch (arXiv:1910.00238v1) study polynomial functions on split square-zero dual numbers. Their inspected formulas do not imply the specific length-three chain-ring retraction spectrum because here the radical square is nonzero. Aichinger (DOI:10.1017/S0013091599001418), Theorem 1.1, characterizes near-ring ideal ranges, rather than arbitrary fiberwise image subsets with exact polynomial-map multiplicities. An earlier square-zero image/retract theorem likewise has different nilpotence hypotheses and cannot be used by renaming parameters. The quadratic Hasse jet and exceptional binary function identity are the new ingredients. Targeted equivalence and table searches found no matching full formula, but searches do not certify novelty.

## Value — PASS

The first nonsquare-zero finite chain-ring stage is a natural test case for polynomial-function semigroups. The result classifies all possible retract images and their multiplicities for infinitely many finite fields, detects a binary jet exception, and identifies sharp image-size extremes. These exact invariants are not limited to an arbitrary small numerical slice.

## Residual scientific and access risks

The result does not treat mixed-characteristic chain rings, other nilpotence lengths, or multivariate polynomial self-maps. The complete Frisch (1999) and Bulyovszky--Horvath (2017) sources were not obtained; equivalent older near-ring terminology could conceal a pre-existing formula. Direct local computational tests are finite. The detailed proof remains subject to independent review.

Self-review: passed. Independent audit: not yet performed.
