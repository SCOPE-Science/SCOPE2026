---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The 28 rational bitangents have 378 line pairs, giving 6h+3e+f=378 for multiplicities four, three and two. Fullness forces all rational branch points onto bitangents; double-cover fibers give #S=2#U-N=q²+8q+1 and (q-24)²+N=6h+2e-125. From f>=0, 6h+2e<=252+2h. Kuwata Theorem 5.1 gives a distinct involution from each fourfold bitangent intersection in characteristic !=2; Dolgachev–Martin tame characteristic-37 lifting and the complex genus-three involution cap yield h<=21. Thus RHS incidence 6h+2e<=294, but at q=37 fullness requires 294+N. Hasse–Weil gives N>=ceil(38-6sqrt(37))=2, contradiction. All quantifiers explicitly split/full and q37. Independently enumerated 2,332 admissible incidence triples and maximum 294; this cannot verify geometric lemmas.

## originality

PASS

PASS (best knowledge): Knecht–Reyes 2015 explicitly lists F37 as possible and supplies the necessary incidence identity, while Kuwata, Janasz–Pokora–Zieliński and Dolgachev–Martin each supply separate geometric inputs. The audited field exclusion is a specific mathematically motivated synthesis and not an invented new constituent lemma. No equivalent result located in checked material, but historical corollary priority is not guaranteed.

## value

PASS

PASS: F37 is one of the explicit unresolved finite fields in Knecht–Reyes degree-two full split classification; excluding it has a natural categorical value and sharpens the remaining odd-prime-power upper bound from 37 to 31. Not a generic novelty claim about involutions or Hasse–Weil.

The dated certificate retains the supplied scientific assessment, sources and limitations.
