# The Gorenstein symbolic defect of the ten nodes of the Segre cubic

## Finding

Let \(k\) be any field of characteristic zero, and put
\[
R=k[x_0,x_1,x_2,x_3,x_4],\qquad s=\sum_{i=0}^4 x_i,\qquad F=\sum_{i=0}^4x_i^3-s^3.
\]
Write \(Z\subset\mathbb P^4_k\) for the ten ordinary double points of \(V(F)\), and \(I=I(Z)\) for their saturated homogeneous ideal. Then
\[
I=(x_1^2-x_0^2,x_2^2-x_0^2,x_3^2-x_0^2,x_4^2-x_0^2,s^2-x_0^2),
\qquad \boxed{I^{(2)}=I^2+(F)}.
\]
Here \(I^{(2)}=\bigcap_{P\in Z}\mathfrak m_P^2\) is the second *symbolic* power, not ordinary squaring. More precisely, the graded \(R\)-module \(M=I^{(2)}/I^2\) is cyclic on \([F]\) of degree three, and its degree-three, degree-four, degree-five components have dimensions \((1,5,1)\), with all higher degrees zero. After shifting by three degrees, \(M\) is a graded Artinian Gorenstein algebra. In coordinates \(x_0,\ldots,x_4\), its socle-normalized multiplication pairing on degree one is
\[
\boxed{B=\tfrac15(6I_5-J_5),\qquad\det B=\tfrac{1296}{3125}\ne0,}
\]
where \(J_5\) is the all-ones matrix. Thus every diagonal entry is \(1\), and every off-diagonal entry is \(-1/5\).

The doubled-point scheme has length fifty and Hilbert series
\[
\boxed{H_{R/I^{(2)}}(t)=\frac{1+4t+10t^2+19t^3+16t^4}{1-t}}.
\]
Its Hilbert function is \((1,5,15,34,50,50,\ldots)\). Its homogeneous ideal has exactly one minimal cubic generator and fifteen minimal quartic generators.

## Assumptions and scope

All claims are valid over fields of characteristic zero (not merely over \(\mathbb C\)). The displayed hypersurface is the standard six-coordinate Segre cubic \(\sum_{i=0}^5X_i=\sum_{i=0}^5X_i^3=0\) after eliminating \(X_5=-s\). The ten nodes lie in the affine chart \(x_0=1\). They are the projective points \(P_A=[1:\epsilon_1:\epsilon_2:\epsilon_3:\epsilon_4]\), indexed by all \(A\subset\{1,2,3,4\}\) of cardinality one or two, with \(\epsilon_i=1\) for \(i\in A\) and \(-1\) otherwise.

The ideal equality holds in the entire polynomial ring \(R\), without an omitted saturation. The Gorenstein assertion concerns the shifted *symbolic defect module* with its induced multiplication, not the homogeneous coordinate ring of the doubled scheme.

## Proof

**1. The ten-point ideal.** Define \(q_i=x_i^2-x_0^2\) for \(1\le i\le4\), and \(q_5=s^2-x_0^2\), and put \(Q=(q_1,\ldots,q_5)\). Every \(P_A\) annihilates the five quadrics. Conversely, the first four equations, on \(x_0\ne0\), force each \(x_i/x_0\) to be \(\pm1\), and the fifth forces \(s/x_0\in\{\pm1\}\), giving exactly those ten points. The exact Gröbner calculation described below gives an initial ideal with seven monomial generators none divisible by \(x_0\), whose standard monomial degrees in the other variables have dimensions \((1,4,5)\). Thus \(R/Q\) is free of rank ten over \(k[x_0]\). Since there are ten distinct reduced points in \(x_0\ne0\), localization at \(x_0\) is their reduced coordinate ring; freeness rules out any extra components or nilpotents on \(x_0=0\). Therefore \(Q=I\) as homogeneous ideals. The gradients \(\partial F/\partial x_i=3(x_i^2-s^2)\) vanish at each of the ten points; these are precisely the classical nodes of the Segre cubic.

**2. A cubic in the symbolic square.** The exact identity
\[
F=\sum_{i=1}^4x_iq_i-sq_5
\]
puts \(F\) in \(I\); gradient vanishing makes it vanish to order at least two at every \(P_A\), so \(F\in I^{(2)}\). Hence \(J=I^2+(F)\subseteq I^{(2)}\).

**3. Equality without saturation.** Over \(\mathbb Q\), a reduced degree-reverse-lexicographic Gröbner basis for \(J\), with variable order \(x_1>x_2>x_3>x_4>x_0\), has twenty leading monomials, all involving only \(x_1,\ldots,x_4\). The corresponding finite standard-monomial staircase has graded dimensions \((1,4,10,19,16)\), then zeros. Therefore \(R/J\) is a free \(\mathbb Q[x_0]\)-module of rank \(1+4+10+19+16=50\). The same initial-ideal argument commutes with any characteristic-zero field extension. On the other hand, the quotient by \(I^{(2)}\), which defines ten disjoint first-order neighborhoods of points in \(x_0=1\), has rank \(10\binom{4+1}{4}=50\) after inverting \(x_0\). It is a quotient of the free \(k[x_0]\)-module \(R/J\). Its kernel must be torsion because ranks coincide, but a free module over \(k[x_0]\) has no torsion submodules. Thus \(J=I^{(2)}\), including the full homogeneous ideal, rather than only its saturation. The same staircase proves the claimed Hilbert series and length.

**4. Integral multiplication structure of the defect.** The class \([F]\) generates \(M=I^{(2)}/I^2\). Reduce \(Fx_ix_j\) modulo the exact Gröbner basis of \(I^2\), and let \(\eta=[Fx_0^2]\). The resulting exact identities are
\[
[Fx_ix_j]=\begin{cases}\eta,&i=j,\\-\eta/5,&i\ne j,\end{cases}
\qquad [Fx_ix_jx_\ell]=0\quad(0\le i,j,\ell\le4).
\]
The five classes \([Fx_i]\) are independent, and \(\eta\ne0\). Thus the shifted cyclic algebra \(M(3)\) has Hilbert function \((1,5,1)\). Its degree-one multiplication pairing is \(B=(6I_5-J_5)/5\), whose eigenvalues are \(6/5\) (multiplicity four) and \(1/5\) (multiplicity one); hence it is nondegenerate and the algebra is Gorenstein, with one-dimensional socle in degree two. The identities show that every higher-degree product vanishes. The generators of \(I^2\) in degree four are the fifteen linearly independent \(q_iq_j\) for \(i\le j\); together with \(F\) in degree three, these form the stated minimal homogeneous generating set for \(I^{(2)}\).

## Verification

The standalone `verify.py` uses exact rational SymPy Gröbner bases. It independently checks the ten points and their first derivatives, computes the two initial monomial ideals and their finite staircases, obtains direct rank \(34\) for cubic first-jet interpolation and rank \(50\) for quartic first-jet interpolation, then recomputes every degree-two pairing, all cubic annihilation relations, and the determinant \(1296/3125\). It needs Python 3 and SymPy 1.14 or a compatible version. Execute `python verify.py` in a directory containing that file; the success marker is `VERIFY_OK`. The expected exact output is provided as `verification_output.txt`. The Gröbner computations over \(\mathbb Q\) supply certificates for characteristic-zero identities; finite rank checks alone would not prove the entire infinite family.

## Relationship to prior work

The Segre cubic, its ten nodes, and its symmetric equations are classical; see Dolgachev (2015). Bocci and Harbourne (2009) explain the general distinction between ordinary and symbolic powers of point ideals and related containment phenomena, primarily for planar point configurations. These geometric facts and general frameworks do not themselves specify the entire second symbolic power, the complete doubled-node Hilbert series, or the Gorenstein symbolic defect calculated here. The assessed claim is that explicit degree-three-to-five defect structure, rather than the classical existence of the ten nodes.

## Limitations

The result treats the second symbolic power of this distinguished ten-point configuration in characteristic zero; no claim is made about all higher symbolic powers, symbolic resurgence, the reduction in small positive characteristics, or deformation families of other ten-node cubic threefolds. Although the searches described in the accompanying review did not locate an equivalent computation, historic priority has not been independently certified. A relevant 1936 paper of Baker on polarities of the nodes was available only bibliographically, and its complete text was not assessed.

## References

1. C. Bocci and B. Harbourne, *The resurgence of ideals of points and the containment problem*, arXiv:0906.4478v1, first public 24 June 2009. https://arxiv.org/html/0906.4478v1
2. I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432v1, first public 26 January 2015. https://arxiv.org/abs/1501.06432
3. H. F. Baker, *Polarities for the nodes of a Segre cubic primal in space of four dimensions*, Proceedings of the Cambridge Philosophical Society (1936), DOI:10.1017/S0305004100019253. Bibliographic/abstract record only.
