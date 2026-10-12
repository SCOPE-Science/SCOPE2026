# Power-law degree and height growth survives a free-commutative direct factor
## Finding
Let \(F\) be a semigroup with a multiplicative weight \(d_F\ge 2\) and
\[
N_F(x)=C_Fx^\rho+o(x^\rho),\qquad C_F,\rho>0.
\]
Let \(A(m)\) be the free commutative semigroup on generators of weights \(e_1,\ldots,e_m\ge2\). Give the direct product \(F\times A(m)\), in the standard adjoined-identity convention, the product weight. Then
\[
N_{F\times A(m)}(x)=C_F\prod_{j=1}^m(1-e_j^{-\rho})^{-1}x^\rho+o(x^\rho).
\]

For the family \(S(a,b,c,k,n,m)\cong F(n)\times A(m)\) of Proposition 6.11 of arXiv:2610.02348v1, take \(n\ge2\). Its free generators are \(f_i=\alpha\circ\beta^i\), while the commuting central generators are multiplication maps \(g_j=[q_j]\). Their polarization weights are
\[
d(f_i)=c^2(kc)^{2i},\qquad d(g_j)=q_j^2.
\]
The first two free-generator weights \(c^4k^2\) and \(c^6k^4\) are multiplicatively independent because \(\gcd(c,k)=1\) and \(c,k>1\). Hence the free factor satisfies the power-law asymptotic of the free-semigroup case of Theorem 1.1. If its constants are \(C_F,\rho\), then the whole disconnected-complement family has
\[
\#\{G\in S:d(G)\le x\}\sim C_F\prod_{j=1}^m(1-q_j^{-2\rho})^{-1}x^\rho.
\]
Thus the degree-growth prediction stated as numerical evidence in Remark 1.9 holds for this explicit family.

The same family also has the predicted height asymptotic. The divisor \(D\) of Proposition 6.11 is symmetric and ample. For its Néron--Tate height and every \(G\in S\), functoriality gives
\[
\widehat h_D(G(P))=d(G)\widehat h_D(P).
\]
Consequently, for every non-torsion \(P\in E^3(K)\),
\[
\#\{G\in S:\widehat h_D(G(P))\le x\}
\sim C_F\widehat h_D(P)^{-\rho}\prod_{j=1}^m(1-q_j^{-2\rho})^{-1}x^\rho.
\]
Since any Weil height \(h_D\) differs from \(\widehat h_D\) by a bounded function, replacing the canonical-height cutoff by a Weil-height cutoff changes the threshold by only \(O(1)\), so the same leading asymptotic holds for \(h_D\).

## Assumptions and scope
The abstract direct-product statement assumes only a power-law count for the first factor and finitely many commuting generators with weights at least \(2\). It does not require the first factor itself to be free.

The application is to the explicit elliptic-curve family of Proposition 6.11 of arXiv:2610.02348v1, with \(n\ge2\) and \(m\ge1\), a nontrivial Pythagorean triple \((a,b,c)\), \(k>1\) coprime to \(c\), and distinct primes \(q_j>kc\). The height conclusion is stated for non-torsion \(K\)-rational points, where \(\widehat h_D(P)>0\). No claim is made for arbitrary partially commutative semigroups with disconnected complement graph.

## Proof
For \(\mathbf r=(r_1,\ldots,r_m)\in\mathbb Z_{\ge0}^m\), put
\[
Q(\mathbf r)=\prod_{j=1}^m e_j^{r_j}.
\]
Using the adjoined identity in each factor, every nonidentity element of \(F\times A(m)\) is uniquely either a pure commutative element or a pair consisting of a nonidentity element of \(F\) and an exponent vector \(\mathbf r\). Therefore
\[
N_{F\times A(m)}(x)=N_A(x)+\sum_{\mathbf r\in\mathbb Z_{\ge0}^m}N_F\!\left(\frac{x}{Q(\mathbf r)}\right),
\]
where \(N_A(x)=O((\log x)^m)=o(x^\rho)\).

The assumed asymptotic implies a global bound \(N_F(y)\le C y^\rho\) for \(y\ge1\), after increasing \(C\) to cover a bounded initial interval. For fixed \(\mathbf r\),
\[
x^{-\rho}N_F\!\left(\frac{x}{Q(\mathbf r)}\right)\longrightarrow C_FQ(\mathbf r)^{-\rho}.
\]
Moreover the normalized summand is bounded by \(CQ(\mathbf r)^{-\rho}\), and
\[
\sum_{\mathbf r\in\mathbb Z_{\ge0}^m}Q(\mathbf r)^{-\rho}
=\prod_{j=1}^m\frac{1}{1-e_j^{-\rho}}<\infty.
\]
Dominated convergence on the countable exponent lattice gives the abstract formula.

For Proposition 6.11, Lemma 6.12 gives \(d(\alpha)=c^2\) and \(d(\beta)=(kc)^2\); multiplicativity of polarization weights gives \(d(f_i)=c^2(kc)^{2i}\). The multiplication map \([q_j]\) has matrix \(q_jI_3\), so Lemma 6.12 gives \(d(g_j)=q_j^2\). To check the noncyclic hypothesis for the free factor when \(n\ge2\), suppose \((c^4k^2)^r=(c^6k^4)^s\) for positive integers \(r,s\). Because \(c\) and \(k\) are coprime and both exceed \(1\), comparison at primes dividing \(k\) gives \(2r=4s\), while comparison at primes dividing \(c\) gives \(4r=6s\), a contradiction. Hence the first two weights are multiplicatively independent. The free-semigroup case of Theorem 1.1 therefore supplies \(N_F(x)=C_Fx^\rho+o(x^\rho)\), and the abstract direct-product formula gives the displayed degree count.

Finally, \(D=2\sum_i\pi_i^*(O)\) is symmetric. For an endomorphism \(G\) with \(G^*D\sim d(G)D\), functoriality and homogeneity of the Néron--Tate height give \(\widehat h_D(G(P))=d(G)\widehat h_D(P)\). A non-torsion point has positive canonical height, so the canonical-height count is exactly the degree count with cutoff \(x/\widehat h_D(P)\). The bounded difference between \(h_D\) and \(\widehat h_D\) sandwiches the Weil-height count between degree counts with cutoffs differing by a fixed additive constant; the leading \(x^\rho\) term is unchanged.

## Verification
The proof uses no finite experiment. The direct-product count is an exact decomposition, the interchange of limit and the exponent-lattice sum is justified by the summable majorant \(CQ(\mathbf r)^{-\rho}\), and the application uses the explicit matrices and direct-product isomorphism of Proposition 6.11. The prime-valuation comparison proves that the free-factor degree image is not cyclic for \(n\ge2\). The height step uses standard Néron--Tate functoriality for a symmetric ample divisor and the bounded difference between Weil and canonical heights.

## Relationship to prior work
Hindes, arXiv:2610.02348v1, proves power-law degree and height asymptotics when the complement of the commutation graph is connected. Its Proposition 1.8 and Proposition 6.11 construct the family \(F(n)\times A(m)\), whose complement graph is disconnected; Remark 1.9 explicitly says that the main theorem does not directly apply and reports only numerical evidence that the same degree and height asymptotics should hold. The argument above proves those two asymptotics for the explicit family and gives the exact multiplicative change in the leading constant contributed by the commuting factor.

Bell--Hindes--Zhong establish the free-semigroup height/degree asymptotic used for the free factor. Their theorem does not include an independent free-commutative direct factor. Standard trace-monoid and graph-product references identify the algebraic direct-product structure but do not, in the inspected material, state the weighted power-law constant above for this arithmetic-dynamical family.

## Limitations
The result does not remove the connected-complement hypothesis in general. It handles the direct-product geometry \(F(n)\times A(m)\) because the commutative factor has a summable weight zeta factor at the free-factor exponent. The height statement is for non-torsion points; torsion points have zero Néron--Tate height and require a different formulation. No claim is made about counts of distinct orbit points after identifying collisions \(G(P)=H(P)\); the count is the map-counting height function used in Theorem 1.1 of the source.

## References
W. Hindes, “Arithmetic growth in partially commutative semigroups of endomorphisms,” arXiv:2610.02348v1, 1 October 2026; especially Theorem 1.1, Proposition 1.8, Remark 1.9, Proposition 6.11, and Lemma 6.12.

J. P. Bell, W. Hindes, X. Zhong, “Counting points by height in semigroup orbits,” Canadian Journal of Mathematics 77 (2025), 2061--2082, DOI 10.4153/S0008414X24000579.

M. Hindry, J. H. Silverman, Diophantine Geometry: An Introduction, Graduate Texts in Mathematics 201, Springer, for the standard Néron--Tate height formalism on abelian varieties.
