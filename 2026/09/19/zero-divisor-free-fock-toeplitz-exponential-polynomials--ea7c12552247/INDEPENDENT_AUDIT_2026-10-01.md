---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

On the natural dense invariant exponential-polynomial domain of Fock space, nonzero finite-frequency pluriharmonic exponential-polynomial Toeplitz operators have no zero divisors: every finite product of nonzero such operators is nonzero, and a holomorphic polynomial detects the product.

## Correctness — PASS

For holomorphic polynomial-exponential pieces, Toeplitz quantization is multiplication; for antiholomorphic conjugates it becomes a polynomial in derivatives followed by translation. Normal ordering embeds finite sums into a twisted crossed product of the Weyl algebra by the finitely generated torsion-free frequency group. Ordering that group and using that the Weyl algebra is a domain makes the crossed product a domain. Exponential-vector evaluation separates distinct translation/multiplication frequencies, so the representation is faithful. Gaussian averaging gives symbol injectivity, and Taylor expansion in the exponential-vector parameter supplies a polynomial witness.

**Checked sources.** assigned RESULT.md at tree e01159ee98332a6e93523a6d11e3752e07b1d956; Qin, arXiv:2609.20555, full primary text; Cichon 2002/2003 exponential-polynomial Toeplitz calculus

**Residual risks.** Domain invariance is essential; the theorem is not a bounded-operator statement on all of Fock space.

## Originality — PASS

Qin's full primary paper explicitly ends with the one-sided zero-product question for pluriharmonic symbols whose entire parts are of exponential type. The closest older result cited there proves only a two-sided implication in one complex dimension. Cichon's exponential-polynomial adjoint calculus supplies operator formulas but no zero-divisor-free crossed-product theorem. Targeted searches found no earlier finite-frequency, all-dimensional, one-sided finite-product result.

### Equivalent formulations

The finite-frequency class is a strict natural subclass of the open class, and the audited theorem answers that subclass positively.

### Broader coverage

These results provide ingredients or different hypotheses but do not imply the one-sided finite-frequency crossed-product domain theorem.

### Exact database or table

No database/table computation is relevant; coverage is theorem-level.

### Claim versus prior implication

The source question motivates the gap, while the faithful normal-form theorem is the substantive new step.

**Checked sources.** https://arxiv.org/abs/2609.20555; https://doi.org/10.4064/sm150-2-6; https://doi.org/10.1016/j.jfa.2015.03.003; https://doi.org/10.1090/S0002-9939-2014-12110-1

**Residual risks.** Older differential-difference algebra literature could contain an abstract domain result close enough to shorten the proof, but no source tying it to this Toeplitz class was located.

## Value — PASS

The theorem isolates a natural positive island inside an explicit current open zero-product problem and identifies the structural reason: finite frequency forces a faithful domain-like crossed-product algebra. It also shows that any counterexample to the broader question must leave this finite-frequency regime.

**Residual risks.** The class is narrower than general exponential type and gives no quantitative witness degree.

## Limitations

- Only finite sums of polynomial amplitudes times linear exponentials are treated.
- The theorem does not settle arbitrary exponential-type pluriharmonic symbols or boundedness of all generators on the full Fock space.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
