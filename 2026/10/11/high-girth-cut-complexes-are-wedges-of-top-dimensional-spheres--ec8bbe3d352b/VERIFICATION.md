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

# Reproducibility and scope
Run `python3 verify.py` from the directory containing the standalone script; only Python's standard library is required. The script reconstructs graph neighborhoods, checks the shortest cycle by breadth-first search, enumerates every connected induced \(k\)-subset, and confirms its private deletion face occurs in exactly one connected \(k\)-subset. It also verifies the absence of \((k+1)\)-element faces in the Alexander dual, computes mod-two boundary ranks for its full chain complex, checks the predicted reduced Betti numbers, and independently counts connected four-sets from degrees. It examines 23 graph-parameter pairs, including hexagonal chains with 10 and 14 vertices, a nine-vertex theta graph with shared-cycle edges, and the Heawood and Petersen graphs. Expected terminal message: `VERIFY_OK 23 complete finite graph/parameter checks`.

The proof's critical integral step is not a modular inference: for every connected \(k\)-simplex, a *distinct private* \((k-2)\)-face contributes exactly one unit entry to its integral boundary column. Those rows form an identity matrix up to sign, proving split injectivity and a torsion-free cokernel over \(\mathbb Z\). The finite tests independently check the combinatorial condition in examples, while the written short-cycle argument establishes it for all parameters. Standard Alexander duality, Hurewicz, and Whitehead handle the infinite family. This verifier does not test shellability, graphs below the girth threshold, or low-dimensional boundary cases excluded from the theorem.
