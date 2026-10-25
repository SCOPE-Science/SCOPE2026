# Self-review

## Correctness — PASS
The four invariant subspaces have dimensions \(1,k-1,k,1\), with eigenvalues \(0,1,3,2k+1\). Orthogonal projector matrices reconstruct \(L_ke^{-tL_k}\). The hub and leaf coefficient row sums give exactly the three candidate exponential expressions; the leaf-pair off-diagonal is the only sign-ambiguous entry. The strictly increasing local sign polynomial and strictly convex hub-comparison polynomial each have one root on \((0,1)\). The inequality \(3^k\ge2k^2\) proves the roots are ordered. Positive root derivatives give two genuine norm corners, and their equations imply the separate asymptotic scales. Exact finite sign inputs attain the matrix norm. The independently reconstructed spectral-polynomial checker passed 20,235 exact-rational assertions at nine graph sizes and six parameters; these are supporting tests, not the basis of the universal proof.

## Originality — PASS within the checked record
Keller–Lenz treat general graph Laplacians and the Markov heat semigroup; they do not identify this exact finite-family derivative norm. Cioabă–Haemers–Vermette–Wong treat friendship-graph adjacency spectra; Abdian–Ashrafi–Beineke–Oboudi treat Laplacian **spectral determination** of path-friendship graphs. Their inspected results do not furnish coordinatewise absolute row sums or the two crossover times. A comparable exact derivative norm on complete multipartite graphs has different graph geometry; for \(k\ge2\) friendship graphs are not complete multipartite. Work on metric stars and tree heat gradients uses different operators. Search results did not supply an older equivalent all-time norm. Nonretrieval is not a proof of global novelty: unindexed exact matrix-exponential computations remain a historical risk.

## Value — PASS
The exact bounded-input sensitivity of the heat **rate** is a natural semigroup endpoint invariant for a nonregular graph with increasing hub degree and nontrivial triangles. The answer exhibits two independent mechanisms: hub-to-leaf relocation in a vanishing \((\log k)/k\) boundary layer, and a same-triangle interference sign flip at a nonzero limiting time. Complete sharp time profiles, attainable input signs and different scales provide substantive information not contained in the raw Laplacian spectrum. The precise graph family, measurement norm, and limitations are stated rather than implying broader robustness for all networks.

## Closest literature and limits
- Keller and Lenz, *Unbounded Laplacians on Graphs* (2010/2011), DOI 10.1051/mmnp/20105409, arXiv:1101.2979: general heat-semigroup and generator framework.
- Cioabă et al., *The graphs with all but two eigenvalues equal to ±1* (2013), arXiv:1310.6529: spectral structure of friendship graphs.
- Abdian et al., *Laplacian Spectral Determination of Path-Friendship Graphs* (2019), arXiv:1903.11121: Laplacian spectral determination, not temporal derivative norms.
- Remaining risk: possibly unpublished or differently named sharp derivative-norm formula for Dutch windmills; independent historical priority review not performed.

Self-review: passed. Independent audit: not yet performed.
