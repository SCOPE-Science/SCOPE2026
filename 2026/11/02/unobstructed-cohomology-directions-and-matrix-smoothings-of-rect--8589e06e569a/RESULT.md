# Unobstructed cohomology directions and matrix smoothings of rectangular-band algebras

## Finding
Let \(k\) be any field and \(m,n\ge2\). For the rectangular band \(B_{m,n}=I\times J\), with \((i,j)(i',j')=(i,j')\), put \(A_{m,n}=k[B_{m,n}]\). There is an explicitly constructed injective linear map
\[
\operatorname{Hom}_k(T\otimes U,k)\hookrightarrow HH^2(A_{m,n},A_{m,n}),
\qquad \dim_k U=m-1,\quad\dim_k T=n-1,
\]
whose entire image consists of classes admitting simultaneous polynomial, hence formal, associative integrations. In particular, \(\dim HH^2(A_{m,n},A_{m,n})\ge(m-1)(n-1)\).

In the square case \(m=n=r\ge2\), there is a free one-parameter associative deformation of \(A_{r,r}\) over \(k[t]\) whose generic fiber over \(k((t))\) is \(M_r(k((t)))\). The special fiber has Jacobson radical of dimension \(r^2-1\) with square of dimension \((r-1)^2\) and cube zero. The theorem does **not** assert that the displayed lower bound is the entire second Hochschild cohomology.

## Assumptions and scope
Fix positive integers \(m,n\ge2\) and an arbitrary field \(k\), with no restriction on characteristic. Set \(V=k^m\) and \(W=k^n\), equipped with the coordinate-sum functionals \(\varepsilon_V,\varepsilon_W\). Choose \(v_0\in V\), \(w_0\in W\) with \(\varepsilon_V(v_0)=\varepsilon_W(w_0)=1\), and write \(U=\ker\varepsilon_V\), \(T=\ker\varepsilon_W\). There are direct sums \(V=kv_0\oplus U\) and \(W=kw_0\oplus T\). Identify the underlying vector space of \(A_{m,n}\) with \(V\otimes W\), equivalently \(m\times n\) matrices. For each bilinear form \(Q:W\times V\to k\), write \(XQY\) for sandwich matrix multiplication with the corresponding \(n\times m\) matrix.

Hochschild cohomology uses the ordinary \(k\)-linear Hochschild complex of the associative, possibly nonunital algebra \(A_{m,n}\), with coefficients in itself: \(C^d(A,A)=\operatorname{Hom}_k(A^{\otimes d},A)\). No unitization convention is used in this claim.

## Proof
**1. The band as a rank-one sandwich algebra.** Let \(P_0(w,v)=\varepsilon_W(w)\varepsilon_V(v)\). Matrix units satisfy \(E_{ij}P_0E_{i'j'}=E_{ij'}\), so their sandwich product is precisely that of the rectangular band. Put \(e=v_0\otimes w_0\). Relative to
\[
A=ke\oplus U\oplus T\oplus(U\otimes T),
\]
where \(u\in U\) abbreviates \(u\otimes w_0\) and \(s\in T\) abbreviates \(v_0\otimes s\), multiplication is
\[
(\alpha,u,s,z)(\beta,u',s',z')=(\alpha\beta,\,\beta u,\,\alpha s',\,u\otimes s').
\]
Thus every \(s\in T\) annihilates \(A\) on the left, every \(u\in U\) is annihilated by \(A\) on the right, and \(s u=0\).

**2. Simultaneously integrable infinitesimal deformations.** Let \(\mathcal Q\) be the space of bilinear forms \(Q:W\times V\to k\) satisfying \(Q(w_0,V)=Q(W,v_0)=0\). Restriction identifies \(\mathcal Q\simeq\operatorname{Hom}_k(T\otimes U,k)\); its dimension is \((m-1)(n-1)\). With independent coordinates \(s_\nu\) on this space and a basis \(Q_\nu\), define
\[
X\star_{\mathbf s}Y=X\bigl(P_0+\sum_\nu s_\nu Q_\nu\bigr)Y.
\]
This product is associative over the entire polynomial base \(k[\mathbf s]\), since
\((X P Y)PZ=XP(Y P Z)\) for any rectangular sandwich matrix \(P\). Its specialization at \(\mathbf s=0\) is the original band algebra, and its underlying module is free, so the deformation is flat. Differentiation in a \(Q\)-direction gives \(F_Q(X,Y)=XQY\). Associativity to first order gives \(\delta F_Q=0\). Indeed, with the standard Hochschild differential,
\[
(\delta F_Q)(x,y,z)=xF_Q(y,z)-F_Q(xy,z)+F_Q(x,yz)-F_Q(x,y)z=0.
\]
Moreover each direction integrates to all orders, already through the explicit polynomial product.

**3. Distinct cohomology classes.** Let \(H:A\to A\) be any \(k\)-linear map. For \(s\in T\), \(u\in U\), the first Hochschild coboundary satisfies
\[
(\delta H)(s,u)=sH(u)-H(su)+H(s)u=0,
\]
because \(sA=0\), \(Au=0\), and \(su=0\). But direct sandwich multiplication gives
\[
F_Q(s,u)=Q(s,u)e.
\]
Therefore \(F_Q\) can be a coboundary only if \(Q|_{T\times U}=0\), hence only if \(Q=0\). This proves injectivity of \(\mathcal Q\to HH^2(A,A)\) in every characteristic. This is a lower bound, not an unproved claim of full \(HH^2\) classification.

**4. A smoothing to simple matrix algebra.** For \(m=n=r\), \(U\) and \(T\) have the same dimension. Choose \(Q\in\mathcal Q\) so that its restriction \(T\times U\to k\) is a nondegenerate pairing. In bases adapted to \(kv_0\oplus U\) and \(kw_0\oplus T\), the sandwich matrix \(P_t=P_0+tQ\) is block-diagonal with blocks \(1\) and \(tC\), where \(C\) is invertible of size \(r-1\). Thus \(P_t\) is invertible over \(k((t))\). The map \(X\mapsto XP_t\) identifies the generic fiber of \(X\star_tY=XP_tY\) with the ordinary full matrix algebra \(M_r(k((t)))\). This does not require \(k\) to be infinite.

**5. Radical of the special fiber.** The total-augmentation map \(\varepsilon:A\to k\) is multiplicative. Its kernel \(J=U\oplus T\oplus(U\otimes T)\) has \(J^2=U\otimes T\) and \(J^3=0\) by the multiplication formula. Since \(A/J\cong k\) and \(J\) is nilpotent, \(J\) is exactly the Jacobson radical (equivalently, use the unitization to define this for a nonunital algebra). For square \(r\), this gives the dimensions stated above.

## Verification
The standalone \(verify_deformations.py\) checks the adapted-basis product and every ordered basis triple for the deformation with a nondegenerate pairing in ranks \(2\) and \(3\), over \(\mathbb F_2\) and \(\mathbb F_3\), at every field parameter. It also checks all \((r-1)^2\) annihilator-pair probes that force cohomology independence. Run \(\texttt{python3 verify_deformations.py}\); the final marker is \(\texttt{RECTANGULAR_BAND_DEFORMATIONS_OK}\). These finite tests corroborate but do not prove the uniform theorem; all-characteristic validity follows from the displayed identities.

## Relationship to prior work
Rectangular bands and their rank-one Rees/Munn sandwich algebras are classical. Margolis and Steinberg discuss rectangular-band ideals in their representation-theoretic treatment of monoid quivers; this is antecedent structure, not a deformation classification. Soroushmehr (2015) determines homomorphisms from Munn algebras into commutative Banach algebras. Esslamzadeh (2016), Theorem 2.1, gives a much broader factorization of homomorphisms from Munn algebras into arbitrary Banach algebras; consequently no novelty is claimed for the mere sandwich description or automorphism formulas. The present statement concerns explicit nonzero Hochschild cohomology directions, their simultaneous associative integrability, and flat smoothings from rank-one band algebras to full matrix algebras. The inspected homomorphism theorem does not state these cohomology or deformation conclusions. Their noncoverage by all earlier literature is not independently certified.

## Limitations
The injection does not determine the full \(HH^2(A,A)\) and no miniversal deformation is claimed. The generic full-matrix identification requires equal row and column cardinalities; rectangular cases still admit the displayed multi-parameter flat associative deformation. A preexisting deformation or cohomology calculation in specialized historical Munn-algebra literature could imply the result; this remains a publication-priority risk. Independent mathematical audit has not been carried out.

## References
- Margolis, S. W., and Steinberg, B., *Quivers of monoids with basic algebras*, arXiv:1101.0416, first publicly posted January 2, 2011, https://arxiv.org/abs/1101.0416. Section concerning rectangular bands and monoid quivers.
- Soroushmehr, M., *Homomorphisms of ℓ¹-Munn algebras and applications to semigroup algebras*, Bulletin of the Australian Mathematical Society 92 (2015), 115–122, DOI 10.1017/S0004972715000210, particularly Theorem 2.1.
- Esslamzadeh, G. H., *Homomorphisms of ℓ¹-Munn algebras and Rees matrix semigroup algebras*, Semigroup Forum (2016), DOI 10.1007/s00233-016-9774-0, especially Theorem 2.1 and Proposition 2.2.
- Araújo, J., Bünau, P., Mitchell, J. D., and Neunhöffer, M., *Computing automorphisms of semigroups*, preprint, https://www.math.rwth-aachen.de/~Max.Neunhoeffer/Publications/pdf/computing14.pdf; semigroup automorphisms rather than algebra deformation.
