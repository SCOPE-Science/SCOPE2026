# All-length classification of cardinality-two ACD codes over \(I_2\)
## Finding

Let
\[
I_2=\langle a,b\mid 2a=2b=0,\ a^2=b,\ ab=0\rangle
=\{0,a,b,c=a+b\}.
\]
For every
\[
n\ge1,
\]
every additive code of cardinality two in \(I_2^n\) has the form
\[
C_v=\{0,v\}
\]
for a unique nonzero vector \(v\).

Write
\[
n_0(v),\quad n_a(v),\quad n_b(v),\quad n_c(v)
\]
for the four coordinate multiplicities. Then
\[
C_v\text{ is ACD}
\quad\Longleftrightarrow\quad
n_a(v)+n_c(v)\text{ is odd}.
\]

Consequently, up to coordinate permutation, cardinality-two ACD codes of length \(n\) are classified exactly by the compositions
\[
(n_0,n_a,n_b,n_c)
\]
satisfying
\[
n_0+n_a+n_b+n_c=n,
\qquad
n_a+n_c\equiv1\pmod2.
\]

If such a code has Hamming distance
\[
d=n-n_0,
\]
then the number of coordinate-permutation classes at distance \(d\) is
\[
N_d=
\begin{cases}
t(t+1),&d=2t,\\[2mm]
(t+1)(t+2),&d=2t+1.
\end{cases}
\]
In particular, this distance profile depends only on \(d\), once \(n\ge d\).

Summing over \(1\le d\le n\), the total number \(A_n\) of coordinate-permutation classes is
\[
A_{2m}
=
\frac{2m(m+1)(m+2)}{3}
\]
and
\[
A_{2m+1}
=
\frac{(m+1)(m+2)(2m+3)}{3}.
\]

Before quotienting by coordinate permutations, the exact number of labeled cardinality-two ACD codes is
\[
2^{2n-1}.
\]

The largest possible Hamming distance is \(n\). The number of classes attaining it is
\[
m(m+1)
\]
when
\[
n=2m,
\]
and
\[
(m+1)(m+2)
\]
when
\[
n=2m+1.
\]

For
\[
n=1,2,3,4,5,
\]
the total class counts are
\[
2,\ 4,\ 10,\ 16,\ 28,
\]
exactly the cardinality-two counts displayed in Table 5 of Kim, Olavides, and Roe. The formulas above extend this finite row to every length and refine it by Hamming distance.

## Assumptions and scope

The additive group of \(I_2\) is
\[
(\mathbb Z/2\mathbb Z)^2.
\]
We use the Euclidean coordinatewise inner product employed for ACD codes over \(I_2\):
\[
\langle x,y\rangle=\sum_{i=1}^n x_i y_i.
\]
For an additive code \(C\),
\[
C^\perp=\{x:\langle x,c\rangle=0\text{ for all }c\in C\},
\]
and \(C\) is ACD when
\[
C\cap C^\perp=\{0\}.
\]

Equivalence in the classification statement means permutation of the \(n\) coordinates. The theorem is restricted to additive codes of cardinality two; larger additive codes have additional subgroup structure and are not classified here.

The published article has a later revision that corrects three theorem statements and their proofs. The argument here uses only the defining ring relations, the ACD definition, and the published small-length cardinality-two counts, so it does not depend on those corrected theorem statements.

## Proof

Because every nonzero element of the additive group \(I_2\) has order two, every cardinality-two additive subgroup of \(I_2^n\) is
\[
C_v=\{0,v\}
\]
for a unique nonzero \(v\).

Since \(C_v\) has only one nonzero word,
\[
C_v\cap C_v^\perp\ne\{0\}
\]
holds exactly when
\[
v\in C_v^\perp,
\]
which is equivalent to
\[
\langle v,v\rangle=0.
\]

The multiplication table of \(I_2\) gives
\[
0^2=b^2=0,
\qquad
a^2=c^2=b.
\]
Therefore
\[
\langle v,v\rangle
=
\bigl(n_a(v)+n_c(v)\bigr)b.
\]
The additive order of \(b\) is two, so
\[
\langle v,v\rangle\ne0
\]
if and only if
\[
n_a(v)+n_c(v)
\]
is odd. This proves the ACD criterion.

Two vectors are in the same coordinate-permutation orbit exactly when their four coordinate multiplicities agree. Hence the ACD classes are exactly the stated compositions.

Fix the Hamming distance
\[
d=n-n_0.
\]
Put
\[
j=n_a+n_c.
\]
The ACD condition says that \(j\) is odd. Once \(j\) is fixed,
\[
n_b=d-j
\]
is forced, while
\[
(n_a,n_c)
\]
can be chosen in exactly
\[
j+1
\]
ways. Thus
\[
N_d
=
\sum_{\substack{1\le j\le d\\ j\text{ odd}}}(j+1).
\]

If
\[
d=2t,
\]
this is
\[
2+4+\cdots+2t=t(t+1).
\]
If
\[
d=2t+1,
\]
this is
\[
2+4+\cdots+2(t+1)=(t+1)(t+2).
\]
This proves the distance-refined profile.

For
\[
n=2m,
\]
summing the even- and odd-distance contributions gives
\[
A_{2m}
=
2\sum_{t=1}^m t(t+1)
=
\frac{2m(m+1)(m+2)}{3}.
\]
For
\[
n=2m+1,
\]
one adds the final odd-distance term:
\[
A_{2m+1}
=
A_{2m}+(m+1)(m+2)
=
\frac{(m+1)(m+2)(2m+3)}{3}.
\]

For the labeled count, at each coordinate there are exactly two symbols,
\[
a,c,
\]
that contribute one to the parity \(n_a+n_c\), and two symbols,
\[
0,b,
\]
that contribute zero. Exactly half of the
\[
4^n
\]
vectors therefore have odd parity, giving
\[
2^{2n-1}
\]
labeled ACD codes.

Finally, maximum Hamming distance means
\[
n_0=0,
\]
so its number of classes is simply \(N_n\), yielding the two displayed parity formulas.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It realizes the four ring elements as pairs in
\[
\mathbb F_2^2,
\]
with
\[
a=(1,0),\qquad b=(0,1),\qquad c=(1,1),
\]
and multiplication
\[
(xa+yb)(x'a+y'b)=xx'b.
\]

For every
\[
1\le n\le7,
\]
the verifier enumerates all
\[
4^n
\]
vectors directly. It checks the ACD condition by computing
\[
\langle v,v\rangle
\]
from the ring multiplication and independently checks the parity criterion.

It groups all ACD vectors by their exact coordinate composition, verifies the distance-refined orbit counts, the total closed formulas, the labeled count
\[
2^{2n-1},
\]
and the number of full-support classes.

For
\[
n=1,\ldots,5,
\]
it checks the published cardinality-two totals
\[
2,\ 4,\ 10,\ 16,\ 28.
\]

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Kim, Olavides, and Roe study ACD codes over the non-unital rings \(I_2\) and \(I_3\), relate them to binary and ternary LCD codes, and classify the best small-length examples. Their Table 5 records cardinality-two ACD counts
\[
2,\ 4,\ 10,\ 16,\ 28
\]
for lengths \(1\) through \(5\), together with maximum Hamming distance equal to the length in each of those rows.

A July 2026 revision of the article states that Theorems 3.5, 4.7, and 4.8 and their proofs were corrected. Its abstract continues to describe the \(I_2\) classification as complete for lengths \(1,2,3\) and partial for lengths \(4,5\), rather than as an all-length enumeration.

The broader theory of ACD codes supplies generator-matrix characterizations and constructions over finite-field extension alphabets, while earlier duality work over non-unital rings of order four develops the ambient ring-code framework. Neither inspected source states the parity classification of every cardinality-two \(I_2\) code or the all-length orbit and distance formulas above.

Focused searches using the ring name, cardinality two, the published sequence
\[
2,4,10,16,28,
\]
the odd-\(a/c\) parity condition, and the two closed counting formulas located no prior all-length statement.

## Limitations

The theorem classifies only cardinality-two additive codes. It does not enumerate cardinality \(4\), \(8\), or larger ACD codes, where multiple generators interact.

The equivalence relation used here is coordinate permutation. A larger equivalence relation allowing alphabet automorphisms could merge some composition classes and would require a separate analysis.

The source article has a later correction. Although the present proof is independent of the corrected theorem statements, a future full revision could potentially contain further classification remarks not visible in the inspected public abstract and tables.

The counting argument is elementary once the multiplication table is isolated; the mathematical value is the complete all-length classification and distance profile of the smallest nontrivial ACD layer, extending the finite classification row in the recent source.

## References

1. Jon-Lark Kim, Marvin Olavides, and Young Gun Roe, *Some MDS and ACD codes over commutative non-unital rings of orders 4 and 9*, Advances in Mathematics of Communications 24 (2026), 61--76, DOI 10.3934/amc.2026028.
2. Jon-Lark Kim, Marvin Olavides, and Young Gun Roe, *Some MDS and ACD codes over commutative non-unital rings of orders 4 and 9 (Revision)*, arXiv:2609.20190v1, 2026.
3. Adel Alahmadi, Amani Melaibari, and Patrick Solé, *Duality of codes over non-unital rings of order four*, IEEE Access 11 (2023), 53120--53133, DOI 10.1109/ACCESS.2023.3261131.
4. Whan Hyuk Choi, Cem Güneri, Jon-Lark Kim, and Ferruh Özbudak, *Theory of additive complementary dual codes, constructions and computations*, Finite Fields and Their Applications 92 (2023), 102303, DOI 10.1016/j.ffa.2023.102303.
