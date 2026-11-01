---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Induction verifies f^n=(t+n,x_i,y_i product_{j=1}^n(x_i-t-j)) and the stated pullback ideal. Restriction to J=(t,y_i-x_i) gives the Koszul complex on H_n(x_i)=product_{j=0}^n(x_i-j) and P(x,n). The first m generators form an A-regular sequence, whose quotient B is the product of k over the finite grid by CRT, since char k=0. Koszul-cone homology gives H_1=ker(P(x,n):B->B); diagonal multiplication has exactly one zero coordinate per witness. The I_n regular-sequence condition is genuinely needed; the result does not assert it for every P.

## originality

PASS

Bell proves return times equal bounded polynomial existential zeros and a special square-time first-Tor nonvanishing example; the new result yields general exact first-Tor multiplicities conditionally on regular sequences, not merely positivity. The method is a standard Koszul/CRT deduction and its originality is confined to this exact dynamical quantitative reading.

## value

PASS

For the known Diophantine return construction, the Tor dimension is a natural finer invariant than return/nonreturn. It exactly counts bounded solutions for arbitrary m and polynomial P (subject to regularity), making homological multiplicity explicit in arithmetic dynamics. The algebraic tools are standard; the mathematical value is this motivated structural counting bridge, not a new Koszul theorem or generic textbook identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
