# Characteristic-two Rota–Baxter operators on square-zero local algebras: exact rank, orbit and nilpotency profiles

## Finding
Let \(A=K1\oplus V\) be the unital commutative algebra with \(V^2=0\), where \(r=\dim_K V\ge1\). A weight-zero Rota–Baxter operator means a \(K\)-linear map \(R:A\to A\) satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr)\quad(x,y\in A).
\]
**Normal form over every field.** Such an \(R\) is equivalent to a unique pair \((u,T)\) with
\[
R(1)=u\in V,\qquad R(v)=Tv\ (v\in V),\qquad T^2=0,\qquad 2Tu=0.
\]
In characteristic two, the last condition disappears; \(R^3=0\), and \(R^2(1)=Tu\). Hence the nilpotency index is exactly three if and only if \(Tu\ne0\), a possibility precisely when \(r\ge2\). In characteristic other than two all these operators instead satisfy \(R^2=0\).

**Exact finite-field census.** For \(q\) a power of two, put \(M_{r,t}(q)={r\brack t}_q{r-t\brack t}_q|\mathrm{GL}_t(q)|\), for \(0\le t\le\lfloor r/2\rfloor\), where \({n\brack k}_q\) denotes the Gaussian binomial coefficient and \(|\mathrm{GL}_0(q)|=1\). The numbers of weight-zero operators with radical-block rank \(t\), respectively nilpotency index exactly three, are
\[
q^r M_{r,t}(q),\qquad (q^r-q^{r-t})M_{r,t}(q).
\]
The complementary rank-\(t\) count with \(R^2=0\) is \(q^{r-t}M_{r,t}(q)\). The total is \(q^r\sum_{t=0}^{\lfloor r/2\rfloor}M_{r,t}(q)\).

**Conjugacy-orbit classification.** Algebra automorphisms act by the natural \(\mathrm{GL}(V)\) action on \((T,u)\): \((T,u)\mapsto(gTg^{-1},gu)\). For each \(t\ge1\), the nonempty classes are given by \(u=0\), \(0\ne u\in\operatorname{im}T\), \(u\in\ker T\setminus\operatorname{im}T\), and \(u\notin\ker T\). The third type exists exactly when \(r>2t\). For \(t=0\), there are precisely the two classes \(u=0\) and \(u\ne0\). Thus the total number of conjugacy classes is
\[
\begin{cases}2r,&r\text{ odd},\\2r+1,&r\text{ even}.\end{cases}
\]
For fixed positive \(t\), their cardinalities in that displayed order are \(M_{r,t}(q)\), \(M_{r,t}(q)(q^t-1)\), \(M_{r,t}(q)(q^{r-t}-q^t)\) when nonempty, and \(M_{r,t}(q)(q^r-q^{r-t})\). At \(t=0\), the two sizes are \(1\) and \(q^r-1\).

## Assumptions and scope
The normal form and orbit classification hold over **every** field, the distinction using only its characteristic; numerical counts assume \(K=\mathbb F_q\) with \(q\) a power of two. Every operator is \(K\)-linear. Conjugacy is under algebra automorphisms, **not** arbitrary linear changes of the whole vector space \(A\); all such algebra automorphisms fix \(1\) and act on the unique maximal ideal \(V\). The result concerns weight zero, not nonzero weight, and \(r\ge1\). Nilpotency index means the smallest positive \(j\) such that \(R^j=0\).

## Proof
Write a general linear map as \(R(1)=a1+u\), \(R(v)=\ell(v)1+Tv\), with \(a\in K\), \(u\in V\), a linear functional \(\ell\), and an endomorphism \(T\). Substitute \(x=y=v\in V\) into the Rota–Baxter identity and compare scalar parts. Since \(V^2=0\), this yields \(\ell(v)^2=2\ell(v)^2\), hence \(\ell(v)=0\) over **any** field. Substituting \(x=y=1\) and comparing scalar parts now gives \(a^2=2a^2\), so \(a=0\); its radical part gives \(2Tu=0\). Substituting \(x=1,y=v\) gives \(T^2v=0\) for every \(v\). Conversely the identity is bilinear in \((x,y)\), so checking the three types of basis pairs \((1,1)\), \((1,v)\), \((v,w)\) proves these conditions suffice. Powers satisfy \(R^2(1)=Tu\), \(R^2(V)=0\), and \(R^3=0\). If the characteristic is not two, \(2Tu=0\) forces \(Tu=0\); if it is two and \(r\ge2\), choose \(Tx_1=x_2\) and \(Tx_i=0\) otherwise, with \(u=x_1\).

For any rank-\(t\) square-zero map \(T\), its image \(U\) has dimension \(t\) and lies in its kernel \(W\) of dimension \(r-t\). Choosing \(U\subset W\subset V\), then an isomorphism \(V/W\to U\), recovers \(T\) uniquely. The number of such flags and isomorphisms is \({r\brack t}_q{r-t\brack t}_q|\mathrm{GL}_t(q)|\). For fixed \(T\), there are \(q^r\) choices for \(u\); exactly \(q^{r-t}\) lie in \(\ker T\). This proves the census and index-three formula.

To classify conjugacy, place \(T\) in a basis \(x_1,\ldots,x_t,y_1,\ldots,y_t,z_1,\ldots,z_{r-2t}\) with \(Tx_i=y_i\) and \(Ty_i=Tz_j=0\). Its centralizer in \(\mathrm{GL}(V)\) is transitive on each of the four indicated nonempty regions: simultaneous invertible changes in the \(x\)- and \(y\)-blocks move nonzero \(y\)-vectors to \(y_1\); invertible changes of the \(z\)-block and permitted shears \(z\mapsto z+\sum a_i y_i\) move vectors of \(\ker T\setminus\operatorname{im}T\) to \(z_1\); for vectors outside \(\ker T\), change the nonzero \(x\)-component to \(x_1\) and use shears \(x_1\mapsto x_1+\sum b_i y_i+\sum c_j z_j\) to eliminate the remaining components. Each such change commutes with \(T\) and is invertible. The four regions are invariant, establishing both exhaustiveness and inequivalence. Counting their vectors yields the class sizes. Summing two classes at \(t=0\), four per \(1\le t<r/2\), and three at \(t=r/2\) when \(r\) is even yields the stated total.

## Verification
The accompanying standalone script `check_rota_baxter.py` exhaustively enumerates **all** linear maps on \(A\) and directly checks the Rota–Baxter identity on basis pairs. It tests \((q,r)=(2,1),(2,2),(2,3),(4,1),(4,2)\), comprising \(328{,}464\) linear maps; it independently checks rank and nilpotency counts and brute-force \(\mathrm{GL}_r(\mathbb F_2)\) conjugacy orbits for \(r=1,2,3\). All tests passed. Use `python3 check_rota_baxter.py` in the same directory. The exact finite tests corroborate, but do not establish, the general proof.

## Relationship to prior work
Gubarev (2018, §§5.1–5.2) constructs general weight-zero Rota–Baxter operators and proves characteristic-zero nilpotency for unital algebraic algebras, including discussion of their Rota–Baxter index. His source assigns primary MSC code 16W99. Gubarev's later *Spectrum of Rota–Baxter operators* (2020, §4, Theorem 2) extends spectral nilpotence to positive characteristic but does not determine these orbit and rank distributions. Farooq (2026, §3, Theorem 3.4) classifies operators on the **same** square-zero local algebra in characteristic zero: his block condition is \(T^2=Tu=0\). The characteristic-two alternative \(Tu\ne0\), its exact nilpotency-index-three locus, and the dimension-uniform finite-field conjugacy census are outside those stated characteristic-zero hypotheses. This comparison concerns claims and implications, not just titles.

## Limitations
The finite-field counts are for even prime powers, and the conjugacy classification uses the automorphism action fixing the unit. This does not classify weight-one operators, higher radical nilpotence, or classification under a different equivalence relation. The cited literature comparisons are not proof of historical uniqueness; an older equivalent classification in specialized modular Rota–Baxter literature remains possible. The checker does not certify infinite-dimensional cases, and no independent audit has been performed.

## References
1. V. Gubarev, *Rota–Baxter operators on unital algebras*, arXiv:1805.00723 (first public May 2, 2018), https://arxiv.org/html/1805.00723v3, §§5.1–5.2.
2. V. Gubarev, *Spectrum of Rota–Baxter operators*, arXiv:2006.02654 (first public 2020), https://arxiv.org/html/2006.02654v2, §4, Theorem 2.
3. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670 (first public May 15, 2026), https://arxiv.org/abs/2605.15670, §3, Theorem 3.4.
