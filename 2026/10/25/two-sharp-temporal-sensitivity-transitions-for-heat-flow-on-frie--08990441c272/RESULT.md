# Two sharp temporal sensitivity transitions for heat flow on friendship graphs

## Finding
For an integer \(k\ge2\), let \(F_k\) be the graph obtained by identifying one vertex in each of \(k\) disjoint triangles. Its distinguished common vertex is the hub; its other \(2k\) vertices form \(k\) adjacent pairs. Let \(L_k=D-A\) be the **unnormalized combinatorial Laplacian**, with unit edges and counting measure on vertices. Let
\[
H_k(t)=e^{-tL_k},\qquad G_k(t)=L_ke^{-tL_k}=-\frac{dH_k(t)}{dt},\qquad t\ge0.
\]
The sharp induced coordinatewise norm \(N_k(t)=\|G_k(t)\|_{\ell^\infty(V)\to\ell^\infty(V)}\), also equal to its \(\ell^1\) operator norm, has **exactly two positive corner times** \(0<\tau_k<\sigma_k\):
\[
\boxed{N_k(t)=\begin{cases}
4k e^{-(2k+1)t},&0\le t\le\tau_k,\\
3e^{-3t}+\dfrac{k-1}{k}e^{-t}+\dfrac1k e^{-(2k+1)t},&\tau_k\le t\le\sigma_k,\\
\dfrac{2(k-1)}{k}e^{-t}+\dfrac2k e^{-(2k+1)t},&t\ge\sigma_k.
\end{cases}}
\]
Here \(\xi_k\in(0,1)\) is the unique root of
\[
(4k^2-1)\xi_k^k-3k\xi_k-(k-1)=0,
\]
\(\eta_k\in(0,1)\) is the unique root of
\[
3k\eta_k-(k-1)-\eta_k^k=0,
\]
and \(\tau_k=-\tfrac12\log\xi_k\), \(\sigma_k=-\tfrac12\log\eta_k\). Both times are genuinely nondifferentiable corners of the norm curve. For \(t<\tau_k\) the hub is its unique maximizing output vertex; for \(t>\tau_k\) every leaf is a maximizing output vertex (at equality, both hub and leaves maximize). At \(\sigma_k\), the kernel coefficient coupling two leaves of the same triangle changes sign. At each time an input vector taking only the values \(\pm1\) attains the sharp norm.

The corners have **different size-dependent scales**:
\[
\boxed{\tau_k=\frac{\log k}{2k}+O\!\left(\frac{\log k}{k^2}\right),\qquad
\sigma_k=\frac{\log3}{2}+\frac1{2k}+O(k^{-2})}\qquad(k\to\infty).
\]
In particular, the first sensitivity relocation accelerates to zero with increasing hub degree, while the second local sign transition survives at a fixed positive time. The initial norm equals \(N_k(0)=4k\). The case \(k=1\), a single triangle, is excluded from the two-transition theorem: there \(N_1(t)=4e^{-3t}\).

## Assumptions and scope
The vertex space is \(\mathbb R^{2k+1}\) with ordinary coordinate \(\ell^\infty\) and counting-measure \(\ell^2\). The Laplacian is \(L_{vv}=\deg(v)\), \(L_{vw}=-1\) for adjacent distinct vertices and zero otherwise; the **degree-normalized** random-walk Laplacian is not used. Time is continuous and nonnegative. The operator is the *time derivative of heat diffusion* (up to sign), rather than a spatial graph gradient or the heat operator itself. The displayed norm measures the maximum possible absolute instantaneous change in heat response from an initial signal bounded coordinatewise by one. The statement is for all integers \(k\ge2\) and all real \(t\ge0\), not just sampled times.

## Proof
**Spectral decomposition.** Label the hub \(0\) and leaves \((i,\pm)\), \(1\le i\le k\). The following four mutually orthogonal invariant spaces span all vertex signals: constants (eigenvalue \(0\)); leaf signals constant within each pair, with zero sum over pairs and zero hub (eigenvalue \(1\)); leaf signals antisymmetric within each pair, with zero hub (eigenvalue \(3\)); and the one-dimensional span of the vector with hub component \(-2k\) and every leaf component \(1\) (eigenvalue \(2k+1\)). The multiplicities are \(1,k-1,k,1\), respectively. Denote the orthogonal projections for the three nonzero eigenvalues by \(P_1,P_3,P_{2k+1}\). Their nonzero matrix entries, for leaves \(u,v\), are
\[
(P_1)_{uv}=\frac12\mathbf1_{\{u,v\text{ in one pair}\}}-\frac1{2k},\qquad
(P_3)_{uv}=\frac12\bigl(\mathbf1_{\{u=v\}}-\mathbf1_{\{v=\operatorname{partner}(u)\}}\bigr),
\]
\[
(P_{2k+1})_{00}=\frac{2k}{2k+1},\quad
(P_{2k+1})_{0u}=-\frac1{2k+1},\quad
(P_{2k+1})_{uv}=\frac1{2k(2k+1)}.
\]
Thus \(G_k(t)=e^{-t}P_1+3e^{-3t}P_3+(2k+1)e^{-(2k+1)t}P_{2k+1}\).

**Every coefficient and its sign.** Put \(a=e^{-t}\), \(b=3e^{-3t}\), \(u=e^{-(2k+1)t}\). The hub diagonal entry of \(G_k(t)\) is \(2ku\), and all \(2k\) hub-to-leaf entries are \(-u\). Hence the hub absolute row sum is \(R_h=4ku\). Every leaf has entries
\[
\begin{array}{ll}
G(v,v)=\dfrac{k-1}{2k}a+\dfrac12b+\dfrac1{2k}u,&
G(v,\operatorname{partner}(v))=\dfrac{k-1}{2k}a-\dfrac12b+\dfrac1{2k}u,\\[3pt]
G(v,0)=-u,&
G(v,w)=\dfrac{u-a}{2k}\quad\text{for other leaves }w.
\end{array}
\]
The diagonal is positive and all other-pair entries are nonpositive since \(0<u\le a\). Only the same-pair off-diagonal coefficient can change sign. Summing absolute values gives the leaf row sum
\[
R_\ell(t)=\max\left\{R_-(t),R_+(t)\right\},\quad
R_-(t)=b+\frac{k-1}{k}a+\frac{u}{k},\quad
R_+(t)=\frac{2(k-1)}{k}a+\frac{2u}{k}.
\]
Every leaf has the same row sum. Therefore \(N_k(t)=\max\{R_h,R_-,R_+\}\), and symmetry of the matrix also gives the same \(\ell^1\) norm. A sign vector selected from a maximizing row attains each norm exactly.

**The local sign transition.** Set \(x=e^{-2t}\in(0,1]\). The sign of the partner entry is the sign of \((k-1)-3kx+x^k\). The function \(g(x)=3kx-(k-1)-x^k\) increases strictly, since \(g'(x)=3k-kx^{k-1}\ge2k\). Moreover \(g(0)=-(k-1)<0\) and \(g(1)=2k>0\), so its root \(\eta_k\) is unique. Since \(g(1/3)=1-3^{-k}>0\), one has \(0<\eta_k<1/3\). For \(t<\sigma_k\), the partner entry is negative, so \(R_\ell=R_-\); for \(t>\sigma_k\), it is positive, so \(R_\ell=R_+\). The crossing is transverse, giving a corner provided leaves dominate there.

**Hub–leaf crossing and its order.** The equation \(R_h=R_-\), after division by \(e^{-t}/k\), becomes
\[
f(x)=(4k^2-1)x^k-3kx-(k-1)=0.
\]
The function \(f\) is strictly convex for \(k\ge2\); it starts below zero, initially decreases, and is positive at \(x=1\), where \(f(1)=4k(k-1)\). Hence it has exactly one root \(\xi_k\in(0,1)\), and the crossing is transverse. At \(x=\eta_k\), the hub-to-leaf ratio is
\[
\frac{R_h}{R_\ell}=\frac{2k^2\eta_k^k}{k-1+\eta_k^k}<1.
\]
Indeed, \(3^k\ge2k^2\) for all \(k\ge2\) (verify at \(2\) and induct using \(3k^2>(k+1)^2\)); therefore \((2k^2-1)\eta_k^k<(2k^2)3^{-k}\le1\le k-1\). At \(t=0\), the hub sum \(4k\) strictly exceeds the leaf sum \(4\). Consequently the unique hub–leaf crossing occurs before the partner sign crossing: \(\xi_k>\eta_k\) and \(0<\tau_k<\sigma_k\). After \(\sigma_k\), the hub-to-positive-leaf ratio is \(2k^2x^k/(k-1+x^k)\), which increases in \(x\), so it remains below one for smaller \(x\). These observations prove the entire piecewise formula and the claimed maximizing vertex locations.

**Corners and scales.** Both crossings are transverse: \(f\) has positive derivative at its unique root, while \(g'(\eta_k)>0\). Thus the upper envelope switches branch with unequal one-sided derivatives at each positive time. The second root equation gives \(\eta_k=(k-1+\eta_k^k)/(3k)=1/3-1/(3k)+O(3^{-k}/k)\), proving the expansion for \(\sigma_k\). The first gives
\[
\xi_k^k=\frac{3k\xi_k+k-1}{4k^2-1}.
\]
Bounding its right side between \((k-1)/(4k^2-1)\) and \((4k-1)/(4k^2-1)\) first yields \(-\log\xi_k=O(\log k/k)\). Substituting \(\xi_k=1+O(\log k/k)\) back yields \(\xi_k^k=k^{-1}(1+O(\log k/k))\), hence \(\tau_k=(\log k)/(2k)+O(\log k/k^2)\). This completes the proof.

## Verification
The standalone `checker.py` uses exact rational arithmetic on the adjacency-defined Laplacian for every \(2\le k\le10\), at six rational values of \(z=e^{-t}\). It constructs each spectral projector **independently as a polynomial in the Laplacian**, verifies the spectral identities, reconstructs all matrix entries, checks all row sums and the full induced norm, and realizes equality with sign-valued inputs. Execution produced 20,235 passing exact-rational assertions. These finite checks do **not** prove the claims for unbounded \(k\) or all real times; the preceding analytical arguments do.

## Relationship to prior work
Keller and Lenz describe graph Laplacians, their Markovian heat semigroups and the heat equation in general. Cioabă, Haemers, Vermette and Wong analyze the **adjacency spectra and spectral determination** of friendship graphs. Neither inspected work derives the induced \(\ell^\infty\) norm of the *temporal derivative* on this family or its two switching times. Results on complete multipartite graphs and Boolean cubes concern different graph families; in particular, for \(k\ge2\) a friendship graph is not complete multipartite. Existing tree-gradient and metric-star semigroup estimates concern different output operators. The present result specifically combines an exact all-time temporal-derivative norm, two structural corners and their separated asymptotic scales. This is an evidence-limited comparison, not a proof of global historical priority.

## Limitations
This result uses the unnormalized combinatorial Laplacian on the unweighted friendship graph with \(k\ge2\). It does not give the same formulas for random-walk normalization, weighted triangles, other windmill clique sizes, or spatial gradient norms. It is not a general bound over all graphs with the same degree sequence. The novelty check does not exhaust older spectral-graph literature under every possible synonym. Independent bibliographic and mathematical confirmation remain outstanding.

## References
- M. Keller and D. Lenz, *Unbounded Laplacians on Graphs: Basic Spectral Properties and the Heat Equation*, Mathematical Modelling of Natural Phenomena **5** (2010), 198–224, DOI 10.1051/mmnp/20105409; open preprint arXiv:1101.2979 (2011).
- S. M. Cioabă, W. H. Haemers, J. Vermette and W. Wong, *The graphs with all but two eigenvalues equal to ±1*, arXiv:1310.6529 (first posted 2013), Journal of Algebraic Combinatorics **41** (2015), 887–897.
- A. Z. Abdian, A. R. Ashrafi, L. W. Beineke and M. R. Oboudi, *Laplacian Spectral Determination of Path-Friendship Graphs*, arXiv:1903.11121 (2019); later published in AKCE International Journal of Graphs and Combinatorics (2021). Structural context; publication after the archived source date.
