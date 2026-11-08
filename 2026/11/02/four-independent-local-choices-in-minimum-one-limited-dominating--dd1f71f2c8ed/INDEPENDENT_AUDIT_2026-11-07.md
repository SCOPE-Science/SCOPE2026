# Independent mathematical audit

## correctness

PASS

For the word-labelled S(n,3) with n>=3 and the stated one-limited domination predicate, partition into disjoint S(2,3) nine-vertex blocks. A terminal triangle cannot have exactly one chosen vertex (it would have two omitted neighbors); if no triangle is empty, there are at least six chosen. If one triangle is empty, its two intertriangle-linked omitted vertices require chosen endpoints in the two other triangles, and their one-outside-neighbor budget forces those whole triangles chosen, again >=6. Thus global |D|>=6*3^(n-2)=2*3^(n-1). In S(3,3), two balanced 18-vertex configurations come from the two six-cycle perfect matchings of non-diagonal terminal triangles, each omitting all three outer corners. Two unbalanced 18-vertex configurations omit all terminal triangles with b=a+s mod3, s=1 or2; other triangles are full, including outer corners. Each is a valid minimum set. Inter-block edges meet only corners; balanced corners are absent but internally dominated, unbalanced corners are selected in full triangles and can tolerate one omitted cross neighbor. Any of four states may therefore be chosen independently for each of the 3^(n-3) S(3,3) blocks, giving distinct minimum sets and M_n>=4^(3^(n-3)), entropy liminf log M_n/3^n >= log4/27. Bound is not asserted exact. Independent literal graph-edge enumeration verified four states and all 64 n=4 products; the unrestricted proof uses the corner argument.

## originality

PASS

Qualified PASS for the new labelled multiplicity lower bound and four-state product including nonbalanced choices. Božović (2026) establishes the MINIMUM CARDINALITY in exactly the same word-labelled Sierpiński graph, and that is credited; a matching/dimer literature study of Hanoi graphs has a different invariant and could overlap the balanced construction, not shown to supply nonbalanced 1-limited domination counts. Inaccessible 2019 full text is named residual risk.

## value

PASS

The count of minimum solutions and positive exponential density of independent choices are natural graph-enumerative invariants, beyond the already known minimum cardinality. Two qualitatively different boundary-compatible configurations create a meaningful entropy lower bound and show balanced-only pictures miss many optimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
