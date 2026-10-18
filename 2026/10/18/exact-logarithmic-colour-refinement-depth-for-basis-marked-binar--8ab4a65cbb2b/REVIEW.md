# Scientific review

## Correctness — PASS

The proof tracks a two-sort synchronous refinement process, not a colour-unaware graph traversal. Because the original geometry is a Steiner triple system whose lines have exactly three points, a pair of individually coloured points produces a uniquely coloured line in one round and identifies its third point in the next. The induction's converse checks that every still-unnamed point has precisely one incident line of each singly labelled type and a fixed number of wholly unlabelled lines. This prevents unproved extra splitting, yielding an **exact** partition at every even round. The support-doubling identity and an explicit pair of same-coloured late lines prove both sharpness formulas, including dimensions two and three. The automorphism lower bound for fewer than a basis of marked points is an explicit linear shear fixing the span. Direct and independent arithmetic checks corroborate, but are not used as a substitute for the proof.

## Originality — PASS, subject to remaining priority risk

The inspected Arvind–Köbler–Rattan–Verbitsky treatment of colour refinement and refinability (arXiv:1502.01255, Introduction and Section 8) gives the general framework, but not this binary projective incidence partition. The Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan individualization study (arXiv:1606.04383, Introduction and Section 4) develops general complexity classifications and bounded-round decision problems, not the sharp all-dimension incidence calculation. Assmus's 1995 treatment of binary Steiner-system codes is pertinent background; its accessible abstract was read, **not the full paper**. Earlier low-dimensional or marked-configuration calculations do not imply the precise doubled-support partition in unbounded dimension, its first-discreteness depths, or its exact minimum landmark count. Targeted research-record searches found no equivalent or stronger statement. Inaccessible specialized literature, or an unrecognized consequence of earlier geometry/individualization theory, remains a genuine residual publication-priority risk. Search failure is not proof of uniqueness.

## Value — PASS

Individualization followed by colour refinement is a standard tool in descriptive complexity and graph isomorphism. This result solves the **exact** least-landmark problem for a canonical highly symmetric incidence family and also determines when its many unmarked vertices become distinguishable. The unusual effect is a binary parallel closure: the maximum newly labelled support size doubles per **two** rounds, giving a sharp logarithmic rather than linear depth; discreteness of the whole graph occurs one round before the naive point-then-line estimate at exactly the special dimensions stated. It supplies a reproducible all-parameter classification and a natural test family for bounded-round refinement and landmark selection, not an arbitrary finite enumeration.

## Limitations and review status

No generalization to odd characteristic, arbitrary Steiner systems, or graph identification among all structures is proved. Experiments cover limited dimensions only. Earlier specialist coverage has not been excluded by an independent audit.

Self-review: passed. Independent audit: not yet performed.
