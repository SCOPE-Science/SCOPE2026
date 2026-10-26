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

# Verification details

Run `python3 verify.py` using a standard Python 3 interpreter; the script has no third-party dependencies. Its stdout should reproduce the accompanying `verification_output.txt` verbatim and end in `VERIFY_OK`.

For each integer \(3\le n\le7\), the verifier constructs the adjacency masks of \(L(K_n)\) directly from edge intersections in \(K_n\). It then enumerates all \(2^{\binom n2}\) initial subsets and iterates the original closed-neighborhood domination and unique-neighbor forcing rules until convergence. It independently compares success against the isolated-original-vertex criterion. It tests minimality by deleting each selected graph vertex, compares that to the star-forest/matching condition, counts the exact full polynomial and minimum coefficient, and identifies inclusion-maximal failures by trying each possible single addition. The total number of tested initial subsets is \(2{,}131{,}016\).

The numerical polynomial is independently reconstructed by inclusion–exclusion on isolated original vertices. Checks of polynomial coefficients and minimum-set counts continue through \(n=14\) with exact integer arithmetic, without exhaustive enumeration at those larger orders.

Recorded values: for \(n=5\), the minimum is \(2\) with \(45\) attaining sets; for \(n=6\), \(45\) minimum sets of size \(2\) and \(60\) other inclusion-minimal sets of size \(3\); for \(n=7\), \(735\) minimum sets of size \(3\) and \(105\) inclusion-minimal sets of size \(4\). These counts agree with the independently checked formulas.

**Limits.** Finite exhaustive checks do not establish correctness for all \(n\), nor do they settle literature novelty. The proof in `RESULT.md` supplies the infinite argument. No independent audit has been performed.
