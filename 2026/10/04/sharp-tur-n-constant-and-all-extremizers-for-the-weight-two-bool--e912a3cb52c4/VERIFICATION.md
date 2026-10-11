---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Walsh nonnegativity is \(Q(s)=1+\sum_{i<j}a_{ij}s_is_j\ge0\). Averaging over balanced signs for even \(d\), or the sign-sum-one slice for odd \(d\), gives the sharp objective bounds, and the radial choices attain them. Equality forces \(Q\) to vanish on the relevant slice. In odd dimension, sign swaps plus spanning of the slice force all edge coefficients equal. In even dimension, balanced-slice row differences force the additive form \(a_{ij}=u_i+u_j\); then \(Q(s)=(\sum s_i)(\sum u_is_i)\), and positivity is exactly the stated subset family. A fresh exact replay verified the radial inequalities and odd equality-slice full rank through dimension eight; the frozen verifier extends exact checks through dimension ten and gives explicit nonradial even examples.

## originality

PASS

Kolountzakis–Révész formulate Turán's positive-definite extremal problem on arbitrary locally compact abelian groups and emphasize finite groups, with general packing and spectral-set upper bounds. The inspected full primary paper does not state the Boolean weight-two shell problem or its equality cases. Nearby halved-cube literature studies equitable colorings rather than this translation-invariant positive-definite optimization. Resultary returned the audited record itself as the exact hit and no earlier covering finding.

## value

PASS

The weight-two shell is a canonical Boolean Hamming/halved-cube set. Determining not only the optimal Turán constant but every equality case reveals a sharp parity transition from odd-dimensional rigidity to an explicit continuum of even-dimensional nonradial extremizers, a natural structural result within finite harmonic analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
