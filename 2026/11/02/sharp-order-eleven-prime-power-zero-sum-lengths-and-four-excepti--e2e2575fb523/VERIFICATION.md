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

# Verification scope

The certificate `verify.cpp` is self-contained and uses C++17 integer arithmetic with 128-bit intermediate products where needed. Compile and run:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
```

Observed output:

```text
VERIFY_OK primes=945 vectors_per_prime=352715 exceptions=23,67,89,683 deeper_checks=6
```

The checker sieves all eligible primes up to the rigorously justified bound of 100000, lifts one root of exact order eleven modulo each prime square, and enumerates all \(352715\) multiplicity vectors of mass from one to ten. It confirms only four exceptional square moduli: \(23,67,89,683\), with minima \(5,8,9,9\). For exponents \(3,4,5\) at \(23\), and exponent \(3\) at \(67,89,683\), it repeats the complete enumeration and checks minima \(9,9,11,11,11,11\), respectively.

The unbounded theorem additionally depends on two exact mathematical arguments in `RESULT.md`: the nonzero cyclotomic resultant has absolute value at most \(10^{10}\), excluding exceptional primes above 100000 at **every exponent**; and minimum zero-sum lengths are nondecreasing as the prime-power exponent rises, with upper bound eleven. Those assertions are not consequences of finite experimentation alone. The certificate has no external dependencies except a C++17 compiler. No independent audit or formal proof assistant check has been performed.
