# Three symbols are necessary and sufficient for irrational zero-temperature selection between two fixed ground states

## Finding
Consider a one-step potential on a mixing three-symbol full shift with two fixed ground configurations. The unique positive-temperature equilibrium state selects the explicit **irrational** convex combination
\[
\mu_\infty=\frac{5+\sqrt5}{10}\delta_{A^\mathbb Z}+\frac{5-\sqrt5}{10}\delta_{B^\mathbb Z}.
\]
This is impossible in the corresponding two-symbol, nearest-neighbor setting: when its only ergodic ground states are the two constant configurations, both have stationary equilibrium mass exactly \(1/2\) at **every** positive inverse temperature. Hence three is the sharp minimal alphabet size for an unequal two-fixed-point ground-state selection within mixing one-step finite-type dynamics with a finite nearest-neighbor potential.

The three-state example also has a quantitative low-temperature dynamical law. Writing \(\varepsilon=e^{-t}\), its pressure is \(\varphi\varepsilon+O(\varepsilon^2)\), where \(\varphi=(1+\sqrt5)/2\). Its equilibrium Markov chain, observed at times \(\lfloor s/\varepsilon\rfloor\) after identifying the auxiliary symbol \(C\) with \(A\), converges in finite-dimensional distributions to the two-state continuous-time chain with rates \(A\to B:1/\varphi\) and \(B\to A:\varphi\). The slow nontrivial transition eigenvalue is \(1-\sqrt5\varepsilon+O(\varepsilon^2)\).

## Assumptions and scope
On the bilateral full shift \(\{A,B,C\}^{\mathbb Z}\), define the locally constant potential \(f(x)=f(x_0,x_1)\) through the following cost table, with row=current and column=next symbol:
\[
\begin{array}{c|ccc}
 & A&B&C\\\hline
 A&0&1&1\\
 B&1&0&3\\
 C&0&3&3
\end{array}
\]
Specifically \(f(i,j)\) is minus the displayed cost. At inverse temperature \(t>0\), put \(\varepsilon=e^{-t}\) and let \(\mu_t\) be the unique equilibrium state of \(tf\). The positive transfer matrix is
\[
M_\varepsilon=\begin{pmatrix}1&\varepsilon&\varepsilon\\ \varepsilon&1&\varepsilon^3\\1&\varepsilon^3&\varepsilon^3\end{pmatrix}.
\]
We use the shift-invariant Parry–Perron Markov probability for this matrix, with its stationary one-site distribution \(\pi_\varepsilon\). Ground state means a shift-invariant probability maximizing \(\int f\). Limits are as \(t\to\infty\) or, equivalently, \(\varepsilon\downarrow0\). Two-symbol sharpness covers all mixing two-state edge shifts with a finite nearest-neighbor potential whose only ergodic maximizing probabilities are the two constant-orbit Dirac measures; it does not assert an alphabet bound for arbitrary longer-range potentials or ground configurations.

## Proof
**1. Ground states and uniqueness at positive temperature.** All costs are nonnegative. The zero-cost transitions are \(A\to A\), \(B\to B\), and \(C\to A\). The only bi-infinite paths using no positive-cost transition are the two constant paths \(A^\mathbb Z\) and \(B^\mathbb Z\): there is no zero-cost incoming transition into \(C\), and no zero-cost bridge between the other two states. For any invariant probability, an integral of the nonpositive potential is zero precisely when its positive-cost edge frequency is zero. Thus the ground-state simplex is exactly the segment joining these two Dirac measures. The matrix \(M_\varepsilon\) is strictly positive whenever \(\varepsilon>0\). Perron–Frobenius and the standard finite-state variational principle give a unique equilibrium Markov probability \(\mu_t\) for each \(t>0\).

**2. Characteristic and Perron asymptotics.** Let \(\lambda_1(\varepsilon)\) be its Perron root. Substitution \(\lambda=1+\varepsilon z\) in the characteristic polynomial gives the **exact** equation
\[
0=z^2-z-1+\varepsilon(z^3-z)-\varepsilon^2-\varepsilon^3z^2-\varepsilon^5z.
\]
At \(\varepsilon=0\), the two simple roots are \(\varphi\) and \(-\varphi^{-1}\). Implicit-function theory gives the two eigenvalues near one,
\[
\lambda_1=1+\varphi\varepsilon+O(\varepsilon^2),\qquad
\lambda_2=1-\varphi^{-1}\varepsilon+O(\varepsilon^2).
\]
The remaining eigenvalue is \(O(\varepsilon)\) by the trace \(2+\varepsilon^3\). Positivity identifies \(\lambda_1\) as the Perron root. Accordingly,
\[
P(tf)=\log\lambda_1=\varphi\varepsilon+O(\varepsilon^2),\quad
\frac{\lambda_2}{\lambda_1}=1-\sqrt5\varepsilon+O(\varepsilon^2).
\]
Here \(\varphi+\varphi^{-1}=\sqrt5\).

**3. Selected measure.** Normalize positive right and left Perron vectors by \(r_A=\ell_A=1\). Their eigenvector equations imply
\[
\begin{aligned}
(\lambda_1-1)r_B&=\varepsilon+\varepsilon^3r_C,&
(\lambda_1-\varepsilon^3)r_C&=1+\varepsilon^3r_B,\\
(\lambda_1-1)\ell_B&=\varepsilon+\varepsilon^3\ell_C,&
(\lambda_1-\varepsilon^3)\ell_C&=\varepsilon+\varepsilon^3\ell_B.
\end{aligned}
\]
Therefore \(r_B,\ell_B\to\varphi^{-1}\), \(r_C\to1\), and \(\ell_C=\varepsilon+O(\varepsilon^2)\). The Parry stationary weights are \(\pi_i=\ell_ir_i/\sum_j\ell_jr_j\). Hence
\[
(\pi_A,\pi_B,\pi_C)=
\left(\frac{\varphi^2}{1+\varphi^2},\frac1{1+\varphi^2},0\right)+O(\varepsilon).
\]
The weights equal \((5+\sqrt5)/10\) and \((5-\sqrt5)/10\). Since the probability of \(C\), the nonconstant edges, and every nonconstant fixed-length word tends to zero (use the transition estimates below), the full shift-invariant measures converge weakly to the displayed mixture. In particular, the selected weights are irrational.

**4. Metastable time scale.** The one-step equilibrium Markov kernel is
\[
K_\varepsilon(i,j)=\frac{M_\varepsilon(i,j)r_j}{\lambda_1r_i}.
\]
The eigenvector asymptotics imply
\[
K_\varepsilon(A,B)=\varphi^{-1}\varepsilon+O(\varepsilon^2),\qquad
K_\varepsilon(B,A)=\varphi\varepsilon+O(\varepsilon^2),
\]
\[
K_\varepsilon(A,C)=\varepsilon+O(\varepsilon^2),\quad
K_\varepsilon(C,A)=1-O(\varepsilon^3),\quad
K_\varepsilon(B,C)=O(\varepsilon^3),\quad
K_\varepsilon(C,B)=O(\varepsilon^3).
\]
Project \(C\) to \(A\). Over \(O(\varepsilon^{-1})\) steps, projected changes from \(A\) to \(B\) occur at asymptotic rate \(1/\varphi\) and changes from \(B\) to \(A\) at rate \(\varphi\); visits to \(C\) last one step with probability tending to one and produce no projected change. More formally, the \(C\)-sojourn lengths are geometrically bounded and the number of \(C\) entrances before \(s/\varepsilon\) steps is tight; after deleting these visits the two-state transition probabilities have the displayed \(\varepsilon\)-expansions. Geometric waiting times, rescaled by \(\varepsilon\), therefore converge jointly to independent exponential holding times, proving finite-dimensional convergence to the continuous-time chain with generator
\[
Q=\begin{pmatrix}-\varphi^{-1}&\varphi^{-1}\\ \varphi&-\varphi\end{pmatrix}.
\]
The same conclusion follows by the two slow eigenvalues above and the third transition eigenvalue \(O(\varepsilon)\). For stationary initial states, the limiting chain is stationary with the same irrational weights.

**5. Sharp binary obstruction.** A mixing edge shift on two symbols containing both fixed points permits both cross-transitions, hence it is the full two-shift. Let \(g\) be any finite nearest-neighbor potential with these fixed points as its only ergodic maximizers. The equality of their averages forces \(g(A,A)=g(B,B)=a\). Its transfer matrix for inverse temperature \(t>0\) has form
\[
N_t=\begin{pmatrix}e^{ta}&b_t\\c_t&e^{ta}\end{pmatrix},\qquad b_t,c_t>0.
\]
A right Perron vector is proportional to \((\sqrt{b_t},\sqrt{c_t})\); a left one is proportional to \((\sqrt{c_t},\sqrt{b_t})\). Their componentwise products are equal. Both fixed-point symbols therefore have stationary mass **exactly one-half for every** \(t>0\). Every weak-* zero-temperature limit supported on the two fixed points must be their equibarycenter. One symbol cannot support two distinct fixed points, so the three-symbol construction is alphabet-minimal under the stated hypotheses.

## Verification
The accompanying standard-library checker `verify.py` tests the exact degree-three characteristic identity using rational arithmetic and checks finite-temperature Perron eigenvectors, row stochasticity, stationarity, limiting weights, low-temperature jump rates, the two-symbol obstruction, and projected-time transition probabilities at multiple temperature scales. A successful finite checker is only a consistency test, not proof for all inverse temperatures or all two-symbol potentials; those quantified statements follow analytically from the displayed formulas.

## Relationship to prior work
Hedges (arXiv:2604.10225) characterizes which prescribed ergodic states are uniquely realizable as finite-temperature equilibrium states; this theorem concerns a distinct selection question, namely which point in a two-ground-state simplex is approached by uniquely determined positive-temperature states. Chazottes–Gambaudo–Ugalde (arXiv:0903.1212, especially Theorem 1 and Sections 6.1–6.3) already establish convergence and a general renormalization algorithm for *all* locally constant potentials, and exhibit an irrational limit for **four** fixed ground states on a four-symbol alphabet. Our convergence and basic transfer-matrix method are thus not new in general. The contribution assessed here is a **three-symbol full-shift realization with exactly two fixed ground states**, a sharp two-symbol impossibility theorem in the indicated nearest-neighbor class, and its explicit metastable transition rates. Baraviera–Leplaideur–Lopes (arXiv:1004.2848, Theorem in Section 1.2) already obtain the *same golden-ratio mixture coefficients* for a **non-locally-constant** potential on a three-symbol full shift; those numbers alone are expressly not claimed as new. The finite-range realization, minimality boundary, and kinetic law distinguish the present statement.

## Limitations
The minimum-alphabet assertion is for nearest-neighbor potentials and two fixed-point ground states on mixing one-step edge shifts; it is **not** a bound for longer-range potentials or other ground-state configurations. Finite-dimensional distribution convergence of the projected chain is proved, not a general uniform path-space convergence statement. This explicit small matrix calculation may be implicit in established general renormalization or singular Markov-chain perturbation methods. Priority remains subject to further expert and bibliographic verification. No independent verification is asserted.

## References
1. C. Evans Hedges, *A Local Characterization of Unique Equilibrium States*, arXiv:2604.10225 (first publicly posted April 11, 2026), https://arxiv.org/abs/2604.10225 .
2. J.-R. Chazottes, J.-M. Gambaudo, E. Ugalde, *Zero-temperature limit of one-dimensional Gibbs states via renormalization: the case of locally constant potentials*, arXiv:0903.1212 (2009), https://arxiv.org/abs/0903.1212 .
3. A. T. Baraviera, R. Leplaideur, A. O. Lopes, *Selection of measures for a potential with two maxima at the zero temperature limit*, arXiv:1004.2848 (2010), https://arxiv.org/abs/1004.2848 ; journal version *Selection of Ground States in the Zero Temperature Limit for a One-Parameter Family of Potentials*, SIAM J. Appl. Dyn. Syst. 11 (2012), 243–260.
