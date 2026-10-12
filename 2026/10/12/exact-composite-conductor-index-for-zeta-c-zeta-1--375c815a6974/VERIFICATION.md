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

The proof has two independent components: an algebraic discriminant factorization and an arithmetic count of unit-pair sums.

For distinct unit classes \(a,b\pmod n\), the identity
\[
(\zeta^a+c\zeta^{-a})-(\zeta^b+c\zeta^{-b})
=(\zeta^a-\zeta^b)(1-c\zeta^{-a-b})
\]
was checked symbolically. For odd \(n\) and integer \(c\ne1\), the second factor cannot vanish, so the generator has full degree. Dividing the generator discriminant by the cyclotomic discriminant leaves exactly the product of the second factors over unordered pairs.

For each residue \(t\pmod n\), the ordered-pair count is computed locally at every \(p^e\parallel n\): it is \(p^{e-1}(p-1)\) if \(p\mid t\) and \(p^{e-1}(p-2)\) otherwise. CRT multiplication and removal of the unique diagonal when \(t\) is a unit give the exponent \(E_n(m)\), where \(m\) is the order of \(\zeta^t\). Grouping roots of equal order gives \(\Phi_m(c)\).

The bundled exact-integer program `artifacts/verify.py` was replayed from the packaged path. It checks every odd composite \(n\le315\), every residue-sum multiplicity, the total unordered pair count, and the two candidates \(c=0,2\) forced by \(|1-c|=1\). Its captured output is stored in `artifacts/verification_output.txt` and is:

`VERIFY_OK odd_composite_conductors=93 n_max=315 residue_pair_checks=15759 classification_c0_c2=OK`

The replay is finite and is not an exhaustive proof of the theorem for all conductors. The infinite quantifier is discharged by the CRT argument and cyclotomic factorization in `RESULT.md`. No claim is made for even conductors, prime conductors, or \(c=1\).
