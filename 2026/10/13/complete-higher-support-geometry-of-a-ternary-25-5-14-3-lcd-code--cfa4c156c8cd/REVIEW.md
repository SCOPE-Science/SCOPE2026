# Review of higher-support geometry for a ternary LCD code

## Correctness — PASS

The generator is transcribed directly from An–Hong–Kim–Lim, arXiv:2601.20600v1, Proposition 4.1, including the five appended positions. Exact row rank and Gram rank are both five. The exhaustive \(3^5\)-word census reproduces distance \(14\), and unique RREF representatives exhaust respectively \(121,1210,1210,121,1\) subspaces. Every support size is computed by testing vanishing at all \(25\) coordinates, not inferred from samples. A second census of projective planes using finite-field ranks reproduces the full two-space distribution and the six specific maximizing plane sections. The identity \(3\,|\operatorname{Supp}U|=\sum_{[u]\in\operatorname{PG}(U)}\operatorname{wt}(u)\) supplies an independent structural lower bound \(d_2\ge19\), matched by six witnesses. Limitation: this is an exhaustive finite computation tied to the displayed code, not a theorem about arbitrary LCD codes.

## Originality — PASS (with residual search risk)

The source's full publicly accessible preprint states the new code parameters and prints its generator but no higher-support table or exact minimum-support plane family. Anderssen–Johnsen, arXiv:2609.29796, gives a general matroid computation framework and a different worked code family, not the numerical spectrum of this code. Web searches for the code parameter/alias plus generalized weights, higher spectra and support planes found no statement of the same result. Related publicly indexed records on ternary Gashkov–Sidelnikov deep holes, generalized packing-covering and nonbinary weight gaps concern different objects and do not imply these exact numbers. Other examples in the An–Hong–Kim–Lim construction have different matrices; the inspected source does not transfer a higher-support distribution from them to \(\mathcal C_{3,4}\). A generic finite enumerator is not by itself a preexisting exact classification. Search incompleteness, especially abstract-only access to some related works, remains.

## Value — PASS

Higher generalized weights and their complete support distributions are natural invariants beyond the ordinary distance of a new LCD construction. The sharp \(d_2=19\) boundary, exactly six extremal two-subspaces, their explicit projective-plane intersections and the concentration of five of six on one coordinate describe concrete nonuniform minimal support geometry of this code. This is a complete finite classification for a motivated published construction, not a minor alternative normalization, bare weight-enumerator transcription, or an arbitrary selection of a parameter. No downstream universal theorem or application guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
