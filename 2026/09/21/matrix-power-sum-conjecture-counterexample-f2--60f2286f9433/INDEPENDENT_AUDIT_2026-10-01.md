---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For the two-letter word sums over \(M_2(\mathbf F_2)^2\), \(T_{5,18}=I_2\); total degree \(23\) is the first positive-bidegree failure for two letters, with exactly twelve nonzero degree-23 multidegrees and the displayed factorized polynomial identity.

## Correctness — PASS

The coefficient of \(t^a\) in \(\sum_{A,B}(tA+B)^{23}\) is exactly the claimed noncommutative word sum because \(t\) is central. The inspected verifier computes all 256 ordered pairs by the defining shuffle recurrence and independently by polynomial-matrix exponentiation over \(\mathbf F_2\). A fresh independent replay of the shuffle recurrence found no positive-bidegree failure below total degree 23 and found exactly the twelve claimed degree-23 bidegrees, each equal to the bit pattern for \(I_2\), including \(T_{5,18}=I_2\). The primary paper's Conjecture 3 explicitly predicts zero for every such multidegree when \(p=d=2\) and the number of generators exceeds one.

**Checked sources.** assigned RESULT.md and artifacts/verify.py at tree 6615aceed31bbe3a417fbdae51ec83e23e31fa0a; Fortuny--Grau--Oller-Marcén--Rúa 2017 full text around Conjecture 3; fresh exact recurrence replay

**Residual risks.** The exhaustive certificate proves only the stated finite first-failure range and degree-23 identity.

## Originality — PASS

The primary source states the conjecture being contradicted, and targeted searches plus the published-result corpus did not locate a prior correction, counterexample, or equivalent degree-23 identity. The exact finite witness is therefore original to the best of knowledge.

### Equivalent formulations

The coefficient-extraction polynomial identity and the multidegree word-sum formulation are equivalent by centrality of \(t\).

### Broader coverage

No stronger published coverage was found.

### Exact database or table

The finite certificate is not a recomputation of a published table; it supplies the counterexample itself.

### Claim versus prior implication

The final claim directly falsifies the published conjecture rather than merely changing notation or specializing a known counterexample.

**Checked sources.** https://doi.org/10.1142/S0218196717500278; https://arxiv.org/abs/1505.08132; Resultary semantic search

**Residual risks.** A differently phrased or poorly indexed correction remains possible, but no concrete plausible antecedent was found.

## Value — PASS

A dimension- and alphabet-minimal explicit counterexample to a published conjecture is a motivated mathematical finding; the first-failure degree and exact factorized identity make the obstruction reproducible and informative rather than a bare negative check.

**Checked sources.** Fortuny et al. Conjecture 3 and its use in the conditional route to Proposition 13; exact certificate

**Residual risks.** The result does not settle the paper's final Conjecture 1.

## Limitations

- This refutes Conjecture 3 of the cited 2017 paper, not Conjecture 1 or Conjecture 2.
- The first-failure minimality is only for two letters.
- The minimality and polynomial identity are established by exact finite enumeration, not an infinite classification.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
