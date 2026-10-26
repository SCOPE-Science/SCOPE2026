# Sharp eventual positivity horizon for biharmonic heat on Boolean hypercubes

## Finding

For each integer \(d\ge3\), the entrywise positivity-restoration time of the biharmonic heat operator \(S_d(t)=\exp(-tL_d^2)\) on the unweighted Boolean hypercube \(Q_d\) is exactly
\[
\tau_d=-\frac14\log z_d,
\qquad
F_d(z_d)=0,
\qquad
F_d(z)=\sum_{k=0}^d(-1)^k\binom{d}{k}z^{k^2},
\qquad
\frac1d<z_d<\frac1d+\frac1{d^3}.
\]
Here \(z_d\) is the **unique** root in the indicated interval, not necessarily the only root on \((0,1)\). At \(t=\tau_d\), precisely the entries between antipodal vertices vanish, while every other entry is strictly positive. All entries are strictly positive at every later time. Some antipodal entry is negative at times immediately preceding \(\tau_d\), so this is the exact persistent nonnegativity horizon. It has the sharp expansion
\[
\tau_d=\frac14\log d-\frac1{8d^2}+\frac1{8d^3}+O(d^{-4}).
\]

## Assumptions and scope

Vertices of \(Q_d\) are binary words of length \(d\), joined if their Hamming distance is one. The unnormalized combinatorial Laplacian is \(L_d=dI-A_d\), where \(A_d\) is adjacency. We work with counting coordinates on the real Banach lattice \(\mathbb R^{2^d}\), and a matrix is positive if all its entries are nonnegative. The persistent positivity horizon is the infimum of \(t\ge0\) such that \(S_d(u)\) is entrywise nonnegative for every \(u\ge t\). The result is asserted for every integer \(d\ge3\), without boundary conditions beyond the finite graph.

## Proof

**1. Walsh diagonalization and Hamming shells.** For any subset \(B\) of the coordinate set, the character \(\chi_B(x)=(-1)^{\sum_{j\in B}x_j}\) is an eigenvector of \(L_d\) with eigenvalue \(2|B|\). Thus the eigenvalue of \(L_d^2\) at Walsh weight \(k\) is \(4k^2\). For vertices \(x,y\) of Hamming distance \(r\), Fourier inversion gives
\[
2^dS_d(t)_{xy}=H_{d,r}(z):=\sum_{k=0}^d K_k(r)z^{k^2},
\qquad z=e^{-4t},\qquad
K_k(r)=[v^k](1+v)^{d-r}(1-v)^r.
\]
In particular \(K_0(r)=1\), \(K_1(r)=d-2r\), and \(|K_k(r)|\le\binom dk\). At antipodal distance \(r=d\), \(K_k(d)=(-1)^k\binom dk\), so \(H_{d,d}=F_d\).

**2. A uniform Fourier-tail estimate.** Put \(b_d=d^{-1}+d^{-3}\) and \(c=9/8\). For every \(d\ge3\), \(b_d\le c/d\). For every \(0\le z\le b_d\), let \(T_d(z)=\sum_{k=2}^d\binom dk z^{k^2}\). The term \(k=2\) is at most \(c^4/(2d^2)\). For \(k\ge3\), the elementary bounds \(k^2\ge3k\) and \(\binom dk\le d^k/k!\) give
\[
\sum_{k=3}^d\binom dk z^{k^2}
\le \sum_{k=3}^{\infty}\frac{q^k}{k!}
\le\frac{q^3e^q}{6},
\qquad q=\frac{c^3}{d^2}\le\frac{c^3}{9}.
\]
Consequently
\[
T_d(z)\le\frac{c^4}{2d^2}+\frac{c^9e^{c^3/9}}{6d^6}
<\frac{0.81}{d^2}.
\]
The final displayed strict bound is numerical shorthand for the elementary inequalities \(c^4/2<0.801\), \(c^9e^{c^3/9}/6<0.57\), and \(0.57/3^4<0.008\). It holds uniformly for every integer \(d\ge3\) and every \(z\) in the stated closed interval.

**3. The last antipodal zero.** At \(z=1/d\), the first two terms of \(F_d\) cancel, leaving a strictly positive alternating sum: the magnitudes \(a_k=\binom dk d^{-k^2}\) decrease strictly for \(k\ge2\), since \(a_{k+1}/a_k=(d-k)/(k+1)d^{-(2k+1)}<1\). On the other hand,
\[
F_d(b_d)=1-db_d+\sum_{k=2}^d(-1)^k\binom dk b_d^{k^2}
\le -\frac1{d^2}+T_d(b_d)<0.
\]
For \(0\le z\le b_d\), differentiate termwise. The \(k=2\) contribution to the absolute derivative remainder is at most \(2c^3/d\). The higher-degree part satisfies
\[
\sum_{k=3}^d k^2\binom dk z^{k^2-1}
\le\frac d c\sum_{k=3}^{\infty}\frac{k^2q^k}{k!}
\le\frac{3c^8e^{c^3/9}}{2d^5}
<\frac{4.51}{d^5},
\]
where \(k^2/k!\le(3/2)/(k-3)!\) for \(k\ge3\). Therefore
\[
F'_d(z)\le-d+\frac{2c^3}{d}+\frac{4.51}{d^5}<0
\quad(0\le z\le b_d,\ d\ge3).
\]
There exists exactly one zero \(z_d\in(1/d,b_d)\); moreover \(F_d(z)>0\) for \(0\le z<z_d\), and \(F_d(z)<0\) for \(z_d<z\le b_d\).

**4. No other distance controls restoration.** For each \(0\le r\le d-1\) and \(0\le z\le z_d<b_d\), the preceding estimates imply
\[
H_{d,r}(z)\ge1+(d-2r)z-T_d(z)
\ge1-(d-2)b_d-\frac{0.81}{d^2}
=\frac2d-\frac{d-2}{d^3}-\frac{0.81}{d^2}>0.
\]
Thus, at and after \(\tau_d=-\log(z_d)/4\), every nonantipodal kernel entry is strictly positive, and antipodal entries are nonnegative, strictly positive for \(t>\tau_d\). At any time \(t\) slightly less than \(\tau_d\), one has \(z_d<e^{-4t}\le b_d\), so the antipodal entries are negative. This proves exactness of the persistent horizon and the uniqueness of the zero entries at the cutoff.

**5. Sharp large-dimension expansion.** From the bracket, \(z_d=d^{-1}+O(d^{-3})\). At the root the terms of degree \(k\ge3\) total \(O(d^{-6})\) by step 2. Therefore
\[
dz_d-1=\binom d2 z_d^4+O(d^{-6})
=\frac1{2d^2}-\frac1{2d^3}+O(d^{-4}).
\]
Taking \(-\tfrac14\log z_d\) and expanding \(\log(1+u)\) at \(u=0\) yields the stated three-term asymptotic formula. All estimates are uniform over integers \(d\ge3\).

## Verification

The standalone `verify.py` implements the Krawtchouk coefficient formula, brackets the antipodal root, bisects it, and tests positive kernel entries for integer dimensions \(3\le d\le32\). For example it yields \(\tau_3\approx0.263910163763118\), \(\tau_4\approx0.340169530186166\), and \(\tau_{16}\approx0.692686456843626\). The infinite-dimensional-family conclusion rests on the proof inequalities above, not on this finite computation. Run `python3 verify.py` from the package directory; only the Python standard library is needed.

## Relationship to prior work

Daners, Glück, and Kennedy established qualitative criteria for eventual positivity of operator semigroups and discussed matrix exponentials and fourth-order generators. The present finite family satisfies the qualitative spectral hypotheses, but such criteria give neither the sharp cutoff nor its antipodal extremizer and dimension-dependent second-order correction. Existing related exact results for biharmonic evolution on rook, multipartite, and triangular graph families have different spectral data; the exact antipodal sign formula for the Boolean-cube **resolvent** does not yield this exponential-semigroup cutoff because a resolvent is a Laplace average of the heat semigroup. Krawtchouk spectral reduction is standard; the new claim is the universal dominance of the antipodal restoration threshold and its sharp asymptotic.

## Limitations

The theorem concerns the unnormalized, unweighted Boolean hypercube Laplacian and the square power only. It does not classify possible earlier isolated positivity intervals, weighted cubes, general Hamming graphs, or the transient peak of the endpoint operator norm. Literature searches cannot certify absolute novelty; an unindexed direct computation of the same cutoff remains a residual possibility. Only scientific self-review is reported; no independent validation is implied.

## References

1. D. Daners, J. Glück, and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294 (first publicly submitted 17 November 2015), §1 and §9. https://arxiv.org/abs/1511.05294
2. D. Daners, J. Glück, and J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020 (first publicly submitted 29 November 2015), §1 and §6. https://arxiv.org/abs/1511.09020
3. F. Gazzola and H.-C. Grunau, *Eventual local positivity for a biharmonic heat equation in \(\mathbb R^n\)*, Discrete Contin. Dyn. Syst. Ser. S **1** (2008), 83–87, doi:10.3934/dcdss.2008.1.83. This treats the continuum rather than a finite hypercube.
