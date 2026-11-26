# Independent mathematical audit

## correctness

PASS

Open-neighborhood domination requires each gap to be at most five (for unselected vertices) and at least one adjacent gap to be at most two at each selected vertex. Thus the number of long gaps is at most floor(t/2) and the maximum length for t selections is 2t+3 floor(t/2). The exhibited words attain the claimed cardinalities in all seven residues. In particular five selections cover at most sixteen cycle positions, and the word (2,5,2,5,1,2) gives six at n=17. Equality for n=7k forces alternating gaps 2 and 5. Each translate repeats its two residues mod 7 k times, so distinct translates differ by at least k deletions; for k>=2 none are adjacent. At k=1 the distance-two pairs give a 7-cycle. Equality for n=7k+2 forces k gaps of five, k+1 of two, and one short-short junction; its position uniquely marks each translate. An exchange must insert into the gap length 7 created by removing a 2/5 junction, since an unfilled length 7 is impossible. Removing at the 2/2 junction creates length 4; any resulting equality configuration must restore the original 2/2 split. Reversing a 2/5 or 5/2 split is legal exactly at the two boundaries of the short-short junction. In fact take the reference set with vertices 7j for 0<=j<=k and 7j+2 for 0<=j<k: translation by 7 removes 2 and adds 5, so both signed shifts are exchanges. There are at most two by the junction argument, and gcd(7,7k+2)=1 gives a single cycle.

## originality

PASS

The basic move notion and the seven configurations at 7k are prior, and the frozen result already disclaims novelty for that count. A later indexed polynomial record materially repeats the period-seven minimum and the 7k+2 optimal gap pattern. The distinct finding supported by the comparison is the corrected all-size argument against the published five-periodic formula and, especially, the exact powered-cycle exchange classification with signed-seven moves in the 7k+2 class. No priority is assigned from catalogue dates alone, and no separate novelty is credited to the frozen case inferred from the known seven sets.

## value

PASS

This corrects a concrete published numerical claim for a natural invariant, using a uniform sharp density argument rather than checking one counterexample. It also determines whether local moves can connect optima in two infinite residue classes, identifying the exact cyclic translation step or the absence of all moves. The exchange invariant and the finite obstruction at n=17 are independently useful for reconfiguration and polynomial baselines; no additional significance is assigned to recounting the previously known seven sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
