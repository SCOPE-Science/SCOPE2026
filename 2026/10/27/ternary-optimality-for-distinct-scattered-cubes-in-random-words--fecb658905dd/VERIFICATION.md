---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Greedy matching is equivalent to subsequence occurrence: each successive earliest match is no later than the corresponding position in any embedding. Independence after each match gives independent geometric waits including the successful trial; for u^3 their product weights are the cubes of the root-letter weights. The root is uniquely recovered from the first third of the cube. Summing by root length, then by n≥the waiting time, gives the stated OGF as a formal series, with only finitely many contributing roots per coefficient. For positive q≥2 the series T has positive coefficients in all degrees ≥3, is analytic on the closed unit disk, increases from 0 to q on [0,1], and has T'(r)>0. Degrees 3 and 4 force strict triangle inequality at every nonreal or negative point on |z|=r, so the residue of the single simple pole gives exactly the stated constant. For optimization on each closed simplex, stationarity in a positive coordinate pair x,y gives x=y or xy=s² for f_s(x)=(x/(x+s))³. In the unequal case x<s<y, direct differentiation gives f''(x)/(-f''(y))=y/x>1, contradicting maximality along the transfer; the argument also applies in the relative interior of any maximizing face. Thus maxima have equal positive masses. At s*=(∛3−1)/3 the function m/(1+s*m)³ increases to its real maximum in (3,4) and then decreases. The exact rational bounds ∛3>1.442 and ∛4<1.588 give (∛4−1)/4<s*, so m=4 is strictly worse than m=3, which gives one. This bounds T((1+s*)^(-1)) and proves equality only at the strictly positive uniform ternary source. Substitution gives rT'(r)=9/(3−2r), yielding the stated ternary prefactor. Continuity allows near-ternary bias on larger alphabets but not equality. Independent exact coefficient replay enumerated all distinct subsequences then filtered cubes for p=(3/7,4/7), n≤9 and p=(1/6,1/3,1/2), n≤7 (/workspace/replay/independent_checks.py, cubes). The replay does not establish the asymptotics or global optimization.

## originality

PASS

The generic waiting-time encoding of distinct targets, simple-pole analysis, and related source optimizations for different structured languages are not new here. The inspected analogues do not supply the cube-language mean together with its sharp all-source support and equality theorem. The strongest surviving content is the unique ternary optimum and its exact exponential constant for this language.

## value

PASS

Distinct repeated subsequences form a natural language. The mean rate is sensitive to the actual source law, and deciding both the best alphabet size and bias across all finite alphabets is appreciably more informative than a fixed-source calculation. The strict uniform ternary equality case is the structural contribution. It is not a claim about finite-length optimality, typical words, or higher powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
