# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

Writing
\[
g(z)=\sum_{k\ge0}\alpha_kz^k,\qquad
f(z)=\sum_{j\ge0}\beta_jz^j,
\]
the definition in arXiv:2609.19311v1 gives
\[
\widehat{L_gf}(m)=\sum_{j\ge0}\alpha_{m+j}\beta_j.
\]
Thus its matrix is exactly the Hankel matrix \((\alpha_{m+j})_{m,j\ge0}\).
This agrees with the standard analytic Hankel operator treated in the
classical Nehari--Fefferman theory and, for \(H^2\) symbols that may be
unbounded as operators, in Gérard--Pushnitski.

The explicit counterexample was checked directly. For
\[
\alpha_n=\beta_n=(n+1)^{-2/3},
\]
both input sequences are square summable, while for \(m\ge1\)
\[
\sum_{j\ge0}\alpha_{m+j}\beta_j
\ge (m+1)(m+1)^{-2/3}(2m+1)^{-2/3}
\gtrsim m^{-1/3}.
\]
The output coefficients are therefore not square summable. This disproves
the claim that \(L_g:H^2\to H^2\) is well defined for every \(g\in H^2\).

The current full text of arXiv:2609.19311v1 was inspected. Lemma 2.1 makes
the unrestricted \(H^2\to H^2\) assertion and its proof explicitly asserts
bounded \(\ell^2\)-synthesis of the backward-shift orbit. Proposition 2.2
then uses \(L_g(h)\), \(L_{P_m(u)}(h)\), and a corresponding bidisk orbit
series without domain or Bessel hypotheses. Corollary 2.3, Lemma 2.5,
Corollary 2.6, and Theorem 2.7 depend on Proposition 2.2. The review therefore
limits the impact claim to "not established by this proof"; it does not assert
that those conclusions are false.

The 2024 precursor was also checked at the relevant statement. Lemma 15
infers convergence for every \(\ell^2\) coefficient sequence merely from a
uniform bound on individual orbit vectors. Setting the inner function to
\(z\), taking the full bidisk Hardy space, and using the same scalar symbol in
one slice reproduces the explicit divergent synthesis above.

## Originality

The classical Hankel facts are excluded from the novelty claim. In
particular, Nehari's theorem and the Nehari--Fefferman BMOA formulation are
prior art, as are modern results on maximal-domain unbounded Hankel operators.

The claimed contribution is instead the specific correction of the current
preprint and its 2024 precursor: the identification of their orbit-synthesis
operator with the classical Hankel matrix, an explicit \(H^2\) input on which
the asserted everywhere-defined operator leaves \(H^2\), the exact BMOA
boundary for the one-variable synthesis statement, and the dependency
analysis showing which current projection-rigidity arguments require repair.

The current arXiv record is v1, submitted 16 September 2026. Literature
searches using the arXiv identifier, title, authors, lemma number, Hankel/BMOA
terminology, and correction/erratum terminology did not locate a public
correction of these specific statements. No source was found that would
supersede the paper-specific correction. Originality is to the best of our
knowledge.

## Value

Lemma 2.1 is the functional-analytic engine introduced immediately before
Proposition 2.2, and the paper explicitly uses it to transfer information
from one-variable backward-shift orbits into bidisk invariant subspaces.
The error is therefore structural rather than typographical.

The exact BMOA boundary is useful because it replaces a false unrestricted
statement by a standard sharp criterion. The explicit power-law
counterexample makes the failure independently checkable without relying on
subtle examples of BMOA. Tracing the dependency chain also prevents the
correction from being overstated: the record distinguishes a broken proof
from a disproof of the paper's main rigidity conclusions.

## Scope and limitations

The result does not prove Proposition 2.2 or Theorem 2.7 false, and it does
not settle the invariant subspace problem. It does not provide a full
vector-valued Bessel-orbit criterion for \(T_z^*\) on \(H^2(\mathbb D^2)\).
A repair of the bidisk proof would require additional domain or Bessel
hypotheses beyond the scalar statement recorded here.

The BMOA characterization, maximal Hankel-domain construction, and polynomial
core theorem are cited prior literature, not new contributions.

Originality is to the best of our knowledge.
