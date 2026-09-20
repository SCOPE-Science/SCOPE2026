# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

The proof was checked at the three points where hidden geometric assumptions are most likely to enter.

1. **Alternating iteration.** Segal's Lemma 7 applies to \(F_K=F_L\) and forces alternating signs of \(h_K-h_L\) together with strict increase of the common \(F\). The added estimate
   \[
   F_A(v)-F_A(u)\ge \rho_A(v)\bigl(1-\langle u,v\rangle\bigr)
   \]
   follows directly from \(h_A(v)\ge\rho_A(v)\), \(\rho_A(u)\le h_A(u)\), and \(h_A(u)=\rho_A(v)\langle u,v\rangle\). It therefore forces consecutive angular gaps to tend to zero.

2. **Second-jet calculation.** For \(x=h n+h't\), radial angle \(\alpha=\beta+\arctan(h'/h)\), and \(q=1/\rho\), differentiation at a radial-normal fixed direction gives
   \[
   \alpha'=\frac{h+h''}{h},\qquad
   q''=-\frac{h''}{h(h+h'')}.
   \]
   Hence
   \[
   F''=h''+\frac{h''}{h(h+h'')},
   \]
   which is strictly increasing in \(h''\) when \(h>0\) and \(h+h''>0\). This forces equality of the curvature radii of the two bodies at the limiting contact.

3. **First unequal jet under polarity.** The exact variational formula
   \[
   h_{K^\circ}(\alpha)=\max_\beta\frac{\cos(\alpha-\beta)}{h_K(\beta)}
   \]
   has a unique nondegenerate maximizer in the \(C^\infty_+\) class. If the first support-function difference occurs in order \(m\ge3\), the maximizing normals differ by \(O(\alpha^{m-1})\); stationarity makes the induced value error \(O(\alpha^{2m-2})=o(\alpha^m)\). The direct reciprocal-support term therefore reverses the leading coefficient with the strictly negative factor
   \[
   -\frac{a^{m-2}}{R^m},
   \]
   contradicting \(h_K-h_L=h_{K^\circ}-h_{L^\circ}\).

The final analytic step uses only the identity theorem for real-analytic functions on the connected circle.

No numerical or computer-assisted verification is needed.

## Originality

**PASS, to the best of our knowledge.**

The motivating source, arXiv:2609.12685 (submitted September 11, 2026), proves injectivity of \(F_K=h_K-1/\rho_K\) for polytopes and non-injectivity for general convex bodies. Its planar counterexample is an infinite polygon. The source text does not discuss a smooth, real-analytic, strictly convex, or regularity-based rigidity theorem.

Targeted searches were made for the exact polar-sum equation and for combinations of Milman's question with smoothness, strict convexity, real analyticity, support functions, radial functions, and translated/self-dual formulations. No prior result matching the analytic planar rigidity theorem or the infinite-order-contact obstruction was found. The current SCOPE repository was also searched by the motivating author, equation family, and self-duality terminology, with no overlapping record found.

Residual originality risk remains because the motivating preprint is only days old and concurrent or not-yet-indexed work may exist.

## Value

**PASS.**

The result fills a natural regularity gap between Segal's positive polytope theorem and general negative examples. The flat-contact obstruction is stronger than the analytic corollary: it says that a positively curved smooth counterexample, if one exists, cannot emerge through any finite-order mismatch of support-function jets. This gives a concrete structural constraint on future constructions and shows that the known nonsmooth mechanism is not merely an artifact of the particular example.

## Scope and limitations

The result is restricted to dimension two and to positive curvature. It neither rules out \(C^\infty_+\) counterexamples with flat contact nor treats analytic bodies with vanishing curvature. It does not settle analogous analytic rigidity in higher dimensions.

## Sources inspected

- Alex Segal, *Self-dual sets up to a translation: a negative answer to Milman's question*, arXiv:2609.12685. The theorem statements, the support/radial functional reduction, Lemmas 6–7, the planar infinite-polygon construction, and the higher-dimensional revolution construction were inspected.
- Public literature searches for exact and synonymous formulations described above.
- The current public SCOPE archive for internal overlap.

No specifically identified inaccessible paper was found whose title or available metadata closely suggests that it contains this result.
