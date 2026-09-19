# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof was checked at the level of the exact hypotheses used.

The essential analytic input is equation (31) in S. Bera, *New York J.
Math.* 32 (2026), 99--117.  For a two-variable polynomial \(p\), it gives
\[
\|z_1p\|^2-\|p\|^2
=
\int_{\overline{\mathbb D}\times\mathbb T}|p(a,\zeta)|^2\,
d\rho^{(1)}(a)\,dm(\zeta),
\]
and symmetrically for the second coordinate.  This identity is stronger
than a monomial-only calculation and supplies a positive quadratic form on
the full polynomial subspace.

Because the coordinate multipliers are bounded, that quadratic form is
bounded by \(\|M_i^*M_i-I\|\|p\|^2\).  Polynomial density therefore gives a
bounded \(L^2\) trace map \(\Gamma_i\), and the polynomial intertwining
\(\Gamma_iM_i=M_a\Gamma_i\) passes to all vectors by continuity.  This
avoids assuming pointwise boundary values for arbitrary vectors.

For \(h\in H\), the identity
\[
\|M_i^{n+1}h\|^2-\|M_i^nh\|^2
=
\|\Gamma_iM_i^nh\|_2^2
=
\int |a|^{2n}\,d\eta_{i,h}(a)
\]
was checked directly.  Hence \(S_*\eta_{i,h}\) is the Hausdorff representing
measure of the forward difference.  The one-variable relation
\[
\mu=\mu(\{1\})\delta_1+(1-t)\nu
\]
on the level of representing measure, drift, and Lévy measure gives the
claimed \((1-t)^{-1}\) formula on \([0,1)\).  No division by \(1-t\) is made
at \(t=1\).

The joint step uses Theorem 2.4 of Bera--Sequeira
(arXiv:2609.20346v1), which states for every vector that a completely
hyperexpansive tuple with pairwise zero defect has Lévy measure equal to the
sum of its coordinate face measures.  Their paper also records that the
bidisc multiplication pair has zero defect.  Thus the coordinate formulas
apply to the joint measure without an additional inheritance assumption.

The tomography argument was checked separately.  From the probes
\(1,1+z_i^k,1-i z_i^k\), the identities
\[
|1+a^k|^2=1+|a|^{2k}+2\operatorname{Re}a^k,\qquad
|1-i a^k|^2=1+|a|^{2k}+2\operatorname{Im}a^k
\]
recover the complex measures \(S_*(a^k\rho)\) on \(t<1\).
Disintegration over \(t=|a|^2\) then recovers every angular Fourier
coefficient on almost every nonzero radial fiber.  The zero fiber is a
single point.  On the boundary, the same probe identities applied to the
drift recover all Fourier coefficients of the boundary measure.  Standard
Fourier uniqueness completes the reconstruction.

The explicit comparison \(\delta_r\) versus \(\delta_{-r}\) was also
checked: the \(h=1\) radial pushforwards coincide, while for \(h=1+z_1\)
the Lévy atom weights are respectively
\((1+r)^2/(1-r^2)\) and \((1-r)^2/(1-r^2)\).

No numerical computation is needed for the proof.

## Originality

The starting paper, Bera--Sequeira, arXiv:2609.20346v1, was inspected at
the theorem and proof level.  Question 1.3 explicitly asks how the Lévy
measure for arbitrary \(h\) is related to the defining measures.  Theorem
1.4 and its proof specialize the explicit defining-measure computation to
\(h=1\).  The same paper's Theorem 2.4 is an abstract all-vector
decomposition theorem, but it does not identify the coordinate measures in
terms of \(\rho^{(1)},\rho^{(2)}\) for general \(h\).

The 2026 Bera model paper was inspected around its polynomial norm
identity, especially equation (31).  It supplies the defect-energy formula
used here, but does not formulate the arbitrary-vector Lévy identification,
the trace-map extension, or the tomography statement.  The 2025
Bera--Chavan--Ghara paper supplies the unit-circle predecessor of the
Dirichlet norm mechanism.

Searches using the current arXiv identifier and title, arbitrary-vector
Lévy terminology, Dirichlet-type defect/representing-measure terminology,
and equivalent measure-reconstruction language found no public statement
of the all-vector bidisc formula or the countable tomography result.

The following older sources remain the main residual prior-art risk:

- A. Aleman, *The Multiplication Operator on Hilbert Spaces of Analytic
  Functions*, Habilitationsschrift, Hagen (1993), Chapter IV.  The source
  is cited by the current literature for the one-variable completely
  hyperexpansive model, but its full text was not inspected here.  It could
  contain an operator-valued or trace formulation equivalent to the
  one-variable part of the construction.
- A. Athavale and V. M. Sholapurkar, *Completely hyperexpansive operator
  tuples*, Positivity 3 (1999), 245--257,
  DOI 10.1023/A:1009719803199.  Its public abstract and the way it is cited
  in the current paper were inspected, but not a complete searchable full
  text.  It is the likeliest older source for an abstract vectorwise
  Lévy--Khinchin representation.

These risks do not supply concrete evidence of prior coverage of the
specific bidisc trace formula or tomography theorem.  The novelty claim is
therefore deliberately restricted: the known defect identity, abstract
zero-defect decomposition, Hausdorff representation, disintegration, and
Fourier uniqueness are not claimed as new.

## Value

The result answers an explicit arbitrary-vector question in a new
preprint, rather than merely varying the \(h=1\) formula.  It also identifies
a structural information boundary invisible at \(h=1\): radialization loses
angular data, while a countable set of elementary probes recovers the full
defining measures.  The split between interior information in the Lévy
measure and boundary information in the drift is exact and reusable in
related operator-model questions.

## Limitations

The all-vector formula uses canonical \(L^2\) traces defined by completion,
not asserted pointwise traces.  The tomography theorem needs countably many
probes.  Boundary mass cannot be recovered from polynomial Lévy measures
without the drift.  Higher-dimensional polydiscs and nonzero pair-defect
tuples are not covered.
