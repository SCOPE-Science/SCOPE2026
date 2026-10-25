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

# Computational verification

The standalone `verify.py` reconstructs the unordered two-particle cubical cells with disjoint graph-cell closures. Its signed boundary conventions are \(\partial[e,v]=[b,v]-[a,v]\) for an oriented edge \(e:a\to b\), and \(\partial[e,f]=[b,f]-[a,f]-[d,e]+[c,e]\) when \(f:c\to d\) and \(e<f\). The code verifies every \(\partial_1\partial_2\) column vanishes and computes exact modular elimination ranks. A nonzero minor modulo three proves the corresponding lower bound on the rational boundary rank; the independent cycle-surjectivity argument in `RESULT.md` supplies the opposite bound on rational first homology.

The program also computes the signed traces by two independent finite descriptions: direct enumeration of invariant oriented cubes and the fixed-vertex/edge formula. All permutations of six labels and all conjugacy types of seven labels were checked. Its rim-hook recursion computes the rational \(S_6\)-irreducible character multiplicities, checking nonnegativity and total dimension. `verification_output.txt` is the exact stdout from a local run of `python3 verify.py`.

Finite runs are **not** a proof for all values of \(n\); the infinite statement rests on Ko–Park’s theorem and the all-parameter signed-chain argument. The verifier does not establish integral \(H_1\) structure, integral module splitting, or independent review.
