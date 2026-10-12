# Complete symmetry-jump locus in Smith’s quartic del Pezzo family
## Finding
For \(a\in\mathbb C\setminus\{0,\pm1\}\), consider the quartic del Pezzo surface
\[
X_a:\quad \sum_{j=0}^4u_j^2=0,\qquad u_0^2+a u_1^2-u_2^2-a u_3^2=0.
\]
This is the one-parameter family in Smith’s Example 5.1. Its full automorphism group is
\[
\operatorname{Aut}(X_a)\cong C_2^4\rtimes H_a,
\]
with the following exact parameter stratification:
\[
H_a\cong
\begin{cases}
D_5,&(a^2-4a-1)(a^2+4a-1)=0,\\
S_3,&(a^2+3)(3a^2+1)=0,\\
C_4,&a^2+1=0,\\
C_2,&\text{otherwise.}
\end{cases}
\]
Thus the \(D_5\) parameters are exactly \(\pm(2+\sqrt5),\pm(2-\sqrt5)\), the \(S_3\) parameters are exactly \(\pm i\sqrt3,\pm i/\sqrt3\), and the \(C_4\) parameters are exactly \(\pm i\). In particular, one diagonal family that Smith presents as having generic quotient symmetry \(C_2\) already contains representatives of all four quotient stabilizer types \(C_2,C_4,S_3,D_5\).

## Assumptions and scope
The ground field is \(\mathbb C\), and \(a\ne0,\pm1\), exactly the smooth parameter range of the displayed family. The claim concerns the full biregular automorphism group of the abstract quartic del Pezzo surface, equivalently its automorphism group in the anticanonical embedding.

For an intersection of two diagonal quadrics, the five singular quadrics in the pencil determine five points on the pencil parameter line. For the displayed equations they are
\[
S_a=\{0,1,-1,a,-a\}\subset\mathbb P^1.
\]
Smith’s Proposition 2.4 identifies the geometric automorphism group with \(C_2^4\rtimes H_a\), where \(H_a\) is the projective stabilizer of this five-point set. Hence the problem reduces exactly to determining \(\operatorname{Stab}_{\operatorname{PGL}_2}(S_a)\).

## Proof
The involution \(x\mapsto-x\) preserves \(S_a\) for every admissible \(a\), so \(|H_a|\ge2\). To determine when additional projective symmetries occur, use the cross-ratio convention
\[
R(p,q;r,s)=\frac{(p-r)(q-s)}{(p-s)(q-r)}.
\]
For the ordered five-tuple \((0,1,-1,a,-a)\), two independent base values are
\[
R(0,1;-1,a)=\frac{a-1}{2a},\qquad
R(0,1;-1,-a)=\frac{a+1}{2a}.
\]
A permutation \(\sigma\in S_5\) is induced by a Möbius transformation of \(S_a\) if and only if these two cross-ratios equal the corresponding two cross-ratios after applying \(\sigma\). This criterion is sufficient because a projective transformation of \(\mathbb P^1\) is uniquely determined by the images of three distinct points.

There are only \(120\) permutations, so this is an exact finite classification. Clearing denominators in the two cross-ratio equations and taking their polynomial gcd in \(\mathbb C[a]\), while discarding the excluded collision factors \(a\), \(a-1\), and \(a+1\), gives the complete census
\[
\begin{array}{c|c|c}
\text{parameter factor}&\text{additional permutations}&|H_a|\\ \hline
a^2+1&2&4\\
a^2+3&4&6\\
3a^2+1&4&6\\
a^2-4a-1&8&10\\
a^2+4a-1&8&10.
\end{array}
\]
For every other admissible \(a\), only the identity and \(x\mapsto-x\) remain, so \(|H_a|=2\). The five displayed factors are pairwise disjoint on the admissible parameter line, so no further order increase occurs.

It remains only to identify the abstract groups. A finite cyclic subgroup of \(\operatorname{PGL}_2(\mathbb C)\) has two global fixed points and every other orbit has the full cyclic order. Therefore neither a cyclic group of order \(6\) nor one of order \(10\) can preserve a five-point set. Hence the order-six and order-ten stabilizers are \(S_3\) and \(D_5\), respectively. An order-four stabilizer cannot be the Klein four group: a noncyclic finite subgroup of \(\operatorname{PGL}_2\) has no global fixed point, and the point-orbits of a Klein four group have even cardinality, so it cannot preserve a set of cardinality five. Thus the order-four case is \(C_4\). The order-two case is \(C_2\). Combining this with Smith’s \(C_2^4\)-kernel proves the stated full automorphism groups.

Solving the five quadratic factors gives exactly the explicit parameter sets in the finding.

## Verification
The accompanying `verify.py` performs the full \(120\)-permutation cross-ratio enumeration symbolically over \(\mathbb Q(a)\). It verifies that the only noncollision exceptional factors are
\[
a^2+1,\quad a^2+3,\quad 3a^2+1,\quad a^2-4a-1,\quad a^2+4a-1,
\]
and reproduces stabilizer orders \(4,6,6,10,10\), with generic order \(2\). A fresh extraction of the packaged verifier was replayed successfully.

The computation is exhaustive rather than experimental: every permutation of the five marked pencil points is tested by exact polynomial identities. No numerical root search is used.

## Relationship to prior work
Smith proves the structural reduction \(\operatorname{Aut}(X)\cong C_2^4\rtimes H\) and, in Example 5.1, gives the displayed one-parameter family with generic automorphism group \(C_2^4\rtimes C_2\). He also singles out the \(a=i\) member with quotient \(C_4\), then gives a separate \(S_3\) model in the same example and a separate \(D_5\) model in Example 5.2. The paper does not state the complete exceptional parameter locus inside the displayed \(X_a\) family.

Dolgachev and Martin’s classification table records the possible complex quartic-del-Pezzo symmetry strata, including the \(C_2\), \(C_4\), \(S_3\), and dihedral cases. That broader classification does not identify their pullback to Smith’s coordinate \(a\). The result here is precisely that missing pullback: it determines every jump point of the source-highlighted parameter line and shows that the separate higher-symmetry types already occur within it.

## Limitations
The statement is only over \(\mathbb C\). Over a nonclosed characteristic-zero field, Galois descent changes which geometric automorphisms are defined over the base field, and the classification above should not be read as a rationality or descent statement.

The originality claim is limited to the exact symmetry-jump locus of this explicit parameter family and its complete stabilizer stratification. It does not claim a new classification of abstract automorphism groups of all quartic del Pezzo surfaces; that classification is classical and is explicitly used as prior work.

## References
1. Jonathan M. Smith, *Automorphisms of quartic del Pezzo surfaces in characteristic zero*, arXiv:2308.07904v1, 2023. See Proposition 2.4 and Examples 5.1–5.2.
2. Igor Dolgachev and Gebhard Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170v1; Journal of the London Mathematical Society 109 (2024), e12905. See the recalled quartic del Pezzo classification and Table A3.
