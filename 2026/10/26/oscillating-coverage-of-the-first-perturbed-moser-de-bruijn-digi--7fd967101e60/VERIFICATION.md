---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The four one-digit contributions 0,1,6,7 have distinct residues mod4; comparing least differing base-four digit proves injectivity of (x,y)→x+6y for all finite M digit strings. The complete three-state carry map ((0,0,1,1),(2,0,0,1),(2,2,0,0)) follows from per-digit equation ε+6η+c=d+4c_next. Exactly two transitions to final carry0 from each state yields a_L=2·4^{L-1}; b_{L+1}=2a_L+b_L and b_1=2 yields b_L=(4^L+2)/3. Counting leading digit0/1 yields F(2·4^L)=2a_L+b_L. The subsequential normalized counts tend to distinct 1/2 and 2/3; no claim that these are global liminf/sup. Independent explicit sums n<3000 confirmed uniqueness, carry acceptance and both formulas for L=1..5; source verifier extends finite checks to 131072. Infinite proof rests on exact automaton recurrences.

## originality

PASS

PASS, qualified: classical unique M+2M=N0 and de Bruijn direct integer decompositions are acknowledged. De Bruijn 1964 considers signed complete decompositions of integers rather than these two positive M+6M cutoff counts; Nathanson treats the coefficient-two sparse basis. Peter 2003 automatic-sequence density theorems and Heuberger–Kropf–Prodinger 2015 transducers offer broader methods, possibly implying eventual log-periodicity but no inspected exact M+6M counts. Resultary search found no equivalent. Some scanned de Bruijn pages and full Peter text were inaccessible/only partially inspected, so do not assert whole-document not-covering solely on fragments.

## value

PASS

PASS: M+2M is the canonical perfect-coverage digital basis. c=6 is the first coefficient greater than two preserving local injectivity of all four digit-pair residues; its explicit failure of natural density is a meaningful qualitative boundary. The two infinite exact counting sequences show how a natural sparse additive sumset can oscillate between 1/2 and 2/3 cutoff proportions despite unique representations. This is neither a random finite cutoff nor known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
