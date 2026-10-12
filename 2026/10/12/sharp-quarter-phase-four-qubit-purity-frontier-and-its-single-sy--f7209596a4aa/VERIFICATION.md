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

# Reproduction and verification

The source files `verify.cpp` and `verify_independent.py` are standalone and use no third-party numerical libraries. In a directory containing both files, execute:

```sh
c++ -O3 -std=c++17 verify.cpp -o verify
./verify
python3 verify_independent.py
```

The C++ checker iterates over all \(4^{11}=4,194,304\) distinct affine-phase-gauge classes, exactly computes the three \(256P_A\) numerator values, and asserts the minimum of their maximum is \(88\). It asserts that precisely \(96\) gauge classes attain the optimum, all with purity-numerator triple \((88,88,88)\), and that these \(96\) form the generated permutation/bit-flip/conjugation orbit. It separately checks all \(2^{11}\) real-sign gauge classes and obtains optimum numerator \(96\) with \(272\) minimizing gauge classes.

The Python checker independently reshapes the phase tensor into three complex matrices, evaluates their \(4\times4\) Gram matrices, checks the \(96\)-element symmetry orbit, verifies the vanishing one-qubit coherences and four-spin-flip squared overlap \(1/16\), and repeats the complete \(2^{11}\) real-sign sweep. Successful outputs begin with `VERIFY_OK` and `CROSSCHECK_OK` respectively.

The universal bound \(\max_A P_A\ge11/32\) depends on an analytic four-qubit inversion identity and parity quantization and does not depend on enumeration. The exact cardinality and single-orbit classification do depend on the exhaustive finite computation, whose full iteration and normalization are included. No independent external audit or laboratory validation is implied.
