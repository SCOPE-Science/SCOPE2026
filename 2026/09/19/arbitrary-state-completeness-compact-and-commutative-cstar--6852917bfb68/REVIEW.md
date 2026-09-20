# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked separately in the compact-operator and commutative cases.

For \(A=\bigoplus^{c_0}K(H_\lambda)\), the standard-module norm is exactly
\[
\tau(a^*a)^{1/2}
=
\left(\sum_\lambda\|a_\lambda\rho_\lambda^{1/2}\|_2^2\right)^{1/2}.
\]
The closure of the image is the stated Hilbert--Schmidt direct sum because
finite spectral truncations of each \(\rho_\lambda\), followed by finite
central truncation, approximate every Hilbert--Schmidt target.  Surjectivity
holds precisely when the support projection belongs to the \(c_0\)-sum:
then the support has finitely many blocks, each finite rank, so
\(\rho^{-1/2}\) is bounded on the support.  If the support is not in the
algebra, the completion vector \(\rho^{1/2}\) cannot equal
\(a\rho^{1/2}\) for any \(a\in A\), because that would force \(a\) to act as
the identity on an infinite-rank support or on infinitely many nonzero
blocks.  This proves the necessity and sufficiency already on \(E=A\).

For a finite support projection \(p\in A\), the restriction of \(\tau\) to
the finite-dimensional algebra \(pAp\) is faithful.  Thus
\(\mathcal N_\tau^E=\{x:xp=0\}\), and the scalar norm on \(Ep\) is equivalent
to its Hilbert-module norm.  Since \(Ep\) is the range of the bounded
idempotent \(x\mapsto xp\), it is closed and complete.  This verifies the
universal Hilbert-module direction.

For \(A=C_0(X)\), the standard quotient is the image of \(C_0(X)\) in
\(L^2(\mu)\).  Finite support is plainly sufficient.  If the support is
infinite, completeness together with the ordinary Banach quotient norm
would, by the bounded inverse theorem, force a uniform inequality
\(\|f|_{\operatorname{supp}\mu}\|_\infty\le C\|f\|_2\).  Pairwise disjoint
neighborhoods of arbitrarily many support points and compactly supported
bump functions contradict that inequality.  For finite support,
finite-point interpolation makes the natural map onto the finite direct sum
of pure-state fibers, proving completeness for every Hilbert module.

The explicit \(K(\ell^2)\) counterexample was stress-tested independently:
the finite-rank projections are Cauchy in the faithful weighted state norm,
and any putative compact limit would fix every basis vector and hence equal
the noncompact identity.

No complementability, compactness, duality, or inheritance assertion used in
the proof depends on an unconditional-basis argument.

## Originality

The full text of arXiv:2609.13944v1 was inspected, especially its
Introduction and Section 2.  Its abstract defines \(\tau\) as an arbitrary
state and then states the compact-operator/commutative completeness claim
without restating purity.  The body is narrower: the introduction explicitly
states the commutative conclusion for \(\tau\in P(A)\), Proposition 2.10
assumes a pure state, and Example 2.12 assumes a pure state on a \(c_0\)-sum
of compact-operator algebras.

Searches were made for combinations and synonymous formulations involving
GNS pre-Hilbert quotients, completeness without completion, finite-rank
states, support projections, \(K(H)\), Hilbert \(C^*\)-modules, and
finite-support measures.  They recovered standard GNS material, Kadison
transitivity, and the Abedi--Moslehian paper, but no exact statement of the
two arbitrary-state classifications above.

The novelty claim excludes all standard ingredients: trace-class
representation of states on \(K(H)\), density of finite-rank operators in
Hilbert--Schmidt classes, Riesz representation, finite-point interpolation,
and pure-state completeness.  The claimed contribution is the exact
arbitrary-state boundary for the two source classes, the standard-module
completion model for compact-operator algebras, and the resulting explicit
counterexamples to the unrestricted abstract wording.

No specific inaccessible paper was identified as a likely exact antecedent.
The main residual risk is older GNS or Hilbert-module localization literature
using a different closed-range formulation.  The journal landing page was
available while one hosted PDF route was restricted; the complete arXiv v1
text was available and inspected, so this did not create a material
source-access gap.

## Value

The result resolves the natural question left by the mismatch between the
recent paper's arbitrary-state abstract wording and its pure-state proofs.
It also shows that purity is sufficient but not the true boundary: mixed
finite-rank states on compact-operator algebras, and finite atomic states in
the commutative case, still work for every Hilbert module.  Conversely,
infinite support fails already for the standard module, with an explicit
completion defect.  The criteria are sharp and reusable.

## Scope and limitations

This review does not claim a classification for general \(C^*\)-algebras or
for every individual module.  It does not claim that the body of
Abedi--Moslehian's pure-state results is false.  The correction is to the
unrestricted abstract formulation; the positive extension determines the
exact arbitrary-state boundary in the two classes treated there.

Originality is to the best of our knowledge.
