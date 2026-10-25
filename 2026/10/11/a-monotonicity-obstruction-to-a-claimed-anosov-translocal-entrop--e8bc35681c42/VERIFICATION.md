---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed the exact source definition of upper/lower translocal entropy, with initial sets closed B(z,exp(-omega*n)), epsilon-separated n-orbit segments and omega>=0. For omega2>omega1 these sets nest for each n; S(n,epsilon,.) is monotone under inclusion, and n^-1 log, limsup/liminf and epsilon->0 preserve the inequality. Thus both entropy versions are nonincreasing in omega. For fixed positive rates chi_i, the printed alternative R(omega)=h_top(f)-sum_i max(chi_i-omega,0) is nondecreasing, with strict increase whenever an active chi_i>omega. A=[[2,1],[1,1]] is unimodular, affine, hyperbolic and bounded-distortion; its roots are (3+-sqrt(5))/2 and h_top=chi=log((3+sqrt(5))/2)>0. Independent standard Bowen-separation argument gives h_omega=(chi-omega)_+: an initial ball radius exp(-omega*n) needs exp((chi-omega)_+*n+O(1)) unstable Bowen strips of width comparable to epsilon exp(-chi*n), while the stable direction contributes no exponential factor; the source Theorem 2.2 confirms the same. The printed upper-entropy formula evaluated with logarithmic expansion rate chi is R(omega)=min(omega,chi), giving R(0)=0!=chi and R(chi)=chi!=0. The affine example belongs to the broader named class; this refutes the extension as printed. Note that printed formula is for upper entropy; affine upper equals lower. No finite experiment supports the universal set-inclusion step.

## originality

PASS

The assessed contribution is an explicit exact contradiction/counterexample to a claimed general bounded-distortion Anosov extension, NOT the already published cat-map entropy value or shrinking-ball monotonicity separately. Directly inspected publisher, author-hosted and arXiv-v3 mathematical statements retain the conflict. Fresh literature searches and Resultary comparisons found no independent published correction/equivalent theorem; the exact matching Resultary hit is the same research record and is not counted as independent priority evidence. The contradiction is an elementary deduction from two printed statements, so originality is appropriately limited to recognizing and documenting the error. Best-of-knowledge, with stated priority and historical-version risks.

## value

PASS

This is a motivated and consequential counterexample to a published extension of a recently defined entropy invariant: the formula asserted for a broad hyperbolic class violates the definition’s forced monotonicity and reverses the exact cat-map endpoints. Even though the algebra is short and source-internal, pinpointing a false non-affine/Anosov claim with an exact elementary witness prevents use of a mathematically invalid generalization; that is substantive error-correction value, not a parameter-renaming exercise. The contribution is appropriately narrow and does not pretend to be a general theorem, an improved entropy bound, or a new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
