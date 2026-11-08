---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The source’s finite conditional last-preference probability law is explicitly credited to Durmić et al. The positive coefficients a_(n,s) are symmetric, sum 2/(n+1), and have interior n^(−5/2) density proportional to [y(1−y)]^(−3/2), while their endpoint mass gives one half atom at each boundary after rescaling. The discrete increment D_(n,s+1)−D_(n,s)=a_(n,s)+a_(n,s+1), with midpoint zero, gives n^(3/2)D→4(2y−1)/sqrt(2π y(1−y)). The uniform endpoint bound |D|≤C/[n sqrt(min(s+1,n−s))] controls absolute mass in shrinking collars. Therefore the signed n-scaled law converges with norm to (δ0+δ1)/2+[-1+4λ(1−2x)/sqrt(2π x(1−x))]dx. The sign-change integral is sqrt(1+32λ²/π), yielding n TV→(1+sqrt(1+32λ²/π))/2 for fixed λ. Independent log-gamma finite evaluations at λ=0,1/4,1 and n=250,1000,10000 approach the predicted constants monotonically; numerical agreement alone was not used as an infinite-limit proof.

## originality

PASS

Best-of-knowledge comparison of statements rather than titles: close primary results supply tools, partial parameter regimes or weaker scalar/qualitative conclusions but do not directly cover this particular exact claim. Inaccessible plausible broader results are named and retained as specific historical-priority risks, not treated as automatic failure.

## value

PASS

The prior fixed-bias asymptotics leave a natural boundary layer around unbiased parking at p=1/2. The explicit universal critical scaling λ=(p−1/2)sqrt(n), its nontrivial nonlinear total-variation coefficient, and a decomposition into universal boundary atoms plus bias-dependent bulk density resolve that precise missing transition rather than offering a routine tiny correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
