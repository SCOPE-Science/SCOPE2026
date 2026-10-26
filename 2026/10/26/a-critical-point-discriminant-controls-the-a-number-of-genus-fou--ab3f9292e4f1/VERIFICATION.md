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

# Reproduction and limits

`check_cartier.py` checks the polynomial \(x^4\)-coefficient, derivative discriminant and critical-condition invariance for all \(100\) choices of \(\alpha\ne0,\beta,\gamma\in\mathbb F_5\), and tests every translation \(x\mapsto x+u\). The script uses only the Python standard library and runs by `python3 check_cartier.py`. The package contains the entire source. The theorem is infinite-field mathematics proved symbolically in `RESULT.md`; finite-field verification alone does not prove it.

At the stated degree, the Cartier operator maps only \(y^2dx\) potentially nontrivially and squares to zero. The proof explicitly excludes higher pole orders, other characteristics and claims about Newton polygons. Independent audit: not performed.
