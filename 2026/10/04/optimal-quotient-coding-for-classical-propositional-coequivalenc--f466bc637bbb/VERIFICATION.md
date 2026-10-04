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

The proof has two exact ingredients.

First, any separating family of \(m\) formulas defines a map from valuations to
\[
\{0,1\}^m.
\]
Its kernel is the coequivalence relation. Therefore a quotient with \(k\) classes requires
\[
k\le2^m.
\]

Second, if
\[
m=\lceil\log_2k\rceil,
\]
choose distinct \(m\)-bit labels for the quotient classes. For each coordinate, the union of all classes carrying bit \(1\) is a subset of the finite Boolean valuation cube and is therefore definable by a classical propositional formula. Agreement on all coordinates is exactly quotient equivalence.

The bundled `verify.py` enumerates every set partition for \(n=1,2,3\), builds the optimal binary code, checks its kernel, and independently verifies the Bell/Stirling rank counts. It prints `VERIFY_OK`.

## Limits

The finite checker is corroborative only. The proof is valid for every finite \(n\). The result minimizes the number of formulas, not their syntactic length.
