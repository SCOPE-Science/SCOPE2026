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
# Reproduction and mathematical limits

Run `python3 checker.py` in the directory containing this report and the checker. The Python standard library suffices. Successful execution prints `VERIFY_OK`, followed by the positive quartic root, the middle-pair magnitude ratio and the sharp fourth-power constant.

The checker verifies an **exact** cleared-denominator polynomial factorization for the two-variable stationary equations, uses exact rational sign isolation for the quartic root, checks the cyclic convolution-energy formula at 48 integer vectors, compares 3,000 Gaussian-integer input vectors by independent eight-point complex Fourier quadrature and exact cyclic convolution, and tests all eight optimizing phase classes. It uses a fixed random seed. The code's floating-point checks are finite diagnostics and are not evidence of universal maximization; the proof of the claimed optimal constant, all coefficient vectors and equality classification is given in `RESULT.md`.

The mathematical conclusion has undergone only the recorded self-review, not independent audit. An exact historical priority determination is not asserted. The full text of a plausible 1988 continuous-circle comparator was not accessible; the stated finite cyclic result uses an additional alias relation absent from that continuous functional.
