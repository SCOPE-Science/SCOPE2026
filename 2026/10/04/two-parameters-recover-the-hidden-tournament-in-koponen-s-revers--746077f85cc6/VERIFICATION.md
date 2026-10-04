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

The bundled checker verifies the finite combinatorial core in two independent ways.

For each \(0\le m\le3\) and \(1\le n\le5\), it explicitly generates all assignments of the \(n\) variables to named parameters and anonymous values, canonicalizes the anonymous labels by first occurrence, and counts equality patterns with exactly \(k\) new classes. These direct counts are compared with
\[
B_{m,n,k}=\frac1{k!}\sum_{i=0}^k(-1)^i\binom{k}{i}(m+k-i)^n.
\]

Independently, for each \(m\le3\) and \(k\le5\), it enumerates all orientation bit vectors of length
\[
d_{m,k}=mk+\binom{k}{2}
\]
and takes the literal quotient by bitwise complement when the global reversal remains available. The resulting orbit counts are compared with the closed formula for \(w_{m,k}\). Multiplying the two independently generated factors gives the complete type counts. Finally, the script checks that the empty-parameter counts are the Stirling transform of the injective tournament-modulo-converse orbit profile.

Replay command:

`python3 artifacts/verify.py`

Observed output:

```text
canonical_equality_patterns_checked 3612
type_counts_m0_to_m3_n1_to_n5 {0: [1, 2, 8, 64, 948], 1: [2, 8, 64, 948, 26536], 2: [6, 56, 884, 25588, 1450252], 3: [11, 193, 5955, 349769, 41038683]}
injective_empty_parameter_profile_n1_to_n7 [1, 1, 4, 32, 512, 16384, 1048576]
stabilizer_reversal_survives_exactly_m_le_1 True
VERIFY_OK
```

The program does not attempt to prove the infinite-structure statements computationally. The automorphism/anti-automorphism characterization and the two-parameter definability threshold are proved in `RESULT.md` from Koponen's tuple equivalence and omega-categoricity.
