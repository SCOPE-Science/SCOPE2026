# Scientific review: triangular-graph open-neighborhood Littlestone ranks

## Correctness — PASS

The claim has a complete all-parameter proof. For any first edge query, its positive version space is two endpoint stars. A secondary query either has a four-hypothesis positive child or splits into two star-plus-one families, each of dimension at most two by the explicit exhaustive query types; hence the positive first child has rank at most three and the full family rank at most four. The exceptional upper bounds follow from distinct-function counts, including identical antipodal edge predicates for the six-vertex triangular graph of index four. Depth-three and depth-four shattered trees give the two nontrivial lower thresholds. Direct incidence-matrix recurrence through index eleven and separate all-leaf witness checking corroborate, but do not replace, this infinite proof.

## Originality — PASS, with limitations

The closest same-object primary source is Adler, Benediktsson and Macpherson, arXiv:2007.16042, on Johnson-graph open-neighborhood VC dimension and density. Its \(J(7,2)\) static shattering witness **already implies** the dimension-four lower bound from index seven onward, and is credited accordingly; it supplies neither a Littlestone upper bound nor the exceptional finite ranks. Ghazi et al., arXiv:2007.03668, concern general closure bounds, and Malliaris--Moran, arXiv:2108.05569, qualitative stability and online-learning properties. Searches for triangular graphs, complete-graph line graphs, and Johnson level two found no verified full-strength prior implication. A same-named triangular-graph homology publication was seen only through a summary and concerns a different invariant. An exhaustive historical priority certification is not claimed.

## Mathematical value — PASS

The adjacency set system of the first nontrivial Johnson scheme is natural and appears in published research. Exact online shattering is strictly different from static VC shattering. A sharp universal four-mistake bound, a structural local-branch proof, and the surprising transition from one to three before stabilization provide a meaningful infinite-family classification rather than a routine fixed-size calculation.

## Limits and reproducibility

The claim concerns ordinary deterministic realizable Littlestone dimension of **open** neighborhoods only, with neither higher Johnson levels nor agnostic loss models included. `verify_triangular.py`, `witness_trees.json`, and `verification_output.txt` reproduce the finite checks. No independent scientific audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
