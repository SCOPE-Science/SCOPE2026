# Universal phase response for one-entry complex Hadamard Schur multipliers

## Finding

Let \(n\ge 2\) be an integer and \(H\in\mathbb C^{n\times n}\) a **complex Hadamard matrix**: every entry has modulus one and \(HH^*=nI\). Select one position and multiply its entry by a phase \(\zeta\in\mathbb C\), \(|\zeta|=1\), obtaining \(B\). Denote by \(S_B(X)=B\circ X\) its Schur multiplier on complex \(n\times n\) matrices, with the spectral operator norm on both domain and codomain.

Put \(d=n-1\), \(h=|d+\zeta|\), and, for \(n\ge3\), put
\[
a=(n-2)\sqrt n,\qquad b=d^2-1+2dh.
\]
Then the **exact** Schur multiplier norm is
\[
\boxed{\ \|S_B\|=\frac{ah+\sqrt{(a^2+b)((d+h)^2-1)}}{b}\ },\qquad n\ge3.
\]
For \(n=2\), the exact formula is
\[
\boxed{\ \|S_B\|=\sqrt{1+\tfrac12|1+\zeta|}\ }.
\]
This quantity depends only on \(n\) and \(\zeta\), not on the complex Hadamard equivalence class or the modified position. For \(\zeta=e^{i\theta}\), \(0\le\theta\le\pi\), it decreases strictly as \(\theta\) increases. Its values at the endpoints are \(\sqrt n\) and
\[
\frac{(n-2)\sqrt n+2(n-1)\sqrt{n+2}}{3n-2},
\]
respectively. In particular, for fixed \(n\ge2\),
\[
\sqrt n-\|S_B\|=\frac{n-1}{4n^{5/2}}\theta^2+O_n(\theta^4)
\qquad(\theta\to0).
\]
The sign-flip endpoint \(\zeta=-1\) is prior work in the same line of research; the continuous complex-phase law, strict phase ordering and local stability coefficient are the present claims.

## Assumptions and scope

The matrix is **unnormalized**: its entries have modulus one, not \(n^{-1/2}\). An arbitrary existing complex Hadamard matrix is allowed, including Fourier matrices in every dimension. There is exactly one changed entry, the change is multiplication by a **unit** complex phase, and the operator norm is the complex spectral norm. The formula is asserted for every integer \(n\ge2\) and every \(|\zeta|=1\), including \(\zeta=1\) and \(\zeta=-1\). No assertion concerns multiple changed entries or Schatten norms other than the spectral norm.

## Proof

**1. Rank-one trace-norm duality.** Let \(P=\operatorname{diag}(p_1,\ldots,p_n)\) and \(Q=\operatorname{diag}(q_1,\ldots,q_n)\), with nonnegative entries summing to one separately. Duality of spectral and nuclear matrix norms, followed by the fact that extreme points of the nuclear unit ball have rank one, gives the exact identity
\[
\|S_B\|=\max_{p,q}\|P^{1/2}BQ^{1/2}\|_*.
\]
For a maximizer, write \(v_i=\sqrt{p_i}\) and \(w_j=\sqrt{q_j}\); a polar unitary of \(\operatorname{diag}(v)B\operatorname{diag}(w)\) produces an operator-norm-one primal witness, so this identity gives actual operator norms, not just lower bounds.

**2. Concavity and a global stationary-point principle.** For positive matrices \(A,C\), let
\[
\mathcal F(A,C)=\operatorname{Tr}\big[(A^{1/2}CA^{1/2})^{1/2}\big].
\]
The exact variational identity
\[
\mathcal F(A,C)=\frac12\inf_{X\succ0}
  \{\operatorname{Tr}(AX)+\operatorname{Tr}(CX^{-1})\}
\]
shows joint concavity in \((A,C)\), because it is an infimum of affine functions. The identity follows by minimizing over positive definite \(X\); its stationary equation \(XAX=C\) has solution \(X=A^{-1/2}(A^{1/2}CA^{1/2})^{1/2}A^{-1/2}\). Boundary cases follow by continuity. Thus
\[
(p,q)\longmapsto\|P^{1/2}BQ^{1/2}\|_*
=\mathcal F(P,BQB^*)
\]
is jointly concave on the two probability simplices.

Multiplying rows and columns by unimodular constants, and permuting them, leaves the Schur norm unchanged. Hence arrange the modified entry at \((1,1)\) and dephase the underlying \(H\), so its first row and column are all ones and \(B_{11}=\zeta\).

Consider the restricted probability vectors
\[
p=(\alpha,\beta,\ldots,\beta),\qquad
q=(\gamma,\delta,\ldots,\delta),\qquad
\beta=\frac{1-\alpha}{d},\quad\delta=\frac{1-\gamma}{d}.
\]
At such a \(q\), \(BQB^*\) is invariant under arbitrary permutations of coordinates \(2,\ldots,n\): indeed \(BB^*\) and the first column outer product differ from scalar matrices only by terms in the span of the first coordinate vector and the all-ones vector. The analogous statement holds for \(B^*PB\). Therefore, at any positive restricted pair, the partial derivatives with respect to coordinates \(2,\ldots,n\) are separately equal for \(p\) and \(q\).

The restricted objective is symmetric under interchanging \(\alpha\) and \(\gamma\) (verified by the two-dimensional calculation below). Its restriction to the diagonal \(\alpha=\gamma\) has an interior maximum. At that maximum, equality of the two restricted partial derivatives, plus the vanishing diagonal derivative, makes each restricted partial derivative zero. Combined with the equal outside-coordinate derivatives, this gives the complete simplex stationarity conditions. Joint concavity then proves the **global upper bound and equality** at the symmetric restricted maximizer. There is no assumption that the original Hadamard matrix has a transitive permutation automorphism group.

For the exceptional pair \((n,\zeta)=(2,-1)\), the modified matrix has rank one with unimodular entries and its Schur multiplier has norm one; this case is handled directly. For every other case the modified matrix is invertible, so the interior differentiability used above holds.

**3. Exact two-dimensional reduction.** Let \(u=(0,1,\ldots,1)/\sqrt d\). Relative to \(\operatorname{span}\{e_1,u\}\) on each side, the dephased \(H\) has block
\[
\begin{pmatrix}1&\sqrt d\\\sqrt d&-1\end{pmatrix},
\]
and its orthogonal complement carries \(\sqrt n\) times a unitary. Changing \(H_{11}\) to \(\zeta\) changes just the upper-left block entry. Thus, for restricted \(p,q\), all but two singular values of \(P^{1/2}BQ^{1/2}\) equal \(\sqrt{n\beta\delta}\). The exceptional block is
\[
\begin{pmatrix}
\sqrt{\alpha\gamma}\,\zeta&\sqrt{d\alpha\delta}\\
\sqrt{d\beta\gamma}&-\sqrt{\beta\delta}
\end{pmatrix}.
\]
Its squared nuclear norm is its squared Frobenius norm plus twice the absolute determinant:
\[
\alpha\gamma+d\alpha\delta+d\beta\gamma+\beta\delta
+2|d+\zeta|\sqrt{\alpha\beta\gamma\delta}.
\]
This is symmetric in \(\alpha,\gamma\), using \(d\beta=1-\alpha\) and \(d\delta=1-\gamma\), as required above.

On the diagonal \(\alpha=\gamma\), write \(y=\alpha/\beta>0\). Then \(\alpha=y/(y+d)\), \(\beta=1/(y+d)\), and the objective becomes
\[
F(y)=\frac{a+\sqrt{y^2+2(d+h)y+1}}{y+d}.
\]
When \(n\ge3\), the derivative has exactly one positive zero because its sign is the sign of
\[
d(d+h)-1-hy-a\sqrt{y^2+2(d+h)y+1},
\]
a strictly decreasing function of \(y\ge0\) that starts positive and tends to negative infinity. The positive-zero condition follows, for example, from \(h\ge n-2\) and \(d(d+n-2)-1>(n-2)\sqrt n\). The critical point therefore globally maximizes \(F\).

Let \(t=F(y_*)\) and \(K=d+h\). Tangency gives
\[
(a+ht)^2=(K^2-1)(t^2-1).
\]
Writing \(b=K^2-1-h^2=d^2-1+2dh\), the positive solution of the resulting quadratic is exactly
\[
t=\frac{ah+\sqrt{(a^2+b)(K^2-1)}}b.
\]
For \(n=2\), \(a=0\) and the restricted maximum is attained at \(y=1\), giving \(\sqrt{1+h/2}\); when \(h=0\) the objective is identically one. The preceding global concavity argument applies away from that exceptional singular case.

**4. Strict phase ordering and stability.** For \(0<\theta<\pi\),
\[
h=|d+e^{i\theta}|=\sqrt{n^2-2d(1-\cos\theta)}
\]
is strictly decreasing in \(\theta\). For every \(y>0\), \(F(y)\) increases strictly with \(h\), so the maximized norm inherits strict decrease. At \(\theta=0\), the unique optimizer is \(y_*=1\) and \(F(1)=\sqrt n\). The envelope derivative with respect to \(h\) there is \(1/(2n\sqrt n)\), whereas \(h=n-d\theta^2/(2n)+O_n(\theta^4)\), yielding the stated quadratic deficit. Substitution \(h=n-2\) at \(\zeta=-1\) simplifies algebraically to the stated known sign-flip endpoint.

## Verification

The accompanying standalone `check.py` computes the closed formula and independently maximizes the exact dual nuclear norm over **all** row and column probability weights using numerical optimization, rather than imposing symmetric weights. It compares 30 Fourier-matrix order/phase cases across orders \(2,3,4,5,6,8\) and nine cases in a non-real one-parameter order-four complex Hadamard family. It also checks the one-variable restricted maximization. All 39 test cases completed successfully (three independent optimization starts per case). These are **finite consistency checks**, not a proof of the infinite assertion, which is established analytically above. Run with `python check.py` using Python, NumPy, and SciPy.

## Relationship to prior work

Holbrook, Johnston and Schoch (arXiv:2206.02863v1) prove the general Hadamard maximum, study real sign matrices, and give several small-dimensional norms. The formula at one **negative sign** in a real Hadamard matrix, including the order-four special case in that literature, is already established and is not claimed new. The theorem here extends to **every order** via complex Fourier matrices, every complex Hadamard equivalence class, and every continuous unit phase, with the sharp monotonicity and stability law.

Cowen and collaborators describe general spectral/trace dual methods and optimization for Hadamard multipliers; Davidson and Donsig give general structural and symmetry formulas. Christensen studies extremal multipliers and a self-adjoint order formula. Those general techniques do not themselves assert this complex one-defect phase curve. These comparisons support, but cannot certify, historical novelty.

## Limitations

The proof does not cover non-unimodular perturbations, multiple coordinate defects, the real-only operator-norm variant, or other Schatten exponents. The boundary case \(n=2,\zeta=-1\) is singular and is treated separately. The numerical checker supplies supplementary evidence only. Historical priority, especially under alternative formulations of diagonal scaling or matrix fidelity, remains subject to independent literature review. No independent mathematical audit has been performed.

## References

- J. Holbrook, N. Johnston, J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863v1 (public June 6, 2022), Linear and Multilinear Algebra, DOI:10.1080/03081087.2023.2212317.
- C. C. Cowen, P. A. Ferguson, D. K. Jackman, E. A. Sexauer, C. Vogt, H. J. Woolf, *Finding Norms of Hadamard Multipliers*, Linear Algebra and its Applications (1993), author-hosted full text: https://www.math.purdue.edu/~cowen/Downloads/HadNorm.pdf.
- K. R. Davidson, A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073v1 (June 3, 2005).
- E. Christensen, *Extremal Schur Multipliers*, arXiv:2410.20112v1 (October 26, 2024).
- E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670v1 (May 30, 2025; revised version also inspected).
