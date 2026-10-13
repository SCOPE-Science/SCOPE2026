# Exact automorphism lifting for monomial first-order deformations of truncated polynomial algebras

## Finding

Let \(q=p^e\) be any prime power, let \(n\ge 2\), and let \(0\le r<n\). Put
\[
R=\mathbb F_q[\varepsilon]/(\varepsilon^2),\qquad
A=\mathbb F_q[x]/(x^n),\qquad
B_{n,r}=R[x]/(x^n-\varepsilon x^r).
\]
The natural homomorphism \(\rho:\operatorname{Aut}_R(B_{n,r})\longrightarrow\operatorname{Aut}_{\mathbb F_q}(A)\) has the following exact image and fiber sizes. Every special-fiber automorphism has a unique expression
\[
f(x)=x a(x),\qquad a(x)=a_0+a_1x+\cdots+a_{n-2}x^{n-2},\quad a_0\ne0.
\]
Write \(m=n-r\) and put \(\ell=m-1\) when \(p\nmid n\), but \(\ell=m\) when \(p\mid n\). Then
\[
f\in\operatorname{im}\rho\quad\Longleftrightarrow\quad
a(x)^m\equiv1\pmod{x^{\ell}},
\]
where the congruence is understood as vacuous if \(\ell=0\). In particular, putting \(\nu=v_p(m)\) and \(d=\gcd(m,q-1)\), the exact image size is
\[
I_{n,r}(q)=\begin{cases}
(q-1)q^{n-2},&\ell=0,\\
d\,q^{n-1-\lceil\ell/p^{\nu}\rceil},&\ell\ge1.
\end{cases}
\]
Every image element has exactly \(q^{n-1+\mathbf 1_{p\mid n}}\) automorphism lifts. Therefore
\[
\boxed{\left|\operatorname{Aut}_R(B_{n,r})\right|=
q^{n-1+\mathbf 1_{p\mid n}}I_{n,r}(q).}
\]
The formula is valid uniformly in both wild and tame characteristics and for every allowed deformation exponent.

## Assumptions and scope

All automorphisms are unital and fix \(R\) pointwise. The quotient \(B_{n,r}\) is a free \(R\)-module of rank \(n\) with basis \(1,x,\ldots,x^{n-1}\), since its defining polynomial is monic. Its reduction modulo \(\varepsilon\) is \(A\). The exponent \(r\) is an integer in \([0,n-1]\); no geometric smoothness or separability assumption is made. The characteristic \(p\) is the prime underlying \(q\).

## Proof

**Parameterization.** An automorphism of \(A\) is determined by \(f(x)=x a(x)\) with \(a_0\ne0\). A prospective \(R\)-algebra lift is determined by \(X=x a(x)+\varepsilon v(x)\), where \(v\) ranges over \(\mathbb F_q[x]/(x^n)\). It is a homomorphism precisely when \(X^n=\varepsilon X^r\) in \(B_{n,r}\). Because it reduces to a bijective endomorphism of \(A\), every such homomorphism is automatically bijective: in the basis displayed above, its linear matrix has invertible determinant modulo the maximal ideal \((\varepsilon)\) of \(R\).

**Defining-relation obstruction.** In \(B_{n,r}\), \(x^n=\varepsilon x^r\), \(\varepsilon^2=0\), and \(\varepsilon x^n=0\). Expansion therefore gives
\[
X^n-\varepsilon X^r
=\varepsilon\Bigl[x^r a(x)^r\bigl(a(x)^{n-r}-1\bigr)
+n x^{n-1}a_0^{n-1}v(0)\Bigr].
\]
The bracket is tested modulo \(x^n\), because multiplication by \(\varepsilon\) identifies \(A\) with \(\varepsilon B_{n,r}\). If \(p\mid n\), the second term vanishes, and, since \(a(x)^r\) is a unit, the necessary and sufficient condition is \(a(x)^m\equiv1\pmod{x^m}\); each coefficient of \(v\) is free. If \(p\nmid n\), the coefficient of \(v(0)\) at \(x^{n-1}\) is nonzero. It uniquely cancels that coefficient of the first term; the lower coefficients vanish if and only if \(a(x)^m\equiv1\pmod{x^{m-1}}\). In that case \(v(0)\) is uniquely determined and the remaining \(n-1\) coefficients of \(v\) are unrestricted. This proves the liftability test and common fiber size. When \(m=1\) and \(p\nmid n\), the condition reduces to the tautology modulo \(x^0\), so every special-fiber automorphism lifts.

**Exact counting.** If \(\ell\ge1\), the constant coefficient of \(a^m\equiv1\pmod{x^\ell}\) says \(a_0^m=1\), giving exactly \(d=\gcd(m,q-1)\) choices. For each such \(a_0\), write \(a=a_0(1+z)\) with \(z\) having zero constant term. As \(m=p^\nu u\) with \(p\nmid u\), raising principal units modulo \(x^\ell\) to the power \(u\) is bijective; equivalently the lowest nonzero coefficient of a principal unit cannot disappear under this power. Hence \((1+z)^m\equiv1\pmod{x^\ell}\) is equivalent to \(z^{p^\nu}\equiv0\pmod{x^\ell}\). By Frobenius, this forces exactly the coefficients of \(x,x^2,\ldots,x^{\lceil\ell/p^\nu\rceil-1}\) to vanish. There remain \(n-1-\lceil\ell/p^\nu\rceil\) free coefficients among \(a_1,\ldots,a_{n-2}\). Multiplying by the \(d\) choices of \(a_0\) proves the second image-size branch. If \(\ell=0\), all \((q-1)q^{n-2}\) special-fiber automorphisms lift. Multiplying the image size by the proved uniform fiber size yields the automorphism-group order.

## Verification

Run the self-contained Python 3 script `python3 verify.py`. It implements multiplication directly in the quotient ring, tests the defining relation for every possible constant infinitesimal correction, and compares with the closed formulas, independently of the symbolic obstruction calculation. It checks \(43\) complete prime-field parameter cases (characteristics \(2,3,5\)) and \(9\) further cases over \(\mathbb F_4\), for a total of \(52\) exhaustive finite tests. The script prints `EXHAUSTIVE_PARAMETER_CASES= 43 VERIFY_OK` and `INCLUDING_EXTENSION_FIELD_CASES= 52 VERIFY_OK`. This finite verification is corroboration, not a substitute for the general argument.

## Relationship to prior work

Lauritzen and Thomsen, *Hochschild cohomology and lifts of endomorphisms* (2026), Proposition 3.2, establish a general Hochschild-cohomology obstruction to lifting endomorphisms of first-order flat deformations. Their subsequent Azumaya/formally-smooth-center criterion does not directly address the singular truncated-polynomial special fiber here. Maassarani's *One generator algebras* analyzes automorphism groups for one-generator algebras, including the special fiber; it does not compute the image of the reduction map for this deformation family. Greuel and Pham discuss algebraic group actions in arbitrary characteristic, providing context for the Frobenius-sensitive behavior. The present result is a family-specific explicit test, exact image order, and exact uniform lift multiplicity, not a claim of novelty for the general obstruction itself.

## Limitations

Only the monomial deformation \(x^n=\varepsilon x^r\) and automorphisms fixing the coefficient ring \(R\) are classified. The theorem does not classify nonmonomial deformations, all endomorphism lifts, or automorphisms that do not fix \(R\). Broader deformation-stabilizer theories could imply parts of this computation; an exhaustive historical equivalence search is not claimed. The finite tests cover only the stated small fields and dimensions; the full parameter range rests on the written proof.

## References

1. N. Lauritzen and J. F. Thomsen, *Hochschild cohomology and lifts of endomorphisms*, arXiv:2604.16636v1 (17 April 2026), https://arxiv.org/html/2604.16636v1.
2. M. Maassarani, *One generator algebras over perfect fields*, arXiv:2512.20187v1 (23 December 2025), https://arxiv.org/html/2512.20187v1.
3. G.-M. Greuel and T. H. Pham, *Algorithms for group actions in arbitrary characteristic and a problem in singularity theory*, arXiv:1709.08592v1 (2017), https://arxiv.org/html/1709.08592v1.
