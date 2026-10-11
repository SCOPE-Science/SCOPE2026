---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For odd abelian A, every element at in the nontrivial coset is an involution, so its cyclic subgroup is a distinct order-two leaf adjacent only to the trivial subgroup; every other cyclic subgroup lies in A. Hence the cyclic-subgroup Hasse graph is exactly C(A)^* with |A| leaves attached and ε(Dih(A))=ε(A)+|A|. Tărnăuceanu's nilpotent theorem gives ε(A)≥ε(C_m), equality only for cyclic A. For odd m, the coprime product formula gives ε(C_{2m})=2ε(C_m)+τ(m). Writing f(m)=τ(m)+ε(C_m), one has f(p^a)=2a+1≤p^a for odd prime powers, equality only at 3, and for coprime u,v>1, f(uv)=f(u)f(v)-ε(C_u)ε(C_v)<f(u)f(v). Thus f(m)≤m with equality exactly m=3, proving the comparison and equality case. I also independently checked f(m)≤m through odd m<1000, with equality only at 3; this finite check is corroborative, not the universal proof.

## originality

PASS

The primary 2023 theorem covers nilpotent groups and all odd-order groups and explicitly leaves arbitrary even order as a conjecture. The current cyclic-subgroup-graph paper gives the ordinary dihedral formula ε(D_{2m})=ε(C_m)+m, but its inspected family list and table do not cover generalized dihedral groups with noncyclic odd abelian kernel. Resultary searches found the audited theorem, a later generalized-dicyclic companion, and unrelated generalized-dihedral graph invariants, but no earlier statement implying the generalized-dihedral edge formula plus sharp cyclic comparison. The theorem is therefore original to the best of the inspected evidence.

## value

PASS

This proves a published even-order extremal conjecture on a natural infinite nonnilpotent family and identifies the exact equality case. The structural leaf decomposition is reusable and includes all odd abelian kernels, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
