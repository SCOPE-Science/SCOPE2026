# Independent mathematical audit — An effective criterion for Zumkeller numbers of the form 2^a p q

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** For \(p>M=2^{a+1}-1\), the Bhaskara Rao--Peng excess criterion gives exactly \(D=(M(M+1)-(p-M)(q-M))/2\). Under abundance, \(D<pq\), so a representing divisor subset cannot use any divisor containing both odd primes. The three remaining binary divisor blocks independently realize exactly \(x+py+qz\) with \(0\le x,y,z\le M\). The abundance inequality also gives the claimed finite bounds. An independent exact recomputation of every abundant candidate for \(1\le a\le4\), using a separate subset-sum implementation, reproduced candidate counts \(1,3,44,81\) and exactly the displayed exception lists with zero discrepancies.

Checked sources: Assigned RESULT.md and artifact source; Bhaskara Rao--Peng, On Zumkeller Numbers, Facts 3, 6 and 10; Mahanta--Saikia--Yaqubi 2020; Independent exact bounded recomputation.

Residual correctness risks: The low-exponent computation proves only the displayed \(a\le4\) classifications; the arbitrary-\(a\) theorem rests on the analytic finite-reduction proof, not on enumeration..

## Originality

**PASS.** Best-of-knowledge originality survives. The foundational paper supplies the general divisor-subset and product facts used in the proof, and the 2020 paper completely treats numbers with only two distinct prime factors while giving broader bounds and layered-number results. Neither inspected source states the classical Zumkeller criterion for the three-prime support \(\{2,p,q\}\), the bounded three-coefficient reduction, or the complete \(a\le4\) exception lists.

### Equivalent formulations

Searches/sources: Resultary semantic search: Zumkeller \(2^a p q\) squarefree odd part effective criterion; arXiv:0912.0052; arXiv:2008.11096.

Evidence: The published-result search returned the audited finding as the exact match; nearby findings concern different divisor-partition families. Bhaskara Rao--Peng Fact 3 gives the generic excess-as-distinct-proper-divisor-sum test, not the specialized three-block criterion. Mahanta--Saikia--Yaqubi characterize the two-distinct-prime-factor case, not the three-distinct-prime support used here.

The audited statement is a nontrivial specialization of a generic subset-sum criterion, but no equivalent closed criterion or finite reduction for this support was found.

### Broader coverage

Searches/sources: Mahanta--Saikia--Yaqubi 2020 complete two-prime-factor theorem and higher-support bounds; Somu--Kukla--Tran 2023 Zumkeller results; general Zumkeller literature search.

Evidence: The 2020 theorem is broader in some layered-number directions but does not dominate the classical three-support classification. The 2023 paper studies additive and infinitude properties rather than this support-restricted divisor partition.

No inspected stronger theorem implies the exact coefficient criterion or its low-exponent complete classifications.

### Exact database or table

Searches/sources: Resultary exact/semantic search for the theorem and exception pairs; OEIS A083207 and linked Zumkeller references.

Evidence: No earlier exact record or standard table containing the \(a=1,2,3,4\) exception lists was located. The independent computation reproduced all listed exceptions from the proved finite bounds.

The table is not a lookup from an existing database; it is an exhaustive consequence of the finite region proved in the theorem.

### Claim versus prior implication

Searches/sources: Apply Bhaskara Rao--Peng Facts 3, 6 and 10; Compare the 2020 two-prime-factor classification with support \(\{2,p,q\}\).

Evidence: Facts 6 and 10 imply the automatic region \(p\le M\), but Fact 3 alone leaves a general divisor subset problem. The reduction to three independent binary blocks uses the new observation \(D<pq\) and the exact cancellation in the excess. The 2020 two-prime theorem does not imply a theorem with two odd primes.

Part of the theorem is directly prior, and is treated as such; the bounded exceptional-region criterion and classifications require additional structure.

### Source inspections

- **On Zumkeller Numbers** — SUPPORTING_NOT_COVERING.
  Identifier: https://arxiv.org/abs/0912.0052
  Trigger: Foundational source explicitly cited for all three proof inputs.
  Material read: Full arXiv text, including Facts 3, 6 and 10 and their hypotheses.
  Method: lawful open-access full text
  Evidence: It supplies the general excess criterion, prime multiplication closure, and the \(2^a p\) automatic family, but not the \(2^a p q\) exceptional-region criterion.
- **Some properties of Zumkeller numbers and k-layered numbers** — NEARBY_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2008.11096
  Trigger: Closest later classification paper on prime-factor support.
  Material read: ArXiv text/abstract and relevant classification portions concerning two distinct prime factors and higher-support layered results.
  Method: lawful open-access text
  Evidence: It completely characterizes the two-distinct-prime-factor case and studies layered variants; the audited classical three-support theorem was not located.

Residual originality risks:
- A differently notated specialization of the general divisor-partition criterion may exist in unindexed recreational-number-theory literature.

## Scientific value

**PASS.** The theorem treats the next natural squarefree odd-support family after the known two-prime-factor case, splits it into an infinite automatic region and a rigorously finite exceptional region for every fixed binary exponent, and gives complete first-exponent classifications. This is a motivated structural reduction and natural finite classification rather than an arbitrary bounded census.

Residual value risks: For general \(a\), the result is an effective criterion rather than a closed-form classification..

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
