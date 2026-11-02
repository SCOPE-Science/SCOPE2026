---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For connected unweighted finite simple G on N>=3, P_h=2(I+hL_G/2)^(-1)-I, and the inverse of the irreducible M-matrix has positive off-diagonals. Since L_KN-L_G is a positive semidefinite complement Laplacian, inverse Loewner order gives C_G,ii >=(1+t)/(1+Nt), t=h/2. The equality criterion for a positive-semidefinite inverse difference reduces to (L_KN-L_G)e_i=0, equivalent to i being universal. It follows that h<=2/(N-2) is nonnegative on every graph, with exactly universal vertices having vanishing holding entries at the boundary. The block Schur complement at a universal vertex gives (P_h)_vv=(2-(N-2)h)/(2+Nh), negative immediately beyond the boundary. The connected two-vertex exception remains positive for all finite h. Independently enumerated all 770 connected labeled simple graphs on N=3..5, confirming exact equality support on all of them (283 graphs with at least one universal vertex); finite checks corroborate, do not establish the universal proof.

## originality

PASS

The exact general resolvent-return positivity criterion, spectral crossing formula for reversible Markov chains, and complete-graph threshold are acknowledged earlier results. The new statement is the sharp extremal bound over all unweighted N-vertex graphs together with the precise equality class of universal vertices, which needs the nontrivial inverse Loewner comparison and strict equality criterion not supplied in the earlier chain paper. Search did not reveal an implication-equivalent graph-order extremal theorem. Best-of-knowledge with priority risk.

## value

PASS

Uniform positivity timesteps are natural stability limits for diffusion on graphs. This settles the exact worst-case threshold over all connected simple graphs of each order and uniquely characterizes extremal graph structure and zero-return sites, rather than restating the prior fixed-chain resolvent test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
