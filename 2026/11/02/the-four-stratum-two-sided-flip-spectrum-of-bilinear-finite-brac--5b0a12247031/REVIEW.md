# Mathematical review: cosquare-stratified bilinear brace probabilities

## Correctness: PASS

The precise domain is invertible bilinear multiplication matrices over all odd finite fields. The nilpotent-ring brace construction and explicit Yang--Baxter map are verified by direct substitution. A nonzero vector has two simultaneous linear vanishing constraints of rank one exactly on an eigenspace of the cosquare and rank two otherwise, yielding the all-dimensional formula. For two-dimensional matrices, discriminant and quadratic-character counting give the four exhaustive matrix strata. Each singular/alternating/symmetric boundary is treated separately, and the multiplicities sum to the exact general-linear-group order. The standalone standard-library checker enumerates all such matrices over four prime fields and all Yang--Baxter triples for the three types at \(q=3\). The symbolic proof, not the finite experiments, supports arbitrary odd prime powers.

## Originality: PASS, with priority qualifications

Ferrara--Trombetti--Tsang (2026) already defines the four probabilities, identifies their brace-theoretic interpretation, and gives an alternating bilinear determinant example. Bachiller (2014) already classifies prime-cube braces via bilinear-form parameters and change of basis. Mondal--Yadav (2026) already treats commuting probabilities for general skew braces. These are strong adjacent results and are not relabeled as new. The assessed claim is the complete spectral *joint and individual* flip profile for all nondegenerate bilinear radical braces and the exact labeled-matrix distribution for all odd finite-field orders, including nonalternating forms. The full accessible texts of the two closest papers were examined at the indicated portions; neither was found to state the four-row count or the general cosquare formula. Search of published mathematical records did not find a dominating result. Residual priority risk: older work on adjoint bilinear forms, congruence orbit counts, or brace commuting probabilities might imply an equivalent histogram. Priority cannot be guaranteed without broader independent review.

## Mathematical value: PASS

The comparison between two-sided and one-sided flip tests is the central new observable of the 2026 paper. On an established class of small radical braces, the result shows that the easier three probabilities collapse to a universal value while the two-sided probability detects four sharply characterized bilinear-form types. The histogram gives both existence and precise arithmetic frequency of each behavior for every odd finite field. The cosquare method extends to every vector-space dimension, making the finite three-dimensional classification a structural phenomenon rather than an isolated numerical example. The result is a natural exact invariant for the source's framework, not an arbitrary list of small cases.

## Boundaries and source comparisons

The four-row counts distinguish labeled bilinear multiplication matrices and do not count brace isomorphism classes. The computation does not handle degenerate forms, characteristic two, or the higher-dimensional cosquare histogram. See the theorem and reproducibility section in RESULT.md for details. Accessible full primary texts: Ferrara--Trombetti--Tsang, arXiv:2608.20620v1, pp. 2--5, 12--16, 17--19; Bachiller, arXiv:1407.5224v1, especially §§2 and 5.3; and Mondal--Yadav, arXiv:2603.16771v1, relevant introductory and commuting-probability sections. Literature-based originality evaluation cannot replace an independent priority determination.

Self-review: passed. Independent audit: not yet performed.
