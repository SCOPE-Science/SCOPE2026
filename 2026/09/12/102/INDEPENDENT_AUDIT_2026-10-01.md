---
audit_date_utc: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For sigma: 1->2, 2->3, 3->133 and sigma': 1->2, 2->3, 3->313, the balanced-block algorithm closes on exactly nine minimal blocks of maximum word length 7; the induced block substitution is primitive and has the stated exact diagonal coincidence densities.

## Correctness — PASS

The closure was independently reconstructed from the three diagonal seeds using prefix Abelianization. Exactly the nine displayed minimal blocks were obtained, with maximum length 7. Rebuilding the block-incidence matrix from the images reproduced the archived matrix N, and \(N^8\) has strictly positive entries. An independent Perron calculation gives dominant root 2.2055694304 and reproduces the displayed letter-level coincidence density 0.3500509598 and block-level density 0.5920145975; the exact Q(beta) formulas in the package evaluate to those values.

**Evidence inspected:** artifacts/verify_blocks.py; artifacts/blocks.json; artifacts/exact_freq.py; https://publi.math.unideb.hu/paper/1681/download/

**Residual risk:** No pure-point-diffraction or regular-model-set corollary is inferred; those would require additional hypotheses.

## Originality — PASS

Sellami's primary paper supplies the balanced-pair framework and worked examples, but full-text search and inspection did not contain the target words 133/313 or this nine-block output. Its listed examples are different substitutions. The later cubic family uses characteristic polynomial \(x^3-a x^2-b x-1\) with \(a\ge b\ge1\), whereas this pair has \(x^3-2x^2-1\) (\(b=0\)), so that advertised family does not cover it. No exact prior block list or frequency table was located.

**Equivalent formulations:** Checked balanced pair/block terminology, common dynamics, intersection substitution, coincidence frequency, and same-incidence-matrix formulations.

**Broader coverage:** The general balanced-pair algorithm is prior, but it does not mechanically state the termination size, concrete blocks, primitive matrix, or exact frequencies for this excluded \(b=0\) pair.

**Exact database or table:** No published block table for this substitution pair was found.

**Claim versus prior implication:** Applying a known algorithm still requires the finite closure computation; the prior examples and cubic-family formula do not imply this specific output.

**Primary/technical sources inspected:** https://doi.org/10.5486/PMD.2012.5007; https://doi.org/10.3906/mat-1407-3

**Residual risk:** Equivalent data could appear in a specialized substitution database not indexed by the searches.

## Value — PASS

A complete terminating balanced-block decision with exact coincidence densities for a natural same-matrix cubic Pisot pair is a meaningful finite structural classification. It gives reusable common-dynamics data while explicitly stopping short of unsupported spectral corollaries.

**Context inspected:** Sellami's balanced-pair common-dynamics program.

**Residual risk:** The contribution is classificatory and pair-specific.

## Disposition

PASS. The final claim clears correctness, originality, and value as stated. No change to `RESULT.md` or `SLOGAN.txt` is required.
