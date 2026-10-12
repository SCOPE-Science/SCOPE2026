# Catalan-triangle gap law for Dunn modal expansions of finite Gödel chains

## Finding

Let \(C_m\) be the \(m\)-element Gödel chain, \(m\ge2\), and put \(n=m-2\). Flaminio--Godo--Menchón--Rodriguez define Dunn Gödel algebras with operators (Dunn GAOs) by the two Dunn inequalities. The chain classification gives one exceptional expansion \(\Box\equiv1,\Diamond\equiv0\); every other ("normal") expansion is a pair of bounded chain endomorphisms with \(\Box x\le\Diamond x\) for all \(x\).

For a normal expansion define its **modal gap rank**
\[
g(\Box,\Diamond)=|\{x\in C_m\setminus\{0,1\}:\Box x<\Diamond x\}|.
\]
Then for \(0\le k\le n\), the number \(A_(7, 'files')\) of normal Dunn expansions of gap rank \(k\) is
\[
\boxed{A_(7, 'files')=\binom{2n+1}{n}
\left[\binom{n+k}{k}-\binom{n+k}{k-1}\right]}
\]
with \(\binom{n}{-1}=0\). Thus, after removing the common factor \(\binom{2n+1}{n}\), the complete rank distribution is Catalan's ballot triangle A009766.

For \(m=3,4,5,6\) the rank rows are
\[
(3,3),\quad(10,20,20),\quad(35,105,175,175),\quad
(126,504,1134,1764,1764).
\]

Summing the row gives
\[
\sum_kA_{m,k}=\binom{2n+1}{n}\operatorname{Cat}_{n+1}
=(2m-3)\operatorname{Cat}_{m-2}\operatorname{Cat}_{m-1},
\]
recovering the previously established total census.

If a normal expansion is chosen uniformly and \(K_m=g(\Box,\Diamond)\), while
\(J_m=n-K_m\) counts interior points on which the modalities coincide, then
\[
\Pr(K_m=k)=\frac{T(n,k)}{\operatorname{Cat}_{n+1}},
\qquad
T(n,k)=\binom{n+k}{k}-\binom{n+k}{k-1}.
\]
Consequently
\[
\mathbb E[J_m]=\frac{2n}{n+3},\qquad
\operatorname{Var}(J_m)=
\frac{2n(n+1)(2n+3)}{(n+3)^2(n+4)}.
\]
For each fixed \(j\ge0\),
\[
\boxed{\Pr(J_m=j)\longrightarrow\frac{j+1}{2^{j+2}}}
\quad(m\to\infty).
\]
Thus a random normal Dunn expansion has only \(O(1)\) coincidence points: their count converges to the negative-binomial law with mass \((j+1)/2^{j+2}\), mean \(2\), and variance \(4\).

## Proof

Write the interior values in increasing order. A normal pair is exactly two weakly increasing sequences
\[
0\le b_1\le\cdots\le b_n\le n+1,\qquad
0\le d_1\le\cdots\le d_n\le n+1
\]
with \(b_i\le d_i\), and the gap rank is the number of strict coordinates.

Let \(P_{r,N}(z)\) count such pairs of length \(r\), weighted by
\(z^{|\{i:b_i<d_i\}|}\). The exact prefix-sum recurrence for terminal
state \((u,v)\), \(u\le v\), is
\[
F_r(u,v)=z^{[u<v]}\sum_{0\le a\le u,\ a\le b\le v}F_{r-1}(a,b),
\qquad F_1(u,v)=z^{[u<v]}.
\]
Successive application of the hockey-stick identity to these two prefix sums, followed by the specialization \(N=n+1,r=n\), gives
\[
P_{n,n+1}(z)=\binom{2n+1}{n}
\sum_{k=0}^n
\left(\binom{n+k}{k}-\binom{n+k}{k-1}\right)z^k.
\]
The bracketed coefficient is the classical ballot number: by the reflection principle it counts words with \(n\) up-steps and \(k\) down-steps whose partial sums stay nonnegative. This proves the rank formula.

The row sum is \(\operatorname{Cat}_{n+1}\). For \(J=n-K\),
\[
\Pr(J=j)=
\frac{j+1}{n+1}
\binom{2n-j}{n-j}\bigg/\operatorname{Cat}_{n+1}.
\]
Elementary binomial summation gives
\[
\mathbb E[J]=\frac{2n}{n+3},\qquad
\mathbb E[J(J-1)]=\frac{6n(n-1)}{(n+3)(n+4)},
\]
hence the variance formula. Taking \(n\to\infty\) in the displayed exact probability gives \((j+1)/2^{j+2}\).

## Relationship to the literature

The 2021 Gödel-modal source defines Dunn GAOs and their relational representation but does not enumerate finite-chain expansions or refine them by pointwise modal disagreement. The immediately preceding owned result supplied the total Catalan product only. The new statement is strictly finer: it recovers every gap-rank fiber, its exact normalized law, and the limiting coincidence distribution.

Catalan's triangle itself is classical (OEIS A009766 / Bailey ballot numbers) and is not claimed as new. The novelty claim is the modal-algebraic identification of that triangle as the complete disagreement-rank distribution for finite Gödel-chain Dunn expansions.

Self-review: passed. Independent audit: not yet performed.
