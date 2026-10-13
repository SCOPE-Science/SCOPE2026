# Exact gcd of the symmetric determinantal rank tower
## Finding
For every integer \(n\ge2\), let
\[
X_{n,r}\subset\mathbb P(\operatorname{Sym}^2\mathbb C^n),
\qquad
1\le r\le n-1,
\]
be the projective locus of symmetric \(n\times n\) matrices of rank at most \(r\). Write
\[
D_{n,r}=\deg X_{n,r}
\]
for its projective degree and define
\[
G_n=\gcd_{1\le r\le n-1}D_{n,r}.
\]

Then
\[
\boxed{
G_n=
\begin{cases}
2,&n=2,\\
2^{e-1}=n/2,&n=2^e,\ e\ge2,\\
1,&n\ge3\text{ and }n\text{ is not a power of }2.
\end{cases}}
\]

Consequently, the entire proper symmetric determinantal rank tower has a nontrivial common prime divisor exactly when the matrix size is a power of two. In that case the only common prime is \(2\), and for \(n=2^e\ge4\) its exact common exponent is \(e-1\).

## Assumptions and scope
The base field is \(\mathbb C\), and degrees are taken in the standard projective embedding
\[
\mathbb P(\operatorname{Sym}^2\mathbb C^n).
\]

It is convenient to index by corank
\[
q=n-r,
\qquad
1\le q\le n-1.
\]
The classical symmetric determinantal degree formula is
\[
D_{n,n-q}
=
\prod_{j=0}^{q-1}
\frac{\binom{n+j}{q-j}}{\binom{2j+1}{j}}.
\]
Equivalently,
\[
D_{n,n-q}
=
\prod_{j=0}^{q-1}
\frac{(n+j)!\,j!\,(j+1)!}
{(q-j)!\,(n-q+2j)!\,(2j+1)!}.
\]

The rank-one member is the quadratic Veronese variety, so
\[
D_{n,1}=2^{n-1},
\]
while the corank-one member is the determinant hypersurface, so
\[
D_{n,n-1}=n.
\]

## Proof
We first prove a prime-primary witness lemma.

Let \(p\) be prime, put
\[
e=\nu_p(n),
\qquad
q=p^e,
\]
and assume
\[
q<n.
\]
Then
\[
p\nmid D_{n,n-q}.
\]

Indeed, for
\[
F_p(m)=\nu_p(m!)
\]
the factorial degree formula gives
\[
\nu_p(D_{n,n-q})
=
\sum_{a\ge1}E_{p^a}(n,q),
\]
where, for \(t=p^a\),
\[
E_t(n,q)
=
\sum_{j=0}^{q-1}
\left(
\left\lfloor\frac{n+j}{t}\right\rfloor
+
\left\lfloor\frac jt\right\rfloor
+
\left\lfloor\frac{j+1}{t}\right\rfloor
-
\left\lfloor\frac{q-j}{t}\right\rfloor
-
\left\lfloor\frac{n-q+2j}{t}\right\rfloor
-
\left\lfloor\frac{2j+1}{t}\right\rfloor
\right).
\]

Suppose first that
\[
a\le e.
\]
Write
\[
q=Qt,\qquad n=Nt.
\]
Then
\[
\sum_{j=0}^{q-1}\left\lfloor\frac jt\right\rfloor
=
\frac{tQ(Q-1)}2,
\]
and
\[
\sum_{j=0}^{q-1}\left\lfloor\frac{j+1}{t}\right\rfloor
=
\frac{tQ(Q-1)}2+Q.
\]
Moreover,
\[
\sum_{j=0}^{q-1}\left\lfloor\frac{q-j}{t}\right\rfloor
=
\sum_{j=0}^{q-1}\left\lfloor\frac{j+1}{t}\right\rfloor,
\]
while
\[
\sum_{j=0}^{q-1}
\left(
\left\lfloor\frac{2j}{t}\right\rfloor
+
\left\lfloor\frac{2j+1}{t}\right\rfloor
\right)
=
\sum_{u=0}^{2q-1}\left\lfloor\frac ut\right\rfloor
=
tQ(2Q-1).
\]
Finally,
\[
\sum_{j=0}^{q-1}\left\lfloor\frac{n+j}{t}\right\rfloor
=
qN+\frac{tQ(Q-1)}2,
\]
and
\[
\sum_{j=0}^{q-1}\left\lfloor\frac{n-q+2j}{t}\right\rfloor
=
q(N-Q)+
\sum_{j=0}^{q-1}\left\lfloor\frac{2j}{t}\right\rfloor.
\]
Substitution gives
\[
E_t(n,q)=0.
\]

Now suppose
\[
a>e.
\]
Write
\[
t=qs,
\qquad
n=mq,
\]
where
\[
s=p^{a-e}
\]
and \(p\nmid m\). Write
\[
m=hs+\rho
\]
with
\[
1\le \rho\le s-1.
\]
For \(0\le j<q\),
\[
\left\lfloor\frac{n+j}{t}\right\rfloor=h
\]
and
\[
\left\lfloor\frac{n-q+2j}{t}\right\rfloor=h.
\]
All four remaining floor terms vanish because
\[
q<t
\]
and
\[
2j+1<2q\le t.
\]
Hence again
\[
E_t(n,q)=0.
\]
Thus
\[
\nu_p(D_{n,n-q})=0,
\]
proving the witness lemma.

We can now handle every \(n\) that is not a power of two. Any prime dividing \(G_n\) must divide the corank-one degree
\[
D_{n,n-1}=n.
\]
Let \(p\mid n\). If
\[
p^{\nu_p(n)}<n,
\]
the witness lemma supplies the proper corank
\[
q=p^{\nu_p(n)}
\]
for which
\[
p\nmid D_{n,n-q}.
\]
The only remaining case is that \(n\) itself is a prime power. If \(n\) is not a power of two, this means
\[
n=p^e
\]
for an odd prime \(p\). The rank-one degree is
\[
D_{n,1}=2^{n-1},
\]
so again
\[
p\nmid D_{n,1}.
\]
Therefore no prime divides every proper symmetric determinantal degree, and
\[
G_n=1
\]
whenever \(n\ge3\) is not a power of two.

It remains to treat
\[
n=2^e.
\]
The case \(n=2\) has the single proper degree \(2\), so
\[
G_2=2.
\]
Assume now
\[
e\ge2.
\]

Let
\[
A_q=D_{n,n-q}.
\]
From the product formula one obtains the adjacent-corank ratio
\[
\frac{A_q}{A_{q-1}}
=
\frac{\displaystyle\prod_{j=0}^{q-1}(n-q+1+2j)}
{\displaystyle\prod_{t=q}^{2q-1}t}.
\]
For
\[
q=2m,
\]
the numerator is odd, so
\[
\nu_2(A_{2m})-\nu_2(A_{2m-1})
=
-(2m-1).
\]
Pairing the ratios at \(2m-1\) and \(2m\) yields
\[
\nu_2(A_{2m})-\nu_2(A_{2m-2})
=
e-1-2s_2(m-1),
\]
where \(s_2(u)\) is the number of ones in the binary expansion of \(u\). Consequently
\[
\nu_2(A_{2m})
=
m(e-1)-2\sum_{u=0}^{m-1}s_2(u).
\]

Put
\[
k=e-1.
\]
For every
\[
1\le m\le2^k-1,
\]
the binary digit-sum estimate
\[
2\sum_{u=0}^{m-1}s_2(u)
\le
k(m-1)
\]
holds. It follows by induction on \(k\): below \(2^{k-1}\) apply the induction hypothesis, at \(m=2^{k-1}\) use
\[
2^{k-1}\ge k,
\]
and for
\[
m=2^{k-1}+r
\]
use
\[
\sum_{u=0}^{m-1}s_2(u)
=
(k-1)2^{k-2}+r+\sum_{u=0}^{r-1}s_2(u).
\]
Therefore
\[
\nu_2(A_{2m})\ge e-1.
\]
For odd corank,
\[
\nu_2(A_{2m-1})
=
\nu_2(A_{2m})+(2m-1)
>
e-1.
\]
Thus every proper symmetric determinantal degree is divisible by
\[
2^{e-1}.
\]

Sharpness already occurs at corank two:
\[
A_2
=
\frac{n(n-1)(n+1)}6.
\]
Since \(n=2^e\),
\[
\nu_2(A_2)=e-1.
\]
Hence
\[
G_n=2^{e-1}=\frac n2
\]
for every
\[
n=2^e,\qquad e\ge2.
\]

This completes the proof.

## Verification
The bundled checker evaluates the exact symmetric determinantal product formula for every
\[
2\le n\le120
\]
and every proper corank
\[
1\le q\le n-1.
\]
It computes each full rank-tower gcd and compares it with the theorem.

For every non-power-of-two \(n\) in that range, the checker also verifies the prime-primary witness
\[
q=p^{\nu_p(n)}
\]
for every prime divisor \(p\mid n\), using the rank-one Veronese degree only in the exceptional odd-prime-power branch.

Separately, for powers of two through
\[
n=256,
\]
it verifies the closed valuation formula
\[
\nu_2(A_{2m})
=
m(e-1)-2\sum_{u=0}^{m-1}s_2(u)
\]
and the neighboring odd-corank relation.

These computations are regression evidence only. The theorem for arbitrary \(n\) is established by the symbolic proof above.

## Relationship to prior work
The projective symmetric rank loci are classical determinantal varieties. The rank-one member is the quadratic Veronese variety, and the higher-rank members form its secant/rank stratification. Hosono and Takagi study the projective geometry and birational models of these symmetric determinantal loci.

The degree product used here is classical and is reproduced in work on the algebraic degree of semidefinite programming, where it is attributed to Harris and Tu.

Prior work and the inspected sources provide individual degree formulas and detailed geometry. Nearby recent work on the same degree sequence studies adjacent-rank curvature and asymptotic log-convexity versus log-concavity. The statement here is different: it determines the exact gcd of the complete proper rank tower for each fixed matrix size.

Targeted searches for gcd, common-divisor, parity, prime divisibility, and prime-adic formulations of symmetric determinantal degrees did not locate an equivalent whole-tower classification.

## Limitations
The theorem concerns projective degrees of complex symmetric determinantal loci in their standard embedding. It does not cover generic nonsymmetric or skew-symmetric matrix rank loci.

The proof identifies the full common divisor but does not give closed prime-adic formulas for every individual symmetric determinantal degree.

There remains a residual possibility that the same gcd consequence of the classical Harris--Tu product occurs in older, weakly indexed representation-theoretic or enumerative literature.

## References
S. Hosono and H. Takagi, *Geometry of symmetric determinantal loci*, arXiv:1508.01995, first submitted 9 August 2015.

J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, *Topology* 23 (1984), 71--84.

J. Nie, K. Ranestad, and B. Sturmfels, *The algebraic degree of semidefinite programming*, *Mathematical Programming* 122 (2010), 379--405.
