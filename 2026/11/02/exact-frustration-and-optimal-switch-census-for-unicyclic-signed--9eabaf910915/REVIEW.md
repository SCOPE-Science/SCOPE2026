# Mathematical review

## Correctness — PASS

The incidence signs count one negative signed-line edge per incoming–outgoing pair at a common vertex, agreeing with the established orientation formula of Bal [1, Section 8]. Every odd cycle forces a vertex to be mixed on its two cycle edges. At that vertex the indegree–outdegree product is at least its degree minus one. A minimum-degree cycle vertex can attain exactly this bound by alternating sources/sinks on the remaining path and attached trees. At equality there is only one mixed vertex and all remaining edge directions are forced. Counting the two path alternations, the minimal cycle vertices, and the optional uniform direction of noncycle incident edges gives the asserted number of orientations. The line graph is connected, so global orientation reversal is the precise twofold redundancy in the switched signed signatures. A distinct direct-enumeration implementation confirms the formula on all 3,898 labelled unicyclic graphs of orders three through six. Finite tests are not used in place of the proof.

## Originality — PASS with priority risk

Bal [1] establishes the general minimization identity, defect bounds, and several special classes, notably cubic graphs; those results are expressly not new here. The all-degree unicyclic exact expression and complete optimizer multiplicities were not located in the inspected text. Belardo, Stanić and Zaslavsky [2] establish the earlier signed-line construction and general signed-graph principles, not this family enumeration. Targeted alternative-formulation and signed-line-graph searches, along with searches of mathematical research records, did not identify equivalent or dominating coverage. This is evidence of a specific unaddressed refinement, not proof of historical uniqueness. A prior orientation-counting theorem or less-direct consequence of general signed-graph results may still cover the claim.

## Value — PASS

A general frustration inequality can be loose even for graphs with one odd cycle; the formula identifies exactly which local degree controls it and completely classifies equality orientations for an infinite graph class. The two-versus-four optimizer factor distinguishes degree-two cycle vertices from cycle vertices supporting attached trees. The result also characterizes sharpness of both defect bounds within odd unicyclic graphs and provides exact counts of optimum switched signed signatures. The count is a natural structural refinement of a recently studied optimization invariant rather than an arbitrary parameter slice.

## Evidence and limits

Primary references: Bal, *The Antisymmetric Line Graph*, arXiv:2603.03087v2, Sections 3 and 8; Belardo, Stanić and Zaslavsky, *Total graph of a signed graph*, arXiv:1908.02001v3, Section 2 and relevant balance results. The attached exact checker separately enumerates orientations and signed-line switchings. The theorem does not address multicyclic graphs, symmetry orbit counts, or unseen priority results.

Self-review: passed. Independent audit: not yet performed.
