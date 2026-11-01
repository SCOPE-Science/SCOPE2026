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
# Reproduction and scope of verification

Run `python3 verify.py` from the same directory as this document. Only Python's standard library is required. The code computes the normalized expected total interface length via (i) an exact central-binomial rational expression and (ii) a separately evaluated beta integral using log-gamma values, and checks their agreement for multiple site counts. It verifies chord-square moment identities using exact `fractions.Fraction` arithmetic and checks the asymptotic moment predictions at a large sample count.

An independently constructed numerical geometry algorithm draws independent uniform sphere points, parameterizes every pair-bisector great circle, clips it by the halfspaces of all other generating points, and integrates the surviving arcs exactly in that angular parameter. It computes simulated averages of total length and the arclength-weighted common height and generator squared chord, using a fixed seed. This checks the original geometric definitions rather than sampling from the predicted beta distributions. Test site counts and replications: \((2,1600)\), \((3,600)\), \((4,1500)\), and \((6,1200)\).

The executed checker reported:

```
n=2 mean_total_length=6.28318531 theory=6.28318531 length_weighted_U=0.5000000 theory=0.5000000 length_weighted_Q=2.0365716 theory=2.0000000
n=3 mean_total_length=9.42477796 theory=9.42477796 length_weighted_U=0.6254366 theory=0.6250000 length_weighted_Q=2.0000364 theory=2.0000000
n=4 mean_total_length=11.78364538 theory=11.78097245 length_weighted_U=0.7011310 theory=0.7000000 length_weighted_Q=1.8857294 theory=1.8666667
n=6 mean_total_length=15.44230051 theory=15.46252634 length_weighted_U=0.7857325 theory=0.7857143 length_weighted_Q=1.5756772 theory=1.5714286
ALL_EXACT_MOMENT_AND_GEOMETRIC_CHECKS_PASSED
```

These finite samples are consistency tests only. They cannot prove the beta factorization for every sample count, the large-sample limiting law, or historical priority. Those claims rest on the mathematical argument and literature comparison in `RESULT.md` and `REVIEW.md`. No independent audit has been performed.
