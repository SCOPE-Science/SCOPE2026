---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For two positive exponential-rate mixtures on the SAME ordered support, the exact hazard-sign numerator is N(t)=sum_{i<j}(lambda_j-lambda_i)(a_j b_i-a_i b_j) exp(-(lambda_i+lambda_j)t). For m=3 its coefficients, indexed by strictly ordered exponent sums, have signs of (r2-r1,r3-r1,r3-r2), r_i=a_i/b_i, which cannot alternate twice; the elementary exponential variation-diminishing lemma gives at most one strict sign reversal. For rates 1,2,3,4 and a=(4,2,1,4)/11, b=(3,1,3,1)/8, q=exp(-t), exact symbolic expansion gives 8A-11B=(q-1)(21q^2-4q+1)<0 and hazard numerator P=11q^4+4q^3+19q^2-18q+2 with exactly two positive roots in (0,1). Independent symbolic expansion and numerical roots q=0.12945426757,0.58138312339 confirm certificates, while Descartes plus rational brackets prove exactly two crossings.

## originality

PASS

Best-of-knowledge PASS with significant residual priority risk: classical mixture-hazard/frailty theory and Boland–Proschan–Tong variation-diminishing methods explain general crossings, but their accessible material does not establish BOTH the sharp three-vs-four common-rate discrete-class minimum and a four-class exact witness with strict survival ordering. The exact rational four-class construction survives comparison without novelty claims about mixture selection theory.

## value

PASS

PASS: hazard ranks and survival order are distinct natural population quantities under finite latent-class exponential mixtures; the first possible double hazard reversal despite permanent stochastic survival ordering is a sharp, interpretable structural model-complexity threshold with an exact reproducible witness, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
