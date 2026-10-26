# Review of the parity-sensitive semiprime classification

## Correctness — PASS
For primes \(p>q>a\), the shifted divisibility is equivalent to \(p-a\mid q-1\) and \(q-a\mid p-1\), because \(\gcd(a,p-a)=\gcd(a,q-a)=1\). Setting \(r=p-a\), \(s=q-a\), and \(c=a-1\), the exact parameter equations \(s+c=ur\), \(r+c=vs\) give the unique rational formulas with positive denominator \(uv-1\). Conversely, their integer solutions restore both divisibilities. The separate parity argument forces even \(u,v\) when \(a\) is even. Monotonicity of \((v+1)/(uv-1)\) gives sharp universal bounds, with prime examples attaining equality. The included finite verifier confirms 99 independent parameter instances but is not used to prove the infinite statement.

## Originality — PASS with residual risk
Wright (arXiv:2607.02738, first posted 2026-07-02) studies the same shifted Carmichael condition but proves conditional abundance and prescribed-GCD results by constructions with many prime factors. The inspected primary introduction, main theorems and proof do not state this finite two-prime parametrization or the sharp odd/even bound. Zheng's earlier \((-1,1)\)-Carmichael work uses a different ordered pair of shifts and is documented here at abstract level only. Searches of published records, known Carmichael tables, and related archived number-theory results did not identify an equivalent statement; however, search absence does not prove priority. The familiar modular reduction is shared background, not claimed as the contribution.

## Mathematical value — PASS
The least nontrivial factor-support case for the generalized Korselt condition behaves differently from ordinary Carmichael numbers: squarefree two-prime examples can occur but only below a *sharp shift-dependent linear barrier*. The complete integer-parameter bijection makes that branch decidable for every shift, while the parity split quantifies a genuine structural restriction (a factor of \(5/7\) for even shifts versus \(3\) for odd shifts when normalized by \(a-1\)). The two sharp examples demonstrate the optimality of the bounds. This distinguishes the rank-two branch from the many-prime asymptotic constructions without claiming results for smaller prime factors or for arbitrary squarefree integers.

## Closest literature and limitations
Wright, *\((a,a)\)-Carmichael numbers and greatest common divisors of \(p-a\)* (arXiv:2607.02738, 2026) is the closest source; Zheng (arXiv:2207.08641) is earlier nomenclature for a different shift pair. The prime factors must be distinct and larger than \(a\). The proof is unconditional, but bibliographic completeness cannot be guaranteed; the earlier Zheng paper was not inspected in full and absence of a matching record was not treated as a proof of uniqueness. No independent audit or certification was undertaken.

Self-review: passed. Independent audit: not yet performed.
