# Exact spoke–cut compositions in weighted wheel spanning trees and their critical spatial limit

## Finding

**Theorem (exact finite marked-composition classification).** Let \(n\ge3\), and let \(W_{n+1}\) have a cycle of \(n\) labeled rim vertices \(0,\ldots,n-1\) and a central hub \(h\). Give every rim edge conductance \(1\) and every hub-to-rim spoke conductance \(t>0\). Choose a spanning tree \(\mathcal T_{n,t}\) with probability proportional to the product of its edge conductances. Write \(K_{n,t}\) for its hub degree, equivalently its number of spokes.

For each \(1\le k\le n\), the number of spanning trees having exactly \(k\) spokes and its conditional probability are
\[
 c_{n,k}=\frac{n}{k}\binom{n+k-1}{2k-1}
 =\frac{2n}{n+k}\binom{n+k}{2k},
 \qquad
 \Pr(K_{n,t}=k)=\frac{c_{n,k}t^k}{Z_n(t)},
\]
where the known cycle-rooted-forest partition function satisfies
\[
 Z_n(t)=\sum_{k=1}^{n}c_{n,k}t^k
 =\det\bigl(tI+L(C_n)\bigr)
 =2\bigl(T_n(1+t/2)-1\bigr).
\]
Here \(T_n\) is the Chebyshev polynomial of the first kind. The determinant identity and its univariate evaluation are classical ingredients, not a novelty claim.

Condition on \(K_{n,t}=k\), and independently designate one of the \(k\) selected spokes uniformly. Rotate the labeled cycle so that its rim endpoint is at \(0\). Around the cycle, marked spoke vertices and deleted rim edges strictly alternate. Regard a spoke at vertex \(i\) as located at \(2i\) and a deleted rim edge \((i,i+1)\) as located at \(2i+1\), modulo \(2n\). Beginning at the designated spoke, let \(m_1,\ldots,m_{2k}\) be the nonnegative integers satisfying: the clockwise half-edge distance between successive marks is \(2m_j+1\), including the final-to-first distance. Then
\[
 \boxed{\quad(m_1,\ldots,m_{2k})\ \text{is uniform on}\ 
 \{(m_1,\ldots,m_{2k})\in\mathbb Z_{\ge0}^{2k}:\sum_jm_j=n-k\}.\quad}
\]
In particular, if \(S_1,\ldots,S_k\) are the numbers of rim vertices in successive remaining-rim path components, cyclically ordered with the component of the designated spoke first, then
\[
 \boxed{\quad
 \Pr(S_1=s_1,\ldots,S_k=s_k\mid K_{n,t}=k)
 =\frac{\prod_{i=1}^k s_i}{\binom{n+k-1}{2k-1}},
 \quad s_i\ge1,\ \sum_i s_i=n.\quad}
\]
This conditional law is independent of \(t\). Conditional on the component sizes, the spoke vertex is uniform among the vertices of its own path component, independently across the components under the marked cyclic representation.

**Corollary (critical spatial limit).** Fix \(s>0\) and take the **critical spoke conductance** \(t_n=s/n^2\). Then \(K_{n,t_n}\) converges in total variation to a positive-integer variable \(K_s\) with
\[
 \boxed{\quad
 \Pr(K_s=k)=\frac{s^k}{(2k)!(\cosh\sqrt{s}-1)},\quad k\ge1.
 \quad}
\]
Equivalently, \(2K_s\) has the law of a \(\operatorname{Pois}(\sqrt s)\) variable conditioned to be positive and even. The mean satisfies
\[
 \mathbb E K_s=\frac{\sqrt s}{2}\coth\!\left(\frac{\sqrt s}{2}\right).
\]
For every fixed \(k\), conditional on \(K_{n,t_n}=k\), the vector of rescaled successive marked half-edge gaps
\[
 \left(\frac{m_1+1/2}{n},\ldots,\frac{m_{2k}+1/2}{n}\right)
 \Longrightarrow \operatorname{Dirichlet}(1,\ldots,1)
\]
and the rescaled component sizes obey
\[
 \boxed{\quad
 (S_1/n,\ldots,S_k/n)\Longrightarrow\operatorname{Dirichlet}(2,\ldots,2).
 \quad}
\]
Together these statements give a joint mixed-dimension limiting law: first sample \(K_s\), then sample the corresponding uniform \(2K_s\)-simplex spacings; pair the adjacent spacings around each spoke to obtain the rooted-component lengths. The globally marked origin, before rotation, is independent and uniform around the limiting circle.

## Assumptions and scope

The graph is simple; \(n\ge3\). Every tree has exactly \(n\) edges. Its probability is \(t^{K_{n,t}}/Z_n(t)\), since all remaining rim edges have conductance one. A deleted rim edge is a cut, not a retained edge. The marks include all spoke endpoints and all deleted rim edges. There are exactly \(K_{n,t}\) of each type. The sampled distinguished spoke is only a way of specifying a canonical cyclic starting point; none of the asserted laws depends on the initial rim labels. All limits fix \(s>0\) while \(n\) tends to infinity. A \(\operatorname{Dirichlet}(2)\) vector with one component is understood as the unit point mass at \(1\).

## Proof

**1. Alternation is equivalent to the spanning-tree condition.** Delete the central vertex and all spokes from a spanning tree. The remaining rim edges form a spanning forest of the rim cycle. If \(k\) spokes remain, the tree has exactly \(n-k\) retained rim edges, hence exactly \(k\) deleted rim edges. These cuts divide the cycle into exactly \(k\) nonempty path components. Each such component must contain a spoke to be connected to the hub. It cannot contain two, since the two spokes and the retained rim path between them would make a cycle. Therefore each component contains exactly one spoke. Conversely, any configuration consisting of \(k\) cuts and one spoke in each of the resulting \(k\) components forms a spanning tree. Going clockwise, the cut-edge and spoke-vertex marks strictly alternate.

**2. A marked tree is a weak composition.** Choose a spanning tree with \(k\) spokes and mark one spoke. Record its endpoint \(v\) on the \(n\)-cycle, then record all \(2k\) clockwise spacings in the \(2n\)-site interlaced system of vertices and edge midpoints. All spacings are positive and odd, uniquely \(2m_j+1\). Summing the spacings gives \(2n\), so \(\sum_j m_j=n-k\). Conversely, any vertex \(v\) and any ordered weak composition \((m_j)\) of \(n-k\) into \(2k\) slots reconstruct the alternating cut/spoke marks and thus a unique marked spanning tree. Since every tree with \(k\) spokes has exactly \(k\) choices for its marked spoke, the number \(c_{n,k}\) obeys
\[
 kc_{n,k}=n\,\#\{m_j\ge0:\sum_jm_j=n-k\}
 =n\binom{n+k-1}{2k-1}.
\]
Under the conditional weighted measure, every tree with the same number \(k\) of spokes has identical weight \(t^k\). Uniformly distinguishing a spoke makes the pair \((v,(m_j))\) uniform on the indicated Cartesian product, so both \(v\) and the weak composition are independent and uniform.

**3. Component-length size bias.** Index the mark sequence cyclically as spoke, cut, spoke, cut, and so forth. The component containing spoke \(i\) has a length of the form \(s_i=1+m_{2i-1}+m_{2i}\), with the indices interpreted cyclically and the parity convention chosen to cover the two adjacent gaps. For a fixed integer \(s_i\ge1\), there are exactly \(s_i\) ordered nonnegative ways to split \(s_i-1\) between the two adjacent gaps. Thus the number of weak compositions yielding a given positive component-size vector \((s_i)\) is \(\prod_i s_i\); their normalized probability is the stated formula. The identity
\[
 \sum_{\substack{s_i\ge1\\\sum_i s_i=n}}\prod_i s_i
 =[z^n]\left(\sum_{s\ge1}sz^s\right)^k
 =[z^{n-k}](1-z)^{-2k}=\binom{n+k-1}{2k-1}
\]
checks normalization. Each split identifies the spoke's location within its component; uniformity of the weak-composition measure makes this location conditionally uniform. Pairwise factorization of the split multiplicities gives conditional independence.

**4. The weighted partition and the finite distribution.** Summing \(t^k\) over the enumerated trees gives \(Z_n(t)\). Deleting the hub bijects these trees with rooted forests of \(C_n\), and the all-minors matrix-tree identity yields \(Z_n(t)=\det(tI+L(C_n))\). Since the cycle Laplacian has eigenvalues \(2-2\cos(2\pi j/n)\), the product is \(2(T_n(1+t/2)-1)\). This determinant identity can also be independently checked from the marked-tree count. The probability of \(K_{n,t}=k\) follows by division by \(Z_n(t)\).

**5. A full critical-window root-count limit.** For every fixed \(k\ge1\), direct multiplication of the binomial coefficient yields
\[
 \frac{c_{n,k}}{n^{2k}}=\frac{n}{k n^{2k}}\binom{n+k-1}{2k-1}
 \longrightarrow \frac{2}{(2k)!}.
\]
A uniform summable majorant is available: \(c_{n,k}=\frac{2n}{n+k}\binom{n+k}{2k}\le 2(2n)^{2k}/(2k)!\) for \(k\le n\); consequently \(c_{n,k}(s/n^2)^k\le2(4s)^k/(2k)!\). Define terms to be zero when \(k>n\). Dominated convergence for the infinite series gives
\[
 Z_n(s/n^2)\longrightarrow \sum_{k\ge1}\frac{2s^k}{(2k)!}=2(\cosh\sqrt s-1).
\]
The pointwise limiting mass is therefore as asserted. Since the limiting masses sum to one, discrete Scheffé convergence yields total variation. The positive-even Poisson identification follows by canceling the common factor \(e^{-\sqrt s}\). Differentiating \(\cosh\sqrt s-1\), or summing the absolutely convergent series, yields the stated mean.

**6. The spatial joint limit.** Fix \(k\). The conditional gap vector is uniform on the integer lattice points of the \((2k-1)\)-simplex with total sum \(n-k\). Dividing by \(n\), the discrete uniform distribution converges weakly, by Riemann-sum approximation on this fixed-dimensional simplex, to the uniform simplex measure, i.e. \(\operatorname{Dirichlet}(1,\ldots,1)\). Adding the deterministic \(1/(2n)\) offsets to locate actual interlaced marks changes no limit. Each component size is \(1\) plus two adjacent gaps. The aggregation property of the Dirichlet law (or normalized independent exponential variables, paired into independent \(\operatorname{Gamma}(2,1)\) variables) gives \(\operatorname{Dirichlet}(2,\ldots,2)\) for component sizes. Uniform total-variation tightness of \(K_{n,t_n}\), established in step 5, promotes these fixed-\(k\) conditional limits to convergence of the whole random finite collection of lengths and marks. The exact independence of the distinguished spoke's absolute vertex from its gap vector, shown in step 2, gives an independent uniform global rotation in the limit. This completes the proof.

## Verification

The accompanying Python 3 standard-library checker `check_wheel_spokes.py` runs independently of the proof and verifies 5,458 exact assertions/comparison checks. It enumerates every candidate \(n\)-edge subgraph of the wheel for \(3\le n\le8\), independently tests acyclicity, counts the hub degrees, reconstructs the marked compositions, confirms their bijection and size-bias multiplicities, and compares weighted coefficients against an integer Bareiss determinant for four positive conductances. It additionally checks fixed-\(k\) coefficient asymptotics and numerical values of the limiting Poisson-even normalizer and mean. Finite testing does not establish the assertions for arbitrary \(n\); the proof above does.

Reproduce with `python3 check_wheel_spokes.py` in the directory containing this file. The checker requires no input and no third-party dependencies.

## Relationship to prior work

Avena, Castell, Gaudillière and Mélot (2017, subsequently 2018) set out the general weighted rooted-forest law and determinantal root-set framework. Grunwald and Mednykh (2019) give Chebyshev formulas for counting rooted forests in circulant graphs, and their 2020 paper relates cone spanning trees to rooted forests and gives the ordinary wheel tree count. These works justify the measure and the known partition-function machinery. The present claim concerns the **exact finite marked spatial law conditioned on the hub degree** and its uniform weak-composition representation, with the explicit joint Poisson-even/Dirichlet critical regime \(t=s/n^2\) as a corollary; these are not statements of the cited counting identities. In particular, a general determinantal description of root sets alone does not directly give the full joint law of cuts, roots and component lengths without an additional argument.

Related research on unrooted wheel forest or arboreal-gas local processes uses a different random object and weighting, not the conditioned connected spanning-tree measure considered here. The current result does not assert priority for the classical matrix-tree theorem, cycle determinant, weighted rooted-forest ensemble, elementary Dirichlet aggregation or standard Poisson conditioning.

## Limitations

The result is for cycles with an added hub, equal unit rim conductances, homogeneous spoke conductances, and a single fixed positive critical parameter \(s\). The marked composition and finite component law are exact for all \(t>0\), but the Poisson-even/Dirichlet limit is established only when \(t=s/n^2\). No claim is made for spatially varying weights, growing numbers of hubs, non-cycle rims, process dynamics, or all possible crossover scalings. Historical novelty comparisons cannot exhaust inaccessible literature.

## References

- L. Avena, F. Castell, A. Gaudillière and C. Mélot, *Random Forests and Networks Analysis*, arXiv:1711.01635 (first posted 5 November 2017); *Journal of Statistical Physics* 173 (2018), 985–1027. https://arxiv.org/abs/1711.01635
- L. A. Grunwald and I. A. Mednykh, *The number of rooted forests in circulant graphs*, arXiv:1907.02635 (first posted 4 July 2019). https://arxiv.org/abs/1907.02635
- L. A. Grunwald and I. A. Mednykh, *On complexity and Jacobian of cone over a graph*, arXiv:2004.07452 (first posted 16 April 2020). https://arxiv.org/abs/2004.07452
- The classical all-minors matrix-tree theorem and the cycle-Laplacian/Chebyshev identity are used as established background, not independently new claims.
