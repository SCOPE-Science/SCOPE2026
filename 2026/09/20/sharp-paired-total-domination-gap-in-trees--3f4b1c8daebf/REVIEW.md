# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. The established support-vertex inequality gives the basic gap bound. The odd equality case follows from forced support vertices, parity of paired domination, and the fact that adjacent supports would create a smaller paired set. For even order, the saturated support case is exactly a corona; pairing through a maximum matching of its core gives the exact formula for paired domination, and equality forces a star core. In the one-fewer-support case, parity and the forced-support argument imply an independent support set and a universal extra total-dominating vertex, which yields the second extremal family. These arguments cover all orders and the stated small exceptions.
- Originality: **PASS**. The fixed-order maximum gap and complete parity-sensitive extremal classification were not found in the inspected literature. The 2004 source supplies the key support-sensitive upper bound, and the 2022 tree paper supplies modern paired-domination structure and the subdivided-star benchmark, but neither inspected source states the order-only gap theorem or its full equality classification.
- Scientific value: **PASS**. The result gives the exact extremal gap for every tree order and a complete equality classification with a genuine odd/even structural split. That is a natural extremal graph-theoretic classification, not merely a numerical consequence of the support bound.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in `AUDIT.json` without being relabeled as fresh independent evidence.
