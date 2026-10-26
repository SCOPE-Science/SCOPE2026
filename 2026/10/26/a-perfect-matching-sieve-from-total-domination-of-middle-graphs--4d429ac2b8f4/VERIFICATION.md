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

The proof follows by decomposing each total dominating set of a middle graph into its selected original vertices and selected edge-vertices. The latter project to an original edge cover. Selected edge-vertices without selected edge-neighbors force endpoint choices on a matching of isolated cover-edges. Alternating the original-vertex choices cancels every term except perfect matchings.

`verify.py` is a standalone Python 3 standard-library program. Run `python verify.py`. It enumerates the defining adjacency relation of each middle graph independently of the edge-cover factorization, then compares total-domination polynomials, signed edge-monomial coefficients, and perfect-matching counts. The recorded output is `verification_output.txt`.

The executed check covered 725 connected/disconnected labeled test graphs, 1,246,184 total candidate subsets of middle-graph vertices, and one isolated-original-vertex boundary. Exhaustive testing is only for the finite test suite. All larger graphs rely on the mathematical proof. No external computation, independent mathematical audit, or exhaustive priority validation is claimed.
