# Characteristic-two cubic nilpotency and orbit census for weight-zero Rota–Baxter operators on first-order neighborhoods

## Finding
Let \(k\) be any field, \(V\) an \(n\)-dimensional vector space with \(n\geq1\), and \(A=k\oplus V\) the commutative unital algebra with \(V^2=0\). All weight-zero Rota–Baxter operators \(P:A\to A\) are parametrized uniquely by
\[
P(1)=v,\qquad P(u)=Bu\ (u\in V),\qquad B^2=0,\quad 2Bv=0.
\]
Every such \(P\) satisfies \(P^3=0\). In characteristic different from two, \(P^2=0\) for every operator. In characteristic two, there are operators of nilpotency index exactly three if and only if \(n\geq2\); thus total algebra dimension three is sharp.

Under algebra-automorphism conjugacy, the complete classification is by \(r=\operatorname{rank}B\), \(0\leq r\leq\lfloor n/2\rfloor\), and by exactly one of the nonempty classes
\[
v=0,\qquad 0\ne v\in\operatorname{im}B,\qquad v\in\ker B\setminus\operatorname{im}B,\qquad v\notin\ker B.
\]
The last class occurs only in characteristic two. The total orbit numbers are
\[
\begin{cases}
2+4\lfloor n/2\rfloor-\mathbf1_{2\mid n},&\operatorname{char}k=2,\\
2+3\lfloor n/2\rfloor-\mathbf1_{2\mid n},&\operatorname{char}k\ne2.
\end{cases}
\]
The indicator is one if \(n\) is even and zero otherwise.

For a finite field \(k=\mathbb F_q\), let \({m\brack j}_q\) denote the Gaussian binomial coefficient, and write
\[
R_{n,r}(q)={n\brack r}_q{n-r\brack r}_q\,|\operatorname{GL}_r(\mathbb F_q)|.
\]
This counts square-zero \(n\)-by-\(n\) matrices of rank \(r\). If \(q\) is even, the exact number of weight-zero Rota–Baxter operators is
\[
T_{n,q}=q^n\sum_{r=0}^{\lfloor n/2\rfloor}R_{n,r}(q),
\]
and the exact number with nilpotency index three is
\[
C_{n,q}=\sum_{r=0}^{\lfloor n/2\rfloor}R_{n,r}(q)\bigl(q^n-q^{n-r}\bigr).
\]
When \(q\) is odd, the total number instead equals \(\sum_r R_{n,r}(q)q^{n-r}\), and none has index three. At each fixed even \(q\), the sharp characteristic-two phenomenon is generic:
\[
\lim_{n\to\infty}\frac{C_{n,q}}{T_{n,q}}=1.
\]

## Assumptions and scope
The algebra multiplication is \((a+u)(b+w)=ab+aw+bu\), for \(a,b\in k\), \(u,w\in V\). A weight-zero Rota–Baxter operator means a \(k\)-linear map satisfying \(P(x)P(y)=P(xP(y)+P(x)y)\) for all \(x,y\in A\). Nilpotency index is the least positive integer \(s\) with \(P^s=0\), where the zero operator has index one. Automorphisms of \(A\) are unital \(k\)-algebra automorphisms. All classifications hold over arbitrary fields, not necessarily algebraically closed. The counting and limiting assertions require a finite field and, for the limit, fixed even field order.

## Proof
**1. Classification without a characteristic restriction.** Write a general linear map as \(P(1)=a+v\), \(P(u)=f(u)+Bu\), with \(a\in k\), \(v\in V\), a linear functional \(f:V\to k\), and \(B\in\operatorname{End}_k(V)\). For \(u,w\in V\), compare scalar components of the Rota–Baxter identity. The left scalar is \(f(u)f(w)\); the right scalar is \(2f(u)f(w)\). Hence \(f(u)f(w)=0\). Taking \(w=u\) and using that \(k\) is a field gives \(f=0\), including in characteristic two. The scalar components for \((1,1)\) then yield \(a^2=2a^2\), hence \(a=0\). The vector components for \((1,1)\) yield \(2Bv=0\), and those for \((1,u)\) yield \(B^2u=0\). Conversely, if these equations hold, \(P(A)\subset V\) so \(P(x)P(y)=0\). For \(x=a+u\) and \(y=b+w\),
\[
P(xP(y)+P(x)y)=P(aBw+bBu+2abv)=aB^2w+bB^2u+2abBv=0.
\]
Thus every claimed triple and only those triples is a weight-zero operator. Its square is zero on \(V\) and sends \(1\) to \(Bv\), proving \(P^3=0\). If \(2\ne0\), then \(Bv=0\); in characteristic two \(Bv\) is free subject to \(B^2=0\). In dimension one every square-zero \(B\) is zero. For \(n=2\) choose \(B(e_2)=e_1\), \(B(e_1)=0\), and \(v=e_2\). Then \(P^2(1)=e_1\ne0\), proving the sharp threshold.

**2. Orbit classification.** The square-zero radical is the characteristic ideal of nonunits; hence each algebra automorphism fixes \(1\) and restricts to an arbitrary \(g\in\operatorname{GL}(V)\). It sends \((B,v)\) to \((gBg^{-1},gv)\). Square-zero linear maps have Jordan type \((2^r,1^{n-2r})\) over any field, so rank determines the conjugacy class of \(B\). Fix \(r\) and decompose \(V=U\oplus W\oplus T\), where \(B:W\to U\) is an isomorphism and \(B(U\oplus T)=0\), with \(\dim U=\dim W=r\), \(\dim T=s=n-2r\). Relative to these blocks, the invertible centralizer consists precisely of maps of the form
\[
g=\begin{pmatrix}A&C&D\\0&A&0\\0&E&F\end{pmatrix},
\qquad A\in\operatorname{GL}_r(k),\ F\in\operatorname{GL}_s(k),
\]
with unrestricted compatible \(C,D,E\); omit empty blocks when \(r=0\) or \(s=0\). In coordinates \(v=(u,w,t)\), this action sends \((u,w,t)\) to \((Au+Cw+Dt,Aw,Ew+Ft)\). If \(w\ne0\), the choices of \(A,E,C\) reduce \(v\) to one fixed nonzero vector in \(W\). If \(w=0,t\ne0\), the choices of \(F,D\) reduce \(v\) to one fixed nonzero vector in \(T\). If \(w=t=0,u\ne0\), the choice of \(A\) reduces \(v\) to one fixed nonzero vector in \(U\). Zero is its own orbit. These are respectively the four displayed mutually disjoint strata; the first uses \(r>0\), the second uses \(s>0\), and the third uses \(r>0\). When \(\operatorname{char}k\ne2\), the additional condition \(Bv=0\) deletes exactly the stratum \(w\ne0\). For \(r=0\) there are two orbits (zero/nonzero vector); for positive \(r\), there are four minus one if \(s=0\) in characteristic two, or three minus one if \(s=0\) in other characteristics. Summing yields the orbit formulas.

**3. Exact finite-field counts.** Choose \(U=\operatorname{im}B\), an \(r\)-space, in \({n\brack r}_q\) ways; choose \(K=\ker B\), an \((n-r)\)-space containing \(U\), in \({n-r\brack r}_q\) ways; then choose the isomorphism \(V/K\to U\) in \(|\operatorname{GL}_r(\mathbb F_q)|\) ways. This proves the formula for \(R_{n,r}\). The sizes of the corresponding operator orbits (including choices of \(B\)) are
\[
R_{n,r},\quad R_{n,r}(q^r-1),\quad R_{n,r}(q^{n-r}-q^r),\quad R_{n,r}(q^n-q^{n-r}),
\]
respectively, whenever their strata exist. For even \(q\), all \(v\in V\) are allowed and index three is equivalent to \(v\notin\ker B\), giving \(T_{n,q}\) and \(C_{n,q}\). For odd \(q\), only \(v\in\ker B\) is allowed, yielding the stated total count.

**4. Generic index three over a fixed even field.** Set \(d=\lfloor n/2\rfloor\) and \(K_q=\prod_{j\ge1}(1-q^{-j})^{-1}<\infty\). The usual product formulas for Gaussian coefficients and \(|\operatorname{GL}_r|\) imply, uniformly in \(0\le r\le d\),
\[
K_q^{-1}q^{2r(n-r)}\le R_{n,r}(q)\le K_q^2q^{2r(n-r)}.
\]
Here the lower bound uses the two Gaussian coefficients being at least their leading powers and the \(|\operatorname{GL}_r|\) product being at least \(K_q^{-1}\). The probability that an operator is square-zero when sampled uniformly among weight-zero operators equals
\[
\frac{\sum_{r=0}^d R_{n,r}(q)q^{-r}}{\sum_{r=0}^d R_{n,r}(q)}.
\]
For \(r>n/3\), \(q^{-r}\le q^{-n/3}\). For \(r\le n/3\), \(2r(n-r)\le4n^2/9\), while \(2d(n-d)\ge(n^2-1)/2\). The sum of all such small-rank terms divided by the denominator is at most \((n+1)K_q^3q^{-n^2/18+1/2}\), which tends to zero. Therefore the probability of \(P^2=0\) tends to zero, so index three has limiting probability one.

## Verification
A standalone Python 3 checker, `verify.py`, evaluates the Rota–Baxter identities directly for every linear map in the following small test spaces; then verifies rank/index counts and complete conjugacy-orbit partitions. It exhausts \(\mathbb F_2\) at \(n=1,2,3\) and \(\mathbb F_3\) at \(n=1,2\), checks \(\mathbb F_4\) at \(n=2\) through its polynomial model, and tests orbit partitions for \((q,n)=(2,2),(2,3),(3,2)\). A successful run ends with `FULL_VERIFY_OK`. The exhaustive tests verify only the stated finite cases; the generality comes from the arguments above.

## Relationship to prior work
Farooq's *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (15 May 2026), §3 and Theorem 3.4, classifies the **same square-zero-radical algebra** in characteristic zero, proving \(P^2=0\) and a block parametrization subject to \(Bv=0\). The first novelty assessed here is the characteristic-two failure of that equation: for every field of characteristic two the correct condition is \(B^2=0\) without \(Bv=0\), which yields actual cubic-nilpotent operators. The exact characteristic-two Rota–Baxter classification, associated finite-field operator census, and limiting index-three law are not stated in that primary text. The abstract orbit theory of vector-marked nilpotent matrices is substantially older: Achar–Henderson and Bellamy–Boos parametrize the general enhanced nilpotent cone. Our four-type stratification is an elementary specialization of that prior theory to square-zero matrices; neither its bare orbit count nor Jordan theory is claimed as novel independent of the operator interpretation. Other published classifications of weight-zero Rota–Baxter operators on composition, Grassmann, or matrix algebras involve different multiplication structures and do not imply this first-order-neighborhood characteristic-two spectrum without an additional argument.

## Limitations
This classification concerns weight zero, square-zero radical, and unital commutative split local algebras only; no assertion is made for higher truncation powers, nonzero weight, or general local rings. It is not a claim of new Jordan theory or absolute historical priority. An older characteristic-two treatment of the exact same local algebra under another terminology could subsume portions; no such covering statement was identified in the checked accessible sources. Finite computations are finite checks, not proof of the infinite-dimensional limit.

## References
1. A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, 15 May 2026, §3, Theorem 3.4. https://arxiv.org/html/2605.15670v1
2. V. Gubarev, *Rota–Baxter operators on unital algebras*, arXiv:1805.00723, 2018. https://arxiv.org/abs/1805.00723
3. A. Benito, V. Gubarev, P. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, 2018, publicly available manuscript.
4. P. Achar, A. Henderson, *Orbit closures in the enhanced nilpotent cone*, Adv. Math. 219 (2008), 27–62. https://arxiv.org/abs/0712.1079
5. G. Bellamy, M. Boos, *The (cyclic) enhanced nilpotent cone via quiver representations*, Manuscripta Math. 161 (2020), 333–362, first published 2018. https://doi.org/10.1007/s00229-018-1098-9
