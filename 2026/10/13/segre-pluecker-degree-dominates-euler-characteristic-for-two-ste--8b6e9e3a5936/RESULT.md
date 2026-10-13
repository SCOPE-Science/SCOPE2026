# Segre–Pluecker degree dominates Euler characteristic for two-step line flags
## Finding
For integers
\[
n\ge3,
\qquad
2\le k\le n-1,
\]
let
\[
F(1,k;n)
=
\{(L,U):L\subset U\subset\mathbb C^n,\ \dim L=1,\ \dim U=k\}.
\]
Embed this two-step flag variety into
\[
\mathbb P^{n-1}\times\operatorname{Gr}(k,n)
\]
by remembering \(L\) and \(U\), and then use the Segre embedding after the Pluecker embedding of the Grassmannian. Equivalently, the polarization is the homogeneous line bundle
\[
\mathcal O(1,1).
\]

Put
\[
D_{k,n}=\deg_{\mathcal O(1,1)}F(1,k;n),
\qquad
E_{k,n}=\chi_{\mathrm{top}}(F(1,k;n)).
\]
Then
\[
\boxed{D_{k,n}\ge E_{k,n}},
\]
and equality holds if and only if
\[
\boxed{(n,k)=(3,2)}.
\]
Thus every two-step line flag except the complete flag variety of \(\mathbb C^3\) has strictly larger Segre–Pluecker degree than Euler characteristic.

Writing
\[
a=k-1,
\qquad
b=n-k,
\qquad
N=ab+a+b,
\]
the exact formulas are
\[
\boxed{
D_{k,n}
=
\frac{N!\,2^b\prod_{r=0}^{a-1}r!}
{(a+b)!\prod_{r=0}^{a-1}(b+r)!}
}
\]
and
\[
\boxed{
E_{k,n}
=
\frac{(a+b+1)!}{a!\,b!}.
}
\]

## Assumptions and scope
The base field is \(\mathbb C\). The variety is the partial flag variety of block type
\[
(1,k-1,n-k).
\]
Its complex dimension is
\[
N=(k-1)+(n-k)+(k-1)(n-k)=ab+a+b.
\]

The projective degree is taken in the natural Segre–Pluecker embedding. On the full flag variety, the two factors correspond to the fundamental weights \(\omega_1\) and \(\omega_k\); their tensor product corresponds to
\[
\lambda=\omega_1+\omega_k.
\]
This line bundle descends to \(F(1,k;n)\) and is very ample.

The Schubert cells of a partial flag variety are affine spaces indexed by the quotient of the Weyl group by the parabolic Weyl group. Hence
\[
E_{k,n}
=
\frac{n!}{1!\,(k-1)!\,(n-k)!}.
\]

## Proof
We first compute the degree from the Weyl dimension formula.

Represent the dominant weight
\[
\lambda=\omega_1+\omega_k
\]
for \(\operatorname{GL}_n\) by
\[
(2,\underbrace{1,\ldots,1}_{k-1},\underbrace{0,\ldots,0}_{n-k}).
\]
For a positive root
\[
e_i-e_j,
\qquad
i<j,
\]
the leading coefficient in the Weyl dimension polynomial is
\[
\frac{\lambda_i-\lambda_j}{j-i}
\]
when \(\lambda_i>\lambda_j\). There are exactly
\[
N=ab+a+b
\]
such roots.

The nonzero root contributions split into three groups:
\[
i=1,\quad 2\le j\le k;
\]
\[
i=1,\quad k+1\le j\le n;
\]
and
\[
2\le i\le k,\quad k+1\le j\le n.
\]
Their product is
\[
\frac{2^b}{(n-1)!}
\prod_{r=0}^{a-1}\frac{r!}{(b+r)!}.
\]
Multiplying by \(N!\), the leading-coefficient normalization for projective degree, gives
\[
D(a,b)
=
\frac{N!\,2^b\prod_{r=0}^{a-1}r!}
{(a+b)!\prod_{r=0}^{a-1}(b+r)!}.
\]

The Schubert-cell decomposition gives
\[
E(a,b)
=
\frac{(a+b+1)!}{a!\,b!}.
\]
Define
\[
R(a,b)=\frac{D(a,b)}{E(a,b)}.
\]
At
\[
(a,b)=(1,1)
\]
one gets
\[
D(1,1)=E(1,1)=6.
\]

We now prove that \(R\) increases strictly in each coordinate throughout
\[
a,b\ge1.
\]

Since
\[
N=ab+a+b,
\]
direct cancellation of the factorial formulas yields
\[
\frac{R(a+1,b)}{R(a,b)}
=
\frac{(a+1)!}{(a+b+2)!}
\prod_{j=1}^{b+1}(N+j).
\]
Also,
\[
\frac{(a+b+2)!}{(a+1)!}
=
\prod_{j=1}^{b+1}(a+1+j).
\]
For every \(j\),
\[
N+j-(a+1+j)
=
b(a+1)-1>0.
\]
Therefore
\[
R(a+1,b)>R(a,b).
\]

Similarly,
\[
\frac{R(a,b+1)}{R(a,b)}
=
\frac{2(b+1)!}{(a+b+2)!}
\prod_{j=1}^{a+1}(N+j),
\]
whereas
\[
\frac{(a+b+2)!}{(b+1)!}
=
\prod_{j=1}^{a+1}(b+1+j).
\]
For every \(j\),
\[
N+j-(b+1+j)
=
a(b+1)-1>0.
\]
Hence
\[
R(a,b+1)>R(a,b).
\]

Every pair
\[
(a,b)\in\mathbb Z_{\ge1}^2
\]
other than \((1,1)\) is reached from \((1,1)\) by at least one such strict increase. Consequently
\[
R(a,b)>1
\]
away from \((1,1)\), proving the claimed classification.

## Verification
The bundled checker independently evaluates the degree in two ways:

1. from the closed factorial formula above;
2. directly from the positive-root product in the Weyl dimension formula.

It checks agreement for every
\[
3\le n\le80,
\qquad
2\le k\le n-1,
\]
and verifies the degree-versus-Euler classification throughout that range.

It also checks the two exact coordinate-ratio identities for
\[
1\le a,b\le60
\]
using rational arithmetic.

These finite computations are regression evidence only. The inequality for all parameters is proved by the symbolic ratio argument.

## Relationship to prior work
Brion's lectures give a self-contained algebraic-geometric treatment of flag varieties, their Schubert-cell decompositions, their realization as partial flag varieties, and the homogeneous line bundles associated with fundamental weights. In particular, the Pluecker line bundle for a Grassmannian factor is the homogeneous line bundle attached to the corresponding fundamental weight.

The Weyl dimension formula gives the Hilbert polynomial of a homogeneous embedding, so its leading coefficient gives the projective degree. Specializing that standard formula to the weight
\[
\omega_1+\omega_k
\]
produces the closed degree formula above.

The comparison with Euler characteristic is a different question: it asks whether the enumerative complexity of a generic complementary Segre–Pluecker section exceeds the number of Schubert cells of the same variety. Targeted searches for this comparison, for the exact \(F(1,k;n)\) degree-versus-Euler inequality, and for equivalent cell-count formulations did not locate the monotone two-parameter quotient law or the unique equality case.

## Limitations
The result treats only flags
\[
L\subset U
\]
with the first step one-dimensional, and only the natural polarization \(\mathcal O(1,1)\).

Other two-step flag types
\[
F(p,q;n)
\]
have different dominant weights and a more complicated parameter geometry; the present monotonicity proof does not automatically extend to them.

The inequality is a short consequence of standard homogeneous-space formulas once the two invariants are placed in the same two-parameter coordinates. An older or unindexed Schubert-calculus source could contain the same comparison.

## References
Michel Brion, *Lectures on the geometry of flag varieties*, arXiv:math/0410240, first submitted 9 October 2004; in *Topics in Cohomological Studies of Algebraic Varieties*, Trends in Mathematics, Birkhauser, 2005, 33--85.
