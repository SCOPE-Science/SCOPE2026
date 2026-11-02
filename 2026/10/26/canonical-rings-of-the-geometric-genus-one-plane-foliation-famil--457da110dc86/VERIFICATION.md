---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The two explicitly specified blowup valuation chains give v_e2(X^aY^bZ^c)=a+2b on Z=1 and v_fn(X^aY^bZ^c)=b+nc on X=1, from transformations y=x^2 w and q=p^n s. Requiring both exceptional valuations >=m yields b>=c and a<=(n-1)c. The monomial initial terms are distinct, hence no cancellation; every allowed monomial factors as U^(b-c) times c among T_j with indices summing a. The sorted-index quadratic relations are the full toric ideal; lattice saturation gives normality. Summing monomials yields rational Hilbert series, checked for 328 (n,m) pairs, which does not itself verify blowup geometry. The source paper full text was inaccessible: the local reduced-model valuation identification is a remaining external geometric verification risk and has been reconstructed from the package local chart data rather than verified against the original full appendix.

## originality

PASS

Best-of-knowledge: The family and basic geometry are prior art; the grade-by-grade canonical ring is not synonymous with the single volume/geometric-genus statement. It could nevertheless be derivable from original charts, so priority is qualified. The audited claim adds all section multiplicities and equations. Its derivation from explicit prior geometry is mathematically valid if the local center data are correctly transcribed; because the complete primary example could not be reviewed, the originality PASS is expressly conditional best-of-knowledge. Priority and access limits explicitly preserved.

## value

PASS

The complete canonical ring and plurigenera, not just geometric genus or volume, are natural exact birational invariants; the graded toric presentation and n=2 weighted projective canonical model are directly reusable for this geometric family. The motivator is the first geometric-genus-one example at the sharp volume bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
