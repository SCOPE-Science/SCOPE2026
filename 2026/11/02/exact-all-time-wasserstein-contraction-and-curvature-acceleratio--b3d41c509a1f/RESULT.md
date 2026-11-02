# Exact all-time Wasserstein contraction and curvature acceleration on crown graphs

## Finding
For every integer \(n\ge5\), form the crown graph \(G_n=K_{n,n}\setminus M\) by deleting one perfect matching from the complete bipartite graph. Give every remaining edge length one and jump rate one. Its Markov heat semigroup \(P_t=e^{-tL_n}\), where \(L_n=(n-1)I-A_n\), has the **exact** Wasserstein-one and real-Lipschitz contraction norm
\[
\boxed{\mathcal C_n(t)=\frac{2(n-2)e^{-(n-2)t}-(n-4)e^{-2(n-1)t}}{n}},\qquad t\ge0.
\]
For \(t>0\), adjacent initial states are the unique maximizers among vertex-pair orbits. The instantaneous logarithmic contraction rate \(h_n(t)=-\frac{d}{dt}\log\mathcal C_n(t)\) increases strictly from \(2\) to the spectral gap \(n-2\). In particular, the norm has strict submultiplicativity at positive times, even though the semigroup itself satisfies the exact composition law.

## Assumptions and scope
Let the vertices be \(a_i,b_i\) for indices \(i\in\{1,\ldots,n\}\), with \(a_i\sim b_j\) if and only if \(i\ne j\). Its graph metric \(d\) has distance \(1\) between unmatched cross-part pairs, distance \(3\) between the deleted matched pairs, and distance \(2\) between distinct vertices within one part. Probability measures are row vectors and \(W_1\) is the optimal-transport distance with cost \(d\). Write
\[
\mathcal C_n(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)}.
\]
This equals the operator norm of \(P_t\) on real \(\operatorname{Lip}(V)/\mathbb R\), since finite-metric Kantorovich–Rubinstein duality identifies the dual norm with \(W_1\). The Laplacian is **unnormalized**: each adjacent transition rate is one, rather than total departure rate one. The theorem is for every integer \(n\ge5\) and every real \(t\ge0\).

## Proof
**1. Reduction to three vertex-pair types.** For a finite metric, any optimal coupling \(\pi\) between \(\mu\) and \(\nu\) gives
\[
W_1(\mu P_t,\nu P_t)\le\sum_{x,y}\pi(x,y)W_1(P_t(x,\cdot),P_t(y,\cdot)).
\]
This follows by coupling the output kernels conditionally on each pair. The reverse inequality for the largest pairwise ratio follows by taking point masses. Thus \(\mathcal C_n(t)\) equals the maximum of \(W_1(P_t(x,\cdot),P_t(y,\cdot))/d(x,y)\) over vertex pairs. Permutations of the indices and interchange of the two parts leave exactly three types: same-part, matched nonedge, and adjacent edge.

**2. Spectral heat-kernel decomposition.** The adjacency matrix has off-diagonal blocks \(J-I\). Decomposing vectors into constants on each part and zero-sum vectors, the Laplacian has eigenvalues \(0\), \(2(n-1)\), \(n-2\), and \(n\). Set
\[
\alpha=e^{-(n-2)t},\quad\beta=e^{-nt},\quad\gamma=e^{-2(n-1)t},\quad
u=\frac{\alpha+\beta}{2},\quad v=\frac{\alpha-\beta}{2},\quad c=\frac{\alpha-\gamma}{n}.
\]
Here \(u\) and \(v\) are nonnegative auxiliary scalars. For \(t>0\), \(0<c\le v<u\). Indeed \(v\ge c\) is equivalent to \(n(1-e^{-2t})\ge2(1-e^{-nt})\), which follows because \((1-e^{-zt})/z\) decreases in \(z>0\). Heat-kernel rows follow from the four spectral projectors. Denoting the row based at a vertex by \(p_{a_i}\) or \(p_{b_j}\), their signed differences have the following exact supports and weights.

**3. Same-part pairs.** For distinct \(i,j\),
\[
p_{a_i}-p_{a_j}=u(\delta_{a_i}-\delta_{a_j})-v(\delta_{b_i}-\delta_{b_j}).
\]
Transporting \(u\) from \(a_i\) to \(a_j\) and \(v\) from \(b_j\) to \(b_i\) costs \(2(u+v)=2\alpha\). This is optimal: a unit-Lipschitz test function can take values \(2\) on \(a_i,b_j\), zero on \(a_j,b_i\), and one on all other vertices. Thus the ratio for a same-part pair is exactly \(\alpha\).

**4. Matched nonedges.** For a deleted pair \(a_i,b_i\),
\[
p_{a_i}-p_{b_i}=(\alpha-c)(\delta_{a_i}-\delta_{b_i})-c\sum_{k\ne i}(\delta_{a_k}-\delta_{b_k}).
\]
Send \(\alpha-c\) from \(a_i\) to \(b_i\) at cost three per unit. Permute the other \(n-1\) indices by a derangement and send \(c\) from each \(b_k\) to the corresponding \(a_{\sigma(k)}\) at cost one per unit. Total cost is \(3(\alpha-c)+(n-1)c=3\alpha+(n-4)c\). This is exact by the unit-Lipschitz dual potential which is \(3\) at \(a_i\), \(0\) at \(b_i\), \(1\) at all remaining \(a_k\), and \(2\) at all remaining \(b_k\). The ratio is \(\alpha+(n-4)c/3\).

**5. Adjacent pairs.** Fix \(a_i\sim b_j\), so \(i\ne j\). The positive part of \(p_{a_i}-p_{b_j}\) puts mass \(u-c\) at \(a_i\), mass \(v-c\) at \(a_j\), and mass \(c\) at each \(b_k\) with \(k\notin\{i,j\}\). The negative part has the same respective masses at \(b_j,b_i\), and the \(a_k\) with \(k\notin\{i,j\}\). Send the first two masses along edges \(a_i b_j\) and \(a_j b_i\). Since the remaining \(n-2\) indices admit a derangement for \(n\ge4\), send each remaining mass \(c\) across one edge. The transport cost is precisely the total positive mass,
\[
(u-c)+(v-c)+(n-2)c=\alpha+(n-4)c.
\]
Every source and destination of the signed transport are distinct vertices, so no admissible plan can cost less than one per unit of positive mass. Hence this is the exact Wasserstein distance, not merely an upper bound.

**6. Maximization and rate.** Since \(c>0\) and \(n-4>0\), the adjacent-pair ratio \(\alpha+(n-4)c\) strictly exceeds the two other pair-type ratios for \(t>0\). The displayed formula follows by substitution; at \(t=0\) both sides equal \(1\). Write \(z=e^{-nt}\). The logarithmic rate is
\[
h_n(t)=n-2-\frac{n(n-4)z}{2(n-2)-(n-4)z},
\qquad
h_n'(t)=\frac{2n^2(n-2)(n-4)z}{[2(n-2)-(n-4)z]^2}>0.
\]
Therefore \(h_n(0)=2\) and \(h_n(t)\to n-2\). In particular \(h_n(t)>2\) for all \(t>0\), so \(\mathcal C_n(t)<e^{-2t}\). Since \(\log\mathcal C_n\) has strictly decreasing derivative and vanishes at zero, \(\log\mathcal C_n(s+t)<\log\mathcal C_n(s)+\log\mathcal C_n(t)\) for \(s,t>0\). The exact long-time prefactor follows from the first exponential term. This completes the proof.

## Verification
The accompanying standalone standard-library program `verify_crown.py` uses exact rational arithmetic at the sampling times \(t=\log b\), for \(b\in\{2,3,5\}\), and all \(5\le n\le14\). It reconstructs the spectral heat-kernel rows, checks probability normalization and nonnegativity, then verifies **every unordered vertex-pair orbit instance** by explicit optimal transport plans and, where necessary, unit-Lipschitz dual potentials. These finite checks do not prove the statements for arbitrary real \(t\) or unbounded \(n\); those follow from the symbolic argument above. Run `python3 verify_crown.py`.

## Relationship to prior work
Münch and Wojciechowski [1, Theorem 3.8] relate lower Ollivier curvature bounds to exponential Lipschitz and Wasserstein-one contraction estimates for the heat semigroup. Cushing, Kamtue, Kangaslampi, Liu, and Peyerimhoff [2, Theorem 6.2] prove the sharp Lin–Lu–Yau curvature for all distance-regular graphs of girth four. The crown graphs lie in that class, so these results account for the initial rate \(2\) and the general upper bound \(e^{-2t}\). They do not supply this exact two-exponential norm, the strictly increasing finite-time rate, or strict submultiplicativity. The proof here resolves the full finite-time transport rather than inferring a claimed exact formula from curvature alone.

## Limitations
The statement concerns symmetric rate-one combinatorial heat flow, unit-edge graph distances, real Lipschitz/Wasserstein-one norms, integer \(n\ge5\), and all times \(t\ge0\). It does not give the corresponding norm for arbitrarily weighted edges or nonreversible dynamics. The boundary case \(n=4\) has \(\mathcal C_4(t)=e^{-2t}\); the proof of strict acceleration requires \(n\ge5\). Its historical priority is qualified by possible equivalent calculations under other terminology. No independent audit has been performed.

## References
[1] F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875v1 (first public 2017-12-04), especially Theorem 3.8; https://arxiv.org/abs/1712.00875.

[2] D. Cushing, S. Kamtue, R. Kangaslampi, S. Liu, and N. Peyerimhoff, *Curvatures, graph products and Ricci flatness*, arXiv:1909.11565v1 (first public 2019-09-25), especially Theorem 6.2; https://arxiv.org/abs/1909.11565.
