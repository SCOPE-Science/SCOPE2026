# Four components of the zero-product variety of a spin-factor Jordan algebra

## Finding
Let \(k\) be a field of characteristic different from \(2\). Let \(V\) be an \(n\)-dimensional \(k\)-vector space, \(n\ge2\), and let \(B:V\times V\to k\) be a nondegenerate symmetric bilinear form. The spin-factor Jordan algebra is \(J_B=k\oplus V\), with
\[
(a,u)\circ(b,v)=(ab+B(u,v),\;av+bu).
\]
Let \(\mathcal Z_B\) be the **reduced** affine variety of ordered pairs with zero Jordan product. Over an algebraic closure of \(k\), it has **exactly four** irreducible components, all defined over \(k\). Write \(x=(a,u)\), \(y=(b,v)\), and \(F(a,u)=a^2-B(u,u)\). The components are:

1. \(X_L=\{y=0\}\), an affine \((n+1)\)-space;
2. \(X_R=\{x=0\}\), an affine \((n+1)\)-space;
3. \(X_\perp=\{a=b=0,\;B(u,v)=0\}\), of dimension \(2n-1\);
4. \(X_{\mathrm{iso}}\), the variety of two-by-\((n+1)\) matrices with rows \((a,u)\), \((b,-v)\), rank at most one, with both rows isotropic for \(F\); it has dimension \(n+1\).

In particular, \(\mathcal Z_B\) is equidimensional precisely when \(n=2\). For \(n\ge3\), the orthogonality component is uniquely largest, of dimension \(2n-1\). In every dimension \(n\ge2\), the ambient codimension of the zero-product variety is \(3\).

For a finite field \(k=\mathbb F_q\) of odd order, define \(N_B(1)=\#\{u\in V:B(u,u)=1\}\). Then the exact number of ordered zero-product pairs is
\[
\boxed{\#\mathcal Z_B(\mathbb F_q)
=(2q-1)q^n+(q^n-1)q^{n-1}+(q-1)^2N_B(1).}
\]
If \(\chi\) is the quadratic character of \(\mathbb F_q\) and \(\delta\in\mathbb F_q^\times\) is the determinant of a Gram matrix of \(B\), then
\[
N_B(1)=
\begin{cases}
q^{n-1}+\chi((-1)^{(n-1)/2}\delta)q^{(n-1)/2},&n\text{ odd},\\
q^{n-1}-\chi((-1)^{n/2}\delta)q^{(n-2)/2},&n\text{ even}.
\end{cases}
\]
The quadratic-character expression is independent of the chosen basis because a change of Gram matrix multiplies \(\delta\) by a square.

## Assumptions and scope
All geometric components and dimensions are for the reduced zero-fiber variety over arbitrary fields of characteristic not \(2\), assessed after extension to an algebraic closure. They do **not** assert that the defining quadratic ideal is radical. The finite-field count concerns all ordered pairs, including zero elements and singular elements, and all odd prime-power field orders. The vector dimension is at least \(2\) and the bilinear form is nondegenerate; characteristic \(2\) and degenerate forms are outside the claim.

## Proof
**1. Original product equations.** The defining equations for a zero product are
\[
ab+B(u,v)=0,\qquad av+bu=0.
\]
If \(a=b=0\), the first equation is exactly \(B(u,v)=0\), and the point belongs to \(X_\perp\). If \(a\ne0\) and \(b=0\), the vector equation gives \(v=0\), so the point lies in \(X_L\). If \(a=0\), \(b\ne0\), it lies in \(X_R\). Finally, if both scalars are nonzero, the vector equation gives \(v=-(b/a)u\). The scalar equation then becomes \(b(a^2-B(u,u))/a=0\), hence \(F(a,u)=0\). Thus the rows \((a,u)\) and \((b,-v)\) are proportional and \(F\)-isotropic. This proves that every zero-product pair belongs to one of the four stated closed loci.

Conversely, points of \(X_L,X_R,X_\perp\) plainly have zero product. A point of \(X_{\mathrm{iso}}\) with nonzero first row has \((b,-v)=t(a,u)\) for some \(t\), so \(b=ta\), \(v=-tu\), \(av+bu=0\), and \(ab+B(u,v)=tF(a,u)=0\). If its first row vanishes, then \(x=0\), and the product also vanishes. Consequently the reduced zero fiber is the union of these four closed subsets.

**2. Irreducibility and dimensions.** The loci \(X_L\) and \(X_R\) are affine linear spaces of dimension \(n+1\). The polynomial \(B(u,v)\) has bidegree \((1,1)\) and coefficient matrix of rank \(n\). For \(n\ge2\), it cannot factor into linear forms over an algebraic closure: such a factorization of a bihomogeneous form would have to be a linear form in \(u\) times a linear form in \(v\), yielding coefficient-matrix rank one. Therefore \(X_\perp\) is geometrically irreducible of dimension \(2n-1\).

The nondegenerate quadratic form \(F\) on \(k\oplus V\) has dimension \(n+1\ge3\). Its projective zero quadric \(\mathcal Q_F\subset\mathbb P^n\) is geometrically smooth, irreducible, and of dimension \(n-1\). The rank-one matrices with both rows \(F\)-isotropic form the affine cone over the Segre embedding of \(\mathcal Q_F\times\mathbb P^1\). Hence \(X_{\mathrm{iso}}\) is geometrically irreducible of dimension \((n-1)+1+1=n+1\).

None of the four irreducible sets is contained in another. For \(X_L\), take \(x=(1,0)\), \(y=0\); for \(X_R\), interchange the pair. A point of \(X_{\mathrm{iso}}\) with \(a=b=1\), \(B(u,u)=1\), and \(v=-u\) lies in none of the other three (such \(u\) exists over an algebraic closure). For \(X_\perp\), choose linearly independent \(u,v\) with \(B(u,v)=0\), which is possible for nondegenerate \(B\) and \(n\ge2\). This point has matrix rank two and lies in none of the other three. Thus the four sets are exactly the irreducible components.

The maximum dimension is \(\max\{n+1,2n-1\}\). Since \(2n-1=n+1\) exactly when \(n=2\), the equidimensionality assertion follows. The ambient space has dimension \(2n+2\), so its difference from the maximum component dimension equals \(3\) for all \(n\ge2\).

**3. Finite-field count.** Count the annihilator of a fixed \(x=(a,u)\). If \(x=0\), there are \(q^{n+1}\) choices of \(y\). If \(a=0\) and \(u\ne0\), nondegeneracy gives \(b=0\) and \(v\in u^\perp\), hence \(q^{n-1}\) choices. If \(a\ne0\), then \(v=-(b/a)u\) and the remaining equation is \(bF(a,u)=0\). Thus there is one solution \(y\) when \(F(a,u)\ne0\), and \(q\) solutions when \(F(a,u)=0\). The number of pairs \((a,u)\) with \(a\ne0\) and \(F(a,u)=0\) is \((q-1)N_B(1)\), by scaling \(u\) by \(a^{-1}\). Summing yields
\[
q^{n+1}+(q^n-1)q^{n-1}+(q-1)(q^n-N_B(1))+q(q-1)N_B(1),
\]
which simplifies to the stated formula.

**4. Quadratic-form norm count.** Diagonalize \(B\) over \(\mathbb F_q\), possible because \(q\) is odd. For a nontrivial additive character \(\psi\), additive-character orthogonality gives
\[
N_B(1)=\frac1q\sum_{t\in\mathbb F_q}\psi(-t)\sum_{u\in\mathbb F_q^n}\psi(tB(u,u)).
\]
The \(t=0\) contribution is \(q^{n-1}\). For \(t\ne0\), the inner sum is \(\chi(t)^n\chi(\delta)G^n\), where the quadratic Gauss sum \(G=\sum_{z\in\mathbb F_q}\psi(z^2)\) satisfies \(G^2=\chi(-1)q\). If \(n\) is even, use \(\sum_{t\ne0}\psi(-t)=-1\); if \(n\) is odd, use \(\sum_{t\ne0}\chi(t)\psi(-t)=\chi(-1)G\). These yield the two formulas for \(N_B(1)\), with no assumption that \(q\) is prime rather than a prime power.

## Verification
The included standalone Python checker constructs the **original** Jordan multiplication over prime fields and over the genuine degree-two extension \(\mathbb F_9\), enumerates all ordered pairs for twelve form/field configurations, and compares the direct count to the independently enumerated unit-norm formula. Each configuration passed. The checker was run from its packaged source; the log is included. Finite tests corroborate, but do not prove, the theorem for unbounded \(n\) or all finite fields.

## Relationship to prior work
Panyushev, *Commuting involutions of Lie algebras, commuting varieties, and simple Jordan algebras* (arXiv:1210.3785v1, 2012), Section 6, defines zero-product varieties of simple Jordan algebras. Theorem 6.3 relates them to Lie-theoretic commuting varieties; the discussion following it explicitly asks for a classification of all irreducible components and their dimensions. Proposition 6.5 provides lower bounds and a non-equidimensionality result, but not the four-component classification or the finite-field formula established here. Those prior geometric bounds are not claimed as new.

Diniz and da Silva Souza, *Specht property for the 2-graded identities of the Jordan superalgebra of a bilinear form* (arXiv:1601.03351v1, 2016), studies exactly the Jordan algebra \(k\oplus V\) and its graded identities over characteristic zero. Its inspected theorems concern the Specht property and cocharacters, not the zero-product fiber; the first-listed MSC code in the original manuscript is 15A72. The present work handles reduced zero-product geometry in every odd characteristic and finite-field point counts, rather than polynomial identities.

The literature and database comparisons are evidence of a potential gap, not proof of worldwide publication priority.

## Limitations
The reduced irreducible components are classified, not the possibly nonreduced scheme structure of the equations. The argument excludes characteristic \(2\), degenerate bilinear forms, and vector dimension \(1\). The finite-field formula is an ordered-pair count, not an isomorphism- or orbit-classification. The complete earlier literature may contain an equivalent formulation not found by the searches. Independent mathematical auditing has not been performed.

## References
1. D. I. Panyushev, *Commuting involutions of Lie algebras, commuting varieties, and simple Jordan algebras*, arXiv:1210.3785v1 (2012), Section 6, especially Theorem 6.3 and Proposition 6.5. https://arxiv.org/abs/1210.3785
2. D. Diniz and M. da Silva Souza, *Specht property for the 2-graded identities of the Jordan superalgebra of a bilinear form*, arXiv:1601.03351v1 (2016). https://arxiv.org/abs/1601.03351
3. M. Grašič, *Zero product determined Jordan algebras, I*, Linear and Multilinear Algebra 59 (2011), 671–685, DOI:10.1080/03081087.2010.485199 (related terminology, not a source for a component classification).
