# Scientific review of a finite tetranucleotide synchronization tradeoff

## Correctness — PASS
The proposed exact optimum is a finite theorem with a complete computational proof. The orbit reduction from 96 GC-balanced words to 52 reverse-complement orbits is exhaustive. Forbidden supports on at most three orbits exactly encode comma-freeness and framed Hamming distance. The exhaustive branch recurrence uses only an explicitly justified upper bound from pairwise-incompatible color classes; it loses no permissible codebooks. The executable certificate reconstructs the full inventory and direct-checks all 224 maximal codebooks, including the asserted complement-preserving symmetry actions. The verifier produced `VERIFY_OK` after a complete fresh execution. This verifies the claimed length-four theorem, not any asymptotic property.

## Originality — PASS (qualified)
Golomb–Gordon–Welch (1958) and Jiggs (1963) study unrestricted comma-free codes without the simultaneous nucleotide constraints. King (2003, arXiv:math/0306197) studies constant-GC Hamming codes and reverse-complement *separation*, which forbids positive-distance RC-closed nonempty codes, and does not impose comma-freeness. Prior near-neighbor results on reverse-complement-closed non-overlapping codes use a strictly stronger grammar and cannot bound the comma-free family, whose distance-one code attains 21 words. Previous binary comma-free and four-nucleotide deletion-correcting results are distinct. Targeted literature and research-record searches did not reveal a stronger covering theorem or exact table for these three combined constraints. Unindexed historical sources remain a genuine residual priority risk, and no independent historical certification is asserted.

## Value — PASS
For a natural DNA-style framed codebook constrained simultaneously by GC balance, strand symmetry and self-synchronization, the exact capacity loss from no distance restriction (21) to single-substitution detection (17) and correction (7) is meaningful. The complete maximizer census (136/16/72) and symmetry orbits (17/2/9), rather than a single convenient construction, characterize every solution at these three canonical thresholds. This is a self-contained finite classification, not a claim about biochemical behavior, desynchronization after substitution, or longer block lengths.

## Limitations and validation status
The conclusions apply exactly to four-nucleotide, two-GC, Watson–Crick-closed, comma-free codes, with Hamming distance on correctly framed blocks. The finite verifier is supplied for replay; no independent external scientific audit or proof of historical priority has been carried out.

Self-review: passed. Independent audit: not yet performed.
