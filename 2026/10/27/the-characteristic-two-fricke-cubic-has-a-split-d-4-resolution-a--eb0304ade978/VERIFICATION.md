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

The polynomial equation in characteristic two has exact partial derivatives \(yz,xz,xy,(x+y+z)^2\). Their projective common zero set is the single singular point. The quotient \(k[x,y,z]/(xy,xz,yz,x^2+y^2+z^2)\) has basis \(1,x,y,z,y^2,z^2\).

The explicit substitution \(y=xt\), \(s=xr\), \(z=x(r+1+t)\) transforms \(s^2+xyz\) into \(x^2[r^2+xt(r+1+t)]\), with exactly the two finite exceptional singular values \(t=0,1\); the third comes from the complementary chart. Each remaining germ is \(UV+R^2=0\) and one further blowup resolves it. For each power \(q\) of two, direct finite-field arithmetic may corroborate \(\#X(\mathbb F_q)=q^2+3q+1\), while the exact trace proof works for all powers.

The independent checker `checker.py` uses exact characteristic-two arithmetic and verifies \(q=2,4,8,16\); it is not a substitute for a proof over all extensions. No external independent audit has been performed.
