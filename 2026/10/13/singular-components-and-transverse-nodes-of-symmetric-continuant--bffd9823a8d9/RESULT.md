# Singular components and transverse nodes of symmetric continuant hypersurfaces

## Finding
Let \(n\ge 3\), and let \(T_n\) be the generic complex symmetric tridiagonal matrix of order \(n\), with diagonal entries \(a_1,\ldots,a_n\) and adjoining off-diagonal entries \(b_1,\ldots,b_{n-1}\). Put \(X_n=V(F_n)\subset\mathbb P^{2n-2}_{\mathbb C}\), where \(F_n=\det T_n\). For an interval \([r,s]\subseteq[1,n]\), let \(D_{[r,s]}\) denote the determinant of the associated principal consecutive submatrix, taking an empty determinant to be one. For \(1\le j<n\), define the closed projective subvariety
\[
Y_j=V\bigl(b_j,D_{[1,j]},D_{[j+1,n]}\bigr).
\]
Then \(X_n\) is integral and normal, and its reduced singular locus has precisely \(n-1\) distinct irreducible components:
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{j=1}^{n-1}Y_j.
\]
Each \(Y_j\) is an integral complete intersection of projective codimension three, dimension \(2n-5\), and degree \(j(n-j)\). The reduced singular support consequently has degree
\[
\sum_{j=1}^{n-1}j(n-j)=\binom{n+1}{3}.
\]
At every closed point of a nonempty dense open subset of each \(Y_j\), the completed local ring of \(X_n\) is a product of a smooth formal germ with a transverse ordinary double point:
\[
\widehat{\mathcal O}_{X_n,p}\cong
\mathbb C[[u,v,w,t_1,\ldots,t_{2n-5}]]/(uv-w^2).
\]
In particular the generic transverse multiplicity is two and the Jacobian singular scheme is generically reduced on each component.

The distinct-component decomposition, the individual component degrees, and the explicit local transverse models are the asserted contribution. The numerical degree of the *general* corank-two symmetric determinantal locus and generic nodal behavior in general linear sections are established prior work and are not asserted as discoveries here.

## Assumptions and scope
Work over \(\mathbb C\), in projective coordinates \([a_1:\cdots:a_n:b_1:\cdots:b_{n-1}]\). All variables are algebraically independent prior to projectivization. A *continuant* is a determinant of a contiguous symmetric tridiagonal block; the unit convention on an empty block applies throughout. Singular locus means the support of the Jacobian singular subscheme of the hypersurface, subsequently reduced. The theorem holds for every integer \(n\ge3\); it does not assume generic numerical values for matrix entries. The stated completed-ring normal form holds on a specified dense open subset, not necessarily at component intersections.

## Proof
**1. Continuants and integrality.** Define \(D_{[r,r-1]}=1\) and, for convenient recurrence notation, \(D_{[r,r-2]}=0\). Expanding the last row of a nonempty consecutive block yields
\[
D_{[r,s]}=a_sD_{[r,s-1]}-b_{s-1}^{2}D_{[r,s-2]}
\quad(s>r),\qquad D_{[r,r]}=a_r.
\]
Every such continuant is irreducible in the polynomial ring on its variables. Indeed, induct on block length. In the last diagonal variable it is linear, with coefficient the preceding continuant. That coefficient is relatively prime to the constant term \(-b_{s-1}^2D_{[r,s-2]}\): by induction the preceding continuant is irreducible, contains a diagonal variable absent from \(b_{s-1}\), and does not divide the continuant of the block one shorter (their degrees differ). Thus the linear polynomial is primitive and irreducible by Gauss's lemma over the rational function field in the remaining variables. The length-one case is immediate. This proves \(F_n\) irreducible, so \(X_n\) is integral.

**2. Matrix rank gives the entire singular support.** The derivative of \(\det T_n\) in a diagonal parameter is the corresponding diagonal cofactor. Every matrix of rank at most \(n-2\) has zero adjugate and is therefore singular on \(X_n\). Conversely, if \(T_n\) has rank \(n-1\), the symmetric adjugate has rank one, so \(\operatorname{adj}(T_n)=\lambda vv^{\mathsf T}\), with \(\lambda\ne0\) and \(v\ne0\). Some diagonal entry \(\lambda v_i^2\) is nonzero over \(\mathbb C\); the corresponding derivative in \(a_i\) does not vanish. Consequently
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=\{\operatorname{rank}(T_n)\le n-2\}_{\mathrm{red}}.
\]
Partition the path of matrix indices at every position where \(b_j=0\). In each resulting block all adjacent off-diagonal entries are nonzero. The equation \(Tv=0\) determines each successive coordinate of a kernel vector from its first coordinate, because the intervening \(b\)'s are invertible; hence each block has nullity at most one. Thus the full matrix has corank at least two exactly when at least two of its blocks have a zero determinant. Choose a cut \(j\) between two such singular blocks. Then \(b_j=0\) and both principal matrices to its left and right are singular. Conversely, if \(b_j=0\) and both side determinants vanish, the full matrix has at least two independent kernel vectors. Therefore the set on the previous line equals \(\bigcup_jY_j\), as claimed.

**3. Component integrality and degrees.** The three equations for \(Y_j\) involve the single variable \(b_j\) and two disjoint sets of remaining variables; their degrees are \(1\), \(j\), and \(n-j\). Each side continuant is irreducible by step 1. Over algebraically closed \(\mathbb C\), the product of these geometrically integral affine varieties is integral, so \((b_j,D_{[1,j]},D_{[j+1,n]})\) is prime. Since the generators depend on disjoint variable sets, they form a regular sequence and give a complete intersection in projective codimension three, of degree \(j(n-j)\) by Bézout. To see that these \(n-1\) components are pairwise distinct, for fixed \(j\) choose all internal bridge variables nonzero, set \(b_j=0\), and force each side determinant to vanish by solving for its endpoint diagonal variable. This produces a point on \(Y_j\) with \(b_k\ne0\) for every \(k\ne j\), and thus outside any other \(Y_k\). All components have the same dimension \(2n-5\), and summing degrees gives \(\binom{n+1}{3}\).

**4. Exact local normal form.** Expansion across the bridge \(j\) gives the polynomial identity
\[
F_n=U_jV_j-b_j^2C_j,
\quad U_j=D_{[1,j]},\quad V_j=D_{[j+1,n]},\quad C_j=D_{[1,j-1]}D_{[j+2,n]}.
\]
On the open set \(C_j\ne0\), the derivatives \(\partial U_j/\partial a_j=D_{[1,j-1]}\) and \(\partial V_j/\partial a_{j+1}=D_{[j+2,n]}\) are units. Moreover \(C_j\) is independent of \(a_j,a_{j+1},b_j\). Therefore \((U_j,V_j,b_j)\) together with the other coordinates constitute an invertible algebraic coordinate system after localizing at \(C_j\). The exact hypersurface equation in these coordinates is \(U_jV_j-C_jb_j^2=0\). At a closed point of \(Y_j\cap\{C_j\ne0\}\), complete the local ring and take a square root of the nonzero unit \(C_j\); rescale \(b_j\) to obtain \(uv-w^2=0\). The remaining \(2n-5\) parameters are smooth. In these coordinates the Jacobian ideal is \((u,v,w)\), which is radical, and the transverse quadratic form is nondegenerate.

This open set is nonempty for every \(j\): with internal bridges \(b_k=1\), all diagonals equal to two except \(a_j=(j-1)/j\) and \(a_{j+1}=(n-j-1)/(n-j)\), and \(b_j=0\), each side block has determinant zero while its immediately shorter block has determinant \(j\) and \(n-j\), respectively. Its product \(C_j=j(n-j)\ne0\). Thus the local model holds generically along every component.

**5. Normality.** By step 1 the projective hypersurface is integral and hence Cohen--Macaulay, so it satisfies Serre's \(S_2\) condition. Its singular locus consists of subvarieties of codimension \((2n-3)-(2n-5)=2\) in \(X_n\), so \(X_n\) is regular in codimension one (\(R_1\)). Serre's criterion gives normality.

## Verification
Run `python3 verify_continuant.py` (Python standard library only) and compare with `checker_output.txt`. The independent exact-arithmetic tests cover 660 determinant-cut identities over \(2\le n\le11\); exhaustive finite grids of 199,260 integral parameter points for \(3\le n\le6\) comparing singularity derivatives and the union of the \(Y_j\), including 27,728 singular examples; 65 nondegenerate rational witnesses across \(3\le n\le12\); and 17 degree identities. These are supplementary checks, not a proof of a claim for every integer \(n\); the universal proof is above.

## Relationship to prior work
Piontkowski's *Linear Symmetric Determinantal Hypersurfaces* (Proposition 1.5, 2005 preprint/2006 publication) gives the classical degree \(\binom{n+1}{3}\) for the corank-two locus in the ambient full symmetric space and generic nodal intersections in general linear sections. Thus the summed degree and the existence of generic nodes under general-position hypotheses are not novel as abstract phenomena. This work instead establishes that the **special coordinate subspace of variable symmetric tridiagonal matrices**, which does not satisfy those generic-section hypotheses, has exactly the explicit \(n-1\) integral components with componentwise degrees and the displayed exact neighborhood equations. Kerner--Vinnikov (arXiv:0906.3012) study general singular symmetric determinantal representations and essential/accidental singularities without this path-specific component theorem. Henrion--Naldi--Safey El Din (arXiv:1412.5873) address algorithms for determinantal varieties under genericity hypotheses, not these irreducible components. The fixed-off-diagonal continuant in the finite-type cluster-algebra literature is a different slice: it does not allow bridge coordinates to vanish. Searches did not establish historical uniqueness; an unindexed specialization could precede this statement.

## Limitations
No classification of completed local singularities at intersections of the \(Y_j\), or of nilpotents and embedded components in the **global** Jacobian ideal, is claimed. The proof establishes only the reduced global support and the generically reduced scheme on each component. The sum-of-degrees formula alone should not be treated as new in light of the standard corank-two locus degree. The originality comparison cannot exclude unindexed older results on sparse symmetric determinant loci. Computations stop at finite sizes, whereas the written proof is universal. 

## References
1. Jens Piontkowski, *Linear Symmetric Determinantal Hypersurfaces*, Michigan Math. J. 54 (2006), 117--146, Proposition 1.5. Lawful author PDF: https://www.math.uni-duesseldorf.de/~piontkow/det.pdf ; DOI: 10.1307/mmj/1144437441.
2. Dmitry Kerner and Victor Vinnikov, *Determinantal representations of singular hypersurfaces in \(\mathbb P^n\)*, arXiv:0906.3012, first publicly submitted 2009-06-16, https://arxiv.org/abs/0906.3012 .
3. Didier Henrion, Simone Naldi, and Mohab Safey El Din, *Real root finding for determinants of linear matrices*, arXiv:1412.5873, first publicly submitted 2014-12-18, https://arxiv.org/abs/1412.5873 .
4. *Classification of singularities of cluster algebras of finite type: the case of trivial coefficients*, Glasgow Math. J., Section 3 (fixed-bridge continuants), https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/classification-of-singularities-of-cluster-algebras-of-finite-type-the-case-of-trivial-coefficients/CE916C74775FB8EAB2D048160998F672 .
