# The joint opposite-product rank law for square-zero finite-field matrices

## Finding

The ranks of two opposite products of square-zero matrices admit an explicit **joint**, not merely marginal, finite-field distribution. Let \(E,F\) be independent and uniform among the square-zero \(n\)-by-\(n\) matrices of prescribed ranks \(r,s\), respectively. Write \(G_q(a,b)\) for the Gaussian binomial coefficient, zero when \(b\notin\{0,\dots,a\}\), with \(G_q(a,0)=1\).

For \(0\le j\le\min(r,s)\), define
\[
W_j=\frac{G_q(r,j)G_q(n-r,s-j)q^{(r-j)(s-j)}}{G_q(n,s)}.
\]
For integral \(x,y\) define
\[
H_j^E(x)=\frac{G_q(s-j,x)G_q(n-r-s+j,n-2r-x)q^{(s-j-x)(n-2r-x)}}{G_q(n-r,n-2r)},
\]
\[
H_j^F(y)=\frac{G_q(r-j,y)G_q(n-r-s+j,n-2s-y)q^{(r-j-y)(n-2s-y)}}{G_q(n-s,n-2s)}.
\]
Treat any term containing an out-of-range Gaussian coefficient as zero **before evaluating its power of \(q\)**. Then, for every pair of integers \(t,u\),
\[
\boxed{\Pr\bigl(\operatorname{rank}(EF)=t,\ \operatorname{rank}(FE)=u\bigr)
=\sum_{j=0}^{\min(r,s)}W_j H_j^E(s-j-t)H_j^F(r-j-u).}
\]
The factors \(H_j^E,H_j^F\) are conditional, *independent* finite Grassmann intersection distributions.

The same theorem has a sharp dimension-dependent rigidity consequence. If \(r=s=m\ge1\) and \(d=n-2m\ge0\), then
\[
\boxed{\bigl|\operatorname{rank}(EF)-\operatorname{rank}(FE)\bigr|\le\min(m,d),}
\]
and equality is attained over **every** finite field and for every such \(m,d\). Thus opposite product ranks are always equal at the maximal square-zero rank in even dimension \(n=2m\), whereas one-step discrepancies are possible and exhaust the discrepancy range in odd dimension \(n=2m+1\).

For odd dimension \(n=2m+1\), the exact probability of unequal opposite ranks at equal input rank \(m\) is
\[
2\sum_{j=0}^{m}W_jp_j(1-p_j),\qquad
p_j=\frac{q^{m-j}-1}{q^{m+1}-1}.
\]
For fixed field order \(q\) and \(m\to\infty\), this probability tends to the strictly positive, absolutely convergent Euler-series value
\[
\boxed{D_q=2Q_\infty\sum_{j=0}^{\infty}\frac{q^{-(j+1)^2}}{Q_j^2},\quad
Q_j=\prod_{h=1}^j(1-q^{-h}),\quad Q_\infty=\prod_{h=1}^{\infty}(1-q^{-h}).}
\]
Numerically \(D_2\approx0.4412860722\). This gives a sharp even/odd rigidity boundary and a persistent directional rank asymmetry in odd dimension.

## Assumptions and scope

Here \(q\ge2\) is any prime power, \(n\ge1\) an integer, and \(0\le r,s\le\lfloor n/2\rfloor\). The sampling set consists of all matrices over \(\mathbb F_q\) satisfying \(E^2=0\) and \(\operatorname{rank}(E)=r\), and independently the analogous set for \(F,s\). Neither commutativity nor mutual annihilation is assumed. All probabilities are exact rational numbers. In particular, rank zero means the unique zero matrix. Empty products equal one. For \(0\le b\le a\), \(G_q(a,b)=\prod_{i=0}^{b-1}(q^{a-i}-1)/(q^{b-i}-1)\).

## Proof

**1. Parametrization.** If \(E^2=0\), put \(A=\operatorname{im}(E)\) and \(K=\ker(E)\). Then \(A\subseteq K\), \(\dim A=r\), \(\dim K=n-r\). Conversely, any such flag together with an isomorphism \(V/K\to A\) determines exactly one rank-\(r\) square-zero endomorphism. Consequently the cardinality of the rank shell is
\[
G_q(n,r)G_q(n-r,r)\prod_{i=0}^{r-1}(q^r-q^i).
\]
Under uniform sampling, the image \(A\) is a uniform \(r\)-subspace, conditional on it the kernel \(K\) is a uniform \((n-r)\)-subspace containing \(A\), and the induced isomorphism is uniform. The choices for \(E,F\) are independent.

**2. Image overlap.** Let \(B=\operatorname{im}(F)\) and \(j=\dim(A\cap B)\). Fixing \(A\), count the \(s\)-subspaces \(B\) that intersect \(A\) in dimension \(j\). Pick the \(j\)-subspace inside \(A\), the \((s-j)\)-subspace of \(V/A\), and a graph map to \(A/(A\cap B)\). Their counts are respectively \(G_q(r,j)\), \(G_q(n-r,s-j)\) and \(q^{(r-j)(s-j)}\). Division by \(G_q(n,s)\) proves \(\Pr(j)=W_j\), including its zero-weight boundary cases.

**3. Independent kernel intersections.** In \(V/A\), the extension \(K/A\) is a uniform \((n-2r)\)-subspace. The distinguished image \((A+B)/A\) has dimension \(s-j\), with complement quotient dimension \(n-r-s+j\). The standard Grassmann intersection count, proved by choosing the intersection subspace, projecting the remaining part into a complement, and specifying its graph map, gives
\[
\Pr\bigl(\dim((K\cap B)/(A\cap B))=x\mid A,B\bigr)=H_j^E(x).
\]
Applying the same argument to \(\ker(F)/B\) gives \(H_j^F(y)\). The two extended kernels are selected independently after fixing \(A,B\), so these variables are conditionally independent. Since
\[
\operatorname{rank}(EF)=s-\dim(B\cap K)=s-j-x,
\qquad
\operatorname{rank}(FE)=r-\dim(A\cap\ker F)=r-j-y,
\]
conditioning on \(j\) and then summing establishes the displayed **joint** law.

**4. Sharp rigidity.** If \(r=s=m\), then both \(x,y\) belong to \([0,\min(d,m-j)]\), where \(d=n-2m\). Thus the absolute difference of opposite ranks is at most \(\min(d,m-j)\le\min(d,m)\). To attain equality, choose two disjoint \(m\)-subspaces \(A,B\) (possible because \(n\ge2m\)). Choose \(K/A\), a \(d\)-subspace of \(V/A\), meeting \((A+B)/A\) in dimension \(\min(d,m)\). Choose \(\ker(F)/B\) to be a \(d\)-dimensional complement to \((A+B)/B\), hence disjoint from it. Both flags extend to square-zero maps by step 1, and they have \(x=\min(d,m),\ y=0\), proving sharpness for every field and boundary \(d=0\) as well.

**5. Odd-dimensional limit.** For \(d=1\) and given \(j\), each of \(x,y\) is a Bernoulli variable supported on \(\{0,1\}\), with success probability \(p_j=(q^{m-j}-1)/(q^{m+1}-1)\), independently. The disagreement probability is therefore \(2\sum W_jp_j(1-p_j)\). For each fixed \(j\), as \(m\to\infty\),
\[
W_j\longrightarrow\frac{Q_\infty q^{-j(j+1)}}{Q_jQ_{j+1}},
\qquad p_j\longrightarrow q^{-j-1}.
\]
These identities follow by factoring powers of \(q\) in the Gaussian products and taking convergent Euler products. The ratio of the relevant Gaussian-product factors is uniformly bounded above by a constant depending only on \(q\), so \(W_j\le C_q q^{-j(j+1)}\); dominated convergence is applicable. Using \(Q_{j+1}=Q_j(1-q^{-j-1})\) yields exactly \(D_q\). Its first summand is strictly positive; convergence follows from the quadratic exponent and \(Q_j\ge Q_\infty>0\). This proves all claims.

## Verification

Run `python3 CHECK.py` with Python 3 and only the standard library. The checker enumerates all matrices for the listed small finite fields, tests square-zero and exact rank, computes both matrix products, and compares all joint coefficients with independently implemented Gaussian-intersection fractions. The preserved `CHECK_OUTPUT.txt` records successful exhaustive checks for \(111719\) ordered matrix pairs over seven configurations, including the nonprime field \(\mathbb F_4\). The proof above, rather than the enumeration, establishes the general theorem.

## Relationship to prior work

Danchev, García, and Gómez Lozano (2023) study sums of torsion and bounded-nilpotent matrices, emphasizing square-zero structures. Huang (2021) and Fulman–Guralnick (2021) enumerate mutually annihilating matrix pairs and related generating series. Their annihilation counts concern the special event \(EF=FE=0\) (with different sampling restrictions) and do not give a rank-by-rank joint law on two fixed square-zero similarity classes. The present result retains both ordered product ranks and the full conditional independence of kernel-intersection flags. Standard Gaussian-binomial intersection counts and the square-zero flag parametrization are used as known ingredients, not claimed as new.

## Limitations

An exhaustive priority search is impossible, and an equivalent formula may be implicit in broader work on representations of two-generator algebras or finite-field nilpotent pairs. No classification of matrix-product similarity types, beyond the two ranks, is claimed. The odd-dimensional limit fixes the field order and selects each square-zero matrix uniformly at maximal permissible rank. The finite checker does not prove arbitrary-size or asymptotic results. Independent external validation has not been performed.

## References

1. P. Danchev, E. García, M. Gómez Lozano, *Decompositions of Matrices Into a Sum of Torsion Matrices and Matrices of Fixed Nilpotence* (first public 2023-01-15), arXiv:2301.06106v1, https://arxiv.org/abs/2301.06106.
2. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (first public 2021-10-29), arXiv:2110.15566, https://arxiv.org/abs/2110.15566, especially Section 3.1.
3. J. Fulman and R. Guralnick, *Cohen Lenstra Partitions and Mutually Annihilating Matrices over a Finite Field* (first public 2021-11-17), arXiv:2111.09433, https://arxiv.org/abs/2111.09433.
4. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Ann. Probab. 43 (2015), 1274–1314, https://doi.org/10.1214/13-AOP889. The latter addresses unrestricted rectangular-matrix rank distributions, not this joint constrained product law.
