# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The lower bound is a direct specialization of the Erdős--Faudree--Ordman crossing-edge inequality with crossing count `h^2rs` and internal counts `h*C(r,2)` and `h*C(s,2)`.  The covering-number argument is exact because selected representatives induce `K_{h,h}` and every clique meets at most one selected vertex on each side.

The upper construction was checked adversarially for all parity combinations.  Optimal edge-colorings of complete graphs give matching classes of sizes `q/2` for even `q` and `(q-1)/2` for odd `q`; hence for `r<=s` the `K_r` class can be injected into the corresponding `K_s` class.  The condition `h>=chi'(K_s)` ensures distinct color offsets use distinct ordered cluster pairs.  Within one cluster pair, matching structure prevents crossing-edge repetition among K4s; unpaired larger-side matching edges form triangles through a fixed smaller-side vertex, and their B-endpoints are disjoint from paired edges, so they do not repeat K4 crossing edges.  The count then matches the lower bound exactly.

A standalone verifier reconstructs the partition and checks every graph edge has multiplicity one for 90 parameter cases with `2<=r<=s<=10` and `h` equal to `chi'(K_s)` or one larger.  This is supporting evidence only; the proof is general.

## Originality

Status: PASS, to the best of our knowledge.

The most directly relevant current source is Ning (2026), arXiv:2608.11536.  Its Proposition 3.1 treats only the symmetric family `(hK_k)∨(hK_k)` with even `k` and `h>=k-1`, using a one-factorization.  It does not state an unequal-cluster formula and does not cover odd `k` in that proposition.

The primary Erdős--Faudree--Ordman paper (1988) was inspected around its two-sided crossing-edge Lemma 4 and examples.  It proves the lower bound used here and studies graphs with internal edges on both sides, including a clique joined to several cliques, but the displayed examples give lower bounds rather than the exact two-parameter family above.

The Caccetta--Erdős--Ordman--Pullman paper (1985) was inspected around its preliminary exact theorem and special constructions.  Its theorem for a graph joined to a sufficiently large independent set covers the boundary `r=1`; accordingly no originality is claimed there.  Its special constructions include joins involving cluster graphs and independent sets, but no exact formula matching the present `r,s>=2` family was located.

Searches using the equivalent phrases `clique partition`, `edge clique partition`, `join of disjoint unions of cliques`, `joined cluster graphs`, `cograph join`, and the explicit forms `hK_r`, `hK_s`, and `hK_k` did not locate a prior statement of the asymmetric exact formula or the odd symmetric extension.  The principal residual originality risk is the breadth and age of the clique-partition literature: an equivalent edge-decomposition construction may exist under different notation or set-representation terminology.  No specific inaccessible source was found that materially suggested coverage of the theorem.

## Value

Status: PASS.

The result exactly determines both classical clique parameters on a natural two-parameter extension of the construction responsible for the new `Theta(n^{4/3})` extremal bound.  It identifies a general sharpness mechanism for the Erdős--Faudree--Ordman inequality, removes the parity restriction in the symmetric case, and shows how K4 packing and triangle packing coexist in the asymmetric case.  This is more than a numerical parameter check: it gives a reusable decomposition principle and a closed formula for an infinite family.

## Limitations

The hypothesis `h>=chi'(K_s)` is sufficient and is not claimed necessary.  The numbers of clusters on the two sides are equal; unequal cluster counts are not resolved here.  The `r=1` boundary is old.  Finite verification checks the explicit construction, not originality or the general lower bound.  No independent validation or independent audit is asserted.
