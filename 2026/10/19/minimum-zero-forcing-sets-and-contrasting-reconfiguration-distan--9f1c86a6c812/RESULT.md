# Minimum zero forcing sets and contrasting reconfiguration distances in the Pappus graph

## Finding

The **token-jumping graph of the minimum zero-forcing sets of the Pappus graph** has 6,912 vertices and 97,524 edges. It is connected, and every vertex has eccentricity seven. Thus unrestricted one-for-one exchanges make this graph self-centered. For comparison, the token-sliding graph on the same set of configurations is connected with radius sixteen, diameter eighteen, and three eccentricity classes. The minimum-set count and the token-sliding calculation are exact comparison data already given in [2], not distinct contributions here. The result under consideration is the exact jump graph census and the resulting jump-versus-slide distance contrast.

## Assumptions and scope

Use the biaffine model of the Pappus graph \(P\): point vertices \(p_{x,y}\) and line vertices \(\ell_{m,b}\), for \(x,y,m,b\in\mathbb F_3\), are adjacent precisely when \(y=mx+b\). This is a simple undirected incidence graph with 18 vertices, 27 edges, and degree three. Starting from a set of blue vertices, a blue vertex with exactly one white neighbor can turn that neighbor blue. A set is zero forcing if it can color the whole graph blue. Equivalently one can apply all available forces in rounds: a legal force remains legal or its target has already turned blue.

The configurations are unordered minimum zero-forcing sets. A jump replaces one selected vertex by an arbitrary unselected vertex; a slide additionally requires the departing and arriving vertices to be incident in \(P\). Both endpoints of each step must be minimum forcing sets. Distance is shortest-path distance with the chosen move rule.

## Proof

**Complete census of states.** Generate the graph from the displayed incidence equation. Apply the color-change rule to every subset of sizes one through seven (the empty set does not force). There are no forcing sets of sizes below seven, and exactly 6,912 of size seven. They consist of 3,456 sets with three points and four lines and 3,456 with four points and three lines. This reconstructs the entire jump state space, not just example optima. The minimum seven and total 6,912 agree with [2].

**Complete census of moves.** For each optimal set \(B\), and each pair \(u\in B\), \(v\notin B\), include the move exactly when \((B\setminus\{u\})\cup\{v\}\) occurs in the complete list. Each undirected jump is then generated twice, once from each endpoint. This gives 97,524 edges. Mark a move as a slide exactly when \(u\sim v\) in \(P\); the 10,962 slides agree with [2].

**Distances.** A breadth-first traversal of the jump graph from each one of its 6,912 roots reaches all 6,912 vertices and has maximum distance seven. On the slide graph, full traversals reach all states and give eccentricities 16, 17 and 18 with multiplicities 648, 4,968 and 1,296, respectively. These latter data are the comparison with [2].

**Orbit check.** An independently indexed calculation constructs a group of 216 incidence automorphisms and checks preservation of all base edges. This action preserves both zero forcing and the move rules. There are 35 orbits on the optimal seed sets. Weighting the eccentricity of a root in each orbit by the orbit size reproduces both full distance distributions. This orbit calculation is a check on the finite enumeration; it is not a claim about the automorphism groups of the reconfiguration graphs themselves.

## Verification

The bundled standalone programs use exact combinatorial tests. The C++ program exhausts the state and move lists and performs all-root breadth-first search. The Python program uses another indexing, checks the automorphisms and computes distances from representatives of every orbit. To reproduce from the directory containing `verification/`, run:

```sh
g++ -O3 -std=c++17 verification/verify_pappus_cpp.cpp -o verify_pappus_cpp
./verify_pappus_cpp
python3 verification/verify_pappus_python.py
```

The expected outputs are `verification/cpp_output.txt` and `verification/py_output.txt`. The computations prove the stated finite result only, not a theorem for other incidence graphs.

## Relationship to other results

Geneson, Haas and Hogben [1] use exactly the jump rule above in their general definition of the reconfiguration graph of minimum zero-forcing sets. Their framework does not supply the Pappus jump edge count or distances in the text compared here. The exact indexed Pappus slide and seed results of [2] are not treated as new: [2] gives \(Z(P)=7\), the 6,912 states, 10,962 slide edges, connectedness, radius 16, diameter 18 and the same three slide eccentricity classes. Those statements do not determine the distances after arbitrary replacements are permitted. The added exact information is that every optimum in the jump graph has a farthest state at distance exactly seven. The comparison of scientific content makes no claim about who obtained the shared calculations first. Other unindexed or supplementary calculations may contain the same jump result.

## References

1. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, [arXiv:2009.00220](https://arxiv.org/abs/2009.00220).
2. *Local zero-forcing mobility separates the Pappus and Desargues incidence graphs*, Resultary, [exact finite classification theorem](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-local-zero-forcing-mobility-separates-the-pappus-and-desargues-i--c9fe15cd9378/RESULT.md).
3. A. E. Brouwer, [Pappus graph](https://aeb.win.tue.nl/drg/graphs/Pappus.html), for the incidence model and the group order.
