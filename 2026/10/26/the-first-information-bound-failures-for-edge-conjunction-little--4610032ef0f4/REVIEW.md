# Independent mathematical audit

## correctness

PASS

The proof derives the exact binary-tree Littlestone recurrence D(v)=max_U[1+min(D(v&Q(U)),D(v\Q(U)))] over proper nonempty splits, with D(singleton)=0. The actual verify_all.cpp iterates every one of 2^21-1 nonempty edge masks and all 128 vertex queries in induction order; the independent rewritten C++ solver exhaustively confirmed exactly 147 failures, all 16-edge masks of dimension 3. An independent constructive set comparison verifies exactly 42 K6-with-leaf and 105 K6-edge-subdivisions, with no 8/8 query split. Isolated-vertex embedding settles <=6 vertices. Exhaustive finite verification is a complete argument for <=7, not beyond.

## originality

PASS

The invariant is adaptive Littlestone dimension of an edge-indexed class of vertex-conjunction query functions, not primal VC dimension of induced edge sets nor a general aggregation bound. Relevant checked sources do not state its exact <=7 classification; priority remains best-of-knowledge.

## value

PASS

Smallest obstruction to saturation of the information-theoretic Littlestone upper bound is a natural learning-theoretic graph invariant. The sharp 7-vertex, 16-edge cutoff and exact two-class characterization give meaningful boundary structure, not an arbitrary isolated numerical count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
