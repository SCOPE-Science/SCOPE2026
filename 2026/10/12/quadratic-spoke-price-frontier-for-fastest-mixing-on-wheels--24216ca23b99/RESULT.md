# Quadratic spoke-price frontier for fastest mixing on wheels

## Finding

**Theorem (complete continuous-time wheel mixing design).** Let \(n\geq4\) be an integer, and write
\[
\mu_n=4\sin^2(\pi/n),\qquad T_n=1/\mu_n.
\]
Take a wheel graph with hub \(h\), cyclically indexed rim vertices \(v_0,\ldots,v_{n-1}\), spoke conductances \(a_j\geq0\), and rim conductances \(b_j\geq0\) on \(\{v_j,v_{j+1}\}\) (indices modulo \(n\)). A unit of spoke conductance has price \(t>0\); a unit of rim conductance costs one, with total expenditure
\[
\sum_{j=0}^{n-1}(t a_j+b_j)=1.
\]
For the symmetric continuous-time generator \(-L\), maximize the algebraic connectivity \(\lambda_2(L)\), which is the smallest nonzero eigenvalue whenever the positive-conductance graph is connected. The exact optimal value is
\[
\boxed{\lambda_2^*(n,t)=
\begin{cases}
\displaystyle\frac1{nt}, & 0<t\leq T_n,\\[5pt]
\displaystyle\frac{(n+1)\mu_n}{n(\mu_n t+n)}, & t\geq T_n.
\end{cases}}
\]
**Every optimizer**, allowing each edge its own independent conductance, is as follows.

* If \(0<t<T_n\), the optimizer is unique: \(a_j=1/(nt)\) and \(b_j=0\) for every \(j\). Thus the entire rim is optimally deleted and the spokes form a star.
* If \(t>T_n\), the optimizer is unique: for every \(j\),
\[
\boxed{a_j=\frac{\mu_n}{n(\mu_n t+n)},\qquad
b_j=\frac1{\mu_n t+n}.}
\]
* If \(t=T_n\), the **complete** optimizer family has equal rates \(a_j=a\) and \(b_j=b\) with
\[
\boxed{\frac{\mu_n}{n(n+1)}\leq a\leq\frac{\mu_n}{n},\qquad
b=\frac1n-\frac a{\mu_n}.}
\]
In particular, no asymmetric optimizer exists, including at the critical price.

The threshold has the asymptotic expansion
\[
T_n=\frac{n^2}{4\pi^2}+\frac1{12}+O(n^{-2}).
\]
For any fixed finite price \(t>0\), all sufficiently large wheels optimally delete every rim edge.

## Assumptions and scope

The graph is a simple undirected wheel with at least four rim vertices. All \(2n\) edge conductances are freely and independently chosen, may equal zero, and satisfy the stated exact unit-price budget. The hub and rim have equal vertex masses, so the generator is symmetric and its invariant distribution is uniform on \(n+1\) vertices. Time is continuous: no transition-matrix stochastic-row-sum constraints or discrete-time SLEM criterion is imposed. The objective is the Laplacian eigenvalue \(\lambda_2\), not the Kirchhoff index, hitting time, or effective-resistance sum. The stated optimal price is a ratio of spoke conductance price to rim conductance price.

For any nonnegative allocation, \(L\) is defined by
\[
x^{\mathsf T}Lx=\sum_{j=0}^{n-1}a_j(x_h-x_j)^2+\sum_{j=0}^{n-1}b_j(x_j-x_{j+1})^2.
\]
The eigenvalues are ordered \(0=\lambda_1(L)\leq\lambda_2(L)\leq\cdots\), including multiplicity, and disconnected choices have \(\lambda_2=0\). The maximizer always has strictly positive spoke conductances and is connected, including the all-rims-deleted branch.

## Proof

**1. Two universal Rayleigh bounds.** Set \(\bar a=n^{-1}\sum_j a_j\) and \(\bar b=n^{-1}\sum_j b_j\). By the budget, \(n(t\bar a+\bar b)=1\). The vector with hub coordinate \(-n\) and every rim coordinate \(1\) is perpendicular to the all-ones vector. Its Rayleigh quotient is \((n+1)\bar a\), hence
\[
\lambda_2(L)\leq(n+1)\bar a.\tag{1}
\]
Write \(\theta=2\pi/n\) and use the two real, zero-hub, orthogonal-to-constants vectors
\[
c_j=\cos(j\theta),\qquad s_j=\sin(j\theta),\qquad c_h=s_h=0.
\]
For \(n\geq4\), their squared norms are both \(n/2\). The identity \(c_j^2+s_j^2=1\), together with
\[
(c_j-c_{j+1})^2+(s_j-s_{j+1})^2=4\sin^2(\pi/n)=\mu_n,
\]
gives the exact average of the two Rayleigh quotients:
\[
\frac12\left(\frac{c^{\mathsf T}Lc}{c^{\mathsf T}c}
+\frac{s^{\mathsf T}Ls}{s^{\mathsf T}s}\right)
=\bar a+\mu_n\bar b.
\]
Since each quotient is at least \(\lambda_2(L)\),
\[
\lambda_2(L)\leq\bar a+\mu_n\bar b.
\tag{2}
\]
Both inequalities are global and require no symmetry of the edge allocation.

**2. Sharp budget optimization.** Substitute \(\bar a=(1/n-\bar b)/t\) into (1)--(2), with \(0\leq\bar b\leq1/n\). The bound to maximize is the minimum of the two affine functions
\[
f(\bar b)=\frac{n+1}{nt}-(n+1)\bar b/t,
\quad
g(\bar b)=\frac1{nt}+(\mu_n-1/t)\bar b.
\]
When \(t<T_n=1/\mu_n\), both \(f\) and \(g\) strictly decrease: the maximum is \(g(0)=1/(nt)\), attained only with \(\bar b=0\). When \(t>T_n\), \(f\) strictly decreases and \(g\) strictly increases. Their unique intersection occurs at
\[
\bar a=\frac{\mu_n}{n(\mu_n t+n)},
\qquad\bar b=\frac1{\mu_n t+n},
\]
and gives \((n+1)\mu_n/[n(\mu_n t+n)]\). When \(t=T_n\), \(g=\mu_n/n\) is constant over the budget line. The other bound requires \((n+1)\bar a\geq\mu_n/n\), equivalently \(\bar a\geq\mu_n/[n(n+1)]\); nonnegative rim budget requires \(\bar a\leq\mu_n/n\). These give all possible mean allocations at optimality.

**3. Attainment through the complete wheel spectrum.** For equal spoke conductances \(a\) and equal rim conductances \(b\), the Fourier decomposition of the Laplacian has the eigenvalue multiset
\[
\left\{0,\ (n+1)a,\ a+4b\sin^2(\pi k/n)\ (k=1,\ldots,n-1)\right\}.
\tag{3}
\]
In particular, \(\lambda_2=\min\{(n+1)a,a+\mu_n b\}\). Substitution of each displayed optimizer attains the corresponding upper bound in step 2. At the critical price, every stated pair \((a,b)\) attains \(\mu_n/n\), while the budget and both bounds exclude any other mean pair.

**4. Edgewise rigidity; no hidden asymmetric solutions.** Suppose an arbitrary feasible allocation attains the global optimum. In each of the three price regimes, step 2 shows that the inequality (2) is an equality. Thus both real Fourier vectors \(c\) and \(s\) have Rayleigh quotient \(\lambda_2(L)\): each quotient is at least \(\lambda_2(L)\), and their average equals it. By the symmetric-matrix Rayleigh equality criterion, both are eigenvectors of \(L\) at \(\lambda_2(L)\).

Consequently their complex combination \(z=c+\mathrm i s\), whose hub entry is zero and whose rim entries satisfy \(z_j=e^{\mathrm i j\theta}\), is also an eigenvector at that eigenvalue. At each rim vertex, dividing the eigenvector equation by \(z_j\neq0\) gives
\[
a_j+b_{j-1}(1-e^{-\mathrm i\theta})+b_j(1-e^{\mathrm i\theta})=\lambda_2(L).
\tag{4}
\]
The imaginary part of (4) is \((b_{j-1}-b_j)\sin\theta=0\). Since \(\sin(2\pi/n)\neq0\) for \(n\geq4\), all rim weights coincide. The real part then forces all spoke weights to coincide. This argument works even when some weights vanish or the optimal eigenspace is degenerate. Therefore **every** optimizer is uniform within each edge class, and step 2 characterizes the entire optimizer set.

**5. Large-ring price scale.** The Taylor expansion \(\csc^2 x=x^{-2}+1/3+O(x^2)\) at \(x=\pi/n\) proves \(T_n=n^2/(4\pi^2)+1/12+O(n^{-2})\), with the stated consequence for fixed \(t\). This is a pointwise fixed-price statement, not a claim about arbitrary \(n\)-dependent prices.

## Verification

A standalone verifier `check_wheel.py` reconstructs weighted Laplacians, checks exact rational spectra for the six-rim wheel (whose \(\mu_n\) is one), verifies the two universal Rayleigh identities for a nonsymmetric four-rim instance with rational conductances, and checks additional numerically evaluated optimal spectra and feasible nonsymmetric competitors. Its output from the supplied file is:

```text
VERIFY_OK 1246 supplementary finite wheel spectral and Rayleigh checks; analytical argument proves arbitrary size
```

Run it using `python check_wheel.py` with Python 3, NumPy, and SymPy. Finite tests are not a proof for all \(n\) or all real prices: steps 1--5 establish the quantified theorem. The rational checks establish exact identities only in the indicated finite examples; floating-point comparisons are subject to numerical tolerances. No external computation is required to reconstruct the proof.

For an interpretable exact example, \(n=6\) has \(\mu_6=1\) and critical spoke price \(T_6=1\). At \(t=2\) the unique optimum is \(a_j=1/48\), \(b_j=1/8\), with \(\lambda_2=7/48\); at \(t=1\), the entire optimum family is \(1/42\leq a\leq1/6\), \(b=1/6-a\), and \(\lambda_2=1/6\).

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis [1] formulate the continuous-time fastest-mixing Markov-process problem as maximizing the second graph-Laplacian eigenvalue under arbitrary positive linear edge costs and give general semidefinite and geometric dual machinery. This **covers the optimization framework**, but the inspected complete paper does not specify the wheel price frontier, critical continuum or asymmetric-optimizer rigidity.

Boyd, Diaconis, Parrilo and Xiao [2, Section 5.4.3] explicitly diagonalize a **wheel** using Fourier modes and solve a related **discrete-time** fastest-mixing Markov-chain problem minimizing second-largest eigenvalue modulus (SLEM), under stochasticity constraints. Their wheel eigenblock formulas directly anticipate (3), and they are the closest graph-specific antecedent. The objective and feasible constraints of the present theorem are different. Their discrete-time formula does not directly yield the continuous-time relative-price threshold, the all-rims-deleted optimal regime or the full edgewise-optimal face; the spectral method itself is not claimed as new.

Shafi, Arcak and El Ghaoui [3] give general convex optimization methods for graph Laplacian spectral constraints and examples on chains and clustered networks. Their full inspected paper does not supply this priced wheel classification. The result here is a graph-specific exact characterization with a sharp price boundary, not a new general-purpose SDP methodology. General reduction formulas and existing wheel spectral calculations could make rediscovery possible; no exhaustive novelty or independence guarantee is asserted.

## Limitations

This result is specific to symmetric **continuous-time** generators with **uniform vertex masses**, one spoke-price class, one rim-price class, and a single linear conductance budget. It does not address discrete-time SLEM, arbitrary vertex masses, nonuniform prices inside a class, upper bounds on individual rates, total effective resistance, spectral width, or optimal multistep mixing times. The result allows zero rim conductances and never requires deleting a spoke. It claims a complete global solution of the precisely stated mathematical objective, not a characterization of engineering performance under other resource models.

The framework and Fourier spectral decomposition are established prior work. Although inspected papers and mathematical-result searches did not disclose this complete explicit classification, an equivalent historical specialization not retrieved remains possible. An independent scholarly assessment has not been undertaken.

## References

[1] J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* **48** (2006), 681–699. DOI: 10.1137/S0036144504443821. Public full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published electronically 2006-11-02).

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* **20** (2009), 792–819, especially Section 5.4.3 on the wheel graph. DOI: 10.1137/070689413. Public full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] S. Y. Shafi, M. Arcak and L. El Ghaoui, “Graph Weight Allocation to Meet Laplacian Spectral Constraints,” *IEEE Transactions on Automatic Control* **57** (2012), 1872–1877. DOI: 10.1109/TAC.2011.2181795. Public full text: https://people.eecs.berkeley.edu/~elghaoui/Pubs/Laplace_tac2012.pdf.
