# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked against the full text of Matsuzaki's arXiv:2609.18121v1 and Tabor's 2003 paper.

1. Tabor's Corollary 1 states that a surjective solution of the exact Fischer--Muszely norm equation on a group is additive. Applied to the additive group of the domain C*-algebra, this gives additivity from the first norm identity without injectivity. Matsuzaki explicitly makes this same reduction.
2. Matsuzaki's proof that \(u=T(1)\) is a symmetry uses surjectivity and the product-norm identity, not injectivity.
3. The only injectivity step in Matsuzaki's centrality argument can be removed. For \(x\in pBq\), one has \(T(a^2)=0\); additivity gives \(T(1-a^2)=u\) directly, which is sufficient to retain the identities \(\|1\pm2x\|=1\). The C*-order argument then forces \(x=0\), so \(u\) is central.
4. After normalizing \(\Phi=uT\), positivity and self-adjoint contractivity require no injectivity. The additional identity
\[
\|\Phi(a)\|^2=\|\Phi(a^*a)\|\le\|a\|^2
\]
then gives global contractivity, hence continuity and real linearity.
5. The product-norm identity makes \(\ker\Phi\) a two-sided *-ideal; contractivity makes it closed. Factoring it out produces a bijection satisfying Matsuzaki's original hypotheses. Since the induced map is already unital, Matsuzaki's central-symmetry factor on the quotient must be the identity, so the induced map is a real *-isomorphism.
6. The converse was checked directly. Evaluation \(C([0,1])\to\mathbb C\) provides a concrete noninjective example, proving that the surjective theorem is genuinely stronger than the bijective theorem rather than a vacuous reformulation.

No computational evidence is used; the result is purely deductive.

## Originality

PASS, to the best of our knowledge.

Matsuzaki's current theorem is explicitly stated for bijections. The full v1 text was searched for quotient and kernel formulations; none were present. The proof itself highlights injectivity in the centrality step, while additivity is explicitly attributed to surjectivity through Tabor.

External searches covered combinations of "ring isomorphism in norm", "surjective", "epimorphism", "quotient", "C*-algebra", "central symmetry", and "real *-epimorphism". They located Matsuzaki's bijective theorem, the earlier continuous-function bijective results, and Tabor's Fischer--Muszely theorem, but no classification asserting that every surjective map satisfying the three identities factors through a C*-quotient as a central symmetry times a real *-isomorphism.

Tabor's 2003 paper was available and its exact Corollary 1 was inspected, so there is no access uncertainty about the additivity input. No specific inaccessible paper was identified as especially likely to contain the same surjective quotient classification. The main residual risk is terminological: older linear-preserver or nonlinear-preserver literature may encode the same quotient reduction without using the recent phrase "ring isomorphism in norm". The novelty claim is therefore limited to the precise surjective extension and quotient classification of Matsuzaki's 2026 theorem.

## Value

PASS.

The result removes a headline hypothesis from a new rigidity theorem and identifies exactly what replaces it. Noninjectivity is neither pathological nor uncontrolled: it is forced to be a closed C*-ideal, the normalized map is a *-epimorphism, and the target is exactly a real-* copy of the quotient. The exact norm formula \(\|T(a)\|=\operatorname{dist}(a,\ker T)\) further shows that the metric defect is completely described by the quotient. The simple-domain corollary explains when surjectivity alone automatically recovers the original bijective theorem.

## Limitations

Surjectivity remains essential to the present proof and no result is claimed for nonsurjective or approximately satisfying maps. The quotient step invokes Matsuzaki's established bijective theorem rather than reproving its final multiplicativity argument from scratch. The result does not claim that the stated hypotheses are minimal among all possible norm-preserver assumptions.

Originality is to the best of our knowledge; broad older preserver literature was not exhaustively enumerated.
