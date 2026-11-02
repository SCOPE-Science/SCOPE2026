# Reduced critical schemes and exact nodal counts for cubic elementary-symmetric hypersurfaces in odd characteristic

## Finding

Let \(k\) be algebraically closed of odd characteristic \(p\), and let \(n\ge4\) satisfy \(p\nmid(n-2)\). Write
\[
 e_3(x_1,\ldots,x_n)=\sum_{1\le i<j<h\le n}x_ix_jx_h,
 \qquad X=V(e_3)\subset\mathbb P_k^{n-1}.
\]
For any nonempty subset \(S\subseteq[n]\), write \([\mathbf1_S]\) for the projective point with coordinate \(1\) on \(S\) and \(0\) off \(S\). Let \(C\) be the projective scheme cut out by all first derivatives of \(e_3\). Then **as a reduced finite scheme**,
\[
 C=\bigsqcup_{\substack{\varnothing\ne S\subseteq[n]\\ |S|\equiv1\pmod p}}[\mathbf1_S],\qquad
 \deg C=\sum_{\substack{1\le m\le n\\m\equiv1\pmod p}}\binom nm.
\]
The projective singular scheme \(\operatorname{Sing}(X)\), defined by \(e_3\) and its first derivatives, is also reduced. Its geometric points are exactly
\[
 \begin{cases}
 [\mathbf1_S]\text{ with }|S|\equiv1\pmod p,&p\ge5,\\
 [\mathbf1_S]\text{ with }|S|\equiv1\pmod9,&p=3.
 \end{cases}
\]
In either case its degree is the corresponding binomial subset sum. Each singularity is an ordinary quadratic double point, with nondegenerate projective tangent-cone quadric. The cubic \(X\) is geometrically integral and normal.

For instance, when \(p=5\) and \(n=8\), the cubic hypersurface in \(\mathbb P^7\) has exactly \(\binom81+\binom86=36\) geometric nodes. In characteristic \(3\), for \(n=4\), the projective critical scheme has five points but the cubic surface has only four nodes: the all-ones critical point lies off the hypersurface.

## Assumptions and scope

All point and scheme assertions are geometric over \(k\). The hypotheses are: odd prime \(p\), integer \(n\ge4\), and \(p\nmid(n-2)\). Scheme-theoretic reducedness applies to projective critical and projective singular schemes, not automatically to the affine cone at its vertex. The ordinary-double-point assertion applies only to critical points that actually lie on \(X\); in characteristic \(3\) there can be off-hypersurface critical points. Counts are geometric counts and also counts of \(\mathbb F_p\)-rational points because the displayed coordinates are prime-field coordinates.

## Proof

**1. A two-value reduction.** Let \(e_j\) denote the degree-\(j\) elementary symmetric function on all \(n\) coordinates, and write \(e_1\) and \(e_2\) for the first two. For every \(i\), deletion of the \(i\)-th variable gives
\[
 \partial_i e_3=e_2-x_i e_1+x_i^2.
\]
At a critical point all coordinates are therefore roots of the same monic polynomial \(T^2-e_1 T+e_2\). There are at most two distinct values, even over an algebraically closed field and even if this quadratic has a repeated root.

Suppose there are two distinct values \(t,u\), repeated \(m\) and \(\ell=n-m\) times. Set \(a=m-1\) and \(b=\ell-1\), understood as elements of \(k\). The difference between a derivative at a \(t\)-coordinate and one at a \(u\)-coordinate is
\[
 (u-t)(at+bu),
\]
so \(at+bu=0\). The derivative at a \(t\)-coordinate is the second elementary symmetric polynomial of \(a\) copies of \(t\) and \(b+1\) copies of \(u\). The first \(a+b\) entries have sum zero; therefore, using \(2\ne0\) in \(k\), the derivative equals \(-(at^2+bu^2)/2\). Its vanishing yields \(at^2+bu^2=0\). Subtract the first equation multiplied by \(t\) and by \(u\), respectively, to get
\[
 bu(u-t)=0,\qquad at(t-u)=0.
\]
As \(t\ne u\), this implies \(at=bu=0\). If both \(t\) and \(u\) were nonzero, then \(a=b=0\), hence \(n-2=a+b=0\) in \(k\), contrary to hypothesis. Thus one of the two values is zero.

If the nonzero value occurs on \(m\) coordinates, the previous equations imply \(m-1=0\) in \(k\). If all coordinates equal a nonzero value, the same conclusion follows from \(\partial_i e_3=\binom{n-1}2t^2\), since \(p\nmid(n-2)\). Conversely, for each \(S\) with \(m=|S|\equiv1\pmod p\), the derivative at an active coordinate is \(\binom{m-1}2\), and at an inactive coordinate is \(\binom m2\); both vanish. This proves the complete geometric support of \(C\).

**2. Reducedness from the full Hessian.** At \([\mathbf1_S]\), write \(m=|S|\), \(\ell=n-m\) and arrange the coordinates in active and inactive blocks. For \(i\ne j\),
\[
 \partial_i\partial_j e_3=\sum_{h\notin\{i,j\}}x_h,
\]
and diagonal second derivatives vanish. Since \(m=1\) in \(k\), the Hessian decomposes into the two blocks
\[
 H=\begin{pmatrix}I_m-J_m&0\\0&J_\ell-I_\ell\end{pmatrix},
\]
where \(J_s\) is the all-ones matrix (and the empty block is allowed). The first block has one-dimensional kernel spanned by \(\mathbf1_S\) and rank \(m-1\). On the second block, \(J_\ell-I_\ell\) is invertible: its determinant is \((-1)^{\ell-1}(\ell-1)\), and \(\ell-1=n-m-1=n-2\ne0\) in \(k\). (For \(\ell=0\) it is vacuously invertible.) Therefore \(H\) has rank exactly \(n-1\), with kernel equal to the radial line. Choose an active coordinate as affine dehomogenizing coordinate. The Jacobian matrix of the \(n\) partial derivatives with respect to the remaining \(n-1\) affine coordinates has rank \(n-1\). Thus each geometric projective critical point is a reduced simple point. There are no other geometric points, and \(C\) is a reduced finite scheme with the stated degree.

**3. The characteristic-three distinction.** The homogeneous Euler identity reads
\[
 3e_3=\sum_i x_i\partial_i e_3.
\]
For \(p\ge5\), it places every critical point on \(X\). For \(p=3\), evaluation at an indicator point gives \(e_3(\mathbf1_S)=\binom m3\). Writing \(m=1+3a\), the coefficient of \(T^3\) in \((1+T)^m=(1+T)(1+T^3)^a\) over \(\mathbb F_3\) is \(a\pmod3\). Hence \(\binom m3=0\) if and only if \(m\equiv1\pmod9\). The singular scheme is the closed subscheme of the already reduced zero-dimensional scheme \(C\) cut out by \(e_3\); it is precisely the claimed reduced union of its points.

**4. Quadratic types and global geometry.** At every projective critical point the gradient vanishes, and the rank calculation above says the quadratic term in the local affine equation has an invertible Hessian. At any such point belonging to \(X\) this is an ordinary nondegenerate quadratic double point (characteristic different from \(2\)). Its projective tangent-cone quadric is smooth. Therefore \(\operatorname{Sing}(X)\) is finite. Since \(n\ge4\), any two positive-degree hypersurface components of a reducible cubic in \(\mathbb P^{n-1}\) would intersect in dimension at least \(n-3\ge1\), yielding a positive-dimensional singular locus. Thus \(X\) is geometrically integral. Finally, every hypersurface is Cohen–Macaulay and hence satisfies Serre's condition \((S_2)\), while its finite singular locus has codimension at least two in \(X\), giving \((R_1)\). Serre's criterion shows \(X\) is normal. This proves all assertions.

## Verification

The standalone file `verify_e3.py` enumerates all nonzero vectors over the *prime fields* \(\mathbb F_p\) for nine admissible small \((p,n)\), checking the critical-point classification, the hypersurface condition, and Hessian rank \(n-1\). The actual cases tested are \((3,3),(3,4),(3,6),(3,7),(3,9),(5,4),(5,6),(5,8),(7,4)\); the \(n=3\) case is an auxiliary algebraic check, not part of the global integrality assertion. The checker returned `VERIFY_OK`. It is finite confirmation, not a substitute for the proof for arbitrary \(p,n\).

## Relationship to prior work

Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic* (arXiv:2610.00259v1), proves the dimensions of all derivative loci and the generic local rings on coordinate components. For \(d=3\) and \(p\nmid(n-2)\), the reported dimension for the **affine** first-derivative zero locus is one, so the projective critical scheme is zero-dimensional; the source explicitly leaves smaller-dimensional and embedded components and general global reducedness unresolved. The present exact support and reducedness classification, plus the characteristic-three separation and every local quadratic type, go beyond that dimensional conclusion. Xie's common-polynomial observation motivates step 1 but does not provide the complete two-block congruence elimination or final node count.

Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics* (arXiv:2509.05009), establishes dimension bounds motivated by algebraic complexity, not these component and nodal formulas. Cafure, Matera and Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed-Solomon codes* (arXiv:1109.2265), analyze general symmetric hypersurface singularities and partition spaces but do not determine this particular global reduced projective critical scheme in the material inspected. The four-node characteristic-three cubic surface is classical; the uniform formulas are not attributed to that finite special case. No definitive priority claim is made.

## Limitations

The result excludes characteristic two and the exceptional congruence \(p\mid(n-2)\), where higher-dimensional or thickened critical loci may occur. It concerns the third elementary symmetric polynomial and the **projective** first-derivative scheme, not general degrees or affine-cone embedded structure. Numerical point counts on larger extension fields were not attempted. Full priority against unlocated classical symmetric-hypersurface literature is not established; independent validation was not performed.

## References

1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (first publicly posted 2026-09-24), https://arxiv.org/html/2610.00259v1.
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009, https://arxiv.org/html/2509.05009v3.
3. Antonio Cafure, Guillermo Matera and Melina Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed-Solomon codes*, arXiv:1109.2265v1, https://arxiv.org/html/1109.2265v1.
