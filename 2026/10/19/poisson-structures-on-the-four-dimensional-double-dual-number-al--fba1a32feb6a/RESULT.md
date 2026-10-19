# Poisson structures on the four-dimensional double-dual-number algebra

## Finding
Let \(K\) be a field and \(A=K[x,y]/(x^2,y^2)\). A Poisson structure always means an alternating bilinear Lie bracket that is a derivation in each argument; isomorphisms are \(K\)-linear and preserve both operations.

**Classification theorem.** Every Poisson bracket on \(A\) is uniquely specified by \(f=\{x,y\}\). If \(\operatorname{char}K\ne2\), exactly \(f=\lambda xy\), \(\lambda\in K\), are allowed. Two such brackets are isomorphic precisely when their parameters differ by a sign. If \(\operatorname{char}K=2\), all \(f=a+bx+cy+dxy\), \(a,b,c,d\in K\), are allowed; every isomorphism class has exactly one of the canonical representatives
\[
\{x,y\}=\lambda xy,\qquad \{x,y\}=x+\lambda xy,\qquad \{x,y\}=1+\lambda xy,
\]
where \(\lambda\in K\). The three families are pairwise disjoint, and distinct parameters are never isomorphic.

For \(K=\mathbb F_q\), the number of brackets on this fixed algebra is \(q\) in odd characteristic and \(q^4\) in characteristic two. The respective numbers of isomorphism classes are \((q+1)/2\) and \(3q\). In characteristic two the three canonical families, in their displayed order, have orbit sizes \(1\), \(q^2-1\), and \(q^2(q-1)\). Consequently each parameter contributes those numbers of labeled brackets. The corresponding Poisson-automorphism group orders are \(q^2(q^2-1)(q^2-q)\), \(q^2(q^2-q)\), and \(q(q^2-1)\).

In characteristic two, for the third family, put \(h=1+\lambda xy\). Its derived Lie algebra has basis \(h,x,y\) and brackets \(\{x,y\}=h\), \(\{h,x\}=\lambda x\), and \(\{h,y\}=\lambda y\). At \(\lambda=0\) it is Heisenberg; at every \(\lambda\ne0\) it is a three-dimensional **simple** Lie algebra. For the middle family, the Lie-derived algebra has dimension two and is abelian; for the first family it is one-dimensional and central when \(\lambda\ne0\), and zero when \(\lambda=0\).

## Assumptions and scope
The associative algebra is commutative, unital, four-dimensional and fixed throughout. The generators \(x,y\) square to zero but their product \(xy\) does not vanish. Fields are arbitrary in the classification theorem, including imperfect fields; enumerative statements assume a finite field \(\mathbb F_q\). Only \(K\)-linear isomorphisms are considered, not semilinear equivalences. All statements concern ordinary Poisson brackets, not transposed or double-Poisson structures.

## Proof
Write \(A=K1\oplus Kx\oplus Ky\oplus Kxy\). Since \(A\) is unital, Leibniz gives \(\{1,a\}=0\). Every alternating biderivation is determined by \(f=\{x,y\}\). Differentiating the defining relations gives precisely \(2xf=2yf=0\). If the characteristic is odd, these force \(f\in Kxy\); in characteristic two they impose no restriction. Conversely, when the relations hold, the formula
\[
\{u,v\}=f\bigl((\partial_xu)(\partial_yv)-(\partial_yu)(\partial_xv)\bigr)
\]
induces an alternating biderivation on \(A\). Here derivatives are taken on polynomial representatives; the stated relations make the expression independent of representatives. The Jacobiator is an alternating triderivation on a two-generated algebra, hence vanishes; equivalently, the usual two-variable Jacobian bracket multiplied by any coefficient satisfies Jacobi. Thus the listed parameters are necessary and sufficient.

Any associative automorphism preserves the maximal ideal \(\mathfrak m=(x,y)\) and its square \(Kxy\). In characteristic two, every such automorphism has the form
\[
\Phi(x)=ax+by+u xy,\quad \Phi(y)=cx+dy+v xy,\quad\Delta=ad+bc\ne0.
\]
Indeed all these images square to zero, and invertibility on \(\mathfrak m/\mathfrak m^2\) is equivalent to invertibility on \(A\). Its Jacobian is
\[
J_\Phi=\Delta+(av+cu)x+(bv+du)y.
\]
For source parameter \(f=f_0+f_1x+f_2y+f_3xy\) and target \(g\), the Poisson-isomorphism condition is exactly \(\Phi(f)=gJ_\Phi\). Direct comparison of coefficients, eliminating those of \(x\) and \(y\), shows that the coefficient of \(xy\) is invariant: \(g_3=f_3\). One explicit way to see the cancellation is to put \(B=f_1a+f_2c\), \(C=f_1b+f_2d\), \(H=(av+cu)/\Delta\), \(L=(bv+du)/\Delta\). The coefficient identity \(BL+CH=f_1u+f_2v\) cancels the nonconstant terms in the top-degree comparison.

The remaining three strata are characterized by whether \(f_0\ne0\), whether \(f_0=0\) but \((f_1,f_2)\ne(0,0)\), or whether all three coefficients vanish. When \(f_0\ne0\), an arbitrary nonzero determinant normalizes the constant to \(1\); the independent shear parameters \(u,v\) eliminate both linear coefficients. When \(f_0=0\) and \((f_1,f_2)\ne(0,0)\), the contragredient determinant-twisted action of \(\operatorname{GL}_2(K)\) is transitive on nonzero vectors and normalizes the linear part to \(x\). Finally the socle-supported bracket \(\lambda xy\) is fixed by every algebra automorphism. These steps yield the three unique families.

The characteristic-two associative automorphism group has order \(q^2|\operatorname{GL}_2(\mathbb F_q)|=q^2(q^2-1)(q^2-q)\). The three orbit sizes are \(1\), \(q^2-1\), and \(q^2(q-1)\): for a fixed top coefficient, the middle stratum has all \(q^2-1\) nonzero linear parts, and the unit stratum consists of \((q-1)q^2\) triples of constant and linear coefficients. Orbit-stabilizer gives the automorphism orders and summing over \(q\) possible top coefficients gives \(q^4\) brackets.

In odd characteristic, write \(\Phi(x)=ax+by+u xy\), \(\Phi(y)=cx+dy+v xy\). The relations on the squares require \(ab=cd=0\). Invertibility forces the linear matrix to be diagonal or anti-diagonal. Its determinant therefore equals, respectively, the coefficient of \(xy\) in \(\Phi(xy)\), or its negative. Preservation of \(\{x,y\}=\lambda xy\) implies \(\mu=\lambda\) or \(\mu=-\lambda\), with both realized. Thus there are \((q+1)/2\) odd-characteristic classes.

In characteristic two and for \(f=1+\lambda xy\), direct Leibniz calculations give the displayed three-dimensional derived Lie algebra. If \(\lambda\ne0\), it is perfect. It has no one-dimensional ideal: the operator \(\operatorname{ad}h\) has eigenvalue zero on \(Kh\) and eigenvalue \(\lambda\) on \(Kx+Ky\); neither any nonzero vector on the latter plane nor \(h\) spans an ideal. It has no codimension-one ideal, since a one-dimensional Lie quotient would force its derived algebra into that ideal, contradicting perfectness. Hence it is simple. For \(\lambda=0\) it is the Heisenberg Lie algebra. The other families follow from \(\{x,xy\}=xf\) and \(\{y,xy\}=yf\).

## Verification
A standalone script `verify.py` constructs the algebra and the brackets and checks Jacobi and Leibniz identities on all basis triples for every admissible bracket over fields of orders \(2,3,4,5,7\). It also exhaustively enumerates associative automorphism actions and the orbit-size distribution for fields of orders \(2\) and \(4\). Its checked totals are 16 and 256 labeled characteristic-two brackets, with 6 and 12 isomorphism classes respectively, and 3, 5 and 7 labeled odd-characteristic brackets. These are consistency tests, not substitutes for the all-field proof.

## Relationship to prior work
Petrov and Pypka, arXiv:2609.13784v1 (first publicly posted 2026-09-12), classify Poisson algebras of dimensions at most three over arbitrary fields and emphasize new characteristic-two behavior. Their dimensional scope excludes this four-dimensional algebra. Abdelwahab and Sánchez (2025) classify four-dimensional **complex** Poisson algebras, and therefore treat neither finite-field arithmetic nor the characteristic-two orbit stratification and simple derived-Lie transition proved here. Launois and Richard (2009) already study the truncated algebra \(\mathbb C[x,y]/(x^2,y^2)\) with its fixed bracket \(\{x,y\}=xy\), calculating Poisson (co)homology; that specific example and the two-variable Jacobian construction are not claimed new. Their paper does not classify all brackets or the characteristic-two isomorphism orbits. The orbit-based classification principle is also standard. The particular arbitrary-field orbit classification and its characteristic-two arithmetic and Lie consequences are the asserted contribution.

## Limitations
No claim is made about all four-dimensional Poisson algebras, other four-dimensional associative structures, transposed Poisson structures, or semi-linear equivalence. The argument is elementary but the possible existence of equivalent orbit computations in unindexed literature remains an originality risk. The source comparisons and verification do not constitute an independent audit.

## References
1. A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784v1 (public 2026-09-12), https://arxiv.org/html/2609.13784v1.
2. H. Abdelwahab and J. M. Sánchez, *Classification of Four-Dimensional Complex Poisson Algebras*, Axioms 14 (2025), 804, DOI:10.3390/axioms14110804.
3. S. Launois and L. Richard, *Poisson (co)homology of truncated polynomial algebras in two variables*, C. R. Math. 347 (2009), 133–138, arXiv:0805.4694; studies the fixed bracket \(\{x,y\}=xy\) on the same truncated-algebra family.
4. Standard two-variable Poisson biderivation and orbit-stabilizer methods, used as background rather than claimed discoveries.
