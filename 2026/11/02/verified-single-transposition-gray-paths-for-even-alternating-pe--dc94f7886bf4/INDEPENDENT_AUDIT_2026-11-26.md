# Independent mathematical audit

## correctness

PASS

Replayed the frozen gray_paths_u16le.bin with the fresh verifier /workspace/branches/0376a469-53f7-424c-b1d9-a017debe03a4/independent_verify.py (python3, certificate path as its argument). I inspected the decisive code. The recursion tries every unused value subject exactly to the next alternating inequality, so its leaves are precisely all admissible permutations and in lexicographic order. Each fixed-size little-endian block has its entire index range as its index set, hence no omissions or duplicates, and each consecutive pair agrees outside two positions and has the two entries exchanged. All 103944 bytes were consumed: 5, 61, 1385, 50521 states and 4, 60, 1384, 50520 transitions (51968 total). SHA-256 a9fc613421c0eea64144092a959a85754da4fa1d16ceeba607f0611a17657b62 identifies the replayed input; legitimacy comes from the checked moves and exhaustive coverage, not the hash. The supplied two verifiers were read as evidence, not executed. The signs alternate at every edge, so odd vertex counts exclude a Hamilton cycle, not a path. This checks exactly the four stated sizes, not an all-even theorem or a generation algorithm.

## originality

PASS

No inspected source establishes the exact single-transposition paths through the four even sizes. The strongest related literature and indexed result differ in parity class, move set, hypotheses, or invariant. The finite n=10 witness is distinct from the classical vertex count and does not purport to resolve the open general question. This is a bounded best-of-knowledge decision, not a priority claim.

## value

PASS

The cutoff gives explicit positive cases for a documented even-size Gray-code question, including the full 50521-vertex n=10 graph. This is not a re-enumeration of zigzag numbers: the certificate witnesses a global ordering subject to a sharp single-move constraint and can be independently checked in full. The value is a reusable, meaningful finite benchmark, not a uniform construction or resolution of the general problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
