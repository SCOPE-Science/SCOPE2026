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
# Verification

The proof is symbolic.

For each finite binary string \(\sigma\), the cylinder \([\sigma]\) is compact, computably closed, and has positive Lebesgue measure. It therefore qualifies as an initial condition in the dense-set construction used in the proof of Corollary 3.19 of the source.

Running that construction below \([\sigma]\) yields a \(\Pi^0_n\)-generic point inside \([\sigma]\). Hence the generic class is dense. The weakly generic class contains it and is dense as well.

At scale \(2^{-k}\), the length-\(k\) cylinders form a cover of size \(2^k\). Because each genericity class is dense, every cylinder contains a class member. Because the metric is ultrametric, a set of diameter at most \(2^{-k}\) cannot meet two distinct length-\(k\) cylinders. Thus every such cover has at least \(2^k\) members.

Therefore the exact covering number is \(2^k\) at every dyadic scale, giving lower and upper box-counting dimensions equal to \(1\).

The source independently proves Hausdorff dimension \(0\) for the weakly \(\Pi^0_n\)-generic class; the strong generic class is a subset and therefore also has Hausdorff dimension \(0\).

## Limits

The argument concerns classical dimensions of the whole classes. It does not infer effective dimension of individual points. Full box dimension is sensitive to density and closure, so no packing- or Assouad-dimension conclusion is inferred.
