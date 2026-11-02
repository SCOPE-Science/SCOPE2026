# Symmetry breaking of balanced molecules in four-point Lipschitz-free \(p\)-spaces

## Finding
Let \(E=\{1,2,3,4\}\) with \(d(i,j)=1\) for \(i\ne j\), and let \(0<p\le1\). Represent a free-space vector by signed masses whose total is zero; the symbol \(\delta_i\) denotes the point mass at vertex \(i\), with the customary common additive-basepoint convention. For \(0\le t\le1\) put
\[
\mu_t=\delta_1+\delta_2-(1+t)\delta_3-(1-t)\delta_4,
\qquad R_p(t)=\frac{\|\mu_t\|_{\mathcal F_p(E)}}{\sqrt{4+2t^2}}.
\]
Then the **exact, all-exponent norm formula** is
\[
\boxed{\|\mu_t\|_{\mathcal F_p(E)}^p=1+t^p+(1-t)^p.}
\]
For every \(0<p<1\), the function \(R_p\) has exactly one global maximum on \([0,1]\), attained at a number \(t_p\in(0,1/2)\). It is uniquely characterized by
\[
\frac{t_p^{p-1}-(1-t_p)^{p-1}}{1+t_p^p+(1-t_p)^p}
=\frac{t_p}{2+t_p^2}.
\]
In particular, \(R_p(t_p)>R_p(0)=2^{1/p-1}\), and the local symmetry-breaking law is
\[
\frac{R_p(t)}{R_p(0)}=1+\frac{t^p}{2p}+o(t^p)\quad(t\downarrow0).
\]
By contrast \(R_1(t)=(1+t^2/2)^{-1/2}\) is uniquely maximized at \(t=0\). Moreover the balanced masses \((1,1,-1,-1)\) are, up to scalar and permutation, all **global** maximizers of the \(p=1\) quotient \(\|\mu\|_{\mathcal F_1(E)}/\|a\|_2\), for mass vectors \(a\in\mathbb R^4\) with \(\sum_i a_i=0\). Consequently the \(p=1\) global extremizers are not even local maxima for any \(p<1\).

## Assumptions and scope
Everything is over the real scalars. Distances between different vertices are one. The free \(p\)-space is the usual real \(p\)-Banach free space of the pointed metric, and the norm of a zero-mass vector is independent of the chosen basepoint. The Euclidean denominator \(\sqrt{4+2t^2}\) is the ordinary coefficient \(\ell_2\)-norm, not a free-space norm. The exact maximization theorem concerns only the canonical one-parameter family \(\mu_t\); the unrestricted sharp embedding constant for \(0<p<1\) is **not** determined.

## Proof
**Step 1 (finite-tree reduction).** The free \(p\)-unit ball is the absolutely \(p\)-convex hull of its normalized directed molecules. Thus the \(p\)-th power of the norm is the minimum of \(\sum_e|c_e|^p\) over molecular decompositions. In a finite-dimensional spanning decomposition with more than three nonzero edges, a nontrivial linear relation permits varying the coefficients while preserving the represented vector. On a sign-stable interval, \(\sum|c_e|^p\) is concave for \(0<p\le1\); an endpoint removes an edge without increasing the cost. Iteration leaves a linearly independent set of at most three molecular edges. After adding zero-flow edges these form a spanning tree on four vertices. For each edge, its flow is the sum of vertex masses on either side. This reconstructs the four-vertex instance of the finite-tree formula of Cúth and Raunig [1, Theorem 2.2].

**Step 2 (complete exact tree comparison).** There are \(4^{4-2}=16\) labeled spanning trees. For the mass vector \((1,1,-1-t,-1+t)\), the multisets of absolute edge-flow values, with multiplicities in parentheses, are
\[
\begin{gathered}
\{1-t,1,1+t\}(2),\quad\{t,1-t,1+t\}(2),\quad
\{1-t,1,2\}(2),\quad\{1,1+t,2\}(2),\\
\{t,1-t,1\}(2),\quad\{t,1,1+t\}(2),\quad
\{t,1,1\}(2),\quad\{1-t,1,1\}(1),\quad
\{1,1,1+t\}(1).
\end{gathered}
\]
Every multiset contains, after an appropriate matching, numbers no smaller than \(t,1-t,1\) individually throughout \(0\le t\le1\). Two trees realize these values exactly. Since \(x\mapsto x^p\) is increasing, the minimum tree cost is exactly \(1+t^p+(1-t)^p\). An independent integer-affine enumeration and all endpoint comparisons are supplied in `verify.py`; this is a symbolic proof of domination valid continuously in \(t\), not an inference from sample values.

**Step 3 (unique symmetry-broken optimum).** Set \(S_p(t)=1+t^p+(1-t)^p\). On \(0<t<1\), logarithmic differentiation gives
\[
\frac{R_p'(t)}{R_p(t)}=
\frac{t^{p-1}-(1-t)^{p-1}}{S_p(t)}-\frac{t}{2+t^2}.
\]
For \(0<p<1\), on \(0<t<1/2\) the first fraction is strictly decreasing from \(+\infty\) to zero: its numerator is positive and strictly decreasing, while its denominator is strictly increasing. The second term increases strictly from zero. Hence there is one crossing. At \(1/2\le t<1\) the first term is nonpositive and the second positive, so the derivative is negative. The crossing is therefore the unique global maximizer, and it is interior.

Expansion at the origin gives \(S_p(t)=2+t^p+o(t^p)\) for \(0<p<1\) because \(t=o(t^p)\), while \(\sqrt{4+2t^2}=2(1+O(t^2))\). This establishes the claimed positive Hölder cusp. At \(p=1\), \(S_1(t)=2\), giving strict decrease.

**Step 4 (global classical benchmark).** For a zero-mass real vector \(a\), the equilateral free Banach norm is \(\|a\|_{\mathcal F_1(E)}=\frac12\|a\|_1\). Cauchy–Schwarz gives \(\|a\|_1\le2\|a\|_2\). Equality, for nonzero zero-sum \(a\), requires all four magnitudes equal, hence exactly two plus and two minus signs. They are the balanced vectors, establishing the global \(p=1\) extremizer classification. The cusp from Step 3 shows each such vector is not locally maximizing once \(p<1\), by the coordinate-permutation symmetry.

## Verification
Execute `python3 verify.py` using Python's standard library. The program generates all sixteen spanning trees, computes all edge-cut flows as exact integer-affine functions of \(t\), and proves a componentwise matching to the candidate triple on the **entire** interval by testing affine differences at both endpoints. Its five floating-point parameter checks are auxiliary diagnostics only; the infinite-exponent and interval statements are established analytically in the proof. Expected success lines include `EXACT_SYMBOLIC_TREE_CERTIFICATE_OK 16 trees` and `ALL_CHECKS_OK`.

## Relationship to prior work
Cúth and Raunig [1] gave the general finite-tree formula for Lipschitz-free \(p\)-norms, which Step 1 uses; the general algorithm is **not** claimed here. Their three-point explicit formula and applications do not state this four-point coefficient-profile optimum. Bíma [2] studies vertex interpolation on cubes, not symmetry breaking of Euclidean-normalized four-point transport masses. Related sharp constants for planar triangles concern a three-vertex problem. The new assertion is the all-parameter four-point formula **together with** uniqueness of a nonzero optimal asymmetry and the instantaneous loss of local optimality for the classical globally balanced vectors. The unrestricted \(p<1\) embedding maximum is not claimed.

## Limitations
The uniqueness is only within the specified one-parameter orbit. There may be other, larger unrestricted \(p<1\) norm ratios. The general tree formula from [1] makes the fixed-vector norm computationally accessible; bibliographic priority for the explicit symmetry-breaking conclusion still merits independent examination. The finite checker does not certify infinite analytic quantifiers without Steps 1–4. No independent audit has been performed.

## References
[1] M. Cúth and T. Raunig, *Canonical embedding of Lipschitz-free \(p\)-spaces*, arXiv:2311.02920 (first public version, 2023-11-06), especially Theorem 2.2, its proof, and Section 2.2. https://arxiv.org/abs/2311.02920

[2] J. Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265 (2023). https://arxiv.org/abs/2303.03265
