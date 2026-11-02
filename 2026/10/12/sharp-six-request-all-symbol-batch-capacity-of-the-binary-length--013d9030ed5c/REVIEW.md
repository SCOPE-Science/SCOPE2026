# Mathematical assessment

## Correctness

**PASS.** In the affine evaluation generator \(g_x=(1,x)\) over \(\mathbb F_2\), the seven-identical-demand bound follows because six disjoint recovery groups avoiding the requested coordinate require at least eighteen of the fifteen remaining storage coordinates. The six-demand lower bound is established by a complete finite witness procedure: all \(\binom{21}{6}=54{,}264\) six-demand multisets admit six disjoint singleton-or-triple supports. For every accepted set, the underlying five-bit column-sum identity and target multiplicity are checked. This proves the fixed code claim but no longer-length analogue.

## Originality

**PASS, with priority qualifications.** Baumbaugh et al. (2018, Theorems 4.13–4.14) establish a four-query Reed–Muller batch construction. Boruchovsky et al. (2026, Definition 2 and Proposition 29) introduce the all-symbol batch formulation and derive the general upper bound; their Section 5 identifies Reed–Muller all-symbol behavior as a future direction. Neither cited theorem supplies the complete six-mixed-request lower bound. A parallel one-step majority-logic decoder and individual-symbol availability address different assignment constraints. The binary simplex functional-batch results use distinct storage sets/parameters. A historical orthogonal-parity-check equivalence remains a possible priority risk, especially in literature not available in full text.

## Value

**PASS.** The fixed-code maximum is a natural and exact invariant of a classical distributed-storage code. Its full mixed-demand six-query saturation is not a consequence of the six-identical-query guarantee; the full enumeration supplies a reproducible finite witness method. The result is useful as a locality-three benchmark without asserting broader Reed–Muller classification.

## Limits

Recovery is linear over \(\mathbb F_2\), with one physical read per server per batch and repeated requests allowed. The algorithmic certificate covers this fixed 16-coordinate code, not general length or running-time optimality. Computational verification is not formal-machine certification.

## Primary sources

- Baumbaugh, Diaz, Friesenhahn, Manganiello and Vetter (2018), *Batch codes from Hamming and Reed–Muller codes*, Theorems 4.11–4.14, DOI 10.13069/jacodesmath.466634.
- Boruchovsky, Gruica, Niemann and Yaakobi (2026), *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041v2, especially Definition 2, Proposition 29 and Section 5.
- Ly and Soljanin (2026), *Optimum 1-Step Majority-Logic Decoding of Binary Reed–Muller Codes*, arXiv:2508.08736v3, especially Section IV.
