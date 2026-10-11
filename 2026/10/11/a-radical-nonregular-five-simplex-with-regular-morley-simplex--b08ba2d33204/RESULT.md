# A radical nonregular five-simplex with regular Morley simplex
## Finding
Let
\[
a=2\sqrt2-1
\]
and
\[
c=-\frac32+\sqrt2+\frac12\sqrt{-39+36\sqrt2}.
\]
Then
\[
1<c<a<2.
\]
For the six-vertex dihedral system of Tran, take
\[
c_1=c_2=a,\qquad c_3=c,\qquad T=\frac{c+2}{8}.
\]
These parameters satisfy the full system and its positivity conditions. Hence there is a nonregular five-dimensional simplex whose Morley simplex is regular and whose matrix of trisected dihedral data is the circulant matrix with first row
\[
(1,a,a,c,a,a).
\]

The full isometry group on its six vertices is
\[
C_2\wr S_3,
\]
the automorphism group of three disjoint matched pairs, and therefore has order
\[
2^3\,3!=48.
\]
The three matched-pair transpositions are each induced by a hyperplane reflection. In particular the example has three pairwise disjoint vertex transpositions available as reflections, so it satisfies the two-disjoint-reflections conclusion conjectured for five-simplices.

The construction is exact by radicals. Numerically,
\[
a=1.828427124746190\ldots,
\qquad
c=1.639879248813506\ldots,
\qquad
T=0.454984906101688\ldots .
\]

## Assumptions and scope
For an \(n\)-simplex with \(N=n+1\) vertices, Tran writes
\[
q_{ij}=2\cos(\theta_{ij}/3),
\qquad
\phi(x)=\frac{3x-x^3}{2},
\]
where \(\theta_{ij}\) is the interior dihedral angle between the two corresponding facets. In the cyclic-distance ansatz with \(N=6\), the first row of the symmetric circulant matrix \(K=(q_{ij})\) is
\[
r=(1,c_1,c_2,c_3,c_2,c_1).
\]
The source's Lemma 9.1 states that a solution of its equations (15), with \(1<c_m<2\), \(T>0\), and positive nonconstant Fourier eigenvalues of \(H=\phi[K]\), produces an \((N-1)\)-simplex with regular Morley simplex.

The finding is an existence and symmetry theorem for one exact \(N=6\) solution. It is not a classification of all five-simplices with regular Morley simplex, nor a proof of the source's full dimension-five reflection conjecture.

## Proof
Write
\[
A=2\sqrt2-1,
\qquad
C=-\frac32+\sqrt2+\frac12\sqrt{-39+36\sqrt2}.
\]
The two radicals satisfy
\[
A^2+2A-7=0
\]
and
\[
C^2+(2-A)C+A^2-4A+1=0.
\]
Using the first relation, the second becomes
\[
C^2+(3-2\sqrt2)C+14-12\sqrt2=0.
\]
Its value at \(1\) is \(18-14\sqrt2<0\), while its value at \(2\) is \(24-16\sqrt2>0\). Thus its positive root satisfies
\[
1<C<2.
\]
Also \(3/2<A<2\), so all three off-diagonal parameters lie in the required interval.

Set
\[
r=(1,A,A,C,A,A).
\]
For a circulant matrix, the nonconstant Fourier eigenvalues of \(K\) are
\[
\kappa_1=\kappa_3=1-C,
\qquad
\kappa_2=1-2A+C,
\]
with the first and third values carrying the appropriate conjugate multiplicities. Let
\[
h_k
\]
denote the corresponding Fourier eigenvalues of
\[
H=\phi[K].
\]
The constant mode is
\[
h_0=\phi(1)+4\phi(A)+\phi(C).
\]
From \(A^2+2A-7=0\) one gets
\[
A^3=11A-14.
\]
From the second quadratic relation one obtains
\[
C^3=3C+58-32A.
\]
Substitution gives
\[
h_0=0.
\]

For the modes \(1\) and \(3\),
\[
h_1=h_3=1-\phi(C)
=\frac{(C-1)^2(C+2)}{2}.
\]
With
\[
T=\frac{C+2}{8},
\]
this is exactly
\[
h_1=h_3=4T\kappa_1^2.
\]
For the remaining mode,
\[
h_2=1-2\phi(A)+\phi(C).
\]
A direct factorization gives
\[
2h_2-(C+2)(1-2A+C)^2
=2(A-C)\bigl(A^2-AC-4A+C^2+2C+1\bigr).
\]
The factor in parentheses is precisely the second quadratic relation, hence
\[
h_2=4T\kappa_2^2.
\]
Therefore all Fourier eigenvalues of the two circulant matrices
\[
H
\quad\text{and}\quad
4TK\left(I-\frac16\mathbf1\mathbf1^{\mathsf T}\right)K
\]
agree. The matrices are equal, which is equivalent to the source's system (15).

The positivity conditions are strict. Since \(C>1\),
\[
\kappa_1=1-C\ne0.
\]
Since \(A>3/2\) and \(C<2\),
\[
\kappa_2=1-2A+C<0.
\]
Also \(T>0\). Hence
\[
h_k=4T\kappa_k^2>0
\]
for every nonconstant Fourier mode. Tran's Lemma 9.1 now yields a five-simplex \(\Delta\) whose Morley simplex is regular.

The simplex is not regular because \(A\ne C\). Indeed, if \(A=C\), the second quadratic relation reduces to
\[
(A-1)^2=0,
\]
contradicting \(A>3/2\).

Finally, the only off-diagonal entries of \(K\) equal to \(C\) occur on the three pairs
\[
\{0,3\},\qquad \{1,4\},\qquad \{2,5\}.
\]
All other off-diagonal entries equal \(A\). Because \(A\ne C\), a permutation preserves \(K\) exactly when it preserves this perfect matching. Thus the full permutation group preserving \(K\) is
\[
C_2\wr S_3
\]
of order \(48\). By the source's Proposition 3.1, these are exactly the vertex permutations induced by isometries of \(\Delta\), and each transposition within one matched pair is induced by a hyperplane reflection. This proves the symmetry assertion.

## Verification
The bundled checker uses exact rational arithmetic in the degree-four field
\[
\mathbb Q\!\left(\sqrt2,\sqrt{-39+36\sqrt2}\right)
\]
to replay the two algebraic defining relations, the constant-mode identity, all three nonconstant spectral identities, and the four cyclic-distance equations. It separately evaluates the radicals at high decimal precision to display the strict interval inequalities.

The checker is a replay aid. The general existence implication is supplied by the cited Lemma 9.1, while the exact algebraic identities are displayed in the proof.

## Relationship to prior work
Tran's 2026 paper develops the higher-dimensional Morley construction, proves the matrix regularity criterion, formulates the dimension-five two-reflection conjecture, and introduces the dihedral system used here. The paper explicitly states that it makes no existence or nonexistence assertion for the dihedral cases \(N=6,7,8\). It certifies its strictly ordered dihedral branch only from \(N=9\) onward.

The same paper reports that numerical searches in dimension five produced nonregular solutions having two reflections on disjoint pairs, but it states that those observations were not certified and gave no classification. The present result upgrades one natural six-vertex circulant instance to an exact theorem, with radical parameters and its complete vertex-isometry group.

Targeted searches using the source identifier, \(N=6\) dihedral/circulant terminology, the radical fingerprint \(2\sqrt2-1\), and dimension-five Morley aliases found no published statement implying this exact solution. A prior result using the same source studied a continuum limit of the dihedral equations rather than any finite \(N=6\) solution and does not imply the present construction.

## Limitations
This does not classify all solutions of the \(N=6\) dihedral system. In particular, it does not exclude additional regular or nonregular branches. It also does not prove that every five-simplex with regular Morley simplex has the conjectured reflection symmetries.

The broad existence of numerically observed dimension-five solutions with two reflections was already reported by the source; the new content here is an exact radical solution of the explicitly untreated \(N=6\) dihedral system together with its exact symmetry group. Very recent or poorly indexed follow-up work remains a residual bibliographic risk.

## References
1. Q. H. Tran, *Morley Simplices in Higher Dimensions: Regularity, Reflections, and Counterexamples*, arXiv:2610.01216v1, first public 2026-10-01. Primary MSC 51M04.
2. Q. H. Tran, *Morley's trisector theorem for isosceles tetrahedron*, Acta Math. Hungar. 165 (2021), 308--315, DOI 10.1007/s10474-021-01184-0.
