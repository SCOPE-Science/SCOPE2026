---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The symbolic classification is checked in two ways.

The construction code enumerates every birth-time vector
\[
\tau_j\in\{j+1,\ldots,n-1\},
\qquad
1\le j\le n-2,
\]
builds the row closure maps from their fixed points, and checks all five preconditional axioms together with conditional identity, semicomplementation, and double-negation inflation.

Independently, for chain sizes through \(6\), the verifier brute-forces all entries not already forced by conditional identity, semicomplementation, the top row, and the P2 lower bound. It then filters those candidates using the full axiom list.

The two generated sets agree exactly. The surviving counts are
\[
1,1,2,6,24
\]
for sizes
\[
2,3,4,5,6,
\]
and the birth-time construction gives
\[
(n-2)!
\]
through every larger checked size.

The script also verifies that all surviving operations induce the same negation and that exactly one at each size is the Heyting implication.

It prints `VERIFY_OK`.

## Limits

The computation is corroborative. The arbitrary-\(n\) result follows from the nested fixed-point proof, not from extrapolating the finite counts. Bare \(\mathsf K\)-preconditionals are outside the claim.
