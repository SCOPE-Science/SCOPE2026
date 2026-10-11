# Graph-spectral transfer for transposition sampling in the standard Fourier block of the symmetric group

## Finding

Let \(n\ge4\) and write \(G=S_n\). Let \(H\subset L^2(G)\) be the full matrix-coefficient space of the complexified standard representation, and let \(P_H\) be its orthogonal projection. For a simple graph \(\Gamma\) on the labelled vertex set \([n]\), write \(E\) for its edge set, \(m=|E|\), and \(T_E=\{(ij):\{i,j\}\in E\}\). The concentration operator is
\[
 C_E=(P_H M_{\mathbf1_{T_E}}P_H)|_H.
\]
Write \(B\in\{0,1\}^{n\times m}\) for the unsigned incidence matrix (each column has two ones), \(J_m=\mathbf1_m\mathbf1_m^{\mathsf T}\), and
\[
 Q_E=2I_m+B^{\mathsf T}B+(n-5)J_m.
\]
**Transposition sampling theorem.** For every such graph, \(Q_E\) is positive definite and
\[
 \operatorname{spec}(C_E)=\frac{n-1}{n!}\operatorname{spec}(Q_E)
 \ \sqcup\ \{0^{[(n-1)^2-m]}\},
 \qquad \operatorname{rank}(C_E)=m.
\]
Here \(\sqcup\) denotes union of eigenvalue multisets, and a bracketed exponent denotes multiplicity; for \(m=0\), the positive multiset is empty. Thus every prescribed complex function on the edge transpositions is the restriction of a function in \(H\).

For \(n\ge5\), let \(b(\Gamma)\) be the number of bipartite connected components of \(\Gamma\), with isolated vertices counted as bipartite components. Then \(2\) occurs in \(\operatorname{spec}(Q_E)\) with **exact multiplicity**
\[
 m-n+b(\Gamma).
\]
In particular, the bottom concentration eigenspace detects the nullity of the unsigned incidence map, including its even-cycle relations.

If \(\Gamma\) is \(r\)-regular, \(r\ge2\), and its adjacency eigenvalues are \(r=\lambda_1,\lambda_2,\ldots,\lambda_n\), where the first eigenvector is chosen constant, then \(m=nr/2\) and
\[
 \operatorname{spec}(Q_E)=
 \left\{(n-5)m+2r+2\right\}
 \sqcup\!\bigsqcup_{i=2}^n\left\{r+\lambda_i+2\right\}
 \sqcup\left\{2^{[m-n]}\right\}.
\]
Consequently, for fixed \(n\) and \(r\), **adjacency cospectrality and concentration cospectrality are equivalent**. For \(n\ge6\), \(r\ge3\), the largest eigenvalue of \(Q_E\) is \((n-5)m+2r+2\), the smallest is \(2\), and the exact nonzero singular-value condition number of the normalized restriction map is
\[
 \kappa=\sqrt{\frac{(n-5)m+2r+2}{2}}.
\]
Thus this sharp condition number depends on \(n\) and \(r\), but not on the regular graph's detailed topology, even though its intermediate sampling spectrum determines its adjacency spectrum.

For the complete graph \(\Gamma=K_n\), with \(m=\binom n2\), the entire rescaled positive eigenvalue multiset is
\[
 \left\{\left[\frac{n(n-3)^2}{2}\right]^{[1]},\ n^{[n-1]},\ 2^{[n(n-3)/2]}\right\}.
\]
The sampling kernel in \(H\) is exactly the subspace represented by skew-symmetric \((n-1)\)-by-\((n-1)\) coefficient matrices in a real orthonormal basis of the standard representation.

## Assumptions and scope

Equip \(L^2(S_n)\) with \(\langle f,g\rangle=(n!)^{-1}\sum_{s\in S_n}f(s)\overline{g(s)}\). Let
\[
 V=\{z\in\mathbb C^n:\sum_{i=1}^n z_i=0\},\qquad d=n-1,
\]
and let \(\rho:S_n\to O(V_{\mathbb R})\) be the natural real orthogonal representation restricted to the zero-sum hyperplane. Its complexification is irreducible. The coefficient space is \(H=\operatorname{span}_{\mathbb C}\{\rho_{ab}:1\le a,b\le d\}\), and \(\dim H=d^2\). Matrix indices refer to one real orthonormal basis of \(V_{\mathbb R}\).

The restriction operator is \(R_E:H\to\mathbb C^E\), \((R_Ef)_e=f((ij))/\sqrt{n!}\). Then \(R_E^*R_E=C_E\), where the target uses its usual unweighted Euclidean inner product. Thus the nonzero eigenvalues of \(C_E\) are squared singular values of \(R_E\). The theorem does not assert interpolation for an arbitrary Fourier block, nor does it assert that the displayed graph Fourier concentration distinguishes all nonisomorphic graphs.

## Proof

**1. Matrix-coefficient sampling Gram.** By Schur orthogonality, \(u_{ab}(s)=\sqrt d\,\rho_{ab}(s)\), for \(1\le a,b\le d\), forms an orthonormal basis of \(H\). Every \(\rho(t_e)\) is real symmetric because a transposition is an orthogonal involution. Consequently,
\[
 (R_ER_E^*)_{ef}=\frac d{n!}\sum_{a,b}\rho_{ab}(t_e)\rho_{ab}(t_f)
 =\frac d{n!}\operatorname{tr}(\rho(t_et_f))
 =\frac d{n!}\chi(t_et_f).
\]
The standard character is \(\chi(s)=\#\operatorname{Fix}(s)-1\). If \(e=f\), then \(t_et_f=1\) and \(\chi=n-1\); if two distinct edges meet, their product is a three-cycle, so \(\chi=n-4\); if disjoint, their product consists of two transpositions, so \(\chi=n-5\). Since \((B^{\mathsf T}B)_{ef}\) is \(2\) for \(e=f\), \(1\) when \(e,f\) meet, and \(0\) otherwise, these three cases give the exact matrix identity
\[
 R_ER_E^*=\frac{n-1}{n!}(2I_m+B^{\mathsf T}B+(n-5)J_m).
\]
Nonzero spectra of \(R_E^*R_E\) and \(R_ER_E^*\) agree, including multiplicities.

**2. Strict positivity for every edge set.** First let \(E\) contain all \(\binom n2\) edges. The complete-graph incidence matrix satisfies
\[
 BB^{\mathsf T}=(n-2)I_n+J_n.
\]
It has rank \(n\), and \(B^{\mathsf T}B\) has eigenvalues \(2(n-1)\) once, \(n-2\) with multiplicity \(n-1\), and \(0\) with multiplicity \(m-n\). Its constant edge vector is the eigenvector for \(2(n-1)\) and \(J_m\) vanishes on the orthogonal complement. Therefore \(Q_{K_n}\) has eigenvalues \(n(n-3)^2/2\) once, \(n\) with multiplicity \(n-1\), and \(2\) with multiplicity \(m-n=n(n-3)/2\). All are strictly positive for \(n\ge4\). For an arbitrary \(E\), \(Q_E\) is a principal submatrix of \(Q_{K_n}\), hence positive definite (including the vacuous empty case). Thus \(\operatorname{rank} R_E=m\), and the displayed spectrum and interpolation follow. The dimensional inequality \(m\le d^2\) holds for \(n\ge4\).

**3. Exact bottom-eigenvalue multiplicity.** For \(n\ge5\),
\[
 Q_E-2I_m=B^{\mathsf T}B+(n-5)J_m\succeq0.
\]
As \(\mathbf1_n^{\mathsf T}B=2\mathbf1_m^{\mathsf T}\), we have \(\ker B\subset\ker J_m\); hence \(\ker(Q_E-2I_m)=\ker B\). The left nullspace of \(B\) consists of vertex vectors \(y\) satisfying \(y_u+y_v=0\) along every edge. Each bipartite connected component allows precisely one independent alternating scalar assignment, while a component containing an odd cycle allows none. Isolated vertices each contribute one. Thus \(\operatorname{rank}B=n-b(\Gamma)\) and \(\dim\ker B=m-n+b(\Gamma)\), proving the exact multiplicity. When this number is zero, \(2\) is not an eigenvalue.

**4. Regular-graph spectral transfer and conditioning.** If \(\Gamma\) is \(r\)-regular, then
\[
 BB^{\mathsf T}=rI_n+A_\Gamma,
 \qquad B\mathbf1_m=r\mathbf1_n,
 \qquad B^{\mathsf T}\mathbf1_n=2\mathbf1_m.
\]
Consequently \(B^{\mathsf T}B\mathbf1_m=2r\mathbf1_m\). Its remaining \(m-1\) eigenvalues, counting zeros, are the \(n-1\) numbers \(r+\lambda_i\) for \(i\ge2\) together with \(m-n\) zeros. On \(\mathbf1_m\) the rank-one matrix \(J_m\) adds \((n-5)m\); on the perpendicular space it vanishes. This gives the claimed complete regular-graph spectral formula, including disconnected and bipartite graphs and coincident eigenvalues. Deleting one known eigenvalue \((n-5)m+2r+2\) and \(m-n\) copies of \(2\), then subtracting \(r+2\) from the remaining \(n-1\) eigenvalues, recovers the adjacency spectrum other than the chosen leading \(r\). This proves both directions of cospectral equivalence.

Finally, if \(n\ge6\) and \(r\ge3\), then \(m>n\) and the \(m-n\) copies of \(2\) ensure the minimum is \(2\) (all other eigenvalues are at least \(2\), because \(\lambda_i\ge-r\)). The top eigenvalue is \((n-5)m+2r+2\), since each \(r+\lambda_i+2\le2r+2\) and \((n-5)m>0\). The factor \((n-1)/n!\) cancels from the ratio of nonzero singular values, yielding the exact condition number.

**5. Complete-class kernel.** Every matrix \(\rho(t_e)\) is symmetric. Thus coefficient functions of the form \(g\mapsto\operatorname{tr}(A^{\mathsf T}\rho(g))\) with skew-symmetric \(A\) vanish on all transpositions. This space has dimension \(d(d-1)/2\), precisely the nullity \(d^2-\binom n2\) established in step 2. It is therefore the entire restriction kernel for the complete transposition class.

## Verification

The supplied standalone standard-library program `verify.py` checks the three character-value cases and the incidence Gram identity for all edge subsets on four vertices and for 360 deterministic sample masks on five through eight vertices, 424 masks in total. It checks complete-graph eigenvector identities for \(4\le n\le9\), and the unsigned-incidence rank formula on all 424 masks; it also tests regular-graph row sums and adjacency-incidence identities on 17 families/instances. It reports

`VERIFY_OK complete_n=4..9 (6) arbitrary_edge_masks=424 regular_graphs=17 exceptional_n3_rank=2`

The computations are finite consistency tests, not proof of the all-size statement. The proof above rests on Schur orthogonality, elementary character values, exact incidence identities, and matrix spectral arguments. The checker records that \(n=3\) falls outside the theorem's positivity threshold.

## Relationship to prior work

Scarabotti and Tolli develop finite harmonic analysis on homogeneous spaces, matrix-coefficient and spherical-function methods, and explicit symmetric-group examples. Their inspected general framework supplies the relevant setting but does not state a graph-indexed transposition sampling Gram formula or the regular-graph concentration-to-adjacency spectral equivalence. Krebs and Shaheen give a representation-theoretic derivation of the Johnson-graph spectrum; the complete two-subset geometry behind \(B^{\mathsf T}B\) is classical, whereas the restriction of a noncommutative Fourier block to arbitrary graph-chosen transpositions and its sharp sampling conclusions are additional statements here. An inspected published result on conjugate phase retrieval from difference-plus-mean permutation orbits concerns nonlinear vector measurements rather than this linear coefficient-space compression. The theorem explicitly uses rather than reclaims the classical matrix-coefficient orthogonality and incidence/line-graph spectral facts.

## Limitations

The theorem treats the complete standard-isotypic matrix-coefficient block and locations that are transpositions, not higher symmetric-group representations or general permutation classes. It establishes exact singular values but does not supply noise-stability results outside the stated normalized restriction problem. The regular-graph spectral reconstruction is spectral rather than graph-isomorphism reconstruction. The first public date below belongs to the literature anchor, not to this theorem. A different formulation of these identities in classical representation/frame or line-graph literature remains possible and would affect the originality assessment.

## References

1. F. Scarabotti, F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1 (first public 2007-01-19), especially matrix-coefficient harmonic analysis and symmetric-group examples; later Proceedings of the London Mathematical Society 100 (2010), 348–376, DOI 10.1112/plms/pdp027.
2. M. Krebs, A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra 17 (2008), 154–167, DOI 10.13001/1081-3810.1256.
3. D. Bartusel, H. Führ, V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123 (first public 2021-09-15), especially the difference-plus-mean permutation-orbit problem; a related published difference-plus-mean result was inspected for distinction of objects and implications.
