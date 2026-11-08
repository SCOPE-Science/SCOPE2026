---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The prism squares have four signed ±1 color increments summing to zero as an integer (any multiple of five has absolute value <=4), hence top and bottom rim windings coincide. The integer rim sum yields exactly w≡n mod 2 and |5w|<=n, all realizable using one rim sequence and constant vertical sign. Recoloring changes signed increments by an exact vertex coboundary, preserving winding. If |5w|<n, a directed cycle of length L would have integer signed circulation L=5wm with L≥n|m|, impossible for m=0 or |5w|<n. Two colorings of the same winding differ by an exact signed 1-cochain; admissible integer heights form a distributive lattice, and a finite acyclic source-raising argument joins them. A published cycle-target Hom theorem identifies each such acyclic-orientation component with S¹. Extreme winding forces all rim and vertical signs and hence exactly 10 isolated colorings per sign, totaling 20 when 5|n. Independent backtracking enumeration and recoloring-union-find for n=3..8 yielded respective graph-homomorphism totals 0,190,20,1410,560,11070 and exactly the predicted winding components (a check, not proof of the all-n circle type).

## originality

PASS

The full homotopy type of Hom(C_n□K2,C5), n>=3, is one circle for each admissible nonextreme signed winding and exactly twenty isolated vertices precisely when 5 divides n. Originality judgment is best-of-knowledge, with direct comparison to inspected same-object and stronger sources; published ingredients are acknowledged and absent search hits are not proof.

## value

PASS

Ordinary graph-Hom complexes record more than mere colorability. The natural infinite family of polygonal prisms exhibits an exact winding decomposition and a sharp five-divisibility jump from loop components to twenty isolated points; the formula provides a useful explicit topological classification and separates source-reconfiguration connectivity from the known codomain-based component type theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
