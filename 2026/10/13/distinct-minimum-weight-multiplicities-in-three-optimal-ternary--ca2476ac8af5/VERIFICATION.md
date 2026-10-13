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
# Finite verification

Run `python3 verify.py`: it reconstructs the field, checks a primitive element, verifies ten independent parity-check rows, exhausts the signed-coordinate pair syndrome buckets, and prints the three exact coefficients and `VERIFY_OK`. Run `g++ -O3 -std=c++17 direct_check.cpp -o direct_check && ./direct_check`: the independent direct-support algorithm builds field arithmetic from the specified polynomial, exhausts every three- and four-position support with every nonzero sign pattern up to scalar multiplication, checks A3=0, confirms the same A4 counts, and prints `VERIFY_OK`. Both runs completed successfully. No external data file is needed.

The C++ test directly enumerates all four-support candidates rather than sampling. The Python bucket normalization is a proved six-to-one mapping for each weight-four word. Both are finite calculations specific to the three displayed codes; they do not certify results for other exponents or extension degrees. Independent validation is not claimed.
