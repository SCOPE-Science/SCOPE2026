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

The two primary programs use distinct mathematical criteria: standard blue-vertex force closure, and existence of a nonempty fort in the initially white subset. They enumerate all \(65536\) initial configurations for each graph. The complete zero-forcing truth values coincide, bit for bit, against `certificates/forcing_truth_tables.bin` (\(16384\) bytes). Bit \(j\) of byte \(i\) in each graph block encodes the forcing status of integer blue mask \(8i+j\). The first \(8192\) bytes are the Shrikhande block.

From the package root:

```sh
python3 scripts/verify_simulation.py
g++ -std=c++17 -O2 -Wall -Wextra scripts/verify_forts.cpp -o verify_forts
./verify_forts certificates/forcing_truth_tables.bin
python3 scripts/verify_orbits.py
```

Successful execution verifies for Shrikhande the forcing coefficient vector, indexed by degrees \(10\) through \(16\), of \((3616,3600,1760,560,120,16,1)\), and for the rook graph \((3456,3504,1760,560,120,16,1)\). The total counts are \(9673\) and \(9417\). All inclusion-minimal forcing sets in both graphs have size \(10\). The fort program also checks all inclusion-minimal forts and classifies all five- and six-white subsets by their least contained fort order. The orbit program checks all \(192\) displayed affine automorphisms, proves completeness using the six-cycle root-neighborhood argument, and verifies all \(23\) Shrikhande minimum-set orbit representatives and their class sizes; the orbit-size distribution is \(192\) occurring \(15\) times, \(96\) occurring \(7\) times, and \(64\) once.

The code has no stochastic steps and needs only a Python interpreter of version at least 3.10 and a C++17 compiler; all source, certificate, and Python module dependencies are included. A checksum is a useful transport diagnostic but is not substituted for the exact per-mask comparison. No infinite generalization or independently performed mathematical audit is asserted.
