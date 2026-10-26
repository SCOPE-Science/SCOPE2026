# Exact annealed and quenched rates for one-rare-row reshuffled Kaczmarz

## Finding
Consider a consistent homogeneous two-variable linear system with \(a\ge 1\) labelled copies of one unit row normal \(u\in\mathbb R^2\) and one unit row normal \(v\), where \(0<|u^\top v|<1\). At every epoch use an independent uniformly sampled permutation of all \(m=a+1\) labelled rows, applying ordinary unrelaxed Kaczmarz projections. Put \(x=(u^\top v)^2\in(0,1)\). Starting with a nonzero error \(e_0\in u^\perp\), let \(e_k\) be the error **after** epoch \(k\).

Let \(J_k\in\{0,\ldots,a\}\) be the number of copies of \(u\) before the unique \(v\) in epoch \(k\). Then the \(J_k\) are independent and uniform. Write \(A_k=\mathbf1_{\{J_k=a\}}\), \(F_k=\mathbf1_{\{J_k=0\}}\), and \(C_k=\sum_{j=2}^k A_{j-1}F_j\). For each \(k\ge1\), **pathwise**,
\[
\frac{\|e_k\|_2^2}{\|e_0\|_2^2}=x^{\,2k-A_k-2C_k}.
\]
Consequently the almost-sure (quenched) squared-error exponential factor per epoch is
\[
\boxed{\displaystyle\lim_{k\to\infty}(\|e_k\|_2^2/\|e_0\|_2^2)^{1/k}=q_{\rm as}=x^{2(1-m^{-2})}\quad\text{almost surely}.}
\]

For the expectation, define \(w_k\in\mathbb R^2\) by \((w_k)_U=\mathbb E[\|e_k\|_2^2\mathbf1_{\{J_k<a\}}]\) and \((w_k)_V=\mathbb E[\|e_k\|_2^2\mathbf1_{\{J_k=a\}}]\) for \(k\ge1\), with \(w_0=(\|e_0\|_2^2,0)^\top\). Then the **exact finite-horizon identity** is
\[
 w_k=T^k w_0,\qquad
 T=\frac1m\begin{pmatrix} ax^2&x+(a-1)x^3\\x&x^2\end{pmatrix},\qquad
 \mathbb E\|e_k\|_2^2=(1,1)w_k.
\]
Its sharp mean-square exponential factor is
\[
\boxed{\displaystyle\lim_{k\to\infty}(\mathbb E\|e_k\|_2^2/\|e_0\|_2^2)^{1/k}=q_{\rm ms}=\frac{x^2+\sqrt{x^4+4m^{-2}x^2(1-x^2)}}2.}
\]
The annealed and quenched factors have a strict, exact separation for **all** \(a\ge1\), \(0<x<1\):
\[
 \boxed{x^{2(1-m^{-2})}<q_{\rm ms}<x.}
\]
The rightmost quantity \(x\) is the optimal common *per-epoch squared operator-norm bound* over all permutations, so its strict gap from the mean-square rate is an exact quantitative failure of worst-permutation analysis to represent typical epoch rates in this natural repeated-row family. For fixed \(m\), as \(x\downarrow0\), \(q_{\rm ms}\sim x/m\), whereas \(q_{\rm as}=x^{2(1-m^{-2})}\), making their ratio diverge. At \(m=2\), the two factors simplify to \(q_{\rm ms}=(x+x^2)/2\) and \(q_{\rm as}=x^{3/2}\).

## Assumptions and scope
The system is overdetermined but consistent, with solution zero after translation, two real unknowns, \(a\ge1\) rows exactly coinciding with unit normal \(u\), and precisely one distinct row of unit normal \(v\), with nonzero and nonunit overlap. The labelled rows are independently reshuffled afresh for each epoch, uniformly among all \((a+1)!\) permutations; the induced position \(J_k\) of the unique row is uniformly distributed. Each row update is the usual orthogonal projection onto the row's homogeneous hyperplane. All convergence factors are **per complete epoch**, not per row update. The initial vector is assumed to be nonzero and orthogonal to \(u\), which can be arranged by a single preliminary \(u\)-projection when it does not annihilate the error. No statement is made for exactly parallel or orthogonal row normals (the endpoints of the parameter range), inconsistent equations, nonindependent epoch shuffles, or non-orthogonal relaxation.

## Proof
Let \(P_u=I-uu^\top\) and \(P_v=I-vv^\top\). For any nonzero vector on either line \(u^\perp\) or \(v^\perp\), projection onto the **other** line multiplies its squared Euclidean norm by exactly \(x=(u^\top v)^2\); projection onto the **same** line leaves it unchanged. With \(0<x<1\), no finite projection product on these two lines kills a nonzero vector.

The unique \(v\)-row in epoch \(j\) occurs after \(J_j\) repeated \(u\)-rows. If the preceding epoch ends on \(u^\perp\), the squared-norm exponent within the current epoch is \(2\) when \(J_j<a\) and \(1\) when \(J_j=a\). If it ends on \(v^\perp\), those exponents are \(1\) when \(J_j=0\), \(3\) when \(1\le J_j<a\), and \(2\) when \(J_j=a\). These four cases are unified by
\[
 D_j=2+A_{j-1}-A_j-2A_{j-1}F_j,
\]
with \(A_0=0\), because \(e_0\in u^\perp\). Summation telescopes: \(\sum_{j=1}^k D_j=2k-A_k-2\sum_{j=2}^k A_{j-1}F_j\). This proves the pathwise identity, including the exact starting boundary condition. For each \(j\ge2\), the indicator \(A_{j-1}F_j\) has mean \(1/m^2\); the even-indexed indicators form an independent bounded family, and so do the odd-indexed indicators. The strong law applied separately to these two families gives \(C_k/k\to1/m^2\) almost surely. Since \(0\le A_k\le1\), taking logarithms and then exponentiating gives \(q_{\rm as}\).

For the expected squared mass, the endpoint of an epoch is the line \(v^\perp\) precisely when \(J_k=a\), otherwise \(u^\perp\). Conditional on a previous endpoint of type \(U\), the \(a\) cases \(J_k<a\) have squared-mass factor \(x^2\), and the single \(J_k=a\) case has factor \(x\). Conditional on type \(V\), the \(J_k=0\) case has factor \(x\), the \(a-1\) interior cases have factor \(x^3\), and the \(J_k=a\) case has factor \(x^2\). Dividing by \(m\) supplies the two columns of \(T\), giving the exact recurrence \(w_k=Tw_{k-1}\), including its stated \(w_0\). Direct multiplication shows
\[
\operatorname{tr}T=x^2,\qquad
\det T=-\frac{x^2(1-x^2)}{m^2}<0.
\]
Thus its eigenvalues are \(\lambda_\pm=(x^2\pm\sqrt{x^4+4m^{-2}x^2(1-x^2)})/2\), one positive and one negative. Every entry of \(T\) is positive. The Perron–Frobenius theorem, including positivity of the initial vector's projection onto the leading left eigenvector and of the evaluation vector \((1,1)\), yields the exact exponential mean-square factor \(q_{\rm ms}=\lambda_+\).

For the strict lower inequality, put \(t=m^{-2}\in(0,1/4]\), \(z=x^{-2}>1\), and \(y=q_{\rm ms}/x^2\). The positive root satisfies \(y(y-1)=t(z-1)\). Let \(g(z)=z^{2t}-z^t-t(z-1)\). Then \(g(1)=g'(1)=0\) and
\[
 g''(z)=t z^{t-2}\left((4t-2)z^t+1-t\right)<0\qquad(z\ge1),
\]
because the bracket is decreasing in \(z\) and at \(z=1\) equals \(3t-1\le-1/4\). Consequently \(g(z)<0\) for \(z>1\), hence \(z^t(z^t-1)<t(z-1)=y(y-1)\). As \(s\mapsto s(s-1)\) is strictly increasing on \([1,\infty)\), \(z^t<y\), giving \(x^{2(1-t)}<q_{\rm ms}\). For the strict upper inequality, evaluate the characteristic polynomial \(p(\lambda)=\lambda^2-x^2\lambda-tx^2(1-x^2)\) at \(\lambda=x\):
\[
 p(x)=x^2(1-x)[1-t(1+x)]>0.
\]
Since its roots have opposite signs and \(x>0\), \(q_{\rm ms}<x\).

Finally, for any permutation of the \(a+1\) rows, the epoch matrix either has exactly one switch (\(v\) first or last), giving squared operator norm \(x\), or at least two switches (\(v\) interior), giving squared operator norm \(x^2\); since \(a\ge1\), a one-switch permutation always exists. Therefore the exact uniform squared bound is \(x\). For \(x\downarrow0\) at fixed \(m\), the explicit formula gives \(q_{\rm ms}=x/m+O(x^2)\), whereas \(q_{\rm as}=x^{2(1-m^{-2})}\) has strictly larger exponent than one; this gives the divergence of their ratio. The \(m=2\) identities follow by direct substitution.

## Verification
The standalone Python 3 standard-library script `verification/check_rrk.py` constructs the rational projection matrices for \(u=(1,0)\) and \(v=(3/5,4/5)\), so \(x=9/25\). It exhaustively checks the individual one-epoch products and their exact expectation transition matrix for \(1\le a\le8\), enumerates all epoch-position strings of lengths \(1\) through \(5\) for \(1\le a\le4\) against the exact pathwise formula, and checks the exact characteristic trace and determinant identities. Additional floating-point spot checks test the strict comparison over several parameters; the universal comparison is proved above. Execute `python3 verification/check_rrk.py` from the extracted package. The recorded output is `PASS: 11752 deterministic exact-arithmetic and floating-point consistency assertions`.

## Relationship to prior work
D. Han and J. Xie, *A simple linear convergence analysis of the reshuffling Kaczmarz method*, arXiv:2410.01140v1 (2 October 2024), introduce a uniformly random-reshuffling Kaczmarz convergence analysis and give a sharp **uniform worst-permutation** contraction upper bound. Their Sections 2–3 were inspected in full; neither the repeated-row planar exact finite-horizon mean-square matrix nor the almost-sure boundary-pattern exponent is supplied there. The present result studies the *same reshuffling rule* but exact distributional rates in a structured redundant two-dimensional system; it does not claim the general convergence theorem as new. The randomized-with-replacement analysis of Bai and Wu (2018) concerns a different sampling law and cannot imply a without-replacement epoch transfer matrix directly. The published result *Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation* instead concerns a deterministic cyclic **relaxed** two-row method and its worst-case operator powers, not independent epoch permutations, duplicated labels, or distinct annealed and quenched exponents. Classical Kaczmarz projection geometry is used without an originality claim.

## Limitations
The exact rates depend on a repeated-row and one-rare-row configuration, the nonzero initial error in \(u^\perp\), independent complete random reshuffles, exact arithmetic, and two dimensions. They do not classify arbitrary multi-angle row systems or arbitrary initial vectors without adjusting the initial boundary term. The strict distributional gap is an exact mathematical statement for this family, not a claim that row duplication improves work-normalized computational cost. Publication-priority uncertainty persists because an equivalent derivation may exist in specialized older randomized alternating-projection or product-of-random-projections literature. No external independent mathematical validation is asserted.

## References
1. D. Han and J. Xie, “A simple linear convergence analysis of the reshuffling Kaczmarz method,” arXiv:2410.01140v1, first posted 2 October 2024, https://arxiv.org/html/2410.01140v1.
2. Z.-Z. Bai and W.-T. Wu, “On convergence rate of the randomized Kaczmarz method,” *Linear Algebra and its Applications* 553 (2018), 252–269, DOI 10.1016/j.laa.2018.05.009 (sampling with replacement; abstract inspected).
3. “Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation,” publicly available mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-horizon-cost-of-asymptotically-optimal-two-row-kacz--d549f7251aa1 (complete RESULT.md inspected).
4. T. Strohmer and R. Vershynin, “A randomized Kaczmarz algorithm with exponential convergence,” arXiv:math/0702226 (2007) (classical independent-row sampling background).
