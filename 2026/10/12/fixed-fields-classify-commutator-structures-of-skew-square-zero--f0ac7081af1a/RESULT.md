# Fixed fields classify commutator structures of skew square-zero finite rings

## Finding
Let \(K=\mathbb F_{p^e}\) be a finite field and let \(\sigma\ne\mathrm{id}\) be a field automorphism. Form the associative unital ring
\[
R_\sigma=K\oplus Ku,\quad u^2=0,\quad ua=\sigma(a)u\quad(a\in K).
\]
Write \(q=|K|\), \(F=K^\sigma\), and \(s=|F|\). The following statements constitute one classification of the commutator structure of this natural family of square-zero local rings.

**(a) Commutator-preserving equivalence.** For two nonidentity automorphisms \(\sigma,\tau\) of the *same* field \(K\), an additive bijection \(\Phi:R_\sigma\to R_\tau\) satisfying
\[
\Phi([x,y])=[\Phi(x),\Phi(y)]\qquad(x,y\in R_\sigma)
\]
exists if and only if \(K^\sigma=K^\tau\). Such a bijection may be chosen to restrict to the identity on the common radical \(Ku\) and common center \(F\). Consequently the rings are isoclinic in the usual commutator sense exactly when their fixed fields agree. If \(\sigma(a)=a^{p^k}\) and \(\tau(a)=a^{p^\ell}\), this happens exactly when \(\gcd(e,k)=\gcd(e,\ell)\).

**(b) Exact centralizers and graph.** The center is \(Z(R_\sigma)=F\). There are \(q+2\) distinct element-centralizers: the full ring, \(q\) pairwise distinct commutative subrings of size \(q\), and one commutative subring of size \(sq\). The *noncentral commuting graph*, whose vertices are \(R_\sigma\setminus Z(R_\sigma)\), is
\[
\Gamma_{\mathrm{comm}}(R_\sigma)\cong
\left(\bigsqcup_{i=1}^{q}K_{q-s}\right)\sqcup K_{s(q-1)}.
\]
The commuting graph on all ring elements is the join of this graph with a central clique \(K_s\). Within a fixed field size \(q\), these graphs are isomorphic if and only if their fixed-field orders \(s\) agree.

**(c) Every commutator fiber.** For each \(z\in K\), the number of ordered pairs \((x,y)\in R_\sigma^2\) satisfying \([x,y]=zu\) equals
\[
\begin{cases}
q(q^2-s^2)+q^2s^2,&z=0,\\
q(q^2-s^2),&z\ne0.
\end{cases}
\]
No commutator lies outside \(Ku\), and the commuting probability is
\[
\Pr(xy=yx)=\frac{1}{q}+\frac{(q-1)s^2}{q^3}.
\]
Moreover \(R_\sigma\cong R_\tau\) as rings if and only if \(\sigma=\tau\), and they are anti-isomorphic if and only if \(\sigma=\tau^{-1}\). In particular, for \(K=\mathbb F_{32}\), the Frobenius twists \(\sigma(a)=a^2\) and \(\tau(a)=a^4\) give nonisomorphic, non-anti-isomorphic rings with an explicit additive commutator-preserving bijection and identical graph and fiber distributions. The rings each have \(1024\) elements and exactly \(31\) nonzero two-sided zero divisors, so both attain the sharp bound on ring order in terms of those zero divisors.

## Assumptions and scope
Here \(p\) is any prime, \(e\ge2\), \(q=p^e\), and every field automorphism under discussion is nonidentity. The case of the identity automorphism is commutative and is deliberately excluded. Commutators mean the additive word \([x,y]=xy-yx\), not the multiplicative group commutator. An isoclinism consists of additive isomorphisms of the quotients by the centers and of their additive commutator subgroups, compatible with commutators. The stronger bijection asserted in part (a) supplies such an isoclinism. The graph has simple undirected edges between *distinct* commuting vertices; its noncentral version is used for the displayed disjoint-union formula.

## Proof
For \(a,b,c,d\in K\), associative multiplication is
\[
(a+bu)(c+du)=ac+(ad+b\sigma(c))u.
\]
It follows that, with \(\Delta_\sigma=1-\sigma\),
\[
[a+bu,c+du]=(d\Delta_\sigma(a)-b\Delta_\sigma(c))u.\tag{1}
\]
This also proves directly that all commutators lie in \(Ku\); as \(\sigma\ne\mathrm{id}\), choosing \(a\) with \(\Delta_\sigma(a)\ne0\) and varying \(d\) shows \([R_\sigma,R_\sigma]=Ku\).

**Centers and centralizers.** An element \(a+bu\) commutes with all \(c\in K\) only if \(b=0\), because \(\Delta_\sigma\ne0\). It then commutes with all \(du\) exactly when \(\Delta_\sigma(a)=0\). Hence the center is exactly the fixed field \(F\). If \(\Delta_\sigma(a)\ne0\), write \(\lambda=b/\Delta_\sigma(a)\). Solving (1) gives
\[
C_{R_\sigma}(a+bu)=C_\lambda
 =\{c+\lambda\Delta_\sigma(c)u:c\in K\}.
\]
These \(q\) sets, indexed by \(\lambda\in K\), are distinct, commutative subrings, each of size \(q\). If \(a\in F\) and \(b\ne0\), the centralizer is
\[
C_\infty=F\oplus Ku,
\]
a commutative subring of size \(sq\). Elements of \(F\) have full centralizer \(R_\sigma\). Each pair of distinct proper centralizers intersects precisely in \(F\): the equations for \(C_\lambda\cap C_\mu\) with \(\lambda\ne\mu\) force \(\Delta_\sigma(c)=0\), and a similar argument works for \(C_\lambda\cap C_\infty\). The \(q\) sets \(C_\lambda\setminus F\) each have \(q-s\) elements, and \(C_\infty\setminus F\) has \(s(q-1)\). All commuting noncentral pairs lie in a common proper centralizer. This proves part (b) and its graph formula. The all-element graph has \(q^2\) vertices, and precisely \(s\) vertices commute with everything; thus its isomorphism type recovers \(q,s\). For a fixed \(q\), even the noncentral graph has \(q^2-s\) vertices and recovers \(s\).

**Fiber count.** Fix \(z\in K\). There are exactly \(s^2\) choices of \((a,c)\) with \(\Delta_\sigma(a)=\Delta_\sigma(c)=0\), giving \(q^2\) pairs \((b,d)\) with commutator zero and none with nonzero commutator. For each of the remaining \(q^2-s^2\) choices of \((a,c)\), the map
\[
K^2\longrightarrow K,\qquad (b,d)\longmapsto d\Delta_\sigma(a)-b\Delta_\sigma(c)
\]
is a surjective \(K\)-linear functional with exactly \(q\) preimages of each \(z\). Summing gives part (c) and dividing the zero fiber by \(q^4\) gives the probability.

**Fixed-field criterion and strong isoclinism.** If \(K^\sigma=K^\tau=F\), then \(\sigma\) and \(\tau\) generate the same subgroup of the cyclic group \(\operatorname{Gal}(K/\mathbb F_p)\). Therefore \(\tau=\sigma^r\) for a suitable positive integer \(r\), and the polynomial factorization of \(1-\sigma^r\) shows \(\operatorname{im}(1-\tau)\subseteq\operatorname{im}(1-\sigma)\). Both \(F\)-linear maps have kernel \(F\) and hence equal rank; their images are equal. Choose an \(F\)-linear complement \(E\) with \(K=F\oplus E\). The restrictions of \(\Delta_\sigma\) and \(\Delta_\tau\) to \(E\) are bijections onto the same subspace. Define an \(F\)-linear automorphism \(T\) of \(K\) by
\[
T(f+v)=f+(\Delta_\tau|_E)^{-1}(\Delta_\sigma(v)),\qquad f\in F,\ v\in E.
\]
Then \(T|_F=\mathrm{id}\) and \(\Delta_\tau\circ T=\Delta_\sigma\). The additive bijection
\[
\Phi(a+bu)=T(a)+bu
\]
fixes \(F\) and \(Ku\) pointwise. Substituting in (1) proves \(\Phi([x,y])=[\Phi(x),\Phi(y)]\) for every pair. Conversely any such additive commutator-preserving bijection carries elements commuting with all others to the corresponding elements in the target; hence it carries the center to the center. For fixed \(K\), equal center cardinalities mean equal finite subfields, so the fixed fields must be equal. The same necessity holds for an isoclinism since its center quotients and the common ring cardinality determine \(|Z(R)|\). The Galois fixed-field formula gives the gcd characterization.

**Isomorphism and anti-isomorphism distinction.** The radical is \(J=Ku\), with \(J^2=0\), and the residue field is \(R_\sigma/J\cong K\). Any unital ring isomorphism \(\psi:R_\sigma\to R_\tau\) induces an automorphism \(\alpha\) of \(K\) on residue fields. Its restriction to the one-dimensional left \(K\)-space \(J\) satisfies \(\psi(u)=du\) for some \(d\in K^\times\). Applying \(\psi\) to \(ua=\sigma(a)u\), reducing lifted coefficients modulo \(J\) (since \(J^2=0\)), gives
\[
\tau(\alpha(a))=\alpha(\sigma(a))\qquad(a\in K).
\]
The finite-field Galois group is abelian, hence \(\tau=\sigma\). Conversely equal twists give identical rings. In the opposite ring the relation on the distinguished radical generator is twisted by \(\sigma^{-1}\); applying the same argument establishes that anti-isomorphism holds exactly for inverse twists. For \(K=\mathbb F_{32}\), the exponents \(1\) and \(2\) in the cyclic order-five automorphism group are neither equal nor mutual inverses, but both twists have fixed field \(\mathbb F_2\). This verifies the claimed separation. Finally, an element \(a+bu\) is a unit precisely when \(a\ne0\); when \(a=0\), it annihilates every nonzero element of \(Ku\) on both sides. Thus there are precisely \(q-1\) nonzero two-sided zero divisors and \(|R_\sigma|=q^2\), proving the extremal count.

## Verification
The standalone `verify.py` uses explicit polynomial-basis arithmetic over \(\mathbb F_4\), \(\mathbb F_8\), \(\mathbb F_{16}\), and \(\mathbb F_{32}\). It checks eight field-and-automorphism combinations, enumerating all ordered element pairs, testing every commutator fiber and every centralizer, and comparing complete centralizer and clique-size multisets against parts (b) and (c). It constructs a specific additive bijection between the two indicated twists over \(\mathbb F_{32}\) and verifies the required \(\Delta\)-intertwining identities. Run `python verify.py` using Python 3; the success sentinel is `VERIFY_OK`. These finite checks do not establish the arbitrary-prime statements: those follow from the algebraic proof above.

## Relationship to prior work
Kinyon's 2026 note revisits the sharp bound \(|R|\le(n+1)^2\) for rings with \(n>0\) nonzero two-sided zero divisors and points to Corbas's and Raghavendran's earlier classification of equality cases. Our sharpness observation about \(R_\sigma\) is therefore **not** a new bound or a new classification of extremal ring structures. Raghavendran's 1969 Theorem 10 already gives the matrix models \(\bigl(\begin{smallmatrix}a&b\\0&\sigma(a)\end{smallmatrix}\bigr)\) underlying these rings. We use that established family and do not claim to rediscover it.

Dutta, Basnet, and Nath (2018) give general commuting-probability formulas and small centralizer-number results. Dutta, Fasfous, and Nath (2019, Theorem 2.1) prove that the commuting graph of *any* finite CC-ring is a disjoint union of cliques of sizes determined by the centralizers. Thus the abstract clique-decomposition mechanism is known; the new calculation is the complete explicit centralizer structure and all additive commutator fibers for the specified twisted rings. Dutta and Basnet (2017) prove that suitable isoclinic rings have isomorphic noncommuting graphs; this general implication is also acknowledged, while the explicit fixed-field classification of isoclinism in the present ring family and the stronger pointwise commutator-preserving bijection are separate algebraic assertions.

## Limitations
The ring family is restricted to nontrivial degree-two skew square-zero extensions of a *single finite field*; it is not a classification for all rings with a square-zero radical, all finite chain rings, or rings of higher nilpotency length. The graph computations are valid for the conventions stated and may not match differently defined zero-divisor or unit graphs. The isomorphism and anti-isomorphism statements concern rings, not all possible semilinear equivalences of other associated structures. The earlier global theorem on commuting graphs and earlier ring classification are explicitly treated as prior coverage, not claimed as new. An older equivalent statement under the terminology of \(\mathbb Z\)-isoclinism, twisted extensions, or centralizer profiles remains a historical originality risk despite the comparisons listed in the review. No independent audit has been conducted.

## References
1. M. Kinyon, *Rings with finitely many zero divisors*, arXiv:2604.23423v1 (first posted 25 April 2026), revised arXiv:2604.23423v2 (28 April 2026). https://arxiv.org/abs/2604.23423
2. R. Raghavendran, *Finite associative rings*, Compositio Mathematica **21** (1969), 195–229, especially Theorem 10. https://www.numdam.org/item/CM_1969__21_2_195_0/
3. J. Dutta, D. K. Basnet and R. K. Nath, *Commuting probabilities of n-centralizer finite rings*, arXiv:1803.04111v1 (2018). https://arxiv.org/abs/1803.04111
4. J. Dutta, W. N. T. Fasfous and R. K. Nath, *Spectrum and genus of commuting graphs of some classes of finite rings*, Acta Comment. Univ. Tartu. Math. **23** (2019), especially Theorem 2.1. https://doi.org/10.12697/ACUTM.2019.23.01
5. J. Dutta and D. K. Basnet, *On non-commuting graph of a finite ring*, arXiv:1703.05039v1 (2017), especially the isoclinism results. https://arxiv.org/abs/1703.05039
