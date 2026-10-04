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

The verifier `verify.py` performs two independent finite replays.

First, it enumerates all simple \(2\)-uniform hypergraphs through four vertices and all simple \(3\)-uniform hypergraphs through five vertices. For each hypergraph and each \(n\in\{2,3,4\}\), it constructs the incidence structure having \(n-1\) private lines for every hyperedge, confirms direct \(K_{m,n}\)-freeness, reconstructs the saturation hypergraph, and checks every subset \(S\) of points by direct incidence counting after adjoining a new line through \(S\). The accepted subsets agree exactly with the independent sets.

Second, for every graph through five vertices and every \(m\in\{2,3,4,5\}\), it constructs the common-core \(m\)-uniform hardness gadget and checks
\[
i(H_m(G))=(2^{m-2}-1)2^{|V(G)|}+i(G).
\]

Replay command:

`python verify.py`

Expected terminal line:

`VERIFY_OK`

The replay covers 3348 extension instances and 4400 hardness-gadget instances. It is a finite consistency check only; the general theorem is established by the proof in `RESULT.md`.
