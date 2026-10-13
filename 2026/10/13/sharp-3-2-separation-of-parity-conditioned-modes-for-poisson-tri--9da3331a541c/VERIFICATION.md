---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification and reproducibility

The analytical verification consists of five explicit steps in RESULT.md: Hurwitz stability and strict even/odd root interlacing, positive-residue decomposition into Bernoulli deletions, a convolution-based modal-envelope lemma, a compact-limit passage covering endpoint probability vectors, and the exact two-trial equality witness. In particular, the boundary argument passes a mixture representation to the limit rather than assuming argmax sets depend continuously on parameters.

Execute `python3 verify_modal_gap.py` with Python 3. The checker performs exact-integer polynomial convolutions over every probability triple of the form \((L,T,W)=(\ell,t,w)/4\) where the numerators are nonnegative integers summing to four, for each number of trials from one through four. It discards only cases with a zero probability for one of the conditioning events. For every other case it verifies the full modal sets, that each odd modal index is between one less than the smallest even modal index and the largest even modal index, the universal \(\frac32\) distance, and the \(\frac12\) unique-even-mode assertion. It also verifies the exact extremizer polynomial.

Observed results: admissible cases \(9,189,3159,49329\) for trial counts one through four, totaling \(52686\); largest observed distances \(\frac12,\frac32,\frac32,\frac32\), respectively. The explicit sharpness polynomial, before division by sixteen, has coefficients \((0,2,6,2,6)\) in successive powers of the doubled-score variable.

**Boundaries of verification:** The checker is not a proof of arbitrary real parameter choices or arbitrarily many trials. The infinite family is handled by the written analytical argument using established polynomial results. No independent external mathematical audit has been performed.
