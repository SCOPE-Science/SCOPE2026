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

Execute `python3 verify.py` in the directory containing this file. This requires Python 3 with the standard library only. The resulting output is preserved verbatim in `verification_output.txt`.

The code builds the original \(n+1\)-vertex open-neighbour adjacency operator in bit form, independently of the polynomial-ring proof. It implements binary row elimination and polynomial arithmetic, and checks the stated rank formula for 1,195 pairs of rim size and iteration count, all-time fixed-point counts for 1,160 pairs with \(3\le n\le60\), and all actual trajectories for each \(3\le n\le10\). Every least preperiod, recurrent-state count and fixed-divisor-of-time count matched. The final status was `VERIFY_OK`.

The argument in `RESULT.md` (polynomial quotient and primary decomposition, hub/parity coupling, exact rank comparisons, Möbius inversion) is the infinite-family proof. Enumeration and computed rank comparisons are finite corroboration, not certification of unrestricted claims. Independent external mathematical validation has not been performed. The dated primary research source is arXiv:0809.1526 (2008-09-09); the older printed source is from 1988 but has no separately verified day.
