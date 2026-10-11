# A sharp Löwner contact-orbit transition for second partial permutohedra

## Finding

For every integer \(m\ge 2\), let the second partial permutohedron be
\[
P_m=\mathcal P(m,2)
=\operatorname{conv}\!\bigl(\{0\}\cup\{2e_i:1\le i\le m\}\cup
\{2e_i+e_j:1\le i\ne j\le m\}\bigr).
\]
Write \(\mathbf1=(1,\ldots,1)^{\mathsf T}\), \(H=\mathbf1\mathbf1^{\mathsf T}/m\), and \(I\) for the \(m\)-dimensional identity.

**Theorem.** The unique minimum-volume enclosing Euclidean ellipsoid (Löwner ellipsoid) of \(P_m\) is
\[
\mathcal E_m=\left\{x\in\mathbb R^m:
(x-t_m\mathbf1)^{\mathsf T}Q_m^{-1}(x-t_m\mathbf1)\le1\right\},
\qquad Q_m=u_mH+v_m(I-H),
\]
where
\[
(t_m,u_m,v_m)=
\begin{cases}
\left(\dfrac4{m+3},\dfrac{16m}{(m+3)^2},
                   \dfrac{16m}{3(m+3)}\right),&2\le m\le5,\\[8pt]
\left(\dfrac3{m+1},\dfrac{9m}{(m+1)^2},
                   \dfrac{m(5m-9)}{(m-1)(m+1)}\right),&m\ge6 .
\end{cases}
\]
All parameters \(u_m,v_m\) are strictly positive. The two parameter formulas coincide at \(m=5\).

For \(2\le m\le5\), **all** \(m^2+1\) vertices of \(P_m\) touch \(\partial\mathcal E_m\). For every \(m\ge6\), **exactly** the origin and the \(m(m-1)\) vertices \(2e_i+e_j\) with \(i\ne j\) touch; the \(m\) vertices \(2e_i\) lie strictly inside. Thus the contact orbit of single-support vertices disappears sharply between dimensions five and six. The minimum enclosing ellipsoid has Euclidean volume
\[
\operatorname{vol}_m(\mathcal E_m)=\kappa_m\sqrt{u_m\,v_m^{m-1}},
\qquad
\kappa_m=\frac{\pi^{m/2}}{\Gamma(1+m/2)}.
\]

## Assumptions and scope

Coordinates are taken in the standard Euclidean inner product on \(\mathbb R^m\); ellipsoid volume is ambient \(m\)-dimensional Euclidean volume. The definition of \(\mathcal P(m,n)\) is the convex hull of vectors in \(\{0,\ldots,n\}^m\) whose nonzero entries are distinct. At \(n=2\), the displayed vertex list is exact, and equivalently
\[
P_m=\left\{x\in\mathbb R^m:0\le x_i\le2,\
\sum_{i=1}^{m}x_i\le3\right\}.
\]
Indeed, in an intersection of the coordinate box with the sum half-space, a vertex either has all coordinates at box bounds or has the sum constraint active and at most one coordinate between \(0\) and \(2\). The upper bound \(3\) then permits precisely the three stated vertex types. Each listed vertex is exposed by independent active constraints. The statement holds for all integers \(m\ge2\), without an asymptotic or generic-position assumption.

## Proof

**1. Three symmetry orbits and candidate gauges.** Partition the vertices into \(O=\{0\}\), \(A=\{2e_i\}\), and \(B=\{2e_i+e_j:i\ne j\}\). For any \(x\) with coordinate sum \(k\) and squared Euclidean norm \(s\), orthogonal projection onto \(\mathbb R\mathbf1\) and its perpendicular complement gives
\[
q_m(x):=(x-t_m\mathbf1)^{\mathsf T}Q_m^{-1}(x-t_m\mathbf1)
=\frac{(k-mt_m)^2}{m u_m}
 +\frac{s-k^2/m}{v_m}.
\]
The orbit data \((k,s)\) are \((0,0)\) on \(O\), \((2,4)\) on \(A\), and \((3,5)\) on \(B\). Direct substitution of the theorem's rational formulas gives
\[
q_m(0)=1,\qquad q_m(2e_i+e_j)=1
\]
in both regimes. It also gives
\[
q_m(2e_i)=
\begin{cases}
1,&2\le m\le5,\\[2pt]
1-\dfrac{4(m-5)(m+1)}{9m(5m-9)},&m\ge6.
\end{cases}
\]
The last subtracted term is strictly positive for every \(m\ge6\). Every vertex therefore belongs to \(\mathcal E_m\), so its convex hull \(P_m\) does also; the stated contact classification follows exactly.

**2. Explicit contact moment certificates.** Construct a probability distribution supported on the vertex set, uniform within \(A\) and within \(B\). Set the *total* mass of these orbits to \(p_A,p_B\), and the origin mass to \(p_0\), as follows:
\[
(p_0,p_A,p_B)=
\begin{cases}
\left(\dfrac{m^2-4m+27}{3(m+3)^2},
      \dfrac{2m(5-m)}{(m+3)^2},
      \dfrac{8m(m-1)}{3(m+3)^2}\right),&2\le m\le5,\\[10pt]
\left(\dfrac1{m+1},0,\dfrac m{m+1}\right),&m\ge6.
\end{cases}
\]
They are nonnegative, sum to one, and all positive-mass vertices satisfy \(q_m(x)=1\). The zero \(A\)-weight at \(m=5\) causes no difficulty, since the \(A\)-vertices still touch.

Let \(X\) be a random vertex with those weights, and let \(\mu=\mathbb E X\). Permutation symmetry and the orbit sums imply
\[
\mu=\frac{2p_A+3p_B}{m}\mathbf1=t_m\mathbf1 .
\]
Write \(\Sigma=\mathbb E[(X-\mu)(X-\mu)^{\mathsf T}]\). In the radial subspace, the eigenvalue of \(m\Sigma\) is the variance of the coordinate sum, namely
\[
4p_A+9p_B-(2p_A+3p_B)^2=u_m.
\]
On the \((m-1)\)-dimensional coordinate-sum-zero subspace, the eigenvalue of \(m\Sigma\) equals
\[
\frac{m}{m-1}\,\mathbb E\!\left[\lVert X-HX\rVert_2^2\right]
=4p_A+\frac{5m-9}{m-1}p_B=v_m.
\]
Substitution of the displayed orbit weights verifies both identities in each range, so
\[
\boxed{\mathbb E X=t_m\mathbf1,\qquad
       \operatorname{Cov}(X)=Q_m/m.}
\]
This calculation supplies an explicit optimality certificate in every dimension; it does not rely on finite enumeration.

**3. Global minimum volume and uniqueness.** Let any other ellipsoid containing \(P_m\) have center \(b\in\mathbb R^m\) and positive-definite squared-semiaxis matrix \(R\). At every support point of the above probability distribution,
\((X-b)^{\mathsf T}R^{-1}(X-b)\le1\). Averaging yields
\[
1\ge \frac1m\operatorname{tr}(R^{-1}Q_m)
  +(t_m\mathbf1-b)^{\mathsf T}R^{-1}(t_m\mathbf1-b).
\]
In particular \(\operatorname{tr}(R^{-1}Q_m)\le m\). The eigenvalue arithmetic–geometric-mean inequality for \(R^{-1/2}Q_mR^{-1/2}\) gives
\[
\left(\frac{\det Q_m}{\det R}\right)^{1/m}
\le\frac1m\operatorname{tr}(R^{-1}Q_m)\le1 .
\]
Hence \(\det R\ge\det Q_m\), precisely the assertion that the volume of the other ellipsoid is at least that of \(\mathcal E_m\). Equality forces \(b=t_m\mathbf1\) and every eigenvalue of \(R^{-1/2}Q_mR^{-1/2}\) to equal one, hence \(R=Q_m\). This proves both global optimality and uniqueness among **all** ellipsoids, without assuming the competitor has coordinate-permutation symmetry.

**4. Volume.** The eigenvalues of \(Q_m\) are \(u_m\) once and \(v_m\) with multiplicity \(m-1\). Therefore \(\det Q_m=u_mv_m^{m-1}\), proving the stated volume formula.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library and exact rational arithmetic. Run `python3 verify.py`. It checks all scalar rational identities and contact inequalities in every integer dimension \(2\le m\le100\), and independently constructs the complete vertex set, distribution, center, full covariance matrix, and all contact gauges for every dimension \(2\le m\le15\). It should print `PASS: 99 exact dimension formulas and 14 independent full-matrix/contact enumerations.` These finite checks provide reproducible safeguards against algebraic errors; the all-dimensional proof is the moment-certificate and determinant argument above.

## Relationship to prior work

Heuer and Striker, *Partial permutation and alternating sign matrix polytopes* (arXiv:2012.09901, 2020), introduce the partial permutohedra and give vertex, facet, and face-lattice descriptions. Behrend, Castillo, Chavez, Diaz-Lopez, Escobar, Harris, and Insko, *Partial permutohedra* (arXiv:2207.14253, first public version 2022), especially Proposition 2.7 and Theorem 5.11, establish the second partial permutohedron's vertex and inequality descriptions and calculate Ehrhart and ordinary volume quantities. The results inspected there do not state or imply the exact minimum-volume *enclosing ellipsoid* or its vertex-contact transition. The optimality proof here is an application of elementary moment and determinant inequalities to a newly evaluated probability distribution; generic Löwner optimality criteria alone do not evaluate the required orbit weights and dimension threshold.

## Limitations

This classification concerns only \(\mathcal P(m,2)\), not arbitrary \(\mathcal P(m,n)\), and fixes the standard Euclidean metric. It does not classify other enclosing shapes or inscribed ellipsoids. The literature comparison is limited to the named primary works and targeted searches; an equivalent treatment under different terminology for capped or box-truncated simplices remains possible. The computer checks are finite and are not independently certified; the proof above is the basis for the universal claim.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first submitted 17 December 2020. https://arxiv.org/abs/2012.09901
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253, first submitted 28 July 2022; see Proposition 2.7, Theorem 5.11, and its proof. https://arxiv.org/abs/2207.14253
