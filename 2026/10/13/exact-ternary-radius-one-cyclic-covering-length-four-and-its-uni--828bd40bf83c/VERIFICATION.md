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
# Verification procedure and limits

The standalone `verify.py` needs Python \(3.10\) or later and the standard library only. Invoke `python3 verify.py` from the extracted artifact directory. It rebuilds all \(81\) ternary four-words and each radius-one Hamming ball (exactly nine targets), then checks **every** indexed cyclic string of lengths \(9\), \(10\), \(11\) and \(12\). For every string, all modular four-windows are evaluated and their ball bitmasks combined. Thus the covering predicate is equivalent to equality with the all-ones \(81\)-bit target mask; there is no sampling and no external solver.

Expected full census output:

```
length=9 total=19683 covering=0 max_covered=69
length=10 total=59049 covering=0 max_covered=76
length=11 total=177147 covering=0 max_covered=76
length=12 total=531441 covering=48 max_covered=81
orbits_without_reversal=2, each_size=24
orbits_with_reversal=1, size=48
witness=001022021121
VERIFY_OK
```

For shorter lengths, the exact radius-one sphere volume gives \(9m<81\), so lengths at most eight cannot work. The symmetry check forms all rotations of every relabeling of both the witness and its reversal and verifies equality with the **entire** length-twelve winner set. A separately written C++17 implementation is embedded as `verify_independent.cpp`. Compile and run with `g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`; it independently recomputes the same complete four-length census and determines the one equivalence class under relabeling, rotation and reversal. The two implementations agreed.

These checks establish the stated exact finite result; they do not extrapolate to larger spans or other radii. This procedure is reproducible but is not a separately conducted independent scientific audit.
