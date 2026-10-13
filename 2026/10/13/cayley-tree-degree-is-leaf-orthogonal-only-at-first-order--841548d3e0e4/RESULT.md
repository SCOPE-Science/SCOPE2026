# Cayley-tree degree is leaf-orthogonal only at first order

## Finding

Let \(T_n\) be uniformly distributed over the \(n^{n-2}\) labeled trees on \([n]\), with \(n\ge4\). Fix one vertex \(v\). Let
\[
D_{n,v}
\]
be its degree,
\[
L_n
\]
the total number of leaves, and put
\[
N_{n,v}=D_{n,v}-1.
\]

Write
\[
m=n-2,
\qquad
a=\frac{n-1}{n}.
\]
Then the exact mixed probability generating function is
\[
\boxed{
\mathbb E\!\left[L_n z^{N_{n,v}}\right]
=
a^m
+
(n-1)\left(\frac{n-2+z}{n}\right)^m.
}
\tag{1}
\]

This yields an explicit conditional leaf profile. With
\[
b=\frac{n-2}{n-1},
\]
\[
\boxed{
\mathbb E[L_n\mid N_{n,v}=0]
=
1+(n-1)b^m,
}
\tag{2}
\]
while for
\[
1\le k\le m,
\]
\[
\boxed{
\mathbb E[L_n\mid N_{n,v}=k]
=
(n-1)b^{m-k}.
}
\tag{3}
\]

The conditional mean therefore has a one-step valley:
\[
\mathbb E[L_n\mid N_{n,v}=1]
<
\mathbb E[L_n\mid N_{n,v}=0],
\tag{4}
\]
but
\[
\mathbb E[L_n\mid N_{n,v}=k+1]
>
\mathbb E[L_n\mid N_{n,v}=k]
\qquad(1\le k<m).
\tag{5}
\]

For the falling factorial
\[
(x)_r=x(x-1)\cdots(x-r+1),
\]
every order has an exact covariance:
\[
\boxed{
\operatorname{Cov}\!\left((N_{n,v})_r,L_n\right)
=
\frac{(m)_r}{n^r}
a^{m-r}
\left[
(n-1)-na^r
\right],
\qquad
1\le r\le m.
}
\tag{6}
\]

At first order the bracket vanishes:
\[
\boxed{
\operatorname{Cov}(D_{n,v},L_n)=0.
}
\tag{7}
\]

At every higher factorial order it is strictly positive:
\[
\boxed{
\operatorname{Cov}\!\left((D_{n,v}-1)_r,L_n\right)>0,
\qquad
2\le r\le n-2.
}
\tag{8}
\]

For each fixed integer \(r\ge2\),
\[
\boxed{
\operatorname{Cov}\!\left((D_{n,v}-1)_r,L_n\right)
\longrightarrow
\frac{r-1}{e}.
}
\tag{9}
\]

The first nonlinear case is especially simple:
\[
\boxed{
\operatorname{Cov}(D_{n,v}^2,L_n)
=
\frac{(n-2)(n-3)(n-1)}{n^3}
\left(\frac{n-1}{n}\right)^{n-4}>0.
}
\tag{10}
\]

Thus a fixed vertex degree is exactly uncorrelated with the global leaf count, but this is only a first-order cancellation. The dependence is visible immediately at the second factorial moment and persists at every higher fixed factorial order.

## Assumptions and scope

The tree is uniform over labeled Cayley trees on the fixed vertex set \([n]\). The distinguished vertex is deterministic; by exchangeability its label is irrelevant.

The theorem concerns one fixed vertex against the total number of leaves. It does not assert independence: equations (2)--(5) explicitly show that the conditional mean of the leaf count depends on the degree.

The falling-factorial statement is finite and exact for every admissible \(n\) and \(r\). The limit (9) keeps \(r\) fixed while \(n\) tends to infinity.

## Proof

Use the Prüfer correspondence. A uniform labeled tree on \([n]\) corresponds to a word
\[
W=(W_1,\ldots,W_m),
\qquad
m=n-2,
\]
whose letters are independent and uniform on \([n]\).

Let
\[
N_i=\#\{t:W_t=i\}.
\]
The Prüfer degree rule gives
\[
D_{n,i}=1+N_i,
\]
and a vertex is a leaf exactly when its label is absent from the word. Therefore
\[
L_n=\sum_{j=1}^n\mathbf 1\{N_j=0\}.
\tag{11}
\]

Fix \(v\). Its own leaf contribution satisfies
\[
z^{N_v}\mathbf 1\{N_v=0\}
=
\mathbf 1\{N_v=0\},
\]
whose expectation is
\[
a^m.
\tag{12}
\]

For any \(j\ne v\), one Prüfer coordinate contributes weight \(z\) if it equals \(v\), weight \(0\) if it equals \(j\), and weight \(1\) otherwise. Independence therefore gives
\[
\mathbb E\!\left[
z^{N_v}\mathbf 1\{N_j=0\}
\right]
=
\left(\frac{n-2+z}{n}\right)^m.
\tag{13}
\]
Summing (12)--(13) over the leaf indicators in (11) proves (1).

For the conditional formulas, first suppose
\[
N_v=0.
\]
Then \(v\) itself is a leaf. Conditional on this event, all \(m\) Prüfer letters are independent and uniform on the other \(n-1\) labels. Hence each \(j\ne v\) is absent with probability
\[
b^m,
\]
which proves (2).

Now suppose
\[
N_v=k\ge1.
\]
The vertex \(v\) is not a leaf. Conditional on the \(k\) occurrences of \(v\), the remaining \(m-k\) letters are uniform on the other \(n-1\) labels, so each \(j\ne v\) is absent with probability
\[
b^{m-k}.
\]
This proves (3). Equations (4)--(5) follow because
\[
\mathbb E[L_n\mid N_v=1]-\mathbb E[L_n\mid N_v=0]
=
b^{m-1}-1<0
\]
and \(0<b<1\).

For the factorial covariances, fix
\[
1\le r\le m.
\]
The multinomial factorial moment is
\[
\mathbb E(N_v)_r
=
\frac{(m)_r}{n^r}.
\tag{14}
\]
The own-leaf term vanishes because
\[
(N_v)_r\mathbf 1\{N_v=0\}=0.
\]
For \(j\ne v\), choose an ordered \(r\)-tuple of distinct Prüfer positions and force those positions to equal \(v\). The remaining \(m-r\) positions must avoid \(j\). Thus
\[
\mathbb E\!\left[
(N_v)_r\mathbf 1\{N_j=0\}
\right]
=
\frac{(m)_r}{n^r}a^{m-r}.
\tag{15}
\]
Summing over the \(n-1\) labels different from \(v\),
\[
\mathbb E[(N_v)_rL_n]
=
(n-1)\frac{(m)_r}{n^r}a^{m-r}.
\tag{16}
\]

Also
\[
\mathbb E L_n=na^m.
\tag{17}
\]
Subtracting the product of (14) and (17) from (16) proves (6).

For \(r=1\),
\[
(n-1)-na=0,
\]
which gives (7). For \(r\ge2\),
\[
a^r<a=\frac{n-1}{n},
\]
so
\[
(n-1)-na^r>0,
\]
proving (8).

For fixed \(r\),
\[
\frac{(n-2)_r}{n^r}\longrightarrow1,
\qquad
a^{n-2-r}\longrightarrow e^{-1},
\]
and
\[
(n-1)-na^r
=
r-1+O(n^{-1}).
\]
This proves (9).

Finally,
\[
N_v^2=(N_v)_2+N_v.
\]
The first-order covariance is zero, so
\[
\operatorname{Cov}(D_{n,v}^2,L_n)
=
\operatorname{Cov}((N_v)_2,L_n).
\]
Putting \(r=2\) into (6) and simplifying
\[
(n-1)-n\left(\frac{n-1}{n}\right)^2
=
\frac{n-1}{n}
\]
gives (10).

## Verification

The accompanying checker exhaustively enumerates every Prüfer word for
\[
3\le n\le8.
\]

It reconstructs the occupancy vector, the distinguished-vertex degree, and the total leaf count directly from each word. It verifies the mixed generating identity at several exact rational values of \(z\), the complete conditional-mean profile, and every admissible factorial covariance in that range.

The exhaustive replay covers
\[
280391
\]
Prüfer words.

Finite enumeration is supplementary. The universal theorem follows from the Prüfer bijection and elementary multinomial counting.

## Relationship to prior work

Aldous studies uniform spanning trees and uniform labeled trees, with separate sections on leaves and vertex degrees. In the complete-graph specialization he notes the exact binomial law for the degree of a specified vertex. The inspected full text does not state a mixed degree-versus-total-leaves covariance or the factorial hierarchy (6).

Steele studies the total number of leaves in the uniform labeled-tree model and proves a central limit theorem through an exponential-family construction. This supplies classical context for the global leaf statistic but does not retain one distinguished vertex degree in the stated result.

Addario-Berry, Broutin, and Holmgren use uniformly random rooted labeled trees, equivalently conditioned Poisson Galton--Watson trees, as an exact finite model in their cutting process. Their work confirms the standard probabilistic object but concerns cutting statistics rather than the mixed degree/leaf law here.

Wagner's random-tree limit-theorem work is classified primarily under \(60C05\) and provides broad probability context for random tree parameters. The accepted claim is instead a finite exact Prüfer-occupancy identity.

A separate occupancy calculation can of course recover (6), because Prüfer words are uniform allocations of \(n-2\) balls to \(n\) boxes. The point of the result is the tree interpretation: the exact cancellation at degree order one, the nonmonotone conditional leaf profile, and the positive hierarchy at all higher factorial degree orders.

## Limitations

The result uses the uniform Cayley-tree law. Other random tree models generally do not have independent uniform Prüfer coordinates.

The covariance cancellation is specific to the first degree moment. It does not imply independence and does not extend to arbitrary monotone functions of the degree.

The theorem studies one distinguished vertex. Joint laws involving several fixed vertices and the leaf count require multivariate occupancy terms and are not claimed.

Because the proof is elementary once the Prüfer encoding is chosen, an equivalent identity may be implicit in older occupancy or labeled-tree enumeration literature. The originality claim is the explicit local-global cancellation and the all-order factorial covariance hierarchy.

## References

1. L. Addario-Berry, N. Broutin, and C. Holmgren, “Cutting down trees with a Markov chainsaw,” arXiv:1110.6455, first submitted 2011-10-28; later *Annals of Applied Probability* 24 (2014), 2297–2339.
2. D. J. Aldous, “The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees,” *SIAM Journal on Discrete Mathematics* 3 (1990), 450–465, DOI 10.1137/0403039.
3. J. M. Steele, “Gibbs' Measures on Combinatorial Objects and the Central Limit Theorem for an Exponential Family of Random Trees,” *Probability in the Engineering and Informational Sciences* 1 (1987), 47–59, DOI 10.1017/S0269964800000279.
4. S. Wagner, “Central Limit Theorems for Additive Tree Parameters with Small Toll Functions,” *Combinatorics, Probability and Computing* 24 (2015), 329–353, DOI 10.1017/S0963548314000443; published online 2014-09-08.
