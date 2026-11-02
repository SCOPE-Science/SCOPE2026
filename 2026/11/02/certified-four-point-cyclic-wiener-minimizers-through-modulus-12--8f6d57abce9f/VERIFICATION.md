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

The `CHECK.py` file is a standalone rigorous finite enumeration of the cyclic four-element Fourier \(\ell^1\) minimization problem. All statements here concern \(8\le N\le128\). The checker uses exact rational Machin-series and Taylor estimates to enclose each needed trigonometric coordinate within \(10^{-8}\), then compares all support sets by signed 64-bit integer arithmetic with exact integer-square-root inequalities.

Four successful complete runs were performed using the attached exact program and the commands `python CHECK.py 8 96 CERT_8_96.json`, `python CHECK.py 97 112 CERT_97_112.json`, `python CHECK.py 113 120 CERT_113_120.json`, and `python CHECK.py 121 128 CERT_121_128.json`. Their respective anchored set counts were 3,321,925; 2,888,860; 2,003,750; and 2,453,430. Together they cover 121 moduli, 10,667,965 anchored sets, and 10,660,484 strict noncandidate exclusions, with 7,481 predicted minimizers. The minimum fully certified real-score gap is greater than 0.10997296, at modulus 123.

The program proves the rational error budget independently of floating point. Floating-point square root initializes an integer guess only; both floor inequalities are checked exactly. Its strict criterion is a positive integer separation above \(13(N-1)\) in score units, making rounding of the displayed decimal irrelevant. The candidate families have a common true score by cyclic translation and invertible dilation.

The classification is exhaustive only over the specified finite range. The program does not prove the open unbounded-modulus case or cover arbitrary complex-weighted supports. The scientific review was self-review only; independent audit has not been performed.
