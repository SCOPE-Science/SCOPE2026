# Exact leaf–Wiener covariance in random recursive trees
## Finding
Let \(T_n\), \(n\ge2\), be the standard random recursive tree on
\[
\{1,\ldots,n\}.
\]
For each \(j\ge2\), vertex \(j\) chooses its parent independently and uniformly from
\[
\{1,\ldots,j-1\}.
\]
Let \(L_n\) be the number of vertices of outdegree zero, and let
\[
W_n=\sum_{1\le u<v\le n}d(u,v)
\]
be the Wiener index.

Writing
\[
H_n=\sum_{k=1}^n\frac1k,
\]
the exact finite covariance is
\[
\boxed{
\operatorname{Cov}(L_n,W_n)
=
nH_n-\frac{n(n+5)}4+\frac12.
}
\]

It vanishes for \(n=2,3\) and is strictly negative for every \(n\ge4\). In particular,
\[
\operatorname{Cov}(L_n,W_n)
=
-\frac{n^2}{4}+n\log n+O(n).
\]

For the mean unordered-pair distance
\[
\bar d_n=\frac{2W_n}{n(n-1)},
\]
one obtains
\[
\boxed{
\operatorname{Cov}(L_n,\bar d_n)
=
\frac{2}{n(n-1)}
\left(
nH_n-\frac{n(n+5)}4+\frac12
\right)
\longrightarrow-\frac12.
}
\]
Thus the negative association between leaf abundance and pairwise spread survives the natural pair-count normalization.

The calculation is closed by the auxiliary leaf-transmission statistic
\[
S_n
=
\sum_{v:\,v\text{ is a leaf}}
\sum_{u=1}^n d(u,v).
\]
Its exact mean is
\[
\boxed{
\mathbb E S_n
=
n(n+1)H_{n-1}
-
\frac{(n-1)(7n+6)}4.
}
\]

## Assumptions and scope
Leaves mean vertices of outdegree zero in the rooted recursive tree. This is the convention used in the standard leaf-count process; for \(n\ge2\) the root is never such a leaf.

The Wiener index is the sum of graph distances over unordered vertex pairs. All edges have unit length.

The theorem concerns the standard uniform recursive tree. It does not claim the same formula for plane-oriented recursive trees, preferential-attachment trees, random binary search trees, or uniformly labelled Cayley trees.

## Proof
For a deterministic rooted tree \(T_n\), write
\[
D_n(v)=\sum_{u=1}^n d(u,v)
\]
for the transmission of \(v\). Let \(U_n\) be the uniformly chosen attachment vertex for the new vertex \(n+1\), and set
\[
J_n=\mathbf 1\{U_n\text{ is a leaf of }T_n\}.
\]
The growth rules give
\[
L_{n+1}=L_n+1-J_n
\]
and
\[
W_{n+1}=W_n+n+D_n(U_n).
\]
Since
\[
\sum_{v=1}^nD_n(v)=2W_n,
\]
conditioning on \(T_n\) yields
\[
\mathbb E[W_{n+1}\mid T_n]
=
\left(1+\frac2n\right)W_n+n.
\]
Starting from \(W_2=1\), induction gives
\[
a_n:=\mathbb EW_n
=
n(n+1)H_n-2n^2.
\]
The standard leaf recursion gives
\[
\ell_n:=\mathbb EL_n=\frac n2,
\qquad n\ge2.
\]

Now introduce
\[
S_n=\sum_{v:\,v\text{ leaf}}D_n(v).
\]
When the new vertex attaches at \(U_n\), every surviving old leaf gains the distance from that leaf to \(U_n\) plus one, while the new vertex contributes transmission
\[
n+D_n(U_n).
\]
Averaging over \(U_n\) and accounting for deletion of the selected leaf when \(J_n=1\) gives the exact conditional recursion
\[
\mathbb E[S_{n+1}\mid T_n]
=
S_n+
\left(1-\frac1n\right)L_n
+n+\frac2nW_n.
\]
Taking expectations and using the formulas for \(a_n\) and \(\ell_n\) yields
\[
s_{n+1}
=
s_n+\frac{n-1}{2}+n+\frac{2a_n}{n},
\]
where \(s_n=\mathbb ES_n\) and \(s_2=1\). Induction gives
\[
s_n
=
n(n+1)H_{n-1}
-
\frac{(n-1)(7n+6)}4.
\]

Let
\[
c_n=\mathbb E[L_nW_n].
\]
Expanding
\[
(L_n+1-J_n)(W_n+n+D_n(U_n))
\]
and averaging over \(U_n\) uses
\[
\mathbb E[J_n\mid T_n]=\frac{L_n}{n},
\qquad
\mathbb E[D_n(U_n)\mid T_n]=\frac{2W_n}{n},
\qquad
\mathbb E[J_nD_n(U_n)\mid T_n]=\frac{S_n}{n}.
\]
Therefore
\[
c_{n+1}
=
\left(1+\frac1n\right)c_n
+(n-1)\ell_n
+\left(1+\frac2n\right)a_n
+n-\frac{s_n}{n}.
\]

Put
\[
b_n=\operatorname{Cov}(L_n,W_n)=c_n-\ell_na_n.
\]
Using
\[
a_{n+1}=\left(1+\frac2n\right)a_n+n,
\qquad
\ell_{n+1}=\frac{n+1}{2},
\]
the preceding recursion reduces to
\[
b_{n+1}
=
\frac{n+1}{n}b_n+\frac{a_n-s_n}{n}.
\]
The two exact means satisfy
\[
a_n-s_n
=
-\frac{(n-1)(n-2)}4,
\]
hence
\[
\boxed{
b_{n+1}
=
\frac{n+1}{n}b_n
-
\frac{(n-1)(n-2)}{4n}.
}
\]
Since \(b_2=0\), direct induction solves this recurrence as
\[
b_n
=
nH_n-\frac{n(n+5)}4+\frac12.
\]

The recurrence gives \(b_3=0\), and once \(n\ge3\) its forcing term is strictly negative; therefore \(b_n<0\) for every \(n\ge4\). The asymptotic statement follows from
\[
H_n=\log n+O(1).
\]
The formula for \(\bar d_n\) is a deterministic rescaling of \(W_n\).

## Verification
The accompanying `checker.py` independently enumerates every recursive-tree parent sequence through \(n=9\). It computes the leaf count, Wiener index, and leaf-transmission sum directly from each tree and checks their exact expectations and the covariance formula with rational arithmetic.

The same checker verifies the three closed recurrences over a large finite range using incremental exact harmonic numbers. These finite checks supplement, rather than replace, the all-\(n\) proof.

## Relationship to prior work
The Wiener index of random recursive trees has a substantial classical literature. Neininger derived its expectation, variance asymptotics, limit law, and joint asymptotics with internal path length. Later work on recursive-tree Wiener indices and tail bounds treats the Wiener index as a canonical global distance functional.

The leaf count is separately classical. Bryc, Minda, and Sethuraman formulate the leaf process in a uniform random recursive tree as the Markov chain in which a new leaf is created unless the attachment vertex is already a leaf; they develop laws of large numbers, central limits, and large deviations.

The inspected full Wiener-index source contains no leaf-count analysis, and the inspected full leaf-count source contains no Wiener-index analysis. The closest own comparison concerns the exact covariance between leaf count and internal path length. That result does not imply the present theorem: the Wiener update depends on the transmission of a uniformly selected attachment vertex, and closing the mixed moment requires the additional leaf-transmission statistic \(S_n\).

## Limitations
The proof uses the uniform attachment rule. In weighted recursive trees, both the leaf deletion probability and the transmission average are attachment-weighted, so the same one-dimensional closure does not hold automatically.

The result is a second-moment statement; it does not imply negative quadrant dependence, stochastic monotonicity of \(W_n\) conditional on \(L_n\), or a joint limit theorem.

Older recursive-tree or chemical-distance literature may contain the same mixed moment under different notation. Targeted searches did not locate it, but that remains the main originality risk.

## References
1. R. Neininger, “The Wiener Index of Random Trees,” *Combinatorics, Probability and Computing* 11 (2002), 587–597. DOI: 10.1017/S0963548302005321.
2. W. Bryc, D. Minda, and S. Sethuraman, “Large deviations for the leaves in some random trees,” arXiv:0809.4741; *Advances in Applied Probability* 41 (2009), 845–873.
3. G. O. Munsonius, “On tail bounds for random recursive trees,” arXiv:1106.3865; *Journal of Applied Probability* 49 (2012), 566–581. DOI: 10.1239/jap/1339878805.
