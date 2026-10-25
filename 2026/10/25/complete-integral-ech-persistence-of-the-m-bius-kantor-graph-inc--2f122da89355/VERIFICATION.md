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

# Verification evidence

Execute `python3 verify.py` using Python 3 standard library. The executable independently rebuilds the graph and all Čech simplices from the radius-half edge-midpoint/vertex neighborhood rule. It checks the following exact numbers of nonempty faces at integral scales \(0\) through \(7\):

\[
16,\;40,\;168,\;976,\;11028,\;64444,\;65534,\;65535.
\]

It constructs and verifies acyclic vertex-toggle matchings with respectively \(0,15,79,464,5492,32218,32766,32767\) matched incidences. At scale four, exactly \(41\) critical degree-four and \(2\) critical degree-six cells remain alongside one vertex; no lower or intervening critical cells remain. At scale five the exact integral critical boundary matrix is

\[
\begin{pmatrix}
0&1&-1&0&0\\
0&1&-1&0&0
\end{pmatrix},
\]

whose unique nonzero Smith invariant is a unit. Every oriented Hasse incidence is topologically sorted to certify acyclicity. The checker independently computes mod-two simplicial boundary ranks at scales three, four and five and proves the scale-one inclusion survives to scale two using sixty-four validated free-face collapses. It checks purity, antipodal facets and the final simplex.

Expected terminal signal: `VERIFY_OK`. These are exhaustive exact checks of a finite graph, not a proof of a broader graph-family theorem. Homotopy information at scale four beyond the stated cellular model remains unproved, and no independent audit or external certification is asserted.
