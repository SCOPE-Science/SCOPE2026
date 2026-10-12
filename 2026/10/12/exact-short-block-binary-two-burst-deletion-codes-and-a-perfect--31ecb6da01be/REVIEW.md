# Scientific review

## Correctness

**PASS.** The argument gives size-four and size-eight deletion-output transversals at lengths seven through nine, including a six-orbit finite classification for the length-eight transversal. Period-two constructions attain the first four bounds; an eight-word linear code attains the length-nine bound. Its eight explicit output masks are pairwise disjoint and cover all \(32\) five-bit outputs, so it is a perfect code for the stated channel. Two independently implemented checks, `verify.py` and `verify_cpp.cpp`, recompute the entire channel for every short input, checks the masks, orbit witnesses and disjointness, and return `VERIFY_OK`. The general hitting-set bound and parity arguments are separately proved rather than inferred from computation.

## Originality

**PASS, subject to residual risk.** The closest directly matching source, Wang–Kong–Yaakobi–Duman (arXiv:2606.01245v1), establishes the known length-six boundary and bounds for arbitrary and two-two burst parameters. Its inspected Introduction, Sections IV–V, examples and conclusion do not state the exact length-seven-to-nine profile or a perfect length-nine code. Ye–Sun–Yu–Ge–Elishco (arXiv:2408.03113) constructs asymptotically efficient two-burst codes and gives bounds under long-block hypotheses; Lan–Sun–Yu–Ge (arXiv:2504.20460) concerns error-ball intersections and sequence reconstruction. An unindexed earlier short-block computation remains possible; no absence of publication is formally proved.

## Value

**PASS.** The natural first five admissible blocklengths reveal that increasing the length from six to eight does not increase the largest code, but length nine supports eight codewords. More significantly, the exhibited length-nine linear code is perfect for the exact channel: every received five-bit word decodes to precisely one of its eight codewords. This is a concrete finite coding benchmark and a sharp transition not supplied by asymptotic redundancy statements.

Self-review: passed. Independent audit: not yet performed.
