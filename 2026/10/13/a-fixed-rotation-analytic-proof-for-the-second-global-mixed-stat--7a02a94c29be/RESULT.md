# A fixed-rotation analytic proof for the second global mixed-state perfect-entangler family

## Finding
For every \\(0\\leq\\chi\\leq\\pi/4\\), define
\\[
U_\\chi=\\exp\\!\\left[-i\\left(\\frac{\\pi}{4}X\\otimes X+\\chi Y\\otimes Y\\right)\\right]
\\]
and let \\(R_y(\\theta)=\\exp(-i\\theta Y/2)\\).  There is a single local rotation, independent of both purity and \\(\\chi\\), that gives a separable inverse image of every two-qubit maximally entangled mixed state (MEMS).  With the MEMS phase fixed to \\(-\\pi/2\\), put
\\[
\\sigma_{\\gamma,\\chi}
=U_\\chi^\\dagger
(R_y(\\pi/2)\\otimes I)\\rho_{\\rm ME}(\\gamma,-\\pi/2)
(R_y(-\\pi/2)\\otimes I)U_\\chi.
\\]
Then \\(\\sigma_{\\gamma,\\chi}\\) is separable for every \\(0\\leq\\gamma\\leq1\\).  On the rank-three branch \\(0\\leq\\gamma\\leq2/3\\),
\\[
\\operatorname{spec}\\!\\left(\\sigma_{\\gamma,\\chi}^{T_B}\\right)
=\\left\\{0,\\frac13,\\frac13-\\frac\\gamma2,\\frac13+\\frac\\gamma2}\\right\\},
\\]
while on the rank-two branch \\(2/3\\leq\\gamma\\leq1\\),
\\[
\\operatorname{spec}\\!\\left(\\sigma_{\\gamma,\\chi}^{T_B}\\right)
=\\left\\{0,0,1-\\gamma,\\gamma}\\right\\}.
\\]
Both spectra are independent of \\(\\chi\\).

Consequently \\(U_c(\\pi/4,\\chi,0)\\) is analytically certified as a global mixed-state perfect entangler throughout the canonical interval \\(0\\leq\\chi\\leq\\pi/4\\): its output from the source above is exactly a local-unitary copy of a MEMS at the same purity.  Guan et al. identified this family only through a numerical local-rotation search.  The rank-two existence statement is not claimed as new: Di and Liu proved in 2007 that every pure-state perfect entangler is also a perfect entangler for rank-two mixed states with fixed spectrum.  The substantive new part here is the exact rank-three certificate, together with the same fixed rotation that unifies both ranks.

## Assumptions and scope
The Pauli matrices are \\(X\\) and \\(Y\\), and the Cartan kernel is taken in the canonical chamber \\(0\\leq\\chi\\leq\\pi/4\\).  The MEMS phase is chosen as \\(-\\pi/2\\); changing that phase by local diagonal unitaries does not change entanglement or purity.

Write
\\[
\\rho_{\\rm ME}(\\gamma,-\\pi/2)=
\\begin{pmatrix}
g(\\gamma)&0&0&i\\gamma/2\\\\
0&1-2g(\\gamma)&0&0\\\\
0&0&0&0\\\\
-i\\gamma/2&0&0&g(\\gamma)
\\end{pmatrix},
\\]
where
\\[
g(\\gamma)=
\\begin{cases}
1/3,&0\\leq\\gamma\\leq2/3,\\\\
\\gamma/2,&2/3\\leq\\gamma\\leq1.
\\end{cases}
\\]
The corresponding purity is
\\[
\\mu=\\frac13+\\frac{\\gamma^2}2
\\quad\\text{for}\\quad0\\leq\\gamma\\leq2/3,
\\]
and
\\[
\\mu=\\gamma^2+(1-\\gamma)^2
\\quad\\text{for}\\quad2/3\\leq\\gamma\\leq1.
\\]
These two ranges join at \\(\\mu=5/9\\) and cover \\(1/3\\leq\\mu\\leq1\\).

The finding concerns this explicit gate family and source construction.  It does not classify all global perfect entanglers, all local rotations that work, or the broader rank-three regions suggested numerically in the source.

## Proof
Because \\(X\\otimes X\\) and \\(Y\\otimes Y\\) commute,
\\[
U_\\chi
=\\frac{I-iX\\otimes X}{\\sqrt2}
\\left(\\cos\\chi\\,I-i\\sin\\chi\\,Y\\otimes Y\\right).
\\]
Set \\(L=R_y(\\pi/2)\\otimes I\\).  By definition,
\\[
U_\\chi\\sigma_{\\gamma,\\chi}U_\\chi^\\dagger
=L\\rho_{\\rm ME}(\\gamma,-\\pi/2)L^\\dagger,
\\]
so the output is a local-unitary copy of the MEMS and has the same purity and entanglement.  It remains only to prove that the source \\(\\sigma_{\\gamma,\\chi}\\) is separable.

Put \\(c=\\cos\\chi\\) and \\(s=\\sin\\chi\\).  Direct multiplication of the four-by-four matrices, followed by partial transposition on the second qubit, gives on the rank-three branch
\\[
\\det\\!\\left(\\lambda I-\\sigma_{\\gamma,\\chi}^{T_B}\\right)
=\\lambda
\\left(\\lambda-\\frac13\\right)
\\left(\\lambda-\\frac13+\\frac\\gamma2\\right)
\\left(\\lambda-\\frac13-\\frac\\gamma2\\right).
\\]
All dependence on \\(c\\) and \\(s\\) cancels using \\(c^2+s^2=1\\).  Thus the four eigenvalues are
\\[
0,\\qquad\\frac13,\\qquad\\frac13-\\frac\\gamma2,\\qquad\\frac13+\\frac\\gamma2,
\\]
which are nonnegative exactly throughout \\(0\\leq\\gamma\\leq2/3\\).

On the rank-two branch the same calculation yields
\\[
\\det\\!\\left(\\lambda I-\\sigma_{\\gamma,\\chi}^{T_B}\\right)
=\\lambda^2(\\lambda-\\gamma)(\\lambda-(1-\\gamma)),
\\]
so the eigenvalues are \\(0,0,\\gamma,1-\\gamma\\), again nonnegative throughout the required interval.

For two qubits, positivity of the partial transpose is equivalent to separability.  Hence every \\(\\sigma_{\\gamma,\\chi}\\) above is separable.  Since the two branches cover the full MEMS purity interval, the gate family is a global perfect entangler in the mixed-state sense used by Guan et al.

## Verification
The bundled `verify.py` reconstructs the Pauli matrices, the Cartan kernel, the fixed local rotation, both MEMS branches, and the partial transpose symbolically.  It computes the characteristic polynomial \\(\\det(\\lambda I-\\sigma^{T_B})\\) exactly and verifies that its difference from the two displayed factorizations is divisible by \\(\\cos^2\\chi+\\sin^2\\chi-1\\).  It also verifies the two purity formulas and the branch endpoint \\(\\mu=5/9\\).

The checker is a replay of exact algebra; the proof does not infer an infinite statement from a finite parameter grid.  The characteristic-polynomial identities, the two-qubit PPT criterion, and unitary preservation of purity are the critical steps.

## Relationship to prior work
Guan et al. analytically proved a different family, \\(U_c(\\pi/8,\\pi/8,\\chi)\\), to be globally perfect at all purities.  For \\(U_c(\\pi/4,\\chi,0)\\), however, they explicitly moved to a numerical inverse-MEMS search over local rotations and reported the family from that scan; their discussion continued to describe this second family as a numerical finding rather than an analytic theorem.

A broader 2007 result of Di and Liu is important for the high-purity branch: for rank-two mixed states with fixed eigenvalues, the condition for a two-qubit unitary to be a perfect entangler is the same as for pure states.  Since \\(U_c(\\pi/4,\\chi,0)\\) satisfies the pure-state perfect-entangler inequalities in the canonical chamber, that theorem already implies existence of a rank-two separable source.  It does not cover rank-three MEMS, which occupy the purity interval \\(1/3\\leq\\mu<5/9\\), and it does not supply the rank-three partial-transpose spectrum above.  Thus the originality claim is deliberately restricted to the exact rank-three certificate and the resulting unified fixed-rotation proof of the numerically reported all-purity family.

Targeted searches for the exact Cartan family, rank-three MEMS inverse images, a fixed \\(R_y(\\pi/2)\\) witness, and the displayed partial-transpose spectrum did not locate a later paper giving the same analytic statement.  That search evidence is not treated as a proof of priority; the explicit gap in the 2013 source and the rank-two-only scope of the closest earlier theorem are the decisive comparisons.

## Limitations
The result does not exhaust the global perfect-entangler locus, nor does it settle the larger rank-three regions seen numerically in the 2013 paper.  It uses the standard two-qubit MEMS curve and the two-qubit PPT-separability equivalence, so it does not generalize automatically to higher local dimensions.  No claim is made that the rank-two existence result is new.  A differently phrased later proof of the rank-three branch could have escaped the targeted literature searches; this is the principal residual originality risk.

## References
1. Z. Guan, H. He, Y.-J. Han, C.-F. Li, F. Galve, and G.-C. Guo, *Entangling power of two-qubit gates on mixed states*, arXiv:1311.5809v1; Phys. Rev. A 89, 012324 (2014), DOI: 10.1103/PhysRevA.89.012324.
2. Y.-M. Di and L. Liu, *Entanglement capacity of two-qubit unitary operator for rank two mixed states*, Sci. China Ser. G 50, 691-697 (2007), DOI: 10.1007/s11433-007-0075-1.
3. W. J. Munro, D. F. V. James, A. G. White, and P. G. Kwiat, *Maximizing the entanglement of two mixed qubits*, Phys. Rev. A 64, 030302(R) (2001), arXiv:quant-ph/0103113.
4. A. Peres, *Separability Criterion for Density Matrices*, Phys. Rev. Lett. 77, 1413-1415 (1996), DOI: 10.1103/PhysRevLett.77.1413.
5. M. Horodecki, P. Horodecki, and R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Phys. Lett. A 223, 1-8 (1996), DOI: 10.1016/S0375-9601(96)00706-2.
