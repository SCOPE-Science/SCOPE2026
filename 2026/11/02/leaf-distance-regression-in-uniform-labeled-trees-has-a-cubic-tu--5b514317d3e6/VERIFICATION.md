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

# Verification of the conditional leaf–distance law

The exact analytic proof uses the rooted-forest determinant and an explicit leaf-deletion bijection. The factor \((s-q)(n-r-q)^{n-s-1}\) counts prescribed-path trees having \(r\) selected off-path leaves and \(q\) selected path-endpoint leaves; dividing by \(sn^{n-s-1}\) gives the joint inclusion probability. Expanding the product of indicator generating functions proves the full conditional law. Algebraic subtraction reduces the entire regression sign pattern to the strictly decreasing expression \(2(n-1)-k(k+1)^2\).

The standalone program `VERIFY.py` uses Python 3's integer and `fractions.Fraction` arithmetic. Run `python3 VERIFY.py` from the extracted directory. It enumerates all \(280391\) labeled trees for \(n=3,4,5,6,7,8\), tests every eligible chosen leaf-subset configuration relative to the canonical marked path, and checks the sign identity for every \(3\le n<150\). Its observed output was `PASS: 280,391 trees enumerated; 11,214 exact assertions`.

The program verifies only the finite cases within its explicit ranges. It is not an independent validation of originality or a proof of the unrestricted theorem. An independent scientific audit has not been performed.
