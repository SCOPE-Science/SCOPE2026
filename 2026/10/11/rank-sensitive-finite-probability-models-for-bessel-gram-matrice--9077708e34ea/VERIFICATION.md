---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS. A finite bound-one Bessel family has PSD contraction Gram G. The finite Grothendieck/Bessel convex representation gives G=sum p_s z_s z_s* with z_s in the coordinate unit disks (real [-1,1] analog). For any v in kerG, positivity forces z_s*v=0 at every positive-weight term, so all generating vectors lie in RanG. The rank-one image of RanG intersect unit polydisk is compact and connected; it sits inside the real Hermitian operator space on this r-dimensional span (dimension r²), or symmetric real space (dimension r(r+1)/2). Fenchel–Hanner–Rådström's connected-set strengthening of Carathéodory gives at most d atoms, yielding the precise bounds. The rank-zero case is realized by one all-zero atom. This is a universal exact deductive proof, not inferred from finite sampling, and no sharpness/minimality of atom number is claimed.

## originality

PASS

PASS best of knowledge. Liehr–Taylor–Yu establish bounded finite Gram representations but do not give a rank-sensitive number of support points in the inspected finite proof. Hanner–Rådström is a generic connected-set convex hull theorem but does not identify the PSD kernel-forced range restriction for Bessel Gram contractions. The combination supplies a natural intrinsic rank parameter; no previously stated r²/r(r+1)/2 bound was found by targeted searched aliases.

## value

PASS

PASS with modest scope. When N is arbitrarily large but the Bessel Gram rank is small, the finite probabilistic representation can use an atom count depending only on the intrinsic span dimension. This is a natural support-complexity bound motivated by simple-function realizations, not arbitrary tiny-instance enumeration. It gives no sharp minimum-atom classification and combines classical convexity with a short but essential PSD range argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
