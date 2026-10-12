# Stable period-two switching on a complete network in an opinion–action public-goods game

## Finding
In the noncooperative public-goods/opinion game [1], a connected, strictly positive off-diagonal influence network can support a **locally attracting, non-equilibrium, prime-period-two orbit** under simultaneous best-response revision, although both consensus Nash equilibria also attract nearby states. The orbit occurs on an open set of admissible payoff/network parameters, not only at a tuned or tie-breaking boundary. This supplies a counterexample to the unrestricted equilibrium-convergence conjecture at the end of [1], specifically for its explicitly permitted synchronous revision sequences.

**Theorem (open family of attracting two-cycles).** Take four players partitioned into pairs \(\{1,2\}\) and \(\{3,4\}\), all with identical public-goods and opinion parameters \(\alpha,\beta,\lambda>0\), \(\alpha+\beta+\lambda=1\), multiplier \(1<r<4\), and zero attachment to fixed prejudices \(\gamma=0\). Let the symmetric influence weights have zero diagonal, pair-mate weight \(\varepsilon\in(0,1/2)\), and opposite-pair weight \((1-\varepsilon)/2\) for each of the two such neighbors. All four players revise simultaneously at every integer time. Define
\[
\rho=\frac{\beta}{\beta+\lambda},\quad
\eta=\frac{\lambda}{\beta+\lambda},\quad
\kappa=\frac{\beta\lambda}{\beta+\lambda},\quad
D=\eta+2\rho\varepsilon,\quad
b=\frac{\varepsilon}{D},\quad
\theta=\frac{1}{2}+\frac{\alpha(1-r/4)}{\kappa}.
\]
If \(b<\theta<1-b\), put \(L=\rho\varepsilon/D\) and \(H=(\eta+\rho\varepsilon)/D\). Then the opinion vectors
\[
Y_A=(H,H,L,L),\qquad Y_B=(L,L,H,H)
\]
form a strict period-two orbit. Along the two successive steps, the action vectors are respectively \((0,0,1,1)\) and \((1,1,0,0)\). Each point has a relatively open neighborhood in the four-dimensional opinion cube whose orbits converge geometrically to this two-cycle. Both all-defection and all-cooperation are additional locally attracting equilibria. The two-cycle persists under sufficiently small admissible perturbations of the parameters and stochastic influence weights that preserve strict positive off-diagonal entries.

A rational example has
\[
(\alpha,\beta,\lambda,r,\varepsilon)=\left(\frac{1}{20},\frac{1}{5},\frac{3}{4},3,\frac{1}{10}\right),\quad
\rho=\frac{4}{19},\quad\eta=\frac{15}{19},\quad
\theta=\frac{139}{240},\quad
(H,L)=\left(\frac{77}{79},\frac{2}{79}\right).
\]
The network is the complete graph on four vertices with strictly positive off-diagonal weights, and its stochastic matrix is primitive.

## Assumptions and scope
The strategy of player \(i\) is \((x_i,y_i)\in\{0,1\}\times[0,1]\), where the binary action \(x_i=1\) means cooperation. The public-goods payoff multiplier obeys \(1<r<n=4\), as in [1]. Player \(i\)'s joint payoff is the weighted sum in [1, Eq. (4)] of the public-goods payoff, the Friedkin–Johnsen quadratic opinion payoff, and the quadratic action–opinion consistency penalty. There are no self-influence weights, so the best-response formula from [1, Proposition 1] applies without any self-loop ambiguity. All agents are active every timestep, which satisfies [1, Assumption 1] with the allowed window \(T=1\); the zero-discriminant convention is to defect, although it is never invoked on the stated two-cycle.

For \(u_i=\sum_j w_{ij}y_j\), the complete simultaneous best-response law [1, Eqs. (5), (10)–(12)] with \(\gamma=0\) becomes
\[
\delta_i=\alpha\left(\frac{r}{4}-1\right)+\kappa\left(u_i-\frac{1}{2}\right)
=\kappa(u_i-\theta),\qquad
x_i^{+}=\begin{cases}1,&u_i>\theta,\\0,&u_i\le\theta,\end{cases}
\qquad y_i^{+}=\rho u_i+\eta x_i^{+}.
\]
Here \(\rho+\eta=1\). Because all entries of the influence matrix are nonnegative and rows sum to one, this map preserves the closed opinion cube.

## Proof
For any pair-constant state \((H,H,L,L)\) with \(H+L=1\), each high-opinion player's input is \(u_H=\varepsilon H+(1-\varepsilon)L\); each low-opinion player's input is \(u_L=\varepsilon L+(1-\varepsilon)H\). With \(D=\eta+2\rho\varepsilon\), the asserted values satisfy
\[
L=\frac{\rho\varepsilon}{D},\quad H=1-L,\quad
u_H=\frac{\varepsilon}{D}=b,\quad
u_L=1-b.
\]
Indeed, \(\varepsilon H+(1-\varepsilon)L=\varepsilon+(1-2\varepsilon)\rho\varepsilon/D=\varepsilon/D\), because \(\rho+\eta=1\). The opposite-pair input is its complement. Since \(b<\theta<1-b\), all high-opinion players *strictly* select action zero and all low-opinion players *strictly* select action one. The update then gives
\[
y_H^{+}=\rho b=L,\qquad
y_L^{+}=\rho(1-b)+\eta=H.
\]
Thus \(Y_A\mapsto Y_B\). The same calculation with groups exchanged gives \(Y_B\mapsto Y_A\). Moreover \(H>L\): from \(H-L=(\eta)/D>0\), the two states are distinct. Their binary decisions alternate, so the trajectory cannot converge to a fixed equilibrium.

For local attraction, the two strict margins \(\theta-b>0\) and \(1-b-\theta>0\) imply that the action choices stay constant in small infinity-norm neighborhoods of the two points. On each such neighborhood, the opinion map is affine with linear part \(\rho W\). A nonnegative row-stochastic matrix satisfies \(\|Wv\|_\infty\le\|v\|_\infty\), hence \(\|\rho W\|_\infty\le\rho<1\). Choose a radius \(\delta>0\) below both decision-input margins. Then each \(\delta\)-ball about \(Y_A\) maps into the \(\rho\delta\)-ball about \(Y_B\), and conversely; repeated two-step application contracts by at most \(\rho^2\). The full action–opinion process inherits attraction because newly chosen actions depend only on current opinions and then agree exactly after one iteration. The consensus states \((x,y)=({\bf0},{\bf0})\) and \((x,y)=({\bf1},{\bf1})\) are fixed since \(0<\theta<1\), with the same strict local contraction argument.

For robustness, fix the two alternating strict action vectors \(s_A=(0,0,1,1)\) and \(s_B=(1,1,0,0)\). Nearby admissible parameters induce affine branch maps \(F_A(y)=\rho Wy+\eta s_A\) and \(F_B(y)=\rho Wy+\eta s_B\) in the homogeneous family. Solving \(Y_B=F_A(Y_A)\), \(Y_A=F_B(Y_B)\) requires inverting \(I-\rho^2W^2\), which is invertible for all \(0<\rho<1\) since \(\|\rho^2W^2\|_\infty\le\rho^2<1\). Therefore the orbit varies continuously with the parameters. Strict decision margins and \(H>L\) persist under sufficiently small changes; this establishes a genuine parameter-open region rather than a special tie. In a nonhomogeneous perturbation the same contraction/invertibility argument uses the corresponding diagonal coefficient matrices and remains valid sufficiently near this example.

For the rational witness, the two network inputs at \(Y_A\) are \((19/158,19/158,139/158,139/158)\); since \(19/158<139/240<139/158\), the action inequalities are strict. The four discriminants are \((-8701/120080,-8701/120080,5699/120080,5699/120080)\). The opinion update gives exactly \((2/79,2/79,77/79,77/79)\); the next step reverses it. An independent eigenbasis calculation gives the influence matrix eigenvalues \(1,-4/5,-1/10,-1/10\). Thus the two-step linear return map has multipliers \(16/361,256/9025,4/9025,4/9025\), all strictly below one in modulus; the norm argument already establishes attraction without relying on the eigenvalue calculation.

## Verification
Run `python3 verify_cycle.py` using the Python 3 standard library. The script constructs the four-player network and payoff constants as exact rational numbers; checks row stochasticity, positivity, symmetry, no self-weights, the strict discriminants, both best-response updates, the distinctness of the period-two opinions, stability margins, coexistence of the two consensus fixed points, and a complete explicit eigenbasis. The script prints `VERIFY_OK` if all checks succeed. No floating-point simulation is used to certify the orbit. The symbolic proof above, rather than finite testing, proves the open-family theorem and its stability and robustness statements.

## Relationship to prior work
Davidson et al. [1] give precisely the best-response map used here, explicitly permit synchronous updates in Remark 2, prove global defection under an additional sufficient condition, and conclude with a broader equilibrium-convergence conjecture. The construction satisfies their allowed synchronous revision schedule but not the assumptions of their global-defection theorem. It disproves only the unrestricted conjecture, not their established special-case theorem and not possible convergence under strictly singleton asynchronous revisions.

Earlier opinion–action game papers [2,3] primarily treat coordination or anti-coordination rather than the fixed-cost public-goods payoff of [1], with different action dependencies and update hypotheses. Synchronous threshold-response oscillations are already established in general binary-action social games [4]. Accordingly, neither periodic switching in generic simultaneous best responses nor the mere possibility of two-cycles is asserted to be new. The specific result here is a strict, attracting two-cycle with an open parameter region *in the opinion–action public-goods model of [1]*, on a complete primitive weighted graph, which contradicts that model's stated general convergence conjecture.

## Limitations
The construction uses the simultaneous-update subcase explicitly permitted by [1]. It does not show periodicity for strictly one-agent-at-a-time revisions, characterize all equilibria or all recurrent sets, claim global attraction of the cycle, or establish empirical oscillations in real groups. For finite populations, action switching is an idealized deterministic best response and does not represent noise. The claim is proved for the April 2026 publicly available preprint formulation [1]; a later version with extra restrictions could change the target conjecture. No independent audit has been performed.

## References
[1] E. C. Davidson, L. Zino, M. Cao, and M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1, first public 2026-04-10, Sections II–IV, Proposition 1, Assumption 1, Remark 2, equations (4)–(12), and Conclusion. https://arxiv.org/abs/2604.08840

[2] H. Dehghani Aghbolagh, M. Ye, L. Zino, Z. Chen, and M. Cao, *Coevolutionary dynamics of actions and opinions in social networks*, IEEE Transactions on Automatic Control 68 (2023), arXiv:2206.07242. https://arxiv.org/abs/2206.07242

[3] H. Liang, M. Ye, L. Zino, and W. Xia, *Coevolution of actions and opinions in networks of coordinating and anti-coordinating agents*, IFAC Journal of Systems and Control 33 (2025), arXiv:2505.03078. https://arxiv.org/abs/2505.03078

[4] P. Ramazi, J. Riehl, and M. Cao, *Networks of conforming or nonconforming individuals tend to reach satisfactory decisions*, PNAS (2016), DOI:10.1073/pnas.1610244113; discussion of synchronous-update cycles. https://doi.org/10.1073/pnas.1610244113
