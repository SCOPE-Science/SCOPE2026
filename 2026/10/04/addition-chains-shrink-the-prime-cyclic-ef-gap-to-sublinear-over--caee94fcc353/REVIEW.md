# Review

## Correctness
PASS. Any addition chain to \(p\) can be read directly as a sequence of atomic addition relations among selected nonzero residues in \(\mathbb Z_p\), with the final addition landing at the named identity. Preservation in \(\mathbb Z_q\) forces every response to be the corresponding integer multiple of the first response and ultimately forces \(py=0\); because \(q\) is a different prime, this implies \(y=0\), contradicting preservation of inequality from the named identity. The \(p+1\) and \(p-1\) variants are checked separately, including the case where a chain to \(p+1\) passes through \(p\). Yao's singleton power-evaluation bound gives the stated \(n+O(n/\log n)\) consequence.

## Originality
PASS with residual priority risk. Gomaa's dissertation explicitly gives the \(n+1\) lower and \(2n\) upper bounds and asks whether the gap can be narrowed; it also gives sparse exact congruence systems, but no addition-chain formulation or sublinear additive gap. published-finding corpus searches and public-web searches combining Gomaa/cyclic groups/EF games with addition chains, power evaluation, and quantifier depth found no matching or stronger statement. The own ledger's immediately preceding finding gives only the weaker explicit \(n+\lceil n/2\rceil\) upper bound, so the present result is a strict quantitative strengthening rather than a duplicate.

## Value
PASS. The result changes the prime-order upper bound from a constant-factor gap to a sublinear additive gap: \(n+O(n/\log n)\) versus the known \(n+1\) lower bound. It also identifies a general exactness criterion \(\Lambda(p)=n+1\) and connects a mature arithmetic optimization problem—addition-chain length—to finite-model-theoretic distinguishing depth. This directly addresses the archived open direction and materially strengthens the prior ledger entry.

## Closest literature and limitations
The closest finite-model-theory source is Gomaa's 2007 dissertation and 2010 journal paper; the closest arithmetic input is classical addition-chain theory, with Yao's 1976 bound providing the asymptotic estimate. The theorem is restricted to distinct prime-order cyclic groups and does not preserve Gomaa's five-variable guarantee.

Same-model review: passed. Independent audit: not yet performed.
