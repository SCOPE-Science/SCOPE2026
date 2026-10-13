# Euler characteristic stabilizes at rank two in symmetric determinantal towers
## Finding
Let
\[
S_{n,r}\subset\mathbb P(\operatorname{Sym}^2\mathbb C^n)
\]
be the projective variety of nonzero complex symmetric \(n\times n\) matrices of rank at most
\[
r,
\qquad
n\ge2,
\qquad
1\le r\le n.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}(S_{n,1})=n
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(S_{n,r})=\binom{n+1}{2}
\qquad(2\le r\le n).
}
\]

Thus allowing rank two already raises the Euler characteristic to that of the full ambient projective space, and every higher cumulative rank locus has exactly the same Euler characteristic.

Equivalently, define the exact-rank strata by
\[
S_{n,r}^{=r}=S_{n,r}\setminus S_{n,r-1},
\qquad
S_{n,0}=\varnothing.
\]
Then
\[
\boxed{
\chi_{\mathrm{top}}(S_{n,1}^{=1})=n,
\qquad
\chi_{\mathrm{top}}(S_{n,2}^{=2})=\binom n2,
\qquad
\chi_{\mathrm{top}}(S_{n,r}^{=r})=0
\quad(3\le r\le n).
}
\]

In particular, all Euler-characteristic mass of the projective symmetric rank stratification is concentrated in ranks one and two.

## Assumptions and scope
The base field is \(\mathbb C\). The varieties are projectivized, so the zero matrix is absent.

The topological Euler characteristic is the ordinary Euler characteristic of the associated complex projective variety. For the locally closed exact-rank strata, the same integer is computed using additivity of Euler characteristic for complex algebraic constructible decompositions.

No smoothness is assumed. The loci \(S_{n,r}\) are singular for most intermediate ranks.

## Proof
Choose positive integers
\[
a_i=2^i,
\qquad
0\le i\le n-1.
\]
Let \(\mathbb C^*\) act on \(\mathbb C^n\) through
\[
\lambda(t)=\operatorname{diag}(t^{a_0},\ldots,t^{a_{n-1}}),
\]
and on symmetric matrices by congruence:
\[
A\longmapsto \lambda(t)A\lambda(t).
\]
This action preserves matrix rank and therefore preserves every \(S_{n,r}\).

The coordinate of a symmetric matrix indexed by
\[
0\le i\le j\le n-1
\]
has weight
\[
a_i+a_j.
\]
All these weights are distinct. Indeed, if \(i<j\), the binary expansion of \(2^i+2^j\) has two nonzero bits, whereas \(2^i+2^i=2^{i+1}\) has one; uniqueness of binary expansion then distinguishes every unordered pair with repetition.

Hence the fixed points of the induced action on
\[
\mathbb P(\operatorname{Sym}^2\mathbb C^n)
\]
are exactly the coordinate points.

There are two types. The \(n\) diagonal coordinate points
\[
[E_{ii}]
\]
have rank one. The
\[
\binom n2
\]
off-diagonal coordinate points
\[
[E_{ij}+E_{ji}],
\qquad
i<j,
\]
have rank two.

Therefore
\[
(S_{n,1})^{\mathbb C^*}
\]
consists of exactly \(n\) points, while for every
\[
r\ge2
\]
the fixed locus
\[
(S_{n,r})^{\mathbb C^*}
\]
consists of all
\[
n+\binom n2=\binom{n+1}{2}
\]
coordinate points.

For a complex projective variety with an algebraic \(\mathbb C^*\)-action, Euler characteristic localizes to the fixed locus:
\[
\chi_{\mathrm{top}}(X)
=
\chi_{\mathrm{top}}(X^{\mathbb C^*}).
\]
This standard fixed-point identity does not require smoothness. Applying it gives
\[
\chi_{\mathrm{top}}(S_{n,1})=n
\]
and
\[
\chi_{\mathrm{top}}(S_{n,r})=\binom{n+1}{2}
\qquad(r\ge2).
\]

Finally, Euler characteristic is additive on the constructible decomposition
\[
S_{n,r}
=
S_{n,r-1}\sqcup S_{n,r}^{=r}.
\]
Thus
\[
\chi_{\mathrm{top}}(S_{n,2}^{=2})
=
\binom{n+1}{2}-n
=
\binom n2,
\]
and for every
\[
r\ge3
\]
one has
\[
\chi_{\mathrm{top}}(S_{n,r}^{=r})
=
\binom{n+1}{2}-\binom{n+1}{2}
=
0.
\]
This proves the result.

## Verification
The bundled checker constructs the coordinate weights
\[
2^i+2^j,
\qquad
0\le i\le j<n,
\]
and verifies that they are pairwise distinct for every tested
\[
2\le n\le100.
\]

It independently counts the rank-one diagonal fixed points and rank-two off-diagonal fixed points, reconstructs the cumulative Euler values, and verifies the exact-rank differences.

These finite checks are regression evidence only. The theorem for all \(n\) and \(r\) follows from binary uniqueness, rank preservation, Euler fixed-point localization, and additivity.

## Relationship to prior work
Ilic and Landsberg study the same projective symmetric determinantal loci
\[
X_r\subset\mathbb P(S^2V^*)
\]
and develop their geometry through symmetric degeneracy methods. Hosono and Takagi likewise use the rank-bounded symmetric determinantal varieties as central projective models.

General Euler-characteristic formulas for degeneracy loci are available for sufficiently general bundle morphisms. That framework does not directly subsume the present argument because the universal symmetric matrix is constrained to the symmetric subspace of all homomorphisms.

The present statement isolates a particularly simple global topological phenomenon: the cumulative Euler characteristic stabilizes immediately at rank two, so every exact-rank stratum of rank at least three has Euler characteristic zero. Targeted searches using symmetric determinantal, rank-stratum, Euler-characteristic, and fixed-point formulations did not locate this complete stabilization statement in the inspected sources.

## Limitations
The theorem concerns symmetric matrices. Generic rectangular determinantal varieties and skew-symmetric Pfaffian loci have different coordinate-rank behavior.

Only Euler characteristic is determined. Vanishing of the Euler characteristic of an exact-rank stratum does not imply vanishing of its individual cohomology groups.

The proof is short once a generic diagonal one-parameter action is chosen, so an older or unindexed source may contain the same observation.

## References
Bo Ilic and J. M. Landsberg, *On symmetric degeneracy loci, spaces of symmetric matrices of constant rank and dual varieties*, arXiv:alg-geom/9611025, first submitted 20 November 1996; *Mathematische Annalen* 314 (1999), 159--174.

Shinobu Hosono and Hiromichi Takagi, *Geometry of symmetric determinantal loci*, arXiv:1508.01995, first submitted 9 August 2015.
