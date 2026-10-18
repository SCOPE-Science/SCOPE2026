# Uniform asymptotic two-cycle amplitude after rare long transients in a tent map with memory

## Finding

Let \(\tau(u)=2\min\{u,1-u\}\) for \(0\le u\le1\), and consider
\[
G(x,y)=\bigl(y,\tau((x+3y)/4)\bigr),\qquad (x,y)\in[0,1]^2.
\]
Write \(L=\{x+3y<2\}\), \(U=\{x+3y\ge2\}\), and let \(T=\min\{n\ge0:G^n(X_0,Y_0)\in U\}\). Define \(N_n=\{T=n,\ G^{n+j}(X_0,Y_0)\in U\text{ for every }j\ge0\}\). This event records direct, uninterrupted capture into the upper-branch period-two family after a first visit.

Put
\[
B=\begin{pmatrix}0&1\\1/2&3/2\end{pmatrix},\quad
\rho=\frac{3+\sqrt{17}}4,\quad
\sigma=\frac{3-\sqrt{17}}4,\quad
k=\frac{1+3\rho}{1+2\rho^2}.
\]
For every \(n\ge3\), the exact Lebesgue area of the event \(T\ge n\) is
\[
\operatorname{area}\{T\ge n\}=\frac{2}{a_{n-1}b_{n-1}},\qquad
(a_j,b_j)=(1,3)B^j.
\]
In particular, the survival area is asymptotic to \((\rho/k^2)\rho^{-2n}\).

Let
\[
c_0=\frac2{1+3\rho},\quad c_1=\rho c_0,\quad
c_-=\frac5{3(1+2\rho)},\quad c_+=\frac7{3(1+2\rho)}.
\]
For an initial law with a probability density continuous and strictly positive at \((0,0)\), conditioning on \(T=n\) gives
\[
(X_T,Y_T)\ \Longrightarrow\ (C,\rho C),\qquad
f_C(c)=\frac{2c}{c_1^2-c_0^2}\mathbf 1_{[c_0,c_1]}(c).
\]
The conditional probability of never returning to the lower branch has the exact limit
\[
\boxed{\Pr(N_n\mid T=n)\longrightarrow
p_*=\frac{c_+^2-c_-^2}{c_1^2-c_0^2}
=\frac{2(1+3\rho)^2}{3(\rho^2-1)(1+2\rho)^2}
=0.593592135468138\ldots .}
\]
For a trajectory in \(N_n\), put \(R_n=\lim_{j\to\infty}|X_{n+j}-Y_{n+j}|/2\), its unordered period-two amplitude. Then the distinctive selection law is
\[
\boxed{\mathcal L(R_n\mid N_n)\Longrightarrow
\operatorname{Uniform}[0,1/3],\qquad n\to\infty.}
\]
In fact the signed phase \(S_n=X_T+2Y_T-2\), given \(N_n\), converges to the density \(f_S(s)=3(2+s)/4\) on \([-1/3,1/3]\). The signed phase has a linear tilt, but its absolute value is exactly uniform in the limit. The conditional limits are universal over the stated initial-density class.

## Assumptions and scope

All trajectories remain in the unit square. We assign the switching line to \(U\); changing boundary assignments does not affect probabilities under an absolutely continuous initial law. The initial probability density must be continuous at \((0,0)\) with a positive value there (it need not be constant elsewhere). The parameter is exactly the critical memory weight \(\alpha=3/4\). Events \(N_n\) include trajectories staying in \(U\) from their first entrance onward; those that exit \(U\) and later return are excluded. The pointwise global attraction to the period-two line, the linear upper-branch eigenvalues, and the invariant trapping strip were established in the motivating work and are not the new claims.

## Proof

**1. Lower-branch survival geometry.** On \(L\), \(G(z)=Bz\). With \(\ell=(1,3)\), \(\ell(Bz)-\ell(z)=x/2+5y/2\ge0\) for \(x,y\ge0\). Therefore survival for at least \(n\) visits means precisely \(\ell B^{n-1}z<2\). For \(n\ge3\) the intercepts of this half-plane with the positive coordinate axes are already inside the unit square; the survivor is the full triangle with legs \(2/a_{n-1}\) and \(2/b_{n-1}\). This proves its exact area. The Perron eigenvalue of \(B\) is \(\rho>1\) and the other eigenvalue has absolute value smaller than one. With \(v=(1,\rho)^T\) and \(u=(1,2\rho)^T\),
\[
\rho^{-m}B^m\longrightarrow\frac{vu^T}{1+2\rho^2},\qquad
\rho^{-m}\ell B^m\longrightarrow ku^T,
\]
which gives the stated survival asymptotic.

**2. First-entrance phase.** An initial point has \(T=n\) exactly when \(\ell B^{n-1}z<2\le\ell B^nz\). Its coordinates are bounded by a fixed multiple of \(\rho^{-n}\), so put \(w=\rho^nz\). The admissible domains in the positive quadrant converge, up to boundary sets of zero area, to the bounded strip
\[
\frac2k\le w_1+2\rho w_2<\frac{2\rho}k.
\]
Since the starting density is continuous and positive at the origin, the rescaled conditional density converges in total variation on the rescaled initial-coordinate plane to normalized uniform area on this strip. Its slice area at \(u^Tw=s\) is proportional to \(s\), because \(w_1,w_2\ge0\) and \(u\) has positive entries. Also
\[
B^nz\longrightarrow \frac{u^Tw}{1+2\rho^2}(1,\rho)
\]
in the corresponding conditional distribution. The scalar coefficient consequently has density proportional to \(c\) between \(c_0=2/(1+3\rho)\) and \(c_1=\rho c_0\), with normalizing factor \(2/(c_1^2-c_0^2)\). This proves the entrance-point limit.

**3. Exactly which first entries never recross.** In \(U\), the map is the affine branch \(G(x,y)=(y,2-(x+3y)/2)\). Set \(H=x+y-4/3\) and \(s=x+2y-2\). One upper-branch step satisfies exactly \(H'=-H/2\) and \(s'=-s\). Its maximal forward-invariant subset of \(U\) is
\[
Q=\{(x,y)\in U:|x+2y-2|\le1/3\}.
\]
Indeed, if \(|s|\le1/3\), then \(3x+7y=3(x+2y)+y\le8\), so the next state satisfies \(x'+3y'=6-(3x+7y)/2\ge2\). Iteration preserves \(|s|\). Conversely, if every future state stays in \(U\), then \(H\to0\) and \(s\) alternates; its limiting two-cycle \((2/3-s,2/3+s)\) and its swap must be contained in the square, forcing \(|s|\le1/3\). Thus \(N_n\) is exactly the condition \(T=n\) and \(G^n z\in Q\). This also proves that \(R_n=|s(G^nz)|\) on \(N_n\), since \(x-y=3H-2s\).

**4. Rare-transient capture and uniform amplitude.** On the limiting first-entrance ray, \(s(C,\rho C)=(1+2\rho)C-2\). The exact direct-capture criterion is \(C\in[c_-,c_+]\); both endpoints lie strictly between \(c_0\) and \(c_1\). Conditional convergence and the zero measure of these boundary points give
\[
\Pr(N_n\mid T=n)\to \frac{c_+^2-c_-^2}{c_1^2-c_0^2}=p_*.
\]
Conditioning further on \(N_n\) makes \(C\) have density \(2c/(c_+^2-c_-^2)\) on \([c_-,c_+]\). Substitute \(s=(1+2\rho)c-2\); the resulting phase density is \(f_S(s)=3(2+s)/4\) on \([-1/3,1/3]\). Therefore for every \(0<r<1/3\), the density of \(R=|S|\) is \(f_S(r)+f_S(-r)=3\), giving the uniform amplitude. All reductions use only the continuity and strict positivity of the initial density at the origin, so the limit is independent of that density.

## Verification

The included standalone `verify.py` uses rational polygon clipping to independently reconstruct survivor and first-entrance areas for \(3\le n\le18\), and to compute the exact area of first-entrance polygons already inside the no-recross strip. It checks convergence of their conditional ratios toward \(p_*\), verifies the signed-phase density symmetrizes to constant amplitude density \(3\), and checks an exact affine upper-branch identity. Running `python verify.py` prints `VERIFY_OK`. Finite tests are consistency checks, not substitutes for the argument for arbitrary \(n\) or arbitrary densities.

## Relationship to prior work

Góra, Boyarsky, Li and Proppe, *Statistical and Deterministic Dynamics of Maps with Memory*, arXiv:1604.06991v1 (2016), Section 7.2, introduce and analyze exactly this map at \(\alpha=3/4\). In particular, their Theorem 5, invariant trapping region \(B_1\), and stable/neutral eigenvector analysis prove the qualitative eventual attraction to the period-two line. Those facts are credited. The result here is the distributional refinement for a specifically defined **long first-lower-branch transient followed by uninterrupted upper-branch capture**: the limiting direct-capture fraction, the biased signed entrance phase, and the uniform unordered limit-cycle amplitude. It is not a claim that the invariant strip or two-cycle line was first discovered here.

## Limitations

This theorem gives conditional, not unconditional, final-cycle statistics. It does not characterize the statistical phase distribution of trajectories which recross the switching line after their first entry, and it does not generalize to other memory weights. It establishes weak convergence and the exact limiting capture fraction, not a sharp error rate. The source's qualitative trapping geometry is essential prior work. The originality assessment relies on identified accessible results and searches; unindexed earlier derivations remain a possible historical-priority risk. Independent audit has not been performed.

## References

1. P. Góra, A. Boyarsky, Z. Li, H. Proppe, *Statistical and Deterministic Dynamics of Maps with Memory*, arXiv:1604.06991v1, first submitted 24 April 2016, especially Section 7.2 and Theorem 5. https://arxiv.org/html/1604.06991v1
