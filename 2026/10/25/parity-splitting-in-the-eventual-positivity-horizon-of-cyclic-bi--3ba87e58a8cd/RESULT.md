# Parity splitting in the eventual positivity horizon of cyclic biharmonic heat

## Finding

For every integer \(n\ge3\), let \(C_n\) be the unit-weight cycle, let \(L_n=2I-A(C_n)\) be its unnormalized Laplacian, and put \(T_n(t)=\exp(-tL_n^2)\). Define the *eventual entrywise positivity horizon*
\[
\tau_n=\inf\{t\ge0:T_n(u)\text{ is entrywise nonnegative for every }u\ge t\}.
\]
This is a last-negative-time invariant, rather than the first time any particular entry becomes positive.

Set \(c=16\pi^4\) and, for \(s>0\),
\[
H_s(x)=1+2\sum_{k=1}^{\infty}e^{-cs k^4}\cos(2\pi kx),\qquad h(s)=H_s(1/2).
\]
There is a unique zero \(s_*\) of \(h\) in \((1/3000,1/1500)\). Define the absolutely convergent series
\[
\begin{aligned}
D&=-2c\sum_{k\ge1}(-1)^k k^4e^{-cs_*k^4},\\
B&=-8\pi^2\sum_{k\ge1}(-1)^k k^2e^{-cs_*k^4},\\
G&=\frac{4\pi^2}{3}cs_*\sum_{k\ge1}(-1)^k k^6e^{-cs_*k^4},
\end{aligned}
\]
where \(D>0\), \(B>0\), and \(G<0\). As \(n\to\infty\), along the indicated integer parities,
\[
\boxed{\displaystyle
\frac{\tau_n}{n^4}=
\begin{cases}
s_*-\dfrac{G}{D n^2}+O(n^{-4}),&n\text{ even},\\[5pt]
s_*-\dfrac{G+B/8}{D n^2}+O(n^{-4}),&n\text{ odd}.
\end{cases}}
\]
In particular the parity-correction gap is exactly \(B/(8D)>0\). The relevant numerics are
\[
\begin{aligned}
s_*&=0.0004447202008935986806\ldots,\\
-G/D&=0.00292185123498610269\ldots,\\
-(G+B/8)/D&=-0.00024559638089865358\ldots,\\
B/(8D)&=0.00316744761588475627\ldots.
\end{aligned}
\]
For all sufficiently large \(n\), and at every time \(t\ge n^4/3000\), the least matrix entry of \(T_n(t)\) occurs at a vertex at maximum cycle distance from its row vertex. On this time range the semigroup is entrywise nonnegative **if and only if** \(t\ge\tau_n\). At \(t=\tau_n\), precisely the antipodal entries (one per row when \(n\) is even, two when \(n\) is odd) vanish; all other entries are positive.

## Assumptions and scope

The graph is the *simple* cycle with unnormalized combinatorial Laplacian; there is no length or degree normalization in \(L_n\). The operator acts on real vertex functions, although the spectral formula holds complex-linearly. Each occurrence of \(O(n^{-4})\) means a constant independent of sufficiently large integers within the specified parity class. The theorem is asymptotic: it does not assert that the antipodal minimizing property holds for every small cycle or that the semigroup has no isolated earlier nonnegative intervals below \(n^4/3000\).

The continuum comparison is the unit-circumference periodic fourth-order heat kernel \(H_s\). The quantity \(n^{-4}\tau_n\) is the dimensionless physical time associated with a cycle whose nearest-neighbor spacing tends to zero.

## Proof

**1. Exact diagonalization.** The Fourier characters \(j\mapsto e^{2\pi i kj/n}\) diagonalize \(L_n\), with eigenvalues \(4\sin^2(\pi k/n)\). Put
\[
\rho_{k,n}=16n^4\sin^4(\pi k/n).
\]
For \(j\in\{0,\ldots,n-1\}\), the exact normalized kernel entry is
\[
F_n(s,j)=n\,(T_n(sn^4))_{0j}
=1+2\sum_{1\le k<n/2}e^{-s\rho_{k,n}}\cos(2\pi kj/n)
+\mathbf 1_{2\mid n}e^{-16sn^4}(-1)^j.
\]
Thus positivity of the matrix is equivalent to \(F_n(s,j)\ge0\) at all integer vertices \(j\). For nonintegral \(x\in[0,1]\), use this trigonometric polynomial as the definition of \(F_n(s,x)\), replacing \(j/n\) by \(x\) in the cosine, and the final \((-1)^j\) by \(\cos(\pi nx)\).

**2. A rigorously localized continuum crossing.** Fix \(\sigma=1/3000\). Since \(c\sigma>1/2\), for every \(s\ge\sigma\),
\[
\sum_{k\ge2}k^r\frac{e^{-csk^4}}{e^{-cs}}
\le\sum_{k\ge2}k^r e^{-(k^4-1)/2}
\quad(r=2,4,6).
\]
The right side is less than \(1/100\) for \(r=2\), less than \(1/10\) for \(r=4\), and less than \(1/10\) for \(r=6\); the \(k=2\) term and a geometrically dominated \(k\ge3\) tail prove these elementary bounds. The elementary inequality \(|\sin(kz)|\le k\sin z\) for \(z\in[0,\pi]\) shows
\[
\partial_x H_s(x)<0\qquad(0<x<1/2,\ s\ge\sigma),
\]
so the antipode is its unique minimum. The same first-mode domination, now with weights \(k^4\), gives \(h'(s)>0\). Direct exponential bounds using \(1/2<c\sigma<0.52\) show \(h(\sigma)<0\); bounds using \(1<c/1500<1.04\) give \(h(1/1500)>0\). Thus the root \(s_*\) exists and is unique on \([\sigma,\infty)\), and \(D=h'(s_*)>0\), \(B=\partial_x^2 H_{s_*}(1/2)>0\). The \(k^6\) domination also gives \(G<0\).

**3. The last sign change lies at the farthest graph vertex.** For \(1\le k\le n/2\), one has \(\rho_{k,n}\ge256k^4\) and \(\rho_{1,n}\le c\), so for \(s\ge\sigma\) the ratios \(e^{-s(\rho_{k,n}-\rho_{1,n})}\) admit a summable, \(n\)-independent upper bound after multiplication by any fixed power of \(k\). Their limits are \(e^{-cs(k^4-1)}\) for each fixed \(k\). By dominated convergence, for all sufficiently large \(n\), uniformly over \(s\ge\sigma\), the first Fourier mode dominates the sums of all remaining modes weighted by \(k^2\) and, independently, by \(\rho_{k,n}/\rho_{1,n}\). The ratios decrease as \(s\) grows. The even-\(n\) Nyquist term, with half the usual Fourier multiplicity, satisfies the same bounds.

Applying the sine inequality to \(\partial_x F_n\) proves strict decrease for \(0<x<1/2\). Consequently the minimum over vertices occurs at \(j_n=\lfloor n/2\rfloor\) and its reflection. At these vertices the first cosine is negative, whereas all other weighted cosine terms are dominated in absolute value. Hence \(s\mapsto F_n(s,j_n)\) is strictly increasing for \(s\ge\sigma\). By uniform Fourier convergence, it is negative at \(s=\sigma\), tends to \(1\), and has a unique zero \(s_n>\sigma\). Since it is negative immediately below that zero and all entries are nonnegative at every later time, the **definition** of the eventual horizon gives \(\tau_n=n^4s_n\), irrespective of any possible earlier sign changes.

**4. A uniform dispersive expansion.** Taylor's theorem gives for fixed \(k\)
\[
\rho_{k,n}=ck^4\left(1-\frac{2\pi^2k^2}{3n^2}+O(k^4n^{-4})\right).
\]
For \(s\) in any compact subinterval of \((0,\infty)\), splitting the Fourier sums at \(k=n^{1/3}\) and using \(\rho_{k,n}\ge256k^4\) on the remaining frequencies justifies termwise expansion, uniformly in \(x\):
\[
F_n(s,x)=H_s(x)+\frac{Q_s(x)}{n^2}+O(n^{-4}),\quad
Q_s(x)=\frac{4\pi^2}{3}cs\sum_{k\ge1}k^6e^{-csk^4}\cos(2\pi kx).
\]
The same control applies after a bounded number of derivatives in \(s\) and \(x\). At the farthest vertex, \(x=j_n/n=1/2\) for even \(n\) and \(x=1/2-1/(2n)\) for odd \(n\). Symmetry around the antipode gives
\[
F_n(s,j_n)=h(s)+\frac{1}{n^2}
\left(Q_s(1/2)+\mathbf 1_{2\nmid n}\frac{\partial_x^2H_s(1/2)}8\right)+O(n^{-4}).
\]
Finally, \(h(s_*)=0\) and \(h'(s_*)=D>0\). The implicit-root expansion yields
\[
s_n=s_*-\frac{G+\mathbf 1_{2\nmid n}B/8}{Dn^2}+O(n^{-4}),
\]
which proves both branches and the positive parity gap.

## Verification

A standalone standard-library Python program, `check_cycle_biheat.py`, reconstructs finite-cycle matrix exponentials independently by scaling-and-squaring, compares them with the discrete Fourier kernel, finds the last antipodal zeros by bisection, checks every entry at sampled post-threshold times, and tests the even/odd second-order expansions through \(n=321\). Its successful replay completed 1,425 assertions and produced the coefficients listed above. These are reproducibility checks, **not** a substitute for the infinite-series bounds, global minimization argument, or asymptotic proof.

To replay, run `python3 check_cycle_biheat.py` from the directory containing this file. No third-party packages, network access, or external data are required.

## Relationship to prior work

Daners, Glück, and Kennedy established qualitative theory of eventual positivity for operator semigroups, including finite-dimensional and higher-order elliptic examples. Their 2015 preprint does not state a sharp quantitative threshold for cycles, a fourth-power scaling law, or parity-split corrections. The spectral computation above addresses these absent quantitative statements, not their general qualitative theory. Earlier work of Ferrero, Gazzola, and Grunau concerns biharmonic parabolic equations and eventual local positivity on Euclidean domains; those assertions do not give a cycle-graph threshold. The positive-time regularized Crank–Nicolson lattice scheme studied in a more recent independent work has a different propagator. In all comparisons the relevant implication is the mathematical assertion, not only its title.

## Limitations

The antipodal reduction is proved only for sufficiently large cycle orders. The theorem does not give a closed formula for \(\tau_n\) for each small \(n\), nor a characterization of all positivity windows before the final crossing, and it does not extend to weighted cycles, paths, fractional spectral powers, or higher-dimensional tori. The numerical decimals are approximations to precisely defined convergent series. Bibliographic priority beyond inspected accessible sources remains subject to further independent review.

## References

1. D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, first public preprint 17 November 2015, arXiv:1511.05294v1, https://arxiv.org/abs/1511.05294. Accessible full text: https://ar5iv.labs.arxiv.org/html/1511.05294. See Sections 1, 6, and 9.
2. A. Ferrero, F. Gazzola, H.-C. Grunau, *Decay and local eventual positivity for biharmonic parabolic equations*, Discrete Contin. Dyn. Syst. 21 (2008), 1129–1157, DOI:10.3934/dcds.2008.21.1129 (abstract and published bibliographic record examined).
3. D. Daners, J. Glück, J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, first public preprint 29 November 2015, arXiv:1511.09020 (background on uniform eventual positivity).
