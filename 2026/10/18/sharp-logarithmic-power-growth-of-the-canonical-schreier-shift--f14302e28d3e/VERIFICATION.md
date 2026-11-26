---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Pull an admissible output set back, after discarding zero coordinates. If the resulting nonempty set has minimum m and size s, then s≤m+n. Greedy blocks of capacities m, 2m, 4m, … are admissible because the rank of the first entry in a full-capacity block forces its index to be at least the block capacity. Their total capacity after l blocks is m(2^l−1), giving the ceiling upper bound. For the lower bound use p-th powers 1/(j+1) for 1≤j≤n+1: each admissible sum is at most the integral from m to 2m of dt/t, and all n+1 entries can be used together after translation. This works for n=0 and all real or complex 1≤p<∞. Density then extends the one-step operator and its powers. An eventually admissible shifted finite support yields the eventual ℓp norm; if a closed set of uniformly bounded orbits had interior, taking differences on a ball would bound all operator norms, contrary to the lower bound. This is a proof-level check; the frozen finite diagnostic was inspected, not executed or relied on.

## originality

PASS

The supported distinction is the two-sided bounds with sharp leading coefficient for powers of the additive right translation. Prior work already gives boundedness and even a logarithmic lower bound of smaller coefficient. Neither a generic doubling of ranks nor Banach–Steinhaus is claimed new; the orbit contrast is a consequence of the power law.

## value

PASS

The canonical shift is a natural basis operator in a nonsymmetric space. An optimal logarithmic scale and coefficient materially resolve the gap between the direct prior estimates. The contrast between eventual constancy on finite supports and generic unbounded orbits is an interpretable consequence, not the main contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
