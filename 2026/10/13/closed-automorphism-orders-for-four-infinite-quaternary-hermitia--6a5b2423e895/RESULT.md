# Closed automorphism orders for four infinite quaternary Hermitian LCD classes
## Finding

Araya and Harada prove that for every
\[
s\ge6
\]
there are exactly four equivalence classes of quaternary Hermitian LCD codes with parameters
\[
[5s+3,2,4s+1]_4
\]
and Hermitian-dual minimum distance at least \(2\).

These four classes admit representatives with projective-column multiplicity vectors
\[
A_s=(s-1,s+1,s+2,s+2,s-1),
\]
\[
B_s=(s,s+1,s+1,s+2,s-1),
\]
\[
C_s=(s+1,s+1,s+1,s+2,s-2),
\]
and
\[
D_s=(s+1,s+1,s+2,s+2,s-3).
\]

Their full monomial automorphism-group orders are
\[
|\operatorname{Aut}(A_s)|
=
6(s-1)!^2(s+1)!(s+2)!^2,
\]
\[
|\operatorname{Aut}(B_s)|
=
3(s-1)!s!(s+1)!^2(s+2)!,
\]
\[
|\operatorname{Aut}(C_s)|
=
9(s-2)!(s+1)!^3(s+2)!,
\]
and
\[
|\operatorname{Aut}(D_s)|
=
6(s-3)!(s+1)!^2(s+2)!^2.
\]

The corresponding ordinary weight enumerators are
\[
W_{A_s}(z)
=
1+6z^{4s+1}+3z^{4s+2}+6z^{4s+4},
\]
\[
W_{B_s}(z)
=
1+3z^{4s+1}+6z^{4s+2}+3z^{4s+3}+3z^{4s+4},
\]
\[
W_{C_s}(z)
=
1+3z^{4s+1}+9z^{4s+2}+3z^{4s+5},
\]
and
\[
W_{D_s}(z)
=
1+6z^{4s+1}+6z^{4s+2}+3z^{4s+6}.
\]

Thus the four classified infinite classes have four stable symmetry types. The automorphism orders are a closed-form refinement of a classification whose mass-formula calculations otherwise treat automorphism groups computationally.

## Assumptions and scope

Write
\[
\mathbb F_4=\{0,1,\omega,\omega^2\},
\qquad
\omega^2=\omega+1.
\]
Use the five projective points of
\[
\operatorname{PG}(1,4)
\]
with normalized representatives
\[
p_1=(1,0),\quad
p_2=(0,1),\quad
p_3=(1,1),\quad
p_4=(1,\omega),\quad
p_5=(1,\omega^2).
\]

For nonnegative integers
\[
m_1,\ldots,m_5,
\]
let
\[
C(m_1,\ldots,m_5)
\]
be the dimension-two code whose generator matrix contains \(m_i\) copies of \(p_i\).

The primary source gives the four length-\(28\) seed vectors
\[
(4,6,7,7,4),\quad
(5,6,6,7,4),\quad
(6,6,6,7,3),\quad
(6,6,7,7,2)
\]
and proves a one-to-one correspondence with the four equivalence classes of
\[
[5s+3,2,4s+1]_4
\]
codes for every \(s\ge6\).

The claim concerns monomial automorphisms over \(\mathbb F_4\), which is the equivalence notion used in the source.

## Proof

Let
\[
J=(p_1\ p_2\ p_3\ p_4\ p_5).
\]
A direct Hermitian Gram calculation gives
\[
J\overline{J}^{\,T}=0.
\]
Therefore adjoining one copy of every projective point to a dimension-two generator matrix does not change
\[
G\overline{G}^{\,T}.
\]
In particular it preserves the Hermitian LCD property.

Starting from the four source seed vectors at length \(28\), adjoining one complete projective line
\[
s-5
\]
times gives exactly
\[
A_s,\ B_s,\ C_s,\ D_s.
\]
Their lengths are
\[
28+5(s-5)=5s+3.
\]
For a dimension-two projective-multiplicity code, each nonzero message direction vanishes precisely on one projective column class. Hence the five projective codeword classes have weights
\[
(5s+3)-m_i,
\]
and each projective message class contributes three nonzero scalar multiples.

This immediately gives the four displayed weight enumerators. In every case the minimum is
\[
4s+1.
\]
All columns are nonzero, so the Hermitian dual has no weight-one codeword and hence has distance at least \(2\). The four multiplicity multisets are distinct. Thus they give four inequivalent valid codes. Since the source proves that there are exactly four equivalence classes, these four representatives exhaust the classified family.

It remains to determine the full monomial automorphism groups.

Any monomial automorphism of a dimension-two code induces a projective transformation of
\[
\operatorname{PG}(1,4)
\]
that preserves the multiplicity attached to each projective point. Conversely, every such projective transformation lifts to code automorphisms, and after its action on projective classes is fixed, coordinates may be permuted arbitrarily inside each equal-column block.

The natural map
\[
\operatorname{GL}(2,4)\longrightarrow \operatorname{PGL}(2,4)
\]
has scalar kernel of order \(3\). Therefore
\[
|\operatorname{Aut}(C(m_1,\ldots,m_5))|
=
3
\left(\prod_{i=1}^5 m_i!\right)
|\operatorname{Stab}_{\operatorname{PGL}(2,4)}(m_1,\ldots,m_5)|,
\]
where the stabilizer preserves the multiplicity coloring of the five projective points.

Now
\[
\operatorname{PGL}(2,4)\cong A_5
\]
in its natural action on five points. The four multiplicity patterns have color classes of sizes
\[
(2,1,2),\quad(1,2,1,1),\quad(3,1,1),\quad(2,2,1),
\]
respectively.

For \(A_s\), the color-preserving permutations form
\[
S_2\times S_2
\]
before intersecting with \(A_5\); only the identity and simultaneous double transposition are even, so the projective stabilizer has order \(2\).

For \(B_s\), the only possible nontrivial color-preserving permutation is a single transposition, which is odd. The projective stabilizer therefore has order \(1\).

For \(C_s\), the three equal-multiplicity points may be permuted while the other two points are fixed. The even permutations form
\[
A_3,
\]
so the projective stabilizer has order \(3\).

For \(D_s\), the same parity argument as for \(A_s\) gives projective stabilizer order \(2\).

Substitution of the four multiplicity vectors into the general automorphism formula gives exactly the four factorial formulas in the Finding.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements exact arithmetic in
\[
\mathbb F_4,
\]
constructs the five normalized projective points, and verifies
\[
J\overline{J}^{\,T}=0.
\]

For the four source seed vectors and for several values
\[
s\ge6,
\]
it constructs the generator matrices, checks Hermitian LCD nonsingularity, computes all \(16\) codewords, and confirms the four closed weight-enumerator formulas.

The verifier enumerates all
\[
|\operatorname{GL}(2,4)|=180
\]
invertible \(2\times2\) matrices, computes their induced permutations of the five projective points, quotients the scalar repetition, and recovers the full
\[
60
\]
elements of
\[
\operatorname{PGL}(2,4).
\]
It then computes the multiplicity-color stabilizers exactly and confirms the orders
\[
2,\ 1,\ 3,\ 2.
\]

Finally it checks the resulting factorial automorphism formulas against the general
\[
3\prod_i m_i!
\]
times projective-stabilizer expression.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article completes the relevant quaternary Hermitian LCD classification. Proposition 4.13 gives a one-to-one correspondence between the four \([28,2,21]_4\) seed classes and the \([5s+3,2,4s+1]_4\) classes for \(s\ge6\), and it prints the four seed multiplicity vectors. The paper also defines monomial automorphism groups and uses their orders in the mass formula for classification.

The source does not give closed automorphism orders for these four infinite dimension-two classes. Its computational classification machinery uses colored-graph isomorphism and NAUTY for automorphism groups in the finite classification stages.

Earlier dimension-two classification work supplies the projective-multiplicity representation and the correspondence underlying the source's Proposition 4.13. The new step here is to combine that representation with the natural
\[
\operatorname{PGL}(2,4)\cong A_5
\]
action to determine the complete symmetry orders of all four infinite classes.

Focused searches using the exact seed vector
\[
(4,6,7,7,4),
\]
the parameters \([28,2,21]_4\), the infinite parameters \([5s+3,2,4s+1]_4\), and automorphism-group terminology found no prior formulas for these orders.

## Limitations

The theorem treats the four near-optimal classes in the residue class
\[
n\equiv3\pmod5
\]
covered by Proposition 4.13. It does not give automorphism formulas for every dimension-two Hermitian LCD class in the much larger classifications of the source.

Only automorphism-group orders are determined. The abstract group structures and their actions on codewords are not classified here.

The derivation uses the source's exhaustive equivalence-class count to conclude that the four augmented seed representatives exhaust the family. It does not independently redo the source classification.

An earlier dimension-two classification paper or an unpublished code database could contain equivalent individual automorphism orders, although no such formulas were found in the inspected published literature or exact searches.

## References

1. Makoto Araya and Masaaki Harada, *On the classification of quaternary Hermitian LCD codes*, Computational and Applied Mathematics 46 (2027), article 28, published 13 August 2026, DOI 10.1007/s40314-026-03875-2.
2. Makoto Araya and Masaaki Harada, *On the classification of quaternary optimal Hermitian LCD codes*, Cryptography and Communications 14 (2022), 833--847.
3. Kenji Ishizuka, *Classification of optimal quaternary Hermitian LCD codes of dimension 2*, Journal of Algebra Combinatorics Discrete Structures and Applications 7 (2020), 229--236.
