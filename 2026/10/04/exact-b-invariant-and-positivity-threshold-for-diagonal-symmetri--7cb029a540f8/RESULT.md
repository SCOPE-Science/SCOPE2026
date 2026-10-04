# Exact b-invariant and positivity threshold for diagonal symmetric-group permutation invariants
## Finding
Let \(k\) be a field with \(\operatorname{char}k\ne2\), let \(r,m\ge2\), and set
\[
S=k[x_{i,j}:1\le i\le r,\ 1\le j\le m].
\]
Let \(S_m\) act diagonally on the columns by \(\sigma(x_{i,j})=x_{i,\sigma(j)}\). Then the \(b\)-invariant of the invariant ring is completely explicit.

If \(r\) is even, then
\[
b(S^{S_m})=-rm.
\]
If \(r\) is odd, let \(q\) be the unique integer satisfying
\[
\binom{q+r-1}{r}<m\le\binom{q+r}{r}.
\]
Then
\[
b(S^{S_m})=r\binom{q+r-1}{r+1}+q\left(m-\binom{q+r-1}{r}\right)-rm.
\]
In particular, for every odd \(r\ge3\),
\[
b(S^{S_m})>0\quad\Longleftrightarrow\quad m>\binom{2r+1}{r}.
\]
At the boundary \(m=\binom{2r+1}{r}\) one has \(b=0\), while the first positive case
\[
m=\binom{2r+1}{r}+1
\]
has \(b=2\). For \(r=3\), this first positive case is \(m=36\), exactly the example isolated by Maithani--Singh--Watanabe.

## Assumptions and scope
The field has characteristic different from \(2\), and \(r,m\ge2\). The action is the direct sum of \(r\) copies of the natural permutation action of \(S_m\), equivalently the column-permutation action above. The statement concerns the \(b\)-invariant of the standard-graded invariant ring. No claim is made for characteristic \(2\), where the sign character degenerates and the relevant formula in the source has a different form. The case \(r=1\) is excluded because the image then contains transpositions, so the correction term in the general permutation-action theorem is nonzero.

## Proof
View the diagonal action as a subgroup of the symmetric group on the \(rm\) variables. For \(r\ge2\), no nonidentity element of this image is a single transposition: every moved column is moved simultaneously in all \(r\) rows. Thus the number \(c\) of transpositions in the image is \(0\).

Maithani--Singh--Watanabe, Theorem 2.8, states in characteristic different from \(2\) that for a permutation action on \(n\) variables,
\[
b(S^G)=d-2c-n,
\]
where \(d\) is the minimum degree of a monomial whose stabilizer in \(G\) is contained in the ambient alternating group. Here \(n=rm\) and \(c=0\).

If \(r\) is even, the image of a column permutation \(\sigma\) has sign \((\operatorname{sgn}\sigma)^r=1\). Hence the whole image lies in the alternating group. The monomial \(1\) therefore has an admissible stabilizer, so \(d=0\), giving \(b(S^{S_m})=-rm\).

Assume now that \(r\) is odd. For a monomial
\[
M=\prod_{j=1}^{m}\prod_{i=1}^{r}x_{i,j}^{a_{i,j}},
\]
write its exponent column as \(a_j=(a_{1,j},\ldots,a_{r,j})\in\mathbb N^r\). Because \(r\) is odd, the parity of a column permutation agrees with the parity of its permutation of all \(rm\) variables. The stabilizer of \(M\) contains an odd permutation exactly when two exponent columns coincide: a repeated pair can be swapped by a transposition, while pairwise distinct exponent columns give a trivial stabilizer. Therefore \(d\) is exactly the minimum of
\[
\sum_{j=1}^{m}|a_j|_1
\]
over \(m\) distinct points \(a_j\in\mathbb N^r\).

There are \(\binom{s+r-1}{r-1}\) points of \(\mathbb N^r\) of weight \(s\), and \(\binom{q+r}{r}\) points of weight at most \(q\). Hence a minimum is obtained by taking all points of weight below \(q\) and then exactly \(m-\binom{q+r-1}{r}\) points of weight \(q\), where \(q\) is characterized by
\[
\binom{q+r-1}{r}<m\le\binom{q+r}{r}.
\]
Using
\[
\sum_{s=0}^{q-1}s\binom{s+r-1}{r-1}=r\binom{q+r-1}{r+1},
\]
we obtain
\[
d=r\binom{q+r-1}{r+1}+q\left(m-\binom{q+r-1}{r}\right),
\]
and substituting \(b=d-rm\) proves the displayed formula.

For the positivity threshold, order the lattice points by nondecreasing weight. Adding a point of weight \(s\) changes \(d-rm\) by \(s-r\). At
\[
m_0=\binom{2r+1}{r},
\]
all points of weight at most \(r+1\) have been used, and
\[
d=r\binom{2r+1}{r+1}=r\binom{2r+1}{r}=rm_0,
\]
so \(b=0\). Before this boundary the increments through weight \(r+1\) have not yet recovered the negative initial value, so \(b<0\); after it, every new point has weight at least \(r+2\), so every increment is positive. The first point beyond the boundary changes \(b\) by \(2\), giving \(b=2\).

## Verification
The proof is symbolic and does not rely on finite enumeration. Three consistency checks are immediate. For \((r,m)=(3,36)\), the formula gives \(q=5\), \(d=110\), and \(b=2\), matching Example 2.10 of the source. For odd \(r=5\), the first positive case is \(m=\binom{11}{5}+1=463\) and again gives \(b=2\). For even \(r\), the determinant character of the diagonal permutation action is trivial, agreeing with the formula \(b=-rm\).

The only external theorem used in the proof is the permutation-action formula of Maithani--Singh--Watanabe, Theorem 2.8. The lattice-point count and weighted-sum identity are elementary stars-and-bars identities, and the stabilizer criterion is proved directly above.

## Relationship to prior work
Maithani--Singh--Watanabe prove the general permutation-action identity \(b(S^G)=d-2c-n\) and then give the single diagonal example \((r,m)=(3,36)\), where they compute \(d=110\) and obtain \(b=2\). The present result evaluates the previously abstract quantity \(d\) for every diagonal \(r\)-copy action with \(r,m\ge2\), and converts that evaluation into a sharp parity-and-size classification of when the \(b\)-invariant is positive. Their example is therefore the first member of the exact boundary family rather than an isolated construction.

Maithani's earlier work on permutation invariant rings gives the analogous stabilizer criterion for the \(a\)-invariant, but does not compute the anticanonical \(b\)-invariant or the diagonal-copy positivity threshold.

## Limitations
The theorem excludes characteristic \(2\) and the one-copy case \(r=1\). It computes the \(b\)-invariant but does not determine finer structure of the anticanonical module, such as a minimal generating set, for this family. The literature comparison found no statement of the arbitrary-\((r,m)\) formula or the sharp threshold, but a differently phrased equivalent result in the multisymmetric or alternating-polynomial literature remains a residual possibility.

## References
1. Aryaman Maithani, Anurag K. Singh, and Kei-ichi Watanabe, *On the \(b\)-invariant of a normal graded ring*, arXiv:2609.32003v1 (2026), Theorem 2.8 and Example 2.10.
2. Aryaman Maithani, *Homological properties of invariant rings of permutation groups*, Proceedings of the American Mathematical Society 154 (2026), 3257--3272; arXiv:2511.07718v2, especially Corollary 4.8.
