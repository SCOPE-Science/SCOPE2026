# Independent Audit — 2026/09/19/random-word-distinct-substring-first-correction--022b2626ec5b

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `ee83a786341592e9aa2d57cc2d8e8a66ba4f64e8`
- Disposition: **PASSED**

## Correctness

**PASS** — The second-order expansion checks. Gheorghiciuc-Ward provide a fixed-length expected-subword-complexity approximation uniform when the window count and word length vary together; its exponentially weighted error is summable over all k. Writing the occupancy deficit H(N,Q), the exact increment H(N+1,Q)-H(N,Q)=1-(1-Q^{-1})^N bounds replacement of N_k=n-k+1 by n at total cost O((log n)^2). Replacing the binomial survival term with exp(-n/Q) contributes only O(1) on the geometric grid Q=d^k. Thus the total deficit is n sum_{k>=1} f(d^k/n)+O((log n)^2). Reindexing around floor(log_d n) gives the stated absolutely convergent one-periodic correction. The Mellin transform was independently evaluated numerically and matches Gamma(1-s)/(s(1+s)); residue extraction at s=0 and at 2 pi i ell/log d gives exactly the submitted mean and Fourier coefficients. Independent direct series/Fourier evaluations reproduce the reported tiny binary oscillation and the d=3,4,10 amplitudes.

## Originality

**PASS** — The 2007 Gheorghiciuc-Ward theorem supplies the essential level-by-level profile, while Flaxman-Harrow-Sorkin determine the maximum and compare random words only on a coarser scale. A public 2016 heuristic already identifies the coefficient-one n log_d n deficit, so that leading term is not claimed as new. Godbole's September 2026 all-length treatment gives coarser bounds and does not state a linear-order periodic correction. Targeted searches of distinct-substring, suffix/trie-profile and digital-Mellin terminology did not locate the explicit all-length P_d phase or its Fourier series. Older trie literature remains a material residual risk, but the inspected prior statements do not cover the audited theorem.

## Scientific value

**PASS** — The theorem resolves the complete linear-order term in the expected total number of repeated substring occurrences and exposes its lattice-scale digital oscillation, including an explicit Fourier spectrum and phase average. It upgrades the known leading n log n correction to an O((log n)^2) remainder and quantifies why the binary oscillation is practically invisible despite being mathematically nonzero.

## Sources

- **On Correlation Polynomials and Subword Complexity** — Ion Gheorghiciuc; Mark D. Ward. https://doi.org/10.46298/dmtcs.3553 — Provides the uniform fixed-length expectation approximation that is summed over all substring lengths.
- **Strings with Maximally Many Distinct Subsequences and Substrings** — Abraham Flaxman; Aram W. Harrow; Gregory B. Sorkin. https://doi.org/10.37236/1761 — Prior exact extremal substring count and coarse random-word comparison.
- **The Expected Number of Distinct Substrings in an Alphabet String** — Anant P. Godbole. https://arxiv.org/abs/2609.19409 — Recent all-length expectation work; its stated results do not give the audited linear digital correction.
- **Asymptotic Analysis of the kth Subword Complexity** — N. Ahmadi; Mark D. Ward. https://doi.org/10.3390/e22020207 — Related logarithmic-length fixed-k profile asymptotics, not the all-length summation theorem.

## Limitations

- The alphabet size is fixed and the source is uniform i.i.d.; nonuniform memoryless and dependent sources are not covered.
- The O((log n)^2) remainder relies on the uniform 2007 fixed-level approximation rather than only on the elementary collision sandwich.
- The next logarithmic-order phase term, variance and concentration are not identified.
- Older trie and suffix-tree profile literature remains a residual originality risk because similar periodic Mellin phenomena can appear under different formulations.

## Independent checks

```json
{
  "gheorghiciuc_ward_uniform_profile_checked": true,
  "occupancy_reduction_checked": true,
  "mellin_transform_numeric_check": "agreement to about 1e-13 at s=0.2,0.5,0.8",
  "series_fourier_agreement_checked_for_d": [
    2,
    3,
    4,
    10
  ],
  "binary_mean": -1.1099488636120962,
  "binary_peak_to_peak": 3.44993e-07,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive source remained inaccessible, so Oxford Download was not required.
