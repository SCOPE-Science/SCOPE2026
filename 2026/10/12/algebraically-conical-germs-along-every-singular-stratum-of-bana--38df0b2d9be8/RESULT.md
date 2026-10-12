# Algebraically conical germs along every singular stratum of banana graph hypersurfaces

## Finding

For each integer \(n\ge4\), let \(X_n\subset\mathbb P^{n-1}_{\mathbb C}\) be the graph hypersurface of the banana graph with \(n\) parallel edges. Its Kirchhoff equation is
\[
\Psi_n(t_1,\ldots,t_n)=e_{n-1}(t_1,\ldots,t_n)=\sum_{i=1}^n\prod_{j\ne i}t_j=0.
\]
Here \(e_r\) denotes the elementary symmetric polynomial of degree \(r\), with \(e_0=1\). Let \(p\in X_n(\mathbb C)\) have precisely \(k\) zero homogeneous coordinates. Then \(2\le k\le n-1\). For \(k\ge3\), the germ of \(X_n\) at \(p\) admits an **algebraic** (Zariski-local, not merely first-order) change of coordinates taking its equation exactly to \(e_{k-1}(u_1,\ldots,u_k)=0\), with \(n-k-1\) additional free coordinates. Consequently
\[
\widehat{\mathcal O}_{X_n,p}\cong
\mathbb C[[u_1,\ldots,u_k,z_1,\ldots,z_{n-k-1}]]/(e_{k-1}(u_1,\ldots,u_k)).
\]
In particular the germ is isomorphic to its tangent cone, even at higher-multiplicity intersections of singular components. This exact local equivalence, not merely the tangent-cone formula, is the asserted contribution.

The singular support is \(\bigcup_{|I|=3}V(t_i:i\in I)\), consisting of \(\binom n3\) distinct irreducible linear components of dimension \(n-4\). At a point with precisely \(k\ge3\) zero coordinates, the multiplicity is \(k-1\) and the associated-graded Hilbert series is
\[
\operatorname{Hilb}_{\operatorname{gr}_{\mathfrak m_p}\mathcal O_{X_n,p}}(T)
=\frac{1-T^{k-1}}{(1-T)^{n-1}}.
\]
At a generic point of each singular component the transverse model is the nondegenerate quadratic cone \(e_2(u_1,u_2,u_3)=0\), i.e. an ordinary double point. The entire hypersurface is integral and normal. The support, multiplicities, and tangent cones are independently established or implied by prior graph-hypersurface results; they are recorded to explain the stronger analytic normal form.

## Assumptions and scope

All varieties and local rings are over \(\mathbb C\). The index ranges are \(n\ge4\) and \(3\le k\le n-1\) for singular points. All points considered in the asserted local normal forms are closed complex points. Every projective point of \(X_n\) has either exactly two zero coordinates, exactly three or more zero coordinates, or no zero coordinates. The two-zero and zero-zero cases are smooth; a point with exactly one zero coordinate does not belong to \(X_n\). The term “algebraically conical germ” means the specified regular, invertible change of affine coordinates on open neighborhoods of the point, up to multiplication of the defining equation by a unit. It does not claim the global variety is an affine cone or is locally a *linear* product in the original coordinates.

## Proof

**1. Exact decomposition of the local equation.** Fix \(p\) with zero-coordinate set \(I\), \(|I|=k\). Put \(J=\{1,\ldots,n\}\setminus I\), so \(J\ne\varnothing\). Choose \(j_0\in J\), work on the projective chart \(t_{j_0}=1\), and restrict to the open subset on which every \(t_j\), \(j\in J\), is invertible. Write the coordinates indexed by \(I\) as \(x_1,\ldots,x_k\). The remaining \(n-k-1\) coordinates are the nonzero \(t_j\), \(j\in J\setminus\{j_0\}\). Set
\[
U=\prod_{j\in J}t_j,\qquad c=\sum_{j\in J}\frac1{t_j}.
\]
These are regular functions on the chosen open set, and \(U\) is a unit. Sorting terms of \(\Psi_n\) by the index of the omitted factor gives the *exact* equality
\[
\Psi_n/U=e_{k-1}(x_1,\ldots,x_k)+c\,e_k(x_1,\ldots,x_k).
\]
This is an equality of regular functions, not a Taylor approximation.

**2. An invertible rational-to-regular coordinate change.** Regard \(x_k\) as the distinguished vanishing coordinate and put
\[
y=\frac{x_k}{1+c x_k};\qquad x_k=\frac{y}{1-cy}.
\]
The denominators are units at \(p\), since \(x_k(p)=y(p)=0\); after shrinking around \(p\), both maps are regular mutually inverse changes of affine coordinates, fixing all other variables, including the parameters on which \(c\) depends. Writing \(P=\prod_{i<k}x_i\) and \(S=e_{k-2}(x_1,\ldots,x_{k-1})\), the local defining function is \(P+x_k(S+cP)\). Substitution yields the exact identity
\[
(1-cy)\big(P+x_k(S+cP)\big)=P+yS=e_{k-1}(x_1,\ldots,x_{k-1},y).
\]
Therefore the equation is carried to the homogeneous polynomial \(e_{k-1}\), independent of the \(n-k-1\) nonzero-coordinate parameters. This proves the local algebraic product and the completed-local-ring isomorphism. Since the right-hand equation is homogeneous in the transverse variables, its tangent cone *is the entire local equation* in these new coordinates.

**3. Singular set, smooth cases, and components.** If exactly one coordinate vanishes, \(\Psi_n=U\ne0\). If exactly two vanish, the local equation above begins with \(x_1+x_2\), so the point is smooth. At a point with no zeros, writing \(\Psi_n=(\prod_i t_i)\sum_i t_i^{-1}\) shows on \(\Psi_n=0\) that \(\partial\Psi_n/\partial t_i=-(\prod_jt_j)t_i^{-2}\ne0\), hence smoothness. For \(k\ge3\), the lowest degree of the homogeneous polynomial \(e_{k-1}\) is \(k-1\ge2\); every first derivative vanishes. Thus precisely the points with at least three zero coordinates are singular. Their reduced support is the stated union of coordinate subspaces. Each such subspace has dimension \(n-4\) and distinct generic points, giving \(\binom n3\) irreducible components. A general point has exactly three zeros; \(e_2(u_1,u_2,u_3)=u_1u_2+u_1u_3+u_2u_3\) is a nondegenerate quadratic form in characteristic zero, giving the transverse node.

**4. Multiplicity, Hilbert series, and normality.** For \(k\ge3\), the lowest term of the local equation has degree \(k-1\) and is the full equation after the coordinate change. Thus the multiplicity is \(k-1\). A single homogeneous nonzero divisor of degree \(k-1\) in a polynomial ring in \(n-1\) variables has graded Hilbert series \((1-T^{k-1})/(1-T)^{n-1}\), proving the formula. Finally, \(e_{n-1}=P+t_n S\), where \(P=\prod_{i<n}t_i\) and \(S=e_{n-2}(t_1,\ldots,t_{n-1})\). Because \(\gcd(P,S)=1\) for \(n\ge3\), this polynomial is irreducible (a primitive linear polynomial in \(t_n\) over the polynomial coefficient ring). Thus \(X_n\) is integral. Its reduced singular locus has codimension two in \(X_n\) for \(n\ge4\); the hypersurface is Cohen–Macaulay (Serre \(S_2\)) and regular in codimension one (Serre \(R_1\)), hence normal.

## Verification

The standalone exact-arithmetic checker `checks/banana_local_checker.py` computes \(\Psi_n\) and its Jacobian on representative coordinate-support configurations, verifies the transformed polynomial identity over rational numbers, and independently enumerates graded standard monomials to check the Hilbert-function count. Its recorded output is `checks/output.txt`; run with `python checks/banana_local_checker.py`. It reports 1,002 support/Jacobian configurations, 176 exact rational transformed identities, and 135 independent graded-Hilbert comparisons. Every check passed. The infinite assertions are proved symbolically above; finite checks do not prove the global quantifiers.

## Relationship to prior work

Aluffi and Marcolli, *Feynman motives of banana graphs* (first posted 2008-07-10, arXiv:0807.1690), equation (1.28) and Lemma 3.8, give this polynomial and describe its intersection with the coordinate simplex; the coordinate incidence is not new. Patterson, *On the Singular Structure of Graph Hypersurfaces* (first posted 2010-04-29, arXiv:1004.5166), Theorem 4.13 and Proposition 4.17, establishes general rank/multiplicity correspondence and tangent-cone formulas for graph hypersurfaces, with an explicit four-edge example. The present claim is stricter: its displayed invertible nonlinear coordinate transformation removes **all higher-order terms** and supplies an actual algebraic local product isomorphism at **every** singular closed point. Neither a tangent-cone formula nor multiplicity data alone implies this analytic/contact equivalence. It is therefore essential not to treat the multiplicity, coordinate singular support, or tangent-cone descriptions independently as novel.

## Limitations

No classification is asserted for arbitrary graph hypersurfaces or for nonzero external momenta, deformed integrands, or other graph polynomials. The local model is stated at closed points and not as a globally glued trivialization of normal directions. The Hilbert series is for the associated graded local ring, not an independently claimed new motivic or Hodge invariant. A yet-unlocated equivalent explicit local trivialization could supersede the originality assessment.

## References

1. P. Aluffi and M. Marcolli, *Feynman motives of banana graphs*, arXiv:0807.1690v1 (2008-07-10), equation (1.28), Lemma 3.8, https://www.its.caltech.edu/~matilde/AluffiMarcolliCNTP.pdf .
2. E. Patterson, *On the Singular Structure of Graph Hypersurfaces*, arXiv:1004.5166v1 (2010-04-29), especially Theorem 4.13, Proposition 4.17, Example 4.19, https://arxiv.org/html/1004.5166v2 .
