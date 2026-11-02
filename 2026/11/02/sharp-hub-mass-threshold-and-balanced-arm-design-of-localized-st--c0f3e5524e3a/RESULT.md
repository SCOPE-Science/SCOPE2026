# Sharp hub-mass threshold and balanced-arm design of localized star-chain vibrations

## Finding

Consider a freely suspended harmonic spring network consisting of a hub and \(q\geq3\) outward, vertex-disjoint paths. Path \(i\) has \(L_i\geq1\) moving masses beyond the hub. Every spring has stiffness \(k>0\); every arm mass is \(m>0\); the hub has mass \(\mu m\), where \(\mu>0\). Write \(\lambda=m\omega^2/k\), with \(\omega\) an angular frequency. The passband of the infinite uniform one-dimensional arm is \(0\leq\lambda\leq4\).

**Sharp localized-mode threshold.** The finite network has **at most one** eigenfrequency with \(\lambda\geq4\). Defining
\[
\mu_{\mathrm c}(L_1,\ldots,L_q)=\sum_{i=1}^q\frac{L_i}{2L_i+1},
\]
it has exactly one eigenvalue above \(4\) if and only if \(\mu<\mu_{\mathrm c}\); it has an eigenvalue exactly at \(4\) if and only if \(\mu=\mu_{\mathrm c}\); and all eigenvalues lie below \(4\) when \(\mu>\mu_{\mathrm c}\). In the above-band case the exceptional mode is simple and decays in magnitude from the hub toward every leaf.

**Sharp finite-size allocation theorem.** Fix \(q\geq3\) and a total of \(S=\sum_i L_i\geq q\) arm masses. Put \(a=\lfloor S/q\rfloor\), \(r=S-qa\), and \(H=S-q+1\). Among all positive-integer arm-length allocations, the maximum and minimum critical hub masses are
\[
\boxed{\mu_{\max}=(q-r)\frac{a}{2a+1}+r\frac{a+1}{2a+3}},\qquad
\boxed{\mu_{\min}=\frac{q-1}{3}+\frac{H}{2H+1}}.
\]
The maximizing allocations are exactly the balanced profiles with \(q-r\) arms of length \(a\) and \(r\) of length \(a+1\), up to permutation. The minimizing allocations have lengths \((H,1,\ldots,1)\), up to permutation. When all admissible allocations coincide, both descriptions represent the same profile. Thus balancing paths allows an above-band junction mode for the greatest hub mass at fixed total network size.

Moreover, for any \(\mu>0\), the capped spectral top \(\max\{4,\lambda_{\max}\}\) is maximized by the balanced profile and minimized by \((H,1,\ldots,1)\). The maximizing length multiset is unique if its capped top exceeds \(4\); the minimizing length multiset is unique if its capped top exceeds \(4\). At a capped value equal to \(4\), several allocations may tie because they all lack an above-band mode.

For example, with \(q=3\), \(S=9\), and \(\mu=6/5\), the balanced network \((3,3,3)\) supports the above-band mode because \(6/5<9/7\), whereas \((7,1,1)\) does not because \(6/5>17/15\). This is an exact geometry-driven on/off transition at unchanged hub mass, spring budget and number of arm masses.

**Infinite-arm limit.** Keeping \(q\) and \(\mu<q/2\) fixed and increasing every arm length without bound, the eventually present exceptional eigenvalue increases toward
\[
\boxed{\lambda_\infty=\frac{q^2}{\mu(q-\mu)}}.
\]
No finite-arm above-band mode is possible for \(\mu\geq q/2\).

## Assumptions and scope

The network is a tree with exactly one central vertex of degree \(q\) and free (force-free) terminal masses; there are no fixed ends, onsite restoring potentials, bending terms, viscous losses, nonlinearities or nonuniform spring constants. Positive integer \(L_i\) counts moving masses on arm \(i\), excluding the central mass. The unperturbed arm dispersion is \(\lambda=2-2\cos\theta\), so the reference threshold \(4\) is not the finite network's intrinsic maximum: a junction mode may lie above it. The theorem addresses the generalized eigenproblem \(Kx=\lambda Mx\), where \(K\) is the combinatorial Laplacian and \(M\) is diagonal with center entry \(\mu\) and all arm entries \(1\).

## Proof

**1. At most one above-band eigenvalue.** Removing the hub row and column from \(K-\lambda M\) leaves the direct sum of arm matrices \(B_{L_i}-\lambda I\). Here \(B_L\) is the path tridiagonal matrix with diagonal entries \(2\) except for the free leaf's final entry \(1\), and off-diagonals \(-1\); for \(L=1\) it is \([1]\). For every real vector \(y\), the exact positive factorization is
\[
y^\mathsf{T}(4I-B_L)y=\sum_{j=1}^{L-1}(y_j+y_{j+1})^2+y_1^2+2y_L^2.
\]
Thus the spectrum of \(B_L\) lies strictly below \(4\). Thus each arm block is negative definite whenever \(\lambda\geq4\). The inertia of the full matrix can differ from the arm-block inertia by at most one, proving that at most one generalized eigenvalue lies in \([4,\infty)\), counting multiplicity. The same block structure also shows that such an eigenvalue, when it exists, is simple.

**2. Exact arm transfer function.** For \(\lambda>4\), set
\[
\rho(\lambda)=\frac{\lambda-2-\sqrt{\lambda(\lambda-4)}}2\in(0,1),\qquad \lambda=2+\rho+\rho^{-1}.
\]
Take hub displacement \(x_0\neq0\). Solving the interior arm recurrence and free-leaf equation yields, for \(1\leq j\leq L_i\),
\[
\frac{x_{i,j}}{x_0}=(-1)^j\,
\frac{\rho^j-\rho^{2L_i+1-j}}{1-\rho^{2L_i+1}}.
\]
In particular \(x_{i,1}/x_0=-h_{L_i}(\lambda)\), where
\[
h_L(\lambda)=\frac{\rho-\rho^{2L}}{1-\rho^{2L+1}}.
\]
The ratio of successive absolute arm displacements is strictly less than \(\rho\): subtracting the inward-growing reflected term reduces each outward step. Hence the high-frequency mode is junction-localized. At \(\lambda=4\), the repeated-root recurrence gives the continuous limit
\[
\frac{x_{i,j}}{x_0}=(-1)^j\left(1-\frac{2j}{2L_i+1}\right),\qquad
h_L(4)=\frac{2L-1}{2L+1}.
\]

**3. Crossing criterion and uniqueness.** The hub equation is \(q x_0-\sum_i x_{i,1}=\mu\lambda x_0\). Therefore its Schur-complement scalar equation is
\[
F(\lambda)=q+\sum_i h_{L_i}(\lambda)-\mu\lambda=0,\qquad\lambda\geq4.
\]
Since \(h_L(\lambda)=[(\lambda I-B_L)^{-1}]_{11}\), its derivative is strictly negative: \(h_L'(\lambda)=-[(\lambda I-B_L)^{-2}]_{11}<0\). Hence \(F\) decreases strictly and tends to \(-\infty\). At the edge,
\[
F(4)=q+\sum_i\frac{2L_i-1}{2L_i+1}-4\mu
=4\left(\sum_i\frac{L_i}{2L_i+1}-\mu\right).
\]
The intermediate value theorem gives exactly one root in \((4,\infty)\) when \(\mu<\mu_{\mathrm c}\). If equality holds, \(4\) itself is the unique edge root; if the sign is negative, no eigenvalue can reach \(4\). The negative definiteness in step 1 excludes any other above-band mode.

**4. Optimal length allocation, including frequency ordering.** At the band edge the function \(f(L)=L/(2L+1)\) has strictly decreasing positive forward differences
\[
f(L+1)-f(L)=\frac1{(2L+1)(2L+3)}.
\]
Transferring one arm mass from a longer arm to a shorter arm therefore increases the sum of \(f(L_i)\), strictly whenever the original lengths differ by at least two. Repeating this operation produces precisely the balanced allocations. Reversing it until all but one arm have length one gives the unique extreme allocation. This proves both formulas and equality classifications.

For the stronger frequency statement, fix any \(\lambda>4\) and write \(\rho=\rho(\lambda)\). Direct subtraction gives
\[
h_{L+1}(\lambda)-h_L(\lambda)
=\frac{\rho^{2L}(1-\rho^2)^2}{(1-\rho^{2L+1})(1-\rho^{2L+3})}>0.
\]
The ratio of the next increment to this increment equals
\[
\rho^2\frac{1-\rho^{2L+1}}{1-\rho^{2L+5}}<1.
\]
Consequently \(h_L(\lambda)\) is strictly increasing and strictly discretely concave in \(L\). Every balancing step raises \(F(\lambda)\) for all \(\lambda>4\), and every concentration step lowers it. Because every such \(F\) is strictly decreasing, its root above the edge (when present) is ordered the same way. Assign value \(4\) to cases lacking an above-band root to obtain the capped-spectral-top statement. Strictness follows whenever the compared root lies above the edge and lengths differ beyond permutation.

**5. Long-arm limit.** As all \(L_i\to\infty\), \(h_{L_i}(\lambda)\to\rho(\lambda)\) for \(\lambda>4\), while \(\mu_{\mathrm c}\to q/2\). For \(\mu<q/2\), the limiting junction equation is \(q(1+\rho)=\mu(2+\rho+\rho^{-1})\), equivalently \(\rho=\mu/(q-\mu)\in(0,1)\). Substitution into the dispersion relation gives \(\lambda_\infty=q^2/[\mu(q-\mu)]\). Strict monotonicity of the finite-root equations and convergence of the transfer functions give convergence from below. If \(\mu\geq q/2\), each finite cutoff is strictly smaller than \(q/2\), excluding an above-band eigenvalue.

## Verification

The accompanying standalone \`verify.py\` constructs each finite graph's stiffness and mass matrices directly and solves generalized symmetric eigenproblems, rather than reusing the scalar transfer equation to calculate eigenvalues. It compares the exact rational edge threshold against spectral mode counts, directly verifies the root equation, enumerates integer partitions at fixed arm budgets, compares largest eigenvalues against balanced and extreme profiles, and tests increasing-arm convergence toward the infinite-arm formula. Run with \`python3 verify.py\`; dependencies are Python, NumPy and SciPy. The supplied run reports 218 edge checks, 1308 above-band counting comparisons, 254 balance checks, 616 scalar-root checks and 24 infinite-arm checks. These finite checks are diagnostics; the universal result is proved analytically above.

## Relationship to prior work

Nakatsukasa, Saito and Woei (arXiv:1112.4526, first submitted 19 December 2011), in particular Section 3 and Corollary 3.1, already establish the \(4\)-edge localization transition and uniqueness for *unweighted* starlike graph Laplacians. Their theorem includes the case \(\mu=1\) here and is explicitly treated as prior knowledge. Ilić (arXiv:1104.4280, first submitted 21 April 2011), Section 2, proves branch-majorization ordering of *all Laplacian polynomial coefficients* for unweighted starlike trees; that does not give the present hub-mass critical threshold or the generalized-eigenvalue above-band frequency ordering. Iguchi and Yamada (Physical Review E 71, 037102, 2005) analyze masses and springs on scale-free graphs; only their abstract was available for inspection, and priority for any more specialized finite-star calculation there remains uncertain. The assessed additions are the exact variable hub-mass threshold, complete fixed-site design interval and above-band frequency ordering, plus its explicit infinite-arm limit, rather than rediscovery of generic starlike localization.

## Limitations

The infinite-arm limit is taken with \(q\) fixed. Above-band means relative to the identical-arm bulk dispersion, not an infinite-frequency instability. The balanced optimum concerns mass placement among finitely many equal-mass arm sites, *not* continuous branch lengths, a fixed physical circumference, nonuniform spring constants, or optimizing actual damping. The theorem does not imply that every mode is spatially localized; it singles out at most one above-band junction mode. Although targeted literature comparisons did not identify a direct earlier weighted-hub threshold-and-allocation theorem, exhaustive historical priority is not certified. A network-specific analysis of the 2005 paper's full text remains inaccessible; it is not asserted to omit the present formula.

## References

1. A. Ilić, “On the ordering of trees by the Laplacian coefficients,” arXiv:1104.4280 (first submitted 21 April 2011), https://arxiv.org/abs/1104.4280. Full text, especially Section 2.
2. Y. Nakatsukasa, N. Saito and E. Woei, “Mysteries around the graph Laplacian eigenvalue 4,” arXiv:1112.4526 (first submitted 19 December 2011), https://arxiv.org/html/1112.4526v2. Full text, especially Sections 2–4.
3. K. Iguchi and H. Yamada, “Vibrational modes and spectrum of oscillators on a scale-free network,” Physical Review E 71, 037102 (2005), https://doi.org/10.1103/PhysRevE.71.037102. Abstract inspected; full text not inspected.
