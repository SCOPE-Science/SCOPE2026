# A fourteen-to-fifteen-vertex cutoff for centroid-optimal simplex barycentric Lipschitz extension

## Finding

For each integer \(n\ge3\), take the \(n\) vertices \(V_n=\{v_1,\ldots,v_n\}\) of a regular Euclidean simplex of side length \(1\). For every nonempty subset \(S\subseteq[n]\), let \(c_S=|S|^{-1}\sum_{i\in S}v_i\) be its face centroid. Write \(X_n=\{c_S:\varnothing\ne S\subseteq[n]\}\); in particular, \(X_n\) contains all original vertices and the full centroid.

Let \(\lambda_n\) be the least norm of a **real-linear** right inverse to restriction from \(\operatorname{Lip}(X_n)/\mathbb R\) to \(\operatorname{Lip}(V_n)/\mathbb R\), where both spaces use the inherited Euclidean metric and the usual Lipschitz seminorm. Then

\[
\boxed{\lambda_n=\sqrt{\frac{2(n-1)}{n}}\quad(3\le n\le14).}
\]

This minimum is attained by positive, permutation-equivariant operators assigning rational weights to every face centroid, simultaneously at all face ranks. **For each integer \(n\ge15\), the equality fails strictly:**

\[
\boxed{\lambda_n\ge
\frac{1-1/n}{\sqrt{3/7}+\frac17\sqrt{(n-7)/(14n)}}
>\sqrt{\frac{2(n-1)}{n}}.}
\]

The cutoff refers to **vertices**, not ambient dimension: fourteen original vertices form a thirteen-dimensional simplex, whereas fifteen form a fourteen-dimensional one. At the first failing size, the displayed lower bound is approximately \(1.367448176616\), compared with centroid-only value \(1.366260102128\). The obstruction arises already from adding the seven-vertex face centers and the full centroid, rather than from all face ranks interacting.

## Assumptions and scope

The metric is Euclidean, and the target values are real. Extension operators preserve prescribed vertex values and are linear in those values, including modulo additive constants. They are not required in advance to be positive or symmetric. The original vertices are an equilateral metric of side \(1\). All distinct nonempty subsets give distinct barycenters because the vertices are affinely independent.

The parameter \(n\) counts the original vertices. The positive statement covers the full nonempty-face barycentric subdivision vertex set for every \(3\le n\le14\). The negative statement covers all \(n\ge15\) but supplies a lower bound, not an exact minimax constant.

## Proof

**1. Norm reduction.** Any linear constant-preserving extension is represented at each \(c_S\) by a signed coefficient measure \(\mu_S=\sum_i w_{S,i}\delta_{v_i}\) of total mass \(1\); the original vertices have \(\mu_{\{i\}}=\delta_{v_i}\). On the equilateral vertex set, the Kantorovich–Rubinstein norm of a mass-zero coefficient vector \(z\) is exactly \(\frac12\sum_i|z_i|\). Consequently,

\[
\|E\|=\max_{S\ne T}
\frac{\frac12\sum_i|w_{S,i}-w_{T,i}|}{\|c_S-c_T\|_2},
\qquad
\|c_S-c_T\|_2^2=
\frac{|S|+|T|-2|S\cap T|}{2|S||T|}.
\]

The latter metric identity follows because, for barycentric coefficients summing to zero, the squared Euclidean norm is half the sum of their squares.

**2. Unconditional centroid lower bound.** Average any candidate extension over permutations of the vertices; this preserves its extension property and cannot increase its norm. The full centroid is fixed by every permutation, so its averaged coefficient measure is \(u=n^{-1}\sum_i\delta_{v_i}\). For every original vertex the transport distance to \(u\) is \(1-1/n\), whereas its Euclidean distance to the centroid is \(\sqrt{(n-1)/(2n)}\). Thus

\[
\lambda_n\ge\frac{1-1/n}{\sqrt{(n-1)/(2n)}}
=\sqrt{\frac{2(n-1)}{n}}=:\,C_n.
\]

**3. Obstruction at seven-vertex faces.** For \(n\ge8\), averaging makes the measure of each seven-vertex face constant with coefficient \(a\) on the seven incident vertices and coefficient \(b\) outside. The test function equal to \(1\) at one incident vertex and \(0\) elsewhere gives

\[
1-a\le\lambda_n\sqrt{3/7}.
\]

The test function equal to \(1\) on all seven incident vertices and \(0\) elsewhere, compared with the full centroid, gives

\[
7a-7/n\le\lambda_n\sqrt{\frac{n-7}{14n}}.
\]

These are valid for **signed** coefficients as well: each follows from the absolute-value Lipschitz operator inequality after discarding its absolute value in the stated direction. Adding the first inequality to one-seventh of the second gives

\[
\lambda_n\ge B_n:=
\frac{1-1/n}{\sqrt{3/7}+\frac17\sqrt{(n-7)/(14n)}}.
\]

Set \(y=\sqrt{1-7/n}\). Direct simplification yields

\[
\frac{B_n}{C_n}=
\frac{\sqrt{6+y^2}}{\sqrt6+y/7}.
\]

As \(y>0\), the fraction is strictly greater than \(1\) precisely when \(y^2>49/96\), equivalently \(n>672/47\). Therefore it is strictly greater than \(1\) at every integer \(n\ge15\), and not so for \(n\le14\). This proves the claimed *unconditional obstruction*, including all nonsymmetric and signed extensions.

**4. Exact upper certificates for \(3\le n\le14\).** The accompanying standalone checker `verify_barycentric.py` contains, for each integer \(n\) in this range, an explicit vector \(A_{n,2},\ldots,A_{n,n-1}\) of integers, together with denominator \(10^7\). Write \(a_{n,k}=A_{n,k}/10^7\), \(b_{n,k}=(1-ka_{n,k})/(n-k)\). The extension is

\[
(E_nf)(c_S)=
\begin{cases}
f(v_i),&S=\{i\},\\
\frac1n\sum_i f(v_i),&|S|=n,\\
a_{n,k}\sum_{i\in S}f(v_i)+b_{n,k}\sum_{i\notin S}f(v_i),&k=|S|\in\{2,\ldots,n-1\}.
\end{cases}
\]

All coefficients are rational, nonnegative, and sum to \(1\). To check **all** distinct point pairs, set \(k=|S|\), \(l=|T|\), and \(t=|S\cap T|\). The four intersection blocks have multiplicities \(t,k-t,l-t,n-k-l+t\). The coefficient difference is constant on each block. Hence the norm condition \(\|E_n\|\le C_n\) is *equivalent*, with no estimation, to the finite rational inequalities

\[
\left[\frac12\sum_{(m,i,j)}m\left|w_{n,k}(i)-w_{n,l}(j)\right|\right]^2
\le\frac{(n-1)(k+l-2t)}{nkl},
\]

where \(w_{n,k}(i)\) means the in-face or out-of-face rational coefficient, and the sum is over those four blocks. The checker enumerates every integer triple \(1\le k\le l\le n\), \(\max(0,k+l-n)\le t\le\min(k,l)\), excluding \(k=l=t\), which represents identical points. It compares both sides with Python `Fraction`, i.e. **exact integer arithmetic after clearing denominators**, without floating point, optimization calls, probabilistic sampling, or unresolved inequalities. It verifies 1,489 distinct nonidentical symmetry-orbit cases over \(n=3,\ldots,14\), including the coefficient nonnegativity identities. Thus \(\lambda_n\le C_n\) for every required \(n\), completing equality with Step 2.

## Verification

Run `python3 verify_barycentric.py` from a directory containing the standalone file. Only the Python standard library is needed. The proof certificate verifies respectively \(6,13,23,37,55,78,106,140,180,227,281,343\) nonidentical point-pair orbit inequalities for \(n=3,\ldots,14\). It reports 1,489 exact passes and the rational test \(1-7/14<49/96<1-7/15\). Its twelve equalities are exactly the forced vertex–full-centroid orbit, one for each \(n\).

The explicit finite certificate proves the finite affirmative range by exhaustive symmetry classification, not by a numerical experiment. The negative range is proved symbolically for all integers \(n\ge15\), independently of the code. No numerical solver, unpublished external certificate, or individual historical run is required to check the package.

## Relationship to prior work

Bruè, Di Marino and Stra (2018), especially their Theorem 4.1, construct general linear Lipschitz extensions by random projections, without an exact all-face barycentric simplex constant. Basso (2021), especially his definitions of finite linear extension constants and relative Lipschitz-free projections, supplies the correct operator-norm framework but no fourteen-to-fifteen-face threshold. Earlier fixed-cardinality simplex-face interpolation formulas, where all added face centroids have the **same rank**, do not imply simultaneous compatibility across every rank. In particular, a sharp operator for each individual rank is not necessarily a single operator for their union; the new negative half demonstrates why such gluing needs proof. A targeted search for synonymous full-barycentric and face-centroid formulations found no covering theorem; this is bibliographic evidence, not proof of uniqueness or novelty.

## Limitations

The theorem assumes the exact inherited Euclidean metric and real scalar functions, and it does not classify all optimal operators. For \(n\ge15\), the displayed lower bound need not be the true optimal norm, and no all-dimensional formula for \(\lambda_n\) is claimed. The affirmative part uses a finite computer-checkable exact rational certificate, not a closed-form interpolation family uniformly covering arbitrary \(n\). Independent mathematical review has not been performed. Less-indexed literature may contain equivalent prior calculations.

## References

1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and C¹ extension operators through random projection*, initial public arXiv posting 23 January 2018, arXiv:1801.07533, https://arxiv.org/abs/1801.07533. See Sections 3 and 4.1, Theorem 4.1.
2. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, initial public arXiv posting 29 April 2021, arXiv:2104.14238, https://arxiv.org/abs/2104.14238. See Sections 1.1–1.2, Theorems 1.2 and 1.4, and the finite-metric linear programming framework.
