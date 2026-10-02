# Independent mathematical audit — SCOPE-20260920-fc59e27647cf

Final disposition: **PASS**.

## Correctness
**PASS** — The complete-sequence proof is correct. The divisor weights of \(2^a\) form a complete base block of total \(2^{a-1}+2\). For each positive \(p\)-adic exponent, the Carmichael weights factor as \(p^{j-1}\operatorname{lcm}(p-1,\lambda(2^i))\); after normalization the block is a run of ones followed by powers of two, so once its least entry fits there are no internal gaps. Comparing that least entry with the exact previous-block total yields the stated necessary-and-sufficient inequality. The \(b=1\) threshold follows immediately, and adjoining primes up to a suitable half-square-root scale gives the counting lower bound. A fresh independent direct complete-sequence check on a bounded grid found no mismatches, as supplementary evidence only.

## Originality
**PASS** — The complete Schwab-Thompson primary paper defines \(\lambda^\star\)-practical numbers, proves an upper bound, and explicitly reports that it could not prove a reasonable lower bound. Its general prime-adjunction theorem assumes multiplicativity and its proof uses product factorization, so it does not apply mechanically to the nonmultiplicative Carmichael function. Targeted Resultary searches found no published two-prime-support classification, threshold, or square-root-order lower bound beyond the assigned record. Originality therefore passes to the best of current knowledge.

### Equivalent formulations
Equivalent subset-sum and divisor-weight formulations were compared directly.

### Broader coverage
The stronger-looking general theorem does not dominate the Carmichael case.

### Exact database or table
The absence check is supporting evidence; novelty primarily rests on the primary paper's explicit gap and the inapplicability of its multiplicative adjunction theorem.

### Claim versus prior implication
The final classification and counting consequence require a nonmultiplicative block analysis not supplied by the prior theorem.

## Value
**PASS** — This is a natural exact classification on the first genuinely nonmultiplicative two-prime-support family for the Carmichael subset-sum notion, and its simplest slice produces a polynomial-order lower bound for a counting function whose foundational treatment explicitly lacked one. The result is both structurally and quantitatively motivated.

## Source inspections
- **A generalization of the practical numbers** (https://arxiv.org/abs/1701.08504): complete primary text relevant to Theorem 2.3 and Section 5.2 on Carmichael practical numbers Method: primary full-text inspection. Assessment: PRIMARY_SOURCE_LEAVES_LOWER_BOUND_OPEN. Evidence: The paper treats \(\lambda^\star\) separately, proves an \(O(X/\log X)\) upper bound, and explicitly says it had not obtained a reasonable lower bound; its adjunction theorem is stated and proved for multiplicative functions.

## Checked sources
- https://arxiv.org/abs/1701.08504

## Residual risks
- Equivalent results could exist under older Carmichael subset-sum terminology not captured by the searches.
- The counting lower bound is not expected to be sharp and does not settle the conjectural \(X/\log X\) scale.
