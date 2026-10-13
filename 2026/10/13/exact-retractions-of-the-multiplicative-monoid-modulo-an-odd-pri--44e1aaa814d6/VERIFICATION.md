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

The proof checks the composition-idempotence equation on the published normal form for every endomorphism of \((\mathbb Z/p^e\mathbb Z,\cdot)\) when \(p\) is odd.

The critical steps are:

1. Restriction to the cyclic unit group of order \(N=p^{e-1}(p-1)\) gives the necessary and sufficient congruence \(t^2\equiv t\pmod N\).
2. Comparing the valuation of the image of \(p\) under one and two applications forces either \(v=1\) or total collapse of all nonunits to \(0\).
3. In the \(v=1\) branch, equality on \(p\) is exactly \(r^t=1\pmod{p^{e-1}}\); equality then holds on every nonzero residue because \(p\) and the units generate it multiplicatively.
4. The cyclic group of order \(N_-=p^{e-2}(p-1)\) contributes \(\gcd(t,N_-)\) choices of \(r\).
5. CRT choices \(t\equiv0\) or \(1\) on each prime-power component of \(N\) yield
\[
\sum_{t^2\equiv t\ (\mathrm{mod}\ N)}\gcd(t,N_-)
=
\prod_{\ell\mid N}\bigl(1+\ell^{\nu_\ell(N_-)}\bigr).
\]

The standalone script `check_retractions.py` does not assume the parameter classification when enumerating the test cases. It generates all monoid endomorphisms from all possible images of a primitive unit generator and of \(p\), verifies the multiplication table, tests \(f\circ f=f\), and compares with the closed formula for moduli \(9\), \(27\), \(25\), and \(49\). The replay ends with `CHECK_OK`.

Finite checks are not used as an infinite proof. The excluded \(2\)-power case and the unavailable thesis source remain exactly the limitations stated in RESULT.md.
