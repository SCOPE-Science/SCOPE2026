# Scientific assessment: two-prime index rigidity for associated Pell gcds

## Correctness — PASS

The claim ranges over all prime powers and all products of exactly two prime powers with distinct bases. The proof verifies all normalizations, including \(Q_0=Q_1=1\), the odd-prime restriction on the lifting lemma, the parity exceptional case, and exact exponents. Its three critical facts are: Frobenius \(Q_{\ell m}\equiv Q_m\pmod\ell\); odd-prime lifting \(\nu_\ell(Q_{m\ell})=\nu_\ell(Q_m)+1\) when \(\ell\mid Q_m\); and the order bound \(\operatorname{ord}_{\mathbb F_{p^2}^\times}((1+\sqrt2)/(1-\sqrt2))\mid(p-1)\) or \(\mid(p+1)\), excluding the smaller prime. These combine to prove the complete dichotomy without assuming primitive divisors or conjectures. Exact modular tests corroborate the symbolic proof but are not treated as an infinite certificate.

## Originality — PASS relative to examined literature

The closest directly relevant paper, Mbirika–Schrader–Spilker, arXiv:2301.05758v1 (2023), Section 6.2, asks for exact \(\gcd(Q_k,k)\) in Question 31. Its Conjecture 32 is explicitly contradicted by \(k=3\cdot2^a\) with \(a\ge2\), since the entry point \(e_Q(3)=2\) divides these indices although \(\gcd(Q_k,k)=1\). Theorem 28 uses, rather than computes, the index gcd. In arXiv:2408.14632v1, the companion Lucas results concern periods and entry points; the Flórez–Higuita–Mukherjee paper (Integers 18 A14) concerns gcds of sequence values, not a value and its numerical index. Searches for the exact two-prime-power formula, larger-prime-only behavior, lifting and Lucas aliases, plus checks against earlier recorded claims, yielded no covering statement. Absence from checked literature is not proof of unique priority; a classical implicit consequence remains possible.

## Mathematical value — PASS

The result completely solves a natural first nontrivial support class of a published gcd question, pinpoints the only possible prime-power factor of an index gcd, and explains the full exponent phenomenon rather than a binary divisibility test. Its infinite counterexamples to an explicit published conjecture identify a real missing rank constraint. This is a structural classification on an infinite domain, not an isolated congruence or arbitrary computational slice.

## Limits and evidence

The proof establishes no claim for indices with three or more distinct prime factors, nor a global corrected entry-point criterion. The reproduction file `verify.py` and its saved output check a finite sample independently by modular integer arithmetic. The full paper and specific sections were examined as stated above; unindexed equivalent work is the principal remaining originality risk. No independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
