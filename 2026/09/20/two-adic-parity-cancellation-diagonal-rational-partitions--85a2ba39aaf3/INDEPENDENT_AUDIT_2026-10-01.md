---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For the diagonal-rational-partition residue numerator, \(A_N(-1)\) is exactly \((B_N/O)c_0(N)\), where \(c_0(N)\) is the constant coefficient of the displayed power-of-two negacyclic product; this proves the simple cancellation at \(N=8\), the resulting pole order and parity term, and the exact cancellation census through \(N=100\).

## Correctness — PASS

Character orthogonality at \(-1\) leaves exactly characters with \(O\mid 2j+1\). Writing these as the odd Galois conjugates of a primitive \(2D\)-th root converts every even-denominator factor into the displayed finite geometric polynomial. Because \(D\) is a power of two, the cyclotomic trace kills all reduced monomials except the constant term and has trace \(D\) on one, yielding \(A_N(-1)=(B_N/O)c_0(N)\). The actual verification code was inspected, and an independent exact replay reproduced \(P_8=1024x^6\) in \(\mathbb Z[x]/(x^8+1)\) and exactly the cancellation set \(\{4,8,11,12,14,17,27,28,31,61,62,64\}\) for \(3\le N\le100\). The source paper's full text independently confirms its published small table through \(N=7\), including cancellation only at \(N=4\).

**Checked sources.** assigned RESULT.md at frozen tree cb9da58ff3241870765f75fa333da518845d0756; artifacts/verify_parity_cancellation.py blob 066c824b5ce583e9a2d9938a5b0fc6ba997939b4; Raghava, arXiv:2609.18945v1, full primary PDF pages 1--12; Beck--Robins Ehrhart background

**Residual risks.** The finite census is certificate-based and proves only the checked range; it is not evidence for infinitely many cancellations.

## Originality — PASS

The full motivating preprint gives the Ehrhart numerator, root-of-unity pole framework, and a numerical table only for \(3\le N\le7\); it does not state the negacyclic trace criterion, the \(N=8\) cancellation, or the larger census in the inspected text. The source itself says a numerical supplement contains a certificate for its displayed small-\(N\) computations, which remains a residual ancillary-source risk rather than evidence of coverage.

### Equivalent formulations

The audited formulation is a cyclotomic trace compression of the source's character sum, not merely a restatement of its pole criterion.

### Broader coverage

Those frameworks do not by the inspected material produce the specialized power-of-two constant-coefficient criterion.

### Exact database or table

The published table stops before \(N=8\); the audited census is not a recomputation of a published table.

### Claim versus prior implication

That additional two-adic reduction is not mechanically stated by the inspected source; it is the substantive surviving claim.

**Checked sources.** https://arxiv.org/abs/2609.18945; https://doi.org/10.1007/978-1-4939-2969-6; Resultary semantic search

**Residual risks.** The motivating preprint's ancillary source archive was not separately inspected; it could contain unpublished broader evaluations. Concurrent work on this September 2026 preprint may be unindexed.

## Value — PASS

The trace criterion compresses a large character calculation to exact arithmetic in a power-of-two cyclotomic quotient and directly decides survival of the uniquely maximal raw parity pole. The new \(N=8\) cancellation and exact census are mathematically motivated consequences of that structural criterion rather than an arbitrary finite enumeration.

**Checked sources.** Raghava fixed-alphabet pole theorem and small table; Ehrhart period-collapse background; actual exact verifier

**Residual risks.** The census by itself would not establish value; the general trace reduction does.

## Limitations

- The theorem treats only cancellation at the primitive second root.
- The exact pole order is worked out for \(N=8\), not for every cancellation index.
- The finite census stops at \(N=100\) and is not an infinite classification.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
