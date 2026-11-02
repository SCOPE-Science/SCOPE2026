# An explicit full-shift window for every bounded stationary state of the symmetric discrete Nagumo equation

## Finding
For the symmetric cubic discrete Nagumo stationary equation, the entire set of bounded real stationary profiles—not merely a chosen invariant subset—is exactly a three-symbol full shift on a fully explicit positive interval of diffusion strengths. Let
\[
r_* = \frac{3-\sqrt3}{12},\qquad m_* = \frac{\sqrt3}{8},\qquad d_* = \frac{4\sqrt3-3}{416}=0.0094427962266\ldots .
\]
For every \(0\le d<d_*\), the assignment of a profile to its unique nearest root code is a topological conjugacy from spatial translation of the **entire bounded stationary solution space** (with its product topology) to the full shift on \(\{0,\tfrac12,1\}^{\mathbb Z}\). Each code has precisely one realizing stationary profile in its \(r_*\)-neighborhood in sup norm. This is a sufficient, not claimed sharp, threshold.

## Assumptions and scope
A bounded real doubly infinite sequence \(u=(u_j)_{j\in\mathbb Z}\) is stationary if, for every integer \(j\),
\[
d(u_{j-1}-2u_j+u_{j+1})+g(u_j)=0,\qquad g(t)=t(1-t)(t-\tfrac12).
\]
All quantifiers concern this cubic at its symmetric bistable parameter and \(0\le d<d_*\). The shift is in the spatial index, not in physical time. The topology on bounded stationary profiles is pointwise/product convergence, not the sup-norm topology; only the *uniform error bound* uses sup norm.

## Proof
**1. Every bounded stationary profile lies in the unit interval.** Let \(M=\sup_j u_j\). If \(M>1\), choose \(j_k\) such that \(u_{j_k}\to M\). Since neighbors are at most \(M\), the discrete Laplacian is at most \(2(M-u_{j_k})\). The stationary equation gives \(0\le 2d(M-u_{j_k})+g(u_{j_k})\to g(M)<0\), impossible. Likewise, for a negative infimum \(m\), the discrete Laplacian is at least \(2(m-u_{j_k})\), and \(g(m)>0\) contradicts stationarity. Thus \(0\le u_j\le1\) for all \(j\).

**2. Explicit inverse branches.** Let \(S=\{0,\tfrac12,1\}\) and \(J_s=[s-r_*,s+r_*]\) for each \(s\in S\). These intervals are disjoint. The derivative is \(g'(t)=-3t^2+3t-\tfrac12\). Direct elementary minimization on all three intervals yields \(\lvert g'(t)\rvert\ge m_*\) and constant derivative sign on each interval. The images \(g(J_s)\) contain the centered interval \([-r_*m_*,r_*m_*]\), so each restricted map \(g\vert_{J_s}\) has a Lipschitz inverse with constant at most \(1/m_*\).

**3. Uniform contraction for any code.** Fix \(s\in S^{\mathbb Z}\) and let \(B_s=\{v: v_j\in J_{s_j}\text{ for all }j\}\) with its sup norm; it is complete. Define
\[
(T_sv)_j=(g\vert_{J_{s_j}})^{-1}\!\left(-d(v_{j-1}-2v_j+v_{j+1})\right).
\]
For every \(v\in B_s\), its coordinates are in \([-r_*,1+r_*]\), whence \(\lvert v_{j-1}-2v_j+v_{j+1}\rvert\le 2(1+2r_*)\). The exact identity \(2d_*(1+2r_*)=r_*m_*\) proves that \(T_s\) maps \(B_s\) to itself when \(d<d_*\). Moreover,
\[
\|T_sv-T_sw\|_\infty\le \frac{4d}{m_*}\|v-w\|_\infty,
\qquad\frac{4d_*}{m_*}=\frac{4-\sqrt3}{13}<1.
\]
Banach's fixed-point theorem gives one and only one stationary profile \(u(s)\in B_s\). Its root-code distance is at most \(r_*\), and actually strictly smaller for \(d<d_*\).

**4. Exhaustiveness.** Every bounded stationary \(u\) lies in \([0,1]^{\mathbb Z}\) by Step 1; hence \(\lvert g(u_j)\rvert\le 2d\). Outside the union of \(J_0,J_{1/2},J_1\) within \([0,1]\), the magnitude \(\lvert g\rvert\) is at least the smaller of its endpoint magnitudes on the two gaps. Cubic sign and unimodality on either gap guarantee this is at least \(r_*m_*\), by the mean value theorem on the neighboring root intervals. Because \(2d<2d_*(1+2r_*)=r_*m_*\), no coordinate lies in a gap. Consequently \(u\in B_s\) for a unique root code \(s\), and Step 3 forces \(u=u(s)\). This excludes all other bounded stationary states.

**5. Spatial conjugacy.** The inverse code is continuous because the three intervals are separated. For the forward map, the \(k\)-th iterate of \(T_s\) started from the root code depends on only finitely many code coordinates near each selected site; its error to \(u(s)\) is uniformly bounded by \(2r_*(4d/m_*)^k\). Thus \(s\mapsto u(s)\) is continuous in product topology. Spatial translation commutes with \(T_s\), hence with its unique fixed points. This gives the claimed homeomorphism and conjugacy.

## Verification
The exact constants obey \(r_*=(3-\sqrt3)/12\), \(m_*=\sqrt3/8\), \(d_*=(4\sqrt3-3)/416\), \(2d_*(1+2r_*)=r_*m_*\), and \(4d_*/m_*=(4-\sqrt3)/13<1\). The accompanying `verify_nagumo.py` checks the algebraic identities and inverse-branch inequalities, plus periodic sample fixed points near the cutoff. These finite checks are supplementary; the proof above covers all bi-infinite codes and all bounded stationary sequences.

## Relationship to prior work
Hesoun, Stehlík and Volek establish a three-symbol horseshoe *subsystem* and a stability dichotomy for general bistable lattice equations at unspecified sufficiently small diffusion. Their theorem is the motivating qualitative precursor, not replaced here. Hupkes, Morelli, Stehlík and Švígler classify spatially periodic equilibria, while Švígler develops existence-region counts. This theorem instead produces one explicit parameter window and exhausts every bounded (including aperiodic) stationary solution for the symmetric cubic. The classic Chow–Shen spatial chaos treatment is a historical-priority risk; its abstract was available, not its full text.

## Limitations
The cutoff is a conservative analytic sufficient bound, not an optimal threshold for disappearance of spatial chaos, fronts or pinning. Only the cubic with middle root exactly \(1/2\) is treated. The coding is of stationary configurations under spatial shifts, **not** temporal solution trajectories. No independent audit or priority certification has been performed.

## References
- J. Hesoun, P. Stehlík, J. Volek, *Characterization of spatial topological chaos for bistable lattice equation*, arXiv:2609.25868 (initial public preprint 2026-09-22; revised 2026-10-16).
- H. J. Hupkes, L. Morelli, P. Stehlík, V. Švígler, *Counting and ordering periodic stationary solutions of lattice Nagumo equations*, arXiv:1905.06107 (2019).
- V. Švígler, *Periodic stationary solutions of the Nagumo lattice differential equation: existence regions and their number*, arXiv:2003.14070 (2020).
- S.-N. Chow, W. Shen, *Dynamics in a discrete Nagumo equation: Spatial topological chaos*, SIAM J. Appl. Math. 55 (1995), 1764–1781, doi:10.1137/S0036139994261757.
