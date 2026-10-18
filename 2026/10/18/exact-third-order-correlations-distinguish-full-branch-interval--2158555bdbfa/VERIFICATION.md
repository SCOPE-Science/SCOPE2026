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
# Verification details
The exact analytical derivation uses the normalized inverse-branch Perron operator on the two-dimensional centered polynomial span of \(g=x-1/2\) and \(h=g^2-1/12\). Its action is triangular, \(Pg=\theta g\), \(Ph=Ah+Bg\), and the all-lag formula follows by two applications of transfer duality. The finite check cannot substitute for this proof.

`verify.py` independently enumerates all inverse cylinders up to the tested lag, integrates the resulting cubic product using `fractions.Fraction`, and compares these exact rational integrals to the formula. Five two/three-branch orientation/length cases and two separate four-equal-branch patterns are tested. The program also checks the explicit unequal four-branch witnesses and the skew-tent sharp critical point symbolically. Run with Python 3 and SymPy using `python3 verify.py` in a directory containing the script. Actual execution result:

`VERIFY_OK 49 exact rational independent cylinder and witness checks; sharp critical 0.72567115994167 amplitude 0.0046158691679921`

The verifier does not test every length/lag or prove the infinite theorem; no other auxiliary data or external code is required beyond Python 3 and SymPy. The historical novelty assessment compares the 2006 NOLTA paper, the 2014 IJBC article, the 2010 arXiv transfer paper, existing accessible research records, and actual archive searches. Historical completeness remains uncertain; no independent external review is asserted.
