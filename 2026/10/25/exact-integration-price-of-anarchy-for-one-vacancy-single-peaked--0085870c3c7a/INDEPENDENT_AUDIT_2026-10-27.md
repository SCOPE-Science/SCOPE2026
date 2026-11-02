# Independent mathematical audit

## correctness

PASS

A one-vacancy cycle has attainable closed-occupied-neighborhood same-color fractions 1/3,1/2,2/3,1, with utilities q,1,q,0 (0<q<1); a nonsegregated agent at q has two occupied neighbors and moving to the vacant site cannot raise utility, while a utility-one agent cannot improve. Only segregated agents may profit. If vacancy neighbors are both red, every blue must be integrated; blue-run lengths in the occupied path are at most two. Hence at least ceil(b/2) blue runs and ceil(b/2)+1 distinct bordering red agents, attaining minimum NE integration b+ceil(b/2)+1. Symmetric blue-vacancy and mixed-color-vacancy cases have no lower NE integration; run construction with red endpoints saturates the bound for all r>=b>=1, r+b>=3. Global integration <=min(r+b,3b), since each blue can expose at most two red agents; alternating singleton-blue/red-run constructions attain it, with r=b and r>b cases treated separately. Exceptional r=b=1 triangle has value 2 and PoA 1. Independently enumerated all placements/deviations via exact rational utilities for r+b<=11 and r>=b, recovering both extrema. All-size proof uses the run argument, not enumeration.

## originality

PASS

Qualified PASS: Friedrich–Lenzner–Molitor–Seifert 2023 is the exact same jump-game model and proves FIP on one-vacancy cycles and a general PoA upper bound min(Delta,n/(b+1)), but its inspected Section 4.1 does not determine exact worst-cycle equilibrium integration b+ceil(b/2)+1. Bilò et al. use swaps without the vacancy; Agarwal et al. use monotone preferences. An inaccessible broader residential-segregation thesis could contain exact cycle refinements and is flagged, not assumed noncovering.

## value

PASS

In a canonical graph-game instance with guaranteed equilibrium under a single-peaked half-preference, the theorem determines exactly how welfare at the worst Nash equilibrium depends on two populations, sharp constructions and asymptotic inefficiency two. This refines coarse degree-based PoA bounds on an economically and combinatorially motivated family, rather than a routine restatement of potential existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
