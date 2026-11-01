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

For ordinary 3-cut K=Delta_3(C_n²), n>=9, dual L contains all vertices/edges, exactly four cyclic families of connected triangles (4n), and precisely n consecutive-block tetrahedra; no 5-faces. Under s_a, invariant-triangle and invariant-4-face counts are (2,1) for odd n; (4,0) even n/a even; (0,2) even n/a odd. With f fixed vertices, t swaps, Lefschetz Lambda=f-[C(f,2)-t]-T-Q, the top rational H_{n-4} trace is (-1)^t(1-Lambda) by orientation-twisted Alexander duality. Thus all three claimed cases follow. Independently enumerated dual faces and signed reflection Lefschetz for every 9<=n<=18: 4n triangles, n tetrahedra, formula matches every reflection class; no five-face appears. Published shellability concentration is a separate input, not inferred from finite checking.

## originality

PASS

Bayer et al. establish ordinary cut-complex framework and dihedral characters for unpowered cycles, plus exceptional squared-cycle settings distinct from k=3,n>=9. Chauhan–Shukla–Vinayak and the 2026 cycle-powers paper prove nonequivariant shells. Previously published SCOPE cyclic character for powered cycles explicitly restricts to rotations. Reflection-axis classes at even n are independent of the cyclic module and require distinct fixed-dual-face counts. Best-of-knowledge new.

## value

PASS

The complete rational reflection traces close a natural dihedral representation problem for all n>=9, showing the two even-n mirror classes differ, a finer invariant than rank, shellability or cyclic characters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
