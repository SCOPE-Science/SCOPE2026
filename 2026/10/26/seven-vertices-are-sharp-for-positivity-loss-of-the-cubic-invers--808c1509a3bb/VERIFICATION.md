---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. On every connected simple undirected unweighted graph G, the polynomial q_h(s)=1+hs+h^2s^2/2+h^3s^3/6 is positive on s>=0, so R=q_h(L)^{-1} is symmetric SPD with eigenvalues in (0,1], diagonal entries positive, R1=1 and Euclidean contraction. Off-diagonal positivity reduces exactly to positivity of the transposed cofactors of A(h)=6I+6hL+3h^2L^2+h^3L^3, since det A>0. I independently enumerated the entire connected graph-atlas list n=2..6 (counts 1,2,6,21,112), computed all 1,933 unordered-pair cofactor polynomials in exact SymPy integer arithmetic and certified a nonnegative nonzero coefficient vector immediately in 1,932 cases and after multiplication by (1+h)^32 in the remaining case. This exhausts graph order <=6, not a timestep sample. An independent exact 7x7 rational P7 inverse verifies endpoint (1,7) entries at h=1/2,3/4,1,2 as 1036685/130532396219, -529900671519/16012967110980391, -16229/1505893633, and 96462616/19528273141. The complete matrices at 1/2 and 2 are strictly positive, proving reentry. No weighted/directed conclusion follows.

## originality

PASS

PASS best-of-knowledge for the exact minimal seven-vertex graph cutoff and reentrant P7 step, not for Padé schemes or positivity of exponential propagators generally. Blanes–Iserles–Macnamara 2022 and Gottlieb–Shu–Tadmor 2001 give general methods and SSP obstructions, while published related [2/2] Padé results concern different rational functions and/or directed state-space models. The highly relevant Masood–Yousuf 2010 Padé article was located, but its abstract alone cannot establish noncoverage; full text inaccessible after arXiv/OA attempts and authorized Oxford route returned vpn_disconnected. Its possible priority overlap is a MATERIAL residual risk, not a failure assigned solely because literature access failed.

## value

PASS

PASS. Exact smallest counterexample size and a full safe finite-order range for a natural third-order rational heat-step operator are useful invariants; P7 loses and regains coordinate positivity despite spectral stability and mass conservation. The 1933 exact certificates are a meaningful exhaustive classification, not a mere finite numerical simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
