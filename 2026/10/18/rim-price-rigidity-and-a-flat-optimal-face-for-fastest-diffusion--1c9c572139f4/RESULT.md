# Rim-price rigidity and a flat optimal face for fastest diffusion on wheels

## Finding

Fix an integer \(n\ge3\), a budget \(B>0\), and a relative rim-edge price \(t>0\). On the wheel \(W_{n+1}=K_1*C_n\), independently allocate nonnegative conductances \(x_j\) to the \(n\) spokes and \(y_j\) to the \(n\) rim edges, subject to
\[
\sum_{j=0}^{n-1}(x_j+t y_j)=B.
\]
Let \(L(x,y)\) be the combinatorial weighted Laplacian. The fastest continuous-time diffusion design maximizes its second-smallest eigenvalue \(\lambda_2(L)\).

Set
\[
c_n=4\sin^2(\pi/n).
\]
**The complete set of global optimizers, allowing every edge weight to vary independently, consists exclusively of rotation-invariant assignments** \(x_j=a\), \(y_j=b\), as follows.

* If \(0<t<c_n\), the optimizer is unique:
\[
 a=\frac{Bc_n}{n(c_n+nt)},\qquad b=\frac{B}{c_n+nt},\qquad
 \max\lambda_2(L)=\frac{(n+1)Bc_n}{n(c_n+nt)}.
\]
Every edge type receives positive conductance, and \(b/a=n/c_n\).
* If \(t>c_n\), the optimizer is unique:
\[
 a=\frac Bn,\qquad b=0,\qquad \max\lambda_2(L)=\frac Bn.
\]
Thus every rim edge is deleted.
* At the **exact critical price** \(t=c_n\), the optimal value is \(B/n\), but there is a **one-dimensional face of optimal networks**:
\[
 0\le b\le\frac{B}{(n+1)c_n},\qquad a=\frac Bn-c_n b.
\]
There are no asymmetric optimizers, including at this degenerate threshold.

The deletion threshold has the exact asymptotic scale \(c_n\sim 4\pi^2/n^2\) as \(n\to\infty\). For any fixed positive relative price, sufficiently large wheels therefore use only spokes; at the critical price an entire interval of geometrically distinct conductance allocations is optimal.

## Assumptions and scope

The wheel has one hub labeled \(\infty\), rim vertices indexed by \(j\in\mathbb Z/n\mathbb Z\), a spoke \(\{\infty,j\}\) with conductance \(x_j\ge0\), and a rim edge \(\{j,j+1\}\) with conductance \(y_j\ge0\). All prices are linear, with unit spoke price and strictly positive rim price \(t\). Conductance zero means that an edge can be omitted. The budget is fully expended, and the Laplacian is normalized by \(L=\sum_{\{u,v\}}w_{uv}(e_u-e_v)(e_u-e_v)^{\mathsf T}\). The result concerns the continuous-time decay exponent \(\lambda_2\), not the second-largest eigenvalue modulus of a discrete-time Markov chain, total effective resistance, or a fixed-degree constraint. No symmetry restriction is placed on the feasible allocations.

## Proof

Write \(X=\sum_jx_j\), \(Y=\sum_jy_j\); then \(X+tY=B\) and \(0\le Y\le B/t\). The Rayleigh–Ritz principle gives a bound from the hub-versus-rim vector \(w=(-n,1,\ldots,1)\), which is orthogonal to the constants:
\[
 \lambda_2(L)\le \frac{w^{\mathsf T}Lw}{w^{\mathsf T}w}
 =\frac{n+1}{n}X.
\tag{1}
\]
Consider also two orthogonal-to-constants vectors having hub coordinate zero and rim coordinates \(\cos(2\pi j/n)\) and \(\sin(2\pi j/n)\). Each has squared norm \(n/2\). Their **mean** Rayleigh quotient is
\[
 \frac{X+c_nY}{n}.
\]
Indeed, the squared cosine/sine coordinates sum to one at each spoke, while the sums of squared differences of adjacent cosine/sine coordinates equal \(4\sin^2(\pi/n)=c_n\). Since every nonconstant Rayleigh quotient is at least \(\lambda_2(L)\),
\[
 \lambda_2(L)\le\min\left\{
 \frac{B+(c_n-t)Y}{n},\quad
 \frac{(n+1)(B-tY)}{n}
 \right\}.
\tag{2}
\]
For \(t<c_n\), the first affine function increases in \(Y\), and the second decreases; the maximum of their minimum occurs uniquely at \(Y=nB/(c_n+nt)\). For \(t>c_n\), the first decreases and uniquely forces \(Y=0\). At \(t=c_n\), the first is identically \(B/n\) and the second is at least \(B/n\) precisely when \(0\le Y\le nB/((n+1)c_n)\). These yield the upper bounds and budget allocations stated above.

To prove attainability, take equal spoke weights \(a\) and equal rim weights \(b\). Fourier diagonalization around the rim shows that the full spectrum of \(L\), with multiplicities, is
\[
 0,\qquad (n+1)a,\qquad
 a+4b\sin^2(\pi k/n)\quad (k=1,\ldots,n-1).
\]
Thus
\[
 \lambda_2(L)=\min\{(n+1)a,\ a+c_n b\}.
\tag{3}
\]
For all parameter regimes, substituting the proposed \(a,b\) attains the corresponding upper bound in (2).

It remains to rule out **every asymmetric optimum**, which does not follow from symmetry-averaging alone. In every optimal regime, the first bound in (2) is an equality: the arithmetic mean of the two normalized first-Fourier Rayleigh quotients equals \(\lambda_2(L)\). Both quotients separately are at least \(\lambda_2(L)\), so both Fourier vectors are eigenvectors of \(L\) at that eigenvalue. Let \(\zeta=\exp(2\pi i/n)\), and combine them into the complex eigenvector with hub coordinate zero and rim coordinates \(\zeta^j\). The rim-coordinate eigenvalue equation, divided by \(\zeta^j\), gives, for every \(j\),
\[
 x_j+(1-\zeta)y_j+(1-\zeta^{-1})y_{j-1}=\lambda_2(L).
\tag{4}
\]
Its imaginary part is \(\sin(2\pi/n)(y_{j-1}-y_j)=0\). Because \(n\ge3\), the sine is nonzero, so all rim conductances are equal. Equation (4) then forces all spoke conductances to be equal. Consequently (3) and the budget classify **all**, rather than merely one symmetric representative of, the optimizers. Finally, \(\sin(\pi/n)\sim\pi/n\) proves the stated asymptotic threshold.

## Verification

The accompanying `verify_wheel_gap.py` reconstructs weighted Laplacians from edge contributions. With Python 3, NumPy, and SymPy installed, run:

```bash
python verify_wheel_gap.py
```

It reports `PASS 2141 symbolic, exact and numerical checks`. The program uses exact characteristic spectra for wheel sizes with \(n=3,4,6\), verifies rational critical-face points, and tests the general Rayleigh upper bounds and symmetric optima across additional wheel sizes and independently randomized conductances. The all-order proof above, not the finite tests, establishes the theorem and its optimizer rigidity.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulate the fastest-mixing **continuous-time** Markov-process problem as an eigenvalue optimization with a linear edge-cost budget and analyze paths and cycles explicitly. Their cycle calculation supplies the classical Fourier factor \(4\sin^2(\pi/n)\), but their worked examples do not classify weighted wheels or determine the price-dependent all-optimizer face established here. Boyd, Diaconis, Parrilo, and Xiao (2009, §5.4.3) do solve a **discrete-time** fastest-mixing problem on a wheel through Fourier blocks, with stochastic holding and second-largest-eigenvalue-modulus constraints. Their graph-spectrum block calculation is directly related; the constrained objective, price threshold, and complete continuous-time optimizer classification differ. Ghosh and Boyd (2006) present an algebraic-connectivity edge-addition relaxation, not this variable-weight exact theorem. Shakeri et al. (2015) establish budget transitions in multiplex networks with one-to-one interlayer couplings; those topologies and constraints differ.

The method of bounding a spectral minimum with trial vectors and exploiting automorphisms is classical. The claimed contribution is the joint exact rim-price threshold, full conductance allocation, **all-optimizer symmetry rigidity**, and critical nonunique face for arbitrary independently priced wheel weights. Similar formulas elsewhere in unindexed literature cannot be excluded.

## Limitations

Prices are uniform within each of two edge classes, the rim is a simple cycle, and the objective is the ordinary combinatorial Laplacian's second eigenvalue with linear budget. Vertex-dependent prices, degree caps, discrete-time stochastic restrictions, effective-resistance objectives, and arbitrary cone-over-base graphs are not treated. The checks of novelty cover identified scientific literature and records, not every unpublished or inaccessible work. Numerical tests do not certify infinite assertions or novelty.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: `10.1137/S0036144504443821`, full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf; earliest verified online-publication date 2006-11-02.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, DOI: `10.1137/070689413`; full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. A. Ghosh and S. Boyd, *Growing Well-Connected Graphs*, Proceedings IEEE CDC (2006), 6605–6611, full text: https://stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf.
4. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, preprint 2015, arXiv:1510.06785, https://arxiv.org/abs/1510.06785.
