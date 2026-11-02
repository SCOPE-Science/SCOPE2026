# Multiplication-rank strata of the free two-generator Jacobi–Jordan algebra

## Finding
Let \(k\) be any field of characteristic different from \(2\) and \(3\), and let \(F\) be the nonunital free Jacobi–Jordan algebra on two generators. For \(z\in F\), write \(L_z:F\to F\), \(w\mapsto zw\). The only possible ranks of \(L_z\) are \(0,1,2,3,5\). The rank-\(4\) stratum is empty, despite the occurrence of ranks \(3\) and \(5\).

Over every finite field \(k=\mathbb F_q\) of characteristic greater than \(3\), the exact numbers of elements with each rank are

| \(\operatorname{rank} L_z\) | Number of \(z\) |
|---:|---:|
| \(0\) | \(q\) |
| \(1\) | \(q(q^2-1)\) |
| \(2\) | \(q^3(q^2-1)\) |
| \(3\) | \(q^5(q-1)\) |
| \(4\) | \(0\) |
| \(5\) | \(q^6(q^2-1)\) |

All five nonempty strata have an intrinsic geometric description: letting \(F^d\) denote the span of all products of total length at least \(d\), they are respectively \(F^4\), \(F^3\setminus F^4\), a punctured discriminant cone times \(F^3\), the complement of that cone inside \(F^2\), and \(F\setminus F^2\). More explicitly, if \(z\in F^2\) has degree-two part \(a x^2+b(xy)+c y^2\), the rank-\(\le2\) locus in \(F^2\) is the quadratic hypersurface \(b^2-4ac=0\). It is geometrically irreducible and singular exactly along \(F^3\). Thus the complete rank-\(\le r\) determinantal loci, as underlying reduced sets, are \(F^4\) for \(r=0\), \(F^3\) for \(r=1\), this cone for \(r=2\), and \(F^2\) for \(r=3,4\), followed by all of \(F\) for \(r\ge5\).

## Assumptions and scope
A Jacobi–Jordan algebra is a commutative, not necessarily associative algebra satisfying \(u(vw)+v(wu)+w(uv)=0\). The algebra \(F\) is the initial nonunital such algebra on generators \(x,y\). Products with more than two factors are always parenthesized unless their meaning is specified. All statements are for fields of characteristic not \(2\) or \(3\); the arithmetic formulas additionally require a finite field. They do not assert a characteristic-two or characteristic-three analogue.

The eight-dimensional normal form of this free object is the graded vector space with ordered basis
\[
(x,y,a,b,c,d,e,f),\qquad
 a=xx,\ b=xy,\ c=yy,\ d=(xx)y,\ e=x(yy),\ f=(xx)(yy).
\]
Its degrees are \(1,1,2,2,2,3,3,4\). The complete nonzero products, up to commutativity, are
\[
xx=a,\quad xy=b,\quad yy=c,\quad xb=-d/2,\quad xc=e,\quad ya=d,\quad yb=-e/2,\quad ac=f,\quad bb=-f/2,\quad xe=-f/2,\quad yd=-f/2.
\]
Every unspecified basis product vanishes. In particular, \(F^2=\langle a,b,c,d,e,f\rangle\), \(F^3=\langle d,e,f\rangle\), \(F^4=\langle f\rangle\), and \(F^5=0\).

## Proof
**1. The normal form and its independence.** Linearizing the Jacobi identity gives \(x(xx)=y(yy)=0\), \(xb=-d/2\), and \(yb=-e/2\). Substituting \((x,x,b)\) and \((x,a,y)\) proves \(xd=ab=0\); the symmetric substitutions prove \(ye=bc=0\). Substituting \((x,x,c)\) and \((y,y,a)\) yields \(xe=yd=-f/2\). Jacobi on \((x,y,b)\) yields \(b^2=-f/2\). Similar substitutions give \(a^2=c^2=0\). In degree five, Jacobi on \((a,c,x)\) and \((x,x,e)\) yields respectively \(ae=-xf\) and \(ae=xf\), hence \(xf=ae=0\) (and symmetrically \(yf=cd=0\)). All remaining degree-five products reduce to these or to \(xd=ye=0\), so all higher products vanish. Consequently any monomial in the two generators reduces to the eight displayed monomials. Conversely, the displayed eight-dimensional multiplication table satisfies the Jacobi identity on all basis triples (also checked directly by the supplied program), and its basis elements are independent by construction. Therefore it realizes the free algebra. The characteristic restriction avoids divisions by two and three. This normal-form calculation is classical; no novelty is claimed for the multiplication table itself.

**2. Elements with nonzero degree-one part.** Write
\[
z=ux+vy+Aa+Bb+Cc+Dd+Ee+tf
\]
where \(u,v,A,B,C,D,E,t\) are scalar coefficients. If \((u,v)\ne(0,0)\), choose a second element whose degree-one class complements the class of \(z\). Freeness gives an endomorphism taking the two generators to these two elements. Its associated graded map, induced by an invertible linear substitution on \(\langle x,y\rangle\), is invertible in every graded degree and hence the endomorphism is an automorphism. It conjugates \(L_x\) to \(L_z\). The displayed products give \(\operatorname{im}L_x=\langle a,b,d,e,f\rangle\), of dimension \(5\). Thus the entire complement of \(F^2\) has rank \(5\).

**3. Elements in \(F^2\).** Use unambiguous coordinate notation
\[
z=Aa+Bb+Cc+Dd+Ee+tf.
\]
The degree-three part of the restricted map \(L_z:\langle x,y\rangle\to\langle d,e\rangle\) has matrix
\[
M(A,B,C)=\begin{pmatrix}-B/2&A\\C&-B/2\end{pmatrix},
\quad\det M=(B^2-4AC)/4.
\]
The degree-four parts contributed by the cubic terms are \(L_z(x)|_{\langle f\rangle}=-Ef/2\) and \(L_z(y)|_{\langle f\rangle}=-Df/2\). Independently, multiplication of \(Aa+Bb+Cc\) by \(a,b,c\) gives the nonzero linear functional \((C,-B/2,A)f\) whenever \((A,B,C)\ne0\). Thus, if the degree-two part is nonzero, the image rank is exactly \(1+\operatorname{rank}M\): it is \(2\) when the discriminant is zero and \(3\) otherwise. If \(A=B=C=0\), the rank is \(1\) for \((D,E)\ne0\), and \(0\) for \(D=E=0\). This proves the entire rank classification and excludes rank \(4\).

**4. Geometry and counting.** The equation \(B^2-4AC=0\) is the rank-one symmetric \(2\times2\) matrix cone. It is an irreducible quadratic cone over any algebraic closure of characteristic other than two, with unique vertex \((0,0,0)\); Cartesian product with \(F^3\) gives singular locus precisely \(F^3\) inside \(F^2\). Over \(\mathbb F_q\), the cone has \(q^2\) points: its nonzero points are the \((q+1)(q-1)=q^2-1\) scalar nonzero rank-one symmetric matrices. There are \(q^3-q^2\) quadratic parts off the cone, and \(q^3\) freely chosen higher-degree coefficients. The zero quadratic part gives \(q^2-1\) nonzero cubic choices and \(q\) quartic choices. Finally, \(q^2-1\) nonzero degree-one choices each have \(q^6\) higher-degree lifts. Multiplication gives the five numerical formulas. Their sum is exactly \(q^8\), as required.

## Verification
The standalone pure-Python program `verify.py` builds an independent multiplication tensor from the eleven nonzero products above, tests all \(8^3=512\) Jacobi triples separately over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), and computes each \(L_z\) rank by modular Gaussian elimination. It exhaustively tests all \(5^8=390625\) elements over \(\mathbb F_5\) (using that the coefficient of \(f\) does not affect multiplication), and checks 5000 fixed-seed samples each over \(\mathbb F_7\) and \(\mathbb F_{11}\). The expected output includes `FREE_JJ_MULTIPLICATION_RANK_OK`. This is a finite check, not a replacement for the proof above.

## Relationship to prior work
Burde and Fialowski introduced the Jacobi–Jordan setting and classified low-dimensional examples in their April 2014 preprint. Agore and Militaru studied extension objects and canonical two-step examples in July 2015. Remm's February 2022 manuscript (revised April 2024), §5.1, already derives the eight-dimensional free two-generator normal form and its graded multiplication; that basis and its non-speciality are prior work, not discoveries here. The assessed new assertion is the *complete determinantal stratification of left-multiplication ranks*, its missing-rank phenomenon, and the precise finite-field counts. No equivalent rank-count or discriminant-stratum statement was found in the inspected relevant sections or targeted searches. The prior multiplication table makes the new result accessible by computation, so the residual risk is that the same rank calculation was previously recorded elsewhere or considered an immediate standard corollary.

## Limitations
The conclusion concerns a single canonical free eight-dimensional algebra, not all Jacobi–Jordan algebras or the full moduli of algebras. It makes no assertion about representation-theoretic or deformation consequences beyond the explicit rank strata. It describes reduced rank loci, not scheme-theoretic minors or their embedded components. It excludes characteristic two and three. Exhaustive finite-field checks do not certify the universal theorem or historical priority; independent mathematical audit has not been performed.

## References
1. D. Burde and A. Fialowski, *Jacobi-Jordan algebras*, arXiv:1404.5435, first submitted 2014-04-22, https://arxiv.org/abs/1404.5435.
2. A. L. Agore and G. Militaru, *On a type of commutative algebras*, arXiv:1507.08146, first submitted 2015-07-29, https://arxiv.org/abs/1507.08146.
3. E. Remm, *Anti-associative algebras*, arXiv:2202.10812v2, originally submitted 2022-02-22; §5.1 (free two-generator Jacobi–Jordan algebra), https://arxiv.org/html/2202.10812v2.
