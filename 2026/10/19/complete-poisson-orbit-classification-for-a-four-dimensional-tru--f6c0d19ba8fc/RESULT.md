# Complete Poisson-orbit classification for a four-dimensional truncated polynomial algebra

## Finding
Let \(k=\mathbb F_q\) be any finite field and let \(A=k[x,y]/(x^2,y^2)\), with identity fixed. A Poisson structure means an **alternating** \(k\)-bilinear Lie bracket satisfying the Leibniz rule in each argument; isomorphisms are unital, \(k\)-linear Poisson-algebra isomorphisms. Put \(h=\{x,y\}\). The following list consists of exactly one representative of every isomorphism class except for the indicated parameter identification.

* If \(q\) is even, every \(h=u+vx+wy+zxy\) with \(u,v,w,z\in k\) is a Poisson bracket, and there are exactly \(3q\) isomorphism classes. For each \(z\in k\), the three representatives are
  \[h=zxy,\qquad h=x+zxy,\qquad h=1+zxy.\]
  Their respective labeled-bracket orbit sizes are \(1\), \(q^2-1\), and \((q-1)q^2\). In particular, the coefficient \(z\) of \(xy\) is invariant under **every** unital \(k\)-algebra automorphism of \(A\), even if the constant term of \(h\) is nonzero.
* If \(q\) is odd, every Poisson bracket has \(h=zxy\). Two such brackets are isomorphic if and only if their parameters differ by a sign. Thus there are exactly \((q+1)/2\) classes: one class at \(z=0\) and \((q-1)/2\) two-element orbits at \(z\ne0\).

The space of labeled brackets therefore has \(q^4\) members in even characteristic and \(q\) members in odd characteristic. In characteristic two, \(A\) is also the modular group algebra \(k[C_2\times C_2]\), via \(x=g_1-1\), \(y=g_2-1\).

## Assumptions and scope
The classification is for **all** finite fields \(k\) with \(q\ge2\), not merely prime fields, and all ordinary alternating Poisson brackets on this fixed four-dimensional, commutative, unital associative algebra. Field automorphisms are *not* allowed as isomorphisms; the orbit count is for \(k\)-algebra isomorphisms. The notation \(z\) always denotes the coefficient of the socle monomial \(xy\) in the fixed standard presentation of \(A\). Statements about a geometric moduli **scheme**, restricted Poisson structures, deformation quantization, or arbitrary four-dimensional associative algebras are not asserted.

## Proof
**1. All admissible brackets.** The ordered basis \((1,x,y,xy)\) identifies a bilinear biderivation with its value \(h=\{x,y\}\): by the Leibniz rule, \(\{f,g\}=h(f_xg_y-f_yg_x)\), where derivatives are formal partial derivatives followed by reduction in \(A\). Every such expression descends from the polynomial ring exactly when \(\{x^2,y\}=2xh=0\) and \(\{x,y^2\}=2yh=0\). In characteristic two both vanish for every \(h\in A\). In odd characteristic these imply \(xh=yh=0\), whose intersection of annihilators is \(kxy\), hence \(h=zxy\). Conversely these conditions suffice for descent. The Jacobiator of an alternating biderivation is an alternating triderivation. Since \(A\) is generated as a \(k\)-algebra by two elements, every such triderivation is zero (evaluate on ordered triples of \(1,x,y\)), proving the Jacobi identity for each admitted \(h\). This is a genuine characteristic-two Lie bracket: alternation \(\{f,f\}=0\) is explicit in the displayed formula.

**2. Automorphisms.** Every algebra automorphism fixes \(1\), preserves the unique maximal ideal \((x,y)\), and is uniquely of the form
\[\phi(x)=a x+b y+cxy,\qquad \phi(y)=d x+e y+fxy,\]
where \(\Delta=ae-bd\ne0\) and the displayed images square to zero. In characteristic two every invertible \(G=\begin{pmatrix}a&b\\d&e\end{pmatrix}\) occurs, with arbitrary \(c,f\in k\), giving \(q^2|\operatorname{GL}_2(k)|\) automorphisms. In odd characteristic the square-zero conditions are \(ab=de=0\); together with \(\Delta\ne0\), these say that \(G\) is diagonal or anti-diagonal, while \(c,f\) are arbitrary. There are \(2(q-1)^2q^2\) such automorphisms.

**3. The even-characteristic invariant and its complete fibers.** Assume \(\operatorname{char}k=2\), so \(\Delta=ae+bd\), and put \(\alpha=af+cd\) and \(\beta=bf+ce\). The Jacobian of \(\phi\) is
\[J_\phi=\Delta+\alpha x+\beta y.\]
It is a unit, and \((\alpha x+\beta y)^2=0\), so
\[J_\phi^{-1}=\Delta^{-1}+\Delta^{-2}(\alpha x+\beta y).\]
If \(\phi\) transports the bracket with parameter \(h\) to the bracket with parameter \(h'\), then \(\phi(h)=J_\phi h'\), because \(\{\phi(x),\phi(y)\}_{h'}=J_\phi h'\). Multiplication gives, for \(h=u+vx+wy+zxy\),
\[u'=u/\Delta,\qquad (v',w')=\Delta^{-1}(va+wd,vb+we)+u\Delta^{-2}(\alpha,\beta),\]
\[z'=z+(vc+wf)/\Delta+\bigl((va+wd)\beta+(vb+we)\alpha\bigr)/\Delta^2=z.\]
The last equality follows from the elementary identity
\[(va+wd)\beta+(vb+we)\alpha=\Delta(vc+wf).\]
Thus \(z\) is invariant. If \(u=v=w=0\), the entire orbit is a singleton. If \(u=0\) but \((v,w)\ne(0,0)\), the standard \(\operatorname{GL}_2(k)\) action is transitive on nonzero row vectors and \(z\) remains fixed: the orbit has \(q^2-1\) members. If \(u\ne0\), the determinant \(\Delta\) can normalize \(u\) to any other nonzero value. For each fixed invertible \(G\), the map \((c,f)\mapsto(\alpha,\beta)\) has determinant \(\Delta\), so the linear coefficients can then be prescribed arbitrarily. This orbit has exactly \((q-1)q^2\) members. These exhaust all \(q^3\) choices of \((u,v,w)\) in each fixed \(z\)-fiber, since \(1+(q^2-1)+(q-1)q^2=q^3\). Representatives and the total \(3q\) count follow.

**4. Odd characteristic.** Here \(h=zxy\), and \(\phi(xy)=(ae+bd)xy\). For \(G\) diagonal one has \(ae+bd=\Delta\), while for \(G\) anti-diagonal one has \(ae+bd=-\Delta\). The constant term of \(J_\phi\) is \(\Delta\), and every positive-degree term annihilates \(xy\), so the transported bracket has parameter \(z'=z\) in the first case and \(z'=-z\) in the second. These are the only possibilities, and both are attained. There are \(1+(q-1)/2=(q+1)/2\) classes.

## Verification
The standalone file `verify.py` enumerates all algebra automorphisms and induced Poisson-parameter orbits directly in the quotient ring, without using the normal-form proof's coefficient-invariance identity. For \(q=2,4\) it checks every bracket against every automorphism, including all \(24\) and \(2880\) automorphisms respectively. For odd prime fields \(q=3,5,7\) it enumerates all square-zero-preserving invertible changes of generators and the resulting sign orbits. Run `python3 verify.py` from the package directory and require the terminal line `VERIFY_ALL_OK`. Finite enumerations check the implementation in these fields; the preceding proof, not extrapolation, establishes all finite-field cases.

## Relationship to prior work
Launois and Richard, arXiv:0805.4694 (first public 30 May 2008), study Poisson (co)homology on \(\mathbb C[X,Y]/(X^a,Y^b)\) with the specifically fixed bracket \(\{X,Y\}=XY\); their Theorems 1.1 and 1.2 concern cohomology and homology, not classification of all brackets, and their characteristic-zero derivation constraints exclude the characteristic-two family above. Abdelwahab, Barreiro, and Sánchez, arXiv:2410.07957, classify four-dimensional **complex** Poisson algebras, not finite-characteristic brackets with characteristic-two unit and linear terms. Finite-field Dedekind Poisson-algebra enumerations address the subclass where every Poisson subalgebra is an ideal; this unital four-dimensional algebra is not Dedekind because \(k\cdot1\) is a proper unital Poisson subalgebra but not an ideal. These distinctions prevent the inspected statements from implying the characteristic-two \(3q\) orbit classification. The present result is stated with a residual risk of unlocated positive-characteristic special-case literature.

## Limitations
This is a classification of ordinary \(k\)-linear Poisson brackets up to unital \(k\)-algebra isomorphism, not a classification under semilinear field automorphisms. The parameter \(z\) is invariant for the chosen standard algebra but no functorial construction for a different underlying algebra is asserted. No scheme-theoretic reducedness, singularity, or deformation-obstruction statement is claimed. The finite checks are independent spot/exhaustive confirmations in specified small fields only; originality remains conditional on the coverage of historical literature.

## References
1. S. Launois and L. Richard, *Poisson (co)homology of truncated polynomial algebras in two variables*, arXiv:0805.4694v1, 30 May 2008, https://arxiv.org/abs/0805.4694.
2. H. Abdelwahab, E. Barreiro and J. M. Sánchez, *Classification of 4-dimensional complex Poisson algebras*, arXiv:2410.07957 (original 9 October 2024), https://arxiv.org/abs/2410.07957.
3. A. I. Plakosh and O. O. Pypka, *Dedekind Poisson Algebras over Arbitrary Fields*, arXiv:2609.13767 (2026), https://arxiv.org/abs/2609.13767.
