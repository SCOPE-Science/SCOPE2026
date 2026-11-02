# Scientific review

## Correctness — PASS

The claim covers all integer cycle sizes \(n\ge2\) and all real steps \(h\ge0\), with exact normalization. The stability function follows directly from the stated two-stage tableau. Algebraic factorization produces a convergent geometric series because the pole modulus is strictly less than one for positive steps; regrouping by residue classes gives the exact cyclic inverse formula. The sign proof covers both the first negative sine lobe and *every* later oscillatory phase, not only a finite enumeration. Its quantitative estimate \(\rho^n\le e^{-2\pi}\) forbids late-phase recovery below the proposed threshold. At the threshold exactly one displacement coefficient is zero; the zero-step matrix is separately treated. The executable verifier passed 25,420 assertions, including exact rational inversions and independent formula/tableau comparisons. Those finite checks supplement rather than replace the proof.

## Originality — PASS, with residual risk

The closest examined primary paper is Lóczi–Ketcheson (arXiv:1303.6651, accessible complete text, introduction and numerical preservation sections studied). It addresses generic absolute monotonicity, not this graph-specific necessary-and-sufficient cycle threshold. Bharali–Holtz (arXiv:math/0511325, entire paper available in text, especially the section on circulant matrices) addresses arbitrary entrywise-nonnegative circulants under *entire* functions, rather than a rational Runge–Kutta endpoint map of a shifted permutation generator. Baum's 2011 Lobatto IIIC presentation discusses positivity criteria but not the cycle's exact cotangent phase boundary. Related absorbing pure-birth calculations are not equivalent: adding the terminal-to-initial edge creates cyclic aliasing. Prior directed-cycle Radau IIA work uses a different stability function, and its small-dimension threshold does not imply the present all-length classification. Relevant published findings for SSP-SDIRK and [2/2] Padé similarly use different rational maps. An older specialist treatment of essentially the same cyclic resolvent may exist; negative search results do not prove novelty.

## Value — PASS

The result is a complete classification of a natural property of a standard numerical method on every finite directed Markov cycle. It identifies a sharp four-to-five-state obstruction and a nonintuitive positivity-recovery interval in which sufficiently large steps can be valid stochastic matrices even though sufficiently small positive steps are not. The explicit threshold is immediately usable in Markov numerical integration and the inverse-kernel formula explains the structural difference between cyclic and absorbing generators. The all-dimension obstruction and exact transition are not a mere arbitrary finite computation or cosmetic substitution.

## Limitations

The update preserves endpoint nonnegativity but the positive large-step region does not guarantee an accurate time approximation; internal stages, variable jump rates and general generators are outside scope. Primary-text coverage and related records were compared, but specialist historical coverage is not exhaustive. The embedded computation is finite, whereas the proof is analytic; independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
