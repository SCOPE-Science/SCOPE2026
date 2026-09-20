# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The central point is that the localization hypotheses themselves force finite \(t\)-depth:
\[
\bigcap_{n\ge0}t^nR=0.
\]
If a nonzero \(x\) were infinitely divisible by \(t\), localization of \(x^{-1}\) and one extra power of \(t\) would imply \(1\in tR\), contradicting the standing hypothesis. This makes the leading residue \(\rho_t(x)\) well defined for every nonzero \(x\in E\).

The positivity criterion follows directly from the defining form
\[
t^{-n}(a+tr),\qquad a\in F_{>0},
\]
because \(F\cap tR=0\). The converse is immediate by lifting a positive residue representative.

The most delicate claim is the no-minimal-upper-bound statement. After translation and multiplication by a positive power of \(t\), an incomparable pair reduces to \(\{0,x\}\) with \(x\in R\setminus tR\) and residue outside \(F\). Any common upper bound \(u\) cannot lie in \(R\), because the residues of \(u\) and \(u-x\) would then both lie in \(F\). Thus \(u\) has positive level \(n\ge1\). For any \(0<\lambda<1\) in \(F\),
\[
\lambda u-x
=
t^{-n}\!\left(\lambda a+t(\lambda r-t^{n-1}x)\right)
\]
is again positive, while \((1-\lambda)u>0\). Hence \(\lambda u\) is a strictly smaller common upper bound. This works for every common upper bound. Negation gives the dual lower-bound statement.

The equivalence with \(R/tR=F\) then follows from the leading-residue criterion. In the total case, every element outside \(tR\) is a unit by factoring it as
\[
a(1+tr),
\]
and finite \(t\)-depth writes every nonzero element as a unit times a power of \(t\). This proves the DVR characterization.

The finite-extension corollary uses the standard equality
\[
[L:K]=\sum e_if_i
\]
for the integral closure of a DVR in a finite separable extension. Ordered fields have characteristic zero, so separability is automatic. Totality forces one prime with \(e=f=1\), hence degree one.

Edge cases were checked explicitly: \(R=F[t]_{(t)}\) gives the expected total order; \(R=F(i)[t]_{(t)}\) with coefficient field \(F\) gives a nonlattice order, and the residue of \(i\) is a no-join witness.

## Originality

**PASS, to the best of our knowledge.**

The relevant portions of arXiv:2609.20494v1 were inspected. Theorem 2.2 establishes the localization cone, directedness, and positive inverses; the following remark explicitly notes that \(R/tR\) need not be a field; Proposition 2.7 proves a specific no-least-upper-bound statement for \(0\) and \(i\) in the complex-field specialization. The paper does not state the general leading-residue comparison law, the assertion that every incomparable pair lacks minimal upper bounds and maximal lower bounds, the equivalence with \(R/tR=F\), or the DVR characterization.

The classical implication that a division-closed lattice-ordered field is totally ordered is prior art and is not part of the originality claim. Yang's 2005/2006 result and Ma–McGovern's 2017 treatment were checked at the theorem/abstract level and explicitly separated from the new statement.

Targeted literature searches using the localization formula, residue quotient, directed partial orders, lattice orders, and valuation terminology did not locate the exact residue/join criterion. Classical Baer–Krull theory and valuation-compatible orderings are a substantial adjacent body of prior art, and older ordered-field literature may contain an equivalent statement in different language. That is the principal residual originality risk. Because the proof becomes short after identifying the first-residue mechanism, independent rediscovery or an implicit folklore version remains plausible.

The finite-algebraic-extension corollary combines the new criterion with the standard ramification degree formula; the degree formula itself is not new.

## Value

**PASS.**

The result gives an exact boundary for when the recent localization construction produces a total/lattice order and when it produces a genuinely partial nonlattice order. It strengthens a single nonlattice witness to a complete pairwise statement: every incomparable pair has common bounds, by directedness, but no minimal upper bound and no maximal lower bound.

The DVR characterization gives a familiar algebraic interpretation of the boundary. The consequences show that the universal construction of arXiv:2609.20494v1 is automatically nonlattice in transcendence degree at least two, provide real no-join witnesses in the complex-field family, and rule out lattice orders from every nontrivial finite algebraic extension of an ordered rational function field within this construction.

## Limitations

The result concerns this specific localization-cone construction, not arbitrary directed partial orders. It does not settle whether \(\mathbb C\) admits some other lattice order.

The literature search cannot exclude an older equivalent formulation, especially in valuation-theoretic or lattice-ordered-field terminology.

No independent validation or independent audit is claimed.
