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

The general result is verified by the proof in `RESULT.md`; finite computation is supplementary.

`verify_even_gl2.py` constructs \(\mathbb F_2\) and \(\mathbb F_4\) directly, enumerates all matrices in \(\mathrm{GL}_2\) and \(\mathrm{SL}_2\), enumerates every subgroup of \(\mathrm{SL}_2\), and tests the defining condition \(\chi_{xh}=\chi_x\) for every pair \((x,H)\). It also checks that every admissible subgroup is abelian, that its order is at most \(q+1\), and that the stronger order bound \(q\) holds whenever \(\operatorname{tr}x\ne0\).

The exact output is stored in `VERIFY_OUTPUT.txt`:

- for \(q=2\): \(|\mathrm{GL}_2|=6\), \(|\mathrm{SL}_2|=6\), six subgroups, maximal admissible order \(3=q+1\), no violations;
- for \(q=4\): \(|\mathrm{GL}_2|=180\), \(|\mathrm{SL}_2|=60\), fifty-nine subgroups, maximal admissible order \(5=q+1\), no violations.

These finite checks do not certify the theorem for arbitrary \(q\); that scope is established only by the symbolic argument.
