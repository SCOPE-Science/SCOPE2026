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

PASS: For n>=6, all length-three consecutive paths on C_n are geodesics, and a 3-position set is equivalently a cyclic binary word with at most two ones in each four-vertex window. Sum all windows to obtain maximum m=floor(n/2). For an optimal set, write its m positive clockwise gaps g_i, total n, and require g_i+g_{i+1}>=4. For even n, every slack g_i+g_{i+1}-4=0, giving exactly two alternating labeled patterns if n≡2 mod4 and six if n≡0. For odd n, total slack is two and solving this cyclic linear system with odd m or even m yields n(n+3)/4 when n≡1 and n(n+1)/4 when n≡3. Counts of rotation classes follow from gap stabilizers (odd n m coprime to n). Fresh direct graph-distance triples and rotation-orbit enumeration checked all n=6..18 and agree with each predicted count. Example n=9, S={0,1,4,5} is optimal but not a maximally-even set; it is not enough to enumerate only canonical even patterns.

## originality

PASS

PASS (qualified): The complete primary Cody–Moore work, arXiv:2409.05644, Theorem 4.6 proves the maximum size for cycles and displays maximally even *examples*, not the complete labeled extremizer counts or orbit formulas. The introduction’s broad language about maximally even optimizers does not supply a proof that all optimizers are of that type; n=9 provides an actual feasible nonmaximally-even optimizer. Klavžar–Rall–Yero 2020 supplies the definition, cardinality and structural membership constraints. The assessed novel result is the exact unrestricted enumeration/rotation census, not the known maximum size, window criterion, or one explicit optimizer. Classical cyclic constrained-binary-word enumerations could implicitly yield the formulas and remain a risk.

## value

PASS

PASS: Enumeration of *all* maximum-size sets of a natural known graph extremal problem is motivated beyond known size and construction. The sharp mod-four dichotomy—only 2 or 6 labeled optima in even orders versus Θ(n²) in odd orders—and the orbit classification reveal genuine geometric rigidity versus degeneracy. Explicit non-even optimal patterns demonstrate that the enumeration is not just a restatement of maximally even construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
