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

The frozen Finding at lines 14–19 is false as printed: for C_3, k=3 the permutations of (1,2,2) are precisely the three minimum-weight (weight 5) functions, all of support 3, contrary to u^3. The frozen count sentence, proof at line 39, and verifier's support_formula already give the correct n·u^n branch for odd n and odd k. The full corrected RESULT.md is under /workspace/repairs/3/, with the original preserved. To verify the repaired claim, join labels at cyclic difference 2. This is one length-n cycle for odd n or two independent length-n/2 chains for even n, counting the repeated constraint harmlessly at n=4. Summing constraints gives the lower bound mk/2 per component. With even mk it is attained exactly by all-tight alternating pairs (k+1 choices on even m; only k/2 throughout for odd m). With odd mk, the rounded bound is attained by putting the high label (k+1)/2 at both ends of any one edge and alternating (k±1)/2 along the other edges; conversely the total slack is exactly one, forcing one such choice. Each choice is distinct. Thus for 4|n each component contributes 2u^(n/4)+(k−1)u^(n/2) and the factors multiply; other cases have full support for k≥2, with multiplicities n for odd-odd, (n/2)^2 for n≡2 mod 4 and odd k, and one otherwise. The integer lower bound and all minima establish the weight and support transition. Independently enumerated six cases of the original neighbor inequalities, including the C_3 witness and n=4,6,8; replay python3 /tmp/opencode/nov02-independent-checks.py 3. The attached verifier was inspected, not executed; its 18 and 112-case results are recorded finite checks and not proof of the general result.

## originality

PASS

The corrected claim is the complete labelled all-optima support polynomial and zero-support phase distinction, not the already known optimum weight or the binary census. The directly compared same-day path theorem uses different endpoint constraints, and the public k=1 sequence is not the multilevel support enumerator. No equivalent complete cycle census was established in the evidence reviewed, with the close 2018 source-access risk below.

## value

PASS

The corrected theorem gives a complete, labelled support census over all n≥3, k≥2 for a standard optimum problem. The exact criterion 4|n for any sparse optimum, the four smallest-support extremizers in that regime, and multiplicities of all support sizes distinguish structurally different optimizers despite equal optimum weights. This is more informative than the already known weights or isolated small enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
