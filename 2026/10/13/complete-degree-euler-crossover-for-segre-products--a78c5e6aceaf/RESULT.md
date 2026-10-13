# Complete degree–Euler crossover for Segre products
## Finding
Let
\[
X_{\mathbf a}
=
\mathbb P^{a_1}\times\cdots\times\mathbb P^{a_r},
\qquad
a_i\ge1,
\]
and embed \(X_{\mathbf a}\) by the standard Segre line bundle
\[
\mathcal O(1,\ldots,1).
\]
Put
\[
N=\sum_{i=1}^r a_i.
\]

Its projective degree and topological Euler characteristic are
\[
\boxed{
D(\mathbf a)
=
\deg X_{\mathbf a}
=
\frac{N!}{\prod_i a_i!}
}
\]
and
\[
\boxed{
E(\mathbf a)
=
\chi_{\mathrm{top}}(X_{\mathbf a})
=
\prod_i(a_i+1).
}
\]

Up to permutation of the factors, the complete comparison is as follows.

The strict inequality
\[
D(\mathbf a)<E(\mathbf a)
\]
holds exactly in these cases:

\[
r=1;
\]

\[
r=2
\quad\text{and}\quad
a_1=1,
\]
or
\[
(a_1,a_2)=(2,2),(2,3);
\]

\[
r=3
\quad\text{and}\quad
(a_1,a_2,a_3)=(1,1,1).
\]

Equality
\[
D(\mathbf a)=E(\mathbf a)
\]
holds exactly for
\[
\boxed{
\mathbb P^2\times\mathbb P^4
}
\]
and
\[
\boxed{
\mathbb P^1\times\mathbb P^1\times\mathbb P^2.
}
\]

In every other case,
\[
D(\mathbf a)>E(\mathbf a).
\]

A single coordinate-growth identity explains the whole classification. If
\[
R(\mathbf a)=\frac{D(\mathbf a)}{E(\mathbf a)},
\]
then
\[
\boxed{
\frac{R(\mathbf a+\mathbf e_j)}{R(\mathbf a)}
=
\frac{N+1}{a_j+2}
=
1+
\frac{\sum_{i\ne j}a_i-1}{a_j+2}.
}
\]
Thus \(R\) is strictly increasing in every coordinate as soon as there are at least three factors, and for two factors the only flat direction occurs when the other factor is \(\mathbb P^1\).

## Assumptions and scope
The base field is \(\mathbb C\). Every factor has positive dimension.

The embedding is the standard Segre embedding associated with
\[
\mathcal O(1,\ldots,1).
\]
The degree is the ordinary projective degree in that embedding.

The topological Euler characteristic is the ordinary Euler characteristic of the complex projective variety.

The theorem treats arbitrary numbers of projective-space factors and arbitrary positive factor dimensions.

## Proof
Let
\[
h_i
\]
denote the pullback of the hyperplane class from the \(i\)-th projective-space factor. The hyperplane class of the Segre embedding is
\[
H=h_1+\cdots+h_r.
\]
Since
\[
\dim X_{\mathbf a}=N,
\]
the projective degree is
\[
\int_{X_{\mathbf a}}H^N.
\]
Only the monomial
\[
h_1^{a_1}\cdots h_r^{a_r}
\]
contributes to the integral. Its multinomial coefficient is
\[
\frac{N!}{a_1!\cdots a_r!},
\]
and its integral is \(1\). Hence
\[
D(\mathbf a)=\frac{N!}{\prod_i a_i!}.
\]

Euler characteristic is multiplicative on products, and
\[
\chi_{\mathrm{top}}(\mathbb P^a)=a+1.
\]
Therefore
\[
E(\mathbf a)=\prod_i(a_i+1).
\]

Now set
\[
R(\mathbf a)=\frac{D(\mathbf a)}{E(\mathbf a)}.
\]
Increasing \(a_j\) by one changes the multinomial degree by the factor
\[
\frac{N+1}{a_j+1}
\]
and changes the Euler characteristic by
\[
\frac{a_j+2}{a_j+1}.
\]
Thus
\[
\frac{R(\mathbf a+\mathbf e_j)}{R(\mathbf a)}
=
\frac{N+1}{a_j+2}
=
1+
\frac{\sum_{i\ne j}a_i-1}{a_j+2}.
\]

For
\[
r\ge3,
\]
the sum of the other factor dimensions is at least \(2\), so every coordinate increment is strictly increasing.

For
\[
r=2,
\]
assume
\[
1\le a\le b.
\]
If \(a=1\), then
\[
R(1,b)=\frac12.
\]
If \(a=2\), then
\[
R(2,b)=\frac{b+2}{6},
\]
so it is below \(1\) for \(b=2,3\), equal to \(1\) for \(b=4\), and above \(1\) for \(b\ge5\). If \(a\ge3\), coordinate monotonicity from
\[
R(3,3)=\frac54
\]
gives strict domination.

For
\[
r=3,
\]
the minimum tuple is
\[
(1,1,1),
\]
where
\[
R(1,1,1)=\frac34.
\]
The three nearest coordinate increments are permutations of
\[
(1,1,2),
\]
where
\[
R(1,1,2)=1.
\]
Strict coordinate growth thereafter gives \(R>1\) everywhere else.

For
\[
r\ge4,
\]
strict coordinate growth makes
\[
(1,\ldots,1)
\]
the unique minimum. There
\[
R(1,\ldots,1)=\frac{r!}{2^r}.
\]
At
\[
r=4
\]
this is
\[
\frac{24}{16}>1,
\]
and the sequence \(r!/2^r\) is strictly increasing for \(r\ge4\). Hence every such Segre product has degree greater than Euler characteristic.

This proves the complete classification.

## Verification
The bundled checker independently computes the degree from the multinomial formula and the Euler characteristic from the product formula.

It enumerates all unordered dimension tuples with
\[
1\le r\le6,
\qquad
1\le a_i\le10,
\]
and verifies that every case agrees with the symbolic classification above.

It also checks the coordinate-growth identity exactly over the same finite range.

These computations are regression evidence only. The infinite classification is proved by the exact ratio identity and the finite set of symbolic base cases.

## Relationship to prior work
Classical Segre geometry realizes
\[
\mathbb P^{a_1}\times\cdots\times\mathbb P^{a_r}
\]
as the variety of decomposable tensors. Modern archival work on Segre varieties studies their secant and identifiability geometry in precisely this arbitrary-product setting.

The degree formula itself is the elementary intersection number of the Segre hyperplane class
\[
h_1+\cdots+h_r,
\]
while the Euler characteristic is the product of the Euler characteristics of the factors.

The comparison between these two canonical invariants appears to be much less emphasized. Targeted searches for Segre degree versus Euler characteristic, multinomial-versus-cell-count formulations, and exact equality cases did not locate the complete classification above. Nearby literature and database records concern secant varieties, dual degrees, hyperdeterminants, coisotropic degrees, or Euclidean-distance degrees rather than this primal degree–Euler comparison.

## Limitations
The theorem concerns the standard Segre polarization only. Segre--Veronese embeddings have different projective degrees and need not obey the same phase diagram.

Factors of dimension zero are excluded; including them only inserts trivial point factors.

The proof is elementary once the two standard closed formulas are compared, so an older or unindexed source may contain the same classification as an exercise or folklore observation.

## References
Hirotachi Abo, Giorgio Ottaviani, and Chris Peterson, *Induction for secant varieties of Segre varieties*, arXiv:math/0607191, first submitted 7 July 2006; *Transactions of the American Mathematical Society* 361 (2009), 767--792, DOI 10.1090/S0002-9947-08-04725-9.

Cristiano Bocci and Luca Chiantini, *On the identifiability of binary Segre products*, arXiv:1105.3643, first submitted 18 May 2011; *Journal of Algebraic Geometry* 22 (2013), 1--11.
