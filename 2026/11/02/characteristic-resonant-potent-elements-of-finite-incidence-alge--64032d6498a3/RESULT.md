# Characteristic-resonant potent elements of finite incidence algebras and an antichain height law

## Finding
Let \(P\) be a nonempty finite poset, let \(p\) be a prime, \(q=p^e\) for an integer \(e\ge1\), and put \(A=I(P,\mathbb F_q)\). Write \(m(P)=|\{(x,y):x<y\text{ in }P\}|\), and let \(h(P)\) be the maximum cardinality of a chain, with \(h(\varnothing)=0\). Denote by \(\mathcal N_{P,p}(q)\) the number of elements \(a\in A\) satisfying \(a^{p+1}=a\).

**Theorem (one characteristic-resonant census).** Let \(J(S)\) be the strict-interval radical of the incidence algebra of the induced subposet on \(S\subseteq P\), and set \(B_p(S,q)=|\{x\in J(S):x^p=0\}|\). If \(c_P(S)\) counts comparable pairs with exactly one endpoint in \(S\), then
\[
\boxed{\mathcal N_{P,p}(q)=\sum_{S\subseteq P}q^{c_P(S)}B_p(S,q).}
\]
In particular, when \(h(P)\le p\), every radical element of every induced subposet has \(p\)-th power zero, and
\[
\boxed{\mathcal N_{P,p}(q)=\sum_{T\subseteq P}q^{m(P)-m(T)}.}
\]
For the \(n\)-point chain, throughout the sharp first threshold \(1\le n\le p+1\), the count is
\[
\boxed{\mathcal N_{[n],p}(q)=\sum_{r=0}^n\binom nr q^{r(n-r)+\binom r2}-\mathbf 1_{n=p+1}(q-1)^p q^{\binom p2}.}
\]
The subtraction is the exact first breakdown of the low-height formula.

For *every* fixed nonempty \(P\) and fixed characteristic \(p\), as \(q=p^e\to\infty\),
\[
\boxed{\mathcal N_{P,p}(q)=H_p(P)q^{m(P)}+O_{P,p}(q^{m(P)-1}),}
\]
where \(H_p(P)\) is the number of antichains \(T\subseteq P\) whose deletion leaves \(h(P\setminus T)\le p\). In particular,
\[
\boxed{H_p(P)>0\ \Longleftrightarrow\ h(P)\le p+1.}
\]
Thus the highest possible counting degree detects an exact height transition, and at the threshold its leading coefficient counts antichain transversals of all maximum-length chains.

## Assumptions and scope
An incidence-algebra element assigns a field coefficient to each interval \((x,y)\), \(x\le y\). Multiplication is convolution, \((ab)(x,y)=\sum_{x\le z\le y}a(x,z)b(z,y)\). The strict-interval ideal \(J(P)\) has all diagonal coefficients zero and dimension \(m(P)\). The induced subposet \(S\) carries its own incidence algebra, including the empty poset with its zero-dimensional algebra and \(B_p(\varnothing,q)=1\). Chain height counts *vertices*, not covering relations. The polynomial-power equation is in the associative algebra with identity, not in its unit group. All results hold for every prime characteristic, including \(p=2\). The asymptotic varies the field extension degree while keeping \(P\) and \(p\) fixed.

## Proof
**1. Canonical primary decomposition.** In characteristic \(p\), the polynomial identity is
\[
a^{p+1}=a\quad\Longleftrightarrow\quad a(a-1)^p=0.
\]
For every such \(a\), put \(e=a^p\). Multiplying the defining equation by \(a^{p-1}\) gives \(e^2=e\), and it also gives \(ea=ae=a\). Set \(x=a-e\). Then \(x\in eAe\), and the characteristic-\(p\) binomial identity for the commuting elements \(a,e\) yields \(x^p=a^p-e^p=0\). Conversely, if \(e^2=e\), \(x\in eAe\), and \(x^p=0\), then \((e+x)^p=e\), hence \((e+x)^{p+1}=e+x\). These operations are inverse, so the decomposition \(a=e+x\) is **unique**. The diagonal entries of \(x\) vanish, since their \(p\)-th powers do, and thus \(x\) belongs to the nilpotent radical of \(eAe\).

**2. Counting fibers over diagonal idempotents.** Fix \(S\subseteq P\) and let \(d_S\) be the diagonal idempotent equal to one at vertices of \(S\) and zero elsewhere. Every idempotent \(e\) with the same diagonal is conjugate to \(d_S\) by \(U=1+J(P)\). Indeed
\[
u=e d_S+(1-e)(1-d_S)
\]
has diagonal one, is invertible, and satisfies \(e u=u d_S\). The stabilizer of \(d_S\) in \(U\) consists exactly of units whose coefficient at any strict comparable pair \((x,y)\) crossing between \(S\) and its complement is zero. Since all strict-interval coordinates of \(U\) are free, there are exactly \(q^{c_P(S)}\) idempotents with this diagonal. Conjugation identifies \(eAe\) with \(d_S A d_S\cong I(S,\mathbb F_q)\), transporting the nilpotent radicals and the equation \(x^p=0\). Combining with step 1 gives the unrestricted exact sum.

**3. Low-height simplification.** A product of \(p\) elements of \(J(S)\) can have a nonzero strict-interval coefficient only along a strict chain of \(p+1\) vertices. If \(h(P)\le p\), no induced subposet has such a chain, so \(B_p(S,q)=q^{m(S)}\). The three classes of strict comparable pairs—both in \(S\), both in \(T=P\setminus S\), and crossing—partition the total \(m(P)\). Hence \(c_P(S)+m(S)=m(P)-m(T)\), establishing the displayed polynomial.

**4. First forbidden chain.** For the chain \([n]\), choose \(r=|S|\). There are \(\binom nr\) possible \(S\), each with \(c_P(S)=r(n-r)\) and \(m(S)=\binom r2\). If \(n\le p\), all choices are unrestricted. At \(n=p+1\), the only potentially restricted \(S\) is \(S=P\). For a strictly upper triangular \((p+1)\)-square matrix \(x\), its \(p\)-th power is supported only at position \((1,p+1)\), where it equals the product of the \(p\) immediate-superdiagonal entries. Precisely \((q-1)^p q^{\binom{p+1}{2}-p}=(q-1)^p q^{\binom p2}\) choices violate \(x^p=0\). Subtracting them proves the threshold formula, including the case \(p=2\).

**5. The universal leading-coefficient law.** If \(h(S)\le p\), then \(B_p(S,q)=q^{m(S)}\). If \(h(S)\ge p+1\), choose a chain \(x_0<\cdots<x_p\) in \(S\). As a polynomial in the strict-interval coordinates of \(x\in J(S)\), the coefficient \((x^p)(x_0,x_p)\) is nonzero: setting only the \(p\) successive chain coordinates to one makes this coefficient one. It has total degree \(p\). The elementary polynomial zero bound therefore gives \(B_p(S,q)\le p q^{m(S)-1}\) (when \(q=p^e\) varies, this is uniform). For \(T=P\setminus S\), the corresponding summand is at most \(q^{m(P)-m(T)}\). Its contribution has leading order \(q^{m(P)}\) precisely if \(T\) is an antichain (so \(m(T)=0\)) and \(h(P\setminus T)\le p\). All other finitely many terms are \(O_{P,p}(q^{m(P)-1})\). This proves the asymptotic and the interpretation of \(H_p(P)\).

If \(h(P)\ge p+2\), deleting an antichain removes at most one vertex from any chain, so no antichain lowers height to \(p\). If \(h(P)\le p\), the empty antichain works. If \(h(P)=p+1\), the set of elements whose maximum chain-ending length equals a fixed \(j\in\{1,\ldots,p+1\}\) is an antichain meeting every chain of length \(p+1\). Hence it lowers the height to at most \(p\). This proves the exact positivity boundary.

## Verification
The included `verify.py` directly enumerates incidence-algebra coefficient arrays, checks \(a^{p+1}=a\) by convolution, and separately evaluates the radical-fiber formula; it covers nine prime-field poset cases in characteristics two and three, including chains, forks, and a height-two diamond. The saved run ended with `VERIFY_OK`. In particular, chain totals are \(43\) for \((p,q,n)=(2,2,3)\), \(445\) for \((2,2,4)\), and \(4996\) for \((3,3,4)\). The included `verify_ext.py` separately implements the field \(\mathbb F_4\) and tests a three-point chain (count \(269\)) and a three-point fork (count \(89\)); its run ended `VERIFY_EXTENSION_OK`.

The computations test finite instances only. The all-poset theorem and asymptotic bounds are proved above, not inferred from finite experiments. Run locally with `python3 verify.py` and `python3 verify_ext.py`; neither script requires external packages or data.

## Relationship to prior work
Gargate and Gargate (2020) enumerate \((k+1)\)-potents in triangular and incidence algebras, **assuming the coefficient characteristic divides neither \(k\) nor \(k+1\)**. The present case is \(k=p=\operatorname{char}\mathbb F_q\), so their separable-root parametrization does not apply. Their article is the principal motivation and has been examined in its available full-text presentation. Gargate and Gargate (2019) count incidence-algebra involutions in characteristic different from two, a different equation and characteristic regime. Garcés and Khrypchenko (2022) study linear maps preserving idempotents or fixed products, not the cardinalities or field-size asymptotics of the resonant solution locus. Standard idempotent lifting and elementary polynomial zero estimates are used as proof ingredients, not claimed as new.

## Limitations
The unrestricted fiber identity contains the potentially difficult function \(B_p(S,q)\). The result does **not** give an evaluated formula for this function at arbitrary poset height and does not assert that the full count is a polynomial in \(q\) in those cases. The leading coefficient is an asymptotic along field extensions of a *fixed characteristic*; it is not a uniform asymptotic as the characteristic varies. The result has been subjected to the documented self-review only; no independent mathematical audit has been performed. A general result on polynomial-power equations in incidence algebras might imply some statements under alternate terminology.

## References
1. I. Gargate and M. Gargate, *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243, first submitted 2020-08-30, https://arxiv.org/abs/2009.04243.
2. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805, first submitted 2019-07-16, https://arxiv.org/abs/1907.06805.
3. J. J. Garcés and M. Khrypchenko, *Potent preservers of incidence algebras*, Linear Algebra Appl. 635 (2022), 171–200, https://doi.org/10.1016/j.laa.2021.11.020.
4. J. J. Garcés and M. Khrypchenko, *Linear maps preserving products equal to primitive idempotents of an incidence algebra*, arXiv:2206.01788 (2022), https://arxiv.org/abs/2206.01788.
