# Independent mathematical audit

## correctness

PASS

The Singer difference-set incidence yields column weights 9 and pairwise intersection 6 for A, hence A^T A=I and H=[I|A] is a full-rank parity check and generator. The independent replay enumerates the 8,192 codewords, checks minimum distance 6, and xors each of the 83,682 distinct coordinate subsets of weights 0 through 5. They reach all 8,192 syndromes; first-hit weight and number of minimum-weight subsets reproduce all joint counts. In particular the distance counts are (1,26,325,2080,3770,1990), so covering radius is exactly 5, and the weighted sum is 31946, giving 15973/4096. Repeated-coordinate paths are not counted: alternatively each shortest Cayley path uses distinct coordinates and each minimum subset yields precisely d! such paths. The point-preserving permutations act faithfully on the syndromes, preserve the line-column set and generate a group of size 5616. The involution AR exchanges e_i with A_(.,-i) and induces a code automorphism. The two disjoint coordinate-block cosets give at least 11232 elements, which is the full-group order by Höhn. The independent orbit replay verifies all 22 rows, including the five depth-five (size, leader count) pairs (936,18), (702,18), (234,18), (117,10), (1,26), and singleton syndrome 8191. The stored and reproduced CSV SHA-256 is 8d8acd1b504b47d31e62dc0b9b4ebcb62048e9cc845561312ce678ce55279790. Replay with python3 /workspace/branches/df660689-3bb2-49e8-8d07-ffb023b0ed89/independent_check.py. The uploaded verifier was inspected, not run. Uniqueness up to coordinate permutation is imported from the classification, not proved by enumerating this one code.

## originality

PASS

Prior sources give the code, its uniqueness and full group, and its codeword weight enumerator. The supported increment is the exact length-26 coset minimum-distance and minimum-leader multiplicity census and its full automorphism orbit table, not any of those inputs. Comparable decoding and coset-orbit results for other objects do not state these data.

## value

PASS

This is a natural, complete nearest-decoding and symmetry invariant of the unique extremal self-dual code at its length, not an arbitrary chosen subset of syndromes. The 1990 deepest cosets split into five different symmetry types, with exact tie sizes including a full-group-fixed exceptional coset. Those distinctions supply data for decoding and comparisons of symmetry classes that the established weight enumerator and group order do not provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
