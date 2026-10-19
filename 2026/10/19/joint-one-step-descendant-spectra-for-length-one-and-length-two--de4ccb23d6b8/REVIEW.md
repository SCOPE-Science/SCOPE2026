# Scientific review

## Correctness — PASS

The exact-one descendant counts follow from the injective fixed-length difference encoding: inserting a zero block has exactly one distinct outcome per zero-run boundary, giving one plus the number of nonzero differences. A two-state extension of the last adjacent letter pair proves the full bivariate enumerator. Forest-edge independence gives the marginal binomials; pairwise edge independence gives zero covariance. The exact conditional expectation and the binary alphabet extremal classifications are proved separately by sampling without replacement and by the binary adjacent-difference path optimization. `verify.py` independently enumerates actual tandem-duplication outputs for all 27381 tested words, recovers the same bivariate distributions, and checks counts and extrema. No finite experiment is used as proof of an infinite statement.

## Originality — PASS with residual risk

The closest literature is Yehezkeally--Schwartz (arXiv:1801.06022), its follow-up (arXiv:2001.07047), and Jain--Farnoud--Schwartz--Bruck (arXiv:1606.00397), which earlier solved bounded-duplication coding problems but not this joint size spectrum. The first treats reconstruction and descendant-cone geometry for a *fixed* length and already provides the difference transform used in the preliminary lemma. The second explicitly restricts to a single fixed duplication length. Comparison by implication shows that neither inspected manuscript states the *joint* mixed-length enumerator, conditional dependence, or simultaneous q-ary/binary sharp extrema. Relevant published fixed-length confusability and noisy-duplication results are differently quantified and likewise do not supply the joint coefficient law. A hidden equivalent theorem remains a real possibility; search absence is not proof of uniqueness.

## Mathematical value — PASS

The result solves a naturally motivated full two-length one-step sphere-profile problem for every finite alphabet and source length, rather than merely giving another marginal bound. It exposes exact dependence invisible to covariance, provides all bivariate counts via a low-state transfer, and identifies a sharp binary-versus-larger-alphabet extremal transition together with exact extremizer multiplicities. Such output multiplicities are inputs to mixed-length reconstruction and channel ambiguity calculations; no unsupported coding-capacity theorem is asserted.

## Scope and limitations

Only exact one tandem-duplication event of length one or two is classified. No independence or coding bound for multiple errors is claimed. An unindexed two-length refinement may predate the result. There is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
