---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The proof correctly separates fixed universality from fixed word length. For binary universality index \(k\), monotonicity under taking a same-index subsequence reduces every extremal candidate to \(k\) two-letter arches. The two boundary matrices act on a row state by \((x,y)\mapsto(x+y,y)\) or \((x,x+y)\), so sorting coordinates gives the sharp Fibonacci envelope and fixed-index maximum \(F_{k+3}\). For even length \(2m\), the largest feasible index is \(m\), yielding \(F_{m+3}\). For odd length \(2m+1\), exactly one extra symbol occurs at index \(m\); the interior exceptional block collapses the state to equal coordinates and the inequality \(F_{j+1}F_{m-j+3}\le 2F_{m+1}\) controls every interior location, while the six terminal three-letter components give the same bound. Alternating arches plus the stated terminal block attain it. A fresh independent exhaustive reconstruction through length ten reproduced \(1,3,2,5,4,8,6,13,10,21\), matching the theorem; the all-length conclusion rests on the transfer and exceptional-block arguments.

## originality

PASS

The closest full primary source develops the same SAS/arch machinery, proves a gluing lemma, and proves that its alternating \(A_k\) words maximize the number of SAS at fixed universality. Crucially, that section explicitly assumes a large even alphabet with \(\sigma\ge4\), and its quantitative proposition establishes exponential growth rather than the binary Fibonacci count. It does not state the fixed-word-length binary extremal problem, where lower universality indices compete and the odd case has one unavoidable excess symbol. The audited odd-length analysis is therefore not a parameter substitution into the inspected theorem. Current Resultary searches for binary fixed-length SAS maxima returned no equivalent result.

## value

PASS

Fixed word length is the natural extremal parameter for absent-subsequence complexity, and the binary alphabet is the smallest nontrivial case. The sharp parity split, explicit extremizers, and one-extra-symbol obstruction turn the general SAS framework into a complete exact classification rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
