# Independent mathematical audit

## correctness

PASS

Independently reproduced the named graph and all claimed degree/eccentricity counts with /workspace/petersen_replay.py (run `OPENBLAS_NUM_THREADS=1 python -B /workspace/petersen_replay.py`, with NumPy/SciPy). The pentagon/pentagram/spoke presentation was checked against all pairs of the assigned KG(5,2) vertices. Enumerate proper restricted-growth codes with at most six blocks; for a middle edge uv in a proper colouring, a forbidden alternating P₄ exists with that middle edge iff u has another neighbour of v's colour and v has another neighbour of u's colour. Their distinct colours ensure four distinct vertices. This yields no partitions below five and exactly 64 and 410 for five and six blocks. Expanding by all named colour permutations gives 341,280 distinct codes (the five-block case has just one unassigned name). For each omitted coordinate, sort all valid codes by the other nine coordinates: each bucket is exactly a clique of size at most six, and each edge lies in exactly one such clique. This independent adjacency construction gives 1,094,400 edges and degree multiplicities 3:14,400; 4:64,800; 6:108,000; 7:86,400; 8:21,600; 10:46,080. The 7,680 codes avoiding name 5 induce no edges. Independently enumerating graph automorphisms by consistent adjacency assignments gives 120 and eleven partition orbits. Full named-state shortest paths from each orbit representative reach every state; one six-block orbit of 30 partitions has eccentricity 14 and the other ten have 15. Multiplying orbit sizes by 720 gives 21,600 and 319,680 respectively, proving radius 14, diameter 15, and minimum nonempty connected palette six. Source C++ and Python and their logs were inspected, not executed; in particular the Python partition quotient by itself cannot establish named distances.

## originality

PASS

The distinct supported claim is the sharp mobility threshold and exact geometry of named, star-preserving one-vertex reconfiguration on the Petersen graph. The established star-colouring condition and general existence results are not new; the comparison does not rely on a priority claim for the isolated χ★(P)=5 value. No inspected covering reconfiguration theorem or matching indexed census was found.

## value

PASS

Petersen is a canonical cubic graph, and the move constraint is the standard one-vertex reconfiguration move restricted to star colourings, not a chosen ad hoc slice. The first extra palette colour changes complete freezing to global connectivity, and the exact distances and degree data give concrete benchmarks for constrained recolouring and for distinguishing named-state geometry from quotient geometry. The value rests on this mobility and metric classification, not on recomputing an ordinary colouring invariant or merely finding a single valid star colouring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
