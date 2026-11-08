---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For n,q≥2, S_n-word orbits are exactly the weak-composition histograms (T=binom(n+q−1,q−1)). A point of the geometric fixed set has constant barycentric coefficients on each word orbit; this identifies its exact PL orbit-simplex triangulation, not invariants of ambient homology. Every nonconstant histogram orbit contains two words at Hamming distance two (swap unlike coordinates); distinct constant orbits give distance n≥2, while each constant orbit has only one word. Therefore an orbit support is a face exactly when it omits any nonconstant orbit or at least two constant orbits. Its complex is (∂Δ_U*Δ_C)∪(Δ_U*sk_{q−3}Δ_C), with Alexander dual the q isolated constants. Suspension/join plus integral equivariant simplicial Alexander duality gives wedge^(q−1) S^(T−3) and sign of all T histogram vertices tensored with the coaugmentation quotient lattice Z^[q]/Z(1,...,1); using the quotient rather than augmentation kernel matters integrally. A symbol transposition fixes f histograms and swaps (T−f)/2 others, proving the parity twist. The boundary case q=n=2 has S0 and is handled by the model. Independently checked exhaustive omitted nonedge pairs versus orbit-face criterion for (n,q)=(2,2),(3,2),(2,3),(3,3),(2,4), and directly checked transposition histogram parity. These finite instances corroborate; the proof of all n,q rests on the structural duality and orbit argument, not extrapolation.

## originality

PASS

Best-of-knowledge statement-versus-prior comparison found no work proving the complete final claim; specifically distinguishes stronger source statements, aliases, exact tables and non-implications. No failed search is regarded as proof of priority.

## value

PASS

This is a genuine two-parameter infinite family of geometric fixed-point spaces under full coordinate permutations, giving their exact homotopy type and a nontrivial residual integral alphabet-symmetry lattice. Ambient rank and rational character results do not determine the topology of a geometric fixed locus or its integral coaugmentation action, so the structural equivariant refinement has mathematical use beyond parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
