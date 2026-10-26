# Self-review

## Correctness — PASS
The claim is for all integers \(r\ge3,m\ge2\) and all real \(h\ge0\). Three explicit spectral projectors reduce every matrix entry to one of three exact rational functions; both off-diagonal types are positive at every positive step. The quartic numerator of the diagonal controls entrywise positivity. Three positive-coefficient polynomial certificates prove all unconditional cases, monotonicity covers the one smaller case, and four parameter-family witnesses cover all remaining integers. Descartes' rule and the opposite signs at zero, a witness, and infinity prove exactly two distinct positive boundary roots in every failing family. An exact-arithmetic program independently reconstructs the algebraic identities and seven finite matrix instances. These are corroborations, not replacements for the all-parameter proof.

## Originality — PASS (bounded literature assessment)
The closest general sources are the Padé/positive-systems articles of Zappavigna, Colaneri, Kirkland and Shorten (2010; 2012), and the Radau-method exposition of Hairer and Wanner. Neither source's inspected mathematical results gives an equal-part complete multipartite \(r\ge3\) sharp positivity classification. The complete-bipartite Radau classification concerns exactly two parts and the fourth-order Gauss classification uses a different stability map; neither implies the full statement here, especially the proof that the unsafe set has precisely one connected component for every admissible integer pair. Search-based historical noncoverage remains provisional: an equivalent specialized result in poorly indexed literature could exist.

## Value — PASS
This answers a motivated numerical diffusion safety question for every balanced complete multipartite network with at least three nontrivial communities: exact unconditional safety families, and sharp two-sided timestep reentry limits for all others. The threshold occurs at twelve vertices within this family, and the complete positivity set is never merely inferred from finite simulation. The distinction between stability, positivity, and positivity reentry is consequential when numerical states represent concentrations or probabilities.

## Limits
The theorem does not claim unequal part sizes, arbitrary Markov generators, internal-stage positivity, or independently reviewed validity. Exact thresholds are given as algebraic roots instead of radical expressions. The identified literature comparison does not prove historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
