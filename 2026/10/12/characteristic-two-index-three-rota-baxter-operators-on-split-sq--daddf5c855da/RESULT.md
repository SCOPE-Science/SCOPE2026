# Characteristic-two index-three Rota–Baxter operators on split square-zero local algebras

## Finding

Let \(q=2^e\), \(e\ge1\), and \(A=\mathbb F_q\oplus V\), where \(\dim_{\mathbb F_q}V=n\ge1\) and \(V^2=0\). A linear map \(P:A\to A\) satisfies the weight-zero Rota–Baxter equation exactly when \(P(1)=v\in V\) and \(P|_V=T\in\operatorname{End}(V)\) with \(T^2=0\), with NO condition on \(Tv\). Consequently \(P^3=0\) always, while \(P^2\ne0\) occurs exactly when \(Tv\ne0\), and occurs for every \(n\ge2\). Under conjugation by \(\operatorname{Aut}_{\mathbb F_q\text{-alg}(A)=\operatorname{GL}(V)\), the complete orbit classification is indexed by \(r=\operatorname{rank}T\), \(0\le r\le\lfloor n/2\rfloor\), and the nonempty invariant strata \(v=0\), \(v\in\operatorname{im}T\setminus\{0\}\), \(v\in\ker T\setminus\operatorname{im}T\), \(v\notin\ker T\). There are exactly \(2n+1\) orbits when \(n\) is even and \(2n\) when \(n\) is odd. If \(s=n-2r\), the number of square-zero endomorphisms of rank \(r\) is \(H_{n,r}(q)=|\operatorname{GL}_n(q)|/(q^{r^2+2rs}|\operatorname{GL}_r(q)||\operatorname{GL}_s(q)|)\); the corresponding orbit sizes are \(H_{n,r}(q)\) multiplied by the sizes \(1\), \(q^r-1\) (if \(r>0\)), \(q^{n-r}-q^r\) (if \(s>0\)), and \(q^n-q^{n-r}\) (if \(r>0\)), respectively. The number of all operators is \(q^n\sum_rH_{n,r}(q)\), and exactly \(\sum_rH_{n,r}(q)(q^n-q^{n-r})\) have nilpotency index three.

The index-three operators show that the characteristic-zero square-zero criterion \(P^2=0\) does not extend to characteristic two. The orbit sizes determine the complete finite-field moduli census for this family rather than only the existence of counterexamples.

## Assumptions and scope

Fix \(q=2^e\) with \(e\ge1\), and \(n\ge1\). Let \(A=\mathbb F_q\oplus V\) have multiplication \((a,u)(b,w)=(ab,aw+bu)\). A weight-zero Rota–Baxter map is a base-field-linear \(P:A\to A\) obeying \(P(x)P(y)=P(xP(y)+P(x)y)\) for all \(x,y\in A\). Algebra automorphisms are unital and base-field-linear. A nilpotency index of three means \(P^3=0\) but \(P^2\ne0\). Put \(\operatorname{GL}_0(q)=\{1\}\).

## Proof

Write \(P(w)=f(w)+T(w)\) for \(w\in V\), where \(f:V\to\mathbb F_q\) is linear, and \(P(1)=a+v\). For \(u,w\in V\), the scalar components of the Rota–Baxter identity give \(f(u)f(w)=2f(u)f(w)\), hence \(f=0\) by taking \(u=w\) and using that a field has no nonzero square-zero element. Now the scalar component for \((1,1)\) gives \(a^2=2a^2\), so \(a=0\). Thus \(P(A)\subseteq V\), with \(P(1)=v\) and \(P|_V=T\). The equation at \((1,w)\) gives \(T^2(w)=0\). At \((1,1)\) it gives \(0=2T(v)\), automatic because the characteristic is two. Every pair \((v,T)\) with \(T^2=0\) conversely satisfies the defining equation on basis pairs \((1,1)\), \((1,w)\), \((u,w)\), and hence by bilinearity on all pairs. Finally \(P^2(1)=Tv\), \(P^2(V)=0\), \(P^3=0\), so index three is exactly \(Tv\ne0\).

Every algebra automorphism restricts to an arbitrary \(g\in\operatorname{GL}(V)\), and sends \((T,v)\) to \((gTg^{-1},gv)\). A square-zero endomorphism has Jordan type consisting of \(r\) size-two blocks and \(s=n-2r\) size-one blocks, with no restriction on the finite field. Fix \(T\), let \(W=\operatorname{im}T\), choose \(U\) complementing \(W\) in \(\ker T\), and let \(H\) complement \(\ker T\) in \(V\). Thus \(\dim W=\dim H=r\), \(\dim U=s\), and \(T:H\to W\) is an isomorphism. The invertible centralizer consists, in the basis ordered \((W,U,H)\), of block matrices \(\begin{psmallmatrix}g&p&m\\0&k&z\\0&0&g\end{psmallmatrix}\) with \(g\in\operatorname{GL}_r(q)\), \(k\in\operatorname{GL}_s(q)\), and unrestricted compatible blocks \(p,m,z\). Its order is \(q^{r^2+2rs}|\operatorname{GL}_r(q)||\operatorname{GL}_s(q)|\). Orbit–stabilizer therefore gives \(H_{n,r}(q)\) matrices \(T\) of that rank.

The centralizer preserves the chain \(0\subseteq\operatorname{im}T\subseteq\ker T\subseteq V\). Its displayed block form acts transitively on each nonempty difference of successive terms: invertible \(g\) moves nonzero vectors of \(W\), invertible \(k\) and free \(p\) move vectors in \(\ker T\setminus W\), and invertible \(g\) together with free \(m,z\) move those outside the kernel. Consequently the four named strata, with empty ones discarded, are exactly the vector orbits. Their sizes are respectively \(1\), \(q^r-1\), \(q^{r+s}-q^r\), and \(q^n-q^{r+s}\), with \(r+s=n-r\). Multiplying by \(H_{n,r}(q)\) gives the orbit sizes for pairs \((T,v)\). At \(r=0\) there are two strata (zero/nonzero). At positive \(r\) there are three if \(s=0\), and four otherwise. Summation gives \(2n+1\) orbits for even \(n\) and \(2n\) for odd \(n\), including \(n=1\). For each \(T\), \(q^n\) choices of \(v\) exist, of which \(q^n-q^{n-r}\) lie outside \(\ker T\); summing proves both counting identities.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. It enumerates every candidate in the proven normal form for \((n,q)=(1,2),(2,2),(3,2)\), checks the Rota–Baxter identity independently on all basis pairs, compares the resulting counts to the symbolic rank formula, and checks the index-three counts. The observed pairs (total operators, index-three operators) are \((2,0)\), \((16,6)\), \((176,84)\). The general theorem is established by the preceding proof, not by those finite tests.

## Relationship to prior work

Guo–Rosenkranz–Zheng [1] classified weight-zero Rota–Baxter operators for semigroup algebras of order two and three over characteristic zero; this provides an earlier low-dimensional computational research setting, not the present characteristic-two family. Farooq [2], Theorem 3.4, classifies the same split square-zero truncated polynomial algebras in characteristic zero, obtaining \(P^2=0\). The characteristic-two index-three phenomenon and complete \(\operatorname{GL}(V)\)-orbit sizes proved here are outside that theorem's hypotheses. Standard Jordan forms and invertible-centralizer formulas are classical ingredients; their use by itself is not claimed as novel.

## Limitations

Only weight zero, base-field-linear operators and split square-zero commutative local algebras are covered. No classification is claimed for general Artinian local algebras, nonzero weights, or non-split residue fields. A semantically equivalent characteristic-two treatment under other terminology remains possible; the literature and database comparisons are not an independence certification.

## References

[1] L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702v1 (15 February 2014), first MSC 16W99; https://arxiv.org/html/1402.3702v1.

[2] A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (15 May 2026), esp. Theorem 3.4 and Section 3.1; https://arxiv.org/html/2605.15670v1.
