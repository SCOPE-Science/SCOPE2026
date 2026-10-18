# Complete overlap is the sharp coextinction-variance maximizer under fixed-count pollinator losses

## Finding
Consider a finite simple bipartite interaction graph with \(n\) plants and \(n\) pollinators, in which every species has degree \(d\). Assume \(d\ge 2\), \(d\mid n\), and \(n\ge 2d\). Remove a uniformly selected set of exactly \(m\) distinct pollinators, where \(0\le m\le n\). Declare a plant secondarily extinct exactly when all its pollinators have been removed, and write \(Z_G(m)\) for the number of secondarily extinct plants.

Define \(a_m=\binom{n-d}{m-d}/\binom{n}{m}\) and \(b_m=\binom{n-2d}{m-2d}/\binom{n}{m}\), using \(\binom{u}{v}=0\) whenever \(v<0\) or \(v>u\). Then every such graph satisfies the **sharp all-stage upper bound**

\[
\operatorname{Var}(Z_G(m))\le n d\,a_m+n(n-d)b_m-n^2a_m^2.
\]

At every *informative stage* \(d\le m\le n-2\), equality holds if and only if the graph is a disjoint union of \(n/d\) copies of the complete bipartite graph \(K_{d,d}\). The same union attains equality for every \(m\). Outside the informative range, the extinction count is deterministic for every admissible graph, so all variances vanish.

There is also an **exact overlap-defect identity**. Write \(N_i\) for plant \(i\)'s pollinator neighborhood, \(t_{ij}=|N_i\cap N_j|\), and for \(0\le t\le d\) set

\[
B_m(t)=\frac{\binom{n-2d+t}{m-2d+t}}{\binom nm},\qquad
\delta_m(t)=\left(1-\frac td\right)B_m(0)+\frac td B_m(d)-B_m(t).
\]

Then the difference between the displayed upper bound and the actual variance equals

\[
2\sum_{i<j}\delta_m(t_{ij}).
\]

For each informative stage, \(\delta_m(t)>0\) at every integer \(1\le t\le d-1\), while \(\delta_m(0)=\delta_m(d)=0\). Thus partial, rather than zero or complete, neighborhood overlap contributes a strictly positive and explicitly computable variance deficit. In particular, the deficit is at least \(2\delta_{\min}\) times the number of plant pairs with partial overlap, where \(\delta_{\min}=\min_{1\le t<d}\delta_m(t)>0\).

## Assumptions and scope
The network is binary, simple, balanced, and \(d\)-regular in both guilds. Disconnected networks are permitted because the sharp extremizer is a collection of modules. Primary losses are a uniformly random \(m\)-element subset *without replacement*, not independent Bernoulli losses. A plant's extinction is a one-step topological event, without ecological feedback, functional compensation, or within-guild dynamics. The claimed uniqueness is graph-isomorphism uniqueness and concerns only the informative stage range. The requirement \(d\mid n\) ensures that the equality graph exists; the inequality itself also holds for any \(n\ge 2d\) without divisibility, but equality at an informative stage is then impossible. Cases \(n=d\) and \(d=1\) are trivial and deliberately excluded from the nontrivial statement.

## Proof
Fix \(n,d,m\) in the stated range and let \(I_i\) indicate extinction of plant \(i\). Since each plant has \(d\) pollinators, \(\mathbb E I_i=a_m\). A pair with \(t_{ij}\) common neighbors has a combined neighborhood of size \(2d-t_{ij}\), and consequently

\[
\mathbb E[I_iI_j]=B_m(t_{ij}).
\]

Expanding the square of \(\sum_i I_i\) gives the **exact variance identity**

\[
\operatorname{Var}(Z_G(m))=n a_m+2\sum_{i<j}B_m(t_{ij})-n^2a_m^2.
\tag{1}
\]

Each pollinator has \(d\) plant neighbors. Double-counting pairs of plants sharing a pollinator yields

\[
\sum_{i<j}t_{ij}=n\binom d2=\frac{nd(d-1)}2.
\tag{2}
\]

Put \(s=n-m\). The sequence \(B_m(t)=\binom{n-2d+t}{s}/\binom ns\) is discrete convex in integer \(t\), because Pascal's identity yields

\[
B_m(t+2)-2B_m(t+1)+B_m(t)=
\frac{\binom{n-2d+t}{s-2}}{\binom ns}\ge0,
\]

where out-of-range binomial coefficients equal zero. Every point of a convex finite sequence lies at or below the chord joining its endpoints, so

\[
B_m(t)\le\left(1-\frac td\right)B_m(0)+\frac td B_m(d).
\tag{3}
\]

The inequality is strict at every interior integer \(1\le t\le d-1\) if \(d\le m\le n-2\). Indeed then \(2\le s\le n-d\). The successive slopes of \(B_m\) are nondecreasing, and the final slope, proportional to \(\binom{n-d-1}{s-1}\), is strictly greater than the first, proportional to \(\binom{n-2d}{s-1}\): for \(s\ge2\) and \(d\ge2\), the former is positive and exceeds the latter. Nonconstant nondecreasing slopes put every interior point strictly below the endpoint chord.

Summing inequality (3) over all plant pairs and using (2) gives

\[
2\sum_{i<j}B_m(t_{ij})\le n(n-d) B_m(0)+n(d-1)B_m(d).
\tag{4}
\]

Here \(B_m(0)=b_m\) and \(B_m(d)=a_m\). Inserting (4) into (1) proves the asserted bound. Retaining the pairwise chord discrepancies instead of discarding them gives the exact deficit identity.

Equality at an informative stage requires \(t_{ij}\in\{0,d\}\) for every distinct pair of plants. When two plants have an overlapping pollinator, their neighborhoods must therefore be identical. Every pollinator adjacent to a given plant meets exactly \(d\) plants, all with that identical neighborhood. Such a class has exactly \(d\) plants, all joined to exactly those same \(d\) pollinators. Different classes are disjoint, and hence the whole graph is a union of copies of \(K_{d,d}\). Conversely this union has overlaps only \(0\) or \(d\), realizing equality in every step.

If \(m<d\), no plant can lose all \(d\) neighbors, so \(Z_G(m)=0\). If \(m=n-1\), exactly one pollinator survives, preserving precisely its \(d\) plant neighbors, and thus \(Z_G(n-1)=n-d\). If \(m=n\), then \(Z_G(n)=n\). These are deterministic, proving the boundary statements.

## Verification
The accompanying independent exact-arithmetic program `verify_variance.py` enumerates **all 90 labeled 4-by-4 degree-two incidence matrices** and **all 67,950 labeled 6-by-6 degree-two incidence matrices**. It checks the upper bound, the active-stage equality classification, and the exact overlap-defect identity at every possible removal count. It also samples ten degree-three, 6-by-6 matrices for checks (not an exhaustive census in that size), separately computes first and second extinction-count moments by enumerating removal subsets, and checks the block equality for several sizes up to nine plants.

As a transparent example, take \(n=6,d=2,m=3\). The union of three copies of \(K_{2,2}\) has \(\operatorname{Var}(Z)=24/25\). The connected 12-cycle, with plant \(i\) attached to pollinators \(i\) and \(i+1\) modulo six, has variance \(9/25\), despite having the same degree sequences and the same expected plant-extinction count \(6/5\). The exact variance deficit is \(3/5\). These examples follow directly from the displayed finite formulas and are independently replayed in the packaged code.

To replay, run `python3 verify_variance.py` in a directory containing the single standalone verification file. All computations use Python integers; the proof of the unrestricted theorem is analytic, not based on the finite enumeration.

## Relationship to prior work
Memmott, Waser, and Price (2004) motivated the one-step plant-loss rule and uniform without-replacement pollinator removal, examining cumulative losses in empirical ecological networks. Their complete paper reports simulated extinction curves and discusses redundancy and nestedness, but does not give a sharp variance-maximization theorem for regular webs. Kaiser-Bunbury et al. (2010) likewise study empirical robustness and rewiring, not the displayed regular-incidence overlap-defect identity. Bane, Pocock, and James (2018) examine distributions of a different integrated robustness statistic and models with altered extinction direction/rules; their mathematical object is not the variance at a fixed pollinator-loss stage.

A previously accessible related result characterizes projective-plane incidence graphs as **minimum**-variance webs under fixed-count deletion for specified orders and degrees. It neither implies the present maximum nor characterizes the maximizing block structure. Zhao (2009) and earlier Kahn-type results show complete-bipartite components extremize a different observable, the weighted independent-set enumerator; those results do not directly compare the fixed-size-sampling coextinction-count variance or give its exact overlap gap. The occurrence of the same complete-bipartite extremal shape is an important analogy, not a claim of wholly new graph structure.

## Limitations
The mathematical claim is exact within its hypotheses; it does not imply that such fully modular graphs maximize all ecological risk indicators or that ecological assembly favors them. Equal degrees, uniform removals, absence of demographic feedback, and permission for disconnected networks are essential to the stated sharp extremal classification. The claim is not a stochastic-domination theorem. Broad graph-theoretic inequalities on regular incidence structures may contain an equivalent specialization not found in the literature inspected; an independent bibliographic audit is not yet available.

## References
1. Memmott, J., Waser, N. M., and Price, M. V. (2004), “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* 271, 2605–2611. DOI: 10.1098/rspb.2004.2909. Public PDF: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf (first published online 2004-12-06).
2. Kaiser-Bunbury, C. N., Muff, S., Memmott, J., Müller, C. B., and Caflisch, A. (2010), “The robustness of pollination networks to the loss of species and interactions,” *Ecology Letters* 13, 442–452. DOI: 10.1111/j.1461-0248.2009.01437.x.
3. Bane, M. S., Pocock, M. J. O., and James, R. (2018), “Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness,” *Ecology and Evolution*. DOI: 10.1002/ece3.4529.
4. Zhao, Y. (2009), “The Number of Independent Sets in a Regular Graph,” arXiv:0909.3354. https://arxiv.org/abs/0909.3354.
