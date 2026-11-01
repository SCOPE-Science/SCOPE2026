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

For fixed k>=1 and q=2^k, n>=1, the complete accessibility relation makes Diamond tau_a true exactly if at least one of the n labelled worlds carries Boolean type a. Thus failure of the displayed positive edge-disjunction is equivalent to the image support being independent in G. For each independent j-set there are j! S(n,j) onto functions from n worlds, so summing disjoint supports proves M_G(n)=q^n-sum_{j>=1} i_j j! S(n,j), including edgeless, complete and n=1 boundaries (empty image never arises). N_G(n)=q^n-M_G(n) has lower triangular transform with nonzero diagonal n!, hence the first q counts recover every i_j (with i0=1), and equality for all n is exactly equality of independence polynomials within the fixed q type universe. For #P membership, guess nk Boolean bits and test edge co-occurrence in polynomial time for unary n and explicit formula. For hardness, add 2^ceil(log2 r)-r isolates (q<=2r for r>=2), issue q unary-sized queries, invert with polynomial-bit arithmetic to get I_G(1)/2^(q-r)=#IndSet(H); this is a polynomial-time Turing reduction, not parsimonious. Independently enumerated 82 graphs and 424,572 labelled world assignments, 84 padded reductions, and all graph isomorphism classes through order 3; P4 vs triangle+isolate gives identical 1+4z+3z^2 and different two-world truth at types {0,2}. The fixed-G asymptotic follows from j!S(n,j)=j^n+O((j-1)^n), including alpha=1 separately. Verified exact assigned tree from 7 Git blob identities. The independent finite experiments corroborate, but do not prove, the all-n identity, Turing hardness or asymptotic.

## originality

PASS

Fresh semantic and implication comparisons against primary S5 representation/compilation, satisfiability, probability and AMC research and Resultary published mathematics found no prior theorem subsuming the combined labelled complete-frame exact all-n inversion and restricted counting-complexity result. Important elementary ingredients and the four-vertex graph collision are known; originality is best of knowledge, not absolute historical priority.

## value

PASS

This is a natural exact quantitative problem for epistemic co-occurrence formulas on one complete S5 class; an entire infinite model-count spectrum becomes a recoverable graph polynomial and is shown insufficient for logical equivalence. The inverse is a structural identification result rather than merely evaluating one formula, and #P-completeness persists under the severe depth-one positive pair-diamond restriction. The smallest logical collision and exact exponential failure rate delimit the phenomenon naturally. The support lemma, Stirling transform, generic independent-set counting hardness, and graph collision are standard/known ingredients, so value rests on their exact restricted-modal synthesis and inverse complexity classification, not an inflated claim of inventing those constituents. A plausible researcher could use the spectra classification for modal quantitative identifiability and expressive-fragment complexity without requiring a stronger general theorem or a paper-sized follow-up.

The dated certificate retains the supplied scientific assessment, sources and limitations.
