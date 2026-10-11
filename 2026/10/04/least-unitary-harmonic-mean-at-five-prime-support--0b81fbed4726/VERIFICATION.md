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

Hagis--Lord's lower bound reduces the five-prime minimum to integer targets \(10,11,12,13\). For a fixed target, monotonicity of \(x/(x+1)\) gives a proved finite upper bound on each ordered prime-power component. After four choices, the fifth component is forced by \(Px/(x+1)=h/32\), so exact integrality, prime-power, order, and distinct-base checks are necessary and sufficient. The bundled exact rational recursion therefore exhausts all cases: none for 10--12 and exactly the two stated component sets for 13.

## originality

PASS

Prior sources establish fixed-support finiteness, lower bounds, the at-most-four-prime classification, and bounded tables. OEIS already contains \(5460\) and \(8190\), so their existence is not new. What is new is the unrestricted exclusion of every larger five-prime number with mean 10, 11, or 12. Resultary returned the assigned theorem as the exact hit and no stronger five-prime classification. Full older paper text was not available through the web routes used here, so that access risk is retained.

## value

PASS

Exact support five is the first layer beyond the published small-support classification, and the least attainable unitary harmonic mean is a natural extremal invariant. The result turns known candidate values into a rigorous unrestricted classification with exactly two minimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
