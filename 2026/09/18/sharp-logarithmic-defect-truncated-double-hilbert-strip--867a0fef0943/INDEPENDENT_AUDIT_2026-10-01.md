# Independent audit — 2026-10-01

## Final claim

For the bounded diagonal strip, the normalized double-Hilbert defect has the displayed all-orders convergent expansion and in particular is asymptotic to \((2/\pi)\sqrt{\varepsilon\log(1/\varepsilon)}\); positive coordinate dilations reduce the stated sloped strips to the same dimensionless formula.

## Correctness — PASS

The Fourier normalization, bad-quadrant multiplier and reduction to the scalar integral were reconstructed. Abel differentiation gives the stated formula for the second derivative, the Frullani step integrates to the displayed convergent series, and independent numerical quadrature of the original integral agreed with the series at representative values. The dilation reduction uses only positive coordinate dilations, so its stated domain is correct.

## Originality — PASS

Best-of-knowledge originality passes for the full exact expansion. A related published record on the same date independently contains the leading \((2/\pi)\sqrt{\varepsilon\log(1/\varepsilon)}\) asymptotic but not the complete convergent series and coefficients claimed here; later records broaden the asymptotic after this date.

### Equivalent formulations

Searches: Resultary: sharp logarithmic defect truncated double Hilbert strip epsilon log epsilon approximate eigenvector; arXiv:2609.15155

Evidence: The closest same-date published record gives the leading sharp asymptotic and a different ellipse theorem, but its inspected full text does not give this record's all-orders convergent strip expansion. Later 2026-09-19 and 2026-09-20 Resultary records contain broader strip laws but postdate the assigned 2026-09-18 finding.

Reasoning: The leading asymptotic is equivalent across the two same-date records, but the exact convergent expansion is a strictly stronger numerical statement.

### Broader coverage

Searches: Exact elliptic quasi-eigenvectors and sharp strip leakage for the double Hilbert transform; later half-Sobolev and general-cutoff strip records

Evidence: The same-date ellipse record proves only the leading strip law; later records generalize the asymptotic to broader cutoff classes.

Reasoning: The broader later results do not establish pre-existing coverage of the assigned all-orders expansion.

### Exact database or table

Searches: Resultary exact-topic search; targeted exact-series searches around arXiv:2609.15155

Evidence: No earlier exact database or table with the coefficients of the displayed convergent series was located.

Reasoning: Search absence is used only as supporting best-of-knowledge evidence.

### Claim versus prior implication

Searches: arXiv:2609.15155 source theorem versus exact series; same-date ellipse record full RESULT

Evidence: Accessible primary metadata describes the approximate-eigenvector construction; the inspected related full record attributes only an upper bound to the source and derives the matching leading asymptotic separately.

Reasoning: No checked stronger prior theorem mechanically implies every coefficient of the convergent expansion.

### Source inspections

- **Invariant sets of the double Hilbert transform** (https://arxiv.org/abs/2609.15155): Highly relevant; inaccessible full text remains a residual risk but no accessible evidence showed the exact series. Material read: Abstract and bibliographic metadata; full text retrieval failed in both open-access and authorized-access attempts. Method: Primary-source abstract inspection plus access attempts. Evidence: The public abstract concerns invariant/approximate-invariant sets; the independently inspected related record attributes only the upper strip estimate to this source.
- **Exact elliptic quasi-eigenvectors and sharp strip leakage for the double Hilbert transform** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-log-free-elliptic-double-hilbert-quasi-eigenvectors--d45af12fa2b8): Covers the leading asymptotic but not the assigned convergent series. Material read: Complete RESULT and metadata. Method: Full public record inspection. Evidence: Its strip theorem is \(R^2=(4/\pi^2)\varepsilon\log(1/\varepsilon)+O(\varepsilon)\), without the all-orders series.

Checked sources: Abakumov, Domelevo, Petermichl and Poltoratski, Invariant sets of the double Hilbert transform, arXiv:2609.15155v1; Published record: Exact elliptic quasi-eigenvectors and sharp strip leakage for the double Hilbert transform; Resultary semantic searches for truncated-strip defect asymptotics and logarithmic leakage

Residual risks: The source preprint is very recent and its full text could not be recovered in this run after open-access and authorized-access attempts; only its abstract/metadata and independently published related records were available. Contemporaneous unindexed calculations could contain the same full convergent series.

## Scientific value — PASS

The source construction explicitly raises the continuous-versus-dyadic logarithmic contrast. Determining the exact continuous defect and all correction coefficients resolves whether the logarithm is intrinsic to that natural truncation and supplies a reusable benchmark.

## Limitations

- Specific truncated-strip family and positive-dilation images only; no global optimality among approximate invariant sets. The source preprint is very recent, so contemporaneous unindexed overlap remains possible.

## Conclusion

The final claim passes correctness, originality and scientific-value review.
