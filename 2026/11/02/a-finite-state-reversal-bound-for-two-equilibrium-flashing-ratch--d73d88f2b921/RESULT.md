# A finite-state reversal bound for two-equilibrium flashing ratchets

## Finding

Let a particle move on a connected finite graph with \(n\ge3\) sites. In either of two environmental phases its continuous-time jump process satisfies detailed balance, and the phases switch at a common site-independent Poisson rate \(r>0\). For any fixed oriented spatial edge \(e\), the **total stationary particle current** has the form

\[
J_e(r)=\frac{r P_e(r)}{D(r)},\qquad \deg P_e\le n-2,\qquad D(r)>0\quad(r>0).
\]

Here \(D\) is a real polynomial of degree exactly \(n-1\) with \(D(0)=1\), and \(P_e\) may vanish identically. Consequently, unless the current is identically zero, changing only the environment-switching rate causes **at most \(n-2\) positive-rate current zeros, counted with multiplicity**, and hence at most \(n-2\) direction reversals. This is a universal finite-size ceiling, not an assumption about rate-law shapes or a sampling result.

For a triangle, there can be at most one current reversal. That bound is attained even when one phase is spatially uniform: give the first phase unit weights and unit bond conductances, and give the second phase site weights \((1,3,6)\) and oriented cyclic bond conductances \((5,1,2)\). The current across the oriented edge \(0\to1\) is exactly

\[
J(r)=\frac{3r(8r-9)}{2(845r^2+2559r+1530)}.
\]

It is negative for \(0<r<9/8\), zero at \(r=9/8\), and positive for \(r>9/8\), although **each frozen phase separately has exactly zero stationary spatial current**. Thus the three-site ceiling is sharp.

## Assumptions and scope

Use the column-generator convention. For \(a\in\{0,1\}\), let \(Q_a\) be an irreducible continuous-time Markov generator on the same \(n\)-element vertex set \(V\), with rates \(q^{(a)}_{ji}>0\) along the chosen connected undirected edge set, and zero rates on absent edges. Assume its unique normalized stationary law \(\pi_a\) obeys detailed balance:

\[
q^{(a)}_{ji}(\pi_a)_i=q^{(a)}_{ij}(\pi_a)_j
\]

for all unordered graph edges. Let the phase switch \(a\leftrightarrow1-a\) occur at rate \(r>0\), independently of spatial site and direction, without moving the particle. The \(2n\)-state chain has a unique stationary vector \((p_0,p_1)\), with \(\mathbf1^T p_0=\mathbf1^T p_1=1/2\). For \(e=(i,j)\) define

\[
j_e^{(a)}(x)=q^{(a)}_{ji}x_i-q^{(a)}_{ij}x_j,
\qquad J_e(r)=j_e^{(0)}(p_0)+j_e^{(1)}(p_1).
\]

No constraint is imposed on the relative barrier conductances in the two phases. In particular, the example alters both site weights and barriers. The theorem is about stationary mean spatial currents, not trajectory-level fluctuations, deterministic switching or spatially dependent switching rates.

## Proof

**Step 1 (remove the phase equilibrium directions).** Let \(S=\{x\in\mathbb R^n:\mathbf1^T x=0\}\), of dimension \(m=n-1\), and use \(Q_a\) also for its invertible restriction to \(S\). Invertibility follows from irreducibility. Put

\[
p_a=\tfrac12(\pi_a+u_a),\quad u_a\in S,\quad
\delta=\pi_1-\pi_0\in S.
\]

The two stationary balance equations read

\[
Q_0u_0+r(\delta+u_1-u_0)=0,
\qquad Q_1u_1+r(-\delta+u_0-u_1)=0.
\]

Their sum gives \(Q_0u_0=-Q_1u_1=:z\in S\); hence \(u_0=Q_0^{-1}z\) and \(u_1=-Q_1^{-1}z\). Substitution gives the finite-dimensional resolvent equation

\[
(I_S+rH)z=-r\delta,\qquad H=-Q_0^{-1}-Q_1^{-1}.
\]

**Step 2 (exact edge-current resolvent).** Detailed balance implies \(j_e^{(a)}(\pi_a)=0\). Define the linear functional on \(S\)

\[
L_e(z)=j_e^{(0)}(Q_0^{-1}z)-j_e^{(1)}(Q_1^{-1}z).
\]

Therefore

\[
J_e(r)=-\frac r2 L_e\bigl((I_S+rH)^{-1}\delta\bigr).
\]

This identity is exact for every positive switching rate, with no adiabatic or fast-switching approximation.

**Step 3 (denominator never vanishes).** The factorization

\[
-H=Q_0^{-1}(Q_0+Q_1)Q_1^{-1}
\]

shows \(H\) is invertible: \(Q_0+Q_1\) is an irreducible generator, and each restriction to \(S\) is invertible. Consequently \(D(r)=\det_S(I_S+rH)\) has degree exactly \(m\) and constant coefficient one. Were \(D(r)=0\) for some \(r>0\), a nonzero solution of the homogeneous equation would supply a zero-total-mass stationary vector of the full irreducible \(2n\)-state chain, contradicting uniqueness of its stationary direction. Since \(D(0)=1\) and no positive zero exists, \(D(r)>0\) for all positive \(r\).

**Step 4 (polynomial degree and reversal count).** By the adjugate identity,

\[
J_e(r)=-\frac r{2D(r)}L_e\bigl(\operatorname{adj}(I_S+rH)\delta\bigr).
\]

Every entry of the adjugate of an \(m\times m\) affine matrix has degree at most \(m-1=n-2\). Thus its scalar contraction is \(P_e(r)\) of that degree or less, proving the statement. A nonzero real polynomial of degree at most \(n-2\) cannot have more than \(n-2\) distinct positive roots, or more than that number counted with multiplicity. The positive denominator cannot add sign changes. If \(P_e\equiv0\), the current vanishes for every rate and no isolated reversal can be assigned.

**Step 5 (triangle and sharp realization).** For \(n=3\), \(P_e(r)=ar+b\) and

\[
D(r)=1+r\operatorname{tr}H+r^2\det H.
\]

Every frozen phase is reversible, so \(\operatorname{tr}H>0\); also \(\det H>0\) by the factorization in Step 3 and positivity of the nonzero eigenvalue products of three-state irreducible generators. The sign of \(J_e\) is that of \(ar+b\). If the nonzero slow- and fast-switching signs differ, the unique reversal occurs at \(r=-b/a>0\); otherwise no reversal occurs at a strictly positive rate.

For the explicit example, write the jump rate along a bond \(\{i,i+1\}\) in phase \(a\) as \(c^{(a)}_i/w^{(a)}_i\) from site \(i\) and \(c^{(a)}_i/w^{(a)}_{i+1}\) in reverse, with cyclic indices modulo three. The respective data are

\[
(w^{(0)},c^{(0)})=((1,1,1),(1,1,1)),\quad
(w^{(1)},c^{(1)})=((1,3,6),(5,1,2)).
\]

Both phases satisfy detailed balance with \(\pi_a\) proportional to \(w^{(a)}\). Exact elimination gives

\[
\operatorname{tr}H=\frac{853}{510},\quad
\det H=\frac{169}{306},\quad
b=-\frac3{340},\quad a=\frac2{255}.
\]

Substitution yields the displayed rational current and the unique sign change at \(r=9/8\). This establishes attainability of the three-site ceiling.

## Verification

`checker.py` uses only Python's standard-library `fractions.Fraction` to solve the full six-state stationary balance equations, evaluate the reduced resolvent independently, and reconstruct all current coefficients. It passed 759 exact three-site comparisons (including 39 at the sharp example) and 275 exact four- and five-site checks. Those larger checks compare the full stationary system with the \(n-1\)-dimensional resolvent and verify finite-difference consequences of the polynomial-degree bound. Run `python checker.py`. The analytical argument, not these finite tests, proves the result for every finite \(n\).

## Relationship to prior work

Lee, Allison, Abbott and Stanley (first preprint 2002) analyze an exactly solvable **discrete-time, three-state** ratchet, including a noise-dependent current and zero-current surface. Their solved object does not have two independently reversible continuous-time phase generators coupled by an adjustable Poisson switching rate. Jarzynski and Mazonka (1999) solve a specific six-state thermal ratchet; their established model motivates concern about possible coverage by other six-state constructions, but no arbitrary-generator reversal-count theorem was verified from the available material. Rahav, Horowitz and Jarzynski (2008) prove a no-pumping theorem under fixed well depths or fixed barriers in thermally activated stochastic pumps; the sharp example here changes both, so their obstruction does not apply. Levien and Bressloff (2015) analyze a two-state flashing diffusion and its quasi-steady-state reduction, rather than an exact all-rate finite-state polynomial bound.

This statement is a proposed additional finite-state algebraic constraint, not a claim to invent flashing ratchets, detailed-balance pumping or exact finite Markov solutions. Its historical priority is provisional, especially against general finite-network response literature and early six-state motor models.

## Limitations

The bound applies only when there are exactly two reversible, irreducible spatial phases, a common finite vertex set, site-preserving switching, and a single constant symmetric rate \(r\). It does not claim sharpness of the \(n-2\) bound for every \(n>3\), nor classify all admissible numerator polynomials. Extra environmental states, spatially dependent switching, nonreversible frozen phases, infinite spatial lattices, deterministic modulation, or rate parameters that alter the frozen generators are outside scope. The result concerns stationary mean currents; finite-time reversal statistics and entropy production are not classified. Independent verification and comprehensive historical priority assessment remain open.

## References

1. C. Jarzynski and O. Mazonka, *Feynman's ratchet and pawl: An exactly solvable model*, arXiv:cond-mat/9902056 (first posted 3 February 1999); Physical Review E 59, 6448 (1999). https://arxiv.org/abs/cond-mat/9902056
2. Y. Lee, A. Allison, D. Abbott and H. E. Stanley, *Minimal Brownian Ratchet: An Exactly Solvable Model*, arXiv:cond-mat/0205302 (first posted 15 May 2002); Physical Review Letters 91, 220601 (2003). https://arxiv.org/abs/cond-mat/0205302
3. S. Rahav, J. Horowitz and C. Jarzynski, *Directed Flow in Nonadiabatic Stochastic Pumps*, arXiv:0808.0015 (2008); Physical Review Letters 101, 140602. https://arxiv.org/abs/0808.0015
4. E. Levien and P. C. Bressloff, *Quasi-steady-state analysis of coupled flashing ratchets*, Physical Review E 92, 042129 (2015). https://doi.org/10.1103/PhysRevE.92.042129
5. V. Y. Chernyak and N. A. Sinitsyn, *Pumping Restriction Theorem for Stochastic Networks*, arXiv:0808.0205 (2008). https://arxiv.org/abs/0808.0205
