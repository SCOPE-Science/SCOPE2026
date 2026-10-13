---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The verification is exact and finite. `verify.py` uses the binary polynomial \(u^4+u+1\) to construct \(\mathbb F_{16}\), takes an element \(\zeta\) of order \(5\), and realizes the semidirect product on all \(160\) affine elements.

It checks:

- the relations \(a^5=t^2=1\) and \(tat=a^{-1}\);
- the exact order \(|\operatorname{GL}_4(2)|=20160\) by exhaustive enumeration;
- that exactly \(60\) linear maps normalize the chosen \(D_{10}\)-action;
- all \(16\) translations, giving \(960\) affine normalizers;
- every conjugation image on all \(160\) elements of \(G\);
- the resulting orbit sizes \(1,15,20,60,64\);
- the order and characteristic-layer description of each orbit.

The computation does not enumerate the full abstract automorphism group. That is unnecessary: the affine-normalizer subgroup is already transitive on each of five subsets, while \(O_2(G)\), \(G'\), and element order make those subsets invariant under every automorphism. Thus no further automorphism can merge them.
