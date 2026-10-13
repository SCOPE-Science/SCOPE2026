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

The universal result follows from the formula \(\phi=M^2/(h'D)\), polynomial coprimality (using \(h(0)\ne0\) and \(\gcd(h,h')=1\)), exact leading degrees, and the formal derivative \(\phi'=rh(2h'+rh'')/D^2\) when \(p\mid m\). These are mathematical proof steps and do not depend on computational extrapolation.

Execute `python3 verify.py` using Python 3 with no third-party modules. It tests finite-field polynomial gcds, reduced rational-map degrees, and the derivative test for \((p,m)=(7,2),(7,3),(3,2),(5,4),(3,3),(5,5),(7,7)\), with separate squarefree coefficient choices at \(m=p\) exhibiting separable and inseparable maps. The expected terminal line is `VERIFY_OK: polar-degree phase tests and m=p separability examples`.

The verifier does not enumerate infinitely many parameters or primes, and tests alone do not establish novelty or the universal theorem. The characteristic-two non-dominance and characteristic-zero branch are proved symbolically in `RESULT.md`, not numerically replayed by the finite-field program.
