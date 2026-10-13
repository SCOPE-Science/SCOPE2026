# A one-third law for maximal dual degree in the rational-normal secant tower
## Finding
Let
\[
C_d=v_d(\mathbb P^1)\subset\mathbb P^d,
\qquad
d\ge2,
\]
be the rational normal curve. For
\[
1\le k\le\left\lfloor\frac d2\right\rfloor,
\]
let
\[
\sigma_k(C_d)
\]
denote the \(k\)-point secant variety, so its expected and actual dimension is
\[
2k-1.
\]

Define
\[
A_{d,k}
=
\deg\bigl(\sigma_k(C_d)^\vee\bigr).
\]
Then
\[
\boxed{
A_{d,k}
=
2^k\binom{d-k}{k}
}.
\]

For each fixed \(d\), this degree sequence is strictly unimodal. Its unique maximum occurs at
\[
\boxed{
k_{\max}(d)
=
\left\lfloor\frac{d+1}{3}\right\rfloor
}.
\]
Equivalently,
\[
\max_k A_{d,k}
=
2^{m}\binom{d-m}{m},
\qquad
m=\left\lfloor\frac{d+1}{3}\right\rfloor.
\]

In particular,
\[
\frac{k_{\max}(d)}d\longrightarrow\frac13,
\]
and the dimension of the maximizing secant variety satisfies
\[
\frac{2k_{\max}(d)-1}{d}\longrightarrow\frac23.
\]

Thus the tangent-hyperplane complexity of the rational-normal secant tower has an exact one-third rank law.

## Assumptions and scope
The base field is \(\mathbb C\). The \(k\)-point secant variety is the Zariski closure of the union of projective \((k-1)\)-planes spanned by \(k\) points of \(C_d\).

Only proper secant varieties are included. For a rational normal curve, this is exactly
\[
1\le k\le\left\lfloor\frac d2\right\rfloor.
\]

The projective dual is taken in the dual projective space. Its degree is the ordinary projective degree of that dual variety.

## Proof
Lee and Sturmfels identify the \(k\)-point secant variety of the rational normal curve with the projective dual of the multiple-root locus
\[
\Delta_{\{1^{d-2k},2^k\}}.
\]
By biduality,
\[
\sigma_k(C_d)^\vee
=
\Delta_{\{1^{d-2k},2^k\}}.
\]

Hilbert's degree formula for a multiple-root locus indexed by a partition
\[
\lambda=(\lambda_1,\ldots,\lambda_\ell)
\]
is
\[
\deg(\Delta_\lambda)
=
\frac{\ell!}{\prod_j m_j!}
\prod_{i=1}^{\ell}\lambda_i,
\]
where \(m_j\) is the multiplicity of the part \(j\).

For
\[
\lambda=\{1^{d-2k},2^k\},
\]
the partition has length
\[
\ell=d-k,
\]
with
\[
m_1=d-2k,
\qquad
m_2=k.
\]
Hence
\[
A_{d,k}
=
\frac{(d-k)!}{(d-2k)!\,k!}\,2^k
=
2^k\binom{d-k}{k}.
\]

To locate the maximum, compare adjacent terms:
\[
\frac{A_{d,k+1}}{A_{d,k}}
=
\frac{2(d-2k)(d-2k-1)}
{(k+1)(d-k)}.
\]
The sign of this ratio minus \(1\) is the sign of
\[
F_d(k)
=
2d^2-9dk-3d+9k^2+5k.
\]
Along the comparison range,
\[
F_d(k+1)-F_d(k)
=
18k+14-9d<0.
\]
Thus the adjacent ratio can cross \(1\) at most once.

Put
\[
m=\left\lfloor\frac{d+1}{3}\right\rfloor.
\]
We verify that the crossing occurs exactly between \(m-1\) and \(m\).

If
\[
d=3q,
\]
then
\[
m=q,
\qquad
F_d(m-1)=5q+4>0,
\qquad
F_d(m)=-4q<0.
\]

If
\[
d=3q+1,
\]
then
\[
m=q,
\qquad
F_d(m-1)=4(2q+3)>0,
\qquad
F_d(m)=-(q+1)<0.
\]

If
\[
d=3q+2,
\]
then
\[
m=q+1,
\qquad
F_d(m-1)=2(q+1)>0,
\qquad
F_d(m)=-(7q+2)<0.
\]

For the small endpoints where one of these adjacent comparisons does not occur, the sequence contains only its unique admissible first term. Therefore
\[
A_{d,1}<\cdots<A_{d,m}
\]
and
\[
A_{d,m}>A_{d,m+1}>\cdots
\]
whenever the displayed terms exist. This proves strict unimodality and the unique maximizing index.

## Verification
The bundled checker independently reconstructs each dual degree from Hilbert's partition formula and compares it with
\[
2^k\binom{d-k}{k}
\]
for every
\[
2\le d\le1000
\]
and every proper secant order.

It verifies the adjacent-ratio identity, strict unimodality, and the exact maximizing index
\[
\left\lfloor\frac{d+1}{3}\right\rfloor.
\]

These finite computations are regression evidence only. The theorem for every \(d\) follows from the symbolic adjacent-ratio argument above.

## Relationship to prior work
Lee and Sturmfels prove the duality between rational-normal secant varieties and the multiple-root loci with \(k\) double roots. Their paper also recalls Hilbert's general degree formula for multiple-root loci. Raicu's work records the classical determinantal description of rational-normal secant varieties and places this secant tower in the standard algebraic-geometric catalecticant framework.

The closest arithmetic result located for the same secant tower concerns parity of the primal secant degrees, not the projective-dual degrees. Classical combinatorial literature also studies the unweighted binomial sequence
\[
\binom{d-k}{k},
\]
whose mode follows a different law. The extra factor
\[
2^k
\]
coming from the double-root locus shifts the dual-degree maximum to the exact one-third index above.

Targeted searches for the weighted coefficient sequence, for dual-degree maxima of rational-normal secants, and for coincident-root formulations did not locate this strict-unimodality theorem or its maximizing index.

## Limitations
The theorem concerns ordinary projective-dual degree only. It does not classify the full polar or Euclidean-distance degree profiles of the secant varieties.

The argument uses the special duality of rational-normal secants with the double-root loci
\[
\Delta_{\{1^{d-2k},2^k\}}.
\]
It does not automatically extend to higher-dimensional Veronese secant varieties.

The weighted binomial sequence is elementary once the geometric dual-degree formula is known. An unindexed combinatorics source could contain the same mode calculation without the secant-variety interpretation.

## References
Claudiu Raicu, *3x3 Minors of Catalecticants*, arXiv:1011.1564, first submitted 6 November 2010; *Mathematical Research Letters* 20 (2013), 745--756, DOI 10.4310/MRL.2013.v20.n4.a10.

Hwangrae Lee and Bernd Sturmfels, *Duality of Multiple Root Loci*, arXiv:1508.00202, first submitted 2 August 2015; *Journal of Algebra* 446 (2016), 499--526.
