---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a,b,c arbitrary in C, expand on z^4=1: the value Fourier coefficients at frequencies 0,1,2 are S=|a|²+|b|²+|c|², U=b conjugate(a)+c conjugate(b), T=2 Re(c conjugate(a)); the derivative ones are H=|b|²+4|c|² and V=2c conjugate(b) at 0,1, with frequency 2 zero. Conjugate symmetry recovers the rest; the aliased frequency 2 of the value channel retains only the real part. For b≠0, gauge b>0. With x=|b|², A=U−V/2 and C=V/2, each positive common solution of x²−Sx+|A|²+|C|²=0, x²−Hx+4|C|²=0, and Tx=2 Re(AC) reconstructs exactly one class. Two distinct roots force the monic quadratics to be identical and T=Re(AC)=0. For c≠0 the second root is 4|c|², giving exactly the stated partner and a collapse iff |b|=2|c|. With c=0, H fixes x. For b=0 the two moduli and cosine fix the phase difference up to reflection, distinct exactly when its sine is nonzero; zero coefficients leave no relative phase. A crossover requires U=V=0, forcing the b≠0 representative to be a pure middle monomial, and matching H,S,T then gives exactly the two quadrature partners with |a|²=3|c|². At the stated witness all eight intensities are 1 by direct substitution. Zero is uniquely recovered, and the nonuniqueness locus is contained in the proper real-algebraic zero set of |b|²(|a|²−3|c|²). This exhausts the nonempty fibers without any numerical assumption.

## originality

PASS

The four-sample obstruction, the published collision z versus (z²+i√3)/2, and the universal five-sample threshold are prior art. Credit is limited to the sharp three-class bound, complete fixed-design inverse, and classification of all exceptional fibers, including the distinct fully supported scaling mechanism. No inspected stronger or equivalent result supplies that census.

## value

PASS

At the natural sample count where universal recovery first fails for quadratics, identifying exactly when the fixed measurements nonetheless recover a unique polynomial is useful for interpreting noiseless inverses. The sharp size bound, exact partners and distinction between relative-phase reflection and the full-support scaling branch supply substantially more information than a known obstruction or a generic uniqueness statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
