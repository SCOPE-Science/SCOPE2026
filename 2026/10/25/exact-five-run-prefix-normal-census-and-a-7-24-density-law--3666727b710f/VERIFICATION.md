---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

At the exact seven-blob frozen Git tree 9a034ea3a9fe09f745d52d0dae73a6bdc13b4777 (all six root Git blob IDs and src/verify.py were fetched; recursively reconstructed Git tree SHA matches), the final claim counts exactly words 1^a0^b1^c0^d1^e with all a,b,c,d,e positive. The prefix-normal condition for all factor lengths is equivalent to the prefix having the minimal k-gap window sum for each k between successive ones. The only nonzero gaps are b at index a and d at index a+c. Windows of length k<a have zero prefix-gap sum; for a<=k<a+c, avoiding the first spike is possible iff c+e-1>=a, and all such windows include d since c,e<=a; for k>=a+c all windows contain b and d. Thus necessity and sufficiency is c<=a,e<=a and (c+e<=a or d>=b), with equality cases checked. Region c+e<=a has triple enumerator A(z)=z^4/[(1-z)(1-z^2)^2] and unrestricted (b,d) factor z^2/(1-z)^2. Region c,e<=a<c+e has triple enumerator T-A, with T=z^3(1+z^2)/[(1-z)^3(1+z)(1+z+z^2)], and (b,d) factor z^2/[(1-z)(1-z^2)]. Independent exact symbolic simplification gives the claimed P(z)=z^5(1+z+2z^2+2z^3+z^4)/[(1-z)^5(1+z)^3(1+z+z^2)]. The order-five pole at z=1 has coefficient 7/24 while other unit-circle poles have order at most three, so p_n=7n^4/576+O(n^3) and dividing by C(n-1,4) yields exactly 7/24. Independently, normalize five iid exponential lengths: A>=C+E has probability 1/4, and [A largest but A<C+E]∩[D>=B] contributes 1/24. The proof covers n>=5, n<5 gives zero, exact five nonempty maximal runs, no trailing zeros; it does NOT count all prefix-normal words. Finite checks alone would not prove any infinite identity.

## originality

PASS

The exact fixed-five-run length generating function and conditional density 7/24 are not asserted in the four relevant primary papers inspected. The universal prefix-normal gap inequalities and general run rejection/membership tests are established prior results; the special two-spike membership criterion is therefore only proof machinery, not an independent novelty claim. Burcsi et al. 2017 Proposition 16 tabulates GFs at fixed ONE COUNT (0..6), not variable one count and exactly five maximal alternating runs; the general rationality claim is also for fixed one count. Balister–Gerke counts ALL prefix-normal words at exponential order; Gray-code and collapsing papers deal with generation and classes, not the exact five-run coefficient series. The nontrivial unbounded run-composition sum and its limiting conditional probability are new to best knowledge after Resultary and targeted web/database searches. This is not a proof of priority and possible unindexed enumerations remain a risk.

## value

PASS

The exactly-five-alternating-run stratum is a natural first nontrivial three-one-island class with interaction between TWO separating zero gaps: bounding later one-run lengths alone is not sufficient, since the comparison d>=b matters. The complete coefficient-generating function and limiting 7/24 share of all five-positive-run compositions measure prefix-normal frequency on this natural combinatorial slice. The result is independently useful for refined prefix-normal enumeration, generating witnesses and checking run-sensitive algorithms even though it does not solve unrestricted prefix-normal counting. It is not a mere parameter rename, an arbitrary tiny instance, or a recomputation of an identified known table. Its narrowness, standard gap-equivalence prerequisite and absence of a general all-run theorem are explicit limitations; neither code reproducibility nor novelty alone is used to justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
