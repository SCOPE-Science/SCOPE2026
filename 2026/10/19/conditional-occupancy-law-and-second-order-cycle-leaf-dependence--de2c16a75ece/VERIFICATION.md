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

# Mathematical verification

The theorem concerns simple connected labeled unicyclic graphs, one fixed sampling law for each integer order \(n\ge3\). The primary all-order certificate is the bijection between a chosen unique cycle with an attached fixed-root forest, together with deletion of any specified collection of off-cycle leaves. This proves all conditional joint events of the indicator family and hence its equivalence to empty-box indicators with \(h-1\) balls among \(n\) boxes, where \(h=n-k\). It determines the conditional factorial moments, probability generating function, and finite regression without assuming independence of actual graph edges.

## Executed reproducibility check

Using only Python's standard library, the companion `verify_unicyclic.py` was executed. It independently enumerated the connected unicyclic graphs on \(3\), \(4\), \(5\), \(6\), and \(7\) labeled vertices, obtaining exactly 1, 15, 222, 3,660, and 68,295 such graphs. It reconstructed the unique cycle length by leaf peeling, computed degree-one counts, and compared the entire joint histogram with the inclusion-exclusion probabilities derived from empty-box occupancy. It checked 86 exact joint-count, moment, and strict-regression assertions; all passed. All comparison arithmetic is integral or rational.

## Infinite-order and limit checks

The unrestricted finite identities follow from the forest-counting proof, not from enumerating finitely many graph orders. The asymptotic statements use the exact representation of \(n-K_n\) as a right-truncated Poisson variable, a uniform second-order expansion of the conditional leaf mean for \(k=O(\sqrt n)\), and a two-dimensional lattice local central limit argument for a Poissonized occupancy model conditioned on its ball total. The limiting conditional variance is \(e^{-1}-2e^{-2}>0\); the limiting covariance constant is \(-\sqrt{2/\pi}/(2e)\). The conditional normal limit establishes joint weak convergence with independent components, not finite-order independence. No external independent audit or historical-priority certification has been performed.
