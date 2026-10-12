# Exact Grassmann distance spectrum of a dihedral Toeplitz quasi-MRD family
## Finding

Let \(q\) be an odd prime power, let \(n\ge 3\), let \(2\le m\le n-1\), and put \(s=n-m\). Lee and Park define the constant-rank quasi-MRD code \(E_1(m,n)\subseteq\mathbb F_q^{m\times n}\) as the span of successive shifts of \(H=[I_m\;0]\). Write a nonzero coefficient vector as
\[
f(x)=\sum_{i=0}^{s} f_i x^i,
\]
and denote its matrix codeword by \(M_f\). Let
\[
U_f=\operatorname{Row}(M_f)\subseteq\mathbb F_q^n.
\]
Then the distinct row spaces form a constant-dimension code
\[
\mathcal R_{m,n}(q)=\{U_f:0\ne f\in\mathbb F_q[x],\ \deg f\le s\}\subseteq\operatorname{Gr}_q(m,n)
\]
of size
\[
L=\frac{q^{s+1}-1}{q-1}.
\]

For distinct projective classes choose monic representatives \(f,g\), write \(d=\gcd(f,g)\), and set
\[
t(f,g)=\max\{\deg f,\deg g\}-\deg d.
\]
Then
\[
\dim(U_f\cap U_g)=\max\{0,m-t(f,g)\},
\qquad
d_S(U_f,U_g)=2\min\{m,t(f,g)\}.
\]

For every \(1\le t\le s\), the number of ordered distinct projective pairs with \(t(f,g)=t\) is
\[
N_t=(q+1)q^{2t-1}\frac{q^{s-t+1}-1}{q-1}.
\]
Consequently the complete ordered subspace-distance distribution is obtained by assigning \(N_t\) pairs to distance \(2\min(m,t)\). Equivalently, distance \(2j\) has multiplicity \(N_j\) for \(1\le j<m\) and \(j\le s\), while distance \(2m\), when \(s\ge m\), has multiplicity \(\sum_{t=m}^{s}N_t\). There are no other nonzero distances. In particular,
\[
d_S(\mathcal R_{m,n}(q))=2.
\]

## Assumptions and scope

The field has odd cardinality because the source family is constructed under that hypothesis. The range \(2\le m\le n-1\) removes the source's trivial one-row case and ensures \(s\ge1\). The statement concerns the direct row spaces of the full-row-rank matrices in \(E_1(m,n)\), not the standard lifted construction \(X\mapsto\operatorname{Row}[I\mid X]\).

The parameter \(t(f,g)\) is invariant under nonzero scalar changes of \(f\) and \(g\). All products below have degree at most \(n-1\), so no quotient-ring reduction or truncation occurs.

## Proof

By Lee--Park Proposition 3.6, the rows of \(M_f\) are the coefficient vectors of
\[
f,\;xf,\;x^2f,\ldots,x^{m-1}f.
\]
Hence, under \(\mathbb F_q^n\cong\mathbb F_q[x]_{<n}\),
\[
U_f=f\,\mathbb F_q[x]_{<m}.
\]
Multiplication by nonzero \(f\) is injective, so \(\dim U_f=m\).

Write \(f=da\) and \(g=db\), where \(d\) is monic and \(\gcd(a,b)=1\). A common row-space vector has the form \(fu=gv\) with \(\deg u,\deg v<m\). Cancelling \(d\) gives \(au=bv\). Coprimality implies \(b\mid u\) and \(a\mid v\), so uniquely
\[
u=bh,\qquad v=ah.
\]
Both degree restrictions hold exactly when
\[
\deg h<m-\max\{\deg a,\deg b\}=m-t(f,g).
\]
Thus
\[
\dim(U_f\cap U_g)=\max\{0,m-t(f,g)\}.
\]
The subspace-distance formula follows from \(d_S(U,V)=2m-2\dim(U\cap V)\). If two row spaces coincide, then \(t=0\); coprimality then forces \(a=b=1\), so \(f\) and \(g\) are proportional. Thus the row spaces are indexed by \(\mathbb P^s(\mathbb F_q)\), proving the cardinality formula.

For the spectrum, let \(A_t\) count ordered coprime monic pairs \((a,b)\) with \(\deg a,\deg b\le t\). Unique monic gcd decomposition gives
\[
\sum_{\gcd(a,b)=1}u^{\deg a}v^{\deg b}=\frac{1-quv}{(1-qu)(1-qv)}.
\]
Therefore, for positive \(i,j\), the number of coprime monic pairs of exact degrees \(i,j\) is \(q^{i+j}-q^{i+j-1}\), while a degree-zero monic polynomial is \(1\). Summing over \(0\le i,j\le t\) yields
\[
A_t=\frac{q^{2t+1}-1}{q-1},
\]
so
\[
A_t-A_{t-1}=(q+1)q^{2t-1}
\]
counts coprime pairs with maximum degree exactly \(t\). For such a pair, the monic common factor \(d\) may have degree \(e=0,\ldots,s-t\), with \(q^e\) choices. Hence
\[
N_t=(q+1)q^{2t-1}\sum_{e=0}^{s-t}q^e
=(q+1)q^{2t-1}\frac{q^{s-t+1}-1}{q-1}.
\]
Finally, \(\sum_{t=1}^{s}N_t=L(L-1)\), so these strata exhaust all ordered distinct pairs.

## Verification

The bundled verifier reconstructs \(M_f\) directly from coefficients, independently computes finite-field row ranks and polynomial gcds, and exhausts all ordered projective pairs for \((q,m,n)=(3,2,4),(3,3,5),(5,3,6),(9,2,4)\). It verifies full row rank, the intersection formula, every \(t\)-stratum, every distance shell, and the total \(L(L-1)\). The \(q=9\) case uses an explicit model of \(\mathbb F_9\). The finite checks are stress tests only; the infinite statement is proved symbolically above.

## Relationship to prior work

Lee and Park prove that \(E_1(m,n)\) is an \(\mathbb F_q\)-linear constant-rank code with parameters \([m\times n,n-m+1,m]_q\), and for \(m\ge2\) it is quasi-MRD. Their full article gives the Toeplitz form used here but does not projectivize its codewords by direct row space, compute row-space intersections, or give a Grassmann distance spectrum.

Silva--Kschischang--Koetter connect rank-metric and constant-dimension codes through an identity-block lift that preserves rank distance. The direct row-space image here is different: it quotients scalar multiples and its geometry is controlled by ordinary polynomial gcds. Cyclic-subspace-code and Sidon-space constructions use extension-field scalar multiplication and do not imply the displayed bounded-degree ordinary-polynomial spectrum.

Focused searches using the source family, row-space, Grassmann, Toeplitz, gcd, polynomial-multiplication, and constant-dimension aliases found no statement implying these formulas. The closest general literature concerns the standard identity-block lift or extension-field cyclic subspace codes.

## Limitations

No Grassmannian optimality is claimed; the minimum distance is only \(2\). The result does not analyze the source's other orthogonal-group families. An older unindexed convolutional, Toeplitz, or ordinary-polynomial subspace construction could contain an equivalent intersection formula. The finite replay is not an infinite proof.

## References

1. Yoonjin Lee and Junyong Park, *Maximum rank distance codes constructed from orthogonal groups*, Linear and Multilinear Algebra 74 (2026), 1645--1670, DOI 10.1080/03081087.2026.2681140. See Proposition 3.6 and Theorem 3.7.
2. Danilo Silva, Frank R. Kschischang, and Ralf Kötter, *A Rank-Metric Approach to Error Control in Random Network Coding*, IEEE Transactions on Information Theory 54 (2008), 3951--3967, arXiv:0711.0708.
3. Ron M. Roth, Netanel Raviv, and Itzhak Tamo, *Cyclic subspace codes and Sidon spaces*, 2017 IEEE International Symposium on Information Theory, DOI 10.1109/ISIT.2017.8006635.
