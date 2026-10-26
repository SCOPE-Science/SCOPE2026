# Exact qubit metric-cotype constants and a three-level trace-distance separation

## Finding
For each even integer \(m\ge4\), integer \(n\ge1\), and Schatten exponent \(1\le p\le\infty\), let \(K_{m,n}^{(d,p)}\) be the least constant such that every function \(F:(\mathbb Z/m\mathbb Z)^n\to\mathcal D_d\) satisfies
\[
\sum_{j=1}^n\mathbb E_x\bigl\|F(x+(m/2)e_j)-F(x)\bigr\|_{S_p}^2
\le (K_{m,n}^{(d,p)})^2\,\mathbb E_{x,\varepsilon}\bigl\|F(x+\varepsilon)-F(x)\bigr\|_{S_p}^2,
\]
where \(\mathcal D_d\) consists of complex positive semidefinite \(d\times d\) matrices of trace one; \(x\) is uniform on the torus and \(\varepsilon\) is independent and uniform on \(\{-1,0,1\}^n\).

**Theorem (exact qubit constant and first strict trace-distance dimension gap).** For every specified \(m,n,p\),
\[
\boxed{(K_{m,n}^{(2,p)})^2=\frac{2n}{1-\bigl((1+2\cos(2\pi/m))/3\bigr)^n}.}
\]
A nonconstant qubit map attains equality if and only if the Fourier support of its Bloch vector, excluding its constant term, lies in \(\{1,m-1\}^n\). In particular, pure-state maps attain the bound.

At the smallest two-dimensional even-torus test \((m,n)=(4,2)\), the trace-distance geometry displays a strict state-dimension separation:
\[
\boxed{(K_{4,2}^{(2,1)})^2=\frac92,\qquad (K_{4,2}^{(d,1)})^2\ge5\quad\text{for every }d\ge3.}
\]
The lower bound \(5\) is attained as a ratio by an explicit commuting four-state map; it is **not** claimed to be the optimal qutrit constant. The gap is witnessed entirely inside classical three-outcome probability distributions, so it is a genuinely nonlinear trace-distance effect, not a consequence of noncommutativity.

## Assumptions and scope
All groups are finite and use normalized counting measure. Matrix norms are the usual Schatten norms; at \(p=\infty\) this means operator norm. The constants here are the **unnormalized** least multipliers (the conventional metric-cotype constant with an \(m^2\) factor would divide \(K_{m,n}^{(d,p)}\) by \(m\)). A zero denominator means the map is constant, so the inequality is then automatic. The qubit equality classification concerns nonconstant maps with Bloch vectors in the closed Euclidean unit ball; Fourier support is taken componentwise over \(\mathbb C^3\).

## Proof
**1. Reduction of every qubit Schatten metric to Euclidean distance.** Write each qubit state uniquely as \(\rho(r)=(I+r\cdot\sigma)/2\) with \(r\in\mathbb R^3\), \(|r|\le1\), and Pauli matrices \(\sigma\). For any \(r,s\), the traceless Hermitian difference has eigenvalues \(\pm|r-s|/2\). Hence
\[
\|\rho(r)-\rho(s)\|_{S_p}=2^{1/p-1}|r-s|\quad(1\le p\le\infty),
\]
with \(1/\infty=0\). The common factor cancels in the squared ratio. It is therefore enough to determine the sharp Euclidean quadratic difference ratio on the finite torus, provided one can realize an extremal Fourier mode inside the Bloch ball.

**2. Exact Fourier multipliers.** Let \(G=(\mathbb Z/m\mathbb Z)^n\) and write \(\chi_k(x)=\exp(2\pi i\,k\cdot x/m)\). For any real-vector-valued map \(r:G\to\mathbb R^3\), Parseval gives
\[
L(r)=4\sum_{k\in G}s(k)|\widehat r(k)|^2,
\qquad
R(r)=2\sum_{k\in G}(1-Q(k))|\widehat r(k)|^2,
\]
where \(s(k)\) counts the odd coordinates of \(k\), and
\[
Q(k)=\prod_{j=1}^n q(k_j),\qquad
q(h)=\frac{1+2\cos(2\pi h/m)}3.
\]
Indeed \(\chi_k(x+(m/2)e_j)=(-1)^{k_j}\chi_k(x)\), whereas \(\mathbb E_{\varepsilon_j}\chi_k(\varepsilon_j)=q(k_j)\). At the zero frequency both energies vanish. At any nonzero frequency \(1-Q(k)>0\).

**3. The sharp spectral bound and its equality frequencies.** Set \(a=q(1)=(1+2\cos(2\pi/m))/3\), so \(1/3\le a<1\). For every odd residue \(h\) modulo \(m\), \(|q(h)|\le a\); for an even residue \(|q(h)|\le1\). Therefore, whenever \(s=s(k)\ge1\), \(Q(k)\le a^s\) and
\[
\frac{2s(k)}{1-Q(k)}\le\frac{2s}{1-a^s}\le\frac{2n}{1-a^n}.
\]
The last inequality follows since \(t/(1-a^t)\) is strictly increasing for positive \(t\): its derivative has numerator \(1-e^{-ut}(1+ut)>0\), where \(u=-\log a>0\). When \(s=0\), \(L\)'s multiplier is zero. Equality at a nonzero frequency requires \(s=n\) and \(q(k_j)=a\) for every \(j\). Among odd residues this occurs exactly when \(k_j\equiv\pm1\pmod m\). Thus Parseval gives the upper bound and the stated complete Fourier-support characterization of its nonconstant equality maps.

For existence, take \(r(x)=(\cos(2\pi\sum_jx_j/m),\sin(2\pi\sum_jx_j/m),0)\). This is a unit Bloch vector at every point, defines pure states, and has frequencies \(\pm(1,\ldots,1)\). It attains equality for every \(m,n,p\), proving the optimality of the formula.

**4. Exact rational three-level obstruction.** Put
\[
\begin{aligned}
\rho_0&=\operatorname{diag}(1/2,1/3,1/6),&
\rho_1&=\operatorname{diag}(1/6,2/3,1/6),\\
\rho_2&=\operatorname{diag}(1/6,1/3,1/2),&
\rho_3&=\operatorname{diag}(1/2,0,1/2).
\end{aligned}
\]
Each matrix is positive semidefinite and has trace one. Define \(F:(\mathbb Z/4\mathbb Z)^2\to\mathcal D_3\) by \(F(x_1,x_2)=\rho_{(x_1+x_2)\bmod4}\). Consecutive pairs in this cycle have trace norm distance \(2/3\). The opposite pairs \((\rho_0,\rho_2)\) and \((\rho_1,\rho_3)\) have distances \(2/3\) and \(4/3\), respectively. Hence the averaged **squared** long-increment distance is \(\tfrac12(4/9+16/9)=10/9\) for each coordinate, making \(L(F)=20/9\).

For \(\varepsilon\in\{-1,0,1\}^2\), the sum \(\varepsilon_1+\varepsilon_2\) is congruent to \(0,\pm1,2\pmod4\) with respective probabilities \(3/9,4/9,2/9\) (the middle probability includes both signs). Thus
\[
R(F)=\frac49\cdot\frac49+\frac29\cdot\frac{10}9=\frac49,
\qquad \frac{L(F)}{R(F)}=5.
\]
The qubit formula at \((m,n)=(4,2)\) gives \(2n/(1-(1/3)^n)=9/2\), strictly below \(5\). For every \(d>3\), appending a zero block preserves positivity, trace, and the trace distances, so the same lower bound holds.

## Verification
The included standalone `CHECK.py` performs **exact rational arithmetic** for the three-level witness: it verifies positivity, unit traces, long energy \(20/9\), short energy \(4/9\), and ratio \(5\) by averaging every element of the \(4\times4\) torus and every ternary increment. It also checks 15 independent qubit pure-mode configurations numerically for even side lengths \(4,6,8,10,12\) and dimensions \(1,2,3\), with tolerance \(10^{-9}\). The latter tests are finite consistency checks, not a substitute for the all-parameter Fourier proof. Execute `python CHECK.py` with Python 3; no third-party packages are required.

## Relationship to prior work
Mendel and Naor introduced the discrete-torus definition of metric cotype and established its connection to Banach-space cotype. Jiao, Luo, and Wu proved the sharp *scaling order* for general Schatten trace-class maps, uniformly over all matrix dimensions, but their bound \((3\sqrt{70}\,m+6\sqrt n)^2\) does not determine the finite-dimensional best constants or exhibit a strict qubit/qutrit boundary. A published scalar Hilbert-space calculation determines exact constants for a **different**, sign-only increment distribution on the torus; that calculation provides a closely related Fourier method but not the ternary-increment matrix-state comparison or its three-outcome obstruction. A published Schatten-four qutrit geometry result concerns nonexpansivity of nearest-state projection rather than metric cotype.

## Limitations
The exact formula is proved only on qubit states, not on arbitrary matrices or higher-dimensional state spaces. For qutrits and larger state spaces only the lower bound at the single natural test \((m,n,p)=(4,2,1)\) is claimed; no optimal qutrit constant is computed. The dimensional separation is a finite-scale distinction, not a proof of different asymptotic scaling orders. The counterexample uses commuting matrices; it therefore does not isolate noncommutativity. Older unindexed metric-cotype or nonlinear Poincaré computations could conceivably include an equivalent four-cycle test.

## References
1. Y. Jiao, S. Luo and L. Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1, first posted 2026-10-15; Theorem 1.3 and Section 6. https://arxiv.org/html/2610.21445v1
2. M. Mendel and A. Naor, *Metric cotype*, Annals of Mathematics **168** (2008), 247–298, doi:10.4007/annals.2008.168.247.
3. *Exact scalar \(L_2\) metric-cotype lifting constant on even discrete tori*, published-finding corpus public mathematical finding (2026-10-04), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-scalar-l-2-metric-cotype-lifting-constant-on-even-discrete--1ca79d58fa4e ; its increments are uniform signs rather than uniform ternary steps.
4. *The qutrit Schatten-four exception in nonexpansivity of nearest-density-matrix projection*, published-finding corpus public mathematical finding (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-qutrit-schatten-four-exception-in-nonexpansivity-of-nearest--0ee9403dce0d .
