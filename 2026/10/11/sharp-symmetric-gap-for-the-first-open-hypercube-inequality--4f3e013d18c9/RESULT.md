# Sharp symmetric gap for the first open hypercube inequality
## Finding

Let \(v\in\{0,1\}^4\) and write \(|v|\) for its Hamming weight. Assign weights
\[
x_v=
\begin{cases}
a,& |v|\in\{0,4\},\\
b,& |v|\in\{1,3\},\\
c,& |v|=2,
\end{cases}
\qquad a,b,c\ge0,
\]
not all zero. This is exactly the three-parameter cone of weights invariant under every coordinate permutation and under vertex complementation
\[
v\longmapsto \mathbf 1-v.
\]

For a five-vertex subset \(U\subset\{0,1\}^4\), let
\[
\operatorname{Vol}(U)=4!\operatorname{vol}(\operatorname{conv}U)
\]
be its normalized four-dimensional simplex volume, and define
\[
P(x)=
\sum_{U\in\binom{\{0,1\}^4}{5}}
\operatorname{Vol}(U)\prod_{v\in U}x_v.
\]
Also put
\[
T=\sum_{v\in\{0,1\}^4}x_v
\]
and, for each of the eight facets \(F\) of the \(4\)-cube,
\[
S_F=\sum_{v\in F}x_v.
\]

Then the dimension-\(4\) Hypercube ratio satisfies the sharp estimate
\[
\boxed{
\frac{P(x)T^3}{\prod_F S_F}\le\frac{105}{128}.
}
\]
Equality holds exactly when
\[
\boxed{a=b=c>0.}
\]

In particular, the conjectured Hypercube inequality
\[
P(x)T^3\le\prod_F S_F
\]
is not merely valid on this symmetry cone: it has the sharp relative gap
\[
\boxed{
\prod_F S_F-P(x)T^3
\ge
\frac{23}{128}\prod_F S_F.
}
\]

This treats a natural three-parameter slice of the first open cube dimension \(d=4\), corresponding in the source to the conjectural Bézout-type inequality in dimension \(n=5\).

## Assumptions and scope

The Hypercube inequality is the polynomial formulation introduced by Averkov, von Dichter, and Soprunov. In cube dimension \(d\), it is
\[
\left(
\sum_{U\in\binom{\{0,1\}^d}{d+1}}
\operatorname{Vol}(U)\prod_{v\in U}x_v
\right)
\left(\sum_v x_v\right)^{d-1}
\le
\prod_{F}
\left(\sum_{v\in F}x_v\right),
\]
where the product is over the \(2d\) facets of the cube and
\[
\operatorname{Vol}(U)=d!\operatorname{vol}(\operatorname{conv}U).
\]

The source proves the inequality for \(d=3\) and states that \(d=4\) remains open. The result here concerns only the \(d=4\) cone fixed by coordinate permutations and complementation. It does not assert the inequality for arbitrary \(16\)-tuples of nonnegative vertex weights.

For the displayed symmetric weights, set
\[
S=a+4b+3c.
\]
There are two vertices in the \(a\)-class, eight in the \(b\)-class, and six in the \(c\)-class, so
\[
T=2a+8b+6c=2S.
\]
Each facet contains one vertex from the \(a\)-class, four from the \(b\)-class, and three from the \(c\)-class. Hence
\[
S_F=S
\]
for every facet \(F\), and therefore
\[
\prod_F S_F=S^8.
\]

Thus the sharp ratio claim is equivalent to
\[
\boxed{1024P\le105S^5.}
\]

## Proof

Exact enumeration of the \(5\)-vertex subsets of the \(4\)-cube gives
\[
\begin{aligned}
P={}&32a^2b^3+96a^2b^2c+96a^2bc^2+16a^2c^3\\
&+132ab^4+480ab^3c+624ab^2c^2+336abc^3+48ac^4\\
&+64b^5+396b^4c+576b^3c^2+368b^2c^3+96bc^4.
\end{aligned}
\]
The coefficients are sums of the exact normalized volumes
\[
\left|
\det
\begin{pmatrix}
v_0&1\\
\vdots&\vdots\\
v_4&1
\end{pmatrix}
\right|
\]
over all \(5\)-subsets with the corresponding class multiplicities.

Define the following homogeneous cubics:
\[
\begin{aligned}
A={}&58295b^2c+37269b^3+179836abc+69930ab^2\\
&+10710a^2c+12600a^2b,
\end{aligned}
\]
\[
\begin{aligned}
B={}&133209c^3+292940bc^2+357151b^2c+214635b^3\\
&+51915a^2c+56070a^3,
\end{aligned}
\]
and
\[
\begin{aligned}
C={}&19881c^3+404254bc^2+556128b^2c+296583b^3\\
&+104924abc+630a^3.
\end{aligned}
\]

A direct coefficient identity is
\[
\boxed{
6\left(105S^5-1024P\right)
=
(a-b)^2A+(b-c)^2B+(a-c)^2C.
}
\]
Every coefficient of \(A,B,C\) is strictly positive. Hence for \(a,b,c\ge0\),
\[
105S^5-1024P\ge0.
\]
This proves
\[
P\le\frac{105}{1024}S^5.
\]

The equality statement is also immediate from the certificate. For every nonzero triple
\[
(a,b,c)\in[0,\infty)^3,
\]
the cubics \(B\) and \(C\) are strictly positive because each contains positive multiples of
\[
a^3,\qquad b^3,\qquad c^3.
\]
Therefore equality in the certificate forces
\[
b=c
\]
from the \(B\)-term and
\[
a=c
\]
from the \(C\)-term. Thus
\[
a=b=c.
\]
Conversely, all three square factors vanish when \(a=b=c\), so equality indeed holds there.

Finally,
\[
\frac{P T^3}{\prod_F S_F}
=
\frac{P(2S)^3}{S^8}
=
\frac{8P}{S^5}
\le
8\cdot\frac{105}{1024}
=
\frac{105}{128}.
\]
When \(a=b=c>0\), equality holds. Hence the constant \(105/128\) is sharp on this symmetry cone.

Since
\[
1-\frac{105}{128}=\frac{23}{128},
\]
the stated sharp relative gap follows.

## Verification

The bundled checker reconstructs the polynomial \(P\) directly from the \(4\)-cube. It enumerates all
\[
\binom{16}{5}=4368
\]
five-vertex subsets, computes each normalized simplex volume by an exact integer determinant, groups the terms by the three weight classes, and recovers the fourteen displayed coefficients without floating-point arithmetic.

The checker then expands both sides of
\[
6\left(105S^5-1024P\right)
=
(a-b)^2A+(b-c)^2B+(a-c)^2C
\]
as exact integer coefficient dictionaries and verifies equality coefficient by coefficient. It separately checks the facet sums, the total weight, and the equality value
\[
\frac{P T^3}{\prod_F S_F}=\frac{105}{128}
\]
at \(a=b=c=1\).

The finite enumeration is exhaustive because the object being computed is exactly the finite coefficient polynomial attached to the \(16\) vertices of the \(4\)-cube. The all-parameter inequality for every real
\[
a,b,c\ge0
\]
then follows from the exact polynomial certificate; it is not inferred from sampling.

## Relationship to prior work

Averkov, von Dichter, and Soprunov introduce the Hypercube inequality as a reformulation of their conjectural partial-polymatroid inequality for projection volumes of zonoids. They prove the \(d=3\) case, including equality cases, and explicitly state that the next case \(d=4\) remains open. They emphasize that the unrestricted \(d=4\) polynomial has \(16\) variables, degree \(8\), and roughly \(400{,}000\) terms.

Their full text contains no Hamming-weight reduction and no coordinate-permutation-plus-complementation slice. The sharp constant \(105/128\) and the three-variable certificate above are not stated there.

The original full log-submodularity conjecture for zonoid volumes is a different statement. Recent work of Fradelizi, Hubard, Manui, Ndiaye, Wang, and Zvavitch and of Skorupinski shows that that stronger conjecture fails in dimensions at least four. Those counterexamples do not contradict the present result: the Hypercube inequality was proposed precisely as a different partial-submodularity relation after the failure of full log-submodularity.

A related published computation studies a one-parameter scale deformation of a four-dimensional zonotope counterexample to full log-submodularity. That result concerns a different inequality and a different parameter space; it neither implies nor is implied by the \(d=4\) Hypercube ratio computed here.

## Limitations

The unrestricted \(d=4\) Hypercube inequality remains open. The present theorem covers the natural three-parameter fixed cone
\[
x_v=x_{\pi(v)}=x_{\mathbf1-v}
\]
for coordinate permutations \(\pi\), but it does not cover arbitrary radial weights with independent values on all five Hamming shells, nor arbitrary complement-symmetric weights, nor arbitrary \(16\)-variable weights.

The sharp constant \(105/128\) is sharp only within the stated symmetry cone. No claim is made that it is a universal constant for a larger class.

The proof uses an exact finite determinant census to obtain the specialized coefficient polynomial. That census is not a substitute for the subsequent all-parameter certificate.

## References

1. Gennadiy Averkov, Katherina von Dichter, and Ivan Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v1, 14 August 2026.
2. Matthieu Fradelizi, Alfredo Hubard, Auttawich Manui, Cheikh Saliou Ndiaye, Shouda Wang, and Artem Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681v1, 13 August 2026.
3. Robert Skorupinski, *Zonoid volumes are not log-submodular*, arXiv:2608.07702v1, 7 August 2026.
4. Matthieu Fradelizi, Mokshay Madiman, Mathieu Meyer, and Artem Zvavitch, *On the volume of the Minkowski sum of zonoids*, Journal of Functional Analysis 286 (2024), 110247; arXiv:2206.02123.
