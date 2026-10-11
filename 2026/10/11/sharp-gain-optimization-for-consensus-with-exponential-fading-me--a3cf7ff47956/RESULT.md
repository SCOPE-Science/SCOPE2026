# Sharp gain optimization for consensus with exponential fading memory

## Finding

**Theorem (extremal-mode principle and optimal gain).** Let \(L\) be the symmetric weighted Laplacian of an undirected connected graph on \(N\ge2\) vertices, with ordered eigenvalues
\[
0=\ell_1<\ell_2=\alpha\le\cdots\le\ell_N=\beta.
\]
For \(\lambda,b>0\), \(a\ge0\), and any bounded continuous history \(x:(-\infty,0]\to\mathbb R^N\), consider the unique continuation satisfying
\[
\dot x(t)=-aLx(t)-bL\int_0^\infty\lambda e^{-\lambda s}x(t-s)\,ds,\qquad t\ge0.
\]
Write \(\bar x=N^{-1}\sum_jx_j(0)\) and let \(R(a)\) be the **optimal spectral exponential decay exponent**, meaning the supremum of the numbers \(r\) for which all trajectories satisfy \(\|x(t)-\bar x\mathbf1\|\le C_xe^{-rt}\) for \(t\ge0\), with a prefactor permitted to depend on the history.

Define for every \(u>0\)
\[
D_u(a)=(\lambda-au)^2-4\lambda bu,\qquad
r_u(a)=\frac{\lambda+au-\sqrt{\max\{D_u(a),0\}}}{2}.
\]
Then the **entire graph's optimal decay exponent is controlled by only the two extreme nonzero Laplacian eigenvalues**:
\[
\boxed{R(a)=\min\{r_\alpha(a),r_\beta(a)\}.}
\]
If \(\alpha<\beta\), \(R(a)\) is strictly increasing up to one unique positive gain, then strictly decreasing thereafter. Its maximizer and maximum are
\[
\boxed{
 a_* =\frac{\lambda\beta+\sqrt{\lambda^2(\beta-\alpha)^2+4\lambda b\alpha\beta(2\beta-\alpha)}}{\alpha(2\beta-\alpha)},
 \qquad R_*=\frac{\lambda+\alpha a_*}{2}.}
\]
At \(a_*\), the \(\alpha\)-mode has distinct complex-conjugate characteristic roots, the \(\beta\)-mode has two distinct real roots, and all histories satisfy an **attained** estimate \(\|x(t)-\bar x\mathbf1\|\le C_xe^{-R_*t}\). No larger common exponent is possible.

If \(\alpha=\beta=\ell\), the unique maximizing gain is
\[
a_*=(\lambda+2\sqrt{\lambda b\ell})/\ell,
\qquad R_*=\lambda+\sqrt{\lambda b\ell}.
\]
Here \(R_*\) is the sharp **supremal** exponent: at the repeated characteristic root, some histories have a nonzero \(te^{-R_*t}\) factor, so a bound at the endpoint exponent itself cannot hold for every history.

In both cases \(\lim_{a\to\infty}R(a)=\lambda\): increasingly strong instantaneous interaction ultimately slows the convergence rate toward the memory relaxation rate rather than making it arbitrarily fast.

## Assumptions and scope

The graph is finite, fixed, connected and undirected with nonnegative symmetric edge weights. The instantaneous and memory couplings use the **same** graph Laplacian. The history is real-valued, bounded and continuous over the full past; the exponential memory kernel is exactly \(\lambda e^{-\lambda s}\). The prefactor \(C_x\) is not claimed uniform over unbounded collections of histories. The stated sharp rate concerns the positions \(x(t)\), not just an unobservable auxiliary state.

## Proof

**1. Exact finite-dimensional reduction and attainability of modal initial conditions.** Set
\[
m(t)=\int_0^\infty\lambda e^{-\lambda s}x(t-s)\,ds.
\]
The bounded-history convolution is well defined; direct differentiation of the equivalent past integral gives \(\dot m=\lambda(x-m)\). Thus the system is exactly \(\dot x=-aLx-bLm\), \(\dot m=\lambda(x-m)\). The arithmetic mean of \(x\) is conserved. Orthogonal diagonalization of \(L\) gives, for each \(u=\ell_j>0\), the block
\[
\frac d{dt}\begin{pmatrix}X\\M\end{pmatrix}=
\begin{pmatrix}-au&-bu\\\lambda&-\lambda\end{pmatrix}
\begin{pmatrix}X\\M\end{pmatrix},\qquad
p_u(z)=z^2+(\lambda+au)z+\lambda u(a+b).
\]
All roots have negative real part by the quadratic Hurwitz criterion. The least positive magnitude of their real parts is precisely \(r_u(a)\). Every modal initial pair \((X_0,M_0)\) is achievable with a bounded continuous past: choosing \(X(t)=X_0+2(M_0-X_0)(1-e^{\lambda t})\) for \(t\le0\) gives the prescribed convolution value \(M_0\). Moreover no eigenvector of the modal matrix has vanishing position coordinate, since \(bu>0\). Consequently its slowest eigenvalue (or Jordan vector at a repeated root) is observable in \(x\). This proves sharpness of the spectral exponent for all histories, including the endpoint caveat at a repeated root.

**2. Affine-in-eigenvalue test and endpoint bottleneck.** A mode has spectral rate at least \(r\ge0\) exactly when the shifted polynomial \(p_u(z-r)\) has both roots in the closed left half-plane. Its coefficients are
\[
 p_u(z-r)=z^2+B_u(r)z+C_u(r),\quad
 B_u(r)=\lambda+au-2r,\quad
 C_u(r)=r(r-\lambda)+u[\lambda(a+b)-ar].
\]
For a real monic quadratic this closed-half-plane condition is **equivalent** to \(B_u(r)\ge0\) and \(C_u(r)\ge0\). Both quantities are affine in \(u\). Hence if \(r\) does not exceed the rates at \(\alpha\) and \(\beta\), those two inequalities hold for every \(u\in[\alpha,\beta]\). The endpoints themselves are eigenvalues, establishing \(R(a)=\min\{r_\alpha(a),r_\beta(a)\}\) exactly. This argument handles both real and complex characteristic roots without interpolation errors.

**3. Shape of an individual mode.** For \(u>0\) define
\[
a_u^c=\frac{\lambda+2\sqrt{\lambda bu}}{u}.
\]
The discriminant vanishes at \(a_u^c\), and \(r_u(a_u^c)=\lambda+\sqrt{\lambda bu}\). In any complex-root interval, \(r_u(a)=(\lambda+au)/2\), which strictly increases with \(a\). In any real-root interval, the smaller positive decay root \(r=r_u(a)\) obeys \(r^2-(\lambda+au)r+\lambda u(a+b)=0\), whence
\[
\frac{dr}{da}=\frac{u(\lambda-r)}{\sqrt{D_u(a)}}.
\]
In the lower real-root interval \(r<\lambda\), so this derivative is positive; in the upper interval \(a>a_u^c\), \(r>\lambda\), so it is negative. A possible lower discriminant zero has continuous monotone passage. Therefore \(r_u\) increases strictly up to \(a_u^c\), decreases strictly afterward, and has the stated unique maximum.

**4. Unique two-endpoint crossing.** Suppose \(\alpha<\beta\). The function \(u\mapsto a_u^c=\lambda/u+2\sqrt{\lambda b}/\sqrt u\) strictly decreases, so \(a_\beta^c<a_\alpha^c\). At \(a=a_\beta^c\),
\[
r_\alpha(a)\le\lambda+\sqrt{\lambda b\alpha}
<\lambda+\sqrt{\lambda b\beta}=r_\beta(a).
\]
At \(a=a_\alpha^c\), put \(s=\sqrt{\lambda b\alpha}\) and \(v=\lambda+s\). The positive-decay characteristic polynomial is \(P_u(v)=v^2-(\lambda+au)v+\lambda u(a+b)\). Using \(P_\alpha(v)=0\),
\[
 P_\beta(v)=(\beta-\alpha)[\lambda(a+b)-av]
 =-\frac{(\beta-\alpha)s(\lambda+s)}{\alpha}<0.
\]
Thus \(v\) lies between the two real decay roots for the \(\beta\)-mode, and \(r_\beta(a)<r_\alpha(a)\). On \([a_\beta^c,a_\alpha^c]\), the \(\alpha\)-mode rate strictly increases and the \(\beta\)-mode rate strictly decreases, so there is exactly one crossing; before that interval both rates increase, and after it both decrease. This crossing uniquely maximizes their minimum.

At the crossing, \(a>a_\beta^c\) implies \(r_\beta>\lambda\); hence \(r_\alpha>\lambda\). Since \(a<a_\alpha^c\), the \(\alpha\)-mode must lie in its complex-root region (the lower real-root region has \(r_\alpha<\lambda\)), while \(\beta\) lies in its upper real-root region. The equality of rates is therefore equivalent to
\[
\sqrt{(\lambda-a\beta)^2-4\lambda b\beta}=a(\beta-\alpha).
\]
Squaring and rearranging gives
\[
\alpha(2\beta-\alpha)a^2-2\lambda\beta a+\lambda^2-4\lambda b\beta=0.
\]
Its smaller root is at most \(\lambda/(2\beta-\alpha)<\lambda/\beta<a_\beta^c\), so the crossing in \( (a_\beta^c,a_\alpha^c)\) must be the larger root, exactly \(a_*\) above. At the crossing neither endpoint block is defective; any interior defective mode has strictly larger spectral rate by Step 2. Finite-dimensional matrix exponentiation therefore gives the exact \(e^{-R_*t}\) bound. For \(\alpha=\beta\), Step 3 gives the asserted exceptional-root maximum. Finally, the smaller positive modal decay root tends to \(\lambda\) as \(a\to\infty\), yielding the limit of \(R(a)\).

## Verification

For the three-vertex path with unit edge weights, \(\sigma(L)=\{0,1,3\}\). Taking \(\lambda=b=1\), the theorem gives
\[
a_*=\frac{3+\sqrt{4+60}}5=\frac{11}{5},
\qquad R_*=\frac85.
\]
The discriminants are exactly \(D_1(a_*)=-64/25\) and \(D_3(a_*)=484/25\), giving both modal rates \(8/5\). `CHECK.py` reproduces this rational certificate and numerical stress tests of the endpoint reduction and crossing identities. These numerical tests are only supplemental; the universally quantified statements follow from Steps 1–4.

## Relationship to prior work

Pignotti and Wang, arXiv:2609.02454v1 (first public September 2, 2026; primary MSC 34D05), prove unconditional exponential consensus for nonlinearly interacting agents with infinite fading memory, including simultaneous instantaneous and memory forces (Theorems 3.3 and 3.4). Their results do not provide the exact homogeneous-exponential modal decay law or a maximizing instantaneous gain. The present theorem treats the narrower fixed symmetric Laplacian and common exponential kernel, extracting a sharp rate and a network-wide optimum.

Moradian and Kia, arXiv:1912.04442v1, optimize convergence rates for a **point-delay** affine split between current and outdated Laplacian feedback using Lambert-W roots; their characteristic equation and optimization variable are different. Kempton, Herrmann and di Bernardo (2017) optimize graph **edge weights** to improve robustness to a discrete delay, not the present gain for a fixed network with an exponential convolution. Qiao and Sipahi (2013) study rightmost eigenvalues with a homogeneous single delay; only the accessible abstract was compared. These related contributions motivate the extremal-eigenvalue comparison but do not, in their inspected statements, supply the formula proved here.

## Limitations

The optimization is over the single scalar instantaneous gain \(a\), with \(b\), \(\lambda\), and \(L\) fixed. It does not address optimizing control effort, changing graph weights, directed or switching graphs, heterogeneous kernels, discrete delays, or nonlinear state-dependent communication. The degenerate equal-eigenvalue graph has a Jordan prefactor at its maximizing gain. The originality assessment is limited to accessible literature and cannot exclude an equivalent result expressed through different control-theoretic notation.

## References

1. C. Pignotti and Y.-Q. Wang, *Exponential Consensus and Flocking in Multi-Agent Systems with Infinite Fading Memory*, arXiv:2609.02454v1 (2026), https://arxiv.org/html/2609.02454v1 .
2. H. Moradian and S. S. Kia, *A Study on Accelerating Average Consensus Algorithms Using Delayed Feedback*, arXiv:1912.04442v1 (2019), https://arxiv.org/pdf/1912.04442 .
3. L. C. Kempton, G. Herrmann and M. di Bernardo, *Distributed optimisation and control of graph Laplacian eigenvalues for robust consensus via an adaptive multilayer strategy*, Int. J. Robust Nonlinear Control 27 (2017), 1499–1525, https://doi.org/10.1002/rnc.3808 .
4. W. Qiao and R. Sipahi, *A Linear Time-Invariant Consensus Dynamics with Homogeneous Delays: Analytical Study and Synthesis of Rightmost Eigenvalues*, SIAM J. Control Optim. 51 (2013), https://doi.org/10.1137/110832574 .
