# Degree distributions reconstruct finite-field factors in product trace graphs

## Finding

Let \(q\) be a prime power, let \(k\ge2\), and let
\[
n_1,\ldots,n_k\ge2.
\]
For
\[
R=\prod_{i=1}^k M_{n_i}(\mathbf F_q),
\]
define the componentwise trace graph
\[
G=\Gamma_t(R)
\]
to have the nonzero tuples
\[
X=(A_1,\ldots,A_k)\in R\setminus\{0\}
\]
as vertices, with distinct \(X=(A_i)\) and \(Y=(B_i)\) adjacent exactly when
\[
\operatorname{tr}(A_iB_i)=0
\qquad\text{for every }i.
\]
This is the natural direct-product trace graph posed in the 2024 survey.

Put
\[
T=\sum_{i=1}^k n_i^2.
\]
If \(X\) has exactly \(s\) nonzero components, then
\[
\boxed{
\deg(X)\in\{q^{T-s}-2,\ q^{T-s}-1\}.
}
\]
Both values occur for every
\[
1\le s\le k.
\]
Hence the graph has exactly
\[
\boxed{2k}
\]
distinct degrees.

Let
\[
m_s^-
=
\#\{X:\deg(X)=q^{T-s}-2\},
\]
and
\[
m_s^+
=
\#\{X:\deg(X)=q^{T-s}-1\}.
\]
Then
\[
\boxed{
m_s^-+m_s^+
=
e_s\!\left(
q^{n_1^2}-1,\ldots,q^{n_k^2}-1
\right),
}
\]
where \(e_s\) denotes the \(s\)-th elementary symmetric polynomial.

The degree distribution therefore reconstructs the complete finite-field matrix-factor data. If
\[
v=|V(G)|,\qquad \delta=\delta(G),
\]
then
\[
v+1=q^T,
\qquad
\delta+2=q^{T-k},
\]
so
\[
\boxed{
q^k=\frac{v+1}{\delta+2}.
}
\]
Since the number of distinct degrees is \(2k\), the graph first recovers \(k\), and then the displayed ratio recovers \(q\).

The quantities
\[
E_s=m_s^-+m_s^+
\]
are graph invariants. Therefore the graph determines
\[
P(z)
=
z^k-E_1z^{k-1}+E_2z^{k-2}
-\cdots+(-1)^kE_k.
\]
Its roots are exactly
\[
q^{n_1^2}-1,\ldots,q^{n_k^2}-1.
\]
Hence the graph recovers the unordered multiset
\[
\boxed{\{n_1,\ldots,n_k\}}.
\]

Consequently, for prime powers \(q,r\), integers \(k,\ell\ge2\), and all matrix sizes at least two,
\[
\Gamma_t\!\left(\prod_{i=1}^kM_{n_i}(\mathbf F_q)\right)
\cong
\Gamma_t\!\left(\prod_{j=1}^{\ell}M_{m_j}(\mathbf F_r)\right)
\]
if and only if
\[
\boxed{
q=r,\qquad
k=\ell,\qquad
\{n_1,\ldots,n_k\}_{\mathrm{multi}}
=
\{m_1,\ldots,m_k\}_{\mathrm{multi}}.
}
\]

This settles the finite-field case of the survey's Problem 3 under the natural trace-graph range \(n_i\ge2\), and in particular settles its finite-field Problem 2.

## Assumptions and scope

The direct-product trace is interpreted componentwise. Thus adjacency in
\[
\prod_iM_{n_i}(\mathbf F_q)
\]
means simultaneous vanishing of all component traces.

Every matrix size is assumed to satisfy
\[
n_i\ge2.
\]
This is exactly the standard nontrivial range for trace graphs of matrix rings and guarantees the existence, in every factor, of both a nonzero self-orthogonal matrix and a non-self-orthogonal matrix.

The theorem uses a common finite field in all factors. It does not cover products over different finite fields, arbitrary integral domains, or factors of size one.

## Proof

For each factor
\[
M_{n_i}(\mathbf F_q),
\]
the pairing
\[
(A,B)\longmapsto\operatorname{tr}(AB)
\]
is nondegenerate. Indeed, if
\[
A=(a_{uv})\ne0
\]
and
\[
a_{uv}\ne0,
\]
then
\[
\operatorname{tr}(AE_{vu})=a_{uv}\ne0.
\]
Hence, for nonzero \(A\), the kernel of
\[
B\longmapsto\operatorname{tr}(AB)
\]
has exactly
\[
q^{n_i^2-1}
\]
elements. If \(A=0\), there is no constraint and all
\[
q^{n_i^2}
\]
matrices are allowed.

Let
\[
X=(A_1,\ldots,A_k)\ne0
\]
have support
\[
S=\{i:A_i\ne0\}
\]
of size
\[
|S|=s.
\]
The number of tuples
\[
Y=(B_1,\ldots,B_k)
\]
satisfying
\[
\operatorname{tr}(A_iB_i)=0
\]
for every \(i\) is therefore
\[
\prod_{i\in S}q^{n_i^2-1}
\prod_{i\notin S}q^{n_i^2}
=
q^{T-s}.
\]

This count includes the zero tuple, which is not a vertex, so one always subtracts one. It also includes \(X\) itself exactly when
\[
\operatorname{tr}(A_i^2)=0
\qquad\text{for every }i\in S.
\]
Because the graph is simple, one subtracts \(X\) in that case as well. Therefore
\[
\deg(X)=q^{T-s}-1
\]
when \(X\) is not self-orthogonal, and
\[
\deg(X)=q^{T-s}-2
\]
when it is self-orthogonal.

Both values occur for every support set \(S\). Since every
\[
n_i\ge2,
\]
the matrix unit
\[
E_{12}
\]
is nonzero and satisfies
\[
\operatorname{tr}(E_{12}^2)=0,
\]
while
\[
E_{11}
\]
satisfies
\[
\operatorname{tr}(E_{11}^2)=1.
\]
Putting \(E_{12}\) in every supported factor gives a self-orthogonal vertex. Replacing one supported component by \(E_{11}\) gives a non-self-orthogonal vertex with the same support.

The two degree values belonging to different support sizes are distinct. If the support size increases from \(s\) to \(s+1\), then the larger degree in the latter stratum is
\[
q^{T-s-1}-1,
\]
while the smaller degree in the former is
\[
q^{T-s}-2.
\]
Their difference is
\[
(q-1)q^{T-s-1}-1>0.
\]
Thus there are exactly \(2k\) degree values, arranged in \(k\) consecutive pairs.

Now count vertices only by support. For a fixed support
\[
S\subseteq\{1,\ldots,k\},
\]
the number of vertices with exactly that support is
\[
\prod_{i\in S}(q^{n_i^2}-1).
\]
Summing over all supports of size \(s\) gives
\[
m_s^-+m_s^+
=
\sum_{|S|=s}
\prod_{i\in S}(q^{n_i^2}-1)
=
e_s(q^{n_1^2}-1,\ldots,q^{n_k^2}-1).
\]

The total number of vertices is
\[
v=q^T-1.
\]
The minimum degree occurs at support size \(k\) in the self-orthogonal stratum, so
\[
\delta=q^{T-k}-2.
\]
Consequently
\[
\frac{v+1}{\delta+2}
=
q^k.
\]
The graph already determines
\[
k=\frac12|\{\text{distinct degrees}\}|,
\]
so it determines the unique positive integer \(q\) whose \(k\)-th power is this ratio.

Finally, the graph determines each
\[
E_s=m_s^-+m_s^+.
\]
The polynomial
\[
P(z)
=
z^k-E_1z^{k-1}+E_2z^{k-2}
-\cdots+(-1)^kE_k
\]
therefore is graph-invariant, and by Viète's identities its root multiset is
\[
\{q^{n_i^2}-1:1\le i\le k\}.
\]
Since \(q\) is already known, every root determines
\[
n_i^2
\]
uniquely from
\[
q^{n_i^2}=P_i+1,
\]
and then determines \(n_i\).

Thus graph isomorphism forces equality of the field order and the unordered matrix-size multiset. Conversely, equality of these data gives, after permuting factors, a ring isomorphism preserving every component trace and therefore a trace-graph isomorphism.

## Verification

The included replay independently checks the linear-algebra and reconstruction steps over
\[
\mathbf F_2,\ \mathbf F_3,\ \mathbf F_4,\ \mathbf F_5.
\]

For every \(2\times2\) matrix over those fields, it enumerates the full trace-functional kernel and verifies that every nonzero matrix has exactly
\[
q^3
\]
orthogonal matrices.

It also directly constructs the complete product trace graph for
\[
M_2(\mathbf F_2)\times M_2(\mathbf F_2),
\]
enumerates every adjacency, and verifies the two support strata and all four degree values.

For larger test families, the replay independently enumerates self-orthogonality types inside the component matrix spaces and builds the exact degree multiplicities from the defining trace equations. It checks the reconstruction algorithm for
\[
(q;n_1,\ldots,n_k)
=
(2;2,3),\quad
(3;2,2,3),\quad
(4;2,3,3),\quad
(5;2,2,3,3).
\]
In every case it recovers \(q\), \(k\), and the complete unordered matrix-size multiset from only graph order and the degree distribution.

The \(\mathbf F_4\) arithmetic uses
\[
\mathbf F_4=\mathbf F_2[t]/(t^2+t+1).
\]

The replay returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.

## Relationship to prior work

The 2024 survey *Graphs from matrices - a survey* explicitly poses two direct-product problems. Problem 2 asks for the trace graph of
\[
M_{n_1}(R)\times M_{n_2}(R)
\]
when the matrix sizes differ. Problem 3 asks for the trace graph of
\[
M_{n_1}(D)\times\cdots\times M_{n_k}(D)
\]
over an integral domain.

The present theorem solves the finite-field part of Problem 3 when every
\[
n_i\ge2,
\]
and therefore also solves the finite-field instance of Problem 2. The answer is stronger than a local degree computation: the entire matrix-factor multiset is reconstructed from the graph degree distribution.

The same survey reproduces the earlier degree formula for one matrix ring over a finite commutative ring and the earlier isomorphism theorem saying that an isomorphism
\[
\Gamma_t(M_{n_1}(R_1))
\cong
\Gamma_t(M_{n_2}(R_2))
\]
forces equality of the ring cardinalities and matrix sizes. Those results do not state the present direct-product classification. In particular, a product with unequal matrix sizes is not of the form
\[
M_n(R)
\]
for a single common \(n\), so the survey treats it separately as an open problem.

Targeted searches using direct-product, matrix-size, finite-field, trace-graph, degree-distribution, and isomorphism terminology did not locate the displayed elementary-symmetric reconstruction theorem. Searches restricted to work after the 2024 survey likewise returned the survey itself rather than a later solution.

## Limitations

All simple factors use the same finite field. The different-field case has a different support-degree fingerprint and is not asserted here.

The theorem assumes
\[
n_i\ge2.
\]
If a factor has size one, then a nonzero scalar cannot satisfy
\[
\operatorname{tr}(A^2)=0,
\]
so one of the two degree values can disappear on support sets involving that factor. The degree-pair count therefore needs modification.

The theorem handles finite fields, not arbitrary integral domains from Problem 3.

The older original trace-graph articles were not available in full through the public full-text routes checked. Their exact relevant statements were inspected as reproduced in full in the 2024 survey. This leaves a residual bibliographic risk that an older inaccessible article contains an unstated equivalent consequence.

Failed searches do not prove novelty.

## References

1. T. Tamizh Chelvam, “Graphs from matrices - a survey,” *AKCE International Journal of Graphs and Combinatorics* 21 (2024), 198–208, published online 2 April 2024, DOI 10.1080/09728600.2024.2332780.
2. F. A. A. Almahdi, K. Louartiti, and M. Tamekkante, “The trace graph of the matrix ring over a finite commutative ring,” *Acta Mathematica Hungarica* 156 (2018), 132–144, DOI 10.1007/s10474-018-0815-x.
3. T. Tamizh Chelvam and M. Sivagami, “On trace graph of matrices over fields,” *Beiträge zur Algebra und Geometrie* 63 (2022), 217–231, DOI 10.1007/s13366-021-00561-8.
