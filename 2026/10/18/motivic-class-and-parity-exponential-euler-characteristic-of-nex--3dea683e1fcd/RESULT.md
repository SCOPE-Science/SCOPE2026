# Motivic class and parity-exponential Euler characteristic of next-to-banana symmetric hypersurfaces

## Finding

Let \(k\) be an algebraically closed field of characteristic zero, let \(n\ge5\), and put
\[
X_n=V(e_{n-2}(x_1,\ldots,x_n))\subset\mathbb P_k^{n-1},\qquad
 e_r(x_1,\ldots,x_n)=\sum_{|I|=r}\prod_{i\in I}x_i.
\]
Let \(\mathbb L=[\mathbb A^1_k]\) in the Grothendieck ring \(K_0(\operatorname{Var}_k)\). For \(m\ge2\), define the integer polynomial
\[
H_m(T)=\frac{(T-1)^{m-1}+(-1)^m}{T}.
\]
Then \(X_n\) is geometrically integral and its Grothendieck class equals
\[
\boxed{[X_n]=\sum_{s=1}^{n-3}\binom ns(\mathbb L-1)^{s-1}
+nH_{n-1}(\mathbb L)+H_n(\mathbb L)
+(-1)^n\sum_{j=1}^{\lfloor n/2\rfloor}\binom n{2j}\mathbb L^{j-1}
+(-1)^{n-1}n.}
\]
The equality is in \(K_0(\operatorname{Var}_k)\), not merely after Euler-characteristic realization. Over \(k=\mathbb C\), applying the Hodge–Deligne realization gives the full compactly supported Hodge–Deligne polynomial by replacing \(\mathbb L\) with \(uv\). In particular,
\[
\boxed{\chi(X_n(\mathbb C))=\begin{cases}2^{n-1}-n,&n\text{ even},\\ -2^{n-1}+3n,&n\text{ odd}.\end{cases}}
\]
For the first four cases, \([X_5]=\mathbb L^3+\mathbb L^2-4\mathbb L+1\),
\([X_6]=\mathbb L^4+\mathbb L^3+7\mathbb L^2+16\mathbb L+1\),
\([X_7]=\mathbb L^5+\mathbb L^4+15\mathbb L^3-27\mathbb L^2-34\mathbb L+1\), and
\([X_8]=\mathbb L^6+\mathbb L^5+29\mathbb L^4-68\mathbb L^3+85\mathbb L^2+71\mathbb L+1\).

## Assumptions and scope

The ground field must be algebraically closed of characteristic zero for the uniform split-quadric class calculation. The polynomial \(e_{n-2}\) is defined with unit coefficients, and \(n\ge5\). The Grothendieck ring uses scissor relations for reduced separated finite-type \(k\)-varieties; every coordinate stratum is reduced. The result concerns the full projective hypersurface, not solely its dense torus or the complement. Over general finite fields, smooth quadrics can be nonsplit; substitution of the field size into the displayed Grothendieck polynomial does not generally count points.

## Proof

Fix a subset \(I\subset\{1,\ldots,n\}\) of cardinality \(s\). The corresponding exact-support locally closed stratum consists of points whose nonzero coordinate indices are exactly \(I\); its ambient class is \((\mathbb L-1)^{s-1}\). The strata are disjoint and exhaust projective space.

If \(1\le s\le n-3\), then every monomial of \(e_{n-2}\) vanishes, so the entire support stratum is contained in \(X_n\). If \(s=n-2\), the specialization of \(e_{n-2}\) is the product of the \(s\) nonzero coordinates, hence the stratum contributes nothing. For \(s=n-1\), coordinatewise inversion \(y_i=x_i^{-1}\) is an automorphism of the projective torus, and
\[
e_{n-2}(x_i:i\in I)=\Big(\prod_{i\in I}x_i\Big)\sum_{i\in I} y_i.
\]
The intersection of the projective hyperplane \(\sum y_i=0\) with the torus in \(\mathbb P^{s-1}\) has class
\[
H_s(\mathbb L)=\sum_{r=2}^{s}(-1)^{s-r}\binom sr\sum_{h=0}^{r-2}\mathbb L^h
=\frac{(\mathbb L-1)^{s-1}+(-1)^s}{\mathbb L}.
\]
The first equality is coordinate-hyperplane inclusion–exclusion. The last expression denotes a polynomial because its numerator has zero constant term. There are exactly \(n\) choices for the missing coordinate.

On the full-support stratum, inversion gives
\[
e_{n-2}(x_1,\ldots,x_n)=\Big(\prod_{i=1}^n x_i\Big)
\sum_{1\le i<j\le n}y_i y_j.
\]
Write \(Q_s\subset\mathbb P^{s-1}\) for the projective zero scheme of \(\sum_{i<j}y_iy_j\), restricted to \(s\) coordinates. For \(s=1\), this equation vanishes identically and \([Q_1]=1\). For every \(s\ge2\), its symmetric Hessian is the matrix \(J_s-I_s\), with determinant \((-1)^{s-1}(s-1)\ne0\) in characteristic zero. Thus \(Q_s\) is a nonsingular projective quadric. Standard affine cell decompositions of split quadrics over an algebraically closed field give
\[
[Q_s]=\sum_{h=0}^{s-2}\mathbb L^h
+\begin{cases}\mathbb L^{(s-2)/2},&s\text{ even},\\0,&s\text{ odd}.\end{cases}
\]
This includes \(s=2\), where the quadric comprises two points. It excludes \(s=1\), whose separate value is essential. The full-support contribution is obtained by deleting the \(n\) coordinate hyperplanes from \(Q_n\), hence
\[
T_n=\sum_{s=1}^n(-1)^{n-s}\binom ns[Q_s].
\]
Substituting the split-quadric formula and applying the same projective-hyperplane binomial identity gives
\[
T_n=H_n(\mathbb L)
+(-1)^n\sum_{j=1}^{\lfloor n/2\rfloor}\binom n{2j}\mathbb L^{j-1}
+(-1)^{n-1}n.
\]
The last term comes exactly from the \(s=1\) contribution; omitting that term would give an incorrect Euler characteristic. Adding the support-strata contributions establishes the boxed Grothendieck-ring identity.

It remains to note that \(X_n\) is integral. Since \(n\ge5\), the smooth nondegenerate quadric \(Q_n\) is irreducible, and its nonempty open dense torus section is irreducible. The other support strata in \(X_n\) have dimension at most \(n-3\), while any component of the projective hypersurface has dimension \(n-2\); hence no component lies in the coordinate boundary. The hypersurface has a unique generically smooth component, and its defining polynomial is squarefree, proving reducedness and irreducibility. Finally the motivic realization \(\mathbb L\mapsto uv\) proves the Hodge–Deligne assertion. For the topological Euler characteristic set \(\mathbb L=1\): all support strata of size at least two vanish, \(H_m(1)=(-1)^m\), and \(\sum_{j\ge1}\binom n{2j}=2^{n-1}-1\). Elementary simplification yields the displayed parity-dependent formula.

## Verification

The supplied standalone checker verifies the two independently derived finite polynomial expressions for every integer \(5\le n\le15\) by exact integer arithmetic, and checks the Euler specialization for the same range. It also exhaustively enumerates projective points over \(\mathbb F_7\), where \(\#X_5(\mathbb F_7)=365\) and \(\#X_6(\mathbb F_7)=3102\). The latter differs from the algebraically closed class polynomial specialized at seven by \(-2\cdot7^2\), exactly the nonsplit-quadric correction at the full-support stratum. The finite checks corroborate the proof but are not an all-integers or all-fields proof. Run `python3 check.py` without external packages.

## Relationship to prior work

Aluffi and Marcolli's 2008 banana-graph calculation determines motivic classes for \(e_{n-1}\), where inversion gives a hyperplane on the dense torus. Morales-Almazán's banana and flower computations also concern that different graph polynomial. Their torus-stratification approach motivates the present use of coordinate inversion, but neither inspected calculation provides the next-to-banana \(e_{n-2}\) class, whose top-dimensional inverse image is instead a smooth quadric. Bilgin studies classes of several other hypersurface families, with no equivalent all-\(n\) formula found in the inspected sections. General descriptions of reduced elementary-symmetric singular loci do not determine these motivic classes.

## Limitations

The theorem does not calculate integral cohomology groups, intersection pairings, the Jacobian scheme or mixed-Hodge extensions; the Hodge–Deligne polynomial is an alternating-sum invariant. No arbitrary-characteristic or arbitrary finite-field point-count formula is claimed. Literature indexing can miss equivalent formulations in broader motivic or graph-hypersurface studies; the comparison is not a proof that no prior equivalent theorem exists.

## References

1. P. Aluffi and M. Marcolli, *Feynman motives of banana graphs*, arXiv:0807.1690 (public v1 July 10, 2008), especially Section 3 and Theorem 3.10.
2. E. Bilgin, *Classes of some hypersurfaces in the Grothendieck ring of varieties*, arXiv:1112.2131 (2011), abstract and classification of treated families.
3. P. Morales-Almazán, *Grothendieck ring class of Banana and Flower graphs*, arXiv:1208.4129 (2012), Section 4.2.
4. *Singular locus of zero set of elementary symmetric polynomial*, MathOverflow question 264226 (2017), answers concerning the reduced singular support.
