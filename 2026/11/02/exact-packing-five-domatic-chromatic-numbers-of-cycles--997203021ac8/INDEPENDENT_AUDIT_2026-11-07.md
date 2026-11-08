# Independent mathematical audit

## correctness

PASS

PASS. For every simple labelled C_n with n>=5 and exactly five disjoint broadcast-dominating layers, the universal four-color lower bound follows from c2<=floor(n/3),c3<=floor(n/4), making total incidences 3c1+5c2+7c3=5n+2(c3-c1)<5n for 3-color palettes. Singleton-layer counting gives 6 for n=5,6. Independently reimplemented depth-first enumeration of ALL four-palette cyclic packing words for n=7,8,9,11,12,13,14,18: counts 28,68,72,440,760,1092,1554,17172 (sum 21186); only 44 at n11 meet depth>=5, and each has a six-clique in the forced-distinct relation, forbidding five layers. Independently checked all 35 shipped radii/layer witness pairs n=5..39 for packing and every vertex/layer broadcast. Independently checked 171 spliced examples lengths 30..200. The proof for all n>=30 uses the exact centered 9-symbol local window property and shared 8-symbol prefix between n10 and n30..39, allowing repeated 10-symbol addition; neither infinite coverage nor negative completeness is inferred from a finite sample. Boundary n19 is the eventual threshold.

## originality

PASS

PASS with explicit access risk. Brešar–Ferme–Hu 2026 introduce the identical packing k-domatic invariant, give paths for k=3,4,5 and cycles for k=3,4, but their published abstract and detailed available secondary exposition do not claim the cycles k=5 classification. Paths k=5 neither close cyclic boundary constraints nor force the 8 exceptional small-cycle obstacles; lower k cycle formulas do not imply five layers. An inaccessible full preprint remains a priority risk, and absence from its abstract is not a document-wide NOT_COVERING proof. The independently enumerated finite obstructions and splicing lemma supply the mathematical distinction.

## value

PASS

PASS. A complete exact chromatic spectrum for the fixed five-layer broadcast condition on cycles addresses the natural next unclassified parameter of a recent graph invariant, including sharp n19 eventual threshold and eight scattered exceptions. The reusable 8-symbol splicing plus complete small-instance obstructions supply mathematical classification, not merely a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
