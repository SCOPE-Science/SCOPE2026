# Strict positivity-frontier monotonicity for Crank–Nicolson diffusion on rectangular discrete tori

## Finding
For every pair of integers \(m,n\ge3\), let \(G_{m,n}=C_m\square C_n\) be the unweighted Cartesian product of two simple cycles, with graph Laplacian \(L_{m,n}\). Define the Crank–Nicolson heat step and its resolvent by
\[
T_{m,n}(h)=(I+\tfrac h2 L_{m,n})^{-1}(I-\tfrac h2 L_{m,n}),\qquad
R_{m,n}(h)=(I+\tfrac h2 L_{m,n})^{-1},\quad h\ge0.
\]
Here the diffusion coefficient and square of the spatial mesh width are absorbed into the dimensionless step \(h\). There is a unique \(H_{m,n}>0\) such that \(T_{m,n}(h)\) is entrywise nonnegative **if and only if** \(0\le h\le H_{m,n}\). Set
\[
F_{m,n}(h)=\frac1{mn}\sum_{j=0}^{m-1}\sum_{k=0}^{n-1}
\frac1{1+h\bigl(2-\cos(2\pi j/m)-\cos(2\pi k/n)\bigr)}.
\]
Then \(H_{m,n}\) is the unique solution of \(F_{m,n}(h)=1/2\). Its **strict finite-size ordering** holds without requiring either period to divide another:
\[
H_{m+1,n}<H_{m,n},\qquad H_{m,n+1}<H_{m,n}\qquad(m,n\ge3).
\]
The largest threshold on this entire family is exactly
\[
H_{3,3}=\frac{1+\sqrt{57}}{14}.
\]
There is a universal limiting threshold \(H_\infty\), uniquely specified by
\[
\frac{2}{\pi(1+2H_\infty)}
K\!\left(\frac{2H_\infty}{1+2H_\infty}\right)=\frac12,
\qquad H_\infty\in(0.588197,0.588198),
\]
where \(K(z)=\int_0^{\pi/2}(1-z^2\sin^2 t)^{-1/2}\,dt\) denotes the complete elliptic integral with modulus \(z\). With \(z_\infty=2H_\infty/(1+2H_\infty)\in(0,1)\), every finite rectangular torus satisfies the quantitative sharp-limit enclosure
\[
0<H_{m,n}-H_\infty\le\frac{25}{2}z_\infty^{\min(m,n)}.
\]
Thus the step restriction becomes strictly tighter when either period is enlarged and approaches the two-dimensional infinite-lattice threshold exponentially as both periods tend to infinity.

## Assumptions and scope
The cycles are unweighted and simple; each period has at least three vertices. The graph \(C_m\square C_n\) has \(mn\) vertices and degree four, including for \(m=3\) or \(n=3\). All time-step and Laplacian parameters are real. Positivity means preservation of every nonnegative vector after one **complete** Crank–Nicolson step, equivalently entrywise nonnegativity of its matrix; it does not mean that the intermediate linear-solver right-hand side is nonnegative.

The normalized discrete Laplacian is **not** used: \(L_{m,n}=4I-A_{m,n}\), so \(h\) multiplies the unit-conductance combinatorial Laplacian. To apply the formula to the usual equal-mesh two-dimensional diffusion equation with diffusivity \(\kappa>0\), grid spacing \(\Delta x>0\), and physical time step \(\Delta t\), set \(h=\kappa\Delta t/(\Delta x)^2\).

## Proof
**1. Exact positivity test.** Write \(R=R_{m,n}(h)\). The matrix \(I+(h/2)L_{m,n}\) is a nonsingular irreducible \(M\)-matrix for \(h>0\), so \(R\) is strictly positive. The Cayley identity gives \(T=2R-I\). Every off-diagonal entry of \(T\) is positive; only diagonal entries can be negative. Translation-invariance makes all diagonal entries of \(R\) equal to \(F_{m,n}(h)\). The discrete Fourier eigenvalues are
\[
\lambda_{jk}=4-2\cos(2\pi j/m)-2\cos(2\pi k/n).
\]
Consequently \(T\ge0\) exactly when \(F_{m,n}(h)\ge1/2\). As \(h\) increases from zero to infinity, \(F_{m,n}\) decreases strictly from \(1\) to \(1/(mn)<1/2\): all terms except the unique zero-frequency term decrease strictly. Therefore the threshold exists and is unique.

**2. Strict ordering of periods.** For \(a>b>0\), define \(q=(a-\sqrt{a^2-b^2})/b\), so \(0<q<1\). The geometric Fourier expansion
\[
\frac1{a-b\cos t}
=\frac1{\sqrt{a^2-b^2}}\sum_{\ell\in\mathbb Z}q^{|\ell|}e^{i\ell t}
\]
implies, by averaging over the \(n\)th roots of unity,
\[
\frac1n\sum_{k=0}^{n-1}\frac1{a-b\cos(2\pi k/n)}
=\frac{1+q^n}{\sqrt{a^2-b^2}(1-q^n)}.
\]
At fixed \(h>0\) and \(m\), apply the formula with \(a=1+2h-h\cos(2\pi j/m)>h=b\). Since \((1+q^n)/(1-q^n)\) decreases strictly with the positive integer \(n\), each summand in the remaining \(m\)-average decreases strictly as \(n\) increases. Thus
\[
F_{m,n+1}(h)<F_{m,n}(h)\quad(h>0).
\]
Interchanging the two cycle factors proves the corresponding strict inequality in \(m\). Their unique crossings of \(1/2\) inherit the claimed strict ordering. The spectrum of \(C_3\square C_3\) consists of \(0\) once, \(3\) four times, and \(6\) four times. Hence
\[
F_{3,3}(h)=\frac19\left(1+\frac4{1+3h/2}+\frac4{1+3h}\right).
\]
Setting it to \(1/2\) reduces to \(7h^2-h-2=0\), proving the stated maximum. In particular, \(H_{m,n}<1\) uniformly.

**3. Infinite-lattice limit.** For \(h>0\), put \(z=2h/(1+2h)\). If \(P\) is the simple random-walk transition matrix on the torus, then
\[
R_{m,n}(h)=\frac1{1+2h}(I-zP)^{-1}
=\frac1{1+2h}\sum_{t\ge0}z^tP^t.
\]
The same geometric series holds for the simple random walk on \(\mathbb Z^2\). Denote its weighted return sum by \(F_\infty(h)\). By Fourier inversion, followed by the standard square-lattice Green-function integral (also explicitly recorded in Guttmann 2010),
\[
F_\infty(h)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
\frac{d\theta\,d\phi}{1+2h-h(\cos\theta+\cos\phi)}
=\frac{2}{\pi(1+2h)}K(z).
\]
This strictly decreases continuously from \(1\) to \(0\) as \(h\) goes from \(0\) to infinity, giving a unique \(H_\infty\) at level \(1/2\). (The limit to zero follows by dominated convergence on the Fourier integral, since the zero Fourier mode has measure zero.)

Lift the torus walk to \(\mathbb Z^2\). A torus return corresponds to reaching some displacement \((um,vn)\), where \(u,v\) are integers. Therefore
\[
F_{m,n}(h)-F_\infty(h)
=\frac1{1+2h}\sum_{t\ge0}z^t
\sum_{(u,v)\ne(0,0)}\Pr\{X_t=(um,vn)\}.
\]
Every term is nonnegative; one is positive, for example a path of length \(m\) moving only right. A nonzero such displacement requires at least \(\min(m,n)\) steps, and the total probability in the inner sum is at most one. Consequently
\[
0<F_{m,n}(h)-F_\infty(h)\le z^{\min(m,n)}.
\]
At \(h=H_\infty\), this implies \(H_{m,n}>H_\infty\). Furthermore, writing the Fourier sum for the derivative gives
\[
-F'_{m,n}(h)=\frac1{2mn}\sum_{j,k}
\frac{\lambda_{jk}}{(1+h\lambda_{jk}/2)^2}.
\]
Because \(0\le\lambda_{jk}\le8\) and their average is \(4\),
\[
-F'_{m,n}(h)\ge\frac2{(1+4h)^2}\ge\frac2{25}
\quad\text{whenever }0\le h\le H_{m,n}<1.
\]
The mean-value theorem applied between \(H_\infty\) and \(H_{m,n}\), together with the preceding return bound at \(H_\infty\), yields
\[
0<H_{m,n}-H_\infty\le\frac{25}{2}z_\infty^{\min(m,n)},
\]
which proves the exponential enclosure.

**4. Certified numerical interval.** The known square-lattice Green-function expansion is
\[
F_\infty(h)=\frac1{1+2h}\sum_{k=0}^\infty
\frac{\binom{2k}{k}^2}{16^k}z^{2k}.
\]
Truncating before term \(k=23\) gives an exact rational lower bound; the omitted tail is at most \(z^{46}/((1+2h)(1-z^2))\), since every displayed binomial coefficient ratio is at most one. Rational evaluation of the lower bound at \(h=588197/10^6\) exceeds \(1/2\), while the corresponding upper bound at \(h=588198/10^6\) is below \(1/2\). This certifies the stated interval without relying on decimal floating-point output.

## Verification
The standalone `verify_torus.py` uses only the Python standard library. It builds graph Laplacians, exactly inverts \(I+(h/2)L\) over rational numbers for five small rectangular tori at three rational steps each, checks positive resolvent entries, mass preservation, the diagonal threshold test, and agreement with the Fourier formula. Independent floating-point spectral bisections check strict ordering for every pair of periods between three and eight. An arithmetic-geometric-mean evaluation checks the elliptic limit and exponential bound; exact rational binomial-series bounds certify \(0.588197<H_\infty<0.588198\). These checks test the formulas but do not replace the preceding proof for all periods.

## Relationship to prior work
The general resolvent-diagonal positivity equivalence for Crank–Nicolson on finite Markov generators, and the uniqueness of each reversible-chain crossing, are explicitly established in the earlier published result *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*. Neither fact is claimed new. The new structural content here is strict threshold monotonicity **for every increment** in either rectangular torus period, the exact extremal small torus, and a quantitative two-dimensional limit with exponential finite-size error.

Guttmann's *Lattice Green functions in all dimensions* (arXiv:1004.1435v1, 8 April 2010) gives the square-lattice elliptic Green-function formula used above. That formula, and the existence of a limiting crossing when combined with the general positivity criterion, are prior implications; the present claim does not assert that this elliptic evaluation was discovered here. Higueras and Roldán (arXiv:2301.01066) derive Crank–Nicolson positivity thresholds under **one-dimensional homogeneous Dirichlet** boundaries, not two-dimensional periodic boundaries. The published filtered Crank–Nicolson lattice result concerns a distinct composite integrator on a one-dimensional lattice, not this unfiltered two-dimensional step. The archive source and accessible subsequent primary text were compared at theorem and proof level, not just by title. Higueras and Roldán also cite a 2022 manuscript titled *On the positivity and contractivity of Crank–Nicolson method applied to the periodic diffusion problem*. Its full text could not be located through the available arXiv/open-access search or institutional retrieval; its title alone does not establish dimension or theorem coverage, and it remains a specifically identified originality risk.

## Limitations
The theorem concerns one linear Crank–Nicolson end-step on a unit-weight, equal-spacing, rectangular **periodic** lattice. It does not cover variable conductances, nonperiodic boundaries, anisotropic diffusion, nonlinear limiters, or stage-by-stage positivity. Matrix nonnegativity gives neither an accuracy guarantee nor an advantage to taking near-threshold steps for any particular PDE solution. The finite-size thresholds are characterized by an exact one-variable equation rather than a closed radical for arbitrary periods. The elliptic integral identity is established prior knowledge. Although no equivalent finite-size monotonicity and exponential positivity-frontier result was located in the inspected sources, other finite-torus Green-function or numerical-positivity literature may contain a reformulation, notably the inaccessible 2022 periodic-diffusion manuscript named above.

## References
1. Anthony J. Guttmann, *Lattice Green functions in all dimensions*, arXiv:1004.1435v1 (public 8 April 2010), https://arxiv.org/abs/1004.1435 . Square-lattice Green function: equation (4).
2. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066v1 (public 3 January 2023), https://arxiv.org/abs/2301.01066 . Boundary conditions and positivity theorem: sections 1–3.
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a . General exact resolvent criterion and crossing law.
4. *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac . One-dimensional filtered scheme.
5. I. Higueras and T. Roldán, *On the positivity and contractivity of Crank–Nicolson method applied to the periodic diffusion problem*, cited as a 2022 manuscript in reference [10] of arXiv:2301.01066v1; direct full text not accessed, bibliographic details beyond that citation unverified.
