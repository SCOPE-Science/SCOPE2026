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

# Reproducible verification and boundaries

The proof in `RESULT.md` is unconditional for all even bases \(b\ge2\) and positive divisors \(d\mid b-1\). Its critical steps are the congruence \(N\equiv s_b(N)\pmod d\), the alternating-digit congruence modulo \(b+1\), explicit witnesses for the smallest allowed even/odd sums, and closure by concatenation.

The standalone `VERIFY.py` program checks, for each even base \(2\le b\le24\) and every positive divisor \(d\mid b-1\), **all** attainable digit sums \(1\le u\le b+3d+5\) without bounding the number of digits. A finite automaton has states \((r,u)\), tracking residue \(r\) modulo \(d(b+1)\) and total digit sum \(u\); breadth-first reachability includes leading-nonzero initialization and zero-digit transitions. Thus for each fixed parameter and digit-sum cutoff the search is exhaustive over all lengths. It checks the calculated reachable sums against the theorem. There are 28 parameter pairs, all passing.

Execute `python3 VERIFY.py` with Python 3. No dependencies other than the standard library. Finite checks are reproducibility aids, not a proof for arbitrarily large bases or digit sums. No independent audit was performed.
