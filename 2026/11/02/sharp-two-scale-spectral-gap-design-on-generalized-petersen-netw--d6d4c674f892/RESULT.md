# Sharp two-scale spectral-gap design on generalized Petersen networks

## Finding
For each integer \(n\ge13\), let \(GP(n,2)\) have vertices \(u_j,v_j\) with indices modulo \(n\), and edges \(u_ju_{j+1}\) (outer), \(v_jv_{j+2}\) (inner), and \(u_jv_j\) (spokes). Independently choose a nonnegative conductance for every edge subject to total conductance at most \(n\). Let \(\Lambda_n\) be the maximum second-smallest eigenvalue of the resulting weighted graph Laplacian, including disconnected designs. Set
\[
 d_n=4\sin^2(2\pi/n),\qquad s_n=2\sin(2\pi/n),\qquad U_n=\frac{d_n}{(1+s_n)^2+1}.
\]
Then **every finite optimum is strictly below the explicit cap**, and that cap is asymptotically optimal through the first correction:
\[
 \boxed{\Lambda_n<U_n},\qquad
 \boxed{\Lambda_n=\frac{8\pi^2}{n^2}-\frac{32\pi^3}{n^3}+O(n^{-4})}\quad(n\to\infty).
\]
The asymptotic formula holds separately along even and odd integers. For either parity, choose any constant \(\alpha>4\pi^2\) (even) or \(\alpha>3\pi^2\) (odd), and put uniform edge conductances
\[
 \boxed{a_n=\frac{\alpha}{n^2}\quad\text{(outer)},\quad c_n=\frac{2\pi}{n}\quad\text{(spokes)},\quad b_n=1-a_n-c_n\quad\text{(inner)}.}
\]
For every sufficiently large integer of that parity these are positive, have total conductance \(n\), and attain the displayed two-term optimum (with error \(O(n^{-4})\)), **against unrestricted nonuniform edge conductances**.

There is also an asymptotically necessary scale law. For any sequence of feasible designs on one fixed parity with algebraic connectivity \(\Lambda_n+o(n^{-3})\), let \(a_n,b_n,c_n\) denote their edge conductance averages over the three types (whether or not the individual edges have equal weights). Necessarily
\[
 a_n=o(n^{-1}),\qquad nc_n\longrightarrow2\pi,\qquad
 \liminf_{n\to\infty}n^2a_n\ge
 \begin{cases}4\pi^2,&n\text{ even},\\3\pi^2,&n\text{ odd}.
 \end{cases}
\]
The threshold on the outer-ring coefficient is sharp as a strict-feasibility boundary: every fixed coefficient strictly above its parity threshold supports the stated two-term optimal construction. No exact finite-\(n\) optimizer formula, or uniqueness of optimal conductances, is asserted.

## Assumptions and scope
The graph is undirected and has \(2n\) vertices and \(3n\) distinct edges for \(n\ge13\). Laplacian entries have the standard convention \(L_{ij}=-w_{ij}\) off the diagonal, with each diagonal equal to its incident conductance sum. Edge conductances are individually nonnegative, with no imposed symmetry; disconnected designs are allowed and have second eigenvalue zero. The maximum exists because the finite-dimensional feasible simplex is compact. The budget is \(n\) conductance units and all edges have identical unit price. An optimal connected design saturates this budget because uniform dilation increases each nonzero Laplacian eigenvalue.

For comparison, averaging an arbitrary design's weights around each of the three cyclic edge orbits gives type means \((a,b,c)\), with \(a,b,c\ge0\) and \(a+b+c\le1\). Any Fourier trial vector with constant amplitudes on each orbit has exactly the same Rayleigh quotient for the original design and for this orbit-averaged design. In particular, trial-vector upper bounds derived below apply to **all** independently weighted designs, not only symmetric ones. The construction supplies a lower bound; it does not require proving that every optimizer is symmetric.

## Proof
### Fourier decomposition for uniform edge types
For type-constant conductances \((a,b,c)\), take the Fourier frequency \(\omega^j\), \(\omega=e^{2\pi i/n}\), and put
\[
 e_k=4\sin^2(\pi k/n),\quad d_k=4\sin^2(2\pi k/n),\quad
 H_k=\begin{pmatrix}a e_k+c&-c\\-c&b d_k+c\end{pmatrix}.
\]
The eigenvalues of \(H_k\) are
\[
 \ell_\pm(k)=c+\frac{a e_k+b d_k}{2}\pm
 \sqrt{c^2+\frac{(a e_k-b d_k)^2}{4}}.
\]
At \(k=0\) the eigenvalues are \(0,2c\), hence
\[
 \lambda_2=\min\{2c,\min_{1\le k<n}\ell_-(k)\}.
\]
This follows by applying the discrete Fourier transform to the two vertex layers; it includes the disconnected cases.

### A universal sharp-asymptotic upper certificate
Write \(e=e_1\), \(d=d_1\), and \(s=\sqrt d\). For any edge weights, assign the trial-vector amplitudes \((1+s)\omega^j\) to \(u_j\) and \(\omega^j\) to \(v_j\). The vector is orthogonal to constants. Its Rayleigh quotient is
\[
 R=\frac{a e(1+s)^2+(b+c)d}{(1+s)^2+1}
 \le\frac{d-a[d-e(1+s)^2]}{(1+s)^2+1}.
\]
For all \(n\ge13\), \(e(1+s)^2<d\). Indeed, with \(t=\pi/n\), this is equivalent to \(g(t)=2\cos t-1-2\sin(2t)>0\). On \(0\le t\le22/91\), \(g'(t)=-2\sin t-4\cos(2t)<0\). Since \(\pi/13<22/91\), the elementary bounds \(2\cos T\ge2-T^2\), \(\sin(2T)\le2T-(2T)^3/6+(2T)^5/120\), at \(T=22/91\), yield
\[
 g(t)\ge 1-T^2-4T+\frac83T^3-\frac8{15}T^5
 =\frac{1100762249}{93604821765}>0.
\]
Thus \(\lambda_2\le R<U_n\) if \(a>0\). When \(a=0\) and \(n\) is even, the inner skip-two edges form two disconnected parity components (together with their spokes), so the gap is zero. When \(a=0\) and \(n\) is odd, the Fourier frequency \(k=(n-1)/2\) with equal layer amplitudes gives \(\lambda_2\le b e/2\le e/2<U_n\): here \((1+s)^2+1<5\) whereas \(2d/e=8\cos^2(\pi/n)>6\). These strict estimates also cover every nonuniform design because all trial-vector quotients depend only on its three edge-type averages. The compact maximum is therefore strictly below \(U_n\).

Taylor expansion at infinity gives
\[
 d=\frac{16\pi^2}{n^2}+O(n^{-4}),\qquad
 U_n=\frac{8\pi^2}{n^2}-\frac{32\pi^3}{n^3}+O(n^{-4}).
\]

### A matching design and the parity boundary
Choose \(a=\alpha/n^2\), \(c=2\pi/n\), \(b=1-a-c\), with \(\alpha\) above the indicated parity threshold. The constant-mode positive eigenvalue is \(2c\), larger than order \(n^{-2}\). For a fixed nonzero integer \(j\), the low-frequency modes \(k=j\) or \(k=n-j\) satisfy
\[
 n^2\ell_-(k)\longrightarrow8\pi^2j^2.
\]
For modes at bounded distance \(j\) from \(n/2\), where \(j\) is an integer on even \(n\) and a half-integer on odd \(n\),
\[
 n^2\ell_-(k)\longrightarrow 2\alpha+8\pi^2j^2.
\]
In particular, the lowest competing high-frequency limit is \(2\alpha\) for even \(n\), and \(2\alpha+2\pi^2\) for odd \(n\). The strict conditions on \(\alpha\) put both limits above \(8\pi^2\).

There are no escaping intermediate modes. Writing \(A=a e_k\), \(B=b d_k\), we have \(\det H_k=AB+c(A+B)\) and \(\ell_+(k)\le A+B+2c\), so
\[
 \ell_-(k)\ge\frac{c(A+B)}{A+B+2c}.
\]
If the cyclic distances from \(k\) to both \(0\) and \(n/2\) tend to infinity, then \(n^2B\to\infty\) and \(n^2c\to\infty\), making \(n^2\ell_-(k)\to\infty\). The fixed-center alternatives above therefore show that for all sufficiently large \(n\), only modes \(k=1,n-1\) can realize the spectral gap. At \(k=1\), \(A=O(n^{-4})\), \(B=d(1-2\pi/n)+O(n^{-4})\), and \(c=2\pi/n\); direct expansion yields
\[
 \ell_-(1)=\frac{A+B}{2}-\frac{(A-B)^2}{8c}+O(n^{-5})
 =\frac{8\pi^2}{n^2}-\frac{32\pi^3}{n^3}+O(n^{-4}).
\]
Combining this constructive lower bound with the universal upper bound proves the two-term optimum, including unrestricted competitors.

### Necessity of the two scales
Consider any feasible parity-restricted sequence satisfying \(\lambda_2=\Lambda_n+o(n^{-3})\), and denote its orbit means by \(a,b,c\). The upper-certificate margin gives
\[
 U_n-\lambda_2\ge\frac{a[d-e(1+s)^2]}{(1+s)^2+1}=\Theta(a/n^2),
\]
where the implicit coefficient tends to a strictly positive constant. As \(U_n-\lambda_2=o(n^{-3})\), this forces \(a=o(n^{-1})\). The equal-amplitude trial at frequency \(1\) gives \(\lambda_2\le(ae+bd)/2\le d(1-c)/2\), hence \(c=O(n^{-1})\).

The smallest eigenvalue of \(H_1\) is another admissible Rayleigh upper certificate for the original inhomogeneous design. Write \(A=ae=o(n^{-3})\), \(B=bd=d+O(n^{-3})\). Since \(n^2\lambda_2\to8\pi^2\), the exact formula for \(\ell_-(1)\) forces \(c/d\to\infty\), for otherwise it stays a fixed fraction below \(d/2\). If \(nc\to0\), the expansion valid when \(c/d\to\infty\) implies the loss \(d/2-\ell_-(1)\) has order at least \(d^2/c\), larger than order \(n^{-3}\); thus \(nc\) stays bounded above and away from zero. Along any subsequence with \(nc\to\gamma>0\),
\[
 n^3\left(\frac d2-\ell_-(1)\right)
 \longrightarrow8\pi^2\gamma+\frac{32\pi^4}{\gamma}
 \ge32\pi^3,
\]
with equality only at \(\gamma=2\pi\). Since \(\lambda_2\le\ell_-(1)\) and the optimum has the deficit \(32\pi^3/n^3+O(n^{-4})\), only equality is permitted; hence \(nc\to2\pi\).

For even \(n\), the Fourier mode \(k=n/2\) with equal layer amplitudes gives \(\lambda_2\le2a\); for odd \(n\), \(k=(n-1)/2\) similarly gives
\[
 \lambda_2\le 2a\cos^2\!\left(\frac\pi{2n}\right)+2b\sin^2\!\left(\frac\pi n\right).
\]
Since \(n^2\lambda_2\to8\pi^2\), these imply respectively \(\liminf n^2a\ge4\pi^2\) and \(\liminf n^2a\ge3\pi^2\). The stated constructions show sharpness of these limiting thresholds.

## Verification
The accompanying `verify.py` checks the Fourier decomposition against full weighted Laplacians, the upper certificate for many feasible weights, and the two-term asymptotic for both parity classes. It uses Python and NumPy and prints a deterministic PASS count. Its output is supplementary finite evidence only: the all-\(n\), unrestricted-conductance claim and the limit laws depend on the analytic proof above. Run with `python verify.py` from the extracted package directory.

## Relationship to prior work
The unweighted spectral description of \(GP(n,k)\) appears in Gera and Stănică (2011) and Dudek (2014). The Fourier blocks above adapt that structural diagonalization to three conductance classes, while the optimization problem permits every edge to be chosen independently. Boyd (2006) supplies a general convex spectral-gap network-design framework but no explicit parity-dependent two-scale optimum for this graph. Shakeri and collaborators (2015) analyze spectral-gap optimization by adding or tuning interconnection edges between given networks, in contrast to simultaneous allocation across all three edge sets. The earlier paper titled *Optimal Generalized Petersen Graphs* by Beenker and van Lint (1988) concerns graph size and diameter, not optimized weighted Laplacian gaps. These are statement/implication distinctions, not novelty established solely from a title search.

## Limitations
The exact finite optimal weights and uniqueness are not established; the construction is only two-term asymptotically optimal. The graph family is \(GP(n,2)\) with \(n\ge13\), nonnegative independent undirected conductances, uniform edge price, and total budget \(n\). No claim is made for other inner jump sizes, degree caps, stochastic mixing times, or arbitrary edge prices. Positive conductance is not required for every edge in the admissible class, though the displayed construction is strictly positive for sufficiently large \(n\). Relevant specialist literature may contain equivalent results not located in the inspected sources; an independent mathematical and originality audit remains unperformed.

## References
1. W. Dudek, *On the Spectrum of the Generalised Petersen Graphs*, arXiv:1412.3531v1 (publicly posted December 11, 2014), https://arxiv.org/abs/1412.3531.
2. R. Gera and P. Stănică, *The Spectrum of Generalized Petersen Graphs*, Australasian Journal of Combinatorics 49 (2011), 39–45.
3. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians (2006), https://web.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf.
4. H. Shakeri et al., *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (2015), https://arxiv.org/abs/1510.06785.
5. G. F. Beenker and J. H. van Lint, *Optimal Generalized Petersen Graphs* (1988), https://pure.tue.nl/ws/files/2043783/593427.pdf.
