---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each N>=4 and 1<=k<=N-1, with nonzero uniform hopping J and a single loss site, no-jump contraction projects asymptotically to the maximal H-invariant ker(n0). In the hard-core sector the off-site transfer is the Boolean down-map D_k. The entrywise Boolean-lattice commutator gives its full rank min(C(N-1,k),C(N-1,k-1)); A=U D-kI makes ker(D) invariant, so d_dark=max(C(N-1,k)-C(N-1,k-1),0). In the fermionic exterior-power model H=J(N n_u-k), low-energy intersection with wedge^k|0>^perp has dimension C(N-2,k), while the high-energy block has no such vector. Therefore the first-jump probabilities are min(2k/N,1) and 1-(N-k)(N-k-1)/(N(N-1)), respectively. The k=1 and k=N-1 boundaries follow; positivity of their difference only for 2<=k<=N-2. Independent exact/numeric Hamiltonian spectral intersection tests covered 36 cases; finite tests are not the proof.

## originality

PASS

Exact multi-particle, all-filling dark-rank comparison on the complete physical-site graph survives best-of-knowledge originality inspection; Boolean lattice and exterior powers are classical and not claimed new.

## value

PASS

The hard-core versus fermion distinction yields a sharp filling threshold and an O(1) gap in capture despite same one-particle hopping: for even N half-filled fermions retain (N-2)/(4(N-1)) dark mass. This is a substantive transport/statistics boundary, not merely an algebraic reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
