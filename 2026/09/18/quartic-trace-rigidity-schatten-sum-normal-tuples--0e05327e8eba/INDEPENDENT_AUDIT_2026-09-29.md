# Independent audit — A quartic trace identity rigidifies Schatten sum-normal tuples

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/quartic-trace-rigidity-schatten-sum-normal-tuples--0e05327e8eba`
**Audited tree:** `815db875b946682d9479ce9d09dfbc1e53b85bb4`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The trace identity is correct. For T_j in S_4, quadratic products lie in S_2 and quartic products are trace class, so the expansion is legitimate. Expanding sum_{j,k} Tr(C_{jk}^*C_{jk}) and using cyclicity plus pairwise commutativity of the T_j and of their adjoints gives exactly Tr(D^2)=||D||_2^2. Nonnegativity then forces every mixed commutator to vanish when D=0. For S_2 sum-hyponormal tuples, D is positive trace class with trace zero, hence D=0. The finite-tracial-von-Neumann version uses the same algebra and faithfulness of the trace.

### Independent checks

- Re-expanded all four quartic trace sums and matched them term-by-term with Tr((sum_j(T_j^*T_j-T_jT_j^*))^2).
- Checked Schatten ideal bookkeeping S_4*S_4 subset S_2 and S_2*S_2 subset S_1, so every trace used is legitimate.
- Verified the S_2 sum-hyponormal corollary: positivity plus trace zero forces D=0 before applying the quartic identity.
- Tested the identity independently on finite-dimensional commuting nonnormal polynomial-matrix examples; the two sides agreed to numerical roundoff.
- Checked that the finite von Neumann algebra conclusion uses only tracial cyclicity and faithfulness and does not require an unstated compactness hypothesis.

## Originality

**PASS.** PASS to the best of current searchable knowledge. Chavan--Reza--Sequeira's September 2026 preprint introduces the surrounding sum-normal/sum-hyponormal problem and establishes several special cases, while Misra--Pramanick--Sinha study mixed-commutator matrices and trace inequalities. Targeted semantic and repository searches did not locate the exact Hilbert--Schmidt energy identity, its S_4 rigidity consequence, or the finite-tracial formulation before this record.

### Literature and chronology checked

- https://arxiv.org/abs/2609.19287 — Sameer Chavan, Md. Ramiz Reza, Shanola S. Sequeira, Sum of self-commutators of commuting operators (September 2026); nearest recent source defining the problem.
- https://arxiv.org/abs/2012.11115 — Gadadhar Misra, Paramita Pramanick, Kalyan B. Sinha, A trace inequality for commuting tuple of operators; nearby mixed-commutator trace literature.

## Scientific value

**PASS.** The exact sum-of-squares law converts possible cancellation among self-commutators into a no-cancellation identity on a natural Schatten ideal. It yields an affirmative and quantitatively stable S_4 case of the new sum-normal problem, an S_2 sum-hyponormal normality theorem, and a clean finite-tracial analogue.

## Limitations

- Originality is to the best of current searchable knowledge; older multivariable commutator literature is broad and was not exhaustively theorem-by-theorem searched.
- The exponent 4 is a sufficient trace-summability threshold, not claimed sharp, and arbitrary compact sum-normal tuples remain outside the theorem.
- Pairwise commutativity is essential.

## Publication guard

The current source tree on `main` matched the assignment tree `815db875b946682d9479ce9d09dfbc1e53b85bb4` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
