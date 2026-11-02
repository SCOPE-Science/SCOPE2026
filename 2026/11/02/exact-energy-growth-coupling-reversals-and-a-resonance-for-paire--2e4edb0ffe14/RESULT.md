# Exact energy growth, coupling reversals, and a resonance for paired symplectic Euler

## Finding

For the unit harmonic oscillator \(\dot q=p\), \(\dot p=-q\), let \(D_h(q,p)=(q+hp,p)\) and \(K_h(q,p)=(q,p-hq)\) be exact drift and kick flows. Fix any real \(h>0\). At each elementary step choose either \(A_h=K_hD_h\) or \(B_h=D_hK_h\), with both choices marginally fair. Group consecutive steps into *independent*, identically distributed two-step blocks. The most general within-block joint law with two fair marginals has
\[
\Pr(AA)=\Pr(BB)=r,\qquad
\Pr(AB)=\Pr(BA)=\tfrac12-r,\qquad 0\le r\le\tfrac12.
\]
Here \(AB\) denotes the word consisting of an \(A_h\) step followed by a \(B_h\) step. For any deterministic initial state \(z_0=(q_0,p_0)^\mathsf T\), define \(E(z)=(q^2+p^2)/2\). Then for every integer \(m\ge0\),
\[
\boxed{\mathbb E E(z_{2m})=g_r(h)^m E(z_0)},\qquad
\boxed{g_r(h)=1+2h^6+r h^4(h^4-8h^2+4).}
\]
In particular, the energy-minimizing fair coupling is precisely
\[
\begin{cases}
r=0 & 0<h<\sqrt3-1\quad\text{or}\quad h>\sqrt3+1,\\
r=\tfrac12 & \sqrt3-1<h<\sqrt3+1,\\
\text{every }r\in[0,\tfrac12] & h=\sqrt3-1\quad\text{or}\quad h=\sqrt3+1.
\end{cases}
\]
The minimizer is unique except at the two transition steps. Thus even within the single-step elliptic stability range \(0<h<2\), the optimal correlation reverses sharply at \(h=\sqrt3-1\). The exact optimal multiplier is
\[
\boxed{\min_{0\le r\le1/2}g_r(h)=1+\min\big\{2h^6,\tfrac12 h^4(h^2-2)^2\big\}.}
\]
For every \(h>0\) and every fair coupling, \(g_r(h)>1\), **except** at \(h=\sqrt2\), \(r=1/2\), when both possible block maps are exactly \(-I\) and energy is preserved pathwise at all even steps. This is a statement about physical quadratic energy at block endpoints, not about phase accuracy or numerical trajectory error.

## Assumptions and scope

The oscillator has unit mass, stiffness, and frequency; time is nondimensionalized. The matrices act on exact real arithmetic and the initial state is deterministic. Every block consists of two elementary steps of equal positive length \(h\); the two elementary orderings are required to have exactly uniform \(1/2\)-\(1/2\) marginals. The within-block dependence is arbitrary under those marginals, while blocks are independent and identically distributed and independent of the initial state. The expectation is over block orderings alone; no stochastic forcing or random timestep is present. At \(z_0=0\) the energy identity is trivial. The exponential-growth interpretation applies to \(z_0\ne0\). Both elementary maps are symplectic for all \(h\), and individually elliptic for \(0<h<2\).

## Proof

**1. Exhaustive coupling parameterization.** Write \(p_{ij}\) for the joint probability of orderings \(i,j\in\{A,B\}\) in one block. The two sets of marginal equalities give \(p_{AA}=p_{BB}=r\), \(p_{AB}=p_{BA}=1/2-r\), and \(0\le r\le1/2\). Thus there are no other feasible stationary within-block couplings to optimize over.

**2. Exact matrices and Gram cancellations.** In column coordinates \(z=(q,p)^\mathsf T\),
\[
D_h=\begin{pmatrix}1&h\\0&1\end{pmatrix},\quad
K_h=\begin{pmatrix}1&0\\-h&1\end{pmatrix},\quad
A_h=\begin{pmatrix}1&h\\-h&1-h^2\end{pmatrix},\quad
B_h=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix}.
\]
The second-step product of a word \(AB\) is \(B_hA_h\); since both mixed words have equal probabilities, their sum is insensitive to that notational order. Direct polynomial matrix multiplication, valid for **every real** \(h\), gives
\[
\frac{(A_h^2)^\mathsf T A_h^2+(B_h^2)^\mathsf T B_h^2}{2}
=\left[1+\frac{h^4(h^2-2)^2}{2}\right]I,
\]
\[
\frac{(A_hB_h)^\mathsf T (A_hB_h)+(B_hA_h)^\mathsf T (B_hA_h)}{2}
=(1+2h^6)I.
\]
Consequently the expected two-step Gram matrix equals \(g_r(h)I\), where
\[
\begin{aligned}
g_r(h)
&=2r\left[1+\tfrac12 h^4(h^2-2)^2\right]
 +(1-2r)(1+2h^6)\\
&=1+2h^6+r h^4(h^4-8h^2+4).
\end{aligned}
\]
For any state \(z\) at the beginning of a block, independence of that block gives exactly \(\mathbb E[E(z_{\mathrm{after}})\mid z]=g_r(h)E(z)\). Iterating conditional expectation proves the claimed formula simultaneously for all \(m\ge0\) and all deterministic \(z_0\), without an asymptotic approximation.

**3. Sharp optimization and transitions.** The dependence on \(r\in[0,1/2]\) is affine, with slope \(h^4(h^4-8h^2+4)\). Its sign is determined by
\[
h^4-8h^2+4
=(h^2-(4-2\sqrt3))(h^2-(4+2\sqrt3)).
\]
Since \(h>0\), the two positive switch steps are \(\sqrt3-1\) and \(\sqrt3+1\). A nonzero affine slope has a unique minimizing endpoint; at the zeros every coupling ties. The two endpoint multiplier expressions are \(g_0(h)=1+2h^6\) (oppositely ordered steps) and \(g_{1/2}(h)=1+h^4(h^2-2)^2/2\) (identically ordered steps). This proves the complete phase diagram and minimum formula.

**4. Exact resonance, rigidity, and individual spectral stability.** For \(h>0\), \(g_0(h)>1\), whereas \(g_{1/2}(h)=1\) precisely at \(h=\sqrt2\). A nontrivial convex combination with \(g_0(h)>1\) cannot equal one; hence \((h,r)=(\sqrt2,1/2)\) is the unique zero-heating parameter pair. Both \(A_h\) and \(B_h\) have determinant one and trace \(2-h^2\), so their characteristic polynomial is \(\lambda^2-(2-h^2)\lambda+1\). At \(h=\sqrt2\), Cayley–Hamilton gives \(A_h^2=B_h^2=-I\). With \(r=1/2\), only these two words occur and both advance the state exactly by \(-I\), proving the stronger pathwise conclusion. For \(0<h<2\), the trace lies strictly between \(-2\) and \(2\), so each elementary map has eigenvalues on the unit circle. The nonresonant exponential mean energy growth therefore coexists with individually elliptic, symplectic steps.

## Verification

Run `python3 verify.py` with Python 3 and SymPy installed. The program builds the matrices from the displayed drift/kick definitions, checks both full \(2\times2\) polynomial Gram identities exactly, verifies the scalar multiplier, factorization and resonant \(-I\) identities, and independently enumerates every possible sequence of one, two and three blocks for six exact-rational parameter settings. All computations are symbolic or rational, without stochastic simulation. The reported successful result is `VERIFY_OK: polynomial_identities=11, rational_block_enumerations=18, resonance=2`. The proof above is independent of finite enumeration. At \(h=1/2\), the opposite-pair and same-pair multipliers are exactly \(33/32\) and \(561/512\); at \(h=1\) they are \(3\) and \(3/2\). At \(h=\sqrt2\), the same-pair multiplier is one while the opposite-pair multiplier is \(17\).

## Relationship to prior work

Classical symplectic Euler and adjoint splitting methods, the unit-circle spectral criterion for symplectic \(2\times2\) matrices, and symmetric leapfrog compositions are established mathematics. McLachlan (2021), particularly the complete preprint's Sections II–III, studies optimization and the substantial influence of the *fixed ordering* of Hamiltonian splitting terms, including experiments on random-coefficient linear systems. That distinction does not imply a two-consecutive-step **random coupling** of orderings with exact second-moment energy, two sharp correlation switches, or the pathwise resonant block law. Cohen and Vilmart (2020) derive drift-preserving stochastic splitting for Hamiltonian/Poisson systems under *additive stochastic forcing*, a different source of randomness and a different energy objective. Chen and collaborators (2020) study Hamiltonian schemes under additive noise. The stated claim treats the error mechanism from **switching the deterministic adjoint orderings** and determines the minimizing coupling exactly. No uniqueness or publication priority outside the searched and inspected literature is asserted.

## Limitations

The exact isotropic Gram cancellations rely on this two-dimensional, single-frequency oscillator with equal-length elementary drift and kick flows and fair ordering marginals. They do not automatically extend to coupled frequencies, nonlinear potentials, unequal stage lengths, other symplectic schemes, arbitrary nonstationary block laws, or external stochastic forcing. Growth of expected physical energy does not by itself prove almost-sure growth of any trajectory. The energy-preserving resonance does not eliminate phase error: \(-I\) generally differs from the true rotation over physical time \(2h\). The objective is physical energy at **even elementary steps**, not the worst transient norm, numerical solution error, or error per computational cost. Independent verification of publication priority remains outstanding.

## References

- R. I. McLachlan, *Tuning symplectic integrators is easy and worthwhile*, arXiv:2104.10269v1, first posted April 20, 2021, https://arxiv.org/abs/2104.10269 ; journal version *Communications in Computational Physics* 31 (2022), 987–996, https://doi.org/10.4208/CICP.OA-2021-0154.
- D. Cohen and G. Vilmart, *Drift-preserving numerical integrators for stochastic Poisson systems*, arXiv:2005.13991v1 (2020), https://arxiv.org/abs/2005.13991 ; *International Journal of Computer Mathematics* 99 (2022), 4–20, https://doi.org/10.1080/00207160.2021.1922679.
- C. Chen, D. Cohen, R. D'Ambrosio, and A. Lang, *Drift-preserving numerical integrators for stochastic Hamiltonian systems*, *Advances in Computational Mathematics* 46, 27 (2020), https://doi.org/10.1007/s10444-020-09771-5.
