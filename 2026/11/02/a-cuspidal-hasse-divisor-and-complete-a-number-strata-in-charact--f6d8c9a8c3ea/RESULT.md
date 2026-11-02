# A cuspidal Hasse divisor and complete \(a\)-number strata in characteristic seven

## Finding

Let \(k\) be an algebraically closed field of characteristic \(7\). For \((a,b,c)\in k^3\), put
\[
 f_{a,b,c}(x)=x^{11}+a x^6+c x^3+b x,
 \qquad U=\{(a,b,c):\operatorname{Res}_x(f_{a,b,c},f'_{a,b,c})\ne0\}.
\]
For every \((a,b,c)\in U\), the smooth projective hyperelliptic curve \(C_{a,b,c}:y^2=f_{a,b,c}(x)\) has genus \(5\). Define
\[
 F(a,b,c)=2c^5+b(a^2-b)(a^2+b)^2\in k[a,b,c].
\]
Then its Jacobian \(a\)-number is **completely determined** by
\[
 a(C_{a,b,c})=\begin{cases}
 2,&c=0,\ a^2+b=0,\\
 1,&[a=0\text{ or }F=0]\text{ and }(c,a^2+b)\ne(0,0),\\
 0,&aF\ne0.
 \end{cases}
\]
In particular, no smooth member has \(a\)-number above \(2\). The nonordinary Hasse divisor on \(U\) is the reduced union \(V(a)\cup V(F)\), with two distinct irreducible components. The surface \(V(F)\cap U\) is smooth away from precisely the curve
\[
 \Gamma=\{c=0,\ b=-a^2,\ a\ne0\}\subset U,
\]
and has a transverse plane-curve singularity of type \(A_4\), locally \(u^2+v^5=0\), at every point of \(\Gamma\). Thus the entire \(a\)-number-two locus is exactly the cuspidal singular locus of this component. The smooth components \(V(a)\cap U\) and \(V(F)\cap U\) intersect transversely.

## Assumptions and scope

The ground field is algebraically closed of characteristic \(7\). Coefficients are marked, not quotiented by coordinate transformations. Smoothness is stipulated by the nonvanishing resultant; in particular, \(b\ne0\) throughout \(U\), because \(f(0)=f'(0)=0\) if \(b=0\). No statement is made about singular fibers or about the \(7\)-rank or Newton polygons. The name Hasse divisor denotes the determinant divisor of Frobenius on first cohomology (equivalently the Cartier determinant) of this family, with its scheme multiplicity.

## Proof

For \(p=7\) and an odd-degree hyperelliptic model of genus \(g=5\), the coefficient formula for the Hasse–Witt/Cartier–Manin operator is \(H_{ij}=[x^{7i-j}]f^3\), for \(1\le i,j\le5\). Its rank is the Cartier rank; the \(a\)-number is \(5-\operatorname{rank}H\). Direct coefficient extraction gives, with entries in characteristic \(7\),
\[
H=\begin{pmatrix}
0&3b^2c&0&b^3&0\\
3b(a^2+b)&3ac^2&0&6abc&c^3\\
6ac&0&a(a^2+6b)&3c^2&0\\
0&0&3c&0&3(a^2+b)\\
0&1&0&0&0
\end{pmatrix}.
\]
Exact determinant expansion in \(k[a,b,c]\) yields
\[
\det H=-9ab^3\bigl(2c^5+b(a^2-b)(a^2+b)^2\bigr)=-9ab^3F.
\]
The \(4\times4\) minor obtained by removing row \(3\), column \(1\), is \(-3b^3c^4\). Because \(b\ne0\), every fiber with \(c\ne0\) has rank at least \(4\): it has rank \(4\) precisely when \(aF=0\), and otherwise rank \(5\).

For \(c=0\), exactly five potential entries remain, on separate rows and columns: \(b^3,\ 3b(a^2+b),\ a(a^2+6b),\ 3(a^2+b),\ 1\). Their ranks add. The rank equals \(3\) exactly when \(a^2+b=0\): this forces \(a\ne0\), and \(a(a^2+6b)=2a^3\ne0\). Otherwise the rank is either \(4\) or \(5\), determined by the displayed determinant. This proves the three \(a\)-number strata, including the nonexistence of larger \(a\)-numbers.

As a polynomial in \(c\) over \(k[a,b]\), \(F=2c^5+b(a^2-b)(a^2+b)^2\) is Eisenstein at the prime element \(b\): its constant term is divisible by \(b\) but not \(b^2\). Thus \(F\) is irreducible. It is coprime to \(a\), since \(F(0,b,c)=2c^5-b^4\ne0\) as a polynomial. Hence, after inverting \(b\), the determinant divisor is the reduced union of exactly those two components.

On \(V(F)\), the partial derivative \(\partial F/\partial c=10c^4=3c^4\) vanishes only when \(c=0\). At \(c=0\), \(F=b(a^2-b)(a^2+b)^2\). Since \(b\ne0\), the branch \(a^2=b\) is smooth (the factor \(a^2-b\) has nonzero \(b\)-derivative), whereas the branch \(a^2=-b\) is precisely the singular locus. Every point of this latter branch with \(a\ne0\) belongs to \(U\): for \(c=0\), a common root of \(f=x(x^{10}+ax^5+b)\) and \(f'\) occurs exactly if \(b=0\) or \(a^2=4b\), neither of which holds when \(b=-a^2\ne0\). Along this branch, \(u=a^2+b\) and \(v=c\) are local coordinates transverse to the parameter \(a\); the coefficient \(b(a^2-b)\) of \(u^2\) is a unit. Taking its formal square root transforms the completed transverse equation \(F=0\) to \(u'^2+2v^5=0\), an \(A_4\) cusp in characteristic \(7\).

Finally, if \(a=F=0\) with \(b\ne0\), then \(2c^5=b^4\), so \(c\ne0\) and \(F_c=3c^4\ne0\). Therefore the two Hasse components are smooth and transverse at their intersection. The intersection is nonempty inside \(U\), for example \((a,b,c)=(0,1,2)\) over \(\mathbb F_7\). The cusp is nonempty inside \(U\), for example \((a,b,c)=(1,6,0)\).

## Verification

Run `python3 verify_symbolic.py` with SymPy installed to rederive the \(5\times5\) matrix, the determinant identity modulo \(7\), the decisive rank minor, and the degeneration factors. The expected success line is `EXACT_HASSE_CUSP_SYMBOLIC_OK`. Run `python3 verify_primefield.py` (Python standard library only) for an independent coefficient extraction, polynomial-gcd smoothness test and Gaussian-elimination rank over all \(343\) marked parameter triples in \(\mathbb F_7^3\). It returns `GF7_EXHAUSTIVE_343_CUSP_STRATA_OK` and the respective counts: \(192\) ordinary, \(60\) of \(a\)-number \(1\), \(6\) of \(a\)-number \(2\), and \(85\) singular models. These finite checks verify sample reductions and implementation consistency; the preceding polynomial identities prove the result for every \(k\)-point.

## Relationship to prior work

Novoselov's 2019 preprint and 2020 article analyze the three-monomial dihedral family \(y^2=x^{2g+1}+ax^{g+1}+bx\), including a coefficient/Legendre-polynomial formula and Frobenius characteristic polynomials modulo \(p\) for genera up to seven. The present family introduces the cubic term \(cx^3\), which lies outside that three-monomial parameter space; the source's generalized permutation-matrix factorization no longer applies. The new statement concerns the complete Cartier-rank locus and the intrinsic cuspidal singularities of its nonordinary divisor. The general coefficient formula and the interpretation of Cartier rank are standard, and neither is claimed as novel. Frei's work on extreme \(a\)-numbers provides broader context without supplying the present family-specific stratification.

## Limitations

This is a complete \(a\)-number result on the explicitly defined smooth parameter locus only. It does not classify \(7\)-ranks, Newton polygons, isomorphism classes, or the entire genus-five hyperelliptic moduli space. The family is weighted-homogeneous under coordinate scaling, so coefficient-marked strata need not correspond to distinct isomorphism classes. Although no earlier statement of the complete four-term cusp locus was identified in inspected sources, an unindexed earlier computation could affect priority. Independent mathematical audit has not been performed.

## References

1. S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992v1, first posted 15 February 2019, especially Section 2, Theorem 4 and the mod-\(p\) tables; journal version *Finite Fields and Their Applications* **68** (2020), article 101757, DOI:10.1016/j.ffa.2020.101757.
2. S. Frei, *The \(a\)-number of hyperelliptic curves*, arXiv:1703.03516, 10 March 2017.
