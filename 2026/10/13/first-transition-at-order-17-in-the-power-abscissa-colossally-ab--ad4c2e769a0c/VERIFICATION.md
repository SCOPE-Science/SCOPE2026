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
# Verification

Execute `python3 artifacts/verify.py`. The source and actual replay output are packaged in `artifacts/verify.py` and `artifacts/replay.txt`.

The verifier constructs the prime-increment ordering with directed 110-digit decimal intervals and confirms all 56 critical increments exceed the threshold for prime \(167\), with pairwise separation. All 42 classical CA candidates below \(10^{65}\) beyond the reference \(55440\) are evaluated by exact rational divisor-sums and outward-rounded logarithm/exponential intervals. The strict winner at order \(17\) is classical CA index \(15\), \(6983776800\). The best-versus-second margin is certified above \(1.6\%\). The code also verifies the order-\(16\) reference winner and the known finite order-\(32\) index \(27\).

For the infinite tail, the code checks that the primorial through \(167\) exceeds \(10^{65}\), the last enumerated subthreshold event is index \(51\), and the first later event exceeds the cutoff. Using Robin's unconditional inequality, the analytic proof bounds all larger reference secants by the strictly decreasing function
\[
B(u)=\frac{(1.8u+0.6483/u)^{17}}{\exp(u^2)-\exp(u(55440)^2)},\qquad u\ge5.
\]
The certified numerical endpoint satisfies \(B(5)<300000\), while the chosen winner exceeds \(173600000\). The packaged code checks this precise endpoint inequality.

No claims beyond the first transition are proved; the uninspected ancillary computations from the preprint are identified as an originality-access limitation.
