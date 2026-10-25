---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For mixed cyclic words, zero-/one-run counts r and singleton counts s0,s1 yield p=2(r-s0)+s1, q=2(r-s1)+s0, and pure counts a,d=sum(max(run_length-2,0)), forcing the congruence and boundary inequalities. Conversely A=(2p+q)/3, B=(p+2q)/3 and r=ceil(max(A,B)/2) give singleton counts 2r-A and 2r-B in [0,r] and enough length≥2 runs whenever a,d>0; cyclic interleaving attains every admissible quadruple, including n=1,2 separately. Class enumeration by p≡q modulo 3 and K_p(z) gives the rational generating function, and partial fractions yield the period-three formula and density 1/3. Independently enumerated every cyclic binary word at n=1..12 and every admissible 4-tuple of the same mass; their full sets and counts 2,3,4,5,8,12,16,23,32,42,56,73 agree. Infinite n is established by the run construction and exact GF, not this bounded check.

## originality

PASS

PASS on a best-of-knowledge basis: prior composition reconstruction studies use full linear prefix/suffix or all-substring composition multisets, whereas the claim enumerates the image of fixed-length-three CYCLIC unordered-composition measurements. The circular string result uses ORDERED factor frequencies, shorter or absent-word criteria and a unique-decoding question. None of the material read implies the exact congruence/boundary characterization or number of distinct histogram outputs. Abstract-level inspections limit confidence about uninspected theorems; exact alias searches found no direct coverage, which is not a novelty certificate.

## value

PASS

The fixed circular trimer composition measurement is a natural observation channel. Determining its entire image, sharp modulo-three obstruction and fraction of feasible histograms is an exact informative combinatorial invariant; the size also determines optimal noiseless distinguishable-input cardinality. Its significance does not rest solely on reproducible counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
