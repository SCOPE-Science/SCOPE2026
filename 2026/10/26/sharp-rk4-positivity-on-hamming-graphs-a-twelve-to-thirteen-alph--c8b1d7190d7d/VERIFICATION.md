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

# Reproduction of mathematical checks

Run `python verify_hamming_rk4.py` after installing the single dependency in `requirements.txt`. The script symbolically reconstructs the four nonzero Hamming-distance off-diagonal polynomial classes, checks the Bernstein positivity certificates including the \(q=13\) change, and directly computes exact-rational generator powers on representative finite Hamming graphs. Its successful output was:

`VERIFY_OK: symbolic Hamming heat-kernel coefficients r=1..4; Bernstein positivity and sharp q=13 crossover certificates; 32118 exact rational transition-entry comparisons`

The direct checks include dimensions three, four and five, alphabets two, three, four, six, twelve, thirteen and seventeen (as paired in the code), and timesteps on both sides of the distance-three boundary. These tests do not prove the infinite parameter classification; that follows from the self-contained Bernstein and distance-three arguments. The independent audit channel is not performed; no independent certification is claimed.
