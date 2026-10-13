# Self-review

## Correctness
**PASS.** In \(K_{n_1,\ldots,n_r}\), every outside vertex in part \(V_i\) has exactly \(s-d_i\) neighbors in a selected set with occupancies \(d_i\) and total size \(s\). The proper \(3\)-domination definition therefore becomes the exact occupancy criterion stated in RESULT.md. An exact-three witness leaves exactly three selected vertices outside one part; trimming the witness part proves that every existence instance has a witness of size at most \(6\). The cases \(s=3,4,5,6\) are then exhaustive and each converse construction satisfies the defining inequalities. Independent finite implementations in `verify.py` agree with the formula on all multipartite profiles through the declared ranges.

## Originality
**PASS.** The closest primary source is Chen–Cai, DOI 10.3390/math13121960. Its definition and complete-bipartite theorem were inspected directly. It proves the values for \(K_{3,n}\) and for bicliques with both shores at least \(4\), but no complete-multipartite theorem was found in its full text. Searches under the exact invariant name, proper-\(p\) aliases, the equivalent “\(3\)-dominating but not \(4\)-dominating” formulation, secondary-domination terminology, and complete-multipartite specialization found no statement implying the present classification. Broader complete-multipartite domination results inspected use different neighborhood inequalities and do not encode the required exact-three witness.

## Value
**PASS.** This is a natural exact graph-family classification for a recently introduced invariant. It extends the known complete-bipartite calculation to all complete multipartite graphs, closes the omitted small-shore biclique cases, gives exact nonexistence conditions, and isolates a reusable structural reduction that forces every finite value into \(\{3,4,5,6\}\). The initiating source itself identifies calculation of the parameter on further graph classes as a meaningful direction.

Closest literature: D. Chen and S. Cai, “Proper 3-Dominating Sets in Graphs,” *Mathematics* 13 (2025), 1960, DOI 10.3390/math13121960; P. Bednarz and M. Pirga, “On Proper 2-Dominating Sets in Graphs,” *Symmetry* 16 (2024), 296; A. P. Kazemi, “On the Total k-domination Number of Graphs,” *Discussiones Mathematicae Graph Theory* 32 (2012), 419–426.

Limitations: the theorem is specific to complete multipartite graphs and proper \(3\)-domination. A poorly indexed equivalent result under substantially different terminology remains a residual literature risk. Computation checks finite ranges only and is not used as an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
