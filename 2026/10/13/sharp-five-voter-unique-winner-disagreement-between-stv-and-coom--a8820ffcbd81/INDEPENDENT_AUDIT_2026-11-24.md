# Independent mathematical audit

## correctness

PASS

A fresh exact multiset enumeration, with all tied eliminations and tied pairwise finals represented, gives anonymous disagreement counts (0,0,0,0,6), labeled disagreements (0,0,0,0,180), and labeled both-singleton counts (6,12,132,576,6516) through five voters. Replay: python3 /workspace/branches/52bde4da-ea0f-45f4-a482-61df5d028e63/reproduce_stv_coombs.py --max-n 5. The six profiles form one orbit, each with 5!/(1!2!2!)=30 labelings, and the stated vector is the lexicographic representative. The fractions reduce to 5/216, 5/181 and 1/42. Independently, a majority-first candidate survives some Coombs branch at n<=5 (at most floor((n-1)/2) last places, not enough for a unique last-place maximum) and wins every final it reaches; STV elects it. Without that majority, n=2 has first counts (1,1,0) and a final tie; n=3 has (1,1,1), and any sole STV winner must beat both others; n=4 gives (2,2,0) and a final tie, or (2,1,1) where the only possible sole STV winner must beat both others. In the latter Condorcet cases the winner can be last at most once, so cannot be the uniquely eliminated Coombs first-round candidate. At n=5 without a majority, first counts are (1,2,2). If eliminating A elects C, the sole A ballot is ACB. Coombs cannot have A among its eliminations if it uniquely elects someone else. C can have at most two last places and cannot be the sole elimination; B cannot be a sole winner from eliminating C if another tied elimination removes B or A. Thus the only different sole winner is A from eliminating B. Both B-first ballots must then be BAC to give A the runoff against C, which puts C last twice. To make B uniquely most-last, both C-first ballots must be CAB. This forces the stated orbit; its pairwise margins and the Condorcet description follow directly. Majority-stop preserves the disagreement layer, not the full winner correspondences or necessarily the conditional denominator under a changed convention.

## originality

PASS

The checked sources establish the runoff definitions and earlier comparison questions, but not the first distinct-singleton layer, its conditional denominator or its orbit. The strongest indexed numerical and structural overlaps concern different rule pairs and do not give the result by substitution.

## value

PASS

These two close three-candidate runoff systems share a head-to-head final but select first-round losers by opposite types of ballot information. The first exact distinction stable under every admissible tie resolution is therefore a meaningful finite cutoff. The single orbit and the Condorcet winner's role explain the voting mechanism; the labeled and both-singleton counts serve different, explicit sampling questions rather than arbitrary data slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
