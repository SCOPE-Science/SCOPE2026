# Exact lattice volume loss under matching deletions in type-A root polytopes

## Finding

For integers \(n\ge3\) and \(0\le r\le\lfloor n/2\rfloor\), let \(M\) be an arbitrary matching of \(r\) edges of the complete graph \(K_n\). Write \(G=K_n\setminus M\). In the ambient hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), define the symmetric edge polytope

\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G)\}.
\]

Its normalized lattice volume, with respect to \(A_{n-1}=H\cap\mathbb Z^n\), satisfies the exact formula

\[
\boxed{\operatorname{Vol}_{A_{n-1}}(P_G)=\binom{2n-2}{n-1}-r\,2^{n-2}.}
\]

In particular, a single deleted graph edge removes precisely \(2^{n-2}\) units of normalized lattice volume, and the losses from pairwise disjoint deleted edges are additive. Each removed oriented-root cap is a lattice pyramid with a crosspolytopal base and normalized lattice volume \(2^{n-3}\). By the indecomposability classification of Higashitani and Mori, for \(n\ge5\) every nonempty matching deletion also changes the polytope from Minkowski decomposable to Minkowski indecomposable. The relative volume loss from one edge is exactly \(2^{n-2}/\binom{2n-2}{n-1}\), asymptotic to \(\sqrt{\pi(n-1)}/2^n\).

## Assumptions and scope

The matching has pairwise disjoint endpoints, all edges have the standard unweighted type-A root realization, and the ambient lattice is the full root lattice \(A_{n-1}\). Normalized volume in lattice dimension \(d\) is \(d!\) times coordinate Euclidean volume after identifying a lattice basis with \(\mathbb Z^d\). This formula does not assert additive losses for nonmatching (intersecting) graph-edge deletions or characterize arbitrary graph deletions.

## Proof

**Step 1: full root-polytope volume.** Let \(\Delta=\operatorname{conv}\{e_1,\ldots,e_n\}\). Then \(P_{K_n}=\Delta-\Delta\). In the basis \(e_i-e_n\) for \(1\le i\le n-1\), its coordinate description is

\[
P_{K_n}=\bigl\{x\in\mathbb R^{n-1}:\sum_i\max(x_i,0)\le1,\ \sum_i\max(-x_i,0)\le1\bigr\}.
\]

Put \(d=n-1\). In each orthant with \(k\) nonnegative coordinates, the polytope is the product of a \(k\)-simplex and a \((d-k)\)-simplex of respective coordinate volumes \(1/k!\) and \(1/(d-k)!\). The orthants meet along lower-dimensional boundaries. Thus

\[
\operatorname{Vol}_{A_{n-1}}(P_{K_n})
=d!\sum_{k=0}^d\binom dk\frac1{k!(d-k)!}
=\sum_{k=0}^d\binom dk^2=\binom{2d}{d}.
\]

**Step 2: one oriented-root cap.** Fix distinct indices \(a,b\), set \(u=e_a-e_b\), and define the primitive integral linear functional \(h_{ab}(x)=x_a-x_b\) on \(A_{n-1}\). On the roots of \(P_{K_n}\), its maximum \(2\) occurs uniquely at \(u\); its value is \(1\) exactly at the \(2(n-2)\) roots \(e_a-e_j\) and \(e_j-e_b\) for \(j\ne a,b\). We claim

\[
P_{K_n}\cap\{h_{ab}\ge1\}
=\operatorname{conv}\bigl(\{u\}\cup\{e_a-e_j,e_j-e_b:j\ne a,b\}\bigr).
\]

To see this without assuming an edge graph, let \(x\in P_{K_n}\) have \(h_{ab}(x)>1\), and let \(\tau=h_{ab}(x)-1\). Since each positive and negative coordinate mass is at most \(1\), we have \(x_a\ge\tau\) and \(-x_b\ge\tau\). Therefore \(y=(x-\tau u)/(1-\tau)\) lies in \(P_{K_n}\cap\{h_{ab}=1\}\) for \(\tau<1\), with the case \(\tau=1\) giving \(x=u\). If \(h_{ab}(y)=1\), then \(y_a\ge0\), \(y_b\le0\), and writing \(p=y_a\), \(1-p=-y_b\), the remaining coordinates have total positive mass at most \(1-p\) and negative mass at most \(p\). Because their total sum is \(1-2p\), there exist nonnegative coefficients \(\lambda_j,\mu_j\) such that \(\sum_{j\ne a,b}\lambda_j=p\), \(\sum_{j\ne a,b}\mu_j=1-p\), and \(y_j=\mu_j-\lambda_j\). Hence \(y=\sum_j\lambda_j(e_a-e_j)+\sum_j\mu_j(e_j-e_b)\). The asserted pyramid description follows. (For \(n\ge3\), at least one other index is present to receive equal slack.)

**Step 3: exact cap volume.** The pyramid's base \(B_{ab}\) lies in \(h_{ab}=1\) and is centered at \(u/2\). Writing \(v_j=(e_a+e_b)/2-e_j\), for \(j\ne a,b\), its base is the \((n-2)\)-dimensional crosspolytope

\[
B_{ab}=\frac u2+\operatorname{conv}\{\pm v_j:j\ne a,b\}.
\]

By permuting indices set \(a=1\), \(b=2\), and \(k=n\). The rank-\((n-2)\) lattice of directions of the base, \(\Lambda_0=A_{n-1}\cap\ker h_{12}\), has basis \(w=e_1+e_2-2e_n\), together with \(e_j-e_n\) for \(3\le j\le n-1\). In this basis \(v_n=w/2\) and \(v_j=w/2-(e_j-e_n)\) for \(3\le j\le n-1\). The absolute determinant of the \(n-2\) vectors \(v_j\) is exactly \(1/2\). The standard crosspolytope volume formula therefore gives normalized base volume \(2^{n-2}\cdot(1/2)=2^{n-3}\). As \(h_{ab}\) is primitive on \(A_{n-1}\), the apex \(u\) has lattice height \(1\) over \(h_{ab}=1\). The normalized full-dimensional pyramid volume is also \(2^{n-3}\). Its opposite oriented cap has the same volume.

**Step 4: disjoint matching caps and exact remaining vertices.** For disjoint edges \(\{a,b\},\{c,d\}\), every root \(e_i-e_j\) satisfies \(\pm h_{ab}(e_i-e_j)\pm h_{cd}(e_i-e_j)\le2\), for any independent choice of the two signs: the coefficient vector has entries in \(\{-1,0,1\}\), and any coordinate difference is at most \(2\). Convexity extends this inequality to all of \(P_{K_n}\). Consequently no point can lie in the interiors of two removed caps (where each of the corresponding signed functionals exceeds \(1\)). Moreover, the one-cap description shows that cutting at \(h_{ab}=1\) creates no new vertex: every boundary vertex already belongs to the original root set. For disjoint pairs, all other cap planes have values at most \(1\) on these retained vertices, and their open caps are pairwise disjoint. Intersecting the supporting halfspaces therefore leaves exactly the convex hull of the roots whose unoriented graph edges are outside \(M\), namely \(P_G\). Subtracting \(2r\) cap volumes \(2^{n-3}\) from the full volume in Step 1 gives

\[
\operatorname{Vol}_{A_{n-1}}(P_G)=\binom{2n-2}{n-1}-r2^{n-2}.
\]

**Step 5: qualitative jump in Minkowski decomposability.** Higashitani--Mori's classification identifies the decomposable symmetric-edge cases as \(K_n\), \(K_{2,n-2}\), and \(K_{1,1,n-2}\). When \(n\ge5\) and \(M\ne\varnothing\) is a matching, \(K_n\setminus M\) belongs to none of these three graph families, hence its symmetric edge polytope is indecomposable. Stirling's central-binomial asymptotic gives the stated exponentially small relative volume loss for one deleted edge.

## Verification

The accompanying `verify.py` uses only the Python standard library and independently computes the lattice determinant for each crosspolytope base in a canonical root-lattice basis, checks the exact factorial/binomial identities and all signed functional cap-disjointness inequalities on the original root vertices for finite parameter ranges. It is run as `python3 verify.py`. A separate convex-hull calculation in floating-point coordinates was also performed for all allowed matchings of canonical form with \(3\le n\le8\), matching the exact normalized-volume formula; this last observation is a finite sanity check, not an infinite proof. The general theorem follows from the exact geometric argument above.

## Relationship to prior work

The 2026 paper by Higashitani and Mori establishes the general Minkowski decomposability classification, which is used only for the qualitative corollary; it does not state the matching-deletion volume formula. D'Alì, Delucchi, and Michałek (2022), *Many faces of symmetric edge polytopes*, develops the symmetric-edge model, graph constructions, triangulations, and volume formulas for trees, cycles, wheels, and bipartite outerplanar graphs. Those displayed formulas and constructions do not include the complete graph after arbitrary matching deletions. The present exact additive cut-volume identity is derived independently here. The general complete-graph central binomial volume is classical and not claimed as new.

## Limitations

The claim is restricted to disjoint graph-edge deletions, and does not classify interacting deletions, full Ehrhart numerators, or higher-dimensional Minkowski sums. Existing general methods for computing symmetric-edge volumes may also recover these volumes, even though the consulted theorem statements do not give this particular closed form. Priority against all literature is not certified, and independent validation has not been performed.

## References

1. A. Higashitani and A. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445, first submitted August 3, 2026; https://arxiv.org/abs/2608.02445.
2. A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, Electron. J. Combin. 29(3) (2022), P3.24; https://doi.org/10.37236/10387.
