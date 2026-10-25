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

# Reproducibility and limits

The standalone Python 3 checker `verify.py` requires only the standard library. Execute `python3 verify.py` beside `verify_output.txt`; expected terminal output is exactly the single line recorded in the latter file. The checker compares the direct unrestricted zero-forcing polynomial for each assembled graph against the independently computed four-local-polynomial splitting identity, covering every ordered pair from 43 connected rooted labeled graph instances of orders two through four and every ordered triple from five rooted graph instances of orders two and three. It also compares 23 clique-bouquet examples against their displayed closed form.

All integers and polynomials are computed exactly. The tests enumerate 1,974 rooted assemblies and 23 clique bouquets; they do not establish an infinite identity by themselves. The unrestricted theorem is proved combinatorially in `RESULT.md`, especially the monotonicity of root-suppressed closure and the complete root-blue/root-white case split. No external or independent scientific review has occurred.
