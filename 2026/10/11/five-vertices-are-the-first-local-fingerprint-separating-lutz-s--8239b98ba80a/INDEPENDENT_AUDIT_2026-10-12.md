# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md cf7cad5053159a237e7ed7c2320c6eb4fefb21f6, verify.py 820da3f232a5125a876c7d52da200850b445175c inspected. The 38 tetrahedra are reconstructed from Lutz Table2 and two 37-facet balls by deleting 2457 versus 34610. Independently rewrote entire combinatorial calculation in JS (not a replay of verify.py): for every vertex subset S of sizes 1 through 5, generated induced faces from the actual facets, computed f-vector and GF2 boundary-map ranks of all nonempty faces, Betti numbers and histogram Phi_k. Exhaustive counts 12,66,220,495,792 subsets for k=1..5; histograms equal through k=4 (distinct profiles 1,2,5,14), and first differ at k=5 (each 38 distinct profiles). Exactly six profile keys differ, each by one: A-B +1 at ((5,10,4),(1,2,0)),((5,8,1),(1,3,0)),((5,9,4),(1,1,0)), and -1 at ((5,10,5),(1,1,0)),((5,8,2),(1,2,0)),((5,9,2),(1,3,0)). No probabilistic sampling; this is a complete finite proof for all 792 relevant five-vertex subsets and all lower sizes under the explicit induced-complex definition. Global f-vector equality alone would not imply profile equality for k<=4, which was separately computed and verified.

## originality

PASS

Best-of-knowledge PASS. Lutz 2003 constructs the exact pair, equal face vectors and boundary-isomorphism, but does not give first local induced-f/Betti histogram distinction. A highly relevant Benedetti-Lutz 2013 full source computes mod2 homology after deleting five vertices from the PARENT 38-facet ball (thus retaining seven vertices) for evasiveness; this is not an equality/distinction comparison of five-vertex induced profiles for two 37-facet balls. Resultary found homology fingerprints for different Lutz spaces but no dominating result for this pair.

## value

PASS

PASS. For the classic pair of nonisomorphic balls whose boundaries and global f-vectors agree, the smallest vertex subset size at which the complete label-free local face-plus-homology distribution distinguishes them is a natural sharp combinatorial invariant. The exact cutoff 5 and six one-count shifts furnish a reproducible local recognition benchmark beyond known global/boundary data; a narrow finite classification can be scientifically useful without generalizing to all 3-balls.

The dated certificate retains the supplied scientific assessment, sources and limitations.
