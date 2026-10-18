---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Over F9=F3[u]/(u²+1), a symmetric 2×2 matrix [[a,b],[b,c]] satisfies A⁻¹=-A iff A²=-I, giving a²+b²=c²+b²=-1 and b(a+c)=0. b=0 yields exactly four diagonal choices a,c=±u. b!=0 gives c=-a and six (a,b): (0,±u),(±1,±1). Thus exactly 10, not published table’s 8. Independent separate GF9 polynomial-pair implementation exhausts 729 symmetric matrices and 81 message words per code: four MDS [4,2,3], six [4,2,2]; self-duality follows GGᵀ=I+A²=0. Witness [[1,1],[1,-1]] has 1+32z³+48z⁴. This classification is finite and genuinely exhaustive.

## originality

PASS

Primary publisher’s public Table1 explicitly says q=9 n=2 has 8 SIS matrices with [4,2,2] AMDS. Neither its abstract nor the observable tables give the corrected 10 or four [4,2,3] constructions. Resultary query returned exact assigned finding and nearby coding results, not a correction. Full article body could not be verified: public HTML asks for login, arXiv/OA searches did not locate an open full preprint, and authorized Oxford lookup reported no_pdf. The inaccessible source is a qualified priority/comparison risk, not alone an originality failure. General 2×2 matrix counting methods could imply ten, but no checked published SIS instance identified this combined table and MDS correction.

## value

PASS

The finite correction overturns a published computational count and its coding conclusion for a natural first extension field: four source-family generators produce self-dual MDS [4,2,3] codes where the table reports only distance-two constructions. It is not merely a recount of a known table because it changes the attainable code parameters and supplies an explicit code plus complete dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
