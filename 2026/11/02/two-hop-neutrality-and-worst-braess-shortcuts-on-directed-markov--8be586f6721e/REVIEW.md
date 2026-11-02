# Scientific review

## Correctness — PASS

The theorem is proved for every integer \(n\ge3\), all strictly positive original jump rates, and every added rate \(t\ge0\). The cyclic matrix determinant plus one rank-one cofactor yields the exact first two positive-order characteristic coefficients; since the CTMC is irreducible, their ratio is the integrated trace of the semigroup. A direct differentiation certifies the all-strength sign classification. In unit rates, a factorization by \(k-2\) gives an exact sharp neutrality boundary, while strict scalar unimodality and an adjacent difference factor settle every shortcut maximizer and tie. Independent exact-rational characteristic-polynomial computations in `verify.py` passed 9,920 assertions. The finite tests do not prove the quantifiers; the accompanying determinant/coefficient argument does. There is no claim concerning other mixing metrics.

## Originality — PASS, with a specified residual risk

The primary sources actually inspected are Catral–Kirkland–Neumann–Sze (2010, full 24-page text, especially Sections 5–6), Kirkland (2010, full 15-page text), Hunter (2012, full 13-page text), Kirkland–Zeng (2016, full 21-page text), and Patel–Agharkar–Bullo (2014/2015, full 12-page text). Catral et al. give general perturbation identities and a discrete-time graph invariance criterion when directed cycles have equal length; neither assumption nor conclusion matches the chorded continuous-time ring with its generally unequal cycle lengths. Kirkland optimizes over unrestricted stochastic matrices, not positive-base-rate continuous-time link additions; Kirkland–Zeng discuss undirected trees; Patel et al. focus on surveillance Markov optimization. Related existing numerical-integration and fastest-mixing research addresses different dynamical quantities, rather than the exact chorded-ring integrated-trace law. Searches included direct wording, synonyms, parameter reductions and exact primary-source theses. A general existing perturbation identity could be specialized to derive parts of the formula, and unindexed specialized continuous-time digraph work might have an equivalent classification; this is an acknowledged residual risk, not an assertion of exhaustive novelty proof.

## Mathematical value — PASS

The unit-rate sign flips at precisely a two-step jump, in a counterintuitive direction for every longer shortcut; the neutrality holds for every positive strength, not at an isolated tuned value. The exact transition between worst shortcut locations as added rate increases supplies a practical network-design boundary. The heterogeneous formula predicts when the same two-step addition becomes beneficial or harmful under altered baseline jump rates, adding meaningful structure beyond a numerical case or a tautological specialization.

## Limitations and closest literature

The scope is one fixed directed one-way ring with one added jump, and the functional is continuous-time integrated relaxation rather than the usual spectral gap or total-variation mixing time. Full text was inspected for the five named sources. Earlier specialized unindexed papers or a stronger general theorem may encompass the result; that residual risk should be checked in an independent literature audit.

Self-review: passed. Independent audit: not yet performed.
