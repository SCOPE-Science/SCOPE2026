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
# Verification record

The mathematical reduction from the one-letter saturation criterion to border events was rederived by inspecting all position cases, including empty matches, constant tails, and the last tail position. The period-multiple lemma requires the even length \(m=2J+2\) and was proved for all \(J\ge0\); it was not assumed for odd length. The limit proof uses only elementary independent fair bits and the bound \(\Pr(F_j)=2^{-j-1}\). Explicit output is a count of distinct length-marked rules, not a Hénon geometric monodromy count.

Run `python3 verify_marker_density.py` to check the literal saturation conditions against the separate independent-cylinder formula through \(J=6\), including all even lengths up to \(14\) and odd lengths up to \(15\). Run `c++ -O3 -std=c++17 marker_density_fast.cpp -o marker_density_fast && ./marker_density_fast` to reproduce the exact integer sum through \(J=25\), ending in \(1298518439058409\). Since every summand and denominator is an integer, the reported rational and error interval do not rely on floating-point confidence. Runtime grows exponentially with the truncation index, and these finite tests are not an infinite proof.

No independent audit has been performed. The full historic literature cannot be exhaustively ruled out, especially older marker or border-avoidance enumerations not available in full text.
