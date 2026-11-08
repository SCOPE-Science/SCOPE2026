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

PASS. Reconstructed B B^T=(n-2)I+J, rank n and projector Q with constant diagonal q=(n-3)/(n-1). Cauchy-Schwarz on Qe gives the sharp inner radius 1/sqrt(q). For even n, the odd row-degree cube-slice inequality forces exactly one zero per row, a perfect matching, with alternating-sign Eulerian complement attaining N-n/2. For odd n, any extreme point has unsaturated B columns independent: a free-edge forest leaf contradicts parity, while an odd unicyclic component forces every free coordinate zero. Thus extremizers are balanced trinary edge signings; parity of N forces zero triangle for n=3 mod 4 and zero-free for n=1 mod 4; Euler tours attain both. Symmetrizing any quadratic Euclidean comparison under S_n and reducing the same/shared/disjoint edge-pair invariants forces scalar Euclidean form on X_n, hence global Banach-Mazur optimality. Independent rational projector/row-balance checks n=4..8 and exhaustive {-1,0,1} feasible bounds n=4,5,6 passed; they are auxiliary, not proofs for all n.

## originality

PASS

PASS on searched and compared mathematics, with historical priority risk. The exact unsigned complete-graph cube section, all Hilbert comparisons and modulo-four contact classes are not obtained from the inspected signed-incidence cographic ellipsoid theorem, general cube bounds or different bipartite transportation spaces. Absence of indexed matches is not a proof of novelty.

## value

PASS

PASS. Canonical irreducible signless-incidence cube sections of symmetric hollow zero-row-sum matrices have a natural Hilbert distortion invariant; the exact global ellipsoid, contact classifications and sharp modulo-four parity transition across all n identify a structural geometric extremum, not a routine change of coordinates or isolated numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
