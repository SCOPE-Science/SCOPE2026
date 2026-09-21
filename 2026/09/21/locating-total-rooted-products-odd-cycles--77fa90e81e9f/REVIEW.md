# Same-model review

## Correctness

**PASS.** The proof was checked independently at the level of its mathematical implications.

For the lower bound, the total-domination constraints contributed by the nonroot vertices of one \(C_{4k+1}\) copy form the vertex-cover constraints of a path on \(4k+1\) vertices. Its cover number is \(2k\), and because the path has odd order its minimum vertex cover is unique. Translating that unique cover back to the cycle gives exactly the claimed low pattern, with the root and both cycle-neighbors of the root absent.

This uniqueness is the essential point: any copy that differs from the low pattern costs at least \(2k+1\). If \(A\) is the set of such copies and \(R\) is the set of selected roots, then \(R\subseteq A\). A root belonging to a low copy has selected-neighbor signature precisely \(N_H(v)\cap R\). Total domination makes these signatures nonempty; the locating condition makes them pairwise distinct. Therefore \(A\) is a locating-dominating set of the base graph, giving the lower bound \(2k|V(H)|+\gamma_L(H)\).

For the upper bound, the low and high periodic patterns were checked vertex by vertex. Every selected vertex has a selected neighbor; every unselected nonroot vertex has a unique singleton signature using a selected nonroot cycle vertex; and unselected roots have exactly the signatures supplied by a locating-dominating set of the base graph. Root and nonroot signatures use disjoint types of selected vertices, preventing cross-type collisions. The construction therefore attains the lower bound.

As supplementary evidence, exact 0-1 optimization agrees with the theorem on all 62 products obtained from connected Graph Atlas base graphs of order at most five and rooted cycles \(C_5,C_9\). It also gives \(\gamma_t^L(P_{10}\odot C_5)=24\).

## Originality

**PASS, to the best of our knowledge.** The closest primary source is Wei, Ahmad, Hameed and Hanif (2020), Theorem 9. For \(q_1\equiv1\pmod4\), it states
\[
\gamma_t^L(P_{q_2}\odot C_{q_1})
=
q_2\gamma_t^L(C_{q_1-1})+\frac{q_2}{2},
\]
which differs from the theorem in this record. In particular, \(P_{10}\odot C_5\) is predicted there to have value \(25\), while the exact value here is \(24\).

Searches were performed using both rooted-product and synonymous comb-product terminology, together with locating-total and location-total terminology. No published correction of the \(1\pmod4\) case and no general formula
\[
\gamma_t^L(H\odot C_{4k+1})=2k|V(H)|+\gamma_L(H)
\]
was located. Pribadi and Saputro (2020) give a general result for **ordinary locating domination** of comb products, which is a distinct parameter. Raza et al. (2021) study locating-total domination for other cycle-related and rotationally symmetric graphs, not this rooted-product identity.

The principal residual originality risk is a result indexed under different domination/product terminology or a correction not surfaced by the searches used here.

## Value

**PASS.** The result is not merely a rounding correction. It replaces the erroneous path formula by an exact theorem for every connected base graph, and shows that the extra cost beyond \(2k|V(H)|\) is exactly the ordinary locating-domination number of \(H\). This gives both a conceptual mechanism and a direct transfer between two domination parameters.

## Limitations

The theorem addresses only the \(4k+1\) cycle class. It does not reprove or refute the remaining congruence cases in the 2020 source, and it does not evaluate \(\gamma_L(H)\) for arbitrary \(H\). The finite computations are supplementary.

**Same-model review: passed. Independent audit: not yet performed.**
