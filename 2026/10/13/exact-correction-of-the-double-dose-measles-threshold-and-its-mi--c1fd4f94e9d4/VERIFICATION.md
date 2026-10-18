---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Direct equilibrium balances yield V1=ψS/k3, V2=κψS/(k3k4), R=ωκψS/(μk3k4), N*=Λ/μ and S*=Λk3/D with D=μk3+ψ(κ+μ); infected E,I block equals [[-k1,βS*/N*],[φ,-k2]], giving R_tot=βφμk3/(k1k2D). The 2026 display is βφ k4/(k1k2Q), 2024 display restores k3, and subtraction simplifies to βφ k3 ψκω/(k1k2 D Q). Under all-rate unit rescaling R26 scales inversely, while correct Rtot and R24 are invariant. Local Jacobian block determinant k1k2(1−Rtot) and negative trace give stability below one, instability above; at equality a zero eigenvalue (no nonlinear classification). Independent SymPy exact algebra verified every identity and witness Rtot=93/100 versus R24=31/30 at the stated positive rates. This does not assess stochastic or global conclusions.

## originality

PASS

PASS: The 2026 full primary source equation (2.1), Table 1, and printed R_D at PDF-text p.18719 independently confirm the dimensionful expression; the 2024 full author-posted primary predecessor indeed retains k3 but normalizes by S*+V1*+V2*, omitting R* despite its six-class N. Neither corrects both defects or gives their exact positive gap. The other published measles finding concerns Milstein drift, not deterministic R0 normalization. Searches of source-specific formulas and equivalent claims identified no prior combined correction.

## value

PASS

PASS: R0 is supposed to be dimensionless and its comparison to 1 directly controls DFE local stability. The two independent errors make the 2026 number physically noninvariant and even the 2024 fixed-factor version can predict the opposite disease-free regime (the exact 93/100 vs31/30 witness). A substantive correction to a currently published mathematical model, not cosmetic dimensional editing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
