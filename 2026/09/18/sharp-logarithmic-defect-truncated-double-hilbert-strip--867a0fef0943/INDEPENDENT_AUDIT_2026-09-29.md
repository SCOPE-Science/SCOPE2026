# Independent Audit — 2026/09/18/sharp-logarithmic-defect-truncated-double-hilbert-strip--867a0fef0943

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `60136836fb8d57bffc77fd8d965e14d823ebdb99`
- Disposition: **PASSED**

## Correctness

**PASS** — The Fourier constants and series are correct. With the stated unitary normalization, the strip indicator transforms to (2/pi) sin(epsilon xi1)/xi1 times sin(xi1+xi2)/(xi1+xi2). The double Hilbert multiplier equals -1 on same-sign quadrants and +1 on opposite-sign quadrants, so Plancherel gives R^2=8 J/(pi^2 epsilon). Reversing the tail integral yields J''=(1/epsilon) integral (1-cos x) sin(epsilon x)/x^2 dx. Abel-regularized differentiation and the cosine Frullani identity give A'=0.5 log((1-epsilon^2)/epsilon^2), hence the displayed closed form for J''. Twice integrating with J(0)=J'(0)=0 produces the convergent series, including -epsilon^3/(9 pi^2) in R^2. Independent numerical quadrature at epsilon=0.1 and 0.03 agreed with the series to about 1e-7 using a direct oscillatory tail calculation. Positive coordinate dilation correctly reduces the general positive-slope strip to the dimensionless aspect ratio.

## Originality

**PASS** — The September 2026 source introduces this truncated-strip approximate eigenvector, proves an upper bound of order sqrt(epsilon |log epsilon|), and contrasts it with an exact dyadic defect. Targeted searches using the source title/id, strip defect, approximate eigenvector, epsilon log epsilon and double Hilbert transform did not locate the matching lower asymptotic, constant 2/pi, or convergent expansion. The claim is therefore a sharp evaluation of a newly introduced example, not a new fact about Hilbert transforms in general.

## Scientific value

**PASS** — The result settles whether the logarithm in the source's continuous-strip upper estimate is genuine and quantifies the continuous-versus-dyadic separation. The exact leading constant and lower-order expansion are useful for the source's quantitative-stability viewpoint even though the theorem concerns one specific family.

## Sources

- Invariant sets of the double Hilbert transform (Evgeny Abakumov; Komla Domelevo; Stefanie Petermichl; Alexei Poltoratski): https://arxiv.org/abs/2609.15155 — Primary source introducing the finite-measure truncated-strip approximate eigenvector and the continuous/dyadic comparison.

## Limitations

- The result evaluates one truncated-strip family and is not an optimization over all approximate eigenvectors.
- The affine extension covers positive-slope strips obtainable by positive coordinate dilations, not arbitrary curves.
- The source is very recent, so unindexed contemporaneous observations remain a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "numeric_quadrature_epsilons": [
    0.1,
    0.03
  ],
  "series_agreement_absolute": [
    1.13e-07,
    9.72e-08
  ]
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first.
