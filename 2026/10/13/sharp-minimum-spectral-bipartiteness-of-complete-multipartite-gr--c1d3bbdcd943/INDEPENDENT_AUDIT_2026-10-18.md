# Independent mathematical audit

## correctness

PASS

For fixed N≥r≥3 and complete r-partite K_{n1,…,nr} with positive part sizes, the equitable symmetric quotient B=uu^T−diag(n_i), u_i=√n_i, has nonzero adjacency spectrum θ1>0>θ2≥…≥θr, and N−r further zeros. Arrange n1≤…≤nr. Rank-one interlacing implies θ_{j+1}≤−n_j for j=1,…,r−1. Because tr B=0, θ1+θr=−Σ_{j=2}^{r−1}θj≥Σ_{j=1}^{r−2}n_j≥r−2. Equality forces those small parts singleton and θ2,…,θ_{r−1}=−1. The −1 eigenspace has dimension precisely (# singleton parts−1) (including all-singleton case), forcing r−1 singleton parts. Conversely the complete split quotient has −1 with multiplicity r−2 and the remaining two eigenvalues solve z²−(r−2)z−(r−1)(N−r+1)=0, giving exact equality. r=2 is excluded because any biclique has zero. New independent spectral diagonalization sampled 647 positive multipartitions and 60 equality cases, not an all-parameter proof.

## originality

PASS

The exact extremal functional is λ_max+λ_min, not spectral radius/energy alone. Stevanović–Gutman–Rehman (2015) give unique complete-split minimization for spectral radius and energy among fixed-N fixed-r complete multipartite graphs; their result alone does not constrain a jointly varying least eigenvalue enough to force this same extremum of the sum. Abiad–Kumar–Pragada arXiv:2609.00210 prove upper-extremal spectral-bipartiteness bounds in much broader clique-free settings, not this fixed-multipartite lower problem. No implication-equivalent statement located in checked relevant Resultary searches; residual risk of terminology/index-plus-least adjacency eigenvalue.

## value

PASS

The spectral sum λ1+λN is an explicit measure of deviation from adjacency bipartiteness, and complete multipartite graphs form a canonical extremal model. A sharp fixed-order-and-part-count minimum with a unique split extremizer clarifies the cost of a persistent K_r and gives exact normalized scaling (r−2)/N. The proof needs spectral interlacing and a nontrivial equality multiplicity argument, not a routine table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
