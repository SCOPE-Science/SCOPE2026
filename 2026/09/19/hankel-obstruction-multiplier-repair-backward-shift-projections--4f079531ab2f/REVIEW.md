# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The counterexample is direct. For \(g=f=\sum_{n\ge0}(n+1)^{-3/4}z^n\), both inputs lie in \(H^2\), each formal output coefficient is finite, and the lower bound
\[
c_\ell\ge 2^{-3/4}(\ell+1)^{-1/2}
\]
forces the output outside \(H^2\). The polynomial truncation estimate independently shows operator norms growing at least like \(N^{1/4}\).

The boundedness threshold is the classical Nehari theorem applied to the Hankel matrix \((\alpha_{j+k})\), equivalently to the shifted analytic symbol \(zg\). The bounded multiplier identity \(L_gf=M_{f^\sharp}^*g\) was checked coefficientwise.

The projection-rigidity proof was stress-tested at the possible endpoint \(V_\xi=H^2\), where inclusion is automatic. In the proper case, Beurling gives \(V_\xi=K_\theta=\ker M_\theta^*\). Minimality first makes every nonzero coefficient map injective. Applying \(M_\theta^*\otimes I\) then produces a nonzero vector in the kernel of another nonzero coefficient map whenever two shadow spaces fail inclusion, a contradiction. No complementability assertion is used.

## Originality

PASS, to the best of our knowledge.

The primary source arXiv:2609.19311v1 was inspected at Lemma 2.1, Proposition 2.2, Corollary 2.3, Lemmas 2.4--2.5, Corollary 2.6, and Theorem 2.7. Its Lemma 2.1 asserts the all-\(H^2\) synthesis that the explicit example disproves. The source does not identify the Hankel/BMOA obstruction and does not give the multiplier proof above.

Searches covered the source title and arXiv identifier together with `BMOA`, `Hankel`, `correction`, `minimal invariant subspace`, `backward shift`, `infinite multiplicity`, `vector-valued Hardy space`, `coefficient maps`, and `model space`. No published correction or statement matching the arbitrary-multiplicity common-shadow theorem was found.

Classical Nehari theory and Beurling model-space theory are prior art and are explicitly treated as such. Older vector-valued Hardy/model-space literature is broad, so there is residual risk that the common-shadow lemma exists implicitly or under different terminology. That risk does not affect the explicit counterexample to the 2026 Lemma 2.1.

The related arXiv:2309.03427 was also inspected because the 2026 paper cites its synthesis operators. Its accessible text contains a similar inference from bounded powers to arbitrary \(\ell_2\)-coefficient synthesis. This strengthens the motivation for isolating the exact Hankel obstruction, but no claim is made here about every theorem in that earlier work or about later editorial versions not inspected.

## Value

PASS.

The finding separates a false analytic step from a valid geometric conclusion. It gives an explicit, reusable counterexample; identifies the exact classical function-space boundary for the failed operator; and replaces the defective synthesis argument by a shorter proof that is stronger than the bidisk-coordinate formulation because it works for arbitrary Hilbert multiplicity and arbitrary coefficient directions. This preserves the scientifically interesting projection-rigidity phenomenon without propagating an invalid all-\(H^2\) operator claim.

## Scope and limitations

The result does not settle the Hilbert-space invariant subspace problem. It repairs the common-shadow mechanism for the backward shift, not all claims in the cited papers. Independent audit and independent validation have not been performed.
