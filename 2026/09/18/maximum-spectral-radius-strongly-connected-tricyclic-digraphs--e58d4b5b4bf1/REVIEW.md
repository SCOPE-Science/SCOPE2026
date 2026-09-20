# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at each structural and analytic step.

For every strongly connected \(m\)-vertex digraph with \(m+2\) arcs, all outdegrees are at least one and
\[
\sum_v(d^+(v)-1)=2.
\]
Hence the only possible branching patterns are one outdegree-\(3\) vertex or two outdegree-\(2\) vertices. First-return excursions from the branching set are valid because every nonbranching vertex has a unique successor; a deterministic orbit avoiding the branching set would eventually close and contradict strong connectivity. Counting excursion interiors gives total excursion length at least \(m+2\).

In the one-branch case, direct Perron propagation along deterministic paths gives
\[
\sum_i z^{\ell_i}=1,\qquad z=\rho(G)^{-1}.
\]
Convex exponent transfer under the length and simplicity constraints gives the sharp monomial envelopes
\[
z+z^2+z^{m-1}
\]
with loops and
\[
2z^2+z^{m-2}
\]
without loops. Equality in both the power-sum bound and the vertex-count bound forces internally disjoint excursions covering all vertices, yielding exactly the stated directed roses.

In the two-branch case, the four first-return excursions give a \(2\times2\) irreducible matrix \(M(z)\) satisfying
\[
\rho(M(\rho(G)^{-1}))=1.
\]
There are only three endpoint patterns: one self and one cross return from each branch; one self/cross row and one double-cross row; or two double-cross rows. Each pattern is treated explicitly in RESULT.md. At the conjectured root the first-return Perron radius is strictly below one in all three patterns. The determinant inequalities in the first pattern were rechecked at both endpoint cases; the second pattern reduces to a three-monomial exponent-transfer bound; and the double-cross pattern reduces to the displayed positive identity
\[
(1-s-s^2)^2+s(1-s)^2(1+s)>0
\]
in the loopless case. Strict monotonicity of the Perron radius of \(M(z)\) then places every two-branch graph strictly below the candidate extremum.

As a finite sanity check, exhaustive enumeration of labeled strongly connected digraphs for \(m=3,4,5\) reproduces the claimed maxima in both the loop-allowed and loopless settings (with the known \(m=3\) loopless exception). This computation is supporting evidence only; the theorem is proved analytically.

## Originality

The directly motivating source is Rostislav Klech, arXiv:2609.18367v1, submitted 16 September 2026. Its Conjecture 5.15 states exactly the two maximum-spectral-radius formulas proved here: the general polynomial
\[
1-z-z^2-z^{m-1}
\]
and, for the loopless subclass, the polynomial
\[
1-2z^2-z^{m-2}.
\]
The paper proves the opposite extremum (minimum spectral radius) and does not prove this conjecture.

Searches covered exact polynomial formulas; “maximum spectral radius” together with “strongly connected digraphs” and \(m+2\) or \(n+2\) arcs; “strongly connected tricyclic digraph”; and related rose/generalized-theta/tri-ring terminology. No prior proof of the full \(m+2\)-arc maximum problem was located.

The closest older results found are:
- Lin--Shu (2012), which treats strongly connected bicyclic digraphs, the \(n+1\)-arc class;
- Shan--Wang--He (2022), which proves \(\alpha\)-spectral extremal results inside specified rose, generalized-theta and tri-ring families.

These do not cover all strongly connected \(m\)-vertex, \(m+2\)-arc digraphs. The 2026 source itself cites this literature and still states the full maximum problem as a conjecture.

Because Conjecture 5.15 is only days old, a newly posted or not-yet-indexed parallel proof is the principal residual originality risk. Originality is asserted only to the best of our knowledge.

## Value

The result closes both parts of an explicit current conjecture and supplies equality classifications. It also gives a short structural mechanism that is distinct from the source paper's eighteen-family optimization: excess outdegree determines a branching set of size at most two, and first-return Perron equations reduce the extremal problem to elementary power-sum and \(2\times2\) inequalities.

That mechanism may be reusable for strongly connected digraphs with small fixed arc excess.

## Limitations

No theorem is claimed for \(|E|-|V|\ge3\). The loopless \(m=3\) exceptional case was already settled in the motivating paper and is not a new contribution here. The finite enumeration mentioned above is not formal verification and is not needed for the proof.

The motivating conjecture is exceptionally recent, so residual uncertainty from unindexed parallel work is higher than in a mature literature.
