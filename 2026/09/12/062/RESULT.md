# Face-size multisets of minimum-genus orientable embeddings of K(4,9)

## Context

The complete bipartite graph K(4,9) has bipartition sizes 4 and 9, hence
V = 13 vertices and E = 36 edges. Its orientable minimum genus is given by
Ringel's formula for complete bipartite graphs:

g_min(K(4,9)) = ceil((4-2)(9-2)/4) = ceil(14/4) = 4.

An orientable cellular embedding of genus g satisfies the Euler formula
V - E + F = 2 - 2g, so every minimum-genus (g = 4) cellular embedding has
F = 36 - 13 + 2 - 8 = 17 faces. Because K(4,9) is bipartite, every face
boundary walk has even length. The question is which face-size multisets
actually occur among minimum-genus orientable embeddings, and whether every
Euler-compatible multiset is realizable.

## Definitions

- K(4,9): complete bipartite graph with parts U = {0,1,2,3} and
  W = {4,...,12}.
- Orientable cellular embedding: encoded by a rotation system, i.e. a cyclic
  ordering of neighbors at each vertex.
- Face tracing rule: on arriving along dart t -> h, depart along h -> n where
  n is the successor of t in the rotation list at h (indices mod degree).
- Face-size multiset: the multiset {l_1,...,l_F} of face-walk lengths.
- Minimum-genus embedding: orientable cellular embedding attaining
  g = g_min(K(4,9)) = 4.

## Result

For K(4,9) at orientable minimum genus 4 (hence F = 17 faces), the complete
set S of face-size multisets realized by at least one orientable cellular
embedding is exactly:

S = { {4^15, 6^2}, {4^16, 8^1} }.

That is: every minimum-genus orientable embedding has either fifteen
4-faces and two 6-faces, or sixteen 4-faces and one 8-face; and each of
these two multisets is realized by an explicit verified genus-4 rotation
system. No other even face-size multiset satisfying the Euler count occurs.

## Proof and evidence

Exclusion (pure deduction). Every face walk is even by bipartiteness.
Length 2 is impossible in a rotation system of a simple graph with minimum
degree at least 2: at head h, the successor of the incoming edge in a cyclic
order of length >= 2 is a different edge, so no face walk is x -> y -> x,
and parallel-edge 2-faces are absent. Hence every face has even length at
least 4. With F = 17 faces of lengths l_i:

sum l_i = 2E = 72, and sum (l_i - 4) = 72 - 68 = 4.

Each excess e_i = l_i - 4 is even and nonneg. Partitions of 4 into even
parts are 4 and 2+2. Therefore the only even multisets of 17 integers each
at least 4 summing to 72 are A = {4^15,6^2} (excesses 2+2) and
B = {4^16,8^1} (excess 4). An all-quadrangular embedding would need F = 18
and genus 3.5, impossible; any face of length >= 10 has excess >= 6 > 4,
impossible. So S is a subset of {A, B} unconditionally.

Realizability (verified witnesses). Two explicit rotation systems on
U = {0,1,2,3}, W = {4,...,12} are given in full below and in
output/artifacts/witnesses.json:

Witness A ({4^15,6^2}): rotations 0:[10,7,11,9,6,5,4,8,12],
1:[7,5,6,10,4,9,11,12,8], 2:[6,12,9,4,5,11,8,7,10],
3:[10,12,6,9,11,5,7,8,4], 4:[1,3,0,2], 5:[1,3,2,0], 6:[1,0,3,2],
7:[1,0,2,3], 8:[0,3,2,1], 9:[0,1,2,3], 10:[0,3,1,2], 11:[0,2,3,1],
12:[0,1,2,3]. Face walks include fifteen 4-cycles and two 6-cycles
(11-2-8-1-7-0-11 and 1-12-2-9-3-11-1); F = 17, g = 4.

Witness B ({4^16,8^1}): rotations 0:[10,12,6,11,4,8,9,7,5],
1:[10,7,6,12,9,8,4,11,5], 2:[11,6,4,8,10,5,7,9,12],
3:[8,4,6,7,9,5,11,12,10], 4:[3,0,1,2], 5:[1,3,0,2], 6:[3,2,0,1],
7:[3,1,2,0], 8:[0,3,2,1], 9:[1,2,3,0], 10:[3,0,1,2], 11:[2,3,1,0],
12:[1,0,3,2]. Face walks include sixteen 4-cycles and one 8-cycle
(5-0-10-1-7-2-9-3-5); F = 17, g = 4.

Both were verified with output/artifacts/verify.py, which checks rotation
domains, partition of the 72 directed edges into face walks each used once,
Euler genus, face-length sum 72, and evenness/girth (each length even,
at least 4). The auditor independently re-executed the verifier: A gives
F = 17, g = 4, sorted lengths [4x15,6,6]; B gives F = 17, g = 4,
[4x16,8]. Section 3 is pure deduction; face tracing is computed evidence
re-verifiable by hand or script under the stated successor convention.

## Limitations

Classification is over orientable cellular embeddings only, not
nonorientable embeddings. The minimum-genus value g = 4 uses the standard
Ringel orientable-genus formula for complete bipartite graphs. Face tracing
uses the successor convention fixed above and in verify.py.

## Reproducibility

- output/artifacts/witnesses.json: both rotation systems (machine-readable).
- output/artifacts/verify.py: independent checker reporting F, g, sorted
  face lengths, and every face walk.
- DRAFT rotation tables match witnesses.json; listed face walks alternate
  across the bipartition. Run the verifier's verify() function on each
  stored rotation system to reproduce F = 17, g = 4, and the two multisets.

## References

- Ringel orientable genus formula for K_{m,n} (standard; gives g = 4 here).
- T. Sun, Face distributions of embeddings of complete graphs,
  arXiv:1708.02092 (complete graphs K_n; nearest face-distribution work,
  different graph family).
- G. A. Jones, Regular embeddings of complete bipartite graphs:
  classification and enumeration (regular/balanced case only).
- Z. Shao, Y. Liu, Z. Li, On the number of genus embeddings of complete
  bipartite graphs (counts, not face-multiset classification).
- M. Conder and K. Stokes, New methods for finding minimum genus embeddings
  (genus-finding methods).
