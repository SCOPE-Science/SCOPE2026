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

Conditioning on the independent storm bit gives F(x,y)=p(x+y)+(1−2p)xy. Disjoint sibling subtrees use independent primitive bits. Write c=1−2p, u=F(q,q), d=u−q=−c q(1−q), k=p+cq and v=F(u,q)=u+kd. The balanced root probability is u+2kd+cd², while the comb root is u+k(1+k)d. Their gap is d[k(1−k)+cd]=p(1−p)d. Linearity of expectation adds u−v=−kd to this gap because the count includes the root; the resulting gap is −(p²+cq)d. The factor p²+cq=(1−q)p²+q(1−p)² is positive in the open square. The formulas also give the correct edge behavior: both differences vanish at q=0,1, but at p=0,1 only the root gap need vanish. Four leaves are minimal: root splits of 1+3 and 2+2 give the two shapes, with only one shape at each smaller leaf count. A separate exact 128-assignment polynomial enumeration agreed; the frozen CHECK.py was inspected, not run. The argument is for a single binary update, not a water-balance prediction.

## originality

PASS

The inspected exact gate algebra, hydrological models and indexed reliability reversals do not state or directly imply the paired outlet/count result under independent fresh Bernoulli storm inputs. This is a bounded best-of-knowledge distinction, not a priority certificate.

## value

PASS

The smallest shape-dependent setting already gives a structural counterexample to treating outlet spill as a proxy for the number of spilling confluences. The opposite rankings persist over whole open parameter regions, with a threshold independent of headwater probability; the result is not a single favorable numerical instance. Its utility is as an exact benchmark for the stylized threshold model, not an engineering prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
