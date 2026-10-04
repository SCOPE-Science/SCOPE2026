# Exact pointwise-James constancy threshold in \(\ell_p\) above the Hilbert exponent
## Finding
Let \(2<p<\infty\), let \(X=\ell_p\) over the real scalars, and for \(x\in S_X\) let \(J(x,X,t)\) denote the pointwise James type profile formed from the power mean of \(\lVert x-y\rVert\) and \(\lVert x+y\rVert\), with the continuous extension at a zero argument. Then the map
\[
x\longmapsto J(x,\ell_p,t)
\]
is constant on \(S_{\ell_p}\) if and only if \(t\ge p\).

More precisely, for every \(x\in S_{\ell_p}\) and every \(t\ge p\),
\[
J(x,\ell_p,t)=2^{1-1/t}.
\]
For every \(-\infty\le t<p\), the map is nonconstant. Writing
\[
u=2^{-1/p}(e_1+e_2),
\]
one has
\[
J(u,\ell_p,t)=2^{1-1/p},
\]
whereas
\[
J(e_1,\ell_p,t)<2^{1-1/p}.
\]
Thus \(t=p\) is the exact transition at which the pointwise profile loses its dependence on the base point.
## Assumptions and scope
The space is the real infinite-dimensional sequence space \(\ell_p\) with \(2<p<\infty\). For finite \(t\ne0\), the power mean is
\[
M_t(a,b)=\left(\frac{a^t+b^t}{2}\right)^{1/t},
\]
with \(M_0(a,b)=\sqrt{ab}\), \(M_{-\infty}(a,b)=\min\{a,b\}\), and the continuous extension when one argument is zero. The pointwise profile is
\[
J(x,X,t)=\sup_{y\in S_X}M_t(\lVert x-y\rVert,\lVert x+y\rVert).
\]
The statement does not claim pointwise constancy for \(1\le p<2\), nor does it classify finite-dimensional \(\ell_p^n\).
## Proof
Rincón-Villamizar records the global James type profile for \(p>2\):
\[
J(\ell_p,t)=
\begin{cases}
2^{1-1/p},& -\infty\le t\le p,\\
2^{1-1/t},& t\ge p.
\end{cases}
\]
The second branch is inherited from the earlier exact computation of Yang and Wang.

First suppose \(t\ge p\). For any \(x\in S_{\ell_p}\), choose \(y=x\). Then the two chord lengths are \(0\) and \(2\), so
\[
J(x,\ell_p,t)\ge M_t(0,2)=2^{1-1/t}.
\]
The global formula gives the reverse inequality. Therefore
\[
J(x,\ell_p,t)=2^{1-1/t}
\]
for every unit vector \(x\).

Now suppose \(-\infty\le t<p\). Put
\[
u=2^{-1/p}(e_1+e_2),\qquad v=2^{-1/p}(e_1-e_2).
\]
Both vectors are unit vectors and
\[
\lVert u+v\rVert=\lVert u-v\rVert=2^{1-1/p}.
\]
Hence
\[
J(u,\ell_p,t)\ge2^{1-1/p}.
\]
The first branch of the global formula gives equality:
\[
J(u,\ell_p,t)=2^{1-1/p}.
\]

It remains to show that the coordinate vector \(e_1\) has strictly smaller pointwise value. For \(y\in S_{\ell_p}\), replacing \(y\) by \(-y\) if needed only swaps the two chord lengths, so set \(a=|y_1|\in[0,1]\). The remaining coordinates have \(p\)-mass \(1-a^p\), and therefore the two chord lengths depend only on \(a\):
\[
A(a)^p=(1+a)^p+1-a^p,
\qquad
B(a)^p=(1-a)^p+1-a^p.
\]
Thus
\[
J(e_1,\ell_p,t)=\max_{0\le a\le1}M_t(A(a),B(a)).
\]
For \(0\le a<1\), strict Clarkson inequality for \(p>2\) gives
\[
\frac{A(a)^p+B(a)^p}{2}<2^{p-1},
\]
so
\[
M_t(A(a),B(a))\le M_p(A(a),B(a))<2^{1-1/p}.
\]
At \(a=1\), the two lengths are \(2\) and \(0\), and because \(t<p\),
\[
M_t(2,0)<2^{1-1/p}.
\]
The function of \(a\) is continuous on the compact interval \([0,1]\), including the continuous zero-argument convention. Since it is strictly below \(2^{1-1/p}\) at every point, its maximum is strictly below that number. Hence
\[
J(e_1,\ell_p,t)<2^{1-1/p}=J(u,\ell_p,t).
\]
This proves nonconstancy for every \(t<p\), and completes the classification. \(\square\)
## Verification
The proof is analytic. Its two external ingredients are the published global formula for \(J(\ell_p,t)\) and Clarkson's inequality, including strictness for the coordinate comparison when \(p>2\). The one-variable reduction for \(e_1\) is exact: all dependence on the remaining coordinates enters only through their total \(p\)-mass \(1-a^p\).

The accompanying script `artifacts/verify.py` independently samples the reduced one-variable profile for representative values of \(p\) and \(t<p\), and checks the exact high-parameter witness \(M_t(0,2)=2^{1-1/t}\). It is supplementary and is not used as a proof of the infinite statement.
## Relationship to prior work
Rincón-Villamizar introduced the pointwise James type profile, proved invariance along isometry orbits, and showed that convex transitivity forces the map \(x\mapsto J(x,X,t)\) to be constant. The same paper gives the global \(\ell_p\) profile in Example 3.7, but it does not classify when the pointwise map itself is constant on \(S_{\ell_p}\).

Yang and Wang computed the relevant global James type constants for \(\ell_p\) with \(p\ge2\); their invariant is global rather than based at a prescribed unit vector. The finding above identifies the exact parameter threshold for the newer pointwise invariant and shows that the global phase transition at \(t=p\) is also the pointwise constancy threshold.
## Limitations
The result is restricted to real infinite-dimensional \(\ell_p\) with \(p>2\). The complementary regime \(1\le p<2\), finite-dimensional \(\ell_p^n\), and general \(L_p(\mu)\) spaces are not classified here. The literature comparison found no statement implying this pointwise threshold, but originality remains subject to the usual risk of unindexed or differently phrased results.
## References
1. M. A. Rincón-Villamizar, *The pointwise James type constant*, Analysis Mathematica 49 (2023), 651–659. DOI: 10.1007/s10476-023-0221-7.
2. C. Yang and Y. Wang, *Some properties of James type constant*, Applied Mathematics Letters 25 (2012), 538–544. DOI: 10.1016/j.aml.2011.09.054.
3. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society 40 (1936), 396–414.
