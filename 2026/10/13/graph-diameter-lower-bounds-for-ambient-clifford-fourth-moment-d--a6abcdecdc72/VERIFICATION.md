---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Support of conjugated Z_v grows by at most one graph edge per disjoint local layer and is contained in B(v,L). Pauli fourth-order projector factorizes over arbitrary bipartitions; by Clifford transitivity, of 4^n-1 nonidentity Pauli classes precisely 4^s-1 are supported on s=|B(v,L)| sites. Applying the cited invariant-projector channel inequality yields diamond lower bound 1-(4^s-1)/(4^n-1); all centers imply min volume. For epsilon<3/4 the required integer b_G(L)>n-1 gives b_G(L)=n and depth>=diam(G). Independently checked path n=5 L=3 gives exact bound 256/341>3/4. The source projector theorem remains a separately cited, not independently full-text-reconstructed, premise.

## originality

PASS

Prior West-Cerezo-Larocca Theorem 1 gives the general invariant-projector template, and its printed Clifford Corollary 3 specializes to a 1D nearest-neighbor chain. The new application requires checking arbitrary-graph Heisenberg balls, arbitrary-subset projector factorization and each-center diameter consequence. No searched published mathematical record gives this explicit graph-ball inequality, but the derivation is a close corollary of general prior machinery and full original text was inaccessible; these are material originality limitations.

## value

PASS

Architecture-sensitive sharp lightcone volume obstruction is a natural independent quantitative design bound, distinguishing paths/cycles/other topologies at fixed diamond error. Value is the general graph consequence, not a new projector theory; no tight general-graph construction is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
