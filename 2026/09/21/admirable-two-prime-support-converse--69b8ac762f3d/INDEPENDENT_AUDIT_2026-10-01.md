# Independent mathematical audit — Two-prime-support admirable numbers: a complete converse classification

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The excess \(E=\sigma(2^a p^b)-2^{a+1}p^b\) reduces to \(E=M(1+p+\cdots+p^{b-1})-p^b\) with \(M=2^{a+1}-1\). Parity forces \(b\) odd. For \(b=1\), the two possible divisor shapes give exactly the binary-deviation, isolated \(40\), and even-perfect-divisor families. For odd \(b\ge3\), splitting by \(v_p(M)\) eliminates the zero-valuation case, forces \(b=3\) and \(M=p\) in the intermediate case, and rules out the high-valuation case using the exact two-adic valuation of the geometric sum. Thus the four families are exhaustive. The repository's bounded computation is consistent with the proof but is not used as an infinite certificate.

Checked sources: Assigned RESULT.md and artifact source; Firoozbakht--Hasler 2010 full text; Sachs 1960 complete three-page article; OEIS A111592.

Residual correctness risks: The finite computation checks only a bounded box and is corroborative; the infinite converse rests on the valuation proof..

## Originality

**PASS.** The individual sufficient constructions are substantially prior: Firoozbakht--Hasler give the binary-deviation construction, the Mersenne-cube construction, and perfect-divisor mechanisms. The complete 1960 Sachs article defines admirable numbers and lists elementary examples/conjectures but contains no prime-support classification. The surviving contribution is the converse proving that these mechanisms exhaust support \(\{2,p\}\), with odd-prime exponent only \(1\) or \(3\); no earlier converse was located.

### Equivalent formulations

Searches/sources: Resultary semantic search: admirable numbers \(2^a p^b\) converse Mersenne cube; Firoozbakht--Hasler 2010 full text; Sachs 1960 complete article; OEIS A111592.

Evidence: The published-result search returned the audited theorem as the exact match. Firoozbakht--Hasler provide the relevant sufficient families but do not state their exhaustiveness on two-prime support. Sachs gives the original definition, small examples and broad elementary observations only.

No equivalent support-\(\{2,p\}\) converse classification was found.

### Broader coverage

Searches/sources: Firoozbakht--Hasler equations \(\sigma(x)=2(x+m)\); OEIS admirable-number constructions; older admirable-number literature.

Evidence: The 2010 framework is broader as a family of divisor-sum equations, but its stated theorems are constructions rather than a converse for arbitrary \(2^a p^b\). OEIS records construction data, not the complete exponent restriction.

A broad construction framework does not dominate the audited necessity theorem.

### Exact database or table

Searches/sources: OEIS A111592 complete entry; Resultary exact theorem search.

Evidence: OEIS lists admirable numbers and the binary-deviation family but no statement that \(b\in\{1,3\}\) is exhaustive for support \(\{2,p\}\). No earlier exact theorem record was located.

The classification is not a restatement of a sequence table; the proof covers infinitely many exponents.

### Claim versus prior implication

Searches/sources: Do the Firoozbakht--Hasler sufficient families imply exhaustiveness?; Does Sachs's definition imply an exponent restriction?.

Evidence: None of the prior sufficient constructions excludes all other odd exponents. The audited proof's \(p\)-adic and two-adic case analysis is required to rule out \(b\ge5\) and the unwanted \(b=3\) cases.

The converse is not mechanically implied by the prior constructions.

### Source inspections

- **Variations on Euclid's Formula for Perfect Numbers** — PARTIAL_PRIOR.
  Identifier: https://cs.uwaterloo.ca/journals/JIS/VOL13/Hasler/hasler2.html
  Trigger: Closest source containing the same construction mechanisms.
  Material read: Complete open Journal of Integer Sequences article, including Theorem 1.1, Remark 1.4, Proposition 1.6 and the perfect-divisor constructions.
  Method: lawful open-access full text
  Evidence: It owns the principal sufficient families but does not state the two-prime-support converse.
- **Admirable Numbers and Compatible Pairs** — NOT_COVERING.
  Identifier: https://www.jstor.org/stable/41184328
  Trigger: Original source for the notion and the strongest historical-overlap risk.
  Material read: Complete three-page article, including definition, examples and all ten concluding observations/conjectures.
  Method: lawful full text
  Evidence: The article introduces admirable numbers and elementary examples such as \(12,24,42\), but contains no prime-support or exponent classification.
- **OEIS A111592** — DATABASE_CONTEXT.
  Identifier: https://oeis.org/A111592
  Trigger: Current database for admirable numbers and known constructions.
  Material read: Complete public sequence entry, comments and references.
  Method: public database
  Evidence: It records the binary-deviation construction and data but no exhaustive \(2^a p^b\) converse.

Residual originality risks:
- A later or obscure problem-note treatment may contain the same converse under divisor-sum-equation language, but the original and closest construction sources were inspected in full.

## Scientific value

**PASS.** The theorem closes a natural prime-support slice of the admirable-number problem: it turns several previously sufficient Mersenne/perfect-number mechanisms into an exhaustive classification and proves the strong exponent restriction \(b\in\{1,3\}\). This is a complete structural classification rather than a bounded census.

Residual value risks: The result does not address two odd primes or larger prime support..

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
