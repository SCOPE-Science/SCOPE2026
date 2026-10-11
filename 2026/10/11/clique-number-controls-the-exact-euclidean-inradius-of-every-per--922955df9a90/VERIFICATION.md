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
The arbitrary-graph-family claim is proved symbolically in `RESULT.md`; finite experiments are corroborative only.

Verified premises and steps:
- For perfect \(G\), nonnegativity together with maximal-clique inequalities is the complete H-description of \(\operatorname{STAB}(G)\).
- Coordinate inequalities and maximal-clique inequalities are facet-defining; explicit affinely independent stable-set vertices are supplied in the proof.
- The Euclidean distance from \(c\) to \(x_v=0\) is \(c_v\), while the distance to \(x(C)=1\) is \((1-c(C))/\sqrt{|C|}\).
- A maximum clique gives the sharp upper bound \(r(\omega+\sqrt{\omega})\le1\).
- The uniform center attains that bound simultaneously for every defining halfspace.
- The optimal-radius halfspace conditions are exactly the displayed complete incenter set.
- Equality on maximum cliques forces all covered coordinates to the uniform value, and strict slack gives the converse nonuniqueness construction.

`verify.py` checks representative perfect graph families by explicit stable-set and maximal-clique enumeration, including graphs with and without maximum-clique coverage. It does not assess originality and is not used as proof of the all-graph statement.
