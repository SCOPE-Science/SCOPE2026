# An involution proves the even-length dimension-two Hermitian LCD count identity
## Finding

Araya and Harada ask whether, for every even length,
\[
|\vec{\mathcal C}(n,2,1,\ge2)|
+
|\vec{\mathcal C}(n,2,\ge2,\ge2)|
=
|\vec{\mathcal C}(n+1,2,\ge2,\ge2)|.
\]
The answer is affirmative for every even integer
\[
n\ge4.
\]

More strongly, there is an explicit bijection between the equivalence classes on the two sides.

For a quaternary dimension-two code with Hermitian-dual distance at least \(2\), scale nonzero generator columns projectively and write its corresponding multiplicity vector as
\[
m=(m_1,m_2,m_3,m_4,m_5),
\]
using the five points of
\[
\operatorname{PG}(1,4).
\]
For even \(n\), such a code is Hermitian LCD exactly when precisely two of the five multiplicities are odd.

Define
\[
\Phi(m)_i=
\begin{cases}
m_i+1,&m_i\ \text{is even},\\
m_i-1,&m_i\ \text{is odd}.
\end{cases}
\]
Because exactly two entries are odd and three are even,
\[
\sum_i\Phi(m)_i=n+1.
\]
The output has exactly three odd entries, is Hermitian LCD, and has minimum distance at least \(2\).

The operation commutes with every permutation of the five projective column classes, hence in particular with the projective transformations arising from code equivalence. It therefore descends to equivalence classes.

For an odd-length Hermitian LCD multiplicity vector, exactly three entries are odd. Applying the reverse update,
\[
m_i=
\begin{cases}
m_i'-1,&m_i'\ \text{is odd},\\
m_i'+1,&m_i'\ \text{is even},
\end{cases}
\]
recovers the unique even-length vector. Thus the correspondence is bijective and proves the source's first displayed open identity.

## Assumptions and scope

Let
\[
\mathbb F_4=\{0,1,\omega,\overline{\omega}\},
\qquad
\overline{\omega}=\omega^2,
\qquad
\omega^2+\omega+1=0.
\]

For the notation of the source,
\[
\vec{\mathcal C}(n,2,1,\ge2)
\]
denotes equivalence classes of quaternary Hermitian LCD codes of length \(n\), dimension \(2\), minimum distance \(1\), and Hermitian-dual minimum distance at least \(2\). Similarly,
\[
\vec{\mathcal C}(n,2,\ge2,\ge2)
\]
denotes those with both minimum distances at least \(2\).

Hermitian-dual distance at least \(2\) is equivalent to a generator matrix having no zero column. Up to scaling each nonzero column, there are exactly five projective column classes. We use representatives
\[
v_1=(1,0),\quad
v_2=(0,1),\quad
v_3=(1,1),\quad
v_4=(1,\omega),\quad
v_5=(1,\overline{\omega}).
\]

A multiplicity vector records how often these five projective classes occur. Row operations induce projective linear permutations of the five classes; coordinate permutations and nonzero coordinate scalings do not change the multiplicities. Thus equivalence classes of the codes under consideration correspond to projective-linear orbits of admissible multiplicity vectors.

## Proof

Let \(G\) be a generator matrix whose nonzero columns lie in the five projective classes with multiplicities
\[
m_1,\ldots,m_5.
\]
Write
\[
t=\#\{i:m_i\ \text{is odd}\}.
\]

The Hermitian Gram matrix is
\[
G\overline G^{\,T}.
\]
By the two-dimensional Cauchy--Binet identity,
\[
\det(G\overline G^{\,T})
=
\sum_{\{a,b\}}
\det(g_a,g_b)\,
\overline{\det(g_a,g_b)},
\]
where the sum is over unordered pairs of generator columns.

If two columns belong to the same projective class, the determinant is zero. If they belong to distinct projective classes, their determinant is a nonzero element of \(\mathbb F_4\), and
\[
z\overline z=z^3=1
\qquad
(z\in\mathbb F_4^\times).
\]
Therefore
\[
\det(G\overline G^{\,T})
=
\sum_{1\le i<j\le5}m_im_j
\pmod2.
\]
Only the parities of the \(m_i\) matter, so
\[
\det(G\overline G^{\,T})
=
\binom t2
\pmod2.
\]

The LCD criterion is nonsingularity of the Hermitian Gram matrix. Since
\[
t\equiv \sum_i m_i=n\pmod2,
\]
we obtain:

- for even \(n\), the code is Hermitian LCD exactly when \(t=2\);
- for odd \(n\), the code is Hermitian LCD exactly when \(t=3\).

Now let \(n\ge4\) be even and let \(m\) represent a code on the left side of the identity. Both left-hand sets have Hermitian-dual distance at least \(2\), so every coordinate column is nonzero; their union is exactly the set of all dimension-two Hermitian LCD equivalence classes of length \(n\) with no zero columns.

Since \(t=2\), define
\[
\Phi(m)_i=
\begin{cases}
m_i+1,&m_i\ \text{even},\\
m_i-1,&m_i\ \text{odd}.
\end{cases}
\]
Odd entries are positive, so \(\Phi(m)\) is nonnegative. Three entries increase and two decrease, hence
\[
\sum_i\Phi(m)_i=n+1.
\]
Every parity flips, so \(\Phi(m)\) has exactly three odd entries and is Hermitian LCD.

For a dimension-two code of length \(N\) with projective multiplicities \(a_i\), every nonzero linear functional vanishes on exactly one projective point of \(\operatorname{PG}(1,4)\). Hence
\[
d=N-\max_i a_i.
\]
If the output \(\Phi(m)\) had minimum distance \(1\), one multiplicity would be \(n\) and the other four would sum to \(1\). Since \(n\) is even, this would give exactly one odd multiplicity, contradicting the already established fact that the output has exactly three odd entries. Thus
\[
d(\Phi(m))\ge2.
\]

The transformation \(\Phi\) is coordinatewise and depends only on parity. It commutes with every permutation of the five projective classes. It therefore sends equivalent multiplicity vectors to equivalent multiplicity vectors and induces a map
\[
\vec{\mathcal C}(n,2,1,\ge2)
\sqcup
\vec{\mathcal C}(n,2,\ge2,\ge2)
\longrightarrow
\vec{\mathcal C}(n+1,2,\ge2,\ge2).
\]

Conversely, let \(m'\) represent a code on the right. Its length is odd and it is Hermitian LCD, so exactly three entries of \(m'\) are odd. Define
\[
\Psi(m')_i=
\begin{cases}
m_i'-1,&m_i'\ \text{odd},\\
m_i'+1,&m_i'\ \text{even}.
\end{cases}
\]
This is nonnegative, has total \(n\), has exactly two odd entries, and hence is Hermitian LCD. It has no zero generator columns because multiplicity zero merely means that a projective class is absent, not that a coordinate column is zero. Therefore \(\Psi(m')\) lies in one of the two left-hand sets.

The maps satisfy
\[
\Psi(\Phi(m))=m,
\qquad
\Phi(\Psi(m'))=m',
\]
and both commute with projective transformations. They are inverse bijections on equivalence classes. Taking cardinalities proves the identity.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements \(\mathbb F_4\), the five points of
\[
\operatorname{PG}(1,4),
\]
and all projective permutations induced by
\[
\operatorname{GL}(2,4).
\]
The verifier obtains exactly \(60\) induced permutations.

It checks all \(32\) parity patterns and independently confirms
\[
\det(G\overline G^{\,T})\ne0
\]
exactly for parity weight \(2\) or \(3\).

It then exhaustively enumerates all five-part multiplicity vectors for every even
\[
4\le n\le20,
\]
reduces them to projective-linear orbits, and verifies that the parity involution gives a bijection between all length-\(n\) Hermitian LCD classes with dual distance at least \(2\) and all length-\(n+1\) Hermitian LCD classes with both distances at least \(2\).

For these finite stress tests, the equality of the two class counts is checked orbit-by-orbit, not merely numerically.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Araya and Harada classify quaternary Hermitian LCD codes extensively and explicitly pose two count identities suggested by their dimension-two and dimension-three tables. The first identity is the one proved here. Their paper verifies the relevant counts computationally through substantial finite ranges but states the all-even-length equality as a question.

The same paper uses five-entry corresponding vectors for dimension-two codes and gives classifications in terms of these projective-column multiplicities. It does not state the parity-complement involution above or a proof of the all-length equality.

Earlier classification work on optimal quaternary Hermitian LCD codes supplies the projective multiplicity framework for dimension two, but the 2026 article still identifies this count equality as unresolved. Focused searches using the exact displayed identity, dimension-two count notation, parity-multiplicity language, and projective-line formulations did not locate a prior proof.

## Limitations

Only the first of the two count identities posed together in the source is resolved here. No claim is made about the source's second, dimension-three identity.

The bijection is between the standard monomial-equivalence classes used in the source. It does not count labeled generator matrices.

The proof is special to dimension two over \(\mathbb F_4\), where the five projective column classes and the Hermitian Cauchy--Binet determinant collapse the LCD condition to a parity count.

A proof under substantially different finite-geometric terminology could exist outside the searched literature; no such covering result was found.

## References

1. Makoto Araya and Masaaki Harada, *On the classification of quaternary Hermitian LCD codes*, Computational and Applied Mathematics 46 (2027), article 28, first public 13 August 2026, DOI 10.1007/s40314-026-03875-2.
2. Makoto Araya and Masaaki Harada, *On the classification of quaternary optimal Hermitian LCD codes*, Cryptography and Communications 14 (2022), 833--847.
