# Exact commutator fibers and commutator width for friendship graphical groups

## Finding
For every finite field \(\mathbb F_q\) and integer \(m\ge1\), consider the class-two graphical group \(G_{m,q}\) of the friendship graph comprising \(m\) triangles with a common vertex. The number of ordered pairs having **any prescribed central commutator** has an exact product formula, stated below. In particular, the set of single commutators has cardinality
\[
\left(q^3-q+1\right)^m+q^m-1,
\]
and the commutator width of \(G_{m,q}\) is exactly one for \(m=1\) and exactly two for \(m\ge2\). The fiber formula and its image/width consequences, rather than the previously available commuting-pair aggregate, are the claims assessed here.

## Assumptions and scope
Let \(q\) be a prime power, including powers of two, and let \(m\ge1\). Let the simple friendship graph have hub \(c\), leaves \(a_i,b_i\) for \(1\le i\le m\), and edges \((c,a_i),(c,b_i),(a_i,b_i)\). Fix these edge orientations and the corresponding coordinates. Set \(V=\mathbb F_q^{2m+1}\) and \(Z=\mathbb F_q^{3m}\). The bilinear map \(\beta:V\times V\to Z\) has coordinates \(\beta(x,y)_{uv}=x_u y_v\) for each oriented edge \((u,v)\). Define \(G_{m,q}=V\times Z\) with
\[
(x,z)(y,w)=(x+y,z+w+\beta(x,y)).
\]
This associative group has order \(q^{5m+1}\), commutator subgroup \(Z\), and, because the graph has no isolated vertices, center \(Z\). We use \([g,h]=g^{-1}h^{-1}gh\); its edge coordinate is \(x_u y_v-y_u x_v\), in every characteristic.

For any target \(t\in Z\), write its coordinates blade by blade as \(t=(u_i,v_i,w_i)_{i=1}^m\); \((u_i,v_i)\) are the hub-edge coordinates, and \(w_i\) is the internal-edge coordinate. Put
\[
D_q(w)=\begin{cases}q^3+q^2-q,&w=0,\\q(q^2-1),&w\ne0,\end{cases}
\qquad
L_q(u,v,w)=\begin{cases}
q,&(u,v)\ne(0,0),\\
q^2,&(u,v)=(0,0),\ w=0,\\
0,&(u,v)=(0,0),\ w\ne0.
\end{cases}
\]
Then for **each** central target \(t\), the complete prescribed-commutator fiber is
\[
\boxed{\#\{(g,h)\in G_{m,q}^2:[g,h]=t\}
=q^{6m}\left(\mathbf1_{\forall i\;(u_i,v_i)=(0,0)}\prod_{i=1}^m D_q(w_i)
+(q^2-1)\prod_{i=1}^m L_q(u_i,v_i,w_i)\right).}
\]
The indicator is one precisely when all spoke pairs vanish. An empty product is one (though \(m\ge1\)). All asserted equalities are of integers and are valid for every finite field of the indicated cardinality.

## Proof
**Step 1: The group and its commutator.** Bilinearity of \(\beta\) proves associativity of the displayed multiplication. Its commutator is \((0,\beta(x,y)-\beta(y,x))\). Every oriented edge vector occurs as the commutator of its endpoint basis vectors, so the full \(Z\) is the derived subgroup. The intersection of the kernels of the edge skew forms is zero because every vertex lies on an edge; therefore the center is exactly \(Z\).

**Step 2: Determinant fibers.** The determinant map on pairs of vectors in \(\mathbb F_q^2\) has \(q(q^2-1)\) preimages of each prescribed nonzero value: choose any nonzero first vector, then one affine line of \(q\) choices for the second. Its zero fiber consists of all \(q^4\) pairs less the \((q^2-1)(q^2-q)\) invertible pairs, giving \(D_q(0)=q^3+q^2-q\).

**Step 3: Separate the hub pair.** For an ordered pair of group elements write \(U=(x_c,y_c)\in\mathbb F_q^2\), \(A_i=(x_{a_i},y_{a_i})\), and \(B_i=(x_{b_i},y_{b_i})\). The required commutator coordinates on blade \(i\) become
\[
\det(U,A_i)=u_i,\qquad \det(U,B_i)=v_i,\qquad \det(A_i,B_i)=w_i.
\]
If \(U=0\), all the \(u_i,v_i\) vanish and, independently across blades, the third equation has exactly \(D_q(w_i)\) solutions.

If \(U\ne0\), choose \(K\in\mathbb F_q^2\) with \(\det(U,K)=1\). Every pair satisfying the two spoke equations has a unique expression
\[
A_i=\alpha_iU+u_iK,\qquad B_i=\gamma_iU+v_iK.
\]
The internal condition is the single equation \(\alpha_i v_i-\gamma_i u_i=w_i\). It has exactly \(q\) solutions when the spoke pair is nonzero, \(q^2\) solutions when both spokes and the internal coordinate vanish, and zero solutions when both spokes vanish but the internal coordinate does not. These are exactly \(L_q\). There are \(q^2-1\) choices of nonzero \(U\), and blades are independent. Finally the two unused \(Z\)-coordinates of the group factors are arbitrary, contributing \(|Z|^2=q^{6m}\). Adding the disjoint cases \(U=0\) and \(U\ne0\) proves the fiber formula.

**Step 4: Exact image size.** With all spoke pairs zero, every choice of the \(m\) internal coordinates is representable through the \(U=0\) case, giving \(q^m\) image targets. Otherwise at least one spoke pair is nonzero, and representability is equivalent to each zero-spoke blade also having zero internal coordinate. Each active blade has \(q^2-1\) spoke choices and \(q\) internal choices, whereas each inactive blade contributes the unique triple \((0,0,0)\). The nonempty active sets contribute
\[
\sum_{k=1}^m\binom mk\left((q^2-1)q\right)^k
=\left(q^3-q+1\right)^m-1.
\]
Combining the two disjoint cases gives the claimed cardinality.

**Step 5: Sharp width.** The derived subgroup is \(Z\). Any prescribed target \(t\in Z\) splits as \(t=t_{\mathrm{sp}}+t_{\mathrm{int}}\), where the first component retains only the spoke coordinates and the second retains only the internal coordinates. The image criterion just proved makes each component a single commutator. Since commutators are central, the product of their group values is \(t\); thus width is at most two. For \(m=1\), the image criterion covers every \(t\), so width is one. For \(m\ge2\), choose a nonzero spoke on blade one and a nonzero internal coordinate on blade two, with both spokes on blade two zero. This target is not a single commutator, so width is exactly two.

**Step 6: Normalization and commuting probability.** Summing the vertex-coordinate fibers over all \(q^{3m}\) targets yields \(q^{4m+2}\), the number of ordered pairs in \(V^2\), and hence summing the full fibers yields \(q^{2(5m+1)}\). In particular, the zero target has
\[
\#\{(g,h):[g,h]=1\}=q^{6m}\left((q^2-1)q^{2m}+(q^3+q^2-q)^m\right),
\]
so
\[
\Pr([g,h]=1)=\frac{(q^2-1)q^{2m}+(q^3+q^2-q)^m}{q^{4m+2}}.
\]
The zero-fiber consequence is independently recoverable from the established conjugacy-class theory of graphical groups; it is included for normalization, not as an independently original statement.

## Verification
Run `python3 checker.py`. The standalone checker enumerates all pairs of vertex vectors, computes their blade commutator targets using finite-field arithmetic, and checks **every target's** fiber against the formula; it verifies image size, width decompositions, total mass, and an independent centralizer-class-number calculation for the zero fiber. Checked cases are \((q,m)=(2,1),(3,1),(2,2),(3,2),(4,2),(2,3),(5,1)\); the \(q=4\) case uses explicit arithmetic in \(\mathbb F_2[t]/(t^2+t+1)\). The full saved checker prints `ALL_EXACT_CHECKS_PASSED`. The infinite-parameter theorem rests on the preceding bijective count, not on extrapolation from finite tests.

For example, for \((q,m)=(2,2)\), the derived subgroup has \(64\) elements, precisely \(52\) are single commutators, and the zero target has \(148\) vertex-coordinate representations (hence \(148\cdot2^{12}\) ordered group-pair representations). At \((q,m)=(3,2)\), precisely \(633\) of \(729\) central targets are single commutators.

## Relationship to prior work
Naik's 2018 study provides the setting of probability distributions of commutator word maps in finite groups. Cocke and Ho's 2018 paper establishes more general perspectives on finite-group word maps. Rossmann's 2021 study defines graphical groups over finite fields and develops their conjugacy-class enumeration. Rossmann's framework includes a route to the **zero-target** commuting-pair total in this family, so that aggregate is not counted as original here. The contribution assessed here is the **complete prescribed-target nonzero fiber law**, the support-based image criterion and its exact cardinality, and the sharp commutator-width transition for the friendship family. No claim is made that these expressions follow neither from any unexamined older source nor from all conceivable reformulations of the general literature.

## Limitations
The exact image/width result is established only for the graphical groups associated to bouquets of triangles, not for arbitrary graphs or arbitrary nilpotent groups. The multiplication convention uses the stated fixed edge orientations; changing orientations changes signed coordinates but not the invariant counts. The proof is self-contained conditional only on elementary finite-field arithmetic. A plausible residual priority risk is equivalent commutator-width work on class-two quotients of graph groups or related older finite-group literature that was not fully accessible. Independent mathematical audit has not been performed.

## References
1. Tushar Kanta Naik, *On the probability distribution associated to commutator word map in finite groups II*, arXiv:1805.00091v1 (first public version 2018-04-30).
2. William Cocke and Meng-Che Ho, *The Probability Distribution of Word Maps on Finite Groups*, arXiv:1807.07111v1 (first public version 2018-07-18).
3. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1 (first public version 2021-07-12).
