# Self-review

## Correctness
**PASS.** The heterozygosity identities reduce both statistics to exact rational functions of the allele-count gap \(d\) and pooled-frequency imbalance \(t\). For fixed nonzero \(d\), \(G_{ST}\) is strictly increasing in \(t\) while Jost \(D\) is strictly decreasing. Complete enumeration of all positive biallelic two-population grids through denominator \(5\) gives no reversal for \(m\le4\) and exactly one symmetry class at \(m=5\). The explicit family proves persistence for every larger denominator. The embedded verifier returns `VERIFY_OK`.

Risk: the theorem uses exact population frequencies rather than finite-sample bias-corrected estimators.

## Originality
**PASS.** Jost's foundational paper already establishes that \(G_{ST}\) can misrank differentiation and supplies broader multi-allelic examples, so generic disagreement is treated as prior art. Meirmans and Hedrick give the exact relation between Jost \(D\), \(H_S\), and \(H_T\) and note that small-population-count pairwise comparisons can diverge. The checked sources and exact searches did not state the fixed-gap antimonotonicity formula for the biallelic two-population slice or the sharp positive-grid denominator \(5\) with its unique first reversal.

Risk: the algebra is short enough that an unindexed pedagogical derivation could exist.

## Value
**PASS.** The \(G_{ST}\)-versus-\(D\) distinction is a long-standing interpretive issue in population genetics. The theorem isolates a transparent mechanism in the smallest nontrivial biallelic setting: two population pairs can have the same allele-frequency difference yet be ranked oppositely solely because their pooled frequency lies at different distances from one half. The sharp polymorphic grid and persistent family make this a useful diagnostic for interpretation and software validation rather than an arbitrary numerical example.

Self-review: passed. Independent audit: not yet performed.
