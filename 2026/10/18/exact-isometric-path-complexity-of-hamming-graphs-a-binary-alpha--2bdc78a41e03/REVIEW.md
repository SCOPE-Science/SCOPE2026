# Scientific review: exact isometric-path complexity of Hamming graphs

## Correctness (C): PASS

The claim quantifies over every integer \(d\geq1\), \(q\geq2\), and uses the vertex-cover-by-rooted-geodesics definition, not ordinary isometric-path cover. In a binary cube each geodesic has at most \(d+1\) vertices and each adjacent pair has one endpoint one distance layer above the other. Extending a shortest path to the lower endpoint by their edge proves the pair-cover lemma. An explicit diametral path alternately increases and decreases root distance between two layers; one rooted geodesic contains at most one vertex from each layer. These arguments give matching bounds \(\lceil(d+1)/2\rceil\).

For \(q\geq3\), the proof selects two nonroot letters in every coordinate and switches all coordinates one by one. All \(d+1\) path vertices remain in the farthest distance layer, which each rooted shortest path meets at most once. The diameter provides the matching upper bound. The boundary \(d=1\) is separately checked and covered. A standard-library verifier enumerates 7,210 distinct shortest-path vertex sets and computes exact rooted set-cover minima for ten small \((q,d)\) cases. These experiments are confirmation rather than infinite proof.

## Originality (O): PASS, subject to historical-search limits

The mathematical parameter is already defined in the 2022 paper on isometric-path antichain covers and shown equivalent to the rooted-cover definition in the subsequent paper. The novel claim concerns its **exact values on the entire uniform Hamming family**, including a distinct binary and nonbinary formula. The 2022 original (DOI `10.4230/LIPIcs.ISAAC.2022.12`) mentions the global shortest-path cover number of hypercubes and Cartesian products of cliques, not the rooted single-path parameter; it proves generic upper bounds for the antichain parameter on other graph classes. The expanded open-access 2025 version of the 2023 complexity paper (arXiv `2301.00278`) gives its definition, polynomial algorithm and boundedness theorems, but not the Hamming evaluations. Direct queries using the names `ipco`, `ipacc`, `Hamming graphs`, `binary hypercubes`, `rooted geodesics`, `shortest path antichain` and the proposed parameter values revealed no equivalent formula in the checked sources.

The generic diameter bound gives only \(d+1\), and the class-wide boundedness theorems do not yield the binary exact value. A previously published global shortest-path cover number is not a stronger covering statement: it covers the whole graph using unrestricted geodesics and is quantitatively a different invariant. Database searches and inspected full primary material support originality but do not prove historical uniqueness. Residual risks include a synonymous unpublished or unindexed exact evaluation and older terminology from isometric coverings not captured by the searches.

## Value (V): PASS

This is an exact infinite-family evaluation of a recently introduced natural metric graph invariant for canonical Cartesian powers. It distinguishes two sharply different mechanisms: binary edges always advance or retreat one root layer and allow efficient pairing, but three available letters per coordinate permit a maximum-length geodesic to stay inside a single farthest sphere. The value jumps from about half the dimension to the greatest possible value with a one-symbol enlargement of the alphabet. It quantifies unbounded complexity and its exact growth in two standard graph families, with explicit witnesses rather than an isolated table entry.

## Scope and limitations

The proof establishes only equal-alphabet Cartesian powers of complete graphs; mixed alphabet products and unrelated graph classes are open here. Finite verification cannot replace the quantified arguments. The analysis of historical coverage depends on the available open-access full text and indexed records, and possible overlap under alternate terminology remains. Independent examination may revise the assessment.

Self-review: passed. Independent audit: not yet performed.
