# Same-model scientific review

## Correctness
**PASS.** The lower bound \(n\ge17\) is proved directly from first-choice inequalities, without extrapolating from a finite search. Equality forces first-choice totals \(6,5,6\) and changed-group size \(2\). The remaining ballot-transfer inequalities then force exactly two normal-form families. An exhaustive verifier independently checks every anonymous profile and every homogeneous winner-raising change through \(17\) voters and matches the symbolic \(42\)-class family exactly.

Risk: the exhaustive code is ordinary finite software and therefore carries ordinary implementation risk. This is mitigated by the independent symbolic derivation, exact set equality between enumeration and generated normal forms, and exact orbit/count identities.

## Originality
**PASS.** Ornstein--Norman and Miller give broad three-candidate conditions for upward monotonicity failure. Brandt--Matthäus--Saile give a tie-independent \(17\)-voter minimal witness. The inspected sources do not state the complete minimal homogeneous boundary: \(252\) labeled-candidate anonymous profiles, \(42\) candidate-relabeling classes, the two exact normal-form families, or the fact that every harmful homogeneous move at the boundary is uniquely determined and uses exactly two voters.

Risk: failed search is not a proof of novelty. An unindexed thesis, lecture note, software table, or supplementary enumeration may contain the same boundary classification.

## Value
**PASS.** The result classifies the sharp first size of a canonical pathology of a widely studied voting rule. It converts an isolated minimal witness and general vulnerability inequalities into a complete structural boundary theorem with a short symbolic proof, exact incidence, and symmetry quotient. The boundary is mathematically natural because \(17\) is the minimal tie-independent size and the classification explains why all minimal failures share first-choice totals \(6,5,6\).

Same-model review: passed. Independent audit: not yet performed.
