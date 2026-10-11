---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Using Fu--Xie--Li's equivalent unit-sphere formulation, set \(u=x+y\), \(v=x-y\), \(a=\|u\|\), \(b=\|v\|\), and assume \(a\ge b\). The objective is \((a+b)\|bu-av\|/(2ab)\). Since \(u-v=2y\), the triangle inequality gives \(\|bu-av\|\le2b+(a-b)b\). With \(t=b/a\) and \(a\le2\), this becomes at most \((1+t)(2-t)=9/4-(t-1/2)^2\). The explicit pair \(x=(0,1),y=(1,1)\) in \(\ell_\infty^2\) has \((a,b)=(2,1)\) and attains \(9/4\). The inspected rational verifier independently checks the scalar identity and witness.

## originality

PASS

The defining Fu--Xie--Li paper was inspected in full. It proves the equivalent formula, gives the previous universal upper bound \(\sqrt2+1\), computes \(DW_I(\ell_\infty^2)=9/4\), then explicitly conjectures that \(9/4\) is the best universal upper bound and says they cannot prove it; its closing questions again ask for the best bound. Resultary and adjacent-literature searches found no intervening theorem resolving that stated problem. The audited triangle-inequality reduction therefore closes an explicit published gap.

## value

PASS

The theorem gives the exact best universal value of a named Banach-space geometric constant and resolves the defining paper's explicit conjecture, with a sharp witness. The simplicity of the final estimate does not make the exact universal endpoint a routine or unmotivated fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
