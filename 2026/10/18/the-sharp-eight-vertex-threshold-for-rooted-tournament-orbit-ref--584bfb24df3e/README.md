# Reproduce the finite rooted-tournament classification

The programs use only C++17 and Python 3 standard facilities. Run from the directory containing this file.

```sh
g++ -O3 -std=c++17 cpp/rooted_tournament_census.cpp -o /tmp/tournament_census
/tmp/tournament_census 8

g++ -O3 -std=c++17 cpp/independent_labelled_check.cpp -o /tmp/tournament_labelled
/tmp/tournament_labelled 7

python3 python/witness_crosscheck.py
```

Compare stdout with the three text files under `evidence/`. The canonical representative enumerator uses exact tournament isomorphism: vertex outdegree is an isomorphism invariant, so minimization over permutations in each degree block yields a complete canonical representation. At each order, extend every unrooted class representative by all possible incident arc orientations of the new root. This is a complete rooted-tournament search.

The labelled verifier tests every tournament word at each order, with root fixed at vertex 0; any other root can be moved to vertex 0 by a relabelling. The witness checker reconstructs the adjacency matrices independently and tests all root-fixing permutations. Stable refinement always retains the old colour; in/out counts are separately checked by the Python program. In the C++ algorithms, outgoing counts suffice because tournament incoming counts are obtained by subtracting outgoing counts and self-membership from each colour-class size.

The word `22066` represents the induced seven-vertex regular tournament with pairs in standard upper-triangle order, and `85042`/`220421234` represent the two eight-vertex rooted extensions with root vertex 7.

No source papers are included; consult the cited external literature separately.
