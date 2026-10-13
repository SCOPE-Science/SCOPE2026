# Vertex age creates a leaf-covariance phase transition in random recursive trees

## Finding

Consider the standard random recursive tree \(T_n\) on labels
\[
[n]=\{1,\ldots,n\}.
\]
For every \(j\ge2\), vertex \(j\) independently chooses a parent
\[
P_j\in\{1,\ldots,j-1\}
\]
uniformly.

Let \(L_n\) be the number of leaves, meaning vertices with no children. For a fixed nonroot vertex
\[
2\le v\le n,
\]
let \(D_{n,v}\) be its number of children. For a potential child \(j>v\), put
\[
A_{v,j}=\mathbf 1\{P_j=v\}.
\]

There is an exact local covariance law:
\[
\boxed{
\operatorname{Cov}(A_{v,j},L_n)
=
\frac{j-2v}{2(n-1)(j-2)}.
}
\tag{1}
\]

Thus a potential child born before time \(2v\) is negatively correlated with the final leaf count, the child born exactly at time \(2v\) is uncorrelated when that time exists, and every later potential child is positively correlated with the final leaf count.

Summing over all possible children gives
\[
\boxed{
\operatorname{Cov}(D_{n,v},L_n)
=
\frac1{n-1}
\left[
\frac{n-v}{2}
-
(v-1)\bigl(H_{n-2}-H_{v-2}\bigr)
\right],
}
\tag{2}
\]
where
\[
H_m=\sum_{k=1}^m\frac1k,
\qquad
H_0=0.
\]

For \(n\ge7\), define
\[
\tau_n
=
\min
\left\{
2\le v\le n-1:
\operatorname{Cov}(D_{n,v},L_n)\le0
\right\}.
\tag{3}
\]
Then
\[
\boxed{
\operatorname{Cov}(D_{n,v},L_n)>0
\quad\text{for }2\le v<\tau_n,
}
\tag{4}
\]
\[
\boxed{
\operatorname{Cov}(D_{n,\tau_n},L_n)\le0,
}
\tag{5}
\]
and
\[
\boxed{
\operatorname{Cov}(D_{n,v},L_n)<0
\quad\text{for }\tau_n<v<n.
}
\tag{6}
\]
The terminal vertex satisfies
\[
\operatorname{Cov}(D_{n,n},L_n)=0
\]
because its outdegree is identically zero.

The transition has a macroscopic limiting location. If
\[
\frac{v_n}{n}\longrightarrow x\in(0,1),
\]
then
\[
\boxed{
\operatorname{Cov}(D_{n,v_n},L_n)
\longrightarrow
c(x)
=
\frac{1-x}{2}+x\log x.
}
\tag{7}
\]

The function \(c\) has a unique zero in \((0,1)\),
\[
\boxed{
\rho
=
-\frac1{2W_{-1}(-e^{-1/2}/2)}
=
0.284668137040838\ldots,
}
\tag{8}
\]
where \(W_{-1}\) is the lower real branch of the Lambert \(W\)-function. Consequently,
\[
\boxed{
\frac{\tau_n}{n}\longrightarrow\rho.
}
\tag{9}
\]

So the direction of association between a labeled vertex's eventual degree and global leaf abundance depends sharply on its birth time: vertices born before about \(28.47\%\) of the growth horizon have positive degree–leaf covariance, while later nonterminal vertices have negative covariance.

## Assumptions and scope

The result uses the standard random recursive tree in which all parent choices are independent and uniform among earlier labels.

The degree \(D_{n,v}\) is the rooted outdegree, namely the number of children of \(v\). For nonroot vertices the ordinary undirected degree is \(D_{n,v}+1\), so its covariance with \(L_n\) is the same as in (2).

The phase transition is indexed by the deterministic birth label \(v\), not by a uniformly sampled vertex. The theorem does not assert independence when a displayed covariance vanishes.

The local formula (1) is stronger than the aggregate sign statement: it identifies the precise competition between destroying the possibility that \(v\) remains a leaf and protecting earlier vertices from being chosen by \(j\).

## Proof

For each vertex \(i\), let
\[
Y_i=\mathbf 1\{i\text{ is a leaf of }T_n\}.
\]
Then
\[
L_n=\sum_{i=1}^nY_i.
\]

For \(i\ge2\),
\[
\Pr(Y_i=1)
=
\prod_{k=i+1}^n
\left(1-\frac1{k-1}\right)
=
\frac{i-1}{n-1}.
\tag{10}
\]
The same formula gives
\[
\mathbb E L_n=\frac n2
\tag{11}
\]
for \(n\ge2\), since the root cannot be a leaf once vertex \(2\) is present.

Fix
\[
2\le v<j\le n.
\]
Because
\[
\Pr(A_{v,j}=1)=\frac1{j-1},
\]
the event \(A_{v,j}=1\) forces \(v\) not to be a leaf. Therefore
\[
\operatorname{Cov}(A_{v,j},Y_v)
=
-\frac{v-1}{(j-1)(n-1)}.
\tag{12}
\]

Now take
\[
2\le i<j,
\qquad
i\ne v.
\]
Conditioning on \(A_{v,j}=1\) guarantees that \(j\) did not choose \(i\). All later parent choices remain unchanged. Hence the single factor
\[
1-\frac1{j-1}
=
\frac{j-2}{j-1}
\]
disappears from the probability that \(i\) remains a leaf, and
\[
\Pr(Y_i=1\mid A_{v,j}=1)
=
\Pr(Y_i=1)\frac{j-1}{j-2}.
\]
It follows that
\[
\operatorname{Cov}(A_{v,j},Y_i)
=
\frac{i-1}{(n-1)(j-1)(j-2)}.
\tag{13}
\]

For \(i\ge j\), the leaf event \(Y_i\) depends only on parent choices made after time \(i\), so it is independent of \(A_{v,j}\).

Summing (12)--(13) over the leaf indicators gives
\[
\begin{aligned}
\operatorname{Cov}(A_{v,j},L_n)
&=
-\frac{v-1}{(j-1)(n-1)}
+
\frac{\sum_{i=2}^{j-1}(i-1)-(v-1)}
{(n-1)(j-1)(j-2)}\\
&=
\frac{j-2v}{2(n-1)(j-2)},
\end{aligned}
\]
which proves (1).

Since
\[
D_{n,v}
=
\sum_{j=v+1}^n A_{v,j},
\]
summing (1) yields
\[
\begin{aligned}
\operatorname{Cov}(D_{n,v},L_n)
&=
\frac1{2(n-1)}
\sum_{j=v+1}^n
\left(
1-\frac{2(v-1)}{j-2}
\right)\\
&=
\frac1{n-1}
\left[
\frac{n-v}{2}
-
(v-1)(H_{n-2}-H_{v-2})
\right],
\end{aligned}
\]
proving (2).

For the finite sign pattern, define the unscaled numerator
\[
F_n(v)
=
\frac{n-v}{2}
-
(v-1)(H_{n-2}-H_{v-2}).
\tag{14}
\]
Its first difference is
\[
F_n(v+1)-F_n(v)
=
\frac12+\frac1{v-1}
-
(H_{n-2}-H_{v-2}),
\tag{15}
\]
and the first differences themselves satisfy
\[
\bigl(F_n(v+2)-F_n(v+1)\bigr)
-
\bigl(F_n(v+1)-F_n(v)\bigr)
=
\frac1v>0.
\tag{16}
\]
Thus \(F_n\) is strictly discrete-convex.

At the right edge,
\[
F_n(n)=0,
\qquad
F_n(n-1)=-\frac12.
\tag{17}
\]
At the left edge,
\[
F_n(2)
=
\frac{n-2}{2}-H_{n-2}>0
\]
for every \(n\ge7\). The inequality holds at \(n=7\) directly, and thereafter its left side increases by
\[
\frac12-\frac1{n-1}>0.
\]

Strict convexity together with (17) now permits exactly one positive-to-nonpositive crossing before the terminal zero at \(v=n\). This proves (3)--(6).

Finally, suppose
\[
v_n/n\to x\in(0,1).
\]
The harmonic difference satisfies
\[
H_{n-2}-H_{v_n-2}
\longrightarrow
-\log x.
\]
Dividing the numerator in (2) by \(n\) therefore gives (7).

For
\[
c(x)=\frac{1-x}{2}+x\log x,
\]
one has
\[
c'(x)=\log x+\frac12,
\qquad
c''(x)=\frac1x>0.
\]
Also
\[
c(0+)=\frac12,
\qquad
c(1)=0.
\]
Strict convexity implies a unique additional zero \(\rho\in(0,1)\), and solving
\[
1-\rho+2\rho\log\rho=0
\]
gives (8). The finite single-crossing property and pointwise sign separation on either side of \(\rho\) imply (9).

## Verification

The accompanying checker uses exact rational arithmetic.

It exhaustively enumerates every recursive tree through \(n=9\), directly reconstructing the leaf count, every nonroot outdegree, and every potential-child attachment indicator. It verifies (1), (2), and the mean leaf count from the empirical laws.

It separately evaluates the harmonic formula through \(n=500\), verifies the strict discrete convexity and the complete finite sign pattern, and checks the convergence of the scaled threshold toward the constant in (8).

Finite enumeration is supplementary. The all-\(n\) result follows from the independent-parent calculation above.

## Relationship to prior work

Addario-Berry and Eslava study high degrees in random recursive trees and review a substantial literature on their degree profile. Their public manuscript uses the same recursive-tree model and defines a vertex degree as its number of children. Its primary classification is \(60C05\). The inspected full text does not discuss leaves or terminal vertices, and does not state a labeled-vertex degree covariance with a global leaf count.

Najock and Heyde give an early probability treatment of the number of terminal vertices in random recursive trees and derive its distribution. The accessible source establishes the leaf statistic as classical, but does not expose a covariance with the degree of a specified birth-time vertex.

Drmota and Hwang prove sharp sign changes for correlations between level sizes in the profile of a random recursive tree. That phenomenon is conceptually close to the age-dependent sign change here, but it concerns depth-profile counts rather than a labeled vertex's degree against the total number of leaves.

Janson studies asymptotic degree-count distributions in random recursive trees, including covariance matrices for global degree classes. Those global degree-count covariances do not retain the deterministic birth label \(v\), which is the parameter producing the threshold in (9).

Recent work on leaves in growing random trees also studies age-stratified leaf-related statistics, but its leaf-degree observable counts leaf neighbors of a vertex rather than the covariance between that vertex's total children and the global number of leaves.

## Limitations

The theorem is specific to the uniform recursive attachment rule. Preferential or weighted recursive trees change both the survival probability in (10) and the conditional protection term in (13).

The asymptotic threshold describes labels proportional to \(n\). Finer \(O(1)\) or logarithmic corrections to \(\tau_n\) are not claimed.

A zero covariance at the local time \(j=2v\), or at an exceptional finite aggregate threshold, does not imply independence.

Older joint-distribution work on recursive-tree degree and terminal-vertex statistics may contain an equivalent mixed moment under different notation. The accepted claim is the explicit local sign law, its exact aggregate harmonic formula, and the resulting birth-time phase transition.

## References

1. L. Addario-Berry and L. Eslava, “High degrees of random recursive trees,” arXiv:1507.05981, first submitted 2015-07-21; later *Random Structures & Algorithms* 52 (2018), 560–575.
2. D. Najock and C. C. Heyde, “On the number of terminal vertices in certain random trees with an application to stemma construction in philology,” *Journal of Applied Probability* 19 (1982), 675–680, DOI 10.2307/3213526.
3. M. Drmota and H.-K. Hwang, “Profiles of random trees: correlation and width of random recursive trees and binary search trees,” *Advances in Applied Probability* 37 (2005), 321–341, DOI 10.1239/aap/1118858628.
4. S. Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* 26 (2005), 69–83, DOI 10.1002/rsa.20046.
