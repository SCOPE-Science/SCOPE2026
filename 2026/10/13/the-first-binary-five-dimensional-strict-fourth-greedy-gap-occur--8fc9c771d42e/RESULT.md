# The first binary five-dimensional strict fourth-greedy gap occurs at length eleven
## Finding

For binary linear codes of dimension
\[
5,
\]
the smallest block length at which the CEZ fourth greedy weight can strictly exceed the fourth generalized Hamming weight is
\[
11.
\]

Equivalently, every binary
\[
[n,5]
\]
code with
\[
n\le 10
\]
satisfies
\[
g_4=d_4,
\]
while there exists a binary
\[
[11,5]
\]
code with
\[
d_4=8,\qquad g_4=9.
\]

One length-eleven witness has generator columns
\[
3e_1,\quad
2e_2,\quad
2e_3,\quad
2(e_2+e_3),\quad
e_4,\quad
e_5,
\]
where repeated notation means repeated columns. Its generalized Hamming hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5)
=
(1,2,5,8,11).
\]

Thus length eleven is the exact first binary dimension-five occurrence of a strict fourth-greedy gap.

## Assumptions and scope

The fourth greedy weight is the bottom-up CEZ greedy weight used in the recent dimension-five study: \(g_4\) is the minimum support of a four-dimensional subcode that contains a three-dimensional subcode attaining \(d_3\).

Identically zero coordinates can be deleted without changing the dimension, any generalized Hamming weight, or any greedy weight. It is therefore enough to work with a nondegenerate generator matrix, whose columns determine a multiplicity function
\[
m:\operatorname{PG}(4,2)\longrightarrow\mathbb Z_{\ge0}.
\]

Put
\[
M=\max_p m(p)
\]
over projective points,
\[
L=\max_\ell m(\ell)
\]
over projective lines, and
\[
B=
\max\{m(p):p\in\ell,\ m(\ell)=L\}.
\]

The projective-subspace correspondence gives
\[
d_3=n-L,\qquad d_4=n-M.
\]
A four-dimensional subcode contains a \(d_3\)-minimizing three-dimensional subcode exactly when its annihilator point lies on a line of mass \(L\). Hence
\[
g_4=n-B.
\]
Therefore
\[
g_4>d_4
\]
is equivalent to
\[
B<M.
\]

## Proof

Assume
\[
g_4>d_4.
\]
Choose a point \(p\) with
\[
m(p)=M
\]
and a line \(\ell\) with
\[
m(\ell)=L.
\]
Because
\[
B<M,
\]
no maximum-mass line contains a point of multiplicity \(M\). In particular,
\[
p\notin\ell.
\]

Choose \(q\in\ell\) with largest multiplicity on \(\ell\), and write
\[
b=m(q).
\]
Then every point of \(\ell\) has multiplicity at most \(b\), so
\[
L\le3b.
\]

The binary projective line through \(p\) and \(q\) consists of exactly the three points
\[
p,\quad q,\quad p+q.
\]
It contains the multiplicity-\(M\) point \(p\), so it cannot itself be a maximum-mass line. Consequently
\[
M+b
\le
m(\overline{pq})
\le
L-1,
\]
and hence
\[
L\ge M+b+1.
\]

Combining the two inequalities yields
\[
3b\ge M+b+1,
\]
or
\[
2b\ge M+1.
\]
Since a maximum line contains no point of multiplicity \(M\),
\[
b\le M-1.
\]
Thus
\[
2(M-1)\ge M+1,
\]
so
\[
M\ge3.
\]

The line \(\ell\) spans a two-dimensional vector subspace of \(\mathbb F_2^5\), and adjoining \(p\notin\ell\) raises the span to dimension three. Because the generator has rank five, its positive-multiplicity projective support must contain at least two further points that successively raise this span to dimension five. Each contributes at least one column. Therefore
\[
n\ge M+L+2.
\]
Using
\[
L\ge M+b+1
\]
and
\[
2b\ge M+1,
\]
the smallest possible integer values are
\[
M=3,\qquad b=2,\qquad L\ge6.
\]
It follows that
\[
n\ge3+6+2=11.
\]

To attain equality, take the multiplicity assignment
\[
m(e_1)=3,
\]
\[
m(e_2)=m(e_3)=m(e_2+e_3)=2,
\]
\[
m(e_4)=m(e_5)=1,
\]
and zero elsewhere in \(\operatorname{PG}(4,2)\).

The three points
\[
e_2,\quad e_3,\quad e_2+e_3
\]
form a line of mass
\[
6.
\]
It is the unique maximum-mass line. The global maximum point multiplicity is
\[
M=3
\]
at \(e_1\), while the largest point multiplicity on the maximum line is
\[
B=2.
\]
Hence
\[
d_4=11-3=8
\]
and
\[
g_4=11-2=9.
\]

This proves both the lower bound and the sharp witness.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs the length-eleven generator from the column multiset
\[
3e_1,\ 2e_2,\ 2e_3,\ 2(e_2+e_3),\ e_4,\ e_5
\]
and checks rank \(5\).

It enumerates all
\[
155
\]
projective lines in \(\operatorname{PG}(4,2)\), verifies
\[
M=3,\qquad L=6,\qquad B=2,
\]
and confirms that the line
\[
\{e_2,e_3,e_2+e_3\}
\]
is the unique mass-six line.

It independently enumerates every subspace of the five-dimensional message space and obtains
\[
(d_1,d_2,d_3,d_4,d_5)
=
(1,2,5,8,11).
\]
The unique \(d_3\)-minimizing three-subcode is then tested against all four-dimensional supercodes; their support weights are all
\[
9,
\]
so the direct CEZ definition gives
\[
g_4=9.
\]

The all-code lower bound is the symbolic projective argument in the Proof section; the finite computation is a replay of the sharp equality witness, not a replacement for that proof.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Bose and Wei study the fourth greedy weight specifically for five-dimensional codes and formulate it by projective multiplicities in \(\operatorname{PG}(4,q)\). Their paper develops upper bounds for
\[
g_4-d_4
\]
under prescribed values of
\[
n,d_1,d_2,d_3
\]
and constructs value assignments attaining several such bounds. The full article contains no shortest-length theorem for a strict binary fourth-greedy gap and no binary length-eleven witness.

Johnsen and Verdure place greedy weights in the broader matroid framework and show that the coding-theoretic notions are recovered for representable matroids. Their examples demonstrate that greedy and generalized weights can differ, but do not determine the first binary dimension-five length at which the fourth weights differ.

The present result asks a different extremal question: before optimizing the size of a gap subject to a prescribed weight profile, what is the smallest binary block length on which any strict fourth-greedy gap can occur? The answer is exactly eleven.

Focused searches for a binary
\[
[11,5]
\]
fourth-greedy example, for a minimum-length theorem for
\[
g_4>d_4,
\]
and for the equivalent \(\operatorname{PG}(4,2)\) multiplicity condition located no prior statement of this cutoff.

## Limitations

The theorem is specific to binary dimension-five codes and the CEZ bottom-up fourth greedy weight. It does not give the corresponding shortest length over larger fields or for other greedy indices.

The length-eleven witness has
\[
d_1=1.
\]
The result therefore concerns the first occurrence of the greedy-weight phenomenon itself, not the first occurrence under an additional minimum-distance constraint.

The proof determines the minimum possible length and supplies one sharp multiplicity pattern. It does not classify all binary length-eleven codes with
\[
g_4>d_4.
\]

A differently phrased older result in the greedy-weight literature could state an equivalent cutoff; no such statement was found in the inspected primary and broader sources.

## References

1. Rega Bose and Yao Wei, *On the fourth greedy weight for 5-dimensional codes*, Advances in Mathematics of Communications 27 (2027), article 101088, published online 24 September 2026, DOI 10.3934/amc.2026.101088.
2. Trygve Johnsen and Hugues Verdure, *Greedy weights for matroids*, Designs, Codes and Cryptography 89 (2021), 387--405, DOI 10.1007/s10623-020-00824-w.
3. Wende Chen and Torleiv Kløve, *On the second greedy weight for binary linear codes*, Lecture Notes in Computer Science 1719 (1999), 131--141, DOI 10.1007/3-540-46796-3_13.
