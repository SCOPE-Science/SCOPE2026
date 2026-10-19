# Characteristic-two nilpotency jump and orbit law for Rota–Baxter operators on square-zero local algebras

## Finding
Let \(K\) be any field of characteristic \(2\), let \(n\geq1\), and let \(A=K1\oplus V\) be the commutative associative unital algebra with \(\dim_KV=n\) and \(V^2=0\). The weight-zero Rota–Baxter operators \(P:A\to A\) are **exactly**
\[
P(a1+v)=a u+T(v),\qquad u\in V,\quad T\in\operatorname{End}_K(V),\quad T^2=0.
\]
In particular \(P^3=0\) always, and \(P^2\ne0\) exactly when \(T(u)\ne0\). For \(n\ge2\) this gives the sharp Rota–Baxter nilpotency bound \(3\), whereas for \(n=1\) it is \(2\).

The automorphism group \(\operatorname{Aut}_K(A)=\operatorname{GL}(V)\) has exactly \(2n+1\) conjugacy orbits of these operators for even \(n\), and exactly \(2n\) for odd \(n\). For each rank \(r=\operatorname{rank}T\), set \(s=n-2r\). There are two marked-vector orbits if \(r=0\), three if \(r>0\) and \(s=0\), and four if \(r>0\) and \(s>0\). Their invariants are respectively \(u=0\), \(0\ne u\in\operatorname{im}T\), \(u\in\ker T\setminus\operatorname{im}T\), and \(u\notin\ker T\), omitting empty cases.

For \(K=\mathbb F_q\), \(q\) a power of \(2\), put
\[
B_{n,r}(q)={n\brack r}_q{n-r\brack r}_q\,|\operatorname{GL}_r(q)|,
\qquad 0\le r\le\lfloor n/2\rfloor.
\]
Here \({a\brack b}_q\) is the Gaussian binomial coefficient. The total number of weight-zero operators and the number having nilpotency index exactly \(3\) are
\[
\#\operatorname{RB}_0(A)=q^n\sum_{r=0}^{\lfloor n/2\rfloor}B_{n,r}(q),
\qquad
\#\{P:P^2\ne0\}=\sum_{r=0}^{\lfloor n/2\rfloor}B_{n,r}(q)(q^n-q^{n-r}).
\]
The complementary exact count is \(\#\{P:P^2=0\}=\sum_rB_{n,r}(q)q^{n-r}\), including the zero operator.

For fixed even-field order \(q\), write \(n=2m+\epsilon\), where \(\epsilon\in\{0,1\}\), and define
\[
c_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\qquad
W_{\epsilon,j}(q)=\frac{q^{-2j(j+\epsilon)}}{c_{2j+\epsilon}(q)},\qquad
C_{q,\epsilon}=\frac{\sum_{j\ge0}q^jW_{\epsilon,j}(q)}{\sum_{j\ge0}W_{\epsilon,j}(q)}.
\]
These series are positive and absolutely convergent. If \(P\) is uniformly random among the weight-zero operators, then
\[
\Pr(P^2=0)=C_{q,\epsilon}q^{-m}(1+o(1))
\quad\text{as }n=2m+\epsilon\longrightarrow\infty.
\]
Thus a uniformly chosen operator has nilpotency index \(3\) with probability tending to \(1\). For \(q=2\), the constants are approximately \(C_{2,0}=1.41971069618\) and \(C_{2,1}=1.08804625772\).

## Assumptions and scope
All operators are \(K\)-linear, and the weight-zero identity uses the normalization
\[
P(x)P(y)=P\bigl(xP(y)+P(x)y\bigr)
\quad\text{for all }x,y\in A.
\]
The algebra is split local and commutative with square-zero maximal ideal \(V\). No algebraic-closure assumption is used in the classification or orbit formula. The finite enumeration and asymptotic require \(K=\mathbb F_q\) with characteristic \(2\); the asymptotic keeps \(q\) fixed and lets the radical dimension grow. The nilpotency index of the zero operator is understood as \(1\); the statement \(P^2\ne0\) avoids convention-dependent notation.

## Proof
**1. Reduction to square-zero endomorphisms.** Write \(P(v)=\ell(v)1+T(v)\) for \(v\in V\). Applying the identity with \(x=y=v\) and comparing coefficients of \(1\) gives \(\ell(v)^2=2\ell(v)^2\), hence \(\ell(v)=0\). For \(P(1)=a1+u\), the same identity at \(x=y=1\) in characteristic two reads \(P(1)^2=P(0)=0\); since \(V^2=0\), its scalar part is \(a^2=0\), so \(a=0\). Finally, the identity at \(x=1,y=v\) has left side \(uT(v)=0\) and right side \(P(T(v))=T^2(v)\), proving \(T^2=0\).

Conversely, for any \(u\in V\) and square-zero \(T\), define \(P\) by the displayed normal form. Both \(P(x)\) and \(P(y)\) lie in \(V\) and multiply to zero. With \(x=a1+v\), \(y=b1+w\), the other side becomes
\[
P\bigl(aP(y)+bP(x)\bigr)
=P\bigl(2ab u+aT(w)+bT(v)\bigr)=0
\]
by characteristic two and \(T^2=0\). Hence every displayed map is a Rota–Baxter operator. Moreover \(P^2(1)=T(u)\), \(P^2(V)=0\), and \(P^3=0\). When \(n\ge2\), choose \(T(e_2)=e_1\), \(T(e_i)=0\) for \(i\ne2\), and \(u=e_2\); then \(P^2(1)=e_1\ne0\). In dimension one, \(T^2=0\) forces \(T=0\).

**2. Complete conjugacy-orbit classification.** Every unital algebra automorphism fixes \(1\) and acts on the nilradical \(V\) by an arbitrary \(g\in\operatorname{GL}(V)\), taking \((u,T)\) to \((gu,gTg^{-1})\). Square-zero \(T\) has Jordan type \((2^r,1^s)\), \(s=n-2r\), over any field. Split \(V=X\oplus Y\oplus Z\), with \(\dim X=\dim Y=r\), \(\dim Z=s\), and \(T:Y\to X\) an isomorphism, zero on \(X\oplus Z\). A commuting invertible map acts as
\[
(x,y,z)\longmapsto(Ax+By+Dz,\;Ay,\;Cy+Ez),
\]
where \(A\in\operatorname{GL}_r(K)\), \(E\in\operatorname{GL}_s(K)\), and \(B,C,D\) are unrestricted compatible linear maps. This group is transitive on each nonempty stratum \(u=0\), \(u\in X\setminus\{0\}\), \(u\in(X\oplus Z)\setminus X\), and \(u\notin X\oplus Z\); different strata are distinguished by membership in \(\operatorname{im}T\) and \(\ker T\). Therefore rank zero contributes \(2\) orbits, each \(0<r<n/2\) contributes \(4\), and the terminal rank \(r=n/2\) (when integral and positive) contributes \(3\). Summing yields \(2n+1\) for positive even \(n\), or \(2n\) for odd \(n\), including \(n=1\).

**3. Exact finite-field counts.** If \(\operatorname{rank}T=r\) and \(T^2=0\), choose \(U=\operatorname{im}T\) of dimension \(r\), choose \(W=\ker T\supseteq U\) of dimension \(n-r\), and choose an isomorphism \(V/W\to U\). There are respectively \({n\brack r}_q\), \({n-r\brack r}_q\), and \(|\operatorname{GL}_r(q)|\) choices, proving \(B_{n,r}(q)\). For every \(T\), there are \(q^n\) choices of \(u\); precisely \(q^{n-r}\) of them satisfy \(T(u)=0\). This yields both stated exact counts, including all boundaries \(r=0\) and \(r=\lfloor n/2\rfloor\).

**4. Sharp probability.** The Gaussian coefficient formula gives exactly
\[
B_{n,r}(q)=q^{2r(n-r)}\frac{c_n(q)}{c_r(q)c_{n-2r}(q)}.
\]
With \(n=2m+\epsilon\) and \(r=m-j\), divide by \(q^{2m(m+\epsilon)}\). The resulting weight is
\[
q^{-2j(j+\epsilon)}\frac{c_{2m+\epsilon}(q)}{c_{m-j}(q)c_{2j+\epsilon}(q)}
\longrightarrow W_{\epsilon,j}(q)
\]
for each fixed \(j\). The products \(c_k(q)\) are bounded below by the positive limit \(\prod_{i\ge1}(1-q^{-i})\), so these terms, even after multiplying by \(q^j\), have an absolutely summable bound independent of \(m\). Dominated convergence in the denominator and in the numerator for \(\Pr(P^2=0)=q^{-m}\bigl(\sum_j q^j B_{n,m-j}\bigr)/\bigl(\sum_j B_{n,m-j}\bigr)\) gives the constant \(C_{q,\epsilon}\) and the asserted sharp equivalent.

## Verification
The bundled pure-Python program `artifacts/verify.py` directly checks the defining identity on all matrices of linear maps for \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)\), without assuming the normal form. It also verifies the exact square-zero rank formula, the orbit count by explicit \(\operatorname{GL}_n(q)\) actions in five small configurations, and the parity-dependent asymptotic constants at \(n=80,81\) over fields of orders \(2\) and \(4\). An exhaustive full-map test over \(\mathbb F_4\) in radical dimension \(2\) finds \(256\) operators, of which \(180\) have nonzero square. Run `python3 artifacts/verify.py` from the package root; successful execution ends with `FULL_VERIFY_OK`. Finite enumerations do not prove the all-dimensional statements, which follow from the preceding arguments.

## Relationship to prior work
Azhar Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (May 15, 2026), Theorem 3.4, classifies the same weight-zero problem in characteristic zero, finding \(P^2=0\) and \(\operatorname{im}P\subseteq V\). That proof uses division by two. The present characteristic-two classification differs structurally: \(u\) is unrestricted and \(P^2\ne0\) is possible. The complete automorphism-orbit count and sharp finite-field probability law are not implied by Farooq's characteristic-zero theorem.

Vsevolod Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723 (2018; published 2021), develops the nilpotency-index invariant and proves general nilpotence in characteristic zero, not the characteristic-two square-zero-radical classification. Benito, Gubarev and Pozhidaev, *Rota-Baxter Operators on Quadratic Algebras*, arXiv:1801.07037 (2018), explicitly assumes characteristic different from two, and its main classifications address different settings. Standard linear-algebra facts about square-zero matrices and their Jordan forms are used as known input; they are not claimed as discoveries.

## Limitations
The nilpotency-index jump is special to characteristic two and to the split square-zero-local-algebra family. There is no claim about the full classification for radicals of higher nilpotence degree, other weights, or other algebras. The probability equivalent holds with \(q\) fixed and \(n\to\infty\), not uniformly as \(q\) grows. Bibliographic searching does not exclude all unindexed equivalent results; independent mathematical validation has not been performed.

## References
1. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (first public version 2026-05-15), https://arxiv.org/html/2605.15670v1 .
2. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723, https://arxiv.org/abs/1805.00723 .
3. P. Benito, V. Gubarev and A. Pozhidaev, *Rota-Baxter Operators on Quadratic Algebras*, arXiv:1801.07037, https://arxiv.org/abs/1801.07037 .
