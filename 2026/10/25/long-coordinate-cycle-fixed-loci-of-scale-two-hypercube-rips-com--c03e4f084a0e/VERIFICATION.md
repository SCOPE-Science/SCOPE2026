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

For k≥4, m≥0, the action rotates one block of k binary coordinates in VR_{≤2}(Q_{k+m}). A geometric fixed point has constant barycentric coefficient on each cyclic orbit, and its orbit must itself span a simplex. For a length-k block word of weight w, sum of rotational Hamming distances is 2w(k-w); each shift distance≤2 forces w∈{0,1,k-1,k} when k≥4. The only admissible orbit types are A_z (all zero), B_z (all one), U_z (single one orbit), V_z (single zero orbit), each indexed by z∈Q_m. Maximum cross-orbit Hamming distances show only A-A,B-B at residual distance≤2 and A-U,B-V at residual distance≤1; no interlayer edges or U-U/V-V edges. The finite orbit complex is two Y_m=VR_{≤2}(Q_m) bases, each with one cone vertex on simplex B_1(z) per z. Mapping U_z→A_z and V_z→B_z is a simplicial retraction contiguous to the identity, giving a strong deformation retract. Components are contractible for m≤2 or wedges of c_m three-spheres for m≥3 by the established Adamaszek–Adams Y_m theorem.

## originality

PASS

Best-of-knowledge PASS for the explicit geometric fixed-locus two-component strong deformation retract for arbitrary long coordinate cycle. The prior scale-two Y_m homotopy theorem supplies only each component; the recent hyperoctahedral rational representation classification of the ambient homology does not determine geometric fixed spaces. An unindexed orbit-face fixed-point theorem may exist, but the exact four-type and k≥4 classification was not located.

## value

PASS

An explicit strong deformation retract computes ALL geometric fixed points for every single long coordinate cycle and every number of passive coordinates, a natural equivariant homotopy refinement of hypercube Rips topology. The sharp k=4 orbit-type threshold yields two components and integral topology not recoverable from ordinary homology ranks or group characters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
