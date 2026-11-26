# Independent mathematical audit

## correctness

PASS

Write n=qb+2s and a representation with ell coins as an unordered list of indices in [0,L] summing to s+(q-ell)b/2. Parity and the minimum generator force ell<=q for q>=0 because 2s<2b; the only possible nonnegative representative before q=0 is 2s-b<b. For s=0,1 below the proposed thresholds the ell=q lists are unique when feasible; a shorter eligible list needs index sum at least b+s, beyond its capacity (at most a+1 for the plus cases and at most 2a for the minus cases). For the other residues below threshold there can only be one-coin representations, except the last two minus residues, where q=2 gives the unique unordered pair of sum 2a-1 or 2a. At threshold the displayed pairs or triples are distinct, including at a=2; for the plus a=1 case the middle interval consists of s=2, with pairs (0,2) and (1,1). Adding b to both representations preserves their distinctness and proves exhaustion. The disjoint residue rays give the two rational series, and the threshold sums 3b^2+3b and 3b^2+7b give the asserted genera after subtracting (b-1)/2. The subthreshold counts give exactly the positive singleton sets, excluding the empty representation at zero. An independent exact coin-change check matched thresholds, singleton sets and genera for both families at a=2 through 40 (78 cases).

## originality

PASS

Credit the all-residue minimality and classified singleton loci, not the general Apéry identities, the extreme Frobenius residues or the published witness constructions. The closest publication on the same families establishes the maxima but not the full data: its minus-family middle witnesses can lie in strictly higher layers. The Nov. 8 indexed comparator gives the same arrays and implies the same p=1 consequences for a>=4; this is substantial later indexed coverage, not evidence of an antecedent theorem to the Nov. 2 entry or of independent priority.

## value

PASS

The first repeated representation in each residue is a natural refinement of the p-Frobenius problem for the same motivating families. Knowing each exact onset, and which earlier elements are represented once rather than not at all, answers membership and uniqueness for all n and permits genus and series evaluation; the published maxima cannot give these distinctions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
