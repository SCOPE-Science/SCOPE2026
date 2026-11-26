---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The inverse suffix transform is x_i=s_i+t_i−t_(i+1), x_n=t_n. In the t-cube this removes exactly the redundant side of each coordinate bound and leaves a single comparison across each edge. Ball containment is therefore equivalent to shifting the suffix halfspaces by r√(n−i+1) and the retained comparisons by r, since those are the normal lengths in x, not in t. Summing along any directed path i→j gives the obstruction r(a_i+a_j+d)≤1. A one-edge extension of a path strictly increases this denominator because adjacent weights differ by less than 1; the first-edge denominator even exceeds every zero-edge denominator. Conversely, the maximum of a_j+d over all downstream paths from i gives a potential L_i with L_i≥L_j+1 on edges and a_i≤L_i≤H−a_i. The center t_i=L_i/H thus attains the bound; the exact shifted halfspaces describe all centers, and telescoping equality forces all contacts on maximizing paths. The upper denominator n+√n is attained only by a full directed path; alternating words attain the smallest denominator. Reversal followed by complement in t preserves the reversed edge word and has an integer affine unimodular inverse. For S={1} the length-(n−2) run dominates the first edge for n≥4, with a tie at n=4; for S′={n−1} the longer run dominates strictly. Their denominators differ by √2−1+√n−√(n−1)>0. The n=1 segment and n=2 single edge agree with their separate stated cases. The supplied LP checker was inspected, not run; the analytic argument establishes the universal statement.

## originality

PASS

The complete weighted-run formula, forced incenter contacts, and reversal-pair metric distinction survive comparison with earlier path-potential methods and the source definition. The constant-word simplex subcase is covered, as is the general difference-constraint idea; neither is credited as new. A distinct same-family record proves a surface-area separation, not this inradius separation.

## value

PASS

This is an exact original-coordinate invariant for a natural infinite family, not just a difference-constraint algorithm. It replaces Euclidean LPs by a linear scan, pinpoints necessary contacts, and proves both order-n⁻¹ and order-n⁻¹ᐟ² extremal scales in the same family. The explicit reversal family shows what the usual lattice invariants fail to detect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
