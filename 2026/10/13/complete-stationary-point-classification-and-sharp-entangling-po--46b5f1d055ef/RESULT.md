# Complete stationary-point classification and sharp entangling power of isotropic spin-one two-site gates

## Finding

Let \(P_0,P_1,P_2\) be the mutually orthogonal projectors onto total spin \(0,1,2\) for two spin-one qutrits, of ranks \(1,3,5\). For every pair of relative phases \((\alpha,\beta)\in(\mathbb R/2\pi\mathbb Z)^2\), define
\[
U(\alpha,\beta)=e^{i\alpha}P_0+e^{i\beta}P_1+P_2.
\]
Define the entangling power \(\mathcal E(\alpha,\beta)\) as the mean of \(1-\operatorname{Tr}\rho_A^2\) after applying \(U\) to two independently Haar-distributed pure qutrit inputs. Then this smooth phase-torus function has **exactly eight stationary points**, modulo \(2\pi\) in each coordinate. All of them are nondegenerate, and they fall into four pairs:

| \(\alpha\) | \(\beta\) | \(\mathcal E\) | Type |
| --- | --- | --- | --- |
| \(0\) | \(0,\pi\) | \(0\) | strict global minima |
| \(0\) | \(\pi/2,3\pi/2\) | \(1/4\) | saddles |
| \(\pi\) | \(0,\pi\) | \(20/81\) | saddles |
| \(\pi\) | \(\pi/2,3\pi/2\) | \(131/324\) | strict global maxima |

In particular the sharp all-gate bound within this rotationally invariant two-spin-one family is
\[
0\le\mathcal E(\alpha,\beta)\le\frac{131}{324},
\]
with upper equality **if and only if** \((\alpha,\beta)=(\pi,\pi/2)\) or \((\pi,3\pi/2)\) modulo \(2\pi\). The maximizing gates are \(-P_0\pm iP_1+P_2\). The all-torus classification includes four noncorner stationary points missed by a corners-only analysis.

## Assumptions and scope

The local Hilbert spaces are \(\mathbb C^3\) with the standard spin-one representation of \(SU(2)\). All phase combinations are allowed; the phase in the spin-two sector is fixed to zero, which removes an irrelevant overall phase. There are no locality, positivity, fixed-coupling, or finite-evolution-time restrictions beyond the requirement that the two-site unitary commute with the diagonal \(SU(2)\) action. The entanglement statistic is the **unnormalized linear entropy**, and the input distribution is the product of the two local Haar measures, rather than a measure on entangled input states.

For a concrete normalization, set \(X=\mathbf S_1\cdot\mathbf S_2\), with eigenvalues \(-2,-1,1\), respectively, on total-spin \(0,1,2\) sectors. Writing \(I\) for the identity on \(\mathbb C^3\otimes\mathbb C^3\), the projectors are
\[
P_0=(X+I)(X-I)/3,\qquad
P_1=-(X+2I)(X-I)/2,\qquad
P_2=(X+2I)(X+I)/6.
\]
These polynomial formulas fix every matrix normalization used below.

## Proof

**Exact phase function.** The following full-phase expression is the same as the previously published distinguishable-spin-one scattering formula after substituting its scattering phases by these relative unitary phases:
\[
\begin{aligned}
648\,\mathcal E(\alpha,\beta)={}&156-65\cos\alpha-15\cos(\alpha-2\beta)\\
&-10\cos(2\alpha)-6\cos(2\alpha-2\beta)-60\cos(2\beta).
\end{aligned}
\tag{1}
\]
It also follows independently from the standard two-copy Haar identity
\[
\mathcal E=\frac{10}{16}-\frac{I_R(U)+I_T(U)}{144},
\quad I_R=\operatorname{Tr}[(U^R U^{R\dagger})^2],
\quad I_T=\operatorname{Tr}[(U^{T_A}U^{T_A\dagger})^2],
\]
where the realignment \(U^R_{(ij),(kl)}=U_{(ik),(jl)}\) and partial transpose \(U^{T_A}_{(ik),(jl)}=U_{(jk),(il)}\) use local indices \(i,j,k,l\in\{0,1,2\}\). Substituting the displayed spin-projector polynomials gives (1); the accompanying exact-arithmetic program evaluates both fourth-order traces directly. **Formula (1) itself is prior literature and is not the claimed novelty.**

**Exclusion of every additional stationary point.** Put \(c=\cos\alpha\), and define
\[
A(c)=\frac{166-65c-20c^2}{648},\qquad
B(\alpha)=20+5e^{i\alpha}+2e^{2i\alpha}.
\]
Then (1) reorganizes as
\[
\mathcal E(\alpha,\beta)=A(c)-\frac1{216}\operatorname{Re}\bigl(B(\alpha)e^{-2i\beta}\bigr).
\tag{2}
\]
The triangle inequality gives \(|B(\alpha)|\ge20-5-2=13\), so its phase is always defined. At a stationary point, the \(\beta\) derivative of (2) forces \(B(\alpha)e^{-2i\beta}\) to be real. On either of its two possible signs, the \(\alpha\)-stationarity question is therefore the one-variable stationarity of
\[
F_\pm(c)=A(c)\pm\frac{\sqrt{Q(c)}}{216},\qquad
Q(c)=|B(\alpha)|^2=160c^2+220c+349.
\tag{3}
\]
For \(\sin\alpha\ne0\), the vanishing \(\alpha\) derivative would require \(F_\pm'(c)=0\). Squaring its exact derivative equation yields the necessary polynomial equality
\[
9(320c+220)^2=4(65+40c)^2Q(c).
\]
But the left side minus the right side factors as
\[
-500(4c+5)(8c+19)(64c^2+64c+115).
\tag{4}
\]
For \(-1\le c\le1\), each of the three parenthesized factors is strictly positive: the first two are bounded below by \(1\) and \(11\), and the quadratic equals \(64(c+1/2)^2+99\). Thus (4) is strictly negative, proving **there are no stationary points with \(\sin\alpha\ne0\)**. Squaring introduced no false accepted solutions because the necessary squared condition has none.

It remains to take \(\alpha=0\) or \(\pi\). At these values \(B(\alpha)=27\) or \(17\), respectively, both positive real. The \(\beta\) derivative of (2) then vanishes precisely for \(\beta\in\{0,\pi/2,\pi,3\pi/2\}\) modulo \(2\pi\). At all eight configurations the \(\alpha\) derivative also vanishes directly in (1), since each sine factor has integer-multiple-of-\(\pi\) argument. This proves exhaustion.

**Values, local types, and global sharpness.** Differentiating (1) twice at representatives \(\beta=0,\pi/2\), with the symmetric Hessian ordered as \((\alpha,\beta)\), gives
\[
\begin{array}{c|c|c}
(\alpha,\beta)&\nabla^2\mathcal E&\det\nabla^2\mathcal E\\\hline
(0,0)&\left(\begin{smallmatrix}2/9&-1/12\\-1/12&1/2\end{smallmatrix}\right)&5/48\\
(0,\pi/2)&\left(\begin{smallmatrix}11/108&1/12\\1/12&-1/2\end{smallmatrix}\right)&-25/432\\
(\pi,0)&\left(\begin{smallmatrix}-2/81&1/108\\1/108&17/54\end{smallmatrix}\right)&-275/34992\\
(\pi,\pi/2)&\left(\begin{smallmatrix}-17/324&-1/108\\-1/108&-17/54\end{smallmatrix}\right)&575/34992
\end{array}
\]
The Hessians at each companion with \(\beta\) shifted by \(\pi\) are identical. Their determinant signs and diagonal entries give the announced minima, saddles, and maxima, with all Hessians nonsingular. Substitution in (1) gives the four values in the table above. Finally, a smooth function on the compact two-torus attains global extrema at stationary points. Since we have exhausted these points, their largest and smallest values are globally sharp, with exactly the stated equality cases.

**Physical realization.** For the bilinear–biquadratic Hamiltonian \(H=JX+KX^2\), the evolution \(e^{itH}\), after removing its spin-two phase, has relative phases \(\alpha=3(K-J)t\) and \(\beta=-2Jt\). Thus, for example, \(t=1\), \(J=-\pi/4\), and \(K=\pi/12\) realize the maximizing gate with \((\alpha,\beta)=(\pi,\pi/2)\). No optimization over unrelated arbitrary two-qutrit gates is claimed.

## Verification

The accompanying `verify_spin1.py` (SymPy version specified in `requirements.txt`) directly builds the full \(9\times9\) spin-one matrices and verifies their exact projector ranks and orthogonality. It forms the realigned and partially transposed gate matrices, evaluates both fourth-order trace invariants symbolically, and checks exact equality to (1). Separately, it verifies the elimination factorization (4), the sign-definite quadratic discriminant, all four representative critical values and Hessian matrices, and their \(\pi\)-shifted companions. Execute `python verify_spin1.py` in the package directory; success prints `VERIFY_OK`. The proof of exhaustion is analytic; finite or floating-point sampling is not used as an all-phase certificate.

## Relationship to prior work

Kirchner, Elkamhawy and Hammer (2023 preprint, Table 4) already supply the full trigonometric entangling-power function for distinguishable spin-one scattering; equation (1) is therefore **not new**. Low and McGinnis (September 2026, Sec. IV.3) study the identical three-projector family, prove stationarity of the four corner gates, compute their entangling powers \(0\) and \(20/81\), and discuss the saddle behavior of the latter. The present claim is the **complete exact stationary-set classification**, the four additional noncorner points, the Hessian types, and the resulting sharp global maximum \(131/324\). Low and Goswami (May 2026) study instantaneous and time-averaged entangling power along selected spin-chain dynamics, not a global phase-torus classification. The classical realignment/Haar integration formula is credited as a computational tool, not a new contribution.

## Limitations

The theorem is restricted to two locally three-dimensional spins, rotationally invariant unitary gates, independently Haar-distributed product inputs, and linear entropy. Other entanglement monotones, time-averaged dynamics at fixed couplings, larger spin sectors, higher-site circuits and non-\(SU(2)\)-invariant two-qutrit gates are not covered. The earlier exact phase formula logically contains the function being optimized; the new mathematical step is the explicit exhaustive stationary-point analysis and sharp comparison. The originality assessment has residual risk that this precise optimization may be implicit or independently derived in unindexed literature. No claim of independent external validation is made.

## References

1. T. Kirchner, W. Elkamhawy and H.-W. Hammer, *Entanglement in Few-Nucleon Scattering Events*, arXiv:2312.14484v1 (2023), Table 4, distinguishable spin-one particles. https://arxiv.org/html/2312.14484v1
2. I. Low and N. McGinnis, *Universal Entanglement Dynamics of Unitary Operators*, arXiv:2609.09276v1 (first public 2026-09-08), Sec. II and Sec. IV.3. https://arxiv.org/html/2609.09276v1
3. I. Low and P. Goswami, *Entangling Power: A Probe of Symmetry and Integrability in Quantum Many-Body Systems*, arXiv:2605.20661v2 (2026), Sec. V.2. https://arxiv.org/html/2605.20661v2
4. X.-M. Lu, X. Wang, Y. Yang and J. Chen, *Matrix rearrangement approach for the entangling power with hybrid qudit systems*, arXiv:0803.1032 (2008), realignment/partial-transpose method.
