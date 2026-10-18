# Exact fastest mixing on helm graphs with at least five rim vertices

## Finding
Let \(H_n\) be the helm graph obtained from the wheel \(K_1\vee C_n\) by adding a separate pendant leaf at each rim vertex. For every integer \(n\ge5\), put
\[
 s_n=1-\cos(2\pi/n),\quad u_n=\sqrt{s_n},\quad A_n=\frac1n+s_n\left(1-\frac1n\right),\quad D_n=s_n+2u_n+2.
\]
The minimum second-largest eigenvalue modulus (SLEM) over *all* symmetric nonnegative stochastic kernels on this graph is exactly
\[
 \boxed{\mu_n^*=1-\frac{A_n}{D_n}.}
\]
One global minimizer assigns the three undirected edge-orbit probabilities
\[
 \boxed{a_n=\frac1n\quad\text{(spokes)},\quad c_n=\frac{A_n(1+u_n)}{u_nD_n}\quad\text{(pendants)},\quad b_n=\frac{1-1/n-c_n}{2}\quad\text{(rim edges)}.}
\]
All three are strictly positive. This is the unique *dihedrally invariant* optimal weight triple; no uniqueness is asserted among unrestricted kernels. The hub and rim have no holding probability, and the leaves have holding probability \(1-c_n>0\). As \(n\to\infty\),
\[
 \mu_n^*=1-\frac{1}{2n}-\frac{\pi^2-\pi/\sqrt 2}{n^2}+O(n^{-3}),\qquad c_n\longrightarrow\frac{1}{2\sqrt2\pi}.
\]

## Assumptions and scope
There is one hub \(h\), rim vertices \(r_j\) and leaves \(\ell_j\), indexed modulo \(n\). Edges are \(hr_j\), \(r_jr_{j+1}\) and \(r_j\ell_j\), all undirected. A feasible kernel \(P\) is a real symmetric, entrywise nonnegative, row-stochastic matrix with \(P_{vw}=0\) off the graph edges and diagonal. Define \(\operatorname{SLEM}(P)=\max\{|\lambda|:\lambda\in\operatorname{spec}(P),\lambda\ne1\}\); a disconnected kernel has SLEM one by counting the eigenvalue one on the orthogonal complement of constants. The theorem concerns every integer \(n\ge5\); the exceptional shorter rims are outside the claim.

## Proof
**1. Symmetry and Fourier blocks.** Averaging an arbitrary feasible \(P\) over the dihedral action on the rim preserves feasibility and cannot increase SLEM, since SLEM is the spectral norm of \(P-J\) for \(J=\mathbf1\mathbf1^T/(2n+1)\) and the norm is convex. An invariant kernel has spoke, rim and pendant weights \(a,b,c\ge0\), constrained by \(na\le1\), \(a+2b+c\le1\), \(c\le1\). For each nonconstant Fourier frequency \(j\), the symmetric two-dimensional block is
\[
 X_j=\begin{pmatrix}1-a-c-2(1-\cos(2\pi j/n))b&c\\c&1-c\end{pmatrix}.
\]
The constant-frequency sector on the normalized hub, rim and leaf averages is
\[
 T=\begin{pmatrix}1-na&\sqrt n a&0\\\sqrt n a&1-a-c&c\\0&c&1-c\end{pmatrix},
\]
which has eigenvalue one and two remaining eigenvalues.

**2. A universal lower bound.** Put \(s=s_n\), \(u=\sqrt s\), and \(\alpha=1/n\). For \(c>0\), the largest eigenvalue of \(X_1\) decreases strictly when either \(a\) or \(b\) increases with \(c\) fixed. Hence it is at least the largest eigenvalue at \(a=\alpha\), \(b=(1-\alpha-c)/2\), whenever these have nonnegative values. If \(c>1-\alpha\), feasibility gives \(a\le1-c<\alpha\) and \(b\le(1-a-c)/2\). For every feasible \((a,b,c)\), write \(q=a+2sb\). As \(0<s<1\), \(q\le a+s(1-a-c)\), which is increasing in \(a\), hence \(q\le\alpha+s(1-\alpha-c)=A-sc\). This bound is valid even for \(c>1-\alpha\), because the right side remains positive (indeed \(A-sc=\alpha+s(1-\alpha-c)\ge\alpha-s\alpha>0\)). The top eigenvalue of the Fourier block depends only on \(c,q\) and is strictly decreasing in \(q\) for \(c>0\). Thus it is always at least \(f(c)\) with the formal upper bound \(q=A-sc\); minimizing this function over all \(c\ge0\) gives the global lower bound, regardless of whether the saturating triple is feasible at that particular \(c\).

For the saturated choices let \(A=\alpha+s(1-\alpha)\), \(z=A-sc\). Then the top eigenvalue is
\[
 f(c)=1-c-\frac z2+\sqrt{c^2+\frac{z^2}{4}}.
\]
Its derivative has a unique zero on the positive axis, and it is the unique minimum:
\[
 c_* =\frac{A(1+u)}{u(s+2u+2)},\qquad f(c_*)=1-\frac A{s+2u+2}.
\]
Indeed, differentiating and squaring the stationary equation yields
\[
 s(s^2+4)c^2-2As^2c+A^2(s-1)=0.
\]
As \(0<s<1\), this quadratic has exactly one positive root, the displayed \(c_*\); direct substitution verifies the original (unsquared) equation. The derivative is negative at zero and positive at infinity.

**3. Feasibility of the minimizer.** We establish \(\alpha<c_*<1/2\), so \(b_*=(1-\alpha-c_*)/2>0\). For \(n\ge10\), \(8/n^2\le s\le20/n^2\), by \(\sin x\ge2x/\pi\) on \([0,\pi/2]\) and \(\sin x\le x\), together with \(\pi^2<10\). At \(c=\alpha\), the derivative satisfies \(f'(\alpha)\le-1+s/2+2/\sqrt5<0\), because \(z=A-s\alpha\ge\alpha\). The radical formula gives
\[
 c_*\le\frac{\alpha}{2\sqrt s}+\frac{\sqrt s}{2}+\frac{\alpha s}{4}+\frac{s^2}{4}
 \le \frac1{4\sqrt2}+\frac{\sqrt{20}}{20}+\frac1{200}+\frac1{100}<\frac12.
\]
For \(5\le n\le9\), exact rational interval calculations of the displayed stationary quadratic at \(\alpha\) and \(1/2\) give respectively negative and positive signs. They are reproduced by `check_helm.py`, using Machin's identity and alternating-series rational enclosures of the cosine; for \(n=6\), \(\cos(\pi/3)=1/2\) is exact. Hence the unique positive root belongs to \((\alpha,1/2)\) in every case.

**4. All remaining modes are dominated.** First the candidate top Fourier eigenvalue \(t=f(c_*)\) satisfies \(t\ge1-\alpha\). In fact, for every \(0\le c\le1-\alpha\), \(f(c)\ge1-\alpha\) is equivalent to
\[
 s(1-\alpha-c)(c-\alpha)\le\alpha c.
\]
This is automatic if \(c\le\alpha\). Otherwise the left side divided by \(c\) is at most \(s(1-2\sqrt{\alpha(1-\alpha)})\), and this is at most \(\alpha\). To see the last bound, use \(s\le20/n^2\) and \(20(n-2\sqrt{n-1})\le n^2\) for \(n\ge5\). Writing \(x=\sqrt{n-1}\ge2\), the difference is \(x^4-18x^2+40x-19\ge5\), since its derivative is \(4(x-2)(x^2+2x-5)\ge0\).

The largest eigenvalue of any nonzero-frequency block \(X_j\) is at most \(t\), since \(1-\cos(2\pi j/n)\ge s\). Its smallest eigenvalue is at least \(-(1-\alpha)\): adding \((1-\alpha)I\) produces a positive semidefinite diagonally dominant matrix because \(2(1-\cos(2\pi j/n))\le4\), \(b_*=(1-\alpha-c_*)/2\), and \(c_*\le1-\alpha\).

For the two nonconstant radial eigenvalues, consider the Laplacian \(I-T\) at \(a=\alpha\). Its two positive eigenvalues are roots of
\[
 R(x)=x^2-(1+\alpha+2c_*)x+c_*(2+\alpha).
\]
They both lie in \([\alpha,2-\alpha]\): the lower-end polynomial value is \(R(\alpha)=c_*(2-\alpha)-\alpha>0\), with the larger root greater than \(\alpha\); at the upper end \(R(2-\alpha)=2\alpha^2+3\alpha c_*-5\alpha-2c_*+2>0\) since \(\alpha\le1/5\) and \(c_*\le1/2\). The trace puts the smaller root below \(2-\alpha\). Thus both corresponding eigenvalues of \(T\) have absolute value at most \(1-\alpha\le t\). All eigenvalues off the stationary direction are therefore in \([-t,t]\), and the first Fourier block attains \(t\). This proves global optimality and the formula.

**5. Invariant uniqueness and asymptotics.** At \(c>0\) the first Fourier upper eigenvalue is strictly decreasing in \(a,b\); the one-variable minimum is strict, hence \((a_n,b_n,c_n)\) is the only invariant optimum. The global statement follows by the averaging argument in Step 1, without claiming unrestricted uniqueness. Finally \(s_n=2\pi^2/n^2+O(n^{-4})\); substitution into \(A_n/D_n\) gives the stated two-term asymptotic and the limit of \(c_n\).

## Verification
The standalone program `check_helm.py` provides exact rational interval certificates for \(5\le n\le9\) and direct full-matrix spectral sanity checks for \(5\le n\le110\). The proof above, not the finite tests, establishes all integer orders.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao introduce the symmetry reduction and give an explicit fastest-mixing solution on the *wheel* in section 5.4.3 of their 2009 article (arXiv preprint 2007). That graph has no pendant leaves, and its published spectrum consists of a radial two-dimensional block and scalar Fourier modes. The helm adds a second vertex orbit at every rim location, changing those scalar modes to genuine two-dimensional blocks. The formulas here are not consequences of the wheel formula by merely substituting a parameter. The convex averaging technique itself is established prior work, not a claimed novelty.

## Limitations
The result is restricted to symmetric stochastic kernels with uniform stationary distribution, the helm with one pendant at each rim position, and \(n\ge5\). It does not characterize all non-invariant minimizers, or weighted, nonreversible or nonuniform-stationary extensions. An equivalent result could exist in literature not indexed by the searches described in REVIEW.md.

## References
Boyd, S., Diaconis, P., Parrilo, P. A., and Xiao, L., *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819; arXiv:0709.0955, submitted 6 September 2007, section 5.4.3.
Boyd, S., Diaconis, P., and Xiao, L., *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689 (general formulation).
