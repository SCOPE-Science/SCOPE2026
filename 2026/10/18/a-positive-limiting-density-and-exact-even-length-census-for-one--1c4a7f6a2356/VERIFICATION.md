---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: From the cited single-marker saturation equivalence, the forbidden overlaps are E_j={omega[m-j-1]=A and suffix_j=prefix_j}, 0<=j<=m-2; exclude also the all-B word. For m=2J+2 a smaller period d<=J+1 can be multiplied into [J+2,2J+2], so E_j with j>J is redundant. Disjoint left prefix L and reversed right suffix R give event F_j and N_{2J+2}=2^{2J+2}q_J-1. The cylinder-antichain count yields q25=1298518439058409/2^52; the geometric union bound gives 0<=qJ-rho<=2^{-J-1} and the stated arbitrary-m error. Independent brute-force enumeration of literal E_j for every m=2..14 gave N_m=[1,2,5,9,20,39,78,151,304,601,1200,2381,4762,] and independent L/R event enumeration reproduced J=0..5. A separate compiled C++ enumeration of 2^27 right-tail words independently reproduced the exact J=25 numerator. Positive rho follows from q25-2^-26>0; experiments do not prove the infinite quantifiers, which are supplied by the period and probability arguments. The Cuezva saturation criterion itself is taken as an explicitly attributed external theorem, not reproduced or independently certified because full primary text remained unavailable.

## originality

PASS

PASS on a qualified best-of-knowledge reading: Cuezva supplies single-marker bijectivity through saturation, not the claimed exact even-length overlap count, independent-prefix probabilistic representation or positive limiting density. The Boyle–Lind–Rudolph automorphism-group construction and Hedlund full-shift theory have broader objects but neither a deduction of this restricted one-letter-head count nor an exact rho was identified. The unavailable Cuezva full text is a material priority/assumption risk; neither failed search nor restricted scope alone establishes novelty.

## value

PASS

PASS: The proportion of reversible elements in a natural infinite family of explicitly local binary marker maps is a mathematically motivated exact invariant, rather than arbitrary finite enumeration. The even-length exact census, computable limiting constant and rigorous uniform convergence rate answer a natural density question not implied just by a bijectivity test; a researcher studying restricted symbolic automorphism families could use these numbers even without general automorphism-group consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
