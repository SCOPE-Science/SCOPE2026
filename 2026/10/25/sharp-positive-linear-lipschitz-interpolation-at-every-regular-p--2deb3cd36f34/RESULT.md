# Sharp positive linear Lipschitz interpolation at every regular-pentagon edge midpoint

## Finding

Let \(V=\{v_0,\ldots,v_4\}\) be the five vertices of a regular Euclidean pentagon of side length one, cyclically ordered, and let \(m_i=(v_i+v_{i+1})/2\), with indices modulo five. Equip \(X=V\cup\{m_0,\ldots,m_4\}\) with the inherited Euclidean metric. For a real-linear extension operator \(T:\mathbb R^V\to\mathbb R^X\) (identity on the original vertices), use the Lipschitz-seminorm operator norm. Then the minimum over **all** such operators, including operators with signed coefficients and no prescribed symmetry, is

\[
\boxed{\lambda_{\mathrm{Lip}}(V,X)=\frac{2(\varphi+1)}{1+2u+w}=1.0397164477425277525\ldots,}
\]
where
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
u=\frac{\sqrt{2\varphi+3}}2,\qquad
w=\frac{\sqrt{4\varphi+3}}2.
\]
The minimum is attained simultaneously at all five edge midpoints by one **positive, dihedrally equivariant** linear extension. Equivalently, the relative projection constant of the real Lipschitz-free space \(\mathcal F(V)\) in \(\mathcal F(X)\) has the boxed value. The additional midpoint-to-midpoint Lipschitz constraints are all strictly below the optimum in this construction.

## Assumptions and scope

For any finite metric space \(Y\), put
\[
\|f\|_{\mathrm{Lip}(Y)}=\max_{x\neq y\in Y}\frac{|f(x)-f(y)|}{d(x,y)}.
\]
The norm of an extension is the least \(L\) with \(\|Tf\|_{\mathrm{Lip}(X)}\le L\|f\|_{\mathrm{Lip}(V)}\) for all real data. An operator with finite norm necessarily preserves constants, so its coefficients at every new point sum to one. This is the same operator problem on pointed Lipschitz spaces after factoring out constants. No positivity or symmetry assumption is imposed on competing operators. All distances are Euclidean; no graph shortest-path metric is substituted.

The side and diagonal lengths among the original vertices are respectively \(1\) and \(\varphi\). For an edge midpoint \(m_0\), its distances from \(v_0,v_1\) are \(1/2\), those from \(v_2,v_4\) are \(u\), and the distance from \(v_3\) is \(w\). Among midpoint pairs, adjacent midpoints have distance \(\varphi/2\), and nonadjacent midpoints have distance \(\varphi^2/2\). These identities follow from the parallelogram identity and from the midpoint pentagon being a homothetic copy of the original pentagon with ratio \(\varphi/2\).

## Proof

**1. Universal lower bound.** The dihedral group acts isometrically on both \(V\) and \(X\). Average any finite-norm real-linear extension over its ten conjugates. This preserves the extension property and cannot increase its norm. The averaged operator has, at \(m_0\), a row of the form
\[
(Tf)(m_0)=a(f(v_0)+f(v_1))+b(f(v_2)+f(v_4))+c f(v_3),
\qquad 2a+2b+c=1.
\]
The coefficients here may be signed. For each original vertex \(v_j\), the distance function \(f_j(v)=d(v,v_j)\) is one-Lipschitz and vanishes at \(v_j\). Applying the midpoint-to-vertex constraints for \(j=0,4,3\), respectively, gives
\[
H_0=a+(1+\varphi)b+\varphi c\le\frac L2,
\]
\[
H_1=(1+\varphi)a+\varphi b+c\le Lu,
\]
\[
H_2=2\varphi a+2b\le Lw.
\]
These inequalities remain valid for signed coefficients: they arise by discarding the absolute value from a necessary Lipschitz inequality, not by assuming a positive transport plan. Since \(\varphi^2=\varphi+1\), one has the exact identity
\[
2H_0+2H_1+H_2=2(\varphi+1)(2a+2b+c)=2(\varphi+1).
\]
Therefore \(L(1+2u+w)\ge2(\varphi+1)\), proving the boxed lower bound for every extension.

**2. Positive matching construction.** Define
\[
\Delta=2(\varphi-1)(1+2u+w),
\]
\[
\begin{aligned}
a&=\frac{2\varphi u-1}{\Delta},\\
b&=\frac{2\varphi w+\varphi-2(\varphi+1)u}{\Delta},\\
c&=\frac{4\varphi u-2(\varphi+1)w}{\Delta}.
\end{aligned}
\]
These obey \(2a+2b+c=1\) and
\[
0<c<b<a,
\]
with approximate values \(a=0.48845308227908\), \(b=0.00964585959968\), and \(c=0.00380211624248\). Set the row at every other midpoint by cyclically shifting the displayed coefficients. This defines a linear extension which preserves all constants, is positive, and is equivariant under all pentagon symmetries.

The following exact numerator identities require only \(\varphi^2=\varphi+1\):
\[
\begin{aligned}
\Delta\,(2a+2b+c)&=\Delta,\\
\Delta H_0&=2\varphi,\\
\Delta H_1&=4\varphi u,\\
\Delta H_2&=4\varphi w.
\end{aligned}
\]
Also \(\lambda=4\varphi/\Delta\). Positivity permits the elementary transport estimate \(|(Tf)(m_i)-f(v_j)|\le\sum_k a_{ik}d(v_k,v_j)\|f\|_{\mathrm{Lip}(V)}\). The three possible vertex orbits therefore have exact quotients \(\lambda\), \(\lambda\), \(\lambda\), respectively. Every midpoint-to-original-vertex constraint is thus sharp but not exceeded.

**3. Simultaneous midpoint compatibility.** There are exactly two midpoint-pair orbits. For adjacent midpoints \(m_0,m_1\), the difference of the two positive vertex-weight distributions is transported by sending mass \(a-b\) from \(v_0\) to \(v_2\) and mass \(b-c\) from \(v_4\) to \(v_3\). The transport cost is
\[
\varphi(a-b)+(b-c)<\lambda\frac\varphi2=\lambda d(m_0,m_1).
\]
For nonadjacent midpoints \(m_0,m_2\), send mass \(a-c\) from \(v_0\) to \(v_3\) and mass \(a-b\) from \(v_1\) to \(v_2\). Its cost is
\[
\varphi(a-c)+(a-b)<\lambda\frac{\varphi^2}2=\lambda d(m_0,m_2).
\]
For any one-Lipschitz source function, these explicit transfers dominate the differences of weighted averages. The two strict inequalities follow by multiplying by \(\Delta>0\) and checking the positive radicals
\[
\begin{aligned}
R_1&=2\varphi^2-\bigl(\varphi(\Delta a-\Delta b)+\Delta b-\Delta c\bigr)>0,\\
R_2&=2\varphi^3-\bigl(\varphi(\Delta a-\Delta c)+\Delta a-\Delta b\bigr)>0.
\end{aligned}
\]
For complete exact sign checks, the rational brackets \(1.61803<\varphi<1.61804\), \(1.24860<u<1.24861\), and \(1.53884<w<1.53885\), each verified by squaring, already imply \(\Delta c>0\), \(\Delta(b-c)>0\), \(\Delta(a-b)>0\), and the two positive margins. The accompanying standard-library checker uses narrower outward rational intervals to certify all of these strict inequalities. The original vertex pairs have quotient at most one, and \(\lambda>1\), so every target-point pair is controlled. The lower and upper bounds coincide.

## Verification

Run `python3 pentagon_extension_verify.py`. The script uses the Python standard library, builds certified rational enclosures of all radicals using integer square roots, confirms positivity/order/strict midpoint-pair margins, and cross-checks normalization and the three saturated vertex orbits. Independently it enumerates all extreme one-Lipschitz potentials on the five vertices by signed spanning-tree tight constraints, obtains 70 distinct extreme potentials, and checks 2,450 new-point pair inequalities. The final output is `PENTAGON_EXTENSION_CERTIFICATE_OK`. The analytical identities and explicit transport plans above establish the exact theorem; finite computations are reproducibility checks, not substitute proofs.

## Relationship to prior work

Bruè, Di Marino and Stra (2018), especially their Theorem 4.1, construct linear extension operators on doubling metric subsets through random projections and provide general bounds, but not this ten-point exact constant. Ambrosio and Puglisi (2016) relate linear extensions to transportation and random projections. Basso (2017/2018) gives general extension bounds for finitely many added points with arbitrary Banach targets, not an optimal simultaneous real-linear operator. Basso (2021) defines \(\lambda_{\mathrm{Lip}}(V,X)\), identifies it with relative Lipschitz-free-space projection constants for finite source sets, and provides a general linear-programming method; the inspected statements do not evaluate the particular regular-pentagon midpoint configuration. A separately published regular-polygon result addresses adjoining **one center**, with a snowflake exponent, and hence neither gives the five distinct side-midpoint rows nor proves their pairwise compatibility. Existing explicit square, rectangle and regular-hexagon midpoint formulas similarly do not imply this odd fivefold case. This result's exact dual witness combination and two explicit couplings resolve that separate finite invariant.

## Limitations

The theorem is about real scalar-valued Lipschitz functions, a regular Euclidean pentagon, and simultaneous extension to its five side midpoints. It does not classify all optimizers, other polygon orders, arbitrary side-interior interpolation points, or vector-valued extensions. Searching cannot exclude every unindexed equivalent calculation; originality remains subject to independent bibliographic review. An independent mathematical audit has not been performed.

## References

1. E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533v1 (first public 2018-01-23), https://arxiv.org/abs/1801.07533.
2. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238v1 (first public 2021-04-29), https://arxiv.org/abs/2104.14238.
3. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (2016), https://arxiv.org/abs/1609.01450.
4. G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593v1 (first public 2017-07-20), https://arxiv.org/abs/1707.06593.
5. *A sharp snowflake threshold for simultaneous linear Lipschitz extensions from regular polygons*, publicly accessible result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-snowflake-threshold-for-simultaneous-linear-lipschitz-ex--55dc55bc9348.
