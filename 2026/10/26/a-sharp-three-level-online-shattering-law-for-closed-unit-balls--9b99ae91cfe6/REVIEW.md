# Scientific review: closed unit balls in finite trees

## Correctness — PASS

The claim uses distinct closed-neighborhood indicator functions. For trees with at least three vertices, centers give distinct functions. Lemma 1 gives an exact criterion for a depth-two tree: one query must have two distinct hypotheses on each side. Lemma 2 proves that a positive root branch always has Littlestone dimension at most two and has dimension two precisely at degree at least three. Lemma 3 converts the negative root branch into the explicit neighborhood-intersection inequality. The root recurrence proves both necessity and sufficiency of the full depth-three criterion, and a leaf query gives the dimension-two floor for all trees of at least four vertices. The tiny trees are checked separately. The VC upper bound is a triangle-free, unique-path argument.

The independent direct game recurrence and Prüfer enumeration in `verify.py` agree with the formula on all 48 unlabeled tree types through eight vertices (including all 262,144 labeled eight-vertex Prüfer sequences). The depth-three witness has eight independently checked paths. The infinite theorem is justified by the structural proof, not the finite computation. Risks: code verification assumes the standard correctness of Prüfer decoding and tree canonicalization for the secondary eight-vertex count; these are inspectable in the file.

## Originality — PASS, with residual historical-priority risk

The 2022 full article of Chalopin et al. treats trees and even fixed-radius tree balls, making it a decisive same-object comparison. Its results concern sample compression and the VC bound, not the exact Littlestone dimension, the depth-three threshold or the branching test. The 2024 full paper of Coudert et al. treats the exact closed-neighborhood set system but static VC dimension, without an adaptive shattering classification. Targeted searches also considered aliases including unit balls, radius-one neighborhoods, online shattering, and tree mistake bounds. Relevant historical claims concerning shortest-path vertex sets, rooted descendant cones, and Hamming neighborhoods have different concept membership predicates and do not imply this tree-unit-ball result. The available searches are not exhaustive of unpublished or poorly indexed work.

## Mathematical value — PASS

The natural graph-ball concept class already appears in the cited learning and graph-VC literature. The theorem settles its optimal deterministic realizable online mistake bound for **every** finite tree, gives an efficient necessary-and-sufficient structural test, locates the smallest dimension-three instance exactly, and quantifies the first finite transition (12 of 23 eight-vertex trees). The resulting strict VC/Littlestone separation demonstrates an adaptive phenomenon invisible to the static bound. These are natural structural and algorithmic conclusions, not merely a recomputation of a known VC table.

## Closest literature and scope

Chalopin et al., arXiv:2206.13254v2, especially Sections 1–3; Coudert et al., DOI:10.4230/LIPIcs.SEA.2024.8, especially abstract, Sections 1–2 and 4–6. This review does not claim full historical publication priority, an independent review, or any extension to arbitrary graphs or all radii.

Self-review: passed. Independent audit: not yet performed.
