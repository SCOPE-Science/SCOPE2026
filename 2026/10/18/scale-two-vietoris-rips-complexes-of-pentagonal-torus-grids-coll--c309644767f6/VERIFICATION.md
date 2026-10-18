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

Execute `python3 artifacts/verify.py` with Python 3 and no third-party dependencies. It enumerates every radius-two simplex using the shortest-path metric, and independently generates the \(n+5n+5n\) proposed facet families for each integer \(7\le n\le14\). It checks equality of all face sets, the original face vector, each of the \(40n\) claimed elementary free-face incidences against current cofaces, the exact surviving complex, and its face vector. For \(7\le n\le10\), it computes mod-two boundary ranks and Betti vectors \((1,1,n,0,0)\). Expected final output contains `VERIFY_OK`.

The explicit uniform proof in `RESULT.md` supplies the necessary argument for every integer \(n\ge7\), independent of the finite experiment. The checker is a finite cross-check and cannot establish unbounded correctness or integral homology by itself. The integral homotopy and homology statements come from the proved collapses and the subsequent CW argument. Independent external assessment has not been performed.
