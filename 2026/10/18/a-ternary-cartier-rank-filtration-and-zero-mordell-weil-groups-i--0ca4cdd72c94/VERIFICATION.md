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

The degree-2·3^s+2 polynomial t^(2·3^s+2)-t is squarefree for s>=1; genus q=3^s. Characteristic-3 Cartier coefficient extraction leaves one nonzero entry per relevant row and at most one per column. The row→column map on s ternary digits is 0w→w1 and 2w→w0; leading 1 terminates. Counting survivors gives 2^j·3^(s-j) for 0<=j<=s, 2^(2s-j) for s<=j<=2s and zero thereafter, proving nilpotence at 2s+1 and a-number 3^(s-1), p-rank 0. Independently generated all transitions for s=1..6 and all iterates; this finite check corroborates rather than proves arbitrary s. Read Katsura full primary paper, section 4 theorem 4.1 and hypotheses: f=-t+(t^(2q/3))^3 t², deg f=6(q/3+1)-4, nonzero second derivative at critical roots so Assumption (*) holds; the MW subgroup of the stable Cartier fixed space vanishes.

## originality

PASS

Katsura 2026 gives the structural MW–Cartier relation, Achter–Howe gives the general semilinear hyperelliptic matrix convention; neither evaluated this particular all-s ternary path rank filtration in inspected primary sources. The rank profile is a special computation not a formal statement already implied without its digit lemma. Older related characteristic-three computations remain a priority risk.

## value

PASS

An exact infinite-genus Cartier-iterate filtration, exact nilpotence boundary and induced vanishing of Mordell–Weil groups for a natural quasi-elliptic family supply precise invariants typically inaccessible from p-rank alone. Ternary survivor counts are nontrivial uniform combinatorics, beyond merely plugging into the Cartier formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
