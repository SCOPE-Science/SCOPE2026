# Mathematical review of the wheel acyclic-orientation degree distribution

## Correctness — PASS

The statement uses precisely the wheel \(K_1\vee C_m\), its acyclic orientations and legal single-edge reversals. The proof partitions configurations by their hub-spoke directions. For mixed spoke directions it proves the boundary-edge obstruction and independently identifies which internal path edges and spokes are reversible. The source polynomial of a directed path is counted by sign changes with two virtual end arrows, and the sum over cyclic run compositions gives the degree generating function. The separate constant-spoke cases include a necessary single-minority-rim-edge correction; excluding this correction would change the lowest coefficients. An explicit logarithmic generating function gives the Lucas-number count of minimum-degree configurations. The maximum is attained by alternating rim arrows for even rim lengths or one repeated direction for odd rim lengths, and the triangular smallest case is treated separately.

An independent directed-acyclicity/reachability implementation exhausts all wheel orientations with rim lengths \(3\) through \(8\). A separate path-run/composition implementation confirms the exact polynomial coefficients, extremal multiplicities, Lucas values and edge-count checksum through length \(12\). Neither finite range is treated as proof for all lengths; the combinatorial decomposition supplies that proof.

## Originality — PASS, with an explicit residual risk

Savage, Squire and West, *Gray Code Results for Acyclic Orientations* (1993), study exactly these wheel acyclic orientations and describe the forced rim edges and the \(3^m-3\) total. Those known results are credited, and their wheel section was examined in full. Their principal wheel results concern Hamiltonian traversals of the flip graph rather than its local-degree distribution. Grujić, *Counting faces of graphical zonotopes* (2016), supplies a general formula for global face counts; its full text was examined, and such global counts yield totals of vertices and edges rather than how many orientation states have any given number of reversible arcs. The equivalent descriptions by graphical-zonotope skeletons, graphic-arrangement chambers and acyclic-orientation graphs were also searched; no statement with this wheel degree polynomial or its Lucas simplification was located. Exact statements previously obtained for complete bipartite/split orientation spaces and wheel spanning-tree exchange spaces do not imply this claim because their underlying graph or state space differs.

**Residual risk:** An unindexed historical article or a result phrased in terms of chamber-wall multiplicities might already contain an equivalent formula. Searches are not an absolute novelty proof. No independent external scholarly audit has been performed.

## Mathematical value — PASS

The 1993 wheel flip-graph setting naturally asks for branching degrees at each state, rather than only the total state count and existence of Hamiltonian paths. The all-parameter polynomial determines every degree multiplicity and sharp extremal multiplicities; its exact Lucas simplification counts simple vertices in the wheel graphical zonotope and demonstrates an exponentially diminishing simple fraction. These are intrinsic structural statistics of a canonical infinite family, and the refinement is not obtained merely by substituting wheel parameters into the known global face-count formula.

## Reproducibility and boundaries

`verify_direct.py` performs a full labelled-orientation/reachability census for \(3\le m\le8\). `verify_formula.py` constructs the run-composition model and checks the closed polynomial for \(3\le m\le12\). Both scripts use only Python's standard library. The theorem treats ordinary acyclic orientations and single directed-edge flips; no claim is made for source/sink reversals or other reconfiguration moves. Computations are finite checks. The complete all-length argument is in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
