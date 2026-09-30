# Independent Audit — Exact 2-adic valuations for the tenth power of the Thue–Morse generating function

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/exact-tenth-power-thue-morse-valuations--2cde9accbbd3`
Audited tree: `49d70d3852213b4aaadecb27b628abad92a11869`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The proof is internally coherent and the finite identities used in the induction are exact. The mod-8 sections give the normalized parity pattern for residues 0 through 6; the 9-dimensional dyadic recurrence V_{2n}=A V_n, after diagonal normalization, propagates an all-rows endpoint parity matrix via the displayed Cayley–Hamilton relation whose nonleading normalized coefficients are even. Lucas then supplies the endpoint parity for odd base indices, and Legendre/Kummer converts the block formulas to v2(t_10(n))=v2(C(n+9,9))+2*1_{n=7 mod 8}. An independent implementation using the coefficient recurrence checked every n from 0 through 20000 with no exception and no zero coefficient.

## Originality

**PASS**. The closest 2026 literature found consists of Shen–Wang’s exact m=5 and m=9 formulas and Shen’s later paper whose abstract states exact binomial formulas for m=2^r and m=3*2^r (r>=2), plus a separate m=6 correction. The exponent 10 is outside those advertised families, and targeted searches through 2026-09-29 found no exact tenth-power formula matching the audited theorem. The full text of arXiv:2609.16966 could not be retrieved in this audit, so incidental unadvertised m=10 material remains a stated residual risk rather than being represented as read.

## Scientific value

**PASS**. The result gives a closed exact valuation formula immediately outside the newly solved infinite families, isolates a single exceptional residue class with a two-unit correction, and proves nonvanishing of every coefficient. The matrix normalization provides a reusable proof mechanism for exceptional exponents, giving the result clear standalone number-theoretic value.

## Literature evidence

- https://arxiv.org/abs/2606.28718 — Zhao Shen and Xinping Wang, exact 2-adic formulas for the fifth and ninth powers.
- https://arxiv.org/abs/2609.16966 — Zhao Shen, Powers of the Thue–Morse Series: 2-Adic Valuations and Automatic Odd Parts. Abstract inspected; advertised exact families are m=2^r, m=3*2^r for r>=2, and special m=6; full text was not retrievable.

## Independent checks

- Independently generated t_10(n) from the functional recurrence for all 0<=n<=20000 and verified the exact valuation formula with no zero coefficients.
- Checked the logical coverage of the mod-8 section argument and normalized dyadic-ray argument, including the r=7 split.

## Limitations

- The full text of arXiv:2609.16966 was not retrievable in this execution; the originality conclusion relies on its abstract plus targeted searches and records that residual risk explicitly.
- The audit establishes the valuation theorem only, not odd-part automaticity or a general-exponent classification.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
