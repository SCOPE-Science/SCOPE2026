# An exact jammed-state polynomial and entropy for the Kob–Andersen square ladder

## Finding
On the two-leg periodic square ladder \(C_n\square K_2\), \(n\ge4\), use the conservative Kob–Andersen constraint in which a particle may hop to a vacant neighboring vertex exactly when its departure site has **another** vacant neighbor before the hop and its arrival site has **another** vacant neighbor after the hop (in addition to the vacancy supplied by the exchanged pair). A configuration is jammed if no hop is permitted.

Let \(Z_n(z)=\sum_{\eta\text{ jammed}}z^{N(\eta)}\), with \(N\) the number of particles. Define the two explicit polynomials

\[G(x,z)=x^5-z^2x^3+z^4x^2+z^5x-z^7,\]
\[F(x,z)=x^8-(1+z)^2x^7+(2z+2z^2)x^6-(z^4+z^2)x^5+(3z^5-z^6)x^4+(4z^7-z^5)x^3+(z^9-z^8-2z^7)x^2-2z^9x-z^{11}.\]

The complete grand-canonical finite-volume enumeration is obtained by defining \(g(t,z)=t^5G(1/t,z)\) and \(f(t,z)=t^8F(1/t,z)\). Then, as a formal power series,

\[\sum_{n\ge1} Z_n(z)t^n=-t\frac{\partial}{\partial t}\log\bigl(f(t,z)g(t,z)\bigr).\]

The coefficients for \(n=1,2,3\) are formal transfer-matrix extensions; the physical statement is for \(n\ge4\). In particular, \(Z_4(1),\ldots,Z_8(1)\) are \(54,129,319,837,2150\).

The number of jammed configurations grows exponentially, with entropy per rung

\[\lim_{n\to\infty}\frac1n\log Z_n(1)=\log\lambda,\quad\lambda=2.605506658540588\ldots,\]

where \(\lambda\) is the unique real root exceeding \(2\) of

\[x^8-4x^7+4x^6-2x^5+2x^4+3x^3-2x^2-2x-1=0.\]

Under the uniform measure on jammed configurations the occupied-site fraction converges in probability to \(\rho_\star=0.736222013311\ldots\). Equivalently,

\[\rho_\star=-\frac{F_z(\lambda,1)}{2\lambda F_x(\lambda,1)}.\]

## Assumptions and scope
Every rung has two Boolean occupancies, and every vertex has three distinct neighbors: two neighboring vertices along its leg and its rung-mate. The two legs are periodic in the rung index. Every particle has at most one occupancy unit, and hops exchange an occupied site and an adjacent empty site; no other moves are allowed. The constraint is imposed at both ends of each proposed hop. The transfer-variable \(z\) marks particles, not vacancies. A jammed configuration is one with zero enabled hops, not necessarily a configuration unreachable from other states.

## Proof
Label a rung by \(r=(r_0,r_1)\in\{0,1\}^2\). Consider four consecutive rungs \((a,b,c,d)\), and declare their central test valid exactly when there are no enabled hops on the rung edge in \(b\) and the two longitudinal edges from \(b\) to \(c\). For any edge \(u-v\) with occupancies \(1,0\), respectively, the hop is enabled if and only if at least one of the two other neighbors of \(u\) is empty AND at least one of the two other neighbors of \(v\) is empty. This test depends only on these four rungs. A periodic word of rungs is jammed if and only if all \(n\) central tests succeed: each rung edge and each longitudinal edge is inspected once.

Make the \(64\)-state de Bruijn transfer matrix \(T(z)\) indexed by triples of rungs. Insert the weighted edge \((a,b,c)\to(b,c,d)\) with weight \(z^{d_0+d_1}\) if the above local test succeeds, and zero otherwise. By a bijection between closed walks of length \(n\) and periodic rung words of length \(n\), every permitted configuration contributes exactly its monomial and

\[Z_n(z)=\operatorname{tr}T(z)^n\quad(n\ge4).\]

The exact finite matrix computation in the accompanying checker performs the local Boolean tests on all \(4^4=256\) quadruples, producing \(108\) permitted weighted transitions. It identifies one aperiodic strongly connected recurrent class of \(29\) transfer states (containing a loop); all other states lie on no directed cycle. Exact symbolic characteristic-polynomial elimination on the recurrent block gives

\[\det(xI-T_{\mathrm{rec}}(z))=x^{16}F(x,z)G(x,z),\]

and hence the full characteristic polynomial is \(x^{51}F(x,z)G(x,z)\). The determinant identity and the trace/logarithmic-derivative identity yield the generating function stated above. No extrapolation from finite data is used here.

At \(z=1\), the recurrent matrix is nonnegative, irreducible and aperiodic. Perron–Frobenius therefore supplies a simple strictly dominant positive eigenvalue \(\lambda\). The quintic factor cannot supply it: on \(|x|=2\) its leading term has modulus \(32\), greater than the sum \(8+4+2+1\) of the other term moduli, so every quintic root lies within \(|x|<2\) by Rouché's theorem. The octic has a real root between \(2\) and \(3\): its value at \(2\) is \(-21\), at \(3\) positive. Shifting \(x=y+2\) gives

\[y^8+12y^7+60y^6+158y^5+222y^4+131y^3-32y^2-70y-21,\]

with exactly one sign change in descending order. Descartes' rule gives exactly one root above \(2\). Consequently this root equals the Perron root, proving the exponential growth assertion.

For \(z\) in an open neighborhood of \(1\), positivity on the same primitive recurrent support makes the Perron eigenvalue \(\lambda(z)\) analytic and strictly dominant. Therefore \(\log Z_n(z)=n\log\lambda(z)+O(1)\), together with uniform control of the first two derivatives. The mean particle number is \(n\lambda'(1)/\lambda(1)+O(1)\) and its variance is \(O(n)\). Differentiating \(F(\lambda(z),z)=0\) yields the stated density, and Chebyshev's inequality establishes convergence in probability.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The checker reconstructs every permitted transition, verifies the unique recurrent strongly connected class and aperiodicity, proves the complete weighted characteristic-polynomial identity by exact symbolic arithmetic, and independently enumerates all configurations on each ladder \(n=4,5,6,7,8\) using the physical-graph hop rules. It compares the full occupancy-graded counts from enumeration with Newton-sum coefficients extracted from the characteristic polynomial. The verified totals are \(54,129,319,837,2150\). It checks the numerical Perron root and particle density as supplementary tests. Finite exhaustive checks corroborate the transfer rule; the infinite-volume theorem relies on the analytic matrix argument above.

## Relationship to prior work
Toninelli, Biroli and Fisher (2004/2005) develop the Kob–Andersen dynamics and discuss frozen slabs and the general behavior of infinite hypercubic and Bethe lattices. Their exact results do not provide the fully graded finite-volume enumeration on a periodic two-leg square ladder. In particular, this narrow cylinder is not covered by their infinite-lattice ergodicity theorem. De Oliveira (2005) studies a distinct conserved lattice gas on a ladder: a particle's activity is controlled by *occupied* neighbors, and the ladder phase behavior is studied numerically, not by the present two-end Kob–Andersen vacancy rule. Jack (2013) counts metastable configurations of the nonconserved East model. Raj, Oganesyan and Scardicchio (2024) examine a triangular-ladder rule allowing hops only within single-occupied triangles, which is neither the square graph nor the two-end vacancy rule. These comparisons do not establish absence of all possible unindexed equivalent computations.

## Limitations
The result counts configurations with no currently allowed transition, not the sizes of their basins, dynamically reached jamming probabilities, spectral gaps, or relaxation times. The thermodynamic entropy is per rung; per vertex it is half this value. The model is a width-two periodic ladder with degree-three sites, not a square lattice with periodic transverse period two interpreted as a multigraph. Literature priority has not been independently certified.

## References
1. C. Toninelli, G. Biroli and D. S. Fisher, *Cooperative Behavior of Kinetically Constrained Lattice Gas Models of Glassy Dynamics*, arXiv:cond-mat/0410647, first posted 2004-10-25, https://arxiv.org/abs/cond-mat/0410647.
2. M. J. de Oliveira, *Conserved lattice gas model with infinitely many absorbing states in one dimension*, Physical Review E **71** (2005) 016112, https://doi.org/10.1103/PhysRevE.71.016112.
3. R. L. Jack, *Counting metastable states in a kinetically constrained model using a patch repetition analysis*, arXiv:1309.6247 (2013), https://arxiv.org/abs/1309.6247.
4. A. Raj, V. Oganesyan and A. Scardicchio, *A kinetically constrained model exhibiting non-linear diffusion and jamming*, arXiv:2412.05231 (2024), https://arxiv.org/abs/2412.05231.
