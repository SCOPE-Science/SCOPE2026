---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

When the hub is blue, the white induced graph consists of rim path components if and only if >=2 rim vertices are blue; blue boundary rim vertices peel the white paths, while 0 or 1 blue rim vertices leave no first move (for 1, the unique blue rim vertex has two white rim neighbors and the blue hub sees >=3 whites). Without a blue hub, any remaining white rim vertex connects the entire white induced graph through the white universal hub; a blue rim vertex has exactly one white neighbor iff its two cyclic rim neighbors are blue, exactly a run of three blue consecutive rim vertices. Such a middle vertex forces the hub, reducing to the first case. Hub-contained min sets: choose 2 rims; hub-free min sets: exactly m length-three rim runs, so binom(m,2)+m=binom(n,2). Standard 4-state 00,01,10,11 de Bruijn transfer with forbidden 11->11 and 1-transition weight x has tr(T^m) equal the cyclic 111-avoiding polynomial. Independent direct PSD-component forcing on all subsets of W_5..W_12 exactly reproduced structural criterion, across 8,160 possible subsets, with orderwise successful totals 16,37,82,177,372,773,1594,3269; finite checks corroborate proof.

## originality

PASS

Statement/implication comparison, not mere title search. Closest inspected antecedents give related machinery or narrower/scalar/qualitative statements, but not the full asserted theorem; coverage and inaccessible-source limitations are explicit.

## value

PASS

The complete characterization of every successful initial set, basis multiplicity and size distribution for an archetypal wheel graph is a motivated structural/enumerative refinement of a scalar forcing number; the polynomial answers questions that the known minimum alone cannot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
