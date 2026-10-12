# Self-review

## Correctness — PASS

The finite covariance follows from conditioning a labelled vertex to be isolated. The forbidden arc has length \(2r\); the remaining \(n-1\) points are independent uniform points on its complementary arc. Pair distances cannot connect across the removed arc, so the conditional edge probability is exactly \(1-((L-r)_+/L)^2\). Expanding the exchangeable indicator–edge covariance gives the two polynomial branches. The quadratic's roots and the second branch's linear zero prove the sharp \(n=6\) onset and both sign reversals; the sparse scaling follows by an elementary exponential limit. An exact-rational checker evaluated 15,252 identities, and direct-coordinate Monte Carlo provided five independent numerical checks. The proof is analytic; the computer experiments are not an infinite certificate.

## Originality — PASS, with risk

The nearest inspected works are Penrose and Peres (2010), Penrose (2015), Doku-Amponsah (2016), and Wilsher–Dettmann–Ganesh (2022). They discuss isolated vertices and edges separately, joint large deviations of aggregate empirical measures, or isolation counts in a Poisson soft geometric circle. Inspection of their relevant full-text theorem statements and proofs did not reveal the two sign thresholds or a finite hard-circle isolated-count/edge-count covariance that directly yields them. The known general conditioning and Palm techniques remain plausible routes to a shorter derivation; an exhaustive priority assertion is not justified. The broad Penrose (2003) monograph was not inspected in full, leaving residual indirect-coverage risk.

## Value — PASS

Isolated vertices and edge count are central, jointly observed descriptors of geometric networks. In a graph with independent edges they are always negatively covariant, but geometric conditioning creates a competing density effect. The exact result establishes that a positive interval first becomes possible for six vertices, locates both endpoints for every larger sample, and identifies a distinct sign boundary \(c=4/3\) when \(r=c/n\). The existence of two reversals and a sharp minimal sample size is not a routine reparametrization or arbitrary slice.

## Limits

Fixed \(n\), periodic unit circle, iid uniform positions, deterministic cutoff edges. The result is about unnormalized covariance, not Pearson correlation. Historical uniqueness remains subject to possible general mixed-moment identities in sources not fully available.

Self-review: passed. Independent audit: not yet performed.
