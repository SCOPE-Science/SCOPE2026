---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a pure qubit state, maximal ED means every one-qubit marginal is I/2. In the two-qubit family (I tensor R_y(theta))|Phi+>, local marginals remain maximally mixed, while J_z^2=(I+Z tensor Z)/2 and the rotated Bell correlation is cos(theta), giving F_Q=2(1+cos(theta)) and hence every value in [0,4]. For even N, a tensor product of singlets has all one-body marginals I/2 and is annihilated by J_z, so F_Q=0; GHZ_N has the same one-body marginals and J_z eigenvalues plus/minus N/2, so F_Q=N^2. These calculations establish the continuous and all-even-N claims analytically; the inspected verifier is only a finite consistency check.

## originality

PASS

Best-of-knowledge originality passes narrowly. The current primary source equates Entanglement Distance with a trace/sum of local-direction QFI and makes a broad metrological-resource interpretation. General metrology literature already warns that entanglement alone does not fix performance for a chosen generator. Targeted and Resultary searches did not locate the exact statement that one fixed maximal Entanglement Distance supports the complete two-qubit fixed-J_z QFI interval, together with the all-even-N zero and N-squared endpoints. Because the closest full manuscript was inaccessible, that source remains an explicit residual risk rather than being declared noncovering.

## value

PASS

The theorem isolates a precise boundary of a new ED-to-metrology interpretation: even at the maximal scalar ED value, a prescribed physically standard collective generator can have no sensitivity or Heisenberg-endpoint sensitivity. The exact interval/endpoints are a motivated counterexample clarifying what the trace identity does and does not certify, rather than a claim that the general entanglement-metrology caveat is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
