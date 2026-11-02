# Sharp negative type of pentagonal leaf coronas

## Finding

Let \(r\ge 2\) be an integer. Form \(X_r=C_5\odot\overline{K_r}\) by attaching \(r\) distinct degree-one leaves to each vertex of the five-cycle, with all graph edges of length one and with shortest-path metric \(d\). Define the supremal negative-type exponent by
\[
\wp(X_r)=\sup\left\{p\ge0:\sum_{x,y\in X_r}\alpha_x\alpha_y d(x,y)^p\le0\quad\text{for every real }\alpha\text{ with }\sum_x\alpha_x=0\right\}.
\]

**Theorem.** The exponent \(\wp(X_r)=p_r\) is the unique real \(p>1\) satisfying
\[
\boxed{r\bigl(2\cdot4^p-2^p-2\cdot3^p\bigr)=2^p.}
\]
It lies strictly between \(1\) and \(9/7\). The space has strict \(p\)-negative type for every \(0\le p<p_r\), nonstrict negative type at \(p_r\), and fails \(p\)-negative type for every \(p>p_r\). Its equality space at \(p_r\), within the zero-mass coefficient vectors, is exactly the line with coefficient \(-r\) at each of the five core vertices and coefficient \(1\) at every leaf. Consequently the minimum affine dimension of an isometric real Hilbert embedding of \((X_r,d^{p/2})\) is \(5(r+1)-1\) for \(0<p<p_r\) and \(5(r+1)-2\) at \(p=p_r\).

The sequence \((p_r)_{r\ge2}\) is strictly decreasing to \(1\). With
\[
L=4\log2-3\log(3/2),\qquad M=4(\log2)^2-3(\log(3/2))^2,
\]
it has the asymptotic expansion
\[
\boxed{p_r=1+\frac{1}{Lr}-\frac{M}{2L^3r^2}+O(r^{-3}).}
\]
In particular \(L^{-1}=0.6425936527809607\ldots\).

## Assumptions and scope

The five core vertices are \(c_i\), indexed by \(i\in\mathbb Z/5\mathbb Z\), and the leaves at \(c_i\) are \(l_{i,a}\), where \(1\le a\le r\). Set \(\delta(i,j)=\min\{|i-j|,5-|i-j|\}\), using cyclic differences in \(\{0,1,2,3,4\}\). For distinct vertices, the distances are
\[
d(c_i,c_j)=\delta(i,j),\quad d(c_i,l_{j,a})=1+\delta(i,j),\quad d(l_{i,a},l_{j,b})=2+\delta(i,j).
\]
(The last formula applies to distinct leaves, including leaves with the same parent.) No edges are weighted, no multiplicities are identified, and \(r\) is an integer at least two. The underlying normed-space question is the exact Hilbert snowflake threshold, an invariant under isometry rather than a property of a particular drawing of the graph.

## Proof

**1. All zero-sum modes.** Fix \(p>0\) and abbreviate \(u=2^p\), \(v=3^p\), and \(w=4^p=u^2\). Within the \(r\) leaves at each core vertex, vectors whose coefficients sum to zero are eigenvectors of the powered-distance matrix with eigenvalue \(-u\). This yields \(5(r-1)\) strictly negative directions. The remaining subspace consists of vectors constant on each leaf bundle; normalize the common leaf coefficient by a factor \(\sqrt r\). A discrete Fourier transform over the five core positions produces five real Hermitian two-dimensional blocks.

For a nonconstant Fourier frequency, the cosine sum \(z=2\cos(2\pi k/5)\) equals one of
\[
z_+=\frac{\sqrt5-1}{2},\qquad z_-=-\frac{1+\sqrt5}{2};
\]
the distance-two cosine sum is \(-1-z\). The corresponding block is
\[
\mathcal M_z(p,r)=\begin{pmatrix}A_z&\sqrt r B_z\\ \sqrt r B_z&rC_z-u\end{pmatrix},
\quad A_z=z-u(1+z),\quad B_z=1+uz-v(1+z),\quad C_z=u+vz-u^2(1+z).
\]
Each of the two choices of \(z\) occurs with real multiplicity two. The constant-frequency block contains one direction excluded by the zero-mass constraint and one direction with coefficient \(a=-rb\) on each core vertex and \(b\) on each leaf. Writing \(H(p)=2u^2-u-2v\), its powered-distance quadratic form equals
\[
5r\bigl(rH(p)-u\bigr)b^2.
\]
Thus the constant direction becomes critical precisely at \(rH(p)=u\).

**2. Unique candidate and a uniform upper bound.** Divide that equation by \(u\). Its left side is \(r\Phi(p)\), where
\[
\Phi(p)=\frac{H(p)}{u}=2\cdot2^p-1-2(3/2)^p.
\]
We have \(\Phi(1)=0\), and \(\Phi'(p)=2^{p+1}\log2-2(3/2)^p\log(3/2)>0\) for every \(p\ge1\). Also \(\Phi(p)\to\infty\). Therefore each \(r\ge2\) determines a unique \(p_r>1\). The exact rational interval calculation in step 4 establishes \(2H(9/7)-2^{9/7}>0\), so \(p_r<9/7\).

**3. All nonconstant modes are strictly negative at the candidate.** For \(1\le p\le9/7\), we have \(A_{z_+}<0\). Also \(A_{z_-}<0\), because \(2^{9/7}<(3+\sqrt5)/2\). At \(p=p_r\), where \(u=rH\), the determinant simplifies to
\[
\det\mathcal M_z(p_r,r)=rE_z(p_r),\qquad E_z=A_zC_z-B_z^2-A_zH.
\]
Using \(z^2+z=1\), expand this as the exponential polynomial
\[
E_z(p)=(4+3z)8^p-(4+3z)4^p-(1+2z)6^p-(2+z)9^p+(3+3z)3^p-1.
\]
We claim \(E_{z_-}(p)>0\) and \(E_{z_+}(p)>0\) for every \(1<p\le9/7\).

For completeness, the **exponential Descartes rule** says that, for increasing real \(\lambda_j\), a nonzero sum \(\sum_j a_je^{\lambda_jx}\) has at most as many real zeros, counted with multiplicity, as the number of sign changes of its nonzero coefficient list \((a_j)\). An induction proves it: divide by the lowest exponential and differentiate, which removes the first coefficient without changing the signs of the others. Rolle's theorem allows one extra zero when the first two signs differ; when they agree, the derivative has an additional zero to the left of the first zero because the function and its derivative start with the same sign at negative infinity. This establishes the sign-variation bound.

For \(z=z_-\), the coefficient signs of \(E_{z_-}\), ordered by bases \(1,3,4,6,8,9\), are \((-,-,+,+,-,-)\), with two sign changes. Direct substitution gives \(E_{z_-}(1)=0\) and \(E_{z_-}(2)=11-9\sqrt5<0\). The exact inequality \(E_{z_-}(9/7)>0\), proved below, forces another zero strictly between \(9/7\) and \(2\). There can be no further real zero, so \(E_{z_-}(p)>0\) on \((1,9/7]\).

Moreover, \(E_{z_+}(p)-E_{z_-}(p)=\sqrt5\,T(p)\), where
\[
T(p)=3\cdot8^p-3\cdot4^p-2\cdot6^p-9^p+3\cdot3^p.
\]
Its coefficient signs, ordered by bases \(3,4,6,8,9\), are \((+,-,-,+,-)\), with three changes. Since \(T(0)=T(1)=0\), \(T(9/7)>0\), and \(T(10)<0\), these are exactly three distinct real zeros: zero, one, and another strictly greater than \(9/7\). Hence \(T>0\) on \((1,9/7]\), proving \(E_{z_+}>E_{z_-}>0\) there. Both \(\mathcal M_z(p_r,r)\) are therefore strictly negative definite.

**4. Reproducible exact endpoint bounds.** The supplementary checker uses only integer inequalities to enclose each \(a^{9/7}\) between consecutive multiples of \(10^{-9}\): if \(h=\lfloor10^9a^{9/7}\rfloor\), it verifies \(h^7\le a^9 10^{63}<(h+1)^7\). It also bounds \(\sqrt5\) by consecutive multiples of \(10^{-9}\) via integer squares. Rational interval arithmetic then yields the rigorously enclosed numerical ranges
\[
2H(9/7)-2^{9/7}\in[0.036969417,0.036969428],
\]
\[
E_{z_-}(9/7)\in(0.031225926,0.031225937),\qquad
T(9/7)\in[1.078326034,1.078326046],
\]
\[
(3+\sqrt5)/2-2^{9/7}\in(0.180006679,0.180006682).
\]
These rational enclosures prove all positive-sign decisions above; the code makes the exact integer comparisons before any floating-point computation. The other sign decisions are exact: \(11-9\sqrt5<0\) and \(T(10)<0\), the latter an integer inequality.

**5. Exact threshold, equality, dimension, and asymptotics.** At \(p_r\), step 3 shows every nonconstant-frequency block is strictly negative; the within-leaf contrasts have eigenvalue \(-u\); the constant zero-mass mode has exactly one null vector. Therefore \(d^{p_r}\) is conditionally negative semidefinite with one-dimensional zero-mass kernel. By the strict negative-type interval theorem (Li–Weston, Theorem 5.4), \(d^p\) is strictly conditionally negative for all \(0\le p<p_r\). For \(p>p_r\), monotonicity of \(\Phi\) makes the constant zero-mass quadratic form positive, so negative type fails. Schoenberg's theorem converts this into the isometric Hilbert-snowflake classification. The rank of the centered Gram matrix \(-\tfrac12 JD^pJ\) is \(5(r+1)-1\) below the endpoint and \(5(r+1)-2\) at it, yielding the affine dimension statement.

Finally, \(r\Phi(p_r)=1\), and \(\Phi\) is strictly increasing with \(\Phi(1)=0\), so \(p_r\) decreases strictly to one. Taylor inversion of \(\Phi(1+t)=Lt+Mt^2/2+O(t^3)\) gives the displayed two-term expansion.

## Verification

Run \(`python verify_sun5.py`\) with Python 3, NumPy and SciPy installed. The checker uses exact integer and rational interval arithmetic for all four endpoint inequalities, then independently constructs the graph by its edges, obtains every distance using breadth-first search, and compares complete zero-mass distance-matrix spectra for \(r\in\{2,3,4,5,8,10,30\}\) at and around the predicted threshold. A finite numerical spectrum is not a substitute for the all-parameter proof above. The successful reproducibility marker is \(`CHECK_OK`\).

## Relationship to prior work

Sánchez's 2011 analysis [2] supplies general finite-distance-matrix methods and calculates the sharp exponent of the bare five-cycle. It neither attaches the private leaves nor solves the all-multiplicity classification here. Li and Weston [3] establish the strict interval property used in step 5, not the critical value. Robertson's 2023 treatment [1] develops negative type and Hilbert embedding questions, with examples involving bipartite graphs and Hamming cubes, not the present corona family. The new point is the switch to a uniform core-versus-leaves obstruction for every \(r\ge2\), including an exact transcendental equation, its unique equality space, and the two-term large-leaf expansion.

## Limitations

The proof covers **exactly** five core vertices and at least two unit-length leaves at every core vertex. It does not classify an isolated five-cycle, a one-leaf sunlet, larger odd-cycle coronas, inhomogeneous leaf counts, or weighted edges. The cited general distance-matrix framework algorithmically applies to individual finite instances but does not itself establish the uniform family theorem. Historical priority may be limited by an unindexed equivalent presentation under generalized-roundness, snowflake-embedding, or graph-corona terminology; no claim of independent audit is made.

## References

1. Gavin Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1, September 27, 2023; https://arxiv.org/abs/2309.16070.
2. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, August 2, 2011; https://arxiv.org/abs/1108.0451.
3. Hanfeng Li and Anthony Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first posted January 6, 2009); https://arxiv.org/abs/0901.0695.
