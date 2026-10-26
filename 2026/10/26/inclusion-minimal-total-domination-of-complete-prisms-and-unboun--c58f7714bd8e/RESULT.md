# Inclusion-minimal total domination of complete prisms and unbounded gaps

## Finding

For every integer \(n\ge 2\), let \(G_n=K_n\mathbin{\square}K_2\), with two indexed clique layers \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\) and matching edges \(u_iv_i\). The complete family of inclusion-minimal total dominating sets of \(G_n\) is:

1. The \(n\) matched pairs \(\{u_i,v_i\}\).
2. The two full clique layers \(U\) and \(V\).
3. The four-vertex sets \(\{u_i,u_j,v_k,v_\ell\}\) with four pairwise distinct indices \(i,j,k,\ell\).

Consequently, the polynomial enumerating *inclusion-minimal* total dominating sets by their cardinality is
\[
M_t(G_n;z)=nz^2+6\binom n4z^4+2z^n.
\]
For \(n=2\) or \(n=4\), equal-degree terms are added; \(\binom n4=0\) when \(n<4\). Thus the upper total domination number is \(2\) if \(n=2\), \(3\) if \(n=3\), and \(\max\{4,n\}\) if \(n\ge4\). For \(n\ge6\), the set of occurring cardinalities is precisely \(\{2,4,n\}\), leaving \(n-5\) consecutive unattained values \(5,6,\ldots,n-1\). Therefore arbitrarily long gaps occur even in connected, vertex-transitive, diameter-two, \(n\)-regular graphs.

## Assumptions and scope

Graphs are finite and simple. A total dominating set \(D\subseteq V(G)\) satisfies \(N_G(v)\cap D\ne\varnothing\) for every vertex \(v\), *including selected vertices*. It is inclusion-minimal if no proper subset remains totally dominating. Because total domination is upward closed, it is enough to test deletion of a single selected vertex. A maximum inclusion-minimal set is not the same as a minimum total dominating set. All vertices are distinguished; the two layers and matching labels fix the counting convention.

## Proof

Write \(A=\{i:u_i\in D\}\), \(B=\{i:v_i\in D\}\), and \(a=|A|\), \(b=|B|\). For every index \(i\), the counts of neighbors of the two vertices inside \(D\) are exactly
\[
|N(u_i)\cap D|=a-\mathbf1_{i\in A}+\mathbf1_{i\in B},\qquad
|N(v_i)\cap D|=b-\mathbf1_{i\in B}+\mathbf1_{i\in A}.
\]
Therefore the upper layer is entirely totally dominated exactly when either \(a\ge2\), or \(a=1\) and the unique member of \(A\) also belongs to \(B\), or \(a=0\) and \(B=[n]\). The analogous criterion for the lower layer interchanges \(A,B\). These conditions are necessary and sufficient for \(D\) to be a total dominating set.

If \(a=0\), the criterion forces \(B=[n]\); this full layer is inclusion-minimal, because removing any \(v_i\) leaves \(u_i\) without a neighbor in the chosen set. The symmetric case \(b=0\) gives \(U\). If \(a=b=1\), the unique indices must coincide: these are precisely the matched pairs, each inclusion-minimal. If one of \(a,b\) equals one and the other exceeds one, the two sets share the singleton's index. Deleting all but that shared vertex from the larger layer leaves a strictly smaller total dominating matched pair; hence such a set is not inclusion-minimal.

Now assume \(a,b\ge2\). If \(a\ge3\), deletion of any chosen upper vertex leaves both layer counts at least two, so \(D\) is not inclusion-minimal. Similarly \(b\ge3\) is excluded. Thus \(a=b=2\). If \(A\cap B\ne\varnothing\), retain any index in the intersection as the unique selected upper index while keeping both bottom indices; the total-domination criterion remains satisfied, so deleting the other selected upper vertex proves nonminimality. Conversely, if \(A\cap B=\varnothing\), removing either top vertex leaves a top singleton not selected in the bottom layer, and removing either bottom vertex leaves a bottom singleton not selected in the top layer. Every deletion destroys total domination. Thus exactly the disjoint two-element index choices are inclusion-minimal.

Their number is \(\binom n2\binom{n-2}2=6\binom n4\), giving the polynomial. Its support and maximum exponent give the parameter and gap statements. Each vertex has its \(n-1\) same-layer neighbors and one matching neighbor, hence degree \(n\); any vertices in opposite layers with different indices have a two-edge path, proving diameter two. Simultaneous permutations of matching indices and interchange of layers act transitively on vertices.

## Verification

Run `python3 verify.py` (standard library only). The checker builds the original graph adjacency masks, tests the open-neighborhood definition on **every nonempty vertex subset** for \(2\le n\le10\), and compares the complete family of inclusion-minimal total dominating sets with the three predicted families, not merely their counts. It also verifies the coefficient formula and gap assertion for those instances. The recorded output is in `verify_output.txt`. These finite computations corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work

Brešar, Cornet, Dravec and Henning (first public preprint 11 October 2023) explicitly introduce the same graph as two copies of \(K_n\) joined by a perfect matching and state \(\gamma_t(G_n)=2\) while studying zero-forcing and total-domination bounds. That minimum does not determine inclusion-minimal sets of larger cardinalities, the entire enumerator, or the gap pattern. General literature treats upper total domination and Cartesian products, including Dorbec–Henning–Rall (2008), but accessible material does not establish this claimed complete classification. The general open-private-neighborhood criterion for inclusion-minimal total dominating sets predates this result; the contribution is its sharp specialization and full enumeration for these highly symmetric graphs.

## Limitations

This theorem applies to \(K_n\mathbin{\square}K_2\), not arbitrary Cartesian products or all vertex-transitive graphs. It counts inclusion-minimal sets, not all total dominating sets. The exact product-specific 2008 source was not accessible in full during the literature comparison; an unindexed equivalent or stronger prior classification cannot be excluded. No independent mathematical review has been performed.

## References

1. B. Brešar, M. G. Cornet, T. Dravec and M. A. Henning, *Bounds on zero forcing using (upper) total domination and minimum degree*, first public version 11 October 2023, arXiv:2310.07432v1, https://arxiv.org/abs/2310.07432.
2. M. Dorbec, M. A. Henning and D. F. Rall, *On the upper total domination number of Cartesian products of graphs*, Journal of Combinatorial Optimization (2008), DOI:10.1007/s10878-007-9099-8 (abstract only examined).
3. T. W. Haynes and M. A. Henning, *Nordhaus–Gaddum bounds for upper total domination* (2022), for contextual upper-total-domination bounds.
4. E. J. Cockayne and collaborators, foundational open-private-neighbor characterization of inclusion-minimal total dominating sets (as recalled in Haynes, Hedetniemi and Henning, *Domination in Graphs: Core Concepts*, 2023).
