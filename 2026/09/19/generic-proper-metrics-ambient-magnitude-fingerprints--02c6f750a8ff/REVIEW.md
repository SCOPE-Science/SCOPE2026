# Review

## Correctness

**PASS.**

The proof has three independent ingredients whose interfaces were checked directly.

First, finite uniform distance preserves properness: if
\(D_X(d,e)\le C\), an \(e\)-closed ball of radius \(R\) is a closed subset (in the
common compatible topology) of the compact \(d\)-closed ball of radius \(R+C\).
This also shows that properness is constant on finite-\(D_X\) uniform components.

Second, Ishiki's Theorems 1.2 and 1.3 apply to a strongly zero-dimensional locally
compact Polish space: it is \(\sigma\)-compact and has cardinality at most the
continuum. The approximation can therefore be made with arbitrarily small finite
\(D_X\), so the approximating algebraically independent metric remains proper.

Third, algebraic independence makes the distance map on unordered pairs injective.
That injectivity forces every distance-preserving map from a subset with at least three
points to fix every point, by intersecting two preserved unordered pairs. For two-point
sets it forces the image pair to be the same pair. O'Hara's Theorem 2.4(2), also cited
explicitly by Ishiki's Remark 3.4, recovers any rationally independent finite metric
space from its magnitude function; algebraic independence is stronger than rational
linear independence. The ambient rigidity argument then upgrades abstract
reconstruction to equality of subsets.

The singleton exception was checked separately: all singleton magnitude functions equal
\(1\). The strict-triangle and four-point-tree consequences are direct forbidden linear
relations and are not used in the main theorem.

## Originality

**PASS, to the best of our knowledge.**

Ishiki's inspected preprint proves uniform density and \(G_\delta\)-genericity of
algebraically independent metrics in the full compatible-metric space, and separately
proves a relative \(G_\delta\) theorem for rigid proper metrics. It does not state that
algebraically independent *proper* metrics are dense \(G_\delta\) among proper metrics,
nor the finite-\(D_X\) properness transfer used to obtain that conclusion.

Ishiki's Remark 3.4 states that finite subspaces are determined by magnitude up to
isometry, using O'Hara's theorem. The inspected O'Hara paper concerns abstract finite
metric spaces. Neither inspected source states the stronger ambient conclusion that, for
one algebraically independent metric on \(X\), the magnitude function is injective on
the collection of all finite ambient subsets of cardinality at least two, or the
distance-preserving-subspace rigidity that yields it.

Targeted searches using combinations of “algebraically independent distances”, “proper
compatible metrics”, “magnitude function”, “ambient reconstruction”, “finite subsets”,
and “strongly rigid” did not locate a matching theorem. Current SCOPE records were also
searched by the source paper, object, and claim family without a collision.

No inaccessible paper was identified as a specific likely source of prior coverage.
The main residual originality risk is instead the recency of Ishiki's preprint: the
properness transfer and ambient-magnitude consequence are short deductions and could
appear in a later revision or an unindexed parallel note.

## Value

**PASS.**

The proper-metric statement places Ishiki's stronger algebraic genericity inside the
natural class used for locally compact metric geometry, rather than only in the full
space of compatible metrics. The ambient hereditary rigidity conclusion is stronger
than triviality of the global self-isometry group: no subset of three or more points has
a second isometric placement anywhere in the same ambient space. Combining this with
magnitude reconstruction turns a scalar-valued metric invariant into an injective
fingerprint for every nontrivial finite point cloud simultaneously. The result is short,
but it links generic metric construction, proper geometry, and magnitude reconstruction
in a form not stated in the inspected sources.

## Limitations and residual risk

- Strong zero-dimensionality is essential to the available algebraically independent
  approximation theorem.
- No quantitative stability or conditioning for magnitude reconstruction is obtained.
- Singleton point clouds remain indistinguishable by magnitude.
- The main conclusions are structural consequences of recent metric-genericity and
  finite-magnitude theorems rather than a new construction of algebraically independent
  metrics.
- The motivating preprint is extremely recent, so later revisions or unindexed parallel
  observations remain a genuine originality risk.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
