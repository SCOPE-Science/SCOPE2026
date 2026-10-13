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

# Reproduction and limits

Execute `python3 verify.py` with SymPy, NumPy and SciPy. The code constructs the unweighted path adjacency matrix, verifies the polynomial formula for its evolution, builds the nine-vertex Cartesian probability matrix and evaluates all 81 entries under a generic reflection-symmetric degree-four moment law. Exact symbolic checks establish the two-variable objective and its cubic derivative. Exact rational signs bracket the unique root; an independent nine-by-nine matrix exponential checks the two-time witness and objective to within \(10^{-12}\).

The proof's unrestricted statements use convexity, Jensen's inequality \(\mathbb E[x^4]\ge(\mathbb E[x^2])^2\), exact moment expansion, monotonicity, and strict convexity of the squared matrix norm. The code does not exhaust all probability laws and is not an independent external audit. The theorem does not assert exact uniform mixing, only the best positive deficit.
