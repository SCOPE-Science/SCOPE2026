# Exact fastest mixing on the second power of every finite cycle

## Finding

Let \(n\ge5\) and \(G=C_n^2\) be the undirected graph on \(\mathbb Z/n\mathbb Z\) in which distinct vertices are adjacent when their cyclic separation is one or two. Self-loops are permitted. Among **all** real symmetric, nonnegative, row-stochastic transition matrices supported on \(G\) and its loops, the minimum second-largest eigenvalue modulus (SLEM) and an optimizing transition matrix have the following exact formulas.

For \(n=5\), the graph is complete: the unique optimum is \(P=J_5/5\), with SLEM zero. For every \(n\ge6\), define

\[
 h=\lfloor n/2\rfloor,\qquad j=\lfloor(n+2)/4\rfloor,
 \qquad u=\cos(2\pi/n),\quad
 \ell=\cos(2\pi h/n),\quad
 v=\cos(2\pi j/n),
\]
\[
 \Delta=(v-\ell)(u-v),\qquad
 T=\Delta+2(1-\ell)(1-u).
\]

Write \(S\) for the forward cyclic permutation matrix. There is an optimal chain

\[
 P_*=p_0 I+p_1(S+S^{-1})+p_2(S^2+S^{-2})
\]

with the **unique optimum among dihedrally invariant chains** given by

\[
 \boxed{p_1=-\frac{u+\ell}{T},\qquad
 p_2=\frac1{2T},\qquad
 p_0=\frac{\Delta+1+2u\ell}{T}},
 \qquad
 \boxed{\mu_*(n)=\frac\Delta T}.
\]

All three weights are strictly positive for every finite \(n\ge6\). The result is global: no spatially inhomogeneous symmetric stochastic chain on this support can have a smaller SLEM. We do **not** claim uniqueness among all such inhomogeneous optimizers.

Furthermore, as \(n\to\infty\),

\[
 1-\mu_*(n)=\frac{8\pi^2}{n^2}+O(n^{-4}),\qquad
 p_2\longrightarrow\frac12,
\]
\[
 n^2p_1\longrightarrow
 \begin{cases}2\pi^2,&n\text{ even},\\[2pt]
 3\pi^2/2,&n\text{ odd}.
 \end{cases}
\]

Here the last display means limits along the even and odd subsequences. The optimal next-nearest-neighbor weight tends to \(1/2\), while the essential one-step links and holding probability vanish. For comparison, the optimal ordinary one-hop cycle has gap asymptotic to \(2\pi^2/n^2\); thus the best two-hop spectral gap is asymptotically four times as large.

## Assumptions and scope

The problem minimizes \(\mu(P)=\|P-J_n/n\|_2\), where \(P=P^{\mathsf T}\), \(P\mathbf1=\mathbf1\), \(P\ge0\) entrywise, and \(P_{xy}=0\) if \(x\ne y\) and cyclic separation exceeds two. Every positive off-diagonal entry is an individual transition probability, not a total over both directions. The range \(n\ge6\) ensures that \(\pm1\) and \(\pm2\) are four distinct neighbors. The exceptional complete graph \(n=5\) is treated separately. No stationarity masses other than the uniform masses, no directed transition rules, and no other performance objective are asserted.

## Proof

**1. Reduction without imposing equal edge weights.** The objective \(\mu(P)=\|P-J_n/n\|_2\) is convex and invariant under simultaneous permutation of rows and columns. Average any feasible \(P\) over the dihedral automorphisms of \(C_n^2\). The average is feasible and its SLEM is no greater. For \(n\ge6\), its three coefficient classes are a holding probability \(p_0\), probability \(p_1\) for each one-step neighbor, and probability \(p_2\) for each two-step neighbor, with \(p_0+2p_1+2p_2=1\). Therefore, finding the global optimum value reduces to these three coefficients. This averaging argument alone does not assert every optimizer is invariant.

**2. Quadratic Fourier spectrum.** On Fourier mode \(k\), with \(x_k=\cos(2\pi k/n)\), the eigenvalue is

\[
 \lambda_k=p_0+2p_1x_k+2p_2(2x_k^2-1)
 =1-2p_1(1-x_k)-4p_2(1-x_k^2).
\]

Consequently, the nontrivial multipliers are evaluations of a degree-at-most-two real polynomial \(f(x)\) satisfying \(f(1)=1\) at the finite grid \(x_k\), \(1\le k\le h\). These grid values decrease strictly from \(u=x_1\) to \(\ell=x_h\). We may first solve the *relaxed* minimax problem over all real degree-two polynomials anchored at \(f(1)=1\), without any coefficient sign constraints.

**3. Identification of the middle extremum.** The product \((x-\ell)(u-x)\) is a concave quadratic in \(x\), whose maximum is reached at the grid point closest to \((u+\ell)/2\). That grid point is \(v=x_j\), with \(j=\lfloor(n+2)/4\rfloor\). For completeness, the assertion follows by the following four parity checks. If \(n\equiv0\pmod4\), \(v=0\), the midpoint is \(-\sin^2(\pi/n)\), and its distance to zero is no larger than its distance to \(-\sin(2\pi/n)\); the latter follows from \(\cos(\pi/n)\ge\sin(\pi/n)\). If \(n\equiv2\pmod4\), the two grid points straddling zero are \(\pm\sin(\pi/n)\), and the negative one is closer to the negative midpoint \(-\sin^2(\pi/n)\). If \(n\equiv1\pmod4\), with \(a=\pi/(2n)\), the candidates are \(\sin a\) and \(-\sin3a\), while the midpoint is \(-\sin a\sin3a\). For \(n\ge9\), \(\sin3a>2\sin a\) and \(\sin3a\le1/2\), so the positive candidate is nearer. If \(n\equiv3\pmod4\), the midpoint is again \(-\sin a\sin3a\), but the two candidates instead are \(\sin3a\) and \(-\sin a\); the negative candidate is nearer since \(\sin3a>\sin a\). All more distant grid points are monotone farther from the midpoint. The omitted \(n=5\) has only two distinct nontrivial cosine values.

**4. Three-point equioscillation and the exact minimum.** Set

\[
 f_*(x)=t+\frac2T(x-\ell)(x-u),
 \qquad t=\frac\Delta T.
\]

Then \(f_*(\ell)=f_*(u)=t\), \(f_*(v)=-t\), and \(f_*(1)=t+2(1-\ell)(1-u)/T=1\). Because \((x_k-\ell)(u-x_k)\) ranges from zero to at most \(\Delta\), every sampled value lies between \(-t\) and \(t\). No other anchored degree-two polynomial can attain a smaller maximum absolute sampled value: if \(g\) did, the difference \(g-f_*\) would have strict signs negative, positive, negative at the ordered points \(\ell<v<u\), hence two distinct roots between them, and also the root \(x=1\), impossible for a polynomial of degree at most two. For equal maximal error, the corresponding weak signs and the factorization \(g(x)-f_*(x)=(x-1)(\alpha x+\beta)\) show uniqueness: the affine function is nonnegative at \(\ell,u\), nonpositive at their interior point \(v\), and so must vanish identically. Thus \(f_*\) uniquely solves even the relaxed problem.

**5. Nonnegative transition probabilities.** Equating coefficients of \(x^2\) and \(x\) in \(f_*\) gives \(p_2=1/(2T)\) and \(p_1=-(u+\ell)/T\); normalization gives \(p_0=(\Delta+1+2u\ell)/T\). Here \(T>0\). The inequality \(u+\ell<0\) holds for even \(n\), because \(\ell=-1\), and for odd \(n\), because \(u=\cos(2\pi/n)<\cos(\pi/n)=-\ell\). Hence \(p_1,p_2>0\).

To establish the remaining strict inequality, put \(E=\Delta+1+2u\ell\). If \(n\equiv0\pmod4\), direct substitution yields \(E=1-u>0\). If \(n\equiv2\pmod4\), putting \(s=\sin(\pi/n)\) gives \(E=s^2(1+2s)>0\). For odd \(n\ge7\), put \(s=\sin(\pi/(2n))\). The cosine identities \(-\ell=1-2s^2\) and \(u=2(1-2s^2)^2-1\) give

\[
 E=s^2(4s^2-3)
 \begin{cases}
 4s^2+2s-3,&n\equiv1\pmod4,\\
 4s^2-2s-3,&n\equiv3\pmod4.
 \end{cases}
\]

Since \(0<s<1/4\), all displayed factors other than \(s^2\) are negative, so \(E>0\). Therefore the relaxed optimum is genuinely stochastic. Its global optimality and uniqueness within the invariant family follow from the previous steps.

**6. Asymptotics.** The endpoints obey \(u=1-2\pi^2/n^2+O(n^{-4})\) and \(\ell=-1+O(n^{-2})\), with \(\ell=-1\) identically in even dimensions and \(\ell=-1+\pi^2/(2n^2)+O(n^{-4})\) in odd dimensions. The selected middle frequency has \(v=O(n^{-1})\), hence \(\Delta=1+O(n^{-2})\) and \(2(1-\ell)(1-u)=8\pi^2/n^2+O(n^{-4})\). Substitution into \(\mu_*=\Delta/T\) proves the asserted gap expansion and the two parity limits for \(n^2p_1\). The one-hop comparison is the standard cycle formula from the cited spectral symmetry analysis.

## Verification

The standalone standard-library script `verify.py` checks the exact rational \(n=5,6\) boundary cases, evaluates the complete discrete Fourier spectrum and active modes through \(n=1000\), checks all probability constraints and the nearest-grid-frequency rule, and performs separately formulated three-variable linear-programming comparisons through \(n=80\) when SciPy is available. The script also checks large-dimension asymptotics numerically. It prints `VERIFICATION_OK` with its assertion count. Finite computation is corroborative only; the preceding all-dimensional proof is the correctness basis.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced the symmetric fastest-mixing problem and its semidefinite formulation. Boyd, Ghosh, Prabhakar and Shah (2005), Section 3.1, study precisely the \(k\)-nearest-neighbor ring family, whose \(k=2\) case has the present support, and derive a lower bound \(\cos(4\pi/n)\) plus a nearly optimal construction in the regime of fixed \(k\) and large \(n\). Their stated results in Section 3.1 do not identify the exact finite-\(n\) optimum, all three probability weights, or the parity-dependent one-step asymptotics. Boyd, Diaconis, Parrilo and Xiao (2009) prove the symmetry reduction and give an exact *one-hop* cycle example, but not the two-hop graph. The present result sharpens the earlier \(k=2\) asymptotic bounds to a global finite-dimensional equality and explicit unique invariant weights, not a general solution for larger \(k\).

## Limitations

The result only minimizes asymptotic SLEM for symmetric uniform-stationary, discrete-time chains on \(C_n^2\). It neither optimizes total-variation distance at a prescribed finite time nor proves uniqueness among all noninvariant matrices. A complete search of every historical circulant-optimization source is not claimed; an unindexed exact formula equivalent to this result could exist. The standalone checks use floating-point trigonometry away from the exact small boundary cases and therefore are not formal numerical certificates for arbitrary \(n\).

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689; publicly dated 2004-10-29. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Mixing Times for Random Walks on Geometric Random Graphs*, Proceedings of ANALCO (2005), 240–249, especially Section 3.1 and its appendix. https://web.stanford.edu/~boyd/papers/pdf/gnr_mix.pdf
3. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (initial public version 2007-09-06), SIAM Journal on Optimization 20 (2009), 792–819. https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf
