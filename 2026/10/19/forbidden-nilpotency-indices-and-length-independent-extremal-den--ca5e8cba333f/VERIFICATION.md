---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Nilpotence is equivalent to nilpotent reduction because A² is then in πM₂(R), so A^(2m)=0. There are q² residue nilpotents (zero plus (q+1)(q−1) choices of image line and nonzero quotient-to-line map), each with q^(4m−4) lifts. The zero fiber dies by power m. In each other fiber t=tr(A) and d=det(A) belong to (π). If d∈(π²), Cayley–Hamilton gives inductively A^h∈π^(h−1)RA+π^h RI, so A^(m+1)=0. If d=πδ with δ a unit and t=πτ, put B=τA−δI; then A²=πB, B commutes with A, and B modulo π is invertible as a nonzero scalar plus a nilpotent. Thus π^(m−1)B^(m−1)A=A^(2m−1)≠0, since its factor after π^(m−1) has nonzero reduction. The determinant's first-order map at each rank-one residue matrix has a nonzero cofactor and is affine surjective; this applies without a coefficient-field splitting. The fraction (q−1)/q of each nonzero fiber therefore has index 2m, giving the stated count and density. Companion matrices with (t,d)=(π,0),(0,π) attain m+1 and 2m. For the nonchain witness, C³=−xC−xyI, C⁴=−2xyC and C⁵=0; the lower-left entries certify both characteristic cases. Separate literal matrix-power enumeration matched total/extremal counts 1024/384 in Z/8 and F₂[t]/(t³), 16384/6144 in Z/16, and 59049/34992 in Z/27. No forbidden index occurred. Finite tests corroborate but do not establish the general proof.

## originality

PASS

The distinct claim supported by the inspected literature is the joint full forbidden interval and global extremal mass for all finite commutative chain rings at every m≥3, including mixed characteristic, with an explicit nonchain failure. Known companion classification supplies the reduction; the equal-characteristic length-three regular-fiber result and the equal-characteristic arbitrary-length extremal-fiber count materially overlap and are not credited as separate novelty. The inspected higher-tail theorem does not cover the full new interval for m>3 or the mixed-characteristic scope.

## value

PASS

The result replaces a coarse universal 2m nilpotency bound by a forbidden interval whose length increases without bound, and supplies a ring-independent exact extremal share across mixed and equal characteristics. The determinant-layer criterion makes the result usable without similarity enumeration; the nonchain example isolates a real boundary rather than adding an arbitrary small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
