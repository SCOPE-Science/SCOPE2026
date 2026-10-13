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

The infinite proof has three independent components.

1. For \(a=b+t(b+1)\), reduction modulo \(q=2^{b+1}-1\) gives \(p\equiv-2^b\pmod q\), hence \(\gcd(p,q)=1\). This justifies the distinct divisor box used in the representation.
2. Substituting the definitions into the full divisor-box sum minus the two omitted complementary pairs simplifies identically to \(2N_{b,t}\). This establishes strong pseudoperfectness for all parameters.
3. The elementary factorization of \(z^r+1\) shows that \(2^m-1\) is never a nontrivial perfect power. Because it is coprime to \(p\), its prime valuations occur unchanged in \(N_{b,t}\), excluding every nontrivial perfect-power presentation and proving primitivity.

The growth estimate \(N_{b,t}=2q\,4^a(1-(2^b+1)/2^{a+1})\) gives the counting law directly.

`verify_primitive_rows.py` is a finite regression check. It verifies exact complement closure and sums on \(1\le b,t\le9\), and checks the stronger \(b=1\) row for \(2\le a\le39\). Its output is stored in `verify_primitive_rows.out`. No finite check is used to infer an infinite statement.
