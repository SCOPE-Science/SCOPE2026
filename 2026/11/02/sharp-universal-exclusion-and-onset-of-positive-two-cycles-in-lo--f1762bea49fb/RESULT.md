# Sharp universal exclusion and onset of positive two-cycles in logistic predator–prey maps

## Finding
For the planar population map
\[
F_{\lambda,h}(x,y)=\bigl(x(\lambda-x-y),\;yh(x)\bigr),
\]
with \(\lambda>0\) and a positive nondecreasing recruitment function \(h:(0,\infty)\to(0,\infty)\), **no strictly positive orbit of least period two exists when \(0<\lambda\leq3\)**. The growth threshold is sharp within the biologically natural affine family \(h(x)=a+\gamma x\), \(0<a<1\), \(\gamma>0\): for every \(\lambda>3\), suitable \(a,\gamma\) yield a strictly positive least-period-two orbit.

In particular, Shoyimardonov's phytoplankton–zooplankton map \(F(x,y)=(x(2-x-y),y(1-r+\gamma x))\), with \(0<r\leq1\) and \(\gamma>0\), has no strictly positive least-period-two orbit at any of those parameters. This does not exclude periods three or higher, invariant circles, or chaotic recurrence.

## Assumptions and scope
Only positivity and monotonicity of \(h\) are required for the exclusion statement; continuity, differentiability, or boundedness of \(h\) are not needed. A strictly positive two-cycle means two distinct points \((x,y),(u,v)\in(0,\infty)^2\) with \(F_{\lambda,h}(x,y)=(u,v)\) and \(F_{\lambda,h}(u,v)=(x,y)\). No invariance of the entire positive quadrant is assumed, and the theorem concerns exact two-periodic trajectories, not the long-time behavior of arbitrary initial data.

For the sharpness statement, the affine recruitment function has positive intercept and positive slope, so it includes the form \(h(x)=1-r+\gamma x\) with \(0<r<1\).

## Proof
**Exclusion.** Suppose \((x,y)\mapsto(u,v)\mapsto(x,y)\) is strictly positive. The two prey equations give
\[
y=\lambda-x-\frac ux,\qquad
v=\lambda-u-\frac xu.
\]
Subtracting, obtain the exact difference identity
\[
v-y=(x-u)\left(1-\frac1x-\frac1u\right).\tag{1}
\]
Adding the prey identities and using \(u/x+x/u\geq2\) gives
\[
x+u=2\lambda-\left(\frac ux+\frac xu\right)-(y+v)
<2\lambda-2\leq4.
\]
Because \(4xu\leq(x+u)^2\), it follows that
\[
\frac1x+\frac1u=\frac{x+u}{xu}\geq\frac4{x+u}>1.\tag{2}
\]
The predator equations give \(v/y=h(x)\) and \(y/v=h(u)\), hence \(h(x)h(u)=1\). If \(x>u\), monotonicity implies \(h(x)\geq h(u)\); their positive product being one forces \(h(x)\geq1\), hence \(v\geq y\). But (1)–(2) imply \(v<y\), a contradiction. The case \(x<u\) is symmetric. Therefore \(x=u\). The first prey equality then forces \(y=v\), so the alleged orbit is a fixed point, not a genuine two-cycle.

**Sharpness at every \(\lambda>3\).** Choose a real \(z\) satisfying
\[
2<z<\min\left\{\lambda-1,\frac{\lambda+3}{3}\right\},
\]
which is possible exactly because \(\lambda>3\). For sufficiently small \(\varepsilon>0\), put
\[
x=z+\varepsilon,\quad u=z-\varepsilon,\quad
 y=\lambda-x-\frac ux,\quad
 v=\lambda-u-\frac xu.
\]
The two predator densities are positive, as both tend to \(Y=\lambda-z-1>0\). Since \(x,u>2\), formula (1) implies \(v>y\). Define
\[
B=\frac vy>1,\qquad C=\frac yv=\frac1B<1,\qquad
\gamma=\frac{B-C}{x-u},\qquad a=B-\gamma x.
\]
Then \(\gamma>0\), \(a+\gamma x=B\) and \(a+\gamma u=C\); thus the two prey and predator updates close into a positive prime-two orbit. As \(\varepsilon\downarrow0\), elementary division gives
\[
\gamma\longrightarrow\frac{2(1-2/z)}Y,\qquad
 a\longrightarrow1-\frac{2(z-2)}Y.
\]
The imposed inequality \(z<(\lambda+3)/3\) is equivalent to \(Y>2(z-2)\), making the last limit strictly between zero and one. Consequently, \(0<a<1\) holds for every sufficiently small \(\varepsilon>0\), completing the sharpness proof.

An exact rational witness at \(\lambda=4\) is
\[
(x,y)=\left(\frac{12}{5},\frac{29}{40}\right),\quad
(u,v)=\left(\frac{21}{10},\frac{53}{70}\right),\quad
h(t)=\frac{538}{1537}+\frac{6225}{21518}t.
\]
Indeed \(h(12/5)=212/203\), \(h(21/10)=203/212\), and direct substitution gives the specified two-cycle with both coordinates strictly positive.

## Verification
The identities in the proof establish the assertions for all admissible parameters and every nondecreasing positive function, without finite sampling. The accompanying self-contained `verify.py` checks the rational example with exact fractions and verifies additional rational sharpness constructions. Run `python3 verify.py` from the directory containing the two files. Computational tests are consistency checks, not a substitute for the general proof.

## Relationship to prior work
Shoyimardonov (arXiv:2505.09968v1, posted 2025-05-15) studies the special map \(x(2-x-y),y(1-r+\gamma x)\), including equilibria, invariant regions, and a Neimark–Sacker bifurcation. Its parameter \(\lambda=2\) lies strictly inside the exclusion theorem, but the source does not state the sharp general exclusion and realization theorem.

Vidiella, Lázaro, Alsedà and Sardanyés (2019) investigate \(T_{\mu,\beta}(s,t)=(\mu s(1-s-t),\beta st)\), a genuinely overlapping special case. Under the exact coordinate rescaling \(X=\mu s,\;Y=\mu t\), their map becomes \(F_{\mu,h}\) with \(h(X)=(\beta/\mu)X\). Their global-convergence theorems cover low-growth parameter subregions (notably \(\mu<2\)); their analysis of the remaining dynamics does not supply the all-\(h\) exclusion for \(\mu\leq3\) or the affine positive-intercept realization for every \(\lambda>3\). The present theorem does not claim that period-doubling, the one-dimensional logistic flip, or the earlier equilibrium results were newly discovered.

## Limitations
The exclusion is for strictly positive **least period two** only. It does not show global convergence, rule out higher periods, prove boundedness, or exclude quasiperiodic and chaotic states. The constructed supercritical orbit need not attract nearby initial conditions; no stability assertion is made. Although the consulted primary literature did not imply the complete statement, a historically equivalent result in additional predator–prey literature remains possible and requires external priority review.

## References
1. S. K. Shoyimardonov, *Stability and Bifurcation Analysis of a Phytoplankton-Zooplankton Model with Linear Functional Responses*, arXiv:2505.09968v1 (2025-05-15), https://arxiv.org/abs/2505.09968.
2. B. Vidiella, J. T. Lázaro, L. Alsedà and J. Sardanyés, *On Dynamics and Invariant Sets in Predator-Prey Maps*, in *Dynamical Systems Theory*, IntechOpen (2019), DOI:10.5772/intechopen.89572, https://www.intechopen.com/chapters/70218.
3. Wei Shan Lee et al., *Predator Extinction arose from Chaos of the Prey: the Chaotic Behavior of a Homomorphic Two-Dimensional Logistic Map in the Form of Lotka-Volterra Equations* (2023), arXiv:2301.11669. An independently defined homomorphic logistic model, not an implication of the present parameter-uniform period-two theorem.
