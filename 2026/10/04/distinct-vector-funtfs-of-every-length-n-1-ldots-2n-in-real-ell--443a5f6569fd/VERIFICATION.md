---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The displayed positive k-by-n matrix has row sums one, column sums k/n, and distinct rows. The standard basis vectors and added positive rows all have l1 norm one; the proposed functionals have dual norm one and norm their paired vectors. The standard contribution to the frame operator is (1+k/n)I-(k/n)J and the added rows contribute (k/n)J, leaving ((n+k)/n)I. Exact-rational replay verified positivity, margins, distinctness, norming, and every frame-operator entry for all 77 pairs with 2<=n<=12 and 1<=k<=n.

## originality

PASS

Cheng-Heil explicitly state the seven-vector real l1^5 case as Question 2.13 and, later, say they do not know constructions throughout the intermediate no-repetition range. The assigned positive prescribed-margin construction answers that question and uniformly supplies every length n+1 through 2n. No Resultary hit predating the assigned record covers the same family.

## value

PASS

The construction directly closes a published explicit open case and replaces it by a uniform family spanning every first-redundancy length up to 2n. The prescribed-margin cancellation is a reusable construction device, so the result is substantially more than a one-off example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
