# An integrable inverse-square counterexample to exponential decay in acyclic spreading systems

## Finding

A finite, strictly positive, interaction-driven four-compartment spreading model satisfies both the directed-acyclic-transition assumption and the DAG-minus dependency assumption of Chan, Crommelin, and Mandjes, yet one vanishing compartment decays algebraically as \(8t^{-2}\), not exponentially. It therefore disproves their Conjecture 1 as stated. The non-exponential component is nevertheless integrable, so the example does not challenge the paper's integrability theorem.

Concretely, there is a solution with
\[
\lim_{t\to\infty}(X(t),U(t),Y(t),Z(t))=(1/4,1/4,0,1/2),\qquad
\lim_{t\to\infty}t^2Y(t)=8,
\qquad \int_0^\infty Y(t)\,dt=\log(6/5).
\]

## Assumptions and scope

All populations are fractions of one normalized, well-mixed population. Only the following pairwise interaction-induced one-individual transitions occur, at the mass-action rates shown:

* \(X\to Z\), catalyzed by \(Y\), at rate \(2XY\);
* \(U\to Y\), catalyzed by \(Y\), at rate \(UY\);
* \(Y\to Z\), catalyzed by \(X\), at rate \(XY\).

These nonnegative channels produce the autonomous system
\[
\dot X=-2XY,\quad
\dot U=-UY,\quad
\dot Y=(U-X)Y,\quad
\dot Z=3XY.
\]
The strictly positive initial state is
\[
(X(0),U(0),Y(0),Z(0))=(9/25,3/10,1/200,67/200).
\]
The four fractions sum to one initially and at every time, and positive solutions remain in the probability simplex for all finite nonnegative times.

The **transition graph** contains precisely \(X\to Z\), \(U\to Y\), and \(Y\to Z\); it is a DAG (Assumption 1 of the cited paper). The **outflow dependency graph** contains precisely \(X\to Y\), \(U\to Y\), and \(Y\to X\), with no self-loops. Its only directed cycle is \(X\leftrightarrow Y\). Along the solution described below, \(X\to1/4\), and \(Y\) has the dependency successor \(X\). Hence the sole dependency cycle contains a vertex with a **persistent dependency successor**, exactly as required by Assumption 2 of the paper. The successor is allowed to lie on the cycle: the original paper explicitly addresses this as Case 1 of its edge-removal procedure (Proposition 1).

## Proof

**Step 1: Existence and conserved quantities.** All components are bounded within the nonnegative simplex, since the vector field consists of nonnegative mass-action transition channels with conserved total mass:
\[
\dot X+\dot U+\dot Y+\dot Z=0.
\]
For finite time, \(X\), \(U\), and \(Y\) stay positive by their multiplicative equations, and \(Z\) is nondecreasing from a strictly positive initial value. These facts also guarantee global existence.

Direct differentiation yields two independent conserved quantities whenever \(X>0\):
\[
\frac{U(t)}{\sqrt{X(t)}}=\frac12,
\qquad
Y(t)+U(t)-\frac{X(t)}2=\frac18.
\]
In particular, putting \(r(t)=\sqrt{X(t)}\) gives the **exact** identities
\[
U(t)=\frac{r(t)}2,
\qquad
Y(t)=\frac12\left(r(t)-\frac12\right)^2,
\qquad
Z(t)=1-r(t)^2-\frac{r(t)}2-\frac12\left(r(t)-\frac12\right)^2.
\]
The initial value is \(r(0)=3/5\). Setting \(s(t)=r(t)-1/2\) therefore gives \(s(0)=1/10\) and the scalar equation
\[
\dot s=-\frac14s^2(1+2s).
\]

**Step 2: Long-time limit.** The scalar equation implies that \(s(t)>0\) decreases for every finite time and tends to zero; a strictly positive limiting value would imply a strictly negative limiting derivative. Consequently
\[
(X,U,Y,Z)\longrightarrow (1/4,1/4,0,1/2).
\]
For \(s>0\),
\[
\frac{d}{dt}\frac1s=\frac{1+2s}{4}\longrightarrow\frac14.
\]
Integrating this derivative (or using Cesàro averaging) gives \(\lim_{t\to\infty}ts(t)=4\). Since \(Y=s^2/2\),
\[
\boxed{\displaystyle\lim_{t\to\infty}t^2Y(t)=8.}
\]
A direct implicit solution, useful for reproducing the asymptotics, is
\[
t=\frac4{s(t)}-40+8\log\left(\frac{12s(t)}{1+2s(t)}\right),
\qquad 0<s(t)\le1/10.
\]
Differentiation recovers the scalar equation, and the right side vanishes at the initial value.

**Step 3: Integrability without exponential decay.** Integrating \(\dot U/U=-Y\) and using \(U(0)=3/10\), \(U(\infty)=1/4\) gives
\[
\boxed{\displaystyle\int_0^\infty Y(t)\,dt=\log(6/5)<\infty.}
\]
On the other hand, if \(Y(t)\le Ce^{-\lambda t}\) held for some finite \(C>0\) and \(\lambda>0\) and all sufficiently large \(t\), then \(t^2Y(t)\to0\), contradicting the proved limit \(8\). The Conjecture 1 implication fails despite both graph assumptions being satisfied.

## Verification

The standalone program `verify.py` symbolically verifies mass conservation, the two invariants, the explicit parameterization, the scalar differential equation, all initial/limiting fractions, and the inverse-square coefficient. It also evaluates the implicit solution numerically at several times; those finite tests corroborate but do not establish the asymptotic theorem. Run `python -m pip install -r requirements.txt` followed by `python verify.py`. The infinite-time conclusion is proved analytically above.

## Relationship to prior work

Chan, Crommelin, and Mandjes (2025), arXiv:2511.02437v1, §§2–3 and Appendix C, introduce these transition/dependency graphs and prove that every vanishing compartment is time-integrable when their two graph conditions hold. Their Conjecture 1 (p. 25) additionally claims exponential decay; the paper explicitly acknowledges that integrable algebraic rates such as inverse-square are not ruled out by its theorem. Its examples of slow algebraic decay (pp. 25–26 and Appendix C) violate the DAG-minus assumption, unlike the example above. Proposition 1's Case 1 (pp. 21–22) expressly allows a persistent successor lying on the dependency cycle.

The counterexample supplies the missing separation between **integrability** and **exponential decay** within the exact constrained model class. The inverse-square mechanism is a critical cancellation between one inflow and one outflow of the vanishing state, realized here on an invariant algebraic curve. General dynamical-systems facts about polynomial relaxation are not claimed as new.

## Limitations

This is one strictly positive initial condition in an exact four-compartment deterministic fluid model; it does not assert that inverse-square decay occurs for all initial conditions, coefficients, or graphs. It addresses only the exponential-decay conjecture, not the authors' integrability or persistence-classification theorems. The example uses tuned coefficients and initial values, so no genericity is claimed. Historical priority beyond inspected literature remains subject to independent research; the findings have not undergone independent scientific review.

## References

1. K. M. D. Chan, D. T. Crommelin, and M. R. H. Mandjes, *Asymptotic behavior for a general class of spreading models*, arXiv:2511.02437v1 (first posted 2025-11-04), particularly Definition 6–7, Assumptions 1–2, Proposition 1, Conjecture 1, and Appendix C. Full text: https://ir.cwi.nl/pub/36026/36026.pdf.
2. K. M. D. Chan and M. R. H. Mandjes, *A Versatile Stochastic Dissemination Model*, Methodology and Computing in Applied Probability 25, article 69 (2023), doi:10.1007/s11009-023-10041-2 (background on dissemination dynamics, a distinct stochastic-wealth framework).
