# Scientific review

## Correctness — PASS
The claim is finite and precisely specified. Every reverse-complement-closed codebook is a unique union of orbits of the Watson–Crick reverse-complement involution. The proof gives an exhaustive 56-vertex compatibility graph with a complete 56-row adjacency certificate, then uses a terminating exact-integer polynomial recurrence to count every clique. The independent direct-word backtracker does not use the graph recurrence and reproduces every coefficient and the 32 maximizers. It also checks the eight permissible nucleotide relabelings and all four orbits of maximizers. The proof is exact for four-letter words only; no finite experiment is claimed to prove an infinite-family theorem.

## Originality — PASS, qualified
The checked 2003 article by King treats Hamming and reverse-complement *distance* constraints, without forbidding cross-bifix overlaps or imposing reverse-complement *closure*. Blackburn's 2013 preprint/2015 paper treats unrestricted non-overlapping codes and establishes a maximum of 27 for four-letter words on four symbols, without closure or distance constraints. Mir and colleagues' 2013 study concerns barcodes of length six to eight. The checked sources do not give the complete polynomial or the four-orbit classification for the combined finite problem. Targeted numerical and terminology searches, including cross-bifix-free and self-complementary aliases, found no equivalent indexed table. This is a best-knowledge originality assessment, not independent historical-priority certification. An unindexed earlier finite census is the main residual risk.

## Value — PASS
Non-overlap is a synchronization condition, Watson–Crick closure is a strand-symmetry condition, and minimum Hamming distance two detects a single substitution. At word length four, reverse-complement-fixed words coexist with paired orbits and support distinct optimal compositions. The exact feasible-codebook polynomial goes beyond a maximum alone, and all 32 maximizers split into four structurally distinct symmetry classes, with two different fixed-orbit profiles. These exact frequencies give reproducible benchmark data for combining three natural coding constraints. They make no claim of biochemical optimality or applicability to longer barcodes.

## Closest sources and limitations
- O. D. King, *Bounds for DNA Codes with Constant GC-Content* (2003), DOI: 10.37236/1726, https://arxiv.org/abs/math/0306197 . Its reverse-complement-distance condition is different from closure.
- S. R. Blackburn, *Non-overlapping codes* (first arXiv posting 2013-03-05), https://arxiv.org/abs/1303.1026 . Its unrestricted extremum does not count the new constrained spectrum.
- K. Mir et al., *Short Barcodes for Next Generation Sequencing* (2013), DOI: 10.1371/journal.pone.0082933 . Biological and coding-theoretic context, different lengths and constraints.

The result is an exact finite computer-assisted classification, not an all-length construction or biochemical performance assertion. Historical-priority verification and independent proof review remain open.

Self-review: passed. Independent audit: not yet performed.
