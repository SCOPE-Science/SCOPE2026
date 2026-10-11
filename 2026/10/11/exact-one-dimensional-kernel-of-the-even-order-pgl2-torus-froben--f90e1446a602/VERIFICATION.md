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

The proof uses no computation. The following source facts were inspected directly in arXiv:2610.01881v1:

- the torus PGL2 skein algebra has basis consisting of \(\varnothing\), \(w\), and \((k,l)_Y\) for nonzero lattice indices;
- Theorem 5.6 sends \((k,l)_Y\) to \((nk,nl)_Y\), sends \(\varnothing\) to itself, and sends \(w\) to \(\alpha_n w\);
- for even \(n\), \(\alpha_n=0\);
- Corollaries 1.4 and 5.7 state noninjectivity for even \(n\), but do not identify the kernel.

For a putative kernel vector, the image of every non-\(w\) basis term is a distinct target-basis term because \((k,l)\mapsto(nk,nl)\) is injective. Hence all of those coefficients vanish. The coefficient of \(w\) is unrestricted, so the kernel is exactly \(\mathbb C w\).

The proved scope is only the torus, under the source's root-of-unity assumptions and with even \(n=\operatorname{ord}(q^2)\). No extrapolation to other surfaces is made.
