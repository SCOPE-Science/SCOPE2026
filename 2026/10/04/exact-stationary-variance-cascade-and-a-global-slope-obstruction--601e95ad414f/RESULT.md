# Exact stationary variance cascade and a global slope obstruction in the repressilator
## Finding
Consider the classical six-dimensional repressilator
\[
\dot m_i=R(p_{j_i})-m_i,\qquad
\dot p_i=\beta(m_i-p_i),
\]
for
\[
i\in\{1,2,3\},
\qquad
(j_1,j_2,j_3)=(3,1,2),
\]
where
\[
R(s)=\frac{\alpha}{1+s^h}+\alpha_0,
\qquad
\alpha>0,\quad
\alpha_0\ge0,\quad
\beta>0,\quad
h>1.
\]

For every compactly supported invariant Borel probability measure \(\mu\) in the nonnegative concentration orthant,
\[
\boxed{\mathbb E_\mu[R(p_{j_i})\mid m_i]=m_i}
\]
and
\[
\boxed{\mathbb E_\mu[m_i\mid p_i]=p_i}
\]
for each \(i\).

These two calibrations give an exact two-stage fluctuation budget:
\[
\boxed{
\operatorname{Var}_\mu(R(p_{j_i}))
-
\operatorname{Var}_\mu(m_i)
=
\mathbb E_\mu[\dot m_i^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(m_i)
-
\operatorname{Var}_\mu(p_i)
=
\frac1{\beta^2}\mathbb E_\mu[\dot p_i^2]
}.
\]
Hence
\[
\operatorname{Var}_\mu(R(p_{j_i}))
-
\operatorname{Var}_\mu(p_i)
=
\mathbb E_\mu[\dot m_i^2]
+
\frac1{\beta^2}\mathbb E_\mu[\dot p_i^2].
\]

Either individual defect vanishes exactly for measures supported on the equilibrium set. In the three-gene classical model the positive equilibrium is unique, so every non-equilibrium compact stationary state satisfies the strict cascade
\[
\operatorname{Var}_\mu(R(p_{j_i}))
>
\operatorname{Var}_\mu(m_i)
>
\operatorname{Var}_\mu(p_i)
\]
for all three genes.

Let
\[
L=\sup_{s\ge0}|R'(s)|.
\]
Every non-equilibrium compact stationary state must satisfy
\[
\boxed{L>1}.
\]
Indeed, if
\[
V_i=\operatorname{Var}_\mu(p_i),
\]
then a non-equilibrium state has
\[
V_i>0
\]
for all \(i\) and
\[
V_i
<
\operatorname{Var}_\mu(R(p_{j_i}))
\le
L^2V_{j_i}.
\]
Multiplying around the three-gene cycle gives
\[
1<L^6.
\]

For the Hill repression law,
\[
L
=
\frac{\alpha(h+1)^2}{4h}
\left(\frac{h-1}{h+1}\right)^{(h-1)/h}.
\]
Therefore
\[
L\le1
\]
rules out every non-equilibrium compact invariant probability measure, and in particular every nonconstant periodic orbit.

For the common Hill exponent
\[
h=2,
\]
the condition becomes
\[
L=\frac{9\alpha}{8\sqrt3},
\]
so no non-equilibrium compact stationary state can exist when
\[
\alpha\le\frac{8\sqrt3}{9}.
\]

## Assumptions and scope
The six state variables are the three mRNA concentrations \(m_i\) and their three corresponding protein concentrations \(p_i\). The cyclic orientation is immaterial; the displayed indexing agrees with a standard presentation of the Elowitz–Leibler equations.

The invariant measure \(\mu\) is supported on a compact subset of the nonnegative concentration orthant. Compact support gives the integrability needed for the antiderivative test functions below.

The model is the deterministic continuous approximation introduced with the synthetic repressilator. The foundational article was published on 20 January 2000. Later full-system mathematical work treats these equations as a six-dimensional ordinary differential equation and proves Hopf bifurcation results. A mathematical bibliographic record for that work lists MSC \(34C05\), \(34C07\), and \(34C23\); the present result is placed under primary MSC \(34C05\).

The global slope obstruction is only a sufficient no-recurrence condition. It is not claimed to be the sharp Hopf threshold and is independent of the protein-to-mRNA degradation-rate ratio \(\beta\).

## Proof
Fix \(i\). Let \(\phi\) be continuous on the compact \(m_i\)-range of the support, and choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(m_i)=\phi(m_i).
\]
The generator gives
\[
LH
=
\phi(m_i)\bigl(R(p_{j_i})-m_i\bigr).
\]
Invariance implies
\[
\mathbb E_\mu[
\phi(m_i)(R(p_{j_i})-m_i)
]
=
0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[R(p_{j_i})\mid m_i]=m_i.
\]

Similarly, for any continuous \(\psi\) on the compact \(p_i\)-range and an antiderivative \(K\),
\[
LK
=
\beta\psi(p_i)(m_i-p_i).
\]
Therefore
\[
\mathbb E_\mu[m_i\mid p_i]=p_i.
\]

The first conditional law makes the residual
\[
R(p_{j_i})-m_i=\dot m_i
\]
orthogonal to every square-integrable function of \(m_i\). In particular,
\[
\mathbb E_\mu[R(p_{j_i})m_i]
=
\mathbb E_\mu[m_i^2]
\]
and
\[
\mathbb E_\mu[R(p_{j_i})]
=
\mathbb E_\mu[m_i].
\]
Expanding the residual square gives
\[
\mathbb E_\mu[\dot m_i^2]
=
\operatorname{Var}_\mu(R(p_{j_i}))
-
\operatorname{Var}_\mu(m_i).
\]

The second conditional law gives
\[
m_i-p_i=\frac{\dot p_i}{\beta}
\]
orthogonal to functions of \(p_i\). Thus
\[
\frac1{\beta^2}\mathbb E_\mu[\dot p_i^2]
=
\operatorname{Var}_\mu(m_i)
-
\operatorname{Var}_\mu(p_i).
\]

We next classify equality. Suppose
\[
\mathbb E_\mu[\dot m_i^2]=0.
\]
Continuity implies
\[
\dot m_i=0
\]
throughout the support. Along every support trajectory, \(m_i\) is constant and
\[
R(p_{j_i})=m_i.
\]
The Hill function \(R\) is strictly decreasing on the nonnegative half-line, so \(p_{j_i}\) is constant. Then
\[
\dot p_{j_i}=0
\]
forces \(m_{j_i}=p_{j_i}\), hence \(m_{j_i}\) is constant. Repeating around the three-gene cycle makes all six coordinates constant, so the support lies on equilibria.

The same conclusion follows if
\[
\mathbb E_\mu[\dot p_i^2]=0.
\]
Then \(p_i\) is constant on support trajectories and
\[
m_i=p_i
\]
is constant; the preceding argument again propagates around the cycle. The converse is immediate.

The positive equilibrium is unique. At equilibrium,
\[
p_i=m_i=R(p_{j_i}).
\]
Thus \(p_1\) is a fixed point of the third iterate \(R^3\). Since \(R\) is strictly decreasing, \(R^3\) is strictly decreasing, while the identity map is strictly increasing. Hence there is at most one such fixed point. The scalar equation
\[
r=R(r)
\]
has a positive solution by continuity, so the unique equilibrium is
\[
m_1=m_2=m_3=p_1=p_2=p_3=r.
\]

Now assume \(\mu\) is not the equilibrium atom. If any
\[
\operatorname{Var}_\mu(p_i)=0,
\]
then \(p_i\) is constant and the same propagation argument forces equilibrium support. Hence
\[
V_i=\operatorname{Var}_\mu(p_i)>0
\]
for all \(i\).

Both speed defects are then strictly positive, so
\[
V_i
<
\operatorname{Var}_\mu(R(p_{j_i})).
\]
For a Lipschitz function with constant \(L\),
\[
\operatorname{Var}(R(P))
\le
L^2\operatorname{Var}(P).
\]
One proof uses an independent copy \(P'\):
\[
2\operatorname{Var}(R(P))
=
\mathbb E[(R(P)-R(P'))^2]
\le
L^2\mathbb E[(P-P')^2]
=
2L^2\operatorname{Var}(P).
\]
Therefore
\[
V_i<L^2V_{j_i}.
\]
Multiplying the three inequalities gives
\[
V_1V_2V_3
<
L^6V_1V_2V_3,
\]
and positivity of the product yields
\[
L>1.
\]

Finally,
\[
|R'(s)|
=
\frac{\alpha h s^{h-1}}{(1+s^h)^2}.
\]
With
\[
u=s^h,
\]
the positive factor to maximize is
\[
\frac{u^{(h-1)/h}}{(1+u)^2}.
\]
Its logarithmic derivative vanishes exactly at
\[
u=\frac{h-1}{h+1},
\]
and changes sign from positive to negative there. Substitution gives
\[
L
=
\frac{\alpha(h+1)^2}{4h}
\left(\frac{h-1}{h+1}\right)^{(h-1)/h}.
\]
The specialization \(h=2\) follows directly.

## Verification
The accompanying checker verifies the algebraic residual-variance identities and the exact \(h=2\) slope threshold.

It confirms that if
\[
\mathbb E[AB]=\mathbb E[B^2],
\qquad
\mathbb E[A]=\mathbb E[B],
\]
then
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

For \(h=2\), it verifies that the critical point of
\[
|R'(s)|
=
\frac{2\alpha s}{(1+s^2)^2}
\]
is
\[
s=\frac1{\sqrt3}
\]
and that
\[
L=\frac{9\alpha}{8\sqrt3}.
\]
Hence
\[
L\le1
\iff
\alpha\le\frac{8\sqrt3}{9}.
\]

The stored checker output is `VERIFY_OK`.

The general Hill-slope maximization, conditional-expectation steps, and equality classification are analytic arguments detailed above; they are not inferred from finite experiments.

## Relationship to prior work
Elowitz and Leibler introduced and experimentally realized the three-gene repressilator in 2000. Their deterministic continuous approximation uses coupled mRNA and protein concentrations with cyclic Hill repression.

Müller, Hofbauer, Endler, Flamm, Widder, and Schuster gave a detailed 2006 mathematical analysis of generalized repressilator models. Their complete article derives the kinetic equations, treats leaky and auto-activating variants, and analyzes equilibria, Hopf bifurcation, periodic oscillations, and heteroclinic cycles. Document-wide searches of the inspected article did not locate invariant-measure, moment, or variance statements matching the accepted result.

Buzzi and Llibre studied the full six-dimensional repressilator and proved a supercritical Hopf bifurcation. Their complete preprint writes the same mRNA/protein equations and focuses on the local bifurcation and its stable limit cycle. Targeted full-text searches did not locate invariant-measure, average, moment, or variance formulations.

Verdugo's complete 2018 analysis also writes the six-dimensional model and studies equilibria, center-manifold reduction, bifurcation curves, oscillation amplitudes, and frequencies. Targeted searches did not locate invariant-measure, average, moment, or variance statements.

Tyler, Shiu, and Walton later generalized the repressilator to broad transcription, translation, and degradation functions and proved strong qualitative results, including the equilibrium-or-periodic-orbit alternative for odd gene cycles under their assumptions. Their complete open manuscript contains no variance, invariant-measure, average, or moment formulation under the targeted searches performed.

The accepted statement is different in kind from local Hopf criteria and global orbit classification. It gives an exact stationary variance budget at each biochemical stage and a distribution-free global obstruction to recurrent stationary fluctuations based only on the maximum Hill slope.

## Limitations
The theorem concerns compactly supported invariant probability measures in the nonnegative concentration orthant.

The condition
\[
L\le1
\]
is a sufficient obstruction to non-equilibrium compact stationary states; it is not asserted to coincide with the sharp Hopf or global-stability threshold.

The result does not determine the period, amplitude, phase shift, or full invariant distribution of an oscillation.

The variance cascade is deterministic and stationary. It does not include intrinsic molecular noise from stochastic chemical kinetics.

The original 2000 publisher page was used to verify provenance and publication date, while the exact six-dimensional equations were checked in later full mathematical treatments. A differently phrased fluctuation identity could remain in unindexed literature.

## References
1. M. B. Elowitz and S. Leibler, “A synthetic oscillatory network of transcriptional regulators,” Nature 403, 335–338 (2000), DOI 10.1038/35002125.
2. S. Müller, J. Hofbauer, L. Endler, C. Flamm, S. Widder, and P. Schuster, “A generalized model of the repressilator,” Journal of Mathematical Biology 53, 905–937 (2006), DOI 10.1007/s00285-006-0035-9.
3. O. Buşe, R. Pérez, and A. Kuznetsov, “Dynamical properties of the repressilator model,” Physical Review E 81, 066206 (2010), DOI 10.1103/PhysRevE.81.066206.
4. C. A. Buzzi and J. Llibre, “Hopf bifurcation in the full repressilator equations,” Mathematical Methods in the Applied Sciences 38, 1428–1436 (2015), DOI 10.1002/mma.3158.
5. A. Verdugo, “Hopf Bifurcation Analysis of the Repressilator Model,” American Journal of Computational Mathematics 8, 137–152 (2018), DOI 10.4236/ajcm.2018.82011.
6. J. Tyler, A. Shiu, and J. Walton, “Revisiting a synthetic intracellular regulatory network that exhibits oscillations,” Journal of Mathematical Biology 78, 2341–2368 (2019), DOI 10.1007/s00285-019-01346-3.
