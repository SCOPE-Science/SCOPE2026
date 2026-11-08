---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For every integer N>=2 and one exact complex labelled DFT measurement from each additive-character order d|N, removing the order-d sample permits a binary pair x,y with signed difference h=x-y∈{-1,0,1}^N. Galois conjugacy of primitive roots makes zero at one sampled frequency equivalent to vanishing on its entire character-order shell, so h must have Fourier support in V_{N,d}. On p^a the local order-p^b shell has constant-vector minimum support p^a when b=0, or is periodic mod p^b with zero-sum p-class blocks and minimum support 2p^(a-b) when b>0. CRT identifies the order-d rational space as a tensor product. Minimum nonzero Hamming support of linear tensor-product codes is multiplicative by row/column support argument, with attaining rank-one tensors. The local signed ±1 constructions attain all products as binary differences, proving Δ(N,d)=(N/d)2^ω(d), not merely an upper bound. Each local factor >=2 and setting b_i=a_i gives min_d Δ=2^ω(N). Exact DFT complex values (not magnitudes), one erasure, and all N are explicit.

## originality

PASS

Qualified PASS for the sharp lower bound and exact all-divisor deletion-distance classification, not for the previously known minimal sampling design, Galois reduction, or sparse ambiguity witness. Pei–Chang 2022 has high-priority overlap and complete text unavailable; no decisive covered theorem identified in material actually read.

## value

PASS

For the natural minimal cyclic DFT mask this is the exact Hamming-distance robustness invariant after one lost coefficient: the fewest binary positions that can change invisibly. Arithmetic dependence on the deleted order and sharp constructive lower bound supply information unobtainable from mere uniqueness failure or an example ambiguity pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
