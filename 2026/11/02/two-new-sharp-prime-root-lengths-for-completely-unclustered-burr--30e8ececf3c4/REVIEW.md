# Scientific review

## Correctness (C): PASS
The proof gives all stable sorting formulas, the exact unmodified modular permutation, the complete changed-edge routes, and the one-cycle deduction using the order of \(2\) modulo \(p\). The sorted-block matching calculation applies for every \(r\equiv0\pmod4\), including the boundary \(r=0\). Combining the proved one-cycle property with the established cyclic-run/Hamming identity and universal lower bound yields both exact optima. The executable checker tests all stable arrows, cycle lengths, run counts, and independent cyclic BWT reconstructions on the stated finite sample. Finite enumeration is supporting evidence, not a replacement for the symbolic argument. Risk: reliance on the published general BWT identity and universal lower bound, not independently reproved here.

## Originality (O): PASS, subject to priority limits
The closest primary literature is Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267 (2026-05-31), which establishes sharpness at \(p-1\) and \(p\), not the new lengths \(p+2\) and \(p+3\). Fici et al., arXiv:2508.20879 / CPM 2026, establish existence of completely unclustered images for arbitrary lengths without establishing the minimum possible input cyclic runs. Accessible prior finite classifications through length \(64\) overlap with small individual cases but do not cover the new uniform conditional theorem or examples beyond \(64\). Targeted literature and semantic research searches did not reveal a covering statement. Residual risks are unindexed work and the possibility of a different general theorem implying these values.

## Value (V): PASS
The recent extremal problem asks where the sharp two-to-one clustering boundary occurs. Two new prime-root lengths with explicit one-cycle constructions extend its previous arithmetic sharpness theorem beyond the original adjacent pair, with infinitely many *conditional* candidate lengths and concrete additional examples beyond existing finite tables. The splice proof is structural and may be reusable for other length offsets; no unconditional infinitude or downstream theorem is claimed.

## Limits
The assertion is conditional on a multiplicative-order hypothesis and applies to ternary and larger ordered alphabets. It does not settle all lengths or all optimal inputs. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
