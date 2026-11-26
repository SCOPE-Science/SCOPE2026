---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The length-three prefix and suffix sets are disjoint, and their outer length-two end sets A,B are disjoint, including self-comparisons. Each word is uniquely specified by the two triples and one middle block for n≥6. The frozen upper-envelope calculation allocates each common candidate triple to one end and uses all 3^9 assignments of ordered pairs to neither end, A, or B. Independent upper bound without that certificate: for bounding candidate triple sets U_A,V_B enlarge B so that A,B partition all nine pairs. Reverse triples and exchange ends if needed so a=|A|≤|B|. For a≤2 the product is at most (3a)(27−3a)≤126. Otherwise a=3 or 4. Write r_j,c_j for the row and column degrees of A. The number of triples shared by U_A,V_B is h=Σ_j c_j(3−r_j)=3a−Σ_j r_j c_j. For a=3, sorted row sizes (3,0,0), (2,1,0), (1,1,1) give degree-product sums at most 3,5,3 respectively: each c_j is bounded by the number of occupied rows, and Σ c_j=3. For a=4 the row patterns (3,1,0), (2,2,0), (2,1,1) give at most 8,8,7 using the same bounds and Σ c_j=4. Thus h≥4; the disjoint selected end sets have total size at most |U_A∪V_B|=27−h≤23. Their product is at most floor(23²/4)=132. For the lower bound, P has nine triples with middle zero and two with both ends zero and middle nonzero; T has 3·2·2=12. Their relevant ordered pairs and triples are disjoint because the prefix requirements use zeros and the last pair of T does not. Every middle block is free, yielding the claimed optimum. A separate exact check enumerated the 512 complete ordered-pair partitions, built the corresponding triple sets, and maximized x·(|U_A∪V_B|−x) over integers |U_A∖V_B|≤x≤|U_A|; it found 132 with six maximizing partitions. The uploaded verifier was inspected but not executed. The maximum is for restrictions at lengths two and three only, with no conclusion for n<6.

## originality

PASS

The distinct content is the sharp ternary base-six value and its attaining end blocks. Stanovnik already gives the arbitrary-length reduction for n>6, and the boundary-set framework is not itself new. Checked general bounds and published construction counts do not fix the optimum at these parameters.

## value

PASS

Length six is the first stable length from the published reduction, so the finite optimum is not an arbitrary instance: it determines every larger length. The sharp constant 132 and explicit attaining end blocks improve on the cited bipartition sizes and prove optimality over all ternary codes with exactly these overlap restrictions, a useful baseline for restricted-overlap constructions. The scaling itself is prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
