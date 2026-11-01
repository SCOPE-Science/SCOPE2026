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

For all N>=2, positive edge weights, and finite nonzero convex nondecreasing Phi with Phi(0)=0, convexity gives superadditivity. Decompose original coordinate differences by sorted rank gaps and count crossed cuts A_k to bound E(x)>=sum h_k Phi(g_k), while E(Sx)=sum w_k Phi(g_k). A two-valued input from each minimizing cardinality-k cut attains w_k/h_k exactly. Centered even and odd cut profiles yield max(1,t/2) and max(1,t/2,1/(2t)) respectively. Independently checked 48 weighted cut profiles, 13068 energy cases, including boundary strengths and equality witnesses. Finite checks supplement all-N proof.

## originality

PASS

Steinerberger develops discrete Pólya–Szegő edge-isoperimetric machinery, especially an L1 mechanism. Gupta establishes a restricted monotone half-line weighted power-energy inequality, and Bankevich–Nazarov concern continuous rearrangements. Inspected statements do not imply an exact sharp arbitrary-positive-weight finite-path multiplier simultaneously for every convex Phi and its centered asymmetric transition.

## value

PASS

The sharp best constant for every convex edge density under sorting is a natural general weighted-graph inequality. Exact centered-defect transitions and odd/even contrast are mathematically motivated stability boundaries, not arbitrary parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
