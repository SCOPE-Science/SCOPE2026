# A sharp constant-therapy eradication threshold for the weak-Allee cancer model

## Finding

For the weak-Allee single-clone equation with constant treatment,
\[
\dot x
=
x\left[
r\left(1-\frac{x}{K}\right)\frac{x}{x+c}
-g
\right],
\]
define
\[
g_c
=
\frac{r}{K}
\left(\sqrt{K+c}-\sqrt c\right)^2.
\]

Then the cancer-free state is globally asymptotically stable on the nonnegative half-line exactly when
\[
g>g_c.
\]

At
\[
g=g_c,
\]
a positive double equilibrium remains at
\[
x_*=\sqrt{c(K+c)}-c,
\]
so zero is not globally attractive.

For
\[
0<g<g_c,
\]
there are exactly two positive equilibria,
\[
x_\pm
=
\frac{
K(r-g)
\pm
\sqrt{
K^2(r-g)^2-4rgKc
}
}{2r}.
\]
The lower equilibrium is unstable and the upper equilibrium is locally asymptotically stable.

The source states the simpler sufficient condition
\[
g>r
\]
for global stability. Since
\[
g_c<r
\]
for every \(c>0\), that condition is conservative. At the source's displayed value
\[
c=\frac K2,
\]
the exact threshold is
\[
g_c=r(2-\sqrt3)\approx0.267949\,r.
\]

## Assumptions and scope

The parameters satisfy
\[
r>0,\qquad K>0,\qquad c>0,\qquad g>0,
\]
and \(g\) is constant in time.

The state space is
\[
x\ge0.
\]
The result uses the weak-Allee equation obtained from the source by setting its Allee threshold parameter to zero and adding the source's destruction term \(-gx\).

The word eradication here means asymptotic convergence to zero while the constant therapy remains applied. The model does not reach zero in finite time from positive initial data.

The result does not contradict the source's observation that a weak-Allee population can regrow after a finite-duration treatment is stopped.

## Proof

Write the treated per-capita growth rate as
\[
F(x)
=
r\phi(x)-g,
\qquad
\phi(x)
=
\left(1-\frac{x}{K}\right)\frac{x}{x+c}.
\]

For
\[
x>K,
\]
one has
\[
\phi(x)<0.
\]
It is therefore enough to maximize \(\phi\) on \([0,K]\).

Differentiation gives
\[
\phi'(x)
=
\frac{Kc-x^2-2cx}{K(x+c)^2}.
\]
The numerator has exactly one nonnegative zero,
\[
x_*=\sqrt{c(K+c)}-c,
\]
and changes from positive to negative there. Hence \(x_*\) is the unique maximizer.

At that point,
\[
\phi(x_*)
=
\frac{
\left(\sqrt{K+c}-\sqrt c\right)^2
}{K}.
\]
Therefore
\[
g_c
=
r\phi(x_*).
\]

If
\[
g>g_c,
\]
then
\[
F(x)<0
\]
for every \(x>0\). Every positive solution is strictly decreasing and bounded below. If its limit were positive, continuity would give a strictly negative derivative per capita near that limit, a contradiction. Thus every positive solution converges to zero.

If
\[
g=g_c,
\]
then
\[
F(x_*)=0,
\]
so \(x_*\) is a positive equilibrium and zero cannot be globally attractive.

Now suppose
\[
0<g<g_c.
\]
Positive equilibria satisfy
\[
r x(K-x)=gK(x+c),
\]
or
\[
r x^2-K(r-g)x+gKc=0.
\]
Because \(g<g_c\), its discriminant is positive, giving the two roots \(x_-\) and \(x_+\) displayed above. The sign of \(F\) is negative below \(x_-\), positive on \((x_-,x_+)\), and negative above \(x_+\). Thus zero and \(x_+\) are locally asymptotically stable and \(x_-\) is unstable.

Finally, with
\[
q=\frac cK,
\]
the threshold can be written
\[
\frac{g_c}{r}
=
\left(\sqrt{1+q}-\sqrt q\right)^2
=
\frac{1}{
\left(\sqrt{1+q}+\sqrt q\right)^2
}.
\]
This expression decreases strictly with \(q\), tends to \(1\) as \(q\downarrow0\), and tends to \(0\) as \(q\to\infty\).

For
\[
q=\frac12,
\]
\[
\frac{g_c}{r}
=
2-\sqrt3.
\]

## Verification

The bundled `verify.py` differentiates the per-capita growth function symbolically, verifies the maximizer and exact threshold formula, and checks the quadratic equilibrium factorization.

It also replays two exact normalized examples with
\[
K=2,\qquad c=1,\qquad r=\frac3{25}.
\]
At
\[
g=\frac1{25}=0.04,
\]
the checker verifies
\[
g_c<g<r
\]
and confirms that no positive equilibrium exists.

At
\[
g=\frac1{50}=0.02,
\]
it verifies the two positive equilibria
\[
x_\pm=\frac{5\pm\sqrt{13}}6.
\]

No finite grid search or numerical trajectory simulation is used to prove the classification.

## Relationship to prior work

Delitala and Ferraro introduce the exact weak-Allee cancer equation used here and model therapy by adding a destruction term \(-gx\). They state that \(g>r\) is sufficient for global stability of the cancer-free state and that any \(g>0\) makes zero locally stable in the weak-Allee case.

The exact threshold above sharpens that sufficient condition without changing the model. It identifies the required constant treatment strength with the maximum untreated per-capita growth rate and gives the complete one-dimensional phase portrait across the threshold.

Böttger and coauthors study a different tumor model in which density-dependent migration and proliferation generate Allee-type persistence or extinction. Their work establishes the broader relevance of Allee mechanisms to tumor initiation and persistence, but it does not use the Delitala-Ferraro scalar treatment equation or imply the closed-form threshold above.

Searches by the motivating DOI, exact title, weak-Allee treatment terminology, maximum-per-capita-growth terminology, the closed-form square-root threshold, and correction or erratum terminology did not locate a published statement of this source-specific sharp threshold.

## Limitations

The threshold applies to a sustained constant destruction term in the deterministic single-clone model.

It does not determine an optimal finite-duration treatment schedule and does not imply permanent eradication after treatment is stopped.

It is a mathematical model result, not a clinical dosing rule.

The general principle that constant mortality must exceed the maximum per-capita growth rate is elementary population-dynamical reasoning; the source-specific contribution is the exact closed form, full phase classification, and its quantitative implication for the published weak-Allee cancer model.

## References

1. M. Delitala, M. Ferraro, “Is the Allee effect relevant in cancer evolution and therapy?”, AIMS Mathematics 5 (2020), 7649–7660. DOI: 10.3934/math.2020489.
2. K. Böttger, H. Hatzikirou, A. Voss-Böhme, E. A. Cavalcanti-Adam, M. A. Herrero, A. Deutsch, “An Emerging Allee Effect Is Critical for Tumor Initiation and Persistence,” PLoS Computational Biology 11 (2015), e1004366. DOI: 10.1371/journal.pcbi.1004366.
