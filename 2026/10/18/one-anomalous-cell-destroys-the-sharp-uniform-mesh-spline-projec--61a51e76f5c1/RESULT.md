# One anomalous cell destroys the sharp uniform-mesh spline projection bound

## Finding
For each real \(\tau>0\), form a bi-infinite partition of the real line with all consecutive knot gaps equal to \(1\), except for the gap from \(x_0=0\) to \(x_1=\tau\), whose length is \(\tau\). Let \(P_\tau\) be the \(L^2(\mathbb R)\)-orthogonal projection onto the closed space of square-integrable, continuous functions that are affine on every partition cell. It has a canonical bounded integral-kernel extension to \(L^\infty(\mathbb R)\).

**A one-cell rigidity threshold.** The sharp uniform-grid bound holds exactly at the unperturbed mesh:
\[
\|P_\tau\|_{L^\infty\to L^\infty}=2\quad\Longleftrightarrow\quad\tau=1,
\qquad
\|P_\tau\|_{L^\infty\to L^\infty}>2\quad(\tau\ne1).
\]
The strict inequality admits explicit, local witnesses. For a shortened exceptional cell \(0<\tau<1\), its endpoint \(x_0\) witnesses amplification above \(2\). For a lengthened cell \(\tau>1\), the immediately preceding knot \(x_{-1}\) witnesses amplification above \(2\). These statements do not assert that the displayed witnesses are global maximizers.

Writing \(\mathcal L_j(\tau)=\int_{\mathbb R}|K_\tau(x_j,y)|\,dy\) for the nodal Lebesgue function, \(s=\sqrt3\), and \(r=2-\sqrt3\), the exact witnesses are
\[
\mathcal L_0(\tau)-2=\frac{3\tau(1-\tau^2)}{(\tau+s)(s+3\tau)^2},
\]
\[
\mathcal L_{-1}(\tau)-2=\frac{2r}{3}\,
\frac{(\tau^2-1)(\tau+s/2)
 [\tau^2+(5s/3-1)\tau+1]}
 {(\tau+s/3)^2(\tau+s)
 [\tau^2+(2+2s/3)\tau+s]}.
\]
Both signs follow from positive factors. Reflection gives equivalent witnesses at \(x_1\) and \(x_2\).

## Assumptions and scope
The partition is \(x_j=j\) for \(j\le0\), and \(x_j=\tau+j-1\) for \(j\ge1\), with \(\tau\in(0,\infty)\) fixed. The hat basis \(\phi_j\) satisfies \(\phi_j(x_i)=\delta_{ij}\) and is supported on \([x_{j-1},x_{j+1}]\). The Hilbert space is the \(L^2\)-closure of finite linear combinations of these hats. The claimed operator norm is for the canonical bounded \(L^\infty\) extension. It is not a finite-interval result, a classification for arbitrary meshes, or a claim of exact global norm at \(\tau\ne1\).

The primary MSC2020 classification is **41A15** (spline approximation). Earlier finite-interval projection formulas and uniform-grid bounds are antecedents, not new results.

## Proof
**1. Invertible Gram operator.** Let \(h_j=x_{j+1}-x_j\). The Gram operator \(M_{ij}=\langle\phi_i,\phi_j\rangle\) is tridiagonal with \(M_{jj}=(h_{j-1}+h_j)/3\) and \(M_{j,j+1}=h_j/6\). Thus \(Q=6M\) has diagonal \(4\) away from \(0,1\), diagonal \(2(1+\tau)\) at \(0,1\), off-diagonal entries \(1\) away from the \(0\)--\(1\) edge and \(\tau\) on that edge. Alternating-sign conjugation makes all off-diagonal entries negative. It is symmetric, strictly diagonally dominant, and boundedly invertible on \(\ell^2(\mathbb Z)\). The hat representation is therefore a stable Riesz basis for the spline space. The tridiagonal inverse has exponentially decaying rows, so the projection kernel \(K_\tau(x,y)=\sum_{i,j}\phi_i(x)(M^{-1})_{ij}\phi_j(y)\) is pointwise well defined with integrable rows.

**2. Two exact Green rows.** Put \(G_{ij}=(-1)^{i+j}(Q^{-1})_{ij}\); these entries are positive. Define
\[
 s=\sqrt3,\quad r=2-s,\quad c=\frac1{2s},\quad
 a=\frac{s+2\tau}{(s+\tau)(s+3\tau)},\quad
 b=\frac{\tau}{(s+\tau)(s+3\tau)},\quad
 d=c+r^2(a-c).
\]
Direct substitution into the Jacobi recurrence shows
\[
 G_{0,j}=\begin{cases}a r^{-j},&j\le0,\\ b r^{j-1},&j\ge1;\end{cases}
\]
\[
 G_{-1,j}=\begin{cases}d r^{-1-j},&j\le-1,\\ ar,&j=0,\\ b r^j,&j\ge1.\end{cases}
\]
Indeed \(r+r^{-1}=4\); at the exceptional junction the first Green row satisfies \((s+2\tau)a-\tau b=1\) and \((s+2\tau)b-\tau a=0\). The second row satisfies \((4-r)d-ra=1\) at its source. All remaining coordinates obey the homogeneous recurrence, and the rows decay in both directions, giving uniqueness by invertibility.

**3. Exact absolute-integral sum.** For two adjacent nodal kernel values of opposite signs with magnitudes \(6u\) and \(6v\), the integral of their absolute linear interpolant over a cell of length \(h\) is
\[
3h\frac{u^2+v^2}{u+v}.
\]
Apply this formula to the two Green rows above, summing the exterior geometric tails. Using \((1+r^2)/(1-r^2)=2/s\), one obtains
\[
\mathcal L_0=2s(a+b)+3\tau\frac{a^2+b^2}{a+b},
\]
\[
\mathcal L_{-1}=2s(d+br)+3\frac{d^2+(ar)^2}{d+ar}
+3\tau r\frac{a^2+b^2}{a+b}.
\]
Rational simplification in the quadratic field \(\mathbb Q(\sqrt3)\) gives exactly the two factored expressions in the Finding. Their denominators are positive for every \(\tau>0\), and \(5s/3-1>0\), so the first witness is strictly above \(2\) for \(0<\tau<1\), while the second is strictly above \(2\) for \(\tau>1\).

**4. The unperturbed threshold.** At \(\tau=1\), \(G_{ij}=r^{|i-j|}/(2s)\). The same geometric absolute-integral calculation gives \(\mathcal L_j(1)=2\) for every knot. Between knots, \(K_1(x,\cdot)\) is a convex combination of the two endpoint kernels; its \(L^1\) norm is at most \(2\). Thus \(\|P_1\|_{\infty\to\infty}=2\). Conversely, at any knot the projection norm dominates its kernel absolute integral by approximating the sign of the kernel with bounded test functions. This completes both directions.

## Verification
The accompanying `verify.py` independently checks both factorizations and three critical Green recurrence identities as exact rational-function identities modulo \(s^2-3\). It also checks strict signs on representative rational distortions and compares explicit infinite-mesh local witness values against finite-mesh Gram inverses. The checker uses Python 3 and SymPy. These finite tests are reproducibility checks; the quantifier \(\tau>0\) is proved by the positive factorization and not by sampling.

## Relationship to prior work
Ciesielski and Kamont (2004), *The Lebesgue constants for the Franklin orthogonal system*, present a general nodal kernel formula for arbitrary finite spline partitions and obtain an exact sharp bound for a different half-mesh arrangement, consisting of a block of consecutive half-length cells followed by unit-length cells. Their equations (2.2), (2.11), and (2.12) supply the established Gram/kernel tools. The present claim treats a single arbitrary-length anomalous cell in an infinite otherwise uniform partition and determines the two-sided strict threshold and opposite local witness locations.

Passenbrunner (2011), *Monotonicity of the Lebesgue constant for equally spaced knots*, treats precisely uniform finite meshes and their approach to the constant \(2\). His periodic Franklin study treats a different, two-half-cell knot arrangement. Kayumov (2004) treats general boundedness of second-order \(L\)-spline orthoprojectors rather than these local defect formulas. We do not claim discovery of tridiagonal inversion, stability of general spline projections, or the universal sharp constant \(3\).

## Limitations
The work does not determine the exact global Lebesgue constant for \(\tau\ne1\), prove global maximizing locations, or classify multiple defective cells, endpoint effects, arbitrary spline degree, or higher-dimensional finite-element meshes. Literature priority remains subject to specialized historical references on one-defect cardinal splines, including formulations not found in the current searches. The derived formulas are pointwise for fixed \(\tau>0\); no uniform assertion is made as \(\tau\to0\) or \(\tau\to\infty\).

## References
1. Z. Ciesielski and A. Kamont, *The Lebesgue constants for the Franklin orthogonal system*, Studia Math. **164** (2004), 55–73, DOI: 10.4064/sm164-1-4. Full open text: https://www.impan.pl/shop/en/publication/transaction/download/product/90654
2. M. Passenbrunner, *Monotonicity of the Lebesgue constant for equally spaced knots*, arXiv:1103.1949, first posted 2011-03-10. https://arxiv.org/abs/1103.1949
3. M. Passenbrunner, *The Lebesgue Constant for the Periodic Franklin System*, arXiv:1103.1950, first posted 2011-03-10. https://arxiv.org/abs/1103.1950
4. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first posted 2004-08-30. https://arxiv.org/abs/math/0408418
