# A degree-two Möbius counterexample to induced ergodicity
## Finding
Let \(\alpha=\sqrt2-1\) and let \(R:\widehat{\mathbb C}\to\widehat{\mathbb C}\) be the Möbius rotation
\[
R(z)=e^{2\pi i\alpha}z.
\]
Let \(\Gamma\) be the holomorphic correspondence obtained by summing the graph of the identity and the graph of \(R\), and let \(\mathcal F\) be its associated set-valued map. Let \(\mu\) be normalized arclength on the unit circle \(\mathbb S^1\).

Then \(\mu\) is invariant in the normalized pullback sense
\[
\mu=\frac12\mathcal F^*\mu,
\]
and it is ergodic in the almost-invariant-set sense used for holomorphic correspondences in the cited source.

Nevertheless, for
\[
E=\left\{e^{2\pi i t}:0\le t\le \frac1{10}\right\},
\]
the induced correspondence of Definition 5.2 in arXiv:2609.29439v1 is the identity on \(E\). Consequently the normalized restriction \(\mu_E\) is not ergodic for the induced correspondence. In particular,
\[
B=\left\{e^{2\pi i t}:0\le t\le \frac1{20}\right\}
\]
is induced-almost-invariant and satisfies \(\mu_E(B)=1/2\).

Therefore Theorem 5.3 of arXiv:2609.29439v1 is false as stated, even for a degree-two holomorphic correspondence whose two components are graphs of Möbius automorphisms and for a non-atomic invariant ergodic probability measure.

## Assumptions and scope
The correspondence is
\[
\Gamma=\Gamma_{\mathrm{id}}+\Gamma_R\subset \widehat{\mathbb C}\times\widehat{\mathbb C},
\]
with both components counted with multiplicity one. Each component is an irreducible one-dimensional analytic subvariety whose two coordinate projections are surjective, so it is a holomorphic correspondence in the sense of Definition 2.1 of the source. Its generic forward and topological degrees are both two.

The ergodicity notion is exactly the source's Definition 4.6: a normalized-pullback-invariant probability measure is ergodic if every Borel set that is almost invariant under the adjoint correspondence has measure zero or one. The induced almost-invariance notion is exactly Definition 7.4.

The finding addresses only Theorem 5.3 and the reverse implication in Lemma 7.5 needed for its proof. It does not assess the source's other independent results, and it does not claim that every alternative definition of a first-return correspondence fails.

## Proof
For generic \(z\),
\[
\mathcal F(z)=\{z,Rz\},\qquad \mathcal F^\dagger(z)=\{z,R^{-1}z\}.
\]
Because normalized arclength \(\mu\) is invariant under \(R\), for every continuous \(f\),
\[
\frac12\int\left(f(z)+f(R^{-1}z)\right)\,d\mu(z)=\int f\,d\mu.
\]
Thus \(\mu=\frac12\mathcal F^*\mu\).

Let \(A\) be almost invariant for \((\mathcal F,\mu)\). By definition there is a Borel set \(A'\subseteq A\) with \(\mu(A')=\mu(A)\) and \(\mathcal F^\dagger(A')\subseteq A\). Hence \(R^{-1}(A')\subseteq A\). Since \(A'=A\) modulo \(\mu\), rotation invariance gives \(R^{-1}(A)\subseteq A\) modulo \(\mu\). The two sides have the same measure, so \(R^{-1}(A)=A\) modulo \(\mu\). The circle rotation by the irrational angle \(\alpha\) is ergodic for normalized arclength; consequently \(\mu(A)\in\{0,1\}\). Thus \(\mu\) is ergodic for the original correspondence.

Set \(\eta=1/10\). Since \(\alpha>2/5\) and \(\alpha+\eta<3/5\), the arcs \(E\) and \(R(E)\) are disjoint. For every \(z\in E\), the identity branch gives an immediate return, so \(n_E(z)=1\). At that minimum return time,
\[
\mathcal F_E(z)=\mathcal F(z)\cap E=\{z\},
\]
because \(Rz\notin E\). Hence \(\mathcal F_E\) is exactly the identity set-valued map on \(E\).

For the half-arc \(B\subset E\), take \(B'=B\) in Definition 7.4. Since the induced correspondence is the identity,
\[
\mathcal F_E^\dagger(B')=B\subseteq B,
\]
while
\[
\mu_E(B)=\frac{\mu(B)}{\mu(E)}=\frac12.
\]
Thus \(B\) is induced-almost-invariant with nontrivial measure, so \(\mu_E\) is not ergodic.

This also displays the failed implication in the second half of Lemma 7.5: induced almost invariance only controls predecessors that start in \(E\), whereas the original adjoint correspondence sees predecessors outside \(E\).

## Verification
The argument is exact and contains no numerical approximation or finite-search inference. The only dynamical input is the standard ergodicity of an irrational circle rotation. The correspondence axioms, normalized pullback invariance, original ergodicity, first-return time, induced map, and the nontrivial induced-almost-invariant set are all checked directly from the two Möbius branches.

Direct full-text inspection confirms that Theorem 5.3 asserts inheritance of ergodicity and that its proof relies on the reverse direction of Lemma 7.5. The printed proof passes from a predecessor under the original correspondence to first return time one; that passage is not valid for predecessors outside \(E\). The construction above turns that logical gap into an explicit counterexample rather than merely observing that the proof is incomplete.

## Relationship to prior work
Mana and Sridharan introduce the induced correspondence
\[
\mathcal F_E(z)=\mathcal F^{n_E(z)}(z)\cap E
\]
and state in Theorem 5.3 that ergodicity of \(\mu\) for \(\mathcal F\) implies ergodicity of \(\mu_E\) for \(\mathcal F_E\).

A public mathematical audit dated 2026-09-26 identifies the same reverse-almost-invariance step in Lemma 7.5 as invalid and classifies Theorem 5.3 as not independently verified, but it does not provide a counterexample and does not conclude that the theorem itself is false. The example above supplies that missing implication: it proves falsity, with a non-atomic ergodic measure and only two Möbius branches.

Londhe's earlier work supplies the almost-invariant-set notion of ergodicity used by the source. Classical first-return ergodicity for a single measure-preserving map does not cover this example, because the source's multivalued minimum-return rule keeps only branches present at the earliest return time; here it retains the identity branch and discards the irrational-rotation branch that enforces ergodicity of the original correspondence.

## Limitations
The result is a counterexample to the literal statement and definitions in arXiv:2609.29439v1. It does not characterize additional hypotheses under which an induced holomorphic correspondence must be ergodic. A different induced construction that retains branch histories or saturates levels before return may behave differently.

No minimality theorem is claimed for the number of branches, the choice of irrational angle, or the arc length.

## References
1. S. T. Mana and S. Sridharan, *On induced systems and ergodicity for holomorphic correspondences*, arXiv:2609.29439v1, 2026.
2. M. Londhe, *Ergodicity in the dynamics of holomorphic correspondences*, Annales Fennici Mathematici 49 (2024), 695--712, DOI: 10.54330/afm.152565.
3. MathAudit, public audit of arXiv:2609.29439v1, generated 2026-09-26, https://mathaudit.org/paper/2609.29439.
