# Sharp endpoint sensitivity and its unique conductance maximum in two-clique networks

## Finding
Let \(m\ge2\), \(h=(m-1)/m\), and \(y=\sqrt{a/b}\). The Euclidean gradient-edge projector on the complete graph with \(2m\) vertices, intra-community edge conductance \(a>0\), and inter-community conductance \(b>0\), satisfies
\[
\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\Lambda_m(y)
=\begin{cases}
\dfrac{1+2h^2+(1-2h^2)y^2+2hy}{1+y^2},&0<y\le1,\\
\dfrac{2hy^2+2y}{1+y^2},&y\ge1.
\end{cases}
\]
Over every positive conductance ratio there is one and only one maximizer,
\[
\frac ab=\bigl(\sqrt{1+4h^2}-2h\bigr)^2,
\quad \max_{a,b>0}\|P\|=1+h\sqrt{1+4h^2}.
\]
The maximum is strictly greater than either boundary limit \(1+2h^2\) as \(a/b\downarrow0\) or \(2h\) as \(a/b\to\infty\), and strictly greater than the complete-graph value \(1+h\) at \(a=b\). It increases to \(1+\sqrt5\) as \(m\to\infty\); the optimizing conductance ratio tends to \((\sqrt5-2)^2\).

## Assumptions and scope
The vertex set is a disjoint union \(A\sqcup B\), each containing \(m\) vertices. Every pair is connected by one undirected edge, with conductance \(a\) for an edge inside a part and \(b\) for an edge crossing parts. Orient edges arbitrarily. Let \(D\) be the oriented vertex-by-edge incidence matrix and \(C\) the diagonal matrix of conductances. Set \(L=DCD^{\mathsf T}\). On ordinary Euclidean edge coordinates, the projector \(P=C^{1/2}D^{\mathsf T}L^+DC^{1/2}\) is symmetric and idempotent. The operator input/output norm is the usual maximum over individual *conductance-normalized edge-flow coordinates*. The two parameters are positive; the endpoints at zero and infinity are only limits, not members of the family.

## Proof
Put \(d=m(a+b)\), \(q=2mb\), \(n=2m\). The vertex space decomposes orthogonally into constants, fluctuations of zero sum inside each part, and the one-dimensional contrast of the two partwise constant vectors. The Laplacian eigenvalues on these spaces are respectively \(0,d,q\). For any inter-part edge \(e=(u,v)\) with \(u\in A\) and \(v\in B\), letting \(g_A,g_B\) denote part indicators gives
\[
L^+(e_u-e_v)=\frac1d(e_u-e_v)+k(g_A-g_B),
\qquad k=\frac{a-b}{2m^2b(a+b)}.
\]
For an intra-part edge \(e=(u,v)\), simply \(L^+(e_u-e_v)=(e_u-e_v)/d\). For any edge \(f\), the corresponding projector coefficient is
\[
P_{ef}=\sqrt{c_ec_f}\,(e_u-e_v)^{\mathsf T}L^+(e_{f,+}-e_{f,-}),
\]
where \(c_e,c_f\) are its conductances and orientation signs do not affect row absolute sums.

For an intra-part row, there are one identical intra-edge and \(2(m-2)\) other intra-edges sharing exactly one endpoint. Exactly \(2m\) cross edges share an endpoint. Taking absolute coefficients yields the row norm
\[
W_m(y)=\frac{2hy^2+2y}{1+y^2}.
\]
For a cross-edge row, its \(m^2\) cross-edge coefficients have, up to orientation, values \(2/d+2k\) (one), \(1/d+2k\) (\(2(m-1)\) coefficients), and \(2k\) (\((m-1)^2\) coefficients). The first two are strictly positive; the last changes sign precisely at \(a=b\). The \(2(m-1)\) incident intra-edges have magnitude \(\sqrt{ab}/d\). Therefore, with \(h=(m-1)/m\), the cross-edge absolute row sum is
\[
C_m(y)=\begin{cases}
\dfrac{1+2h^2+(1-2h^2)y^2+2hy}{1+y^2},&0<y\le1,\\
1+\dfrac{2hy}{1+y^2},&y\ge1.
\end{cases}
\]
For \(0<y\le1\), direct subtraction gives
\[
(1+y^2)(C_m(y)-W_m(y))
=(1-y)\bigl[1+2h^2+(2h^2+2h-1)y\bigr]\ge0,
\]
using \(h\ge1/2\). For \(y\ge1\),
\[
(1+y^2)(W_m(y)-C_m(y))=(y-1)((2h-1)y+1)\ge0.
\]
These identities prove the piecewise norm formula. Every row absolute sum is realized as an output coordinate by choosing each input coordinate to equal the sign of its kernel coefficient. Symmetry of \(P\) gives equality of its induced \(\ell^1\) and \(\ell^\infty\) norms.

For \(0<y\le1\), the cross-row formula is the Rayleigh quotient of the real symmetric matrix
\[
\begin{pmatrix}1+2h^2&h\\h&1-2h^2\end{pmatrix}
\]
on the positive vector \((1,y)\). Its strictly greatest eigenvalue is \(M_C=1+h\sqrt{1+4h^2}\), uniquely attained at \(y_*=\sqrt{1+4h^2}-2h\in(0,1)\). On \(y\ge1\), the within-row bound is at most the largest eigenvalue \(M_W=h+\sqrt{1+h^2}\) of \(\begin{psmallmatrix}0&1\\1&2h\end{psmallmatrix}\). For \(h\in[1/2,1)\), put \(s=\sqrt{1+4h^2}\). The strict comparison follows from
\[
(1-h+hs)^2-(1+h^2)
=h[-2+h+4h^3+2(1-h)s]
>h^2(4h^2-1)\ge0.
\]
Thus \(M_C>M_W\) and the claimed ratio is the unique global maximum. The stated limits follow by substituting \(h\to1\) or taking the indicated positive-ratio limits.

## Verification
The attached standard-library script `VERIFY.py` forms the *grounded weighted Laplacian* independently, inverts it by exact-rational elimination, constructs every projector entry directly, and checks all row sums against the formulas for \(m=2,3,4,5\) and eight rational values of \(y\), reporting 752 exact rational row assertions. These finite checks support arithmetic and normalization but do not replace the preceding all-parameter argument.

## Relationship to prior work
Lyons's transfer-current formalism identifies the gradient cut-space projection as a canonical edge-space operator, without computing the norm here. Oliveira–de Lima–Nikiforov derive Laplacian spectra for graph blow-ups; their spectral methods motivate the two-community decomposition but do not state or imply the sharp weighted edgewise endpoint norm or its unique nontrivial conductance maximizer. Earlier unweighted complete multipartite computations concern networks lacking *internal* edges and therefore do not cover the full positive-conductance graph studied here. The new value is the exact sensitivity optimization, not the generic Laplacian pseudoinverse identity.

## Limitations
The result assumes two equally sized complete vertex communities and constant positive conductance within and across communities. It does not classify unequal community sizes, more than two communities, arbitrary edge weights, or nonlinear flow recovery. The originality assessment is limited to located primary literature and searchable related results; priority requires further independent bibliographic verification. No independent mathematical audit has been performed.

## References
1. Russell Lyons, *Determinantal Probability Measures*, arXiv:math/0204325, first submitted 2002-04-26, https://arxiv.org/abs/math/0204325. Transfer-current cut-space construction.
2. Carla Oliveira, Leonardo de Lima, Vladimir Nikiforov, *Spectra of the blow-up graphs*, arXiv:1412.0319v1, first submitted 2014-12-01, https://arxiv.org/abs/1412.0319. Laplacian spectral decomposition of blow-up networks.
