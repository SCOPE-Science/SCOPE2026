# Scientific review

## Correctness
PASS. The nine complete minimal support masks follow from all admissible six-bit inputs. Explicit periodic and run-extended input templates witness every forbidden support for all higher run bounds. The complementary graph certificate removes the 111 loop and checks no remaining cycle and a controlling run-length inequality, which proves preservation for all parameters. Determinization with trailing-one tracking is a decision procedure over *all* admitted finite output words, not only bounded enumeration; independent direct block enumeration checks each computed first obstruction. The eventual case follows from a six-symbol full-shift check and the eight-bit predecessor window. `verify.py` reproduces the finite certificates and `classification.csv` exactly.

## Originality
PASS on examined sources, subject to historic-priority uncertainty. Baker–Ghenciu (arXiv:1411.7167) provides general entropy and specification results for bounded-gap shifts, Dastjerdi–Jangjoo (arXiv:1108.3242) provides structural and coding background, and Kari–Taati (DOI:10.1007/s10955-015-1281-2) provides surjectivity/pre-injectivity and entropy principles; none of the examined full-text relevant sections states the radius-one 62/70 family census or exact nonmonotone observation thresholds. Kopra (arXiv:2001.09699) considers a different general beta-shift problem; its abstract was checked and full comparison remains a residual risk. Semantic published-research searches on bounded runs, radius-one endomorphisms, forbidden output words, and sharp eight-block cutoff returned related cellular-automaton work but no equivalent quantified theorem. An unindexed code table could still cover the claim.

## Value
PASS. The object is a natural nested infinite family of mixing finite-type constraints. The result gives a complete restricted-neighborhood endomorphism census, a rigid surjectivity boundary across the entire family, and an *optimal uniform finite observation bound*. The nonmonotone 7-to-8-to-5-to-6 obstruction profile is not a formal consequence of the general Garden-of-Eden equivalence or finite type alone and identifies a meaningful small-scale extremum when the admissible rule family has already stabilized. These are exact structural distinctions, not arbitrary parameter slices or tiny numerical improvements.

## Limitations and closest literature
The result is restricted to radius one and the single forbidden family. Nothing is asserted about larger-radius maps or eventual temporal image limits. Earlier exhaustive enumerations might exist outside inspected sources; no independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
