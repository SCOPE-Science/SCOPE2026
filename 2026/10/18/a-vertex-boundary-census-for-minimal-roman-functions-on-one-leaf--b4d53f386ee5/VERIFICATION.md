---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

A Roman dominating assignment is coordinatewise minimal iff every 1 has no adjacent 2 and each 2 has a private neighboring 0 for which it is the unique 2-neighbor. On H◦K1 the only possible core/leaf configurations are A=(2,0), B=(1,1), C=(0,1), D=(0,2); fix S of A cores, then C exactly on its external boundary ∂S and B or D independently on U=V\(S∪∂S). This establishes full weight enumerator M_H(z)=∑_S 2^|U| z^(2n-|∂S|). Marked cyclic gaps give H(t,z)=1+zt+z²t²/(1-2z²t); labeled cycles contribute n/k times gap coefficients, yielding the displayed cubic rational generating function and Pell–Lucas total. Maximizing ∂ size by ∑min(ell,2) gives floor(2n/3), hence min weight ceil(4n/3), and counting residue-class gap profiles gives min multiplicities 3, n(n+17)/6, or n according as n mod3 is 0,1,2. I independently brute checked all labelings of sunlets n=3,4 against subset boundary counts.

## originality

PASS

Best-of-knowledge original combined claim, not merely its known premises: Existing minimal-RDF decision tests and generic enumeration algorithms do not mechanically state the full weight polynomial for arbitrary one-leaf coronas. A symbolic specialization could produce it, so priority risk about an earlier corona formula remains; exact sunlet coefficients and minimum counts go beyond merely computing single Roman domination numbers. Broader works and residual risks below qualify priority.

## value

PASS

The full weight-by-weight census for minimal (not merely minimum) Roman domination on the natural one-leaf corona operation is intrinsically useful, and its sunlet specialization supplies a complete rational generating function and precise periodic optimal multiplicities. These refine known scalar domination numbers and provide direct enumerative benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
