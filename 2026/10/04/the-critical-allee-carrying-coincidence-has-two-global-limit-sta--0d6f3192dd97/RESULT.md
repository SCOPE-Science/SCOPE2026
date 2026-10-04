# The critical Allee–carrying coincidence has two global limit states
## Finding
For the three-species food-chain model of Satar, Naji, and Haque, impose the source's critical equality \(b_1=1/a_1=:b\), with every parameter positive. Then every nonnegative solution exists globally and converges to one of exactly two equilibria,
\[
E_0=(0,0,0),\qquad E_b=(b,0,0).
\]
Thus \(E_0\) is not globally asymptotically stable at this equality, contrary to the global-stability statement in Theorem 1 of the source.

There is also an exact basin statement on the invariant plane \(v=0\). For \(0\le u(0)<b\), the solution converges to \(E_0\); for \(u(0)\ge b\), it converges to \(E_b\). If \(u(0)>b\), the approach to the nonzero equilibrium is algebraic with the sharp limit
\[
\lim_{t\to\infty}t\bigl(u(t)-b\bigr)=b+b_2.
\]

## Assumptions and scope
The source model is
\[
\begin{aligned}
u'&=u(1-a_1u)\frac{u-b_1}{u+b_2}-uv,\\
v'&=v(u-w-a_2),\\
w'&=w(a_3v-a_4),
\end{aligned}
\]
with \(a_1,a_2,a_3,a_4,b_1,b_2>0\) and initial data in \(\mathbb{R}_{\ge0}^3\). The result concerns the degenerate equality \(b_1=1/a_1\), where the source's Allee threshold and prey carrying scale coincide. No statement is made here about parameter values away from that equality, interior coexistence equilibria, or bifurcations away from this critical surface.

## Proof
Set \(b=b_1=1/a_1\). Since \(1-a_1u=a_1(b-u)\), the prey equation becomes
\[
u'=-\frac{a_1u(u-b)^2}{u+b_2}-uv.
\]
The nonnegative octant is forward invariant because every equation has the corresponding population variable as a factor at its coordinate boundary.

Define
\[
L(u,v,w)=u+v+\frac{w}{a_3}.
\]
Along every nonnegative solution, the interaction terms cancel and give the exact identity
\[
\begin{aligned}
L'&=u'+v'+\frac{w'}{a_3}\\
&=-\frac{a_1u(u-b)^2}{u+b_2}-a_2v-\frac{a_4}{a_3}w\le0.
\end{aligned}
\]
Hence every solution remains in a compact sublevel set of \(L\), so it exists for all forward time. The zero-derivative set is exactly
\[
\{L'=0\}=\{E_0,E_b\},
\]
and both points are equilibria. LaSalle's invariance principle therefore places every omega-limit set inside \(\{E_0,E_b\}\). Because the prey equation also gives \(u'\le0\), the coordinate \(u(t)\) has a limit; consequently a trajectory cannot accumulate on both separated equilibria. Every nonnegative solution therefore converges to exactly one of \(E_0\) or \(E_b\).

The existence of the second equilibrium \(E_b\ne E_0\) already rules out global asymptotic stability of \(E_0\) at the critical equality.

For the sharper invariant-plane statement, set \(v(0)=0\). Then \(v(t)=0\), \(w(t)=w(0)e^{-a_4t}\), and \(u\) solves the scalar equation
\[
u'=-\frac{a_1u(u-b)^2}{u+b_2}.
\]
If \(0<u(0)<b\), uniqueness prevents crossing either equilibrium and monotonicity forces \(u(t)\to0\). If \(u(0)>b\), uniqueness prevents crossing \(b\), monotonicity forces \(u(t)\to b\), and \(u(0)=b\) gives the constant solution \(u(t)=b\). The endpoint \(u(0)=0\) is also constant.

For \(u(0)>b\), put \(y=u-b>0\) and \(z=1/y\). Then
\[
z'=\frac{a_1u}{u+b_2}\longrightarrow\frac{a_1b}{b+b_2}=\frac{1}{b+b_2}.
\]
Averaging this convergent derivative gives \(z(t)/t\to1/(b+b_2)\), which is equivalent to
\[
t\bigl(u(t)-b\bigr)\to b+b_2.
\]
This proves the sharp algebraic rate.

## Verification
The proof is symbolic. A standalone exact-rational checker accompanies this note. It verifies the critical parameter identity on an explicit positive rational parameter set, both equilibria, the Lyapunov derivative identity at exact rational test states, the sign structure of the scalar invariant-plane equation, and the coefficient in the reciprocal-variable rate. Those finite checks are reproducibility aids only; the universal statements above follow from the displayed algebra, compactness, LaSalle's invariance principle, uniqueness, and monotonicity.

## Relationship to prior work
The motivating article states in Theorem 1 that the trivial equilibrium \(E_0\) is globally asymptotically stable when \(b_1=1/a_1\). Later in the same article, the axial equilibria at \(u=b_1\) and \(u=1/a_1\) are explicitly observed to coincide at the nonhyperbolic point \(E_b=(b,0,0)\) under that equality. The present calculation resolves the resulting inconsistency: the same Lyapunov function used in the source has a two-point zero-derivative set, not a one-point invariant set, and the equality case has two possible global limit states rather than universal extinction.

General strong-Allee literature treats the Allee threshold and carrying state as distinct equilibria and explains the familiar extinction-versus-survival separation. That framework motivates checking the singular coincidence but does not give the present three-species two-limit-state theorem or the exact \(1/t\) coefficient. A later food-chain chapter with an Allee effect analyzes a different system and different equilibrium formulas; it does not imply the critical identity proved here.

## Limitations
The theorem does not characterize the full basin of \(E_b\) away from the invariant plane \(v=0\), and it does not classify the center dynamics near \(E_b\) for every relation between \(a_2\) and \(b\). The sharp \(1/t\) law is proved only on \(v=0\) for \(u(0)>b\). No claim is made about stochastic, spatial, delayed, or discrete variants of the model.

## References
1. H. A. Satar, R. K. Naji, and M. Haque, “A food chain model with Allee effect: Analysis on the behaviors of equilibria,” *AIMS Mathematics* 10 (2025), 12598–12618. DOI: 10.3934/math.2025568. Published 29 May 2025.
2. J. M. Cushing and J. T. Hudson, “Evolutionary dynamics and strong Allee effects,” *Journal of Biological Dynamics* 6 (2012), 941–958. DOI: 10.1080/17513758.2012.697196.
3. S. Kumari and J. Omana, “Stability and Bifurcation in a Food Chain Model with the Allee Effect,” IntechOpen (2026). DOI: 10.5772/intechopen.1012240.
