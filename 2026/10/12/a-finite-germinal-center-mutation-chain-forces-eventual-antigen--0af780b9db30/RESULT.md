# A finite germinal-center mutation chain forces eventual antigen clearance

## Finding

Consider the non-mutating-antigen germinal-center model with a finite mutation chain
\[
B_0,B_1,\ldots,B_n
\]
and terminal plasma-cell production
\[
\dot P=\kappa B_n,
\qquad
\dot V=-\mu VP.
\]

Under the source's positive parameters and positive initial naive-cell, founder-B-cell, and antigen populations, every finite chain has
\[
B_i(t)>0\quad(1\le i\le n),
\qquad
P(t)>0
\]
for every
\[
t>0.
\]
Consequently,
\[
V(t)\to0
\qquad
(t\to\infty).
\]

More strongly, for every fixed \(t_0>0\),
\[
V(t)
\le
V(t_0)e^{-\mu P(t_0)(t-t_0)}
\qquad
(t\ge t_0).
\]

Thus the source's \(n=50\) simulation cannot represent positive asymptotic viral persistence in model (1). The exact ODE makes \(B_{50}\) and plasma cells strictly positive at every positive time, although their values may be extremely small over a finite simulation window.

## Assumptions and scope

The claim concerns model (1) of the source with finite
\[
n\ge1
\]
and strictly positive rates
\[
s_N,d_N,\alpha_N,d_H,\gamma,d_G,\eta,d,\sigma,\alpha,\kappa,\mu.
\]

The source initial conditions satisfy
\[
N(0)>0,\qquad
B_0(0)>0,\qquad
V(0)>0
\]
and all other model (1) state variables initially vanish.

The theorem is an exact long-time property of the deterministic ODE. It does not claim rapid clearance. For large \(n\), the terminal clone can be far below plotting or numerical resolution for a long time.

The result does not analyze the later mutating-antigen models.

## Proof

The non-mutating-antigen equations include
\[
\dot N=s_N-d_NN-\alpha_NVN,
\]
\[
\dot H=\alpha_NVN-d_HH-\gamma HB_0,
\]
\[
\dot G=\gamma HB_0-d_GG-\eta G\sum_{i=1}^nB_i,
\]
\[
\dot B_0=-dB_0-\sigma B_0H,
\]
\[
\dot B_1=\alpha\sigma B_0H-\sigma B_1G-dB_1,
\]
\[
\dot B_i=\alpha\sigma B_{i-1}G-\sigma B_iG-dB_i
\quad
(2\le i\le n-1),
\]
\[
\dot B_n=\alpha\sigma B_{n-1}G-(d+\kappa)B_n,
\]
\[
\dot P=\kappa B_n,
\qquad
\dot V=-\mu VP.
\]

First establish global boundedness. Define
\[
Q=
B_0+\sum_{i=1}^n\alpha^{-i}B_i+\alpha^{-n}P.
\]
All mutation terms cancel pairwise after applying the weights, and the plasma-production flux cancels between \(B_n\) and \(P\). Therefore
\[
\dot Q
=
-d\left(
B_0+\sum_{i=1}^n\alpha^{-i}B_i
\right)
\le0.
\]
Thus every B-cell clone and \(P\) is bounded.

Likewise, with
\[
T=N+H+G
\]
the activation and T-follicular-helper differentiation fluxes cancel:
\[
\dot T
=
s_N-d_NN-d_HH-d_GG-\eta G\sum_{i=1}^nB_i.
\]
If
\[
m=\min\{d_N,d_H,d_G\},
\]
then
\[
\dot T\le s_N-mT,
\]
so \(N,H,G\) are bounded. Finally \(V\) is nonincreasing. Hence the nonnegative solution cannot blow up in finite time.

Now prove strict positivity along the finite cascade. Since
\[
V(t)
=
V(0)\exp\!\left(
-\mu\int_0^tP(s)\,ds
\right),
\]
one has
\[
V(t)>0
\]
at every finite time. The \(N\)-equation has a positive source \(s_N\), so
\[
N(t)>0.
\]
The variation-of-constants formula for \(H\) has strictly positive forcing
\[
\alpha_NVN,
\]
hence
\[
H(t)>0
\]
for every \(t>0\).

The founder population satisfies
\[
B_0(t)
=
B_0(0)\exp\!\left(
-\int_0^t(d+\sigma H(s))\,ds
\right)>0.
\]
Therefore the \(G\)-equation has strictly positive forcing
\[
\gamma HB_0
\]
for positive time, so
\[
G(t)>0.
\]

The \(B_1\)-equation has strictly positive forcing
\[
\alpha\sigma B_0H,
\]
hence
\[
B_1(t)>0.
\]
Inductively, once
\[
B_{i-1}(t)>0,
\]
the \(B_i\)-equation has strictly positive forcing
\[
\alpha\sigma B_{i-1}G,
\]
so
\[
B_i(t)>0
\]
for every \(t>0\). In particular,
\[
B_n(t)>0.
\]

Thus
\[
\dot P(t)=\kappa B_n(t)>0
\]
for every \(t>0\), and
\[
P(t)>0
\]
for every \(t>0\). Fix any \(t_0>0\). Monotonicity gives
\[
P(t)\ge P(t_0)>0
\]
for all \(t\ge t_0\). Consequently,
\[
V(t)
=
V(t_0)
\exp\!\left(
-\mu\int_{t_0}^tP(s)\,ds
\right)
\le
V(t_0)e^{-\mu P(t_0)(t-t_0)},
\]
which proves
\[
V(t)\to0.
\]

## Verification

The bundled `verify.py` symbolically checks the weighted cancellation identity for an arbitrary finite chain represented algebraically.

It verifies that the weights
\[
1,\alpha^{-1},\ldots,\alpha^{-n}
\]
cancel every maturation flux
\[
\alpha\sigma B_{i-1}G
\]
against the preceding clone's loss and cancel the terminal plasma-cell flux.

It also checks the cancellation in
\[
N+H+G.
\]

The positivity and asymptotic argument are analytic and do not rely on finite simulation.

## Relationship to prior work

The motivating article develops finite B-cell mutation chains to compare acute and chronic infection. In its \(n=50\) calculation it states that the terminal clone is not reached, predicts no plasma-cell-driven virus removal, and interprets the nearly unchanged antigen as chronic persistence.

The same article's equations contain no plasma-cell death term. Once any terminal clone is present, plasma cells accumulate monotonically and make the antigen equation strictly dissipative.

Meyer-Hermann and coauthors model germinal-center B-cell selection, division, and plasma-cell exit with a substantially different mechanistic framework. That work establishes that delayed production of high-affinity plasma cells is biologically and mathematically natural, but it does not contain the finite irreversible mutation chain and antigen equation used here.

De Boer and Perelson later study broad neutralizing-antibody evolution during chronic HIV infection using a different chronic-infection germinal-center framework with persistent and evolving viral diversity. Their model addresses genuine chronic antigenic evolution rather than the finite one-way cascade in the motivating ODE, so it does not imply the exact clearance theorem above.

Targeted searches by DOI, exact title, terminal-clone terminology, antigen-persistence language, and equivalent finite-chain formulations did not locate a published correction of this source-specific asymptotic claim.

## Limitations

The theorem concerns exact deterministic concentrations. A terminal clone can be mathematically positive while being biologically negligible or numerically unresolved.

The result establishes asymptotic antigen clearance, not a practically short clearance time.

The source's earlier online record reports publication only to month precision as December 2016, while the day-resolved publisher record gives 1 June 2017. The scientific result is independent of this bibliographic granularity.

The theorem applies to model (1) and does not by itself determine the long-time behavior of the mutating-antigen extensions.

## References

1. S. Erwin, S. M. Ciupe, “Germinal center dynamics during acute and chronic infection,” Mathematical Biosciences and Engineering 14 (2017), 655–671. DOI: 10.3934/mbe.2017037.
2. M. Meyer-Hermann, E. Mohr, N. Pelletier, Y. Zhang, G. D. Victora, K.-M. Toellner, “A theory of germinal center B cell selection, division, and exit,” Cell Reports 2 (2012), 162–174. DOI: 10.1016/j.celrep.2012.05.010.
3. R. J. De Boer, A. S. Perelson, “How Germinal Centers Evolve Broadly Neutralizing Antibodies: the Breadth of the Follicular Helper T Cell Response,” Journal of Virology 91 (2017). DOI: 10.1128/JVI.00983-17.
