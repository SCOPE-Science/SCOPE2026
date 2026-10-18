# A facet-covariance Green kernel and exact determinant for cactus metric transportation balls

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite connected simple cactus graph with \(n=|V|\ge2\) and all edge lengths one. Thus each edge belongs to at most one simple cycle. In the zero-sum hyperplane \(H=\{x\in\mathbb R^V:\sum_vx_v=0\}\), consider the real Lipschitz-free unit ball
\[
P_G=\operatorname{conv}\{e_u-e_v,\ e_v-e_u:uv\in E\}.
\]
Choose a facet \(F\) uniformly among its facets, and denote by \(U\in H\) the unique centered, supporting potential whose facet equation is \(\langle U,x\rangle=1\). Set
\[
c_e=\begin{cases}\frac{r}{r-1},&\text{if }e\text{ belongs to an even simple cycle of length }r,\\1,&\text{if }e\text{ is a bridge or belongs to an odd cycle},\end{cases}
\qquad L_c=\sum_{e=uv\in E}\frac{(e_u-e_v)(e_u-e_v)^T}{c_e}.
\]
Then the exact covariance of the uniformly chosen facet normal is the electrical Green kernel
\[
\boxed{\ \mathbb E U=0,\qquad \operatorname{Cov}(U)=\mathbb E(UU^T)=L_c^+.\ }
\]
In particular the expected squared normal difference has the effective-resistance interpretation
\[
\boxed{\ \mathbb E[(U_a-U_b)^2]=(e_a-e_b)^TL_c^+(e_a-e_b)=R_c(a,b).\ }
\]
The unique block-tree route from \(a\) to \(b\) crosses a set of bridges and cycles; if a traversed cycle has length \(r\) and its entry/exit vertices are at cyclic separation \(k\), its contribution to \(R_c(a,b)\) is \(k(r-k)/(r-1)\) when \(r\) is even and \(k(r-k)/r\) when \(r\) is odd. Each traversed bridge contributes one. Thus
\[
\mathbb E\|U\|_2^2=\operatorname{tr}(L_c^+)=\frac1n\sum_{\{a,b\}\subset V}R_c(a,b).
\]
The complete covariance ellipsoid has the exact nonzero-eigenvalue product
\[
\boxed{\ \det_H\operatorname{Cov}(U)=\frac1n\prod_{C\text{ a cycle}}\frac{c_C^{|C|-1}}{|C|},\quad c_C=\begin{cases}\frac{|C|}{|C|-1},&|C|\text{ even},\\1,&|C|\text{ odd}.\end{cases}\ }
\]
For a graph without cycles, the empty product equals one. Finally, the covariance determines the labeled graph: \(\operatorname{Cov}(U)^+=L_c\), and its nonzero off-diagonal entries are precisely the edges, with values \(-1\) on bridges and odd-cycle edges and \(-(r-1)/r\) on even-cycle edges.

## Assumptions and scope

The term *cactus* means that distinct simple cycles are edge-disjoint and have at most one vertex in common. All graphs are finite, connected, simple and unweighted, and the metric is shortest-path distance. We work over real scalars, in the canonical Euclidean coordinates on \(H\). The unit ball of the Lipschitz-free space is the displayed symmetric edge polytope: every longer-distance molecule is a convex combination of signed unit-edge molecules along a geodesic. All facets have distinct polar vertices, and the normal is scaled to support value exactly one; no unit-norm rescaling is performed. The probability measure assigns equal mass to every *facet*, not every graph automorphism orbit or spanning tree. \(L_c^+\) is the Moore--Penrose inverse in \(\mathbb R^V\), vanishing on the constant vector and inverting \(L_c\) on \(H\).

## Proof

**1. Facets and tight-edge connectedness.** A potential \(u\in H\) belongs to the polar of \(P_G\) exactly when \(|u_v-u_w|\le1\) for every edge. The polar has dimension \(n-1\), so its vertex \(u\) has at least \(n-1\) linearly independent tight-edge normals \(e_v-e_w\), hence a connected spanning tight-edge subgraph. Conversely such a subgraph has rank \(n-1\), and its saturated equations determine \(u\) uniquely in \(H\). Along a tight spanning tree all differences are \(\pm1\), so after fixing one vertex to zero all potential values are integers. Thus vertices of the polar, equivalently facets of \(P_G\), are precisely feasible integral potentials whose tight edges connect every vertex. This is also the standard symmetric-edge-polytope facet criterion [4].

**2. Independent local gradient words.** A bridge has to be tight, so its oriented difference is independently \(\pm1\). On a cycle of length \(r\), connectedness of the tight subgraph forces at least \(r-1\) of its edges tight. If \(r\) is even and only \(r-1\) edges were prescribed tight, their signed sum would be odd; the remaining integer difference, bounded in absolute value by one, must also be \(\pm1\). Hence all \(r\) edges are tight and their coherently oriented signed differences form any balanced word with \(r/2\) plus signs and \(r/2\) minus signs. If \(r\) is odd, all edges tight would force an impossible odd signed sum; exactly one edge is slack and has difference zero, while the other \(r-1\) differences are balanced signs. Each allowed cycle word exists. The block-incidence tree has no cycle, so the bridge and cycle words can be chosen independently, with a unique global potential modulo constants. The global tight subgraph is connected if and only if all these local conditions hold. Uniformity over facets therefore makes these local gradient words mutually independent and uniform. The facet *counts* of this decomposition are covered by the existing cycle and gluing literature [4]; our claim concerns their joint second moments.

**3. Local edge covariances.** Orient each cycle coherently. Write \(\mathbf1_r\) for its all-ones vector and \(P_r=I_r-\mathbf1_r\mathbf1_r^T/r\) for the orthogonal projection to zero-sum edge words. Each oriented edge difference has mean zero, and all coordinates are exchangeable. For an even cycle, each coordinate has variance one, and the deterministic zero-sum constraint forces each off-diagonal covariance to equal \(-1/(r-1)\). Its covariance matrix is \(\frac r{r-1}P_r\). On an odd cycle, each coordinate is zero with probability \(1/r\) and otherwise is a sign, giving diagonal variance \((r-1)/r\); the zero-sum constraint forces off-diagonal covariance \(-1/r\), so the covariance is \(P_r\). A bridge has variance one. Different blocks have zero cross-covariance by independence and zero means.

**4. Passing to the Green kernel.** Fix arbitrary directions on edges, with cyclic directions coherent. Let \(B\) be the \(n\)-by-\(|E|\) incidence matrix, \(Y=B^TU\) the edge-gradient vector, and \(C=\operatorname{diag}(c_e)\). The orthogonal projection \(P\) of edge space onto the cut space \(\operatorname{im}(B^T)\) is block diagonal: identity on bridges and \(P_r\) on each cycle. Indeed the cycle space of a cactus is the orthogonal direct sum of its disjoint signed cycle vectors. Therefore step 3 says exactly \(\operatorname{Cov}(Y)=CP\). Because \(C\) is constant on every cycle, it commutes with \(P\). Moreover \(BP=B\), and \(L_c=BC^{-1}B^T\) is positive definite on \(H\). Since \(Y=B^TU\), we have \(BC^{-1}Y=L_cU\) and \(U=L_c^+BC^{-1}Y\). Consequently
\[
\begin{aligned}
\operatorname{Cov}(U)
&=L_c^+BC^{-1}(CP)C^{-1}B^TL_c^+\\
&=L_c^+BC^{-1}B^TL_c^+\\
&=L_c^+.
\end{aligned}
\]
The second equality uses \(BP=B\) and commutation of \(C\) with \(P\); the third uses the defining pseudoinverse identity. This proves the covariance formula for every finite cactus without any enumeration bound.

**5. Resistance, determinant, and recovery.** The covariance identity applied to \(e_a-e_b\) gives the resistance identity. Since every bridge and cycle is connected to the others only through cut vertices, the series law for effective resistance splits the resistance into block contributions. An isolated cycle with uniform edge resistance \(c\) supplies two parallel paths of resistances \(ck\) and \(c(r-k)\), whose effective resistance is \(ck(r-k)/r\). Substituting the two possible \(c\)-values gives the displayed formula; the trace identity is the standard pairwise centered-variance sum.

The weighted Matrix--Tree Theorem yields \(\det_H L_c=n\tau_c\), where \(\tau_c\) is the sum of products of the edge conductances over spanning trees. Every spanning tree contains every bridge and omits exactly one edge from each cycle. Therefore \(\tau_c=\prod_C |C|c_C^{-(|C|-1)}\). Since \(\operatorname{Cov}(U)=L_c^+\) on \(H\), taking determinants gives the displayed exact formula. Finally \((L_c^+)^+=L_c\); because \(G\) is simple and every conductance is positive, the off-diagonal support of \(L_c\) identifies exactly the original graph edges. Their entries determine the edge class and modified conductance. This proves all claims.

## Verification

The accompanying standard-library file `verify.py` independently enumerates all feasible normalized integer edge-Lipschitz potentials on ten small cactus graphs, retains exactly those whose tight-edge subgraph is connected, and computes the empirical covariance using `fractions.Fraction`. It independently forms the modified weighted Laplacian and its pseudoinverse by exact Gauss--Jordan elimination. It compares every covariance entry, every pairwise second moment, the known facet counts, the Kirchhoff-index trace identity, and the restricted determinant with the predicted cycle product. All ten checks pass. For example, the triangle--square bouquet has six vertices, 36 facets, covariance trace \(29/9\) and determinant on the centered hyperplane \(8/243\). The numerical checks corroborate but do not replace the unrestricted proof in Steps 1--5.

Run the bundled checker with `python3 verify.py`; it uses only the Python standard library.

## Relationship to prior work

The general facet criterion and cycle/gluing facet enumeration are established results; particularly relevant is Braun and Bruegge [4], whose Theorem 2.3 and cycle and gluing arguments describe which integral edge potentials support facets and give aggregate facet counts. Aliaga and Pernecká [1] provide Lipschitz-free extreme-point context, Alexander and coauthors [2] study volume and finite metric Banach geometry, and Ohsugi and Tsuchiya [3] treat cactus-related Ehrhart questions for a distinct family of symmetric edge polytopes. We do not claim any prior facet counts, the general vertex criterion, the classical effective-resistance identity or the Matrix--Tree Theorem as new. The result here is the *explicit uniform-facet covariance*, including its even-cycle conductance correction, resistance law, determinant, and inversion/recovery statement. Those statements do not follow solely from an aggregate facet count, although their proof builds on the known local facet descriptions.

## Limitations

The formula assumes edge-disjoint simple cycles and uniform sampling from the facets. It does not assert a Green kernel for arbitrary graphs with overlapping cycles, arbitrary edge lengths, nonuniform facet weights or complex free spaces. The supporting-normal measure is not asserted to be Gaussian; only its first two moments match a Gaussian free field. An equivalent formula in specialized probabilistic graph literature cannot be ruled out solely by indexed searches. No independent scientific audit is claimed.

## References

[1] R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278 (first public version 2018).

[2] S. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public version 2019).

[3] H. Ohsugi and A. Tsuchiya, *Symmetric Edge Polytopes and Matching Generating Polynomials*, arXiv:2008.08621 (first public version 2020).

[4] B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (first public version 2022); see especially Theorem 2.3, Lemma 2.5 and Proposition 2.7.
