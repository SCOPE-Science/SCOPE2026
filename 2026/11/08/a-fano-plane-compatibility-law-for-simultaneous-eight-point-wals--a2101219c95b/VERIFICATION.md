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

For A={0,e1,…,e7}, W_A(v)=8−2wt(v), forcing every nonzero difference among a translated eight-frequency spectrum to have weight four. Complements of the seven differences are seven triples pairwise meeting in one point: they form the unique Fano Steiner triple system, so translated spectra are three-dimensional length-seven simplex codes. There are 7!/|GL(3,2)|=30 planes, 16 cosets each. A one-point mutation B_u satisfies W_B(v)-W_A(v)=(-1)^v7[(-1)^{u·v}−1]; simultaneous orthogonality is precisely u in the associated Hamming dual. Code weight enumerator 1+7z³+7z⁴+z⁷ and S7 incidence imply 30 for h=0,6 for h=3,4,0 for other h∈{1,2,5,6}, hence 480/96/0 common spectra at d=7. Extra coordinates independently lift eight distinct projected frequencies by 2^{8(d−7)}. An independent Python enumeration of 7-bit weight-four 3-spaces found exactly 30 and six orthogonal planes for fixed h=3,4; CHECK.py was inspected and tests all 64 mutations/480 spectra. Finite counts are exhaustive only after the proved Fano classification and lifting bijection; no claim beyond affine-independent supports and this mutation family.

## originality

PASS

No inspected accessible earlier theorem yields this quantitative simultaneous compatibility, although Fano/Hamming incidence itself is classical. Full primary comparison remains limited by unavailable manuscript text. Broader tiling theorems concern existence of separate bases; none of the accessible statements implies 0/96/480 intersection counts. The full Kadowaki manuscript was inaccessible and is retained as priority risk.

## value

PASS

The exact coexistence or incompatibility of two individually Walsh-spectral binary eight-point supports is a structural question distinct from ordinary Fuglede tiling existence. It gives a sharp perturbation boundary, complete natural small-size classification and explicit counts with a canonical Fano/Hamming-code explanation; a future Fourier-tiling investigation could need these precise admissible intersections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
