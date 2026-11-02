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

# Verification record

The supplied `verify.py` is a standalone Python standard-library script. Its finite quotient enumerates every ordered triple of nonempty subsets of four colors, namely all \(3375\) states, tracks each initially present color separately, and confirms the identity \(F^7=F^3\) for all representatives. The proof in `RESULT.md` explains why this finite check covers graphs with arbitrary positive shore sizes. The program checks the 20 cardinality coefficient entries (four fixed plus sixteen primitive-four-cycle), independently counts support cycles, and directly simulates original labelled graph dynamics on nine triples, totalling \(173376\) distinct configurations. It verifies all stated formulas on those test graphs and checks the exact four-cycle/orbit normalization.

The recorded output ends with `CCA4_TRIPARTITE_VERIFY_OK`. `support_classes.tsv` provides the complete finite representative-class record. All source files are supplied as plain text; no external packages are required.

The microscopic examples alone are finite cross-checks, not a substitute for the exact finite-support reduction. The computer-assisted classification may be independently reviewed or proved by a hand-derived smaller case analysis. Novelty and mathematical value were assessed from the cited sources and explicit scientific comparisons; their independent external review remains unperformed.
