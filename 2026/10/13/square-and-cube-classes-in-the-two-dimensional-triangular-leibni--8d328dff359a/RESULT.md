# Square and cube classes in the two-dimensional triangular Leibniz bialgebra moduli

## Finding

Let \(A\) and \(B\) be the two non-Lie two-dimensional Leibniz algebras occurring in Theorem 4.1 of Li, Ma, and Wang. Use a basis \(\{e,f\}\).

For \(A\), the only nonzero bracket is
\[
[f,f]=e.
\]
The theorem displays induced coalgebras
\[
\delta_\gamma(e)=0,
\qquad
\delta_\gamma(f)=\gamma e\otimes e,
\]
where the source \(r\)-matrix contains an additional parameter that does not affect \(\delta\).

For \(B\), the nonzero brackets are
\[
[f,e]=e,
\qquad
[f,f]=e.
\]
The first displayed coalgebra family can be written
\[
\delta_{A_0,\gamma}(e)=0,
\qquad
\delta_{A_0,\gamma}(f)=A_0e\otimes e+\gamma e\otimes f,
\]
where \(A_0=\lambda+\gamma\), and the second family is
\[
\varepsilon_\lambda(e)=\varepsilon_\lambda(f)
=
\lambda(e\otimes f-f\otimes e).
\]
The zero structure occurs in both families and is counted once.

We classify these induced bialgebra structures up to algebra automorphism, forgetting which \(r\)-matrix witness produced a given \(\delta\).

For \(A\),
\[
\operatorname{Aut}(A)
=
\left\{
\phi_{t,u}:
\phi(e)=t^2e,
\ \phi(f)=ue+tf,
\ t\in K^\times,
\ u\in K
\right\}.
\]
Under pushforward,
\[
(\phi_{t,u}\otimes\phi_{t,u})\,\delta_\gamma\,\phi_{t,u}^{-1}
=
\delta_{t^3\gamma}.
\]
Hence
\[
\boxed{
\mathcal T_A(K)/\!\cong
=
\{0\}\sqcup K^\times/(K^\times)^3.
}
\]

For \(B\),
\[
\operatorname{Aut}(B)
=
\left\{
\psi_t:
\psi_t(e)=te,
\ \psi_t(f)=(t-1)e+f,
\ t\in K^\times
\right\}.
\]
On the first family,
\[
\gamma'=t\gamma,
\qquad
A_0'=t^2A_0+t(t-1)\gamma.
\]
Equivalently,
\[
A_0'+\gamma'=t^2(A_0+\gamma).
\]
Thus, if \(\gamma\ne0\), the quantity
\[
s=\frac{A_0+\gamma}{\gamma^2}
\]
is invariant, and every such orbit has the unique representative
\[
\gamma=1,
\qquad
A_0=s-1.
\]
If \(\gamma=0\), nonzero \(A_0\) is classified by its square class.

On the second family,
\[
(\psi_t\otimes\psi_t)\,\varepsilon_\lambda\,\psi_t^{-1}
=
\varepsilon_\lambda,
\]
so every \(\lambda\) is fixed. Moreover, a nonzero second-family structure cannot be isomorphic to a first-family structure because \(\delta(e)=0\) in the first family but \(\varepsilon_\lambda(e)\ne0\) for \(\lambda\ne0\).

Consequently the \(B\)-isomorphism classes consist of
\[
\boxed{
\{0\}
\ \sqcup\ 
K^\times/(K^\times)^2
\ \sqcup\ 
K
\ \sqcup\ 
K^\times,
}
\]
where the four terms respectively represent the zero structure, the first-family locus \(\gamma=0\), the first-family locus \(\gamma\ne0\) indexed by \(s\), and the nonzero second family indexed by \(\lambda\).

Over \(\mathbf F_q\), put
\[
g_2=\gcd(2,q-1),
\qquad
g_3=\gcd(3,q-1).
\]
Then \(A\) has \(q\) distinct displayed coalgebra structures and
\[
\boxed{1+g_3}
\]
isomorphism classes. The algebra \(B\) has
\[
q^2+q-1
\]
distinct displayed structures and
\[
\boxed{2q+g_2}
\]
isomorphism classes.

The two underlying Leibniz algebras are nonisomorphic: \(A\) is nilpotent while \(B\) is not. Therefore, across both source algebras, there are
\[
\boxed{q^2+2q-1}
\]
distinct induced bialgebra structures and exactly
\[
\boxed{2q+1+g_2+g_3}
\]
isomorphism classes.

The reduced raw-structure parameter space has extension-field count
\[
q^{2m}+2q^m-1,
\]
so its Hasse--Weil zeta function is
\[
\boxed{
Z(T)=\frac{1-T}{(1-q^2T)(1-qT)^2}.
}
\]

## Assumptions and scope

Li, Ma, and Wang state their low-dimensional classification in Section 4 over the real field. The theorem here takes exactly the coalgebra formulas displayed in their two-dimensional tables, base-changes those polynomial formulas to an arbitrary field \(K\), and classifies the resulting induced Leibniz bialgebra structures up to algebra isomorphism.

Different \(r\)-matrices that induce the same \(\delta\) are deliberately identified; the object being classified is the Leibniz bialgebra triple \((L,[\ ,\ ],\delta)\), not a bialgebra together with a chosen witness \(r\).

The bundled verifier checks directly from Definition 2.4 that all displayed base-changed coalgebras satisfy the Leibniz coalgebra and bialgebra compatibility identities over several finite fields. The isomorphism formulas themselves are proved over an arbitrary field.

No claim is made that the source's real-field completeness theorem remains a complete classification of every triangular Leibniz bialgebra over an arbitrary non-real field. The finite-field statement classifies the base changes of the displayed two-dimensional source families.

## Proof

For \(A\), let an automorphism satisfy
\[
\phi(f)=ue+tf.
\]
Since
\[
\phi(e)=\phi([f,f])=[\phi(f),\phi(f)]=t^2e,
\]
invertibility is equivalent to \(t\ne0\), and every such pair \((t,u)\) gives an automorphism. The inverse has
\[
\phi^{-1}(f)=-ut^{-3}e+t^{-1}f.
\]
Because \(\delta_\gamma(e)=0\),
\[
\begin{aligned}
(\phi\otimes\phi)\delta_\gamma\phi^{-1}(f)
&=t^{-1}\gamma\,\phi(e)\otimes\phi(e)\\
&=t^3\gamma\,e\otimes e.
\end{aligned}
\]
This proves the cube-class quotient.

For \(B\), the derived ideal is \(Ke\), so an automorphism must have \(\psi(e)=te\). Writing \(\psi(f)=ce+df\), preservation of \([f,e]=e\) gives \(d=1\), and preservation of \([f,f]=e\) gives \(c=t-1\). This proves the automorphism formula.

For the first coalgebra family, direct pushforward gives
\[
\gamma'=t\gamma,
\qquad
A_0'=t^2A_0+t(t-1)\gamma.
\]
If \(\gamma\ne0\), then
\[
\frac{A_0'+\gamma'}{(\gamma')^2}
=
\frac{A_0+\gamma}{\gamma^2}.
\]
Conversely, choosing \(t=\gamma^{-1}\) normalizes \(\gamma\) uniquely to \(1\), so this invariant is complete. If \(\gamma=0\), the transformation is \(A_0\mapsto t^2A_0\), giving the square classes.

For
\[
T=e\otimes f-f\otimes e,
\]
one has
\[
(\psi_t\otimes\psi_t)T=tT.
\]
Since \(\varepsilon_\lambda(e)=\varepsilon_\lambda(f)=\lambda T\), the factor \(t\) from the tensor pushforward cancels the factor \(t^{-1}\) arising from \(\psi_t^{-1}\) on both basis inputs. Therefore every \(\varepsilon_\lambda\) is fixed.

For finite fields, \(\mathbf F_q^\times\) is cyclic. Hence the number of nonzero square classes is \(g_2\) and the number of nonzero cube classes is \(g_3\). The class formulas follow immediately.

The raw point count on \(A\) is \(q\). On \(B\), the first family is an affine plane with \(q^2\) points and the second an affine line with \(q\) points, meeting only at zero, so the count is \(q^2+q-1\). Replacing \(q\) by \(q^m\) gives the stated zeta function.

## Verification

The bundled program `artifacts/verify.py` independently reconstructs both source algebras, enumerates their full automorphism groups, and implements pushforward of coalgebra structures.

It also checks the Leibniz coalgebra identity and both bialgebra compatibility equations from Definition 2.4 for every displayed parameter over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,\quad
\mathbf F_{11}.
\]

For \(q=2,3,5,7,11\), the numbers of \(A\)-classes are
\[
2,\ 2,\ 2,\ 4,\ 2,
\]
and the numbers of \(B\)-classes are
\[
5,\ 8,\ 12,\ 16,\ 24.
\]
The total class counts are
\[
7,\ 10,\ 14,\ 20,\ 26,
\]
matching
\[
2q+1+\gcd(2,q-1)+\gcd(3,q-1).
\]

The checker verifies the two transformation laws and the fixedness of every second-family parameter and returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field orbit classification is proved symbolically above.

## Relationship to prior work

Sheng and Tang introduced triangular Leibniz bialgebras and the classical Leibniz Yang--Baxter equation. Their Example 4.10 already solves the symmetric \(r\)-matrix equation for the algebra \(B\), producing the two \(r\)-matrix families that later reappear in the two-dimensional table.

Li, Ma, and Wang then give all two-dimensional triangular Leibniz bialgebras over the real field in Theorem 4.1 and explicitly list both induced coalgebras. Their paper does not quotient those parameter families by algebra automorphisms: document-wide searches for `automorphism` and `isomorphism` return no classification of the table parameters.

The present result starts after those classifications: it forgets redundant \(r\)-matrix witnesses, computes the full automorphism actions on the induced coalgebras, and identifies the square-class and cube-class arithmetic controlling the quotient. In particular, the finite-field formulas are not raw parameter counts from the source tables.

A later quasi-triangular/factorizable Leibniz bialgebra theory broadens the structural framework but does not provide this low-dimensional automorphism quotient.

## Limitations

The theorem classifies only the base changes of the two induced coalgebra families displayed in the source's two-dimensional real classification.

It classifies Leibniz bialgebra structures after forgetting the chosen \(r\)-matrix witness. A finer moduli problem retaining \(r\) would have additional parameters.

No completeness claim is made for all finite-field triangular Leibniz bialgebras beyond these base-changed source families.

Failed literature searches do not prove absolute historical novelty.

## References

1. H. Li, T. Ma, and S. Wang, “When Leibniz algebras are Nijenhuis?”, arXiv:2310.14267v1, first public 22 October 2023.
2. Y. Sheng and R. Tang, “Leibniz bialgebras, relative Rota--Baxter operators and the classical Leibniz Yang--Baxter equation,” arXiv:1902.03033v1, first public 8 February 2019; *Journal of Noncommutative Geometry* 16 (2022).
3. C. Bai, G. Liu, Y. Sheng, and R. Tang, “Quasi-triangular, factorizable Leibniz bialgebras and relative Rota--Baxter operators,” DOI `10.1515/forum-2023-0268`.
