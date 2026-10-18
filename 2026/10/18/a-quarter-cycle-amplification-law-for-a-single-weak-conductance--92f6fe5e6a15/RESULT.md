# A quarter-cycle amplification law for a single weak conductance edge

## Finding

Let \(n\ge3\). Give the cycle with vertices \(0,1,\ldots,n-1\) unit conductances on all edges except \(\{n-1,0\}\), whose conductance is \(w>0\). Write \(L_{n,w}\) for its **unnormalized** symmetric combinatorial Laplacian. For real zero-sum forcing define the sharp mean-zero Poisson stability norm
\[
\mathcal P_n(w)=\sup_{\substack{f\in\mathbb R^n,\;\sum_j f_j=0\\\|f\|_\infty\le1}}\|L_{n,w}^{\dagger}f\|_\infty.
\]
For every fixed \(w>0\),
\[
\boxed{\lim_{n\to\infty}\frac{\mathcal P_n(w)-\mathcal P_n(1)}n
=\frac1{16}\max\!\left\{\frac{1-w}{w},0\right\}.}
\]
More precisely, for each fixed \(w>0\),
\[
\mathcal P_n(w)=\mathcal P_n(1)+\frac n{16}\left(\frac{1-w}{w}\right)_++O_w(1),
\]
where \((t)_+=\max\{t,0\}\). For \(0<w<1\), the maximizing output vertices necessarily approach the positions one-quarter and three-quarters of the way along the unit-conductance path: every choice of maximizing vertices \(i_n\) satisfies
\[
\operatorname{dist}\!\left(\frac{i_n}{n},\left\{\frac14,\frac34\right\}\right)\longrightarrow0.
\]
For fixed \(w>1\), any maximizing sequence has limiting accumulation points only in \(\{0,\frac12,1\}\); endpoint coordinates \(0\) and \(1\) describe the two sides of the distinguished edge. At \(w=1\), all output vertices tie by cyclic symmetry.

The homogeneous finite norm is **exactly**
\[
\mathcal P_n(1)=\frac{n^2}{32}+
\begin{cases}
0,&n\equiv0\pmod4,\\
\dfrac{n-2}{32n},&n\equiv1\pmod4,\\
\dfrac18,&n\equiv2\pmod4,\\
\dfrac{n+2}{32n},&n\equiv3\pmod4.
\end{cases}
\]
Thus the one-edge weakening changes the sharp norm at order \(n\), despite the homogeneous norm having order \(n^2\). Strengthening the distinguished edge does not increase the norm at order \(n\).

## Assumptions and scope

All finite graph edges are undirected and all conductances strictly positive. The Laplacian is \(L_{n,w}f(i)=\sum_{j\sim i}c_{ij}(f(i)-f(j))\), without division by vertex degree. The pseudoinverse acts as the inverse on \(\{f:\sum_j f_j=0\}\), and its output is normalized by \(\sum_j(L_{n,w}^{\dagger}f)(j)=0\). The domain and codomain use unweighted vertex \(\ell^\infty\) norms. The fixed-conductance asymptotics do not assert uniformity in sequences \(w=w_n\) approaching zero.

## Proof

**1. Rank-one Green kernel.** For the unit cycle put \(G_n=L_{n,1}^{\dagger}\). Direct verification of \(L_{n,1}G_n=I-\mathbf1\mathbf1^{\mathsf T}/n\) and \(G_n\mathbf1=0\) yields, for \(d_{ij}\equiv i-j\pmod n\), \(0\le d_{ij}<n\),
\[
(G_n)_{ij}=\frac{n^2-1}{12n}-\frac{d_{ij}(n-d_{ij})}{2n}.
\]
Let \(b=e_0-e_{n-1}\) and \(v=G_nb\). Then
\[
v_j=\frac{n-1-2j}{2n},\qquad b^{\mathsf T}G_nb=\frac{n-1}{n}.
\]
Since \(L_{n,w}=L_{n,1}+(w-1)bb^{\mathsf T}\), Sherman--Morrison inversion on the zero-sum subspace gives the **exact identity**
\[
L_{n,w}^{\dagger}=G_n+\delta_n(w)vv^{\mathsf T},\qquad
\delta_n(w)=\frac{n(1-w)}{1+(n-1)w}.
\]
The denominator is positive for every admissible \(n,w\), so no singular case has been omitted.

**2. Exact zero-mean endpoint duality.** For every real row \(a=(a_j)_{j=0}^{n-1}\), elementary finite-dimensional duality gives
\[
\sup_{\substack{\sum_jf_j=0\\|f_j|\le1}}\Big|\sum_ja_jf_j\Big|
=\min_{c\in\mathbb R}\sum_j|a_j-c|.
\]
Indeed, subtracting any constant \(c\) proves the upper bound. Equality follows by taking \(+1\) on the largest \(\lfloor n/2\rfloor\) entries and \(-1\) on the smallest \(\lfloor n/2\rfloor\) entries (with a zero at one median entry when \(n\) is odd). In particular, a median of the entries attains the minimum. Therefore
\[
\mathcal P_n(w)=\max_{0\le i<n}\min_{c\in\mathbb R}\sum_{j=0}^{n-1}
\left|\frac{n^2-1}{12n}-\frac{d_{ij}(n-d_{ij})}{2n}
+\delta_n(w)v_iv_j-c\right|.
\]
This also supplies an exact, finite algorithm and sharp forcing vectors at every \(n,w\).

**3. The homogeneous baseline.** When \(w=1\), the row entries decrease strictly as circular distance from the output vertex increases up to distance \(n/2\). Their median is at circular distance \(n/4+O(1)\). Summing the two quadratic branches above and distinguishing the four possible residues of \(n\) modulo \(4\) gives exactly the four-case formula stated in the finding. Equivalently, write
\[
(G_n)_{ij}=n\,g(d_{ij}/n)-\frac1{12n},\quad
 g(s)=\frac1{12}-\frac{s(1-s)}2,
\]
where the constant term disappears under median subtraction. The continuum median is \(g(1/4)=-1/96\), and
\[
\int_0^1|g(s)-g(1/4)|\,ds=\frac1{32}.
\]
For a wholly finite verification, put \(t=\lfloor(n+1)/4\rfloor\) and \(q(j)=j(n-j)\). The value \(G_n(i,i+t)\) is a row median. The entries of the form \(q(j)<q(t)\) occur precisely at \(j=0,1,\ldots,t-1\) and \(j=n-t+1,\ldots,n-1\); the two entries with \(q(j)=q(t)\) contribute zero. Thus
\[
\mathcal P_n(1)=\frac1{2n}\left[\frac{n(n^2-1)}6-4\sum_{j=1}^{t-1}j(n-j)+(4t-n-2)t(n-t)\right].
\]
Substituting \(t\) in the four residue classes and using the elementary sums of consecutive integers and their squares proves the stated exact formula. The continuum integral identifies the leading coefficient; the finite sum identifies the constant correction.

**4. Uniform row perturbation.** Fix \(w>0\). Then \(\delta_n(w)\) stays bounded as \(n\to\infty\), and \(|v_j|\le1/2\). Let \(c_{n,i}\) be any median of the homogeneous row. Adding \(\delta_n(w)v_iv_j\) changes each entry, and hence any chosen compatible median, by at most a constant depending only on \(w\). Around the two median crossings at circular distance \(n/4+O(1)\), consecutive homogeneous row entries differ in absolute value by a quantity bounded below by a positive constant, once \(n\) is large enough. Consequently only \(O_w(1)\) entries lie in a fixed-width neighborhood of the median. Outside that neighborhood the sign of the centered row cannot change, even after both the entry perturbation and the median shift.

Choose signs \(s_{n,i}(j)\in\{-1,0,1\}\) according to the homogeneous row relative to its median, assigning zero at ties. There are only \(O(1)\) ties and \(\sum_js_{n,i}(j)=O(1)\). Comparing the absolute-deviation sums at their respective medians, with the changed signs confined to \(O_w(1)\) indices, proves **uniformly in the output vertex** that
\[
\min_c\sum_j|(G_n)_{ij}+\delta_n(w)v_iv_j-c|
=\mathcal P_n(1)+\delta_n(w)v_i\sum_js_{n,i}(j)v_j+O_w(1).
\]
This estimate is two-sided: median stability controls the minimizing centering constant, not just the expression evaluated at the old median.

**5. A piecewise-quadratic spatial profile.** Put \(x=i/n\), let \(v_*(x)=1/2-x\), and extend it periodically from \([0,1)\) with its jump at integers. The signs in Step 4 are positive for circular distances less than \(n/4+O(1)\) and negative beyond, so uniform Riemann-sum comparison gives
\[
\sum_js_{n,i}(j)v_j=nH(x)+O(1),\quad
H(x)=2\int_{x-1/4}^{x+1/4}v_*(y\bmod1)\,dy.
\]
A direct integration yields
\[
H(x)=\begin{cases}
x,&0\le x\le1/4,\\
1/2-x,&1/4\le x\le3/4,\\
x-1,&3/4\le x\le1.
\end{cases}
\]
As \(v_i=v_*(i/n)+O(1/n)\), the preceding formula becomes
\[
\mathcal P_{n,i}(w)=\mathcal P_n(1)+n\delta_n(w)K(i/n)+O_w(1),\quad
K(x)=(1/2-x)H(x),
\]
where \(\mathcal P_{n,i}(w)\) denotes the sharp norm at output vertex \(i\). The continuous function \(K\) is nonnegative, has maximum \(1/16\) exactly at \(x=1/4,3/4\), and has zero set \(\{0,1/2,1\}\). Because \(\delta_n(w)\to(1-w)/w\), maximizing over the mesh gives the asserted sharp correction and the localization of maximizing vertices. The gap between extrema of \(K\) and any closed set away from them yields the localization statements without claiming uniqueness for finite \(n\). This completes the proof.

## Verification

The attached standalone `CHECK.py` uses rational Gauss--Jordan inversion of \(L_{n,w}+\mathbf1\mathbf1^{\mathsf T}/n\) independently of the rank-one formula, compares every entry for many small cycles and rational conductances, verifies the median duality with explicit balanced sign vectors, checks the exact four-residue homogeneous baseline, and compares large finite cases to the limiting correction and output locations. Run `python CHECK.py` using Python's standard library. Finite computations test the formulas but do not substitute for the proof of the limit or for a literature-priority determination.

## Relationship to prior work

Beveridge's *A Hitting Time Formula for the Discrete Green's Function* (arXiv:1505.06989v1, 26 May 2015) supplies a Green-function framework and a formula for the unweighted cycle. Its convention is the random-walk Laplacian \(I-P=L/2\) on that cycle, so its Green function is **twice** the pseudoinverse used here. The homogeneous Green kernel is classical and is not claimed as original.

Carmona, Encinas, and Mitjana's *Effective resistances for ladder-like chains* (first publicly available on 24 July 2014) provides older Green and resistance formulas for cycle-containing graph families. Its accessible abstract does not settle the present median-centered endpoint optimization, and the uninspected full text remains a priority risk. Pozrikidis's 2015 generalized Sherman--Morrison method studies Green-function updates under modifications of graph edges; the rank-one update is acknowledged as standard machinery, not a new abstract identity. Full text was not accessible in this review. Grudsky, Maximenko, and Soto-González (arXiv:2205.12457v1, 25 May 2022) study **exactly the same one-edge-weighted cycle matrices**, but their inspected theorems concern eigenvalues, eigenvectors and eigenvalue asymptotics. These results do not directly state the present sharp mean-zero \(\ell^\infty\) Poisson norm, its first-order conductance asymmetry, or quarter-cycle localization. The contribution here is the endpoint norm asymptotic and its extremal geometry, not the underlying Green or spectral machinery.

## Limitations

Only real forcing and unweighted vertex \(\ell^\infty\) norms are covered. The \(O_w(1)\) remainder and location claims require a fixed positive conductance and are not uniform as \(w\downarrow0\). The exact finite formula is a median optimization, not a claimed simplified closed expression for every \(n,w\). For \(w>1\) the theorem identifies possible **limiting** maximizer locations, not all finite maximizers. Priority remains provisional, especially regarding earlier formulations through generalized Green updates, operator quotient norms, and bottleneck network response.

## References

1. A. Carmona, A. M. Encinas, and M. Mitjana, *Effective resistances for ladder-like chains*, International Journal of Quantum Chemistry 114 (2014), 1670–1677, first published 24 July 2014, https://doi.org/10.1002/qua.24740.
2. A. Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989v1 (26 May 2015), https://arxiv.org/abs/1505.06989.
3. C. Pozrikidis, *Application of a generalized Sherman--Morrison formula to the computation of network Green's functions and the construction of spanning trees*, J. Stat. Mech. (2015), P05007, https://doi.org/10.1088/1742-5468/2015/05/P05007.
4. S. M. Grudsky, E. A. Maximenko, and A. Soto-González, *Eigenvalues of the laplacian matrices of the cycles with one weighted edge*, arXiv:2205.12457v1 (25 May 2022), https://arxiv.org/abs/2205.12457.
