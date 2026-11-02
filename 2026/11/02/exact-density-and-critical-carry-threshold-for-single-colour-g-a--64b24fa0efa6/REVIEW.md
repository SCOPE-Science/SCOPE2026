# Scientific review: critical g-adic sumset density

## Correctness — PASS

The restricted digits in a maximal allowed run form an integer interval; sums of exactly \(g\) such intervals fill all positions through the one adjacent carry digit without spilling into the next allowed run. This supplies a unique independent-block model. Finite-prefix modular densities are computed exactly. If the limiting product vanishes, nested periodic supersets force density zero. If positive, the forbidden-tail periodic residues are bounded uniformly by three times their total densities, so the full ordinary natural density exists. The replacement of zero-allowed summands by genuinely positive summands changes only \(O_g((1+\log x)^{g-1})\) values below \(x\); the block-coordinate transfer proves sufficiency. Below the critical count, the carry bound excludes \(g-h\) output digits at each missing position. The seven finite test cases use exact arithmetic and three independent forms of the block enumeration.

Risk: The computational tests are finite; the infinite-density conclusion depends on the supplied mathematical tail bound, which is explicitly proved. No independent proof audit has been conducted.

## Originality — PASS (provisional scientific comparison)

Min Tang, arXiv:2610.23152v1 (16 October 2026), proves minimality of the union over \(h\) digit-position classes for \(g>h\), not exact natural density of the single-colour critical self-sumset at \(h=g\). Ling–Tang (2015) treats a two-colour basis and its representation function, while the available Sun–Tao (2019) abstract and preview concern minimal bases from periodic partitions. Glasscock–Moreira–Richter (2024) analyzes fractal dimensions and independent-base sumset questions, not an arbitrary-run natural-density product. Scientific-record and prior-claim searches for the critical sum count, carry blocks, positive-density criterion, and equivalent digit-run formulations did not identify a covering result.

Risk: The full Sun–Tao (2019) article was not available for decisive checking; earlier unindexed work could implicitly give the product. Search absence alone does not certify worldwide priority. The elementary carry bound for \(h<g\) is not presented as independently novel.

## Mathematical value — PASS

This is a complete natural-density and positivity classification for arbitrary infinite coinfinite digit-support sets at a sharp arithmetic threshold. The source literature identifies critical equality between base and summand count as structurally different from the strictly subcritical regime. The theorem identifies exactly which patterns of long allowed runs overcome the infinitely many missing digit positions, and proves the striking fact that the critical sumset can have density arbitrarily close to one even though every smaller self-sumset has density zero. It requires control of infinitely many carry-block restrictions to get an ordinary natural density, not just a cylinder count or numerical observation.

Risk: The result does not address mixed-colour minimal bases or larger summand counts; its value is the exact classification within the specified single-colour family rather than a solution of the broader minimality problem.

## Closest literature and limitations

- M. Tang (2026), arXiv:2610.23152v1, Theorem 1.1, Remark 1.2, Lemma 2.2.
- D. Ling and M. Tang (2015), doi:10.1017/S0004972715000805, Theorem 1.1 and Section 2.
- C.-F. Sun and T.-T. Tao (2019), doi:10.1142/S1793042119500209; only abstract and initial preview inspected.
- D. Glasscock, J. Moreira and F. K. Richter (2024), doi:10.1112/jlms.12902, abstract, additive transversality and Section 5.

The proof and reproducible finite checker are included. The finite checker is not claimed to establish the infinite result or settle historical priority.

Self-review: passed. Independent audit: not yet performed.
