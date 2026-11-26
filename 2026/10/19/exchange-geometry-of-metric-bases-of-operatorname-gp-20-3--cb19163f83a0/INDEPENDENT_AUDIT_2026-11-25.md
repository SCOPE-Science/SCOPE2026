# Independent mathematical audit

## correctness

PASS

Independently reproduced the complete finite classification using reviews/evidence/gp20.py (Python with NumPy/SciPy). The code builds the labelled graph using cyclic rim distances and computes its distance matrix by Floyd–Warshall. A candidate resolves exactly when its landmark mask hits the separator mask for every pair. It tests all 91,390 four-sets (none resolve) and 658,008 five-sets; any smaller resolver would extend to a resolving four-set. The 41,040 successful five-sets have outer counts 1720,13400,20520,5300,100 for r=1,...,5 and zero for r=0. To build the exchange graph independently of trial replacements, all bases containing each shared four-set are connected in a clique; every exchange edge is generated exactly once. This gives 670,930 edges and degree extremes 7,69. Independent simultaneous rotations and reflections preserve the given edges, so eccentricity and rim count are constant on each orbit. There are 12 orbits of size 20 and 1,020 of size 40. Exact unweighted shortest paths from each of the 1,032 orbit representatives reach all states. Orbit-weighted eccentricities are 6 for 40,180 states and 7 for 860. The latter consist of one orbit of size 20 and 21 of size 40 and have rim counts 360,420,80 for r=2,3,4. The designated center and periphery have eccentricities 6 and 7, and the designated witness is distance 7 from the latter. To replay run python3 /workspace/reviews/evidence/gp20.py, or give consecutive half-open orbit ranges [0,256), [256,512), [512,768), [768,1024), [1024,1032) as two integer arguments and sum the weighted profiles. The original source programs and outputs were inspected, not executed.

## originality

PASS

The distinct finding is the full one-replacement graph classification for ordinary resolving bases of GP(20,3), not the previously reported dimension 5. The closest inspected catalogue results are on different underlying graphs and, in one case, a stronger condition on the state sets. A potentially related reconfiguration thesis listing remains bibliographic only and supplies no competing result.

## value

PASS

GP(20,3) is a motivated small parameter in the family because it has the known elevated metric dimension 5, singled out by the small-parameter dimension results rather than chosen by scanning an arbitrary range for a census. This makes it a natural test of reconfiguration of optimal landmarks. The exact data show that all minimum configurations are mutually reachable but that some require seven legal exchanges although any two five-sets can be joined by at most five unrestricted replacements. Radius, peripheral profile and orbit weights give useful exact benchmarks for structural or symmetry-reduced exchange bounds in this exceptional case, beyond recomputing dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
