# Independent audit — Rank-three mechanism obstruction and a correction to Bao's Example 6.3

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/rank-three-mechanism-obstruction-j0-elliptic-surfaces--5cc1d9554668`
**Audited tree:** `ea3e762c5d88f084b34504023a06a56c3258fdf4`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The obstruction follows directly from Bao's simultaneous rank criteria: in nondegenerate E2 rank-one case (c)(i), exactly one of sqrt(A),sqrt(C) lies in Q(omega), while positive E1 and E3 rank require sqrt(A) and sqrt(C), respectively, so total rank is at most two. For Bao's printed Example 6.3 family, m=3/(32n^3-1) is never a rational square by the stated mod-8 argument, hence sqrt(C) is not in Q(omega). The cube identities give E2 rank one, the E1 conditions hold, and E3 fails precisely at the omitted square-root condition. Thus the component ranks are (1,1,0) and the total rank is exactly two. Exact symbolic substitution verifies both displayed sections.

### Independent checks

- Read Bao v1 Section 6: Example 6.3 explicitly claims rank three with (1,1,1), states sqrt(C) not in Q(omega), and then concludes E3 rank one from the cube condition alone.
- Checked Bao Theorem 1.3(d), which separately requires sqrt(C) in Q(omega) for the third summand to have rank one.
- Reproved the general c(i) obstruction: exactly one of sqrt(A),sqrt(C) in Q(omega) forces at least one outer summand rank to vanish.
- Reproduced the mod-8 nonsquare proof for m=3/(32n^3-1) for every integer n>=1.
- Recomputed B^2-4AC=(1-m)^3 and the E2/E1 cube identities exactly.
- Substituted both displayed sections into E0 and verified the identities symbolically.
- Checked Bao v1 arXiv version history: the accessible source is v1 submitted 2026-09-14, so no source revision predating this record was located.

## Originality

**PASS.** PASS to the best of current searchable knowledge. Bao v1 itself explicitly claims Example 6.3 has total rank three with component ranks (1,1,1), while in the very next calculation it states sqrt(C) is not in Q(omega). Bao's Theorem 1.3(d) requires sqrt(C) in Q(omega) for E3 rank one, so the example's inference is internally inconsistent. Targeted searches for the arXiv identifier, Example 6.3, the 32n^3-1 family, and a rank-two correction found no earlier correction or equivalent repository record.

### Literature and chronology checked

- https://arxiv.org/abs/2609.16349v1 — Bao v1. Proposition 6.1 bounds rank by 3; Example 6.3 explicitly makes the erroneous (1,1,1) claim while also stating sqrt(C) is not in Q(omega).
- https://doi.org/10.1007/BF02567626 — A. Bremner, Some simple elliptic surfaces of genus zero (1991), cited by Bao for low-degree criteria; Bao also reproduces the needed criterion in Proposition 3.6.
- https://github.com/SCOPE-Science/SCOPE2026/commit/a2f1b4942cfcf4bf63e2dc08f4066977f8dd21f7 — Commit adding this correction at 2026-09-18T02:48:26Z.

## Scientific value

**PASS.** The result corrects a concrete infinite family in a new closed-form rank classification and, more importantly, isolates a general mechanism obstruction: Bao's E2 case (c)(i) can never participate in total rank three. It also removes the squarefreeness restriction from the corrected rank-two statement and supplies explicit independent sections.

## Limitations

- The correction assumes Bao's Theorem 1.3 as stated and does not independently reprove the full rank formula.
- The accessible Bao source is a very recent v1; a later author revision or contemporaneous unindexed correction may eventually supersede the erratum aspect.
- Bremner's original full article was not independently inspected in this run; Bao's self-contained Proposition 3.6 supplies the specific criterion needed here.

## Publication guard

The current source tree on `main` matched the assignment tree `ea3e762c5d88f084b34504023a06a56c3258fdf4` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
