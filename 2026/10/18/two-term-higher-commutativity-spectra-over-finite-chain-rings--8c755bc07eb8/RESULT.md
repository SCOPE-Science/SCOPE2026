# Two-term higher-commutativity spectra over finite chain rings

## Finding
Let \(R\) be any finite commutative chain ring of length \(m\ge2\), with residue field of cardinality \(q\), so \(|R|=q^m\). Let \(H(R)=\operatorname{UT}_3(R)\) be its three-by-three upper unitriangular group. For each integer \(r\ge1\), define \(C_r(H(R))\) to be the number of ordered \(r\)-tuples of pairwise commuting elements, including repetitions and the identity. Put
\[
A_m(q)=1+q+\cdots+q^m=\frac{q^{m+1}-1}{q-1}.
\]
Then the *complete hierarchy* is the two-term formula
\[
\boxed{C_r(H(R))=A_m(q)q^{2mr}-(A_m(q)-1)q^{(2m-1)r}.}
\]
In particular, the higher commuting probability is
\[
\boxed{P_r(H(R))=A_m(q)q^{-mr}-(A_m(q)-1)q^{-(m+1)r}.}
\]
Thus the hierarchy depends only on the residue-cardinality and the length, not on the isomorphism type or characteristic of the chain ring. Its two exponential bases are both present for \(m\ge2\), and the minimal recurrence for \(r\mapsto C_r\) has order two.

A second consequence is that the largest order of an abelian subgroup of \(H(R)\) is \(q^{2m}\) and the number of abelian subgroups of this order is exactly \(A_m(q)\). The rank-generating series, including \(r=0\) with \(C_0=1\), is
\[
\sum_{r\ge0} C_r(H(R))u^r=\frac{A_m(q)}{1-q^{2m}u}-\frac{A_m(q)-1}{1-q^{2m-1}u}.
\]
For example, for residue size two and length two, \(C_2=1408\) and \(P_2=11/32\); for residue size two and length three, \(C_2=47104\) and \(P_2=23/128\). The same formulas hold for mixed- and equal-characteristic rings with the same \((q,m)\).

## Assumptions and scope
A finite commutative chain ring has a unique maximal ideal \((\pi)\), with \(\pi^m=0\) and \(\pi^{m-1}\ne0\). Every ideal is a power of \((\pi)\); the quotient \(R/(\pi^s)\) has cardinality \(q^s\) for \(0\le s\le m\). We count labeled ordered tuples, not conjugacy classes of tuples. The formula is valid without assumptions on parity or residue characteristic and includes all positive tuple lengths. The field case \(m=1\) is an established boundary case and is not claimed as new.

Write a group element as \(h(a,b,c)\), with \(a,b,c\in R\), representing the matrix
\[
\begin{pmatrix}1&a&c\\0&1&b\\0&0&1\end{pmatrix}.
\]
The multiplication law is \(h(a,b,c)h(a',b',c')=h(a+a',b+b',c+c'+ab')\). Consequently two elements commute precisely when \(ab'-a'b=0\) in \(R\). For a tuple, the middle and top coordinates are unconstrained after choosing \(r\) columns \((a_i,b_i)\) satisfying all pairwise zero-minor equations.

## Proof
**1. Reduction to a determinantal count.** Let \(D_r(R)\) denote the number of \(2\times r\) matrices over \(R\) whose every \(2\times2\) minor is zero. Since each column has an independent central coordinate, \(C_r(H(R))=q^{mr}D_r(R)\). It suffices to prove
\[
D_r(R)=A_m(q)q^{mr}-(A_m(q)-1)q^{(m-1)r}.
\]
The case \(r=1\) is included: both sides equal \(q^{2m}\).

**2. Primitive zero-minor matrices.** For any chain ring \(S\) of length \(s\ge1\) and residue cardinality \(q\), call a vector primitive if one entry is a unit. A \(2\times r\) matrix with a unit entry and all minors zero has a primitive column \(v\) and every other column is a unique scalar multiple of \(v\). It therefore has an outer-product representation \(v w^{\mathsf T}\) with \(v\in S^2\) primitive and \(w\in S^r\) primitive. Two such representations differ precisely by \((v,w)\mapsto(uv,u^{-1}w)\) with \(u\in S^\times\). This action is free. Hence their number is
\[
\begin{aligned}
T_s(r)&=\frac{(q^{2s}-q^{2(s-1)})(q^{rs}-q^{r(s-1)})}{q^s-q^{s-1}}\\
&=(q+1)(q^r-1)q^{(r+1)(s-1)}.
\end{aligned}
\]

**3. Exhaustive valuation strata.** For a nonzero matrix \(M\) let \(v\) be the largest integer such that all entries lie in \(\pi^vR\), so \(0\le v<m\). If \(2v\ge m\), all minors vanish automatically. Taken together, the matrices with every entry in \(\pi^{\lceil m/2\rceil}R\) contribute \(q^{2r\lfloor m/2\rfloor}\), including the zero matrix. If \(2v<m\), write \(M=\pi^vM'\), where \(M'\) is a primitive matrix with entries represented modulo \(\pi^{m-v}\). The zero-minor equations modulo \(\pi^m\) are equivalent to the zero-minor equations for its reduction modulo \(\pi^{m-2v}\). Each of the \(2r\) entries has \(q^v\) lifts, and primitiveness is unchanged by reduction. Thus this exact stratum has
\[
q^{2rv}T_{m-2v}(r)=(q+1)(q^r-1)q^{(r+1)(m-1)-2v}
\]
matrices. Therefore
\[
D_r(R)=q^{2r\lfloor m/2\rfloor}+(q+1)(q^r-1)\sum_{v=0}^{\lfloor(m-1)/2\rfloor}q^{(r+1)(m-1)-2v}.
\]
Define \(B_m=(q+1)q^{m-1}\sum_{v=0}^{\lfloor(m-1)/2\rfloor}q^{-2v}\). If \(m\) is odd, the geometric sum yields \(B_m=A_m(q)\); if \(m\) is even, it yields \(B_m=A_m(q)-1\). Since the first summand above is \(q^{(m-1)r}\) in the odd case and \(q^{mr}\) in the even case, both parities simplify to the asserted formula for \(D_r(R)\). Multiplication by \(q^{mr}\) proves the main result.

**4. Maximal abelian subgroups.** Let \(B\) be an abelian subgroup of \(H(R)\), and let \(W\) be its image in \(R^2\) under \(h(a,b,c)\mapsto(a,b)\). Although \(W\) is initially only an additive subgroup, its \(R\)-linear span \(RW\) is still isotropic for the determinant pairing, by bilinearity. Any submodule of \(R^2\) has Smith normal form \(\pi^aR\oplus\pi^bR\) for some \(0\le a,b\le m\). Isotropy forces \(\pi^{a+b}=0\), so \(a+b\ge m\) and \(|RW|=q^{2m-a-b}\le q^m\). Hence \(|B|\le |Z(H(R))|\,|W|\le q^{2m}\). This bound is attained by \(\{h(0,b,c):b,c\in R\}\).

Let \(K\) be the number of abelian subgroups of maximum order \(M=q^{2m}\). Each such subgroup contains \(M^r\) commuting ordered tuples; for distinct such subgroups, their intersection has size at most \(M/q\). Every remaining commuting tuple is contained in some abelian subgroup of order strictly smaller than \(M\). Since the group has finitely many subgroups, inclusion-exclusion gives \(C_r=K M^r+O((M/q)^r)\) as \(r\to\infty\). Comparing with the exact two-term formula gives \(K=A_m(q)\), as claimed.

## Verification
The standalone script `verify.py` computes zero-minor matrices by direct ring arithmetic, not by the proof's valuation decomposition. It checks twelve configurations, including \(R=\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), \(\mathbb Z/16\mathbb Z\), and the nonisomorphic equal-characteristic rings \(\mathbb F_2[t]/(t^m)\), \(\mathbb F_3[t]/(t^2)\), and \(\mathbb F_4[t]/(t^2)\). Tuple lengths two and three are checked where computationally feasible. Run `python3 verify.py`. Expected final line: `VERIFY_OK_HEISENBERG_CHAIN 12 cases`.

## Relationship to prior work
Higher commuting probabilities \(|\operatorname{Hom}(\mathbb Z^r,G)|/|G|^r\) and their general finite Dirichlet-series nature occur in Torres-Giese [1]. Levit and Shwartz [2] give an exact asymptotic and general abelian-subgroup spectral framework, including formulas for cyclic split extensions; in particular, the cyclic-quotient subfamilies are not claimed here as independent antecedent-free discoveries. Their companion [3], Section 7, gives field-valued symplectic formulas for Heisenberg-type groups. These works do **not** supply in the inspected material the evaluated, ring-independent two-term formula for all finite chain rings of length at least two, including noncyclic additive quotients. The point-counting argument here supplies those coefficients explicitly. The elementary rank-one matrix count for a field is likewise not new.

## Limitations
The result applies to the three-by-three unitriangular group of a finite commutative chain ring. It does not address higher unitriangular ranks, simultaneous-conjugacy orbit counts, or non-chain local rings. The exact priority of this specialized evaluated formula has not been exhaustively established; it may admit another form through previously studied subgroup lattices or determinantal point counts. Computational verification is finite; the unrestricted assertion relies on the preceding proof. No independent mathematical audit has been performed.

## References
[1] E. Torres-Giese, *Higher commutativity and nilpotency in finite groups*, arXiv:1005.3876, public version 21 May 2010, https://arxiv.org/abs/1005.3876.

[2] V. E. Levit and R. Shwartz, *Higher Commutativity in Finite Groups: Exact Asymptotics and Finite Spectrum*, arXiv:2605.02071, https://arxiv.org/abs/2605.02071.

[3] V. E. Levit and R. Shwartz, *Higher Commutativity in Finite Groups: Rigidity, Extremal Bounds, and Heisenberg-Type Families*, arXiv:2605.17171, https://arxiv.org/abs/2605.17171.
