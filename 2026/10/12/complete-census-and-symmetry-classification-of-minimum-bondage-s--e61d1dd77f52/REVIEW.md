# Independent mathematical audit

## correctness

PASS

The fixed source list has 24 cubic vertices and 36 edges. Independent compiled C++ with a direct closed-neighborhood algorithm enumerated all C(24,6)+C(24,7)=480700 candidate small dominating sets (none), 1767 size-eight dominators, every C(36,4)=58905 four-edge deletion (minimum 5 surviving eight-sets), and all C(36,5)=376992 five-edge deletions: exactly 276 kill every size-eight dominator. Each winner contains at least one entire three-edge incident vertex star; 36 winners have two, every vertex has exactly 13 extensions. Separately constructed networkx graph automorphisms (48) and their action on all 276 independently determined eight orbits 12,24,24,24,48,48,48,48 and all claimed representatives. Checked all eight printed nine-vertex domination witnesses by recomputing the surviving edges; the orbit action transports each witness, giving γ(T-F)=9 for every winner. This is an exhaustive finite certificate, not a sampling argument.

## originality

PASS

Srivastava, arxiv:2609.02477v1 Theorem 1, proves only γ(T)=8 and b(T)=5 by one five-edge witness and exhaustive absence of four-edge winners. Its full text gives exactly 1767 domination-eight sets, but nowhere counts all 276 five-edge minima nor specifies eight symmetry orbits, thirteen local extensions or a universal post-deletion γ=9. Those extra natural equality-case assertions are not logical consequences of scalar bondage number five. Nearby Resultary findings on the same truncated octahedron compute unrelated independence complexes, not bondage-minimizer census.

## value

PASS

The complete sensitivity/fault-set classification of the smallest currently exhibited cubic planar counterexample to the planar bondage conjecture is a natural graph invariant. A compulsory full vertex star and eight orbits explain the structure and abundance of extremal destructive edge sets; the result is more than repeating b(T)=5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
