# Same-model review of “Sharp logarithmic support envelope for Abelian pattern Sturmian words”

## Correctness
**PASS.** The claim reduces to a direct edge count in the finite induced subgraph of the incidence forest on two copies of \(\{0,\ldots,N\}\). Each support value \(d\le N\) contributes exactly \(d+1\) different edges, while a forest on \(2N+2\) vertices has at most \(2N+1\) edges. The recurrence and logarithmic bound follow by induction and inversion. Sharpness uses the checked source proposition that \(d_{n+1}>2d_n\) implies forestness; \(d_n=2^n-1\) satisfies it exactly with one unit of slack.

## Originality
**PASS.** The closest inspected primary literature is arXiv:2609.28059v1. It proves the incidence-forest characterization and derives the weaker Sidon consequences \(\binom{h}{2}\le L-1\) and zero upper Banach density, and separately proves the sufficient condition \(d_{n+1}>2d_n\). Full-text inspection did not find the weighted prefix inequality, \(d_n\ge2^n-1\), or the exact logarithmic prefix count. Targeted searches for these equivalent formulations did not return a covering statement. The remaining risk is an equivalent elementary sum-graph observation under different terminology.

## Value
**PASS.** The statement identifies an exact, sharp sparsity law for the new extremal class: the sparse symbol can occur only logarithmically often in an initial interval, with a canonical support attaining the envelope at every scale. This is substantially stronger than the source's Sidon-scale estimate and turns the forest characterization into a quantitative extremal profile.

## Closest literature and limitations
The decisive source is Qingcheng Zeng, Yumei Xue and Cheng Zeng, arXiv:2609.28059v1, especially Theorem E, Lemma 7.5, Proposition 7.14 and Example 7.15. Kamae--Widmer--Zamboni (doi:10.1017/etds.2013.51) is foundational background. The theorem here is binary and does not extend merely from the Sidon condition or resolve the source's higher-alphabet questions.

Same-model review: passed. Independent audit: not yet performed.
