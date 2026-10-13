# All-characteristic Rota–Baxter ranks on split square-zero local algebras

## Finding

Let \(K\) be any field, \(n\ge1\), and \(A=K1\oplus V\), where \(\dim_K V=n\) and \(V^2=0\). Every weight-zero Rota–Baxter operator \(R:A\to A\), defined by
\[
R(x)R(y)=R(R(x)y+xR(y))\quad(x,y\in A),
\]
has the unique form
\[
R(a1+v)=a u+T(v),\qquad T^2=0,\qquad 2T(u)=0,
\]
with \(u\in V\) and \(T\in\operatorname{End}_K(V)\). Conversely every such pair defines an operator. Consequently all such operators are square-zero in characteristic different from two, whereas in characteristic two all are cube-zero and a cube-zero but not square-zero example exists precisely when \(n\ge2\).

Over \(\mathbf F_q\), for \(0\le r\le\lfloor n/2\rfloor\), put
\[
N_r(q)={n\brack r}_q{n-r\brack r}_q\prod_{i=0}^{r-1}(q^r-q^i).
\]
Here \({m\brack k}_q\) is the Gaussian binomial coefficient, and empty products equal one. The complete number of operators of each linear rank is encoded by
\[
\boxed{\mathcal P_{n,q}(X)=\begin{cases}
\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}N_r(q)\bigl(q^rX^r+(q^n-q^r)X^{r+1}\bigr),&q\text{ even},\\[2mm]
\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}N_r(q)\bigl(q^rX^r+(q^{n-r}-q^r)X^{r+1}\bigr),&q\text{ odd}.
\end{cases}}
\]
In particular, the total number of operators is \(\sum_r N_r(q)q^n\) in even characteristic and \(\sum_r N_r(q)q^{n-r}\) in odd characteristic. In characteristic two the number with nonzero square is
\[
\sum_{r=1}^{\lfloor n/2\rfloor}N_r(q)(q^n-q^{n-r}).
\]

There is also a complete classification modulo algebra automorphisms. Fix the rank \(r\) of \(T\). For each pair \((T,u)\), exactly one of the following positions holds: \(u=0\); \(u\in\operatorname{im}T\setminus\{0\}\); \(u\in\ker T\setminus\operatorname{im}T\); or \(u\notin\ker T\). Every nonempty position is exactly one \(\operatorname{Aut}(A)\)-orbit. In that order, their sizes over \(\mathbf F_q\) are
\[
N_r(q),\quad N_r(q)(q^r-1),\quad N_r(q)(q^{n-r}-q^r),\quad N_r(q)(q^n-q^{n-r}).
\]
The last position occurs only in characteristic two. A position with size zero is absent.

## Assumptions and scope

The field is arbitrary for the classification, nilpotency assertions, and orbit *types*. Exact numerical counts and orbit sizes are asserted for every finite field \(\mathbf F_q\), including proper prime-power extensions. The operator weight is zero; all automorphisms are unital \(K\)-algebra automorphisms of \(A\), not arbitrary linear equivalences on the \((n+1)\)-dimensional space. The case \(n=1\) is included. For \(n=0\), the same direct argument gives only the zero operator, but that case is not in the stated range.

## Proof

**1. Reduction of the defining identity.** Write the most general linear operator as \(R(1)=a1+u\) and \(R(v)=f(v)1+T(v)\), with \(a\in K\), \(u\in V\), \(f\in V^*\), and \(T\in\operatorname{End}(V)\). Evaluating the Rota–Baxter identity on \(v,w\in V\) and comparing scalar parts gives
\[
f(v)f(w)=2f(v)f(w)\quad\text{for all }v,w.
\]
Taking \(v=w\) shows \(f=0\) over every field. Evaluating on \((1,1)\) now gives \(a^2=2a^2\) and \(2T(u)=0\), so \(a=0\). Evaluating on \((1,v)\) gives \(T^2(v)=0\). Conversely, given these conditions and \(x=s1+v\), \(y=t1+w\), both \(R(x)R(y)\) and
\[
R\bigl(R(x)y+xR(y)\bigr)=2stT(u)+tT^2(v)+sT^2(w)
\]
are zero. This proves the classification with no division by two.

**2. Nilpotency boundary.** The operator satisfies \(R^2(1)=T(u)\), \(R^2(v)=0\) for \(v\in V\), and \(R^3=0\). If \(2\ne0\) in \(K\), then \(T(u)=0\). In characteristic two, for \(n\ge2\) take two independent elements \(e_1,e_2\in V\), set \(T(e_2)=e_1\), \(T(e_1)=0\), zero on other basis vectors, and take \(u=e_2\). This yields \(R^2(1)=e_1\ne0\). For \(n=1\), \(T^2=0\) forces \(T=0\). Thus the sharp uniform exponent is two unless the characteristic is two and \(n\ge2\), when it is three.

**3. Counting the square-zero operators on the radical.** Let \(T^2=0\) with \(\operatorname{rank}T=r\). Choose \(E=\operatorname{im}T\), an \(r\)-space in \(V\); then choose a \((n-r)\)-space \(H=\ker T\) containing \(E\). Finally choose an isomorphism \(V/H\longrightarrow E\). These choices are bijective with the operators \(T\), yielding \(N_r(q)\) as claimed. The range is \(0\le r\le\lfloor n/2\rfloor\).

**4. Rank distribution.** For fixed \(T\), the image of \(R\) is \(Ku+\operatorname{im}T\). It has dimension \(r\) if \(u\in\operatorname{im}T\) and dimension \(r+1\) otherwise. In characteristic two every \(u\in V\) is allowed, with respectively \(q^r\) and \(q^n-q^r\) choices. In other characteristics the allowed \(u\)'s are exactly \(\ker T\), with respectively \(q^r\) and \(q^{n-r}-q^r\) choices. Multiplication by \(N_r(q)\) proves the two rank-enumerator formulas. In characteristic two, \(R^2\ne0\) precisely when \(u\notin\ker T\), giving the index-three count.

**5. Automorphism orbits.** An algebra automorphism fixes \(1\) and restricts to an arbitrary \(g\in\operatorname{GL}(V)\); it sends \((T,u)\) to \((gTg^{-1},gu)\). Square-zero maps of fixed rank are conjugate. Choose a decomposition \(V=E\oplus H_0\oplus F\) such that \(E=\operatorname{im}T\), \(\ker T=E\oplus H_0\), and \(T:F\to E\) is an isomorphism. Then the matrices
\[
\begin{pmatrix}P&B&C\\0&Q&D\\0&0&P\end{pmatrix},
\qquad P\in\operatorname{GL}_r(K),\quad Q\in\operatorname{GL}_{n-2r}(K),
\]
commute with \(T\) and exhaust its invertible centralizer (with the evident interpretation for zero-sized blocks). The free blocks act transitively on each nonempty subset among \(\{0\}\), \(E\setminus\{0\}\), \((E\oplus H_0)\setminus E\), and \(V\setminus\ker T\). They preserve those subsets, so these are exactly the orbits of vectors for fixed \(T\). The last one violates \(T(u)=0\) and is therefore forbidden in odd characteristic. Counting the sizes of these four subsets and multiplying by \(N_r(q)\) proves the orbit claims.

## Verification

The accompanying standalone files `verify.py` and `orbit_test.py` use only the Python standard library. Run `python3 verify.py` and `python3 orbit_test.py` from their common extracted directory. They independently test the defining Rota–Baxter identity on all basis pairs, calculate linear ranks, enumerate nonzero squares, and check group-orbit transitivity for small prime fields. The former exhaustively examines all linear operators in the specified dimensions (not only the normal-form parametrization): \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\). The latter checks all automorphism orbits for \((2,2),(2,3),(3,2)\). Successful execution ends with `VERIFY_OK` and `ORBIT_OK`. These finite checks corroborate but do not establish the universal theorems; the proof above does that.

## Relationship to prior work

Gubarev's *Rota-Baxter operators on unital algebras* (first public arXiv submission May 2, 2018; MSC 16W99) studies weight-zero operators and uniform nilpotency in characteristic zero, including a bound for unital algebras with nilpotent radicals (Section 5.2). Farooq's *Rota Baxter Operators on Truncated Polynomial Algebras* (arXiv May 15, 2026), Theorem 3.4, classifies exactly this square-zero local algebra in characteristic zero, identifying \(R^2=0\) and image in \(V\). That prior characteristic-zero classification is not claimed here as new. The present theorem addresses every characteristic, proves the characteristic-two index-three phenomenon, and gives complete finite-field rank and automorphism-orbit distributions. Gaussian coefficients and Jordan forms used in the proof are standard ingredients, not claimed as new by themselves.

## Limitations

The work does not classify nonzero-weight operators, products beyond radical-square-zero, or algebras that are not split over their residue field. It does not assert novelty for the characteristic-zero classification or for isolated low-dimensional special cases. Known results might contain an equivalent characteristic-two statement under different terminology. The small-field verifications cannot establish novelty or universal validity by themselves. No independent scientific audit has been performed.

## References

1. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723, first submitted 2018-05-02, Section 5.2, https://arxiv.org/abs/1805.00723.
2. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, first submitted 2026-05-15, Theorem 3.4 and Section 3.1, https://arxiv.org/html/2605.15670v1.
