# Scientific review: covariance tomography of paired-cluster Lipschitz potentials

## Correctness — PASS

The proof fixes the Euclidean zero-sum normalization and derives an exact chamber disintegration by global minima. Each chamber is a product of one interval and \(m-1\) independent diagonal bands, with a volume-preserving change of anchor. The moments \(\mathbb E[(U-V)^2]\) and \(\operatorname{Var}((U+V)/2)\) are computed by elementary one-variable integration, then assembled into the two covariance eigenspaces. Algebra yields a manifestly positive gap for \(0<t<1\), while direct endpoint substitution checks isotropy at \(t=1\). Exact weighted-lattice enumeration matches both eigenvalues in five rational configurations. Limits: the proof does not handle unequal pair lengths or statistical covariance-estimation error.

## Originality — PASS, with residual risk

Aliaga (arXiv:2102.01219) determines the primal extreme-point structure. Alexander–Fradelizi–García-Lirola–Zvavitch (arXiv:1911.10642) treats volume products and the equilateral case, not the complete covariance operator on two-point clusters. Related published results on shortened-pair facet enumeration and clustered subspace projections have different conclusions; neither gives uniform second moments, a bottom-eigenspace matching projector, nor the near-equilateral spectral margin. Existing clustered volume formulas and the equilateral endpoint are expressly credited. Search cannot establish absolute bibliographic uniqueness: differently named treatments of random Lipschitz potentials remain a residual risk.

## Value — PASS

Recovering a labeled metric partition from the covariance of uniformly sampled potential vectors is a natural inverse question: it uses an intrinsic, computationally observable second-order statistic of a Banach dual unit ball. The theorem supplies both the full continuous-parameter covariance and an exact separation margin, and it distinguishes the identifiable regime from the equilateral nonidentifiable endpoint. The \(1/m\) near-equilateral deformation scale and \(1/m^2\) covariance-gap scale quantify conditioning as dimension grows; this is additional geometric information not determined by volume or face counts.

## Closest literature and limitations

The complete-metric Lipschitz-polytope and molecular duality statements are covered by the cited primary literature. The volume normalization is an existing clustered-volume special case. The labeled Euclidean normalization and common pair distance are indispensable. The result does not assert basis-free metric reconstruction or finite-sample guarantees.

Self-review: passed. Independent audit: not yet performed.
