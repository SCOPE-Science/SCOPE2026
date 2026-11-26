---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For q=3 and m=1 the finite sums give p_k(e^(2x))=e^(kx) sinh((k-1)x)/sinh x and p_k(e^(2x))+1=e^((k-1)x) sinh(kx)/sinh x. All exponential prefactors cancel; the resulting logarithm is even and analytic near the positive-domain center since Q_k(18/7)=-120/49, Q_k(0)<0 and its positive zero s*>18/7>2. Independently differentiated the original finite polynomials using power sums, then applied the log-derivative formulas: python -B reviews/check_potts.py verifies the exact quadratic, checks the critical quartic by polynomial remaindering modulo Q_k, verifies the slope at that root, and checks the sign identities. R_k(18/7)=3(43k^2+5k-2)>0 and dR_k/ds=7(k-2)(k+1)(2k-1)>=0, including k=2 where the slope in s vanishes. Thus c4*<0 while c2'(t*)=A_k>0. The analytic equation F_x/(2x)=c2(t)+2c4(t)y+O(y^2), y=x^2, has exactly one nearby analytic y-branch by the implicit-function theorem, y=C_k delta+O(delta^2), C_k=-A_k/(2c4*)>0. For small positive delta the two real noncentral roots have second derivative 4y times the negative y-derivative of that equation, while the center has positive second derivative. Conversion to log v multiplies x by 2, and substituting gives log height gain (A_k C_k/2)delta^2+O(delta^3). No side pair is asserted at delta=0, and none of the derivation addresses distant extrema. The frozen script was inspected, not run: it normalizes P used without definition in the prose, checks the quadratic, quartic reduction and sign certificates symbolically, and evaluates slope/branch signs at finitely many k; the slope identity and normal form were independently derived here, not inferred from that finite loop.

## originality

PASS

The distinct claim is the explicit nonzero quartic normal form at the known threshold for every tree order and the resulting local branch and height amplitudes. The threshold itself, reciprocal symmetry and generic bifurcation argument are not new. The global uniqueness conjecture is a different issue.

## value

PASS

The normal form gives a substantive uniform local classification at the source's critical external-field boundary, distinguishing quartic nondegeneracy from mere second-derivative sign change. The branch and height exponents with exact constants are useful when analyzing maximization near that threshold. The result does not require or resolve global uniqueness for high tree orders, and is not a thermodynamic phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
