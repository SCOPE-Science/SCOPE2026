# Sharp simultaneous Lipschitz interpolation on all regular-simplex faces and a seventeen-vertex extremum

## Finding

Let \(n\ge4\), let \(3\le k\le n-1\), and let \(V=\{v_1,\ldots,v_n\}\) be the vertices of a side-one regular Euclidean simplex. Write \(c_S=k^{-1}\sum_{i\in S}v_i\) for every \(k\)-element subset \(S\subseteq\{1,\ldots,n\}\), and put \(X_{n,k}=V\cup\{c_S:|S|=k\}\), with ambient Euclidean distances. The minimum norm \(\Lambda_{n,k}\) among **all real-linear right inverses** to restriction \(\operatorname{Lip}(X_{n,k})/\mathbb R\longrightarrow\operatorname{Lip}(V)/\mathbb R\) is

\[
\boxed{\Lambda_{n,k}=\begin{cases}
\dfrac{n-1}{q+kp},&n-k=1,\\[5pt]
\dfrac{k\sqrt r\,(n-1)}{n-k+nk p\sqrt r},&n-k\ge2,
\end{cases}}
\]

where \(p=\sqrt{(k-1)/(2k)}\), \(q=\sqrt{(k+1)/(2k)}\), and \(r=\min\{k,n-k\}\). The infimum is attained by a **positive permutation-equivariant** operator, unique within the permutation-equivariant class. It improves strictly upon the naive equal-weight face average.

For each fixed \(k\ge3\), the sharp supremum over \(n\ge k+1\) is
\[
L_k=\lim_{n\to\infty}\Lambda_{n,k}=\frac{k\sqrt k}{1+k\sqrt{(k-1)/2}}.
\]
Its unique maximizing integer face cardinality is \(k=17\); consequently
\[
\boxed{\sup_{n\ge4,\;3\le k\le n-1}\Lambda_{n,k}
=\frac{17\sqrt{17}}{1+34\sqrt2}\approx1.4280386843726.}
\]
No finite simplex attains this supremum. This nonmonotone face-cardinality extremum is distinct from the previously treated edge-midpoint case \(k=2\).

## Assumptions and scope

All spaces are real and finite; distances on \(X_{n,k}\) are **Euclidean chord distances**, not the graph distance of the Johnson graph. Functions are scalar-valued and measured in the Lipschitz seminorm. Linear operators are understood on the quotient by constant functions, and the restriction right-inverse condition fixes every original vertex value. The point sets include **all** \(k\)-face barycenters simultaneously. The asserted minimum is over arbitrary real-linear extensions, without imposing positivity or symmetry as an assumption. The Euclidean simplex has \(n\) vertices, hence geometric dimension \(n-1\), while \(k\) counts vertices of each face.

## Proof

**1. Reduction to finite transportation norms.** Any right inverse can be represented by coefficient measures \(\mu_x=\sum_{i=1}^n w_i(x)\delta_{v_i}\) with \(\sum_iw_i(x)=1\); at \(v_i\), this measure is \(\delta_{v_i}\). This normalization is legitimate because the right inverse fixes vertices and sends constant vertex data to the same constant at every added point. For any signed coefficients summing to zero on the unit equilateral metric \(V\), Kantorovich--Rubinstein duality gives the exact dual norm \(\frac12\sum_i|w_i|\). Thus the extension-operator norm is exactly
\[
\max_{x\ne y\in X_{n,k}}\frac{\|\mu_x-\mu_y\|_{\mathrm{KR}}}{\|x-y\|_2}.
\]
Averaging any extension over all vertex permutations does not increase its norm and still extends vertex data. Therefore a minimizer may be assumed permutation-equivariant. For such an extension there exist real \(a,b\) with \(ka+(n-k)b=1\) and
\[
\mu_{c_S}=a\sum_{i\in S}\delta_{v_i}+b\sum_{i\notin S}\delta_{v_i},\qquad a=\frac{1-(n-k)b}{k}.
\]

**2. All point-pair constraints.** Place \(v_i=(e_i-n^{-1}\mathbf1)/\sqrt2\) in the zero-sum subspace of \(\mathbb R^n\). Then two vertices are distance \(1\). A vertex inside its face is distance \(p\) from its centroid, while a vertex outside is distance \(q\). If two \(k\)-sets \(S,T\) differ by \(t=|S\setminus T|\), then \(\|c_S-c_T\|_2=\sqrt t/k\) and \(\|\mu_{c_S}-\mu_{c_T}\|_{\mathrm{KR}}=t|a-b|\). The largest feasible \(t\) is \(r=\min\{k,n-k\}\).

For \(0\le b\le1/n\), we have \(a\ge b\ge0\). The complete list of potentially maximal ratios is
\[
A(b)=\frac{k-1+(n-k)b}{kp},\qquad
B(b)=\frac{1-b}{q},\qquad
C(b)=\sqrt r\,(1-nb),\qquad 1.
\]
These respectively come from a vertex *inside* a face, a vertex *outside* a face, two centroids at maximum symmetric difference, and two vertices. The first increases and the next two decrease with \(b\). In fact \(A(0)<B(0)<\sqrt2\) and \(A(1/n)>B(1/n),C(1/n)\). For \(b<0\), if \(r\ge2\), then the centroid-pair ratio is at least \(\sqrt r\), larger than the optimum found below; when \(r=1\), the outside-vertex ratio is at least \(1/q\), again larger. For \(b>1/n\), the inside-vertex ratio is at least \((1-a)/p\ge A(1/n)\), larger than the below optimum. Hence no discarded real parameter can improve the minimum, even if its weights are signed.

**3. Exact minimax and positivity.** Define \(b_{AB}\) by \(A(b_{AB})=B(b_{AB})\), and \(b_{AC}\) by \(A(b_{AC})=C(b_{AC})\). Both lie strictly between \(0\) and \(1/n\). Their crossing values are
\[
\lambda_{AB}=\frac{n-1}{(n-k)q+kp},\qquad
\lambda_{AC}=\frac{k\sqrt r\,(n-1)}{n-k+nk p\sqrt r}.
\]
The minimax of the four ratios equals \(\max\{\lambda_{AB},\lambda_{AC}\}\); the constant \(1\) is smaller. Elementary cross-multiplication shows \(\lambda_{AC}>\lambda_{AB}\) precisely when \(\sqrt r>p+q\). Since \(p^2+q^2=1\), \(1<p+q<\sqrt2\). Accordingly, \(r=1\) gives the \(AB\) crossing, whereas every \(r\ge2\) gives the \(AC\) crossing. This proves the stated piecewise formula. Explicit optimal weights are \(a=(1-(n-k)b)/k\), with
\[
b=\begin{cases}
\dfrac{kp-(k-1)q}{q+kp},&n-k=1,\\[5pt]
\dfrac{kp\sqrt r-(k-1)}{n-k+nk p\sqrt r},&n-k\ge2.
\end{cases}
\]
In both cases \(0<b<1/n<a\), so the operator is positive and its minimizing equivariant parameter is unique. At \(b=0\), the naive face average has norm \(1/q\) when \(r=1\), and \(\sqrt r\) when \(r\ge2\). Each is strictly greater than the proved optimum.

**4. Fixed-cardinality limit and global extremum.** For \(n=k+1\), \(\Lambda_{n,k}=k/(q+kp)<k/(kp+1/\sqrt k)\), because \(q>1/\sqrt k\). For \(n=k+t\) with real \(2\le t\le k\), the second branch becomes
\[
\frac{k(k+t-1)}{kp(k+t)+\sqrt t}.
\]
Its derivative has the sign of \(kp+(t-k+1)/(2\sqrt t)>0\), using \(kp=\sqrt{k(k-1)/2}>(k-3)/(2\sqrt2)\). For \(n\ge2k\), the same expression equals \(k(n-1)/(nkp+(n-k)/\sqrt k)\), whose derivative has the sign of \(kp-(k-1)/\sqrt k>0\). Thus the fixed-\(k\) supremum is its strict limit \(L_k\), and no finite \(n\) attains it.

Rewrite \(L_k=\sqrt2/h(k)\), where \(h(x)=\sqrt{1-1/x}+\sqrt2\,x^{-3/2}\). For \(x\ge3\), direct differentiation shows \(h\) decreases until \(x=9+3\sqrt7\in(16,17)\) and increases thereafter. The only remaining integer comparison is \(h(17)<h(16)\), equivalently \(L_{17}>L_{16}\). One exact rational certificate for that comparison uses \(4.123105625<\sqrt{17}<4.123105626\), \(1.414213562<\sqrt2<1.414213563\), and \(5.477225575<\sqrt{30}<5.477225576\); squaring integer numerators verifies these enclosures, and they give
\[
\frac{17(4.123105625)}{1+34(1.414213563)}>
\frac{64}{1+8(5.477225575)}.
\]
Therefore the unique integer maximizer is \(k=17\), with the claimed sharp unattained global supremum.

## Verification

The accompanying `verify.py` independently evaluates every point-pair coefficient norm for all \(4\le n\le9\) and \(3\le k\le n-1\), checks the two coefficient regimes, and reproduces the exact rational interval proof isolating \(k=17\). It also checks strict improvement over face averaging. A separate optional `verify_lp.py` formulates the **unrestricted, nonsymmetrized** finite linear program using all Boolean extreme Lipschitz vertex data, and was run successfully for \((n,k)=(4,3),(5,3),(5,4),(6,3)\). These finite tests supplement, not replace, the proof for arbitrary integers.

## Relationship to prior work

Bruè--Di Marino--Stra (2018) give general linear Lipschitz extension operators via random projections, without these exact simultaneous face-centroid constants. Albiac--Ansorena--Cúth--Doucha (2020), Lemma 2.7, identify such extension questions with complementability in Lipschitz-free spaces, but do not determine this simplex minimax. Borodachov (2022) treats pointwise spline recovery on simplices from vertex values **and derivatives** for a second-derivative-bounded function class, a different objective. An earlier calculation for **edge midpoints only** (\(k=2\)) yields special cases of the pair-orbit method but contains no claim for \(k\ge3\), no global face-size optimization, and no integer peak at \(17\). The new result addresses all higher-dimensional equal-cardinality faces and locates the globally extremal cardinality.

## Limitations

The theorem concerns scalar, real-linear extensions on a side-one regular Euclidean simplex and the discrete set of barycenters of faces of one fixed cardinality. It does not determine constants for mixed face cardinalities, all points of the simplex, arbitrary nonregular simplices, or Banach-valued extensions. Symmetry establishes existence and uniqueness only within the equivariant class, not uniqueness among all optimal operators. A prior equivalent all-face result in poorly indexed literature cannot be categorically excluded by searches; independent mathematical validation has not been performed.

## References

1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533, first version 2018-01-23, Theorem 4.1 and Section 3. https://arxiv.org/abs/1801.07533
2. F. Albiac, J. L. Ansorena, M. Cúth, M. Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555, first version 2020-05-13, Lemma 2.7. https://arxiv.org/abs/2005.06555
3. S. V. Borodachov, *Pointwise optimal multivariate spline method for recovery of twice differentiable functions on a simplex*, arXiv:2212.11070, first version 2022-12-21, Sections 1--2. https://arxiv.org/abs/2212.11070
