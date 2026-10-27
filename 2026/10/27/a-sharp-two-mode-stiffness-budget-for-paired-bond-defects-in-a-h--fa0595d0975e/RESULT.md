# A sharp two-mode stiffness budget for paired bond defects in a harmonic chain

## Finding
For an infinite monatomic harmonic chain with unit masses and unit reference springs, strengthen the bond from site \(0\) to \(1\) by \(\alpha>0\), and the bond from site \(d\) to \(d+1\) by \(\beta>0\), where \(d\) is any positive integer. The exact number \(N\) of spatially square-summable normal modes whose squared frequency lies above the unperturbed band \([0,4]\) is
\[
N=1+\mathbf 1_{\left\{2(2d-1)\alpha\beta>(\alpha+\beta)\right\}}.
\]
At equality, the second mode is only a band-edge threshold solution, not a square-summable normal mode. There is no isolated squared frequency below the band or embedded within it.

For any fixed total excess spring stiffness \(S=\alpha+\beta>0\), two such localized modes are achievable **if and only if**
\[
S>\frac{2}{2d-1}.
\]
Among positive allocations with this fixed \(S\), the equal allocation \(\alpha=\beta=S/2\) uniquely maximizes the lower isolated squared frequency wherever the lower mode exists. It also uniquely minimizes the upper isolated squared frequency for every \(S>0\). Thus equal allocation is the most effective way to obtain and spectrally protect the additional localized branch at fixed stiffness budget.

For equal defects \(\alpha=\beta=a\), put \(a_c=1/(2d-1)\). As \(a\downarrow a_c\) from above, the second squared frequency \(\lambda_{\mathrm{low}}\) emerges by the sharp quadratic law
\[
\lambda_{\mathrm{low}}-4
=\frac{(2d-1)^4}{d^4}(a-a_c)^2+O_d((a-a_c)^3).
\]
The edge coefficient is positive for every \(d\ge1\); no finite positive parameter attains a second localized state at equality.

## Assumptions and scope
The sites form \(\mathbb Z\). All masses equal one, all springs are conservative, and the spring between sites \(j\) and \(j+1\) has stiffness \(w_j\), with \(w_0=1+\alpha\), \(w_d=1+\beta\), and all other \(w_j=1\). Here \(d\ge1\) ensures the bonds are distinct. The squared-frequency operator on \(\ell^2(\mathbb Z)\) is the self-adjoint bounded nonnegative operator
\[
(Hu)_j=w_{j-1}(u_j-u_{j-1})+w_j(u_j-u_{j+1}).
\]
An isolated normal mode means an \(\ell^2\) eigenvector, not a generalized scattering solution. Frequencies in the display are squared and nondimensional; for physical reference spring \(k_0\) and mass \(m\), multiply squared frequencies by \(k_0/m\). At fixed \(S\), the allocation statements concern strictly positive \(\alpha,\beta\); no claim of a localized lower mode is made where it does not exist.

## Proof
**1. The rank-two defect resolvent.** Let \(L=2I-T-T^{-1}\) be the perfect-chain discrete Laplacian and \(g_j=e_j-e_{j+1}\). Then
\[
H=L+\alpha |g_0\rangle\langle g_0|+\beta|g_d\rangle\langle g_d|.
\]
The essential spectrum is \([0,4]\) by finite-rank invariance. Positivity excludes eigenvalues below zero. Within the open band, solutions of the free recurrence outside the finite defect region are superpositions of nondecaying plane waves, so square summability forces them to vanish on both tails and hence everywhere by the nearest-neighbor recurrence. The same recurrence excludes embedded edge eigenvectors at \(0\) or \(4\).

For \(\lambda>4\), parameterize \(\lambda=2+2\cosh t=2+q+q^{-1}\), with \(t>0\) and \(q=e^{-t}\in(0,1)\). The positive resolvent kernel of \(\lambda-L\) is
\[
\langle e_i,(\lambda-L)^{-1}e_j\rangle
=\frac{(-1)^{i-j}q^{|i-j|}}{q^{-1}-q}.
\]
The Birman--Schwinger matrix for the two bonds, after conjugating away an irrelevant off-diagonal sign, is
\[
K(q)=\begin{pmatrix}
\alpha B(q)&\sqrt{\alpha\beta}\,C_d(q)\\
\sqrt{\alpha\beta}\,C_d(q)&\beta B(q)
\end{pmatrix},\qquad
B(q)=\frac{2q}{1-q},\qquad
C_d(q)=\frac{q^d(1+q)}{1-q}.
\]
The positive eigenvalues of \(H\) above \(4\) correspond, including multiplicity, precisely to solutions of \(1\in\sigma(K(q))\). For \(d\ge1\), \(0<C_d(q)<B(q)\), so the two eigenvalues \(\kappa_-(q)<\kappa_+(q)\) of \(K(q)\) are strictly positive.

**2. Exact count and threshold.** As \(\lambda\) increases on \((4,\infty)\), the resolvent strictly decreases as a quadratic form on the span of the two independent bond vectors. Thus both Birman--Schwinger eigenvalues strictly decrease from their limits at \(\lambda\downarrow4\) to zero at infinity. The larger eigenvalue diverges at the upper band edge. Set
\[
F_d(q):=B(q)-C_d(q)=2\sum_{j=1}^{d-1}q^j+q^d.
\]
The polynomial is strictly increasing on \((0,1)\), with \(F_d(1)=2d-1\). The determinant identity
\[
\kappa_-(q)\kappa_+(q)=\alpha\beta\,[B(q)-C_d(q)][B(q)+C_d(q)]
\]
and \(\kappa_+(q)\sim2(\alpha+\beta)/(1-q)\) as \(q\uparrow1\) show that
\[
\lim_{q\uparrow1}\kappa_-(q)=\frac{2\alpha\beta}{\alpha+\beta}(2d-1).
\]
It follows that the larger eigenvalue crosses one exactly once for every positive pair, and the smaller crosses one exactly once if and only if its band-edge limit is strictly greater than one. Equality is a non-\(\ell^2\) threshold, by the outer-tail recurrence in step 1. This proves the count, including all boundaries.

**3. Fixed-budget optimum.** Put \(S=\alpha+\beta\) and \(P=\alpha\beta\). Direct diagonalization gives
\[
\kappa_\pm(q)=\frac{SB(q)}2\pm\sqrt{\frac{S^2B(q)^2}{4}-P\,[B(q)^2-C_d(q)^2]}.
\]
Because \(B(q)>C_d(q)>0\), at every fixed \(q\in(0,1)\) the smaller eigenvalue increases strictly with \(P\), whereas the larger decreases strictly. At a fixed sum \(S\), the product \(P\) is uniquely maximized at \(\alpha=\beta=S/2\). Inverting each strictly monotone eigenvalue crossing transfers this ordering to the isolated squared frequencies: the equal split uniquely maximizes the lower branch and minimizes the upper branch. Moreover
\[
\frac{2\alpha\beta}{\alpha+\beta}\le \frac S2
\]
with equality only at the equal split. The lower-edge crossing is therefore achievable exactly when \((2d-1)S/2>1\), proving the sharp strict budget threshold.

**4. Quadratic edge emergence.** For equal strengths \(a\), the lower Birman--Schwinger eigenvalue is exactly \(aF_d(q)\). The equation for the emerging mode is \(aF_d(e^{-t})=1\). From the finite polynomial,
\[
F_d(e^{-t})=(2d-1)-d^2t+O_d(t^2).
\]
Writing \(a=a_c+\varepsilon\) and applying the analytic implicit-function theorem at \(\varepsilon=t=0\) gives
\[
t=\frac{(2d-1)^2}{d^2}\varepsilon+O_d(\varepsilon^2).
\]
Since \(\lambda-4=2(\cosh t-1)=t^2+O(t^4)\), substitution yields the asserted quadratic coefficient and the cubic error bound.

## Verification
The accompanying `checker.py` independently builds a finite nonuniform spring Jacobi matrix and finds its two largest eigenvalues through a Sturm-inertia bisection, without diagonalizing the infinite resolvent. It also checks the finite-rank formulas, the balanced-allocation inequalities and the quadratic edge coefficient. Executing `python3 checker.py` with a Python 3 standard-library installation reports 56 successful finite comparisons. Finite-size comparisons are made away from threshold regimes where a large chain is needed to distinguish an edge state; the exact mode count and asymptotics rest on the analytical proof, not on extrapolation.

## Relationship to prior work
Montroll and Potts (1955) developed the general Green-function treatment of lattice defects and investigated pair interactions. Poon and Bienenstock (1966) considered randomly distributed impurity springs to first order in concentration; this does not furnish the finite-separation two-bond threshold or fixed-budget optimization. Mannheim (2005) derived a force-constant impurity Green-function analysis in cubic crystals. Luo (2016) derived one-mass impurity thresholds in finite monatomic chains. Ramakrishnan and Matlack (2024) investigated grounded monoatomic chains with multiple defects but explicitly left strongly interacting proximal defects outside their analytical treatment. The present statement concerns two **bond** stiffenings in an **infinite ungrounded monatomic** chain, their exact second-mode birth, and optimization under a common stiffness budget. The finite-rank method itself is established, not claimed as new.

## Limitations
No claims are made for softened or negative-stiffness bonds, disordered or damped chains, finite experimental boundaries, nonlinear springs, or higher-dimensional networks. Band-edge threshold solutions are not counted as localized eigenvectors. Finite-chain numerical tests are not proofs for infinite chains. The complete texts of Montroll and Potts (1955) and Bacon--Dean--Martin (1962) were not accessible; an unrecognized equivalent historical specialization remains a genuine priority risk. The theorem does not address uncertainty or experimental parameter inference.

## References
1. E. W. Montroll and R. B. Potts, “Effect of Defects on Lattice Vibrations,” *Physical Review* 100 (1955), 525--543. DOI: `10.1103/PhysRev.100.525` (published 1955-10-15).
2. M. D. Bacon, P. Dean and J. L. Martin, “Defect Modes in Two-component Chains,” *Proceedings of the Physical Society* 80 (1962), 174--189. DOI: `10.1088/0370-1328/80/1/321`.
3. H.-C. Poon and A. Bienenstock, “Vibrational Spectrum of a One-Dimensional Chain with Randomly Distributed Impurity Springs,” *Physical Review* 141 (1966), 710. DOI: `10.1103/PhysRev.141.710` (published 1966-01-14).
4. P. D. Mannheim, “Arbitrary Force-Constant Changes in the Crystal Impurity Problem,” arXiv:`cond-mat/0512188` (first posted 2005-12-09).
5. Q. Luo, “Local vibrational mode of impurity in a monatomic linear chain under open and periodic boundary conditions,” arXiv:`1607.06946` (first posted 2016-07-23).
6. V. Ramakrishnan and K. H. Matlack, “Localized Band Gap Resonances in Defect-embedded Monoatomic Chains,” arXiv:`2410.19080` (first posted 2024-10-24).
