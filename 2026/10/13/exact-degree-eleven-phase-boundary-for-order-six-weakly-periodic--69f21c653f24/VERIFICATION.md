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
# Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier uses only exact integer and rational arithmetic.

It reconstructs the identity
\[
D(\xi)^2G\!\left(\xi,\frac{N(\xi)}{D(\xi)}\right)=-J(\xi),
\]
where \(N(\xi)=5\xi^4-12\xi^2+3\) and \(D(\xi)=4\xi^3-6\xi\). It also constructs the numerator of \(P(N/D)\) after clearing \(D^{11}\) and verifies by exact polynomial division that \(J\) divides it.

An exact Sturm implementation verifies one root of \(J\) on \((2,\infty)\), one root in \((2.07717459,2.07717460)\), and one root of \(P\) in \((1.894515,1.894516)\). Exact endpoint inequalities and positivity of the derivative of \(A(\xi)=N(\xi)/D(\xi)\) transfer the \(\xi\)-isolation to the stated \(\alpha\)-isolation.

Finally, exact polynomial arithmetic over \(\mathbb F_{41}\) applies the Rabin irreducibility criterion to the degree-\(11\) reduction of \(P\). The script checks
\[
\gcd(P,X^{41}-X)=1
\]
and
\[
X^{41^{11}}-X\equiv0\pmod{P}.
\]
Because \(11\) is prime and \(P\) is primitive over \(\mathbb Z\), this proves irreducibility over \(\mathbb Q\).

Expected successful output:

`VERIFY_OK J_gt2=1 J_tight=1 P_tight=1 elimination=exact irreducible_mod41=1`

The verifier does not re-prove the primary paper's Gibbs-measure correspondence or its phase-count theorem; those are cited premises. It verifies the new exact algebraic identification of the critical constant.
