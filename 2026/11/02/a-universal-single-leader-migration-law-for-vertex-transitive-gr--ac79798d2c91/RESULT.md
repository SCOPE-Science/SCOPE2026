# A universal single-leader migration law for vertex-transitive graph cones

## Finding

A weighted clique cone is the join of a clique of \(r\ge1\) hub vertices and a connected vertex-transitive graph \(H\) on \(m\ge2\) peripheral vertices. Hub–hub and hub–peripheral edges have unit conductance; every edge of \(H\) has common multiplier \(t>0\) relative to its fixed positive symmetric edge conductance. Exactly one vertex is grounded as a noise-free leader. Its cost is the trace of the inverse grounded combinatorial Laplacian, \(J(v;t)=\operatorname{tr}(L_{V\setminus\{v\},V\setminus\{v\}}^{-1})\).

Write the Laplacian eigenvalues of \(H\), including multiplicities, as \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_m\), and put \(N=r+m\) and
\[
\Phi(t)=\sum_{j=2}^{m}\frac{1}{r+t\lambda_j}.
\]
All hubs have a common cost \(J_{\rm hub}\), and all peripheral vertices have a common cost \(J_{\rm periphery}\). Their **exact difference** is
\[
\boxed{J_{\rm periphery}(t)-J_{\rm hub}(t)=\frac{N}{m}\left(\Phi(t)-\frac{m-1}{N}\right).}
\]
There is exactly one critical \(t_*\in(0,\infty)\) characterized by
\[
\boxed{\Phi(t_*)=\frac{m-1}{r+m}.}
\]
For \(0<t<t_*\) the complete set of minimizing leaders is precisely the hub clique; for \(t>t_*\) it is precisely the peripheral vertex orbit; at \(t=t_*\) **every vertex ties**. The threshold satisfies
\[
\frac{m}{\lambda_m}\le t_*\le\frac{m}{\lambda_2},
\]
with equality in either inequality only when all nonzero eigenvalues of \(H\) coincide. In particular, for a complete peripheral graph \(H=K_m\), \(t_*=1\) for every number \(r\) of hubs.

For a cycle peripheral graph \(H=C_m\), \(m\ge3\), and any **fixed** number \(r\ge1\) of hubs, the threshold has a sharp two-term asymptotic. Let \(y_r>0\) be the unique root of \(y_r\coth y_r=r+1\). Then
\[
\boxed{t_*(r,C_m)=\frac{r}{4y_r^2}\,m^2+\frac{r^2(r+1)}{2y_r^2\bigl(y_r^2-r(r+1)\bigr)}\,m+O_r(1).}
\]
Both displayed coefficients are strictly positive. For one hub, they are approximately \(0.06817086453\) and \(0.16355226001\), respectively.

## Assumptions and scope

The finite peripheral graph \(H\) is undirected, connected, vertex-transitive under automorphisms preserving fixed edge conductances, with at least two vertices. Its Laplacian is \(L_H\). An unweighted vertex-transitive graph is a special case. Every hub–hub and hub–peripheral edge is present at unit conductance. Each peripheral edge receives conductance \(t\) times its specified positive base conductance. Exactly one vertex is perfectly pinned (grounded); remaining vertices are followers. Graph sizes \(r,m\) are integers subject to \(r\ge1,m\ge2\); multiplier \(t\) is arbitrary positive. The cycle asymptotic holds with \(r\) fixed and \(m\to\infty\), not uniformly for growing \(r\). The cost is unnormalized \(\operatorname{tr}(L_{FF}^{-1})\); any common positive physical noise factor does not change minimizers.

## Proof

**1. Green-function relation to one-leader cost.** For a connected weighted graph of order \(N\), let \(L^\dagger\) be the Moore–Penrose inverse. The diagonal of the inverse Laplacian grounded at \(v\) equals the effective resistance \(R_{uv}\) from \(u\) to \(v\). Hence
\[
J(v)=\sum_{u\ne v}R_{uv}=\operatorname{tr}(L^\dagger)+N(L^\dagger)_{vv},
\]
because \(R_{uv}=(L^\dagger)_{uu}+(L^\dagger)_{vv}-2(L^\dagger)_{uv}\) and \(L^\dagger\mathbf1=0\).

**2. Spectrum and diagonal blocks.** Write vectors as hub and peripheral blocks. The weighted cone Laplacian is
\[
L=\begin{pmatrix}N I_r-\mathbf1_r\mathbf1_r^\top&-\mathbf1_r\mathbf1_m^\top\\-\mathbf1_m\mathbf1_r^\top&rI_m+tL_H\end{pmatrix}.
\]
Here the upper-left block equals \(mI_r+(rI_r-\mathbf1_r\mathbf1_r^\top)\). An orthogonal decomposition gives the all-ones zero mode; the \((r-1)\)-dimensional hub-difference space at eigenvalue \(N\); the one-dimensional hub–peripheral contrast at eigenvalue \(N\); and the peripheral mean-zero eigenmodes at eigenvalues \(r+t\lambda_j\), \(j=2,\ldots,m\). The hub–peripheral contrast unit projector has hub diagonal \(m/(rN)\), peripheral diagonal \(r/(mN)\). Therefore every hub diagonal of \(L^\dagger\) equals
\[
\frac{r-1}{rN}+\frac{m}{rN^2}=\frac{N-1}{N^2}.
\]
Every peripheral diagonal equals
\[
\frac{r}{mN^2}+\frac{\Phi(t)}m.
\]
For the last equality, vertex transitivity ensures the diagonal of every spectral function of \(L_H\) is constant on peripheral vertices; the sum of these diagonal entries is its trace \(\Phi(t)\). Subtracting the two diagonals and multiplying by \(N\) gives the claimed exact cost difference.

**3. Unique crossing and spectral bounds.** The function \(\Phi\) is continuous and strictly decreasing, with \(\Phi(0^+)=(m-1)/r>(m-1)/(r+m)\) and \(\Phi(+\infty)=0\). Thus it crosses the target exactly once. The sign of the cost difference gives every optimizer and every tie. At crossing, bounding each spectral denominator between those formed with \(\lambda_2\) and \(\lambda_m\) yields
\[
\frac{m-1}{r+t_*\lambda_m}\le\frac{m-1}{r+m}\le\frac{m-1}{r+t_*\lambda_2},
\]
whence the asserted bounds. Strictness follows unless all positive eigenvalues coincide. For \(H=K_m\), every nonzero eigenvalue is \(m\), so the defining equation gives \(t_*=1\).

**4. Cycle asymptotic and the linear correction.** For \(H=C_m\), the eigenvalues are \(4\sin^2(\pi k/m)\), \(k=0,\ldots,m-1\). Let
\[
F_m(t)=r\sum_{k=0}^{m-1}\frac1{r+4t\sin^2(\pi k/m)}.
\]
The root equation is precisely \(F_m(t_*)=1+r(m-1)/(r+m)\). The finite-cycle resolvent identity obtained by factoring the discrete Fourier resolvent into a geometric series reads
\[
F_m(t)=\frac{m\sqrt r}{\sqrt{r+4t}}\coth\!\left(m\operatorname{arsinh}\!\frac{\sqrt r}{2\sqrt t}\right).
\]
For \(t=cm^2+dm\), \(c>0\) fixed, put \(z=m\sqrt r/(2\sqrt t)\). Since \(\operatorname{arsinh}(z/m)=z/m+O_r(m^{-3})\) and \(m\sqrt r/\sqrt{r+4t}=z+O_r(m^{-2})\), uniformly for \(c,d\) in compact positive-range neighborhoods,
\[
F_m(cm^2+dm)=z\coth z+O_r(m^{-2}).
\]
The target admits the expansion
\[
1+\frac{r(m-1)}{r+m}=(r+1)-\frac{r(r+1)}m+O_r(m^{-2}).
\]
Set \(f(z)=z\coth z\). It increases strictly from \(1\) to infinity: \(f'(z)=\coth z-z\operatorname{csch}^2 z>0\) for all \(z>0\), since \(\sinh(2z)>2z\). Thus there is a unique \(y_r>0\) with \(f(y_r)=r+1\). Equating constant terms gives \(c=r/(4y_r^2)\). Since
\[
z=y_r-\frac{y_r d}{2c\,m}+O_r(m^{-2}),
\]
matching coefficients of \(1/m\) yields \(y_r f'(y_r)d/(2c)=r(r+1)\), and
\[
y_r f'(y_r)=y_r^2-r(r+1)>0.
\]
The explicit value of \(d\) follows. The derivative of the rescaled root equation in the \(t/m^2\) variable is nonzero at \(c\); its uniform local Taylor expansion through order \(m^{-2}\) converts the truncated identity into an actual \(O_r(1)\) remainder in \(t_*\). This establishes the two-term formula and positivity.

## Verification

The accompanying `VERIFY.py` constructs full grounded Laplacians independently of the spectral proof and compares exact rational inverse traces. It passed 126 exact comparison identities, 210 symmetry comparisons, 16 cycle spectral threshold/bound checks, and 16 numerical quadratic-plus-linear asymptotic comparisons (see `VERIFY_OUTPUT.txt`). It checks finite inputs only; all-size validity comes from the preceding proof. To reproduce, run `python VERIFY.py` with Python 3, SymPy, NumPy, and SciPy in the directory containing the two verification files.

## Relationship to prior work

Fitch and Leonard [1] establish a general joint-centrality formula for leader selection in noisy consensus and its relation to effective resistance; their first version was publicly available on 2014-07-07. Patterson, McGlohon, and Dyagilev [2] give optimal weighted path/cycle leader algorithms. Bapat and Gupta [3] derive effective-resistance identities for wheel and fan graphs. Those general identities motivate the present question and can in principle be combined to study a particular wheel. The finding here is the **single strict hub-to-periphery crossing for every connected vertex-transitive peripheral network and arbitrary clique size**, with exact spectral bounds and the sharp linear finite-size correction for cycle cones. The general resistance/grounded-inverse machinery itself is not claimed as new. No inspected prior source states this combined classification and two-term asymptotic; specialist coverage remains possible.

## Limitations

The peripheral graph must be connected and vertex-transitive with fixed automorphism-invariant edge weights, so a single scalar comparison suffices. The conductance constraints apply to three prescribed edge classes, not arbitrary individual edge variables. The finding does not solve multiple-leader placement or non-transitive peripheral graphs. The asymptotic is established for fixed hub number only. Exact publication priority is not proven by literature search, and no independent scientific audit has been performed.

## References

[1] K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submitted 2014-07-07, https://arxiv.org/abs/1407.1569.

[2] S. Patterson, Y. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, 2014, https://arxiv.org/abs/1412.6595.

[3] R. B. Bapat and S. Gupta, *Resistance Distance in Wheels and Fans*, Indian Journal of Pure and Applied Mathematics 41 (2010), 1–13.
