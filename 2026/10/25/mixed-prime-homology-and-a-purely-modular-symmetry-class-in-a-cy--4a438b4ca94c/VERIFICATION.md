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

# Computational verification

Run `python3 check.py` with Python 3, NumPy and SymPy. The code starts from the matching definition, enumerates each of the 1,545 nonempty simplices, verifies freeness of the order-five column action on simplices and derives each canonical quotient cell. It builds all four signed integer boundary maps and checks that consecutive compositions vanish.

The exact Smith factors, by degree, are \(1^{\times4}\), \(1^{\times35},5\), \(1^{\times83},3\), \(1^{\times24}\). The modular boundary ranks at primes \(2,3,5,7,11\) are tested through an independent Gaussian eliminator. The checker additionally constructs the explicit 24-term integral three-cycle and verifies that its Bockstein cup pairing equals \(2\pmod5\), then independently enumerates all 120 row permutations to calculate the seven rational Lefschetz character values.

The finite computation establishes only the stated five-by-five result. The simply connectedness of the covering chessboard complex is supplied by the published chessboard connectivity theorem, not inferred from a homology calculation. The character and cup tests do not constitute independent review or mathematical certification.
