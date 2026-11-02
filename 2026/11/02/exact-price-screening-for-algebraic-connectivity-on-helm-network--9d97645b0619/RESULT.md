# Exact price screening for algebraic connectivity on helm networks

## Finding

Let \(m\ge 3\) be an integer. A *helm* consists of a hub \(h\), rim vertices \(v_i\) arranged in a cycle, and private leaves \(u_i\), for \(i\in\mathbb Z/m\mathbb Z\). Its edges are \(hv_i\), \(v_iv_{i+1}\), and \(v_iu_i\). Allow every edge to carry an **independently chosen nonnegative** conductance. A unit of conductance costs \(P>0\) on a hub spoke, \(Q>0\) on a rim edge, and \(R>0\) on a private-leaf edge. For a total budget \(B>0\), maximize \(\lambda_2(L)\), the second-smallest eigenvalue of the **unnormalized combinatorial weighted Laplacian**.

Put
\[
 c_m=2-2\cos(2\pi/m),\quad a=Q/c_m,\quad
 g(z)=2+\frac1{z-1},\quad
 h_m(z)=\frac{2z-1}{(2m+1)z-(m+1)}\qquad(z>1).
\]
Define a positive normalized minimum cost \(C_*\) and its minimizing three edge-class conductances \((X_*,Y_*,Z_*)\) as follows.

If \(P<a\), then
\[
 Z_*=1+\sqrt{P/R},\quad X_*=g(Z_*),\quad Y_*=0,\qquad C_*=2P+R+2\sqrt{PR}.
\]
If \(P=a\), use the same \(Z_*\) and \(C_*\), and **every** invariant optimum is
\[
 h_m(Z_*)\le X_*\le g(Z_*),\qquad
 Y_*=(g(Z_*)-X_*)/c_m.
\]
If \(P>a\), let \(Z_*>1\) be the **unique** solution of
\[
 R=\frac{a}{(Z_*-1)^2}+
 \frac{P-a}{\bigl((2m+1)Z_*-(m+1)\bigr)^2}.
\]
Then
\[
 X_*=h_m(Z_*),\quad Y_*=(g(Z_*)-X_*)/c_m>0,\quad
 C_*=a g(Z_*)+(P-a)h_m(Z_*)+RZ_*.
\]
In **all** cases, the unrestricted global optimum is exactly
\[
 \boxed{\max_{\sum_e p_e w_e\le B}\lambda_2(L(w))=\frac{B}{mC_*}}.
\]
An attaining network sets every spoke conductance to \(BX_*/(mC_*)\), every rim conductance to \(BY_*/(mC_*)\), and every leaf conductance to \(BZ_*/(mC_*)\). Conversely, averaging **any** unrestricted global optimizer over the dihedral symmetries yields one of the classwise optimizers just specified. Hence all unrestricted optimizers delete **every** rim edge when \(P<Q/c_m\), whereas every unrestricted optimizer retains a **strictly positive total** rim conductance when \(P>Q/c_m\). Both behaviors occur at equality. No uniqueness of the full edgewise optimizer is asserted.

In the natural equal-price case \(P=Q=R\), this gives a sharp finite-size transition: rim conductances are necessary for \(3\le m\le5\), optional at \(m=6\), and vanish in **every** global optimum for \(m\ge7\). In particular, for \(m\ge7\),
\[
 \boxed{\lambda_2^{\max}=B/(5m),\qquad
 w_{hv_i}=3B/(5m),\quad w_{v_i u_i}=2B/(5m),\quad w_{v_iv_{i+1}}=0}
\]
is a globally optimal allocation. At \(m=6\), with \(B=30\) and unit prices, both classwise allocations \((x,y,z)=(3,0,2)\) and \((3/19,54/19,2)\) have spectral gap one and the same budget.

## Assumptions and scope

The graph has \(2m+1\) vertices, \(3m\) available edges, and the three specified positive price classes. Individual weights may be zero, but are never negative. Its weighted Laplacian is \(L=\sum_{ij\in E}w_{ij}(e_i-e_j)(e_i-e_j)^\mathsf T\). The optimization uses the ordinary Euclidean Rayleigh quotient, not a degree-normalized Laplacian or the mixing modulus of a stochastic matrix. Budget is linear, and there are no independent upper caps on conductances. The result concerns all integers \(m\ge3\), every \(P,Q,R,B>0\), and **all** feasible independent edge weights.

## Proof

**1. Global symmetry reduction.** On the orthogonal complement of the all-ones vector,
\[
 \lambda_2(L(w))=\min_{\substack{u\perp\mathbf1\\\|u\|=1}}
 \sum_{ij\in E}w_{ij}(u_i-u_j)^2.
\]
It is concave as a function of the edge-weight vector. Dihedral rotations and reflections preserve the graph, each price class, the budget and the spectrum. The average of any feasible allocation over this finite group is feasible and has spectral gap at least that of the original allocation. Thus some global optimum has uniform conductances \(x\) on the spokes, \(y\) on the rim, and \(z\) on the private-leaf edges. Its budget is \(m(Px+Qy+Rz)\). If \(x=0\) or \(z=0\), the graph is disconnected and the gap vanishes, whereas strictly positive feasible weights yield a positive gap; therefore an optimizer has \(x,z>0\).

**2. Exact eigenvalue blocks.** Fourier harmonics on the rim and leaves diagonalize the cyclic action. For a nonconstant harmonic \(k\in\{1,\dots,m-1\}\), the hub amplitude is zero and the remaining block is
\[
 F_k=\begin{pmatrix}x+z+c_k y&-z\\-z&z\end{pmatrix},
 \qquad c_k=2-2\cos(2\pi k/m).
\]
For \(x,z>0\), its smaller eigenvalue is
\[
 f(s,z)=\frac{s+2z-\sqrt{s^2+4z^2}}2,
 \qquad s=x+c_ky.
\]
This is strictly increasing in \(s>0\), and \(c_k\ge c_m\), so the minimum nonconstant block is \(f(x+c_my,z)\). In the constant harmonic, the hub/rim/leaf quotient matrix is
\[
 H=\begin{pmatrix}mx&-mx&0\\-x&x+z&-z\\0&-z&z\end{pmatrix}.
\]
Its characteristic polynomial is
\[
 \lambda\Bigl(\lambda^2-((m+1)x+2z)\lambda+(2m+1)xz\Bigr).
\]
Write \(u(x,z)\) for the smaller positive root of the quadratic. All other constant-sector eigenvalues are the root zero and the larger positive root. Consequently,
\[
 \lambda_2(L)=\min\{f(x+c_my,z),u(x,z)\}.
\]
These block formulas remain valid at zero rim weight; all eigenvalue comparisons involve the full original matrix.

**3. Fix a unit target gap.** Homogeneity makes the original maximization equivalent to minimizing the expenditure needed for \(\lambda_2\ge1\). The smaller eigenvalue of \(F_1\) is strictly less than \(z\), so a feasible unit-gap design has \(z>1\). Because the larger eigenvalue of \(F_1\) exceeds one, the condition \(f(x+c_my,z)\ge1\) is equivalent to nonnegativity of its characteristic polynomial at one:
\[
 (z-1)(x+c_my)-(2z-1)\ge0,
 \quad\text{i.e.}\quad x+c_my\ge g(z).
\]
The larger positive constant-sector eigenvalue is also greater than one, since its sum with the smaller is \((m+1)x+2z>2\). Evaluating its quadratic at one gives the equivalent condition
\[
 ((2m+1)z-(m+1))x-(2z-1)\ge0,
 \quad\text{i.e.}\quad x\ge h_m(z).
\]
For every \(z>1\), the denominator of \(h_m(z)\) is positive and \(0<h_m(z)\le1/m<g(z)\). The target-gap problem is thus **exactly**
\[
 \min_{z>1,\,x\ge h_m(z),\,y\ge0,\,x+c_my\ge g(z)} (Px+Qy+Rz).
\]

**4. Solve the price allocation.** For fixed \(z\), set \(a=Q/c_m\). It is never cheaper to choose \(x>g(z)\), and for \(h_m(z)\le x\le g(z)\) the cheapest permissible rim conductance is \(y=(g(z)-x)/c_m\). The cost becomes \(a g(z)+(P-a)x+Rz\). If \(P<a\), it is strictly minimized at \(x=g(z)\), \(y=0\). If \(P>a\), it is strictly minimized at \(x=h_m(z)\), \(y=(g-h_m)/c_m\). At equality every point of that interval is optimal for fixed \(z\).

For \(P\le a\), the remaining objective \(Pg(z)+Rz=2P+R+P/(z-1)+R(z-1)\) has its unique minimum at \(z=1+\sqrt{P/R}\), with value \(2P+R+2\sqrt{PR}\). For \(P>a\), the remaining objective is
\[
 \Phi(z)=a g(z)+(P-a)h_m(z)+Rz.
\]
Writing \(D(z)=(2m+1)z-(m+1)\), direct differentiation gives
\[
 h_m'(z)=-1/D(z)^2,\quad
 \Phi'(z)=R-a/(z-1)^2-(P-a)/D(z)^2,\quad
 \Phi''(z)=2a/(z-1)^3+2(P-a)(2m+1)/D(z)^3>0.
\]
As \(z\downarrow1\), \(\Phi'(z)\to-\infty\); as \(z\to\infty\), \(\Phi'(z)\to R\). Therefore there is exactly one critical point and it is the unique global minimum. All three regimes, including the equality continuum, follow.

**5. Restore the budget and transfer the rim-screening conclusion.** If \(C_*\) is the minimal price per rim site needed for a unit gap, the minimal total price is \(mC_*\). Scaling all weights by \(B/(mC_*)\) achieves the displayed optimal gap; homogeneity and the previous lower bound show no unrestricted allocation can do better. For any unrestricted optimizer, group averaging must itself be an invariant optimizer; it preserves the sum of rim weights. Since every weight is nonnegative, the invariant \(Y_*=0\) regime forces every actual rim edge to vanish. Conversely, when all invariant optima have \(Y_*>0\), no unrestricted optimum can have all rim edges zero. The equality regime admits both support patterns. Finally, \(c_m\) decreases through one precisely between \(m=6\) and \(m=7\), with \(c_6=1\); setting equal prices yields the stated sharp cutoff and exact weights.

## Verification

The accompanying `VERIFY.py` checks both Fourier-sector characteristic polynomials symbolically, the two exact rational six-rim-site threshold allocations, 84 independent full-Laplacian eigenspectrum-and-budget cases for \(3\le m\le14\), and 48 random-start searches over **independently varying asymmetric edge weights** for \(m\in\{3,4,5,6\}\). The logged output is in `VERIFY_OUTPUT.txt`. These finite tests are independent stress checks and do not substitute for the infinite-family argument in the proof. Run with Python 3 plus NumPy, SciPy and SymPy: `python VERIFY.py`.

## Relationship to prior work

Ghosh and Boyd (available online May 5, 2006) show how symmetry and concavity simplify algebraic-connectivity optimization. Their paper treats broad degree, cut and block-ring graph families, but its block-ring example has no hub or private leaves and does not supply this three-price helm result. Shakeri and collaborators (first arXiv version October 22, 2015) optimize one-to-one *interlayer* weights with fixed component-layer Laplacians; their threshold concerns the coupling budget, not simultaneous priced tuning of a hub, cycle and leaf edges. The proof here uses the established symmetry technique, not as a novelty claim. The additional explicit contribution assessed here is the exact three-price optimum, unique scalar root in the mixed phase, mandatory entire-rim deletion criterion, and the equal-price transition at six rim sites. A broader or equivalent specialist result not located in the consulted sources remains possible.

## Limitations

The prices are homogeneous within three edge orbits; no assertion is made for independent heterogeneous prices, upper edge caps, normalized Laplacians, stochastic SLEM, or robustness against edge failures. The calculation determines the **global optimal objective**, all invariant optima, and the mandatory/nonmandatory rim-support behavior of *all* optimizers; it does not classify all asymmetric optimizer vectors. The implicit scalar root is analytically unique but not generally expressible in a convenient radical formula. Computational checks are finite corroboration, not an infinite certificate. No independent audit has been performed.

## References

1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra and its Applications 418 (2006), 693–707; available online May 5, 2006. https://doi.org/10.1016/j.laa.2006.03.006 ; author-hosted full text https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf .
2. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1, first submitted October 22, 2015. https://arxiv.org/abs/1510.06785 .
