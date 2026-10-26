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

## Reproduction

Run `python3 CHECKER.py` with Python 3. The accompanying `CHECKS.txt` is the exact observed console output. The checks cover 75 parameter triples with \(2\leq k,h\leq6\), independently verify the generated group action size, calculate the quotient final set, and minimize the three automata.

## Analytical verification

The infinite proof uses two explicit words that induce trivial first-coordinate permutations, \(a^k\) and \((ab)^{k-1}\), while moving the counter by coprime increments. Full product reachability then gives minimality and an exact stabilizer image. The known unary interval theorem supplies the remaining smaller output values and the impossibility of universal realization over one letter.

## Limits

These finite computations do not prove the infinite case; that conclusion relies on the algebraic argument in `RESULT.md`. The published unrestricted-spectrum result uses a ternary witness, so its existence theorem alone cannot imply a fixed binary-alphabet realization. No independent audit or external validation has been performed.
