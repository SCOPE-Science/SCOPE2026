---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reviewed RESULT.md commutator calculation for the radical basis a,b,c,d_i,ab,bc,d_ic,abc (dim 2m+6). Commutator coefficients are αβ′−α′β, βγ′−β′γ, δ_iγ′−δ_i′γ, and αB′−α′B+Aγ′−A′γ. The resulting (m+3)×(m+4) matrix has the nine exhaustive case ranks 0,1,2,3,m+2,m+3; the q^(m+1) free central coefficients explain T_r. Centralizer sizes q^(2m+6−r) imply each class size q^r, and direct summation yields k(G)=q^m(2q^(m+2)+2q^3−q^m−q^2−2q+1). Independent fresh finite enumeration over q=2,m=1,2,3 and q=3,m=1 rederived all 4 rank distributions without importing the package verifier: q2 m1 ranks 0:4,1:20,2:56,3:112,4:64; q2 m3 ranks 0:16,1:272,2:800,3:960,5:1024,6:1024; q3 m1 ranks 0:9,1:126,2:756,3:2754,4:2916. For m≥3, the omission 4,...,m+1 follows directly from complete case ranks. Finite tests do not establish prime-power universality; symbolic matrix argument does.

## originality

PASS

No inspected prior statement implies the full q,m class-size distribution for a length-three path algebra with both a 1→2→3→4 line and m parallel 1→3 shortcut arrows. Earlier three-step multiarrow-line result computes ordered commuting pairs for a different quiver and does not supply each adjoint rank. Hennecart–Perry broader quiver methods remain a genuine unverified priority risk because the complete primary full text was inaccessible.

## value

PASS

Natural algebra-group question: a full elementwise centralizer-rank spectrum, exact conjugacy-class number and arbitrarily long missing interval for a small path-algebra family. The shortcut arrows alter commutator structure relative to both pure lines and radical-square-zero algebras; the family and gap are motivated by Higman-type class enumeration, not arbitrary low-dimensional tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
