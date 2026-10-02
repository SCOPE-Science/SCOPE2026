# Independent mathematical audit — SCOPE-20260920-39839f2d9a7f

Audited at: 2026-10-01T18:05:11.787582Z

Disposition: **passed**

## Correctness — PASS

For \(m=3\), the four-decimation identities close the odd-part sequence on itself, its shift, and fixed automatic reductions of the 2-regular coefficient sequence. For \(m=5,9\), the exact valuation formulas remove precisely the powers of two from the published block recurrences, giving fixed integer recurrences in \(r=\nu_2(n+1)\). Modulo any fixed \(2^s\), companion-matrix powers are eventually periodic, while the finitely many initial slices are automatic reductions of 2-regular sequences; the odd-part substitution and valuation-depth control preserve a finite 2-kernel. The finite verifier confirms the identities and normalized recurrences on a large range, but is corroborative rather than exhaustive.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_recurrences.py
- Shen arXiv:2609.16966
- Shen-Wang arXiv:2606.28718

### Correctness risks

- The proof relies on the cited exact valuation formulas and block recurrences from Shen-Wang; those source statements were verified at primary abstract/theorem level but their full text could not be retrieved in this run.

## Originality — PASS

Shen's September paper proves automatic odd parts for powers \(2^r\), for \(3\cdot2^r\) with \(r\ge2\), and for \(m=6\); its primary statement does not include \(m=3,5,9\). Shen-Wang's June paper proves exact valuations for the fifth and ninth powers but does not claim odd-part automaticity in its primary statement. Resultary found no earlier SCOPE result containing these three cases.

### Equivalent formulations

No equivalent prior automaticity theorem for these three exponents was located.

### Broader coverage

They supply essential ingredients but not the finite-state lifting conclusion for \(m=3,5,9\).

### Exact database or table

The claim is structural, not a table lookup.

### Claim versus prior implication

The final claim requires a new combination of valuation-normalized recurrences and automatic-sequence closure.

### Sources inspected

- Powers of the Thue-Morse Series: 2-Adic Valuations and Automatic Odd Parts — https://arxiv.org/abs/2609.16966. NOT_COVERING_IN_MATERIAL_READ: The stated proved families are \(2^r\), \(3\cdot2^r\) for \(r\ge2\), and \(m=6\), leaving 3,5,9 outside the listed theorem.
- 2-adic Valuations of Coefficients of the Fifth and Ninth Powers of the Thue-Morse Generating Function — https://arxiv.org/abs/2606.28718. INGREDIENT_NOT_COVERING: The primary statement proves valuations and nonvanishing, not odd-part automaticity.

### Checked sources

- https://arxiv.org/abs/2609.16966
- https://arxiv.org/abs/2606.28718
- https://arxiv.org/abs/1703.01955
- Resultary semantic search

### Residual risks

- Xinping Wang's May 2026 thesis was not inspected in full and remains a plausible source-access risk.
- The conjecture paper is very recent, so concurrent unindexed work remains possible.

## Value — PASS

The theorem settles three genuinely missing cases of a newly stated automaticity conjecture, including cases with unbounded valuation depth, and isolates a reusable recurrence-to-automaticity mechanism. It is a motivated structural advance rather than a finite numerical check.

### Value sources

- Shen arXiv:2609.16966
- Shen-Wang arXiv:2606.28718

### Value risks

- The general conjecture remains open, including \(m=7\) among exponents at most 9.

## Limitations

- Only \(m=3,5,9\) are proved; the all-exponent conjecture is not settled.
- No minimal automata or state-complexity bounds are given.
- Full text of the recent Shen conjecture paper was not independently retrieved during this audit.
