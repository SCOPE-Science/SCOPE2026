# Exact area-harmonic-mean law for every positive limit cycle in a fear–cooperation predator–prey model
## Finding
For the predator–prey system
\[
\dot x=\frac{rx}{1+s_1y}-a\left(1+s_2\frac{s_1y}{1+s_1y}\right)x-bx^2-(c+ey)xy,
\qquad
\dot y=y\left[-n+\varepsilon(c+ey)x\right],
\]
assume all ecological parameters are positive and \(e>0\). Every nonconstant periodic orbit \(\Gamma\subset(0,\infty)^2\), with enclosed Jordan domain \(D\), obeys
\[
\frac{1}{|D|}\iint_D\frac{1}{y}\,dx\,dy=\frac{\varepsilon e}{b}.
\]
Thus the area harmonic mean of predator density over the region enclosed by the cycle is
\[
H_D(y):=\frac{|D|}{\iint_D y^{-1}\,dx\,dy}=\frac{b}{\varepsilon e}.
\]
In particular every positive periodic orbit strictly crosses the horizontal line
\[
y_H=\frac{b}{\varepsilon e},
\qquad
\min_\Gamma y<y_H<\max_\Gamma y.
\]
At every positive equilibrium the source's exact Jacobian trace is
\[
\operatorname{tr}J=\bar x(\varepsilon e\bar y-b),
\]
so the trace-zero condition required for a Hopf bifurcation is precisely \(\bar y=y_H\). The same parameter-only level therefore governs both the local Hopf condition and a global finite-amplitude geometric constraint on every positive limit cycle.

## Assumptions and scope
The statement concerns the autonomous two-dimensional system above on the positive quadrant. Parameters \(r,a,b,c,e,\varepsilon,s_1,s_2,n\) are positive and \(e>0\). A “positive periodic orbit” means a nonconstant periodic trajectory contained in \((0,\infty)^2\). By uniqueness for the smooth vector field, its image is a simple closed curve; \(D\) denotes its bounded Jordan interior. Because the curve is compact in the positive quadrant, its convex hull, and hence \(D\), also lies in the positive quadrant.

The conclusion is necessary, not sufficient: it neither proves that a cycle exists nor determines its number, stability, period, or detailed shape. It applies equally to stable and unstable positive cycles.

## Proof
Set
\[
B(x,y)=\frac{1}{xy}.
\]
For the displayed vector field \(F=(F_1,F_2)\), direct differentiation gives
\[
\frac{\partial(BF_1)}{\partial x}=-\frac{b}{y},
\qquad
\frac{\partial(BF_2)}{\partial y}=\varepsilon e,
\]
and therefore
\[
\nabla\!\cdot(BF)=\varepsilon e-\frac{b}{y}.
\]
Along a periodic trajectory \(\Gamma\), the vector field \(F\) is tangent to \(\Gamma\), and multiplication by the scalar \(B\) preserves tangency. Hence the outward normal flux of \(BF\) through \(\Gamma\) is zero. Green's theorem yields
\[
0=\oint_\Gamma BF\cdot n\,ds
 =\iint_D\left(\varepsilon e-\frac{b}{y}\right)dx\,dy.
\]
Rearranging gives
\[
\varepsilon e|D|=b\iint_D\frac{1}{y}\,dx\,dy,
\]
which is exactly the asserted area-harmonic-mean identity.

The function \(y\mapsto\varepsilon e-b/y\) is strictly increasing on \((0,\infty)\) and has its unique zero at \(y_H=b/(\varepsilon e)\). If the entire cycle lay in \(y\ge y_H\), then its Jordan interior would also lie in that half-plane, and the integrand would be nonnegative and positive on an open subset, contradicting its zero integral. The same argument excludes a cycle entirely in \(y\le y_H\). Thus the crossing inequalities are strict.

Finally, the source computes for a positive equilibrium \((\bar x,\bar y)\)
\[
\operatorname{tr}J=\bar x(-b+e\varepsilon\bar y).
\]
Since \(\bar x>0\), trace zero is equivalent to \(\bar y=b/(\varepsilon e)=y_H\), proving the local/global threshold coincidence.

## Verification
The proof is symbolic and requires no orbit integration or finite enumeration. The key differentiation can be replayed directly from the two displayed equations: after multiplying by \(B=1/(xy)\), only the term \(-bx/y\) contributes to the \(x\)-derivative and only the term \(\varepsilon ey\) contributes to the \(y\)-derivative, giving \(-b/y+\varepsilon e\).

For the parameter set in the source's Example 4.1, \(b=0.9\) and \(\varepsilon=0.4\). The threshold is therefore \(y_H=2.25\) when \(e=1\) and \(y_H=0.45\) when \(e=5\). The paper's phase portraits display periodic oscillations in both cooperative-hunting regimes; these examples are illustrative only and are not used in the proof.

## Relationship to prior work
Xue, Chen, Xie, and Chen introduce the displayed model and, in the no-cooperation case \(e=0\), use the same Dulac weight \(B=1/(xy)\) to obtain the sign-definite weighted divergence \(-b/y\), excluding closed orbits. In the cooperative case they separately derive the equilibrium trace \(\bar x(\varepsilon e\bar y-b)\), formulate the Hopf condition through \(g(\bar y)=\varepsilon e\bar y-b\), and exhibit finite-amplitude periodic behavior numerically. They do not state the Green-theorem area identity above or its consequence that every positive cycle must cross the same trace-zero level.

Related fear/cooperation and cooperative-hunting predator–prey papers study different vector fields. In particular, Pal et al. analyze a modified Leslie–Gower model, while Bai and Tang give a global classification for another cooperative-hunting model. Those systems do not imply the stated identity for the Xue–Chen–Xie–Chen vector field.

## Limitations
The result is restricted to periodic orbits wholly inside the positive quadrant and to \(e>0\). It does not classify all recurrent invariant sets and does not establish existence, uniqueness, or stability of a periodic orbit. The identity is exact for the printed differential equations; biological conclusions remain conditional on that model.

The literature comparison found no statement implying this exact finite-amplitude identity. A closely related 2019 fear/cooperation paper was available through repository and bibliographic abstracts, but its full-text repository download was inaccessible during checking; because it concerns a different Leslie–Gower system, this remains a non-decisive residual literature risk rather than evidence of coverage.

## References
1. Y. Xue, F. Chen, X. Xie, S. Chen, “An analysis of a predator-prey model in which fear reduces prey birth and death rates,” *AIMS Mathematics* 9(5), 12906–12927 (2024). DOI: 10.3934/math.2024630.
2. S. Pal, N. Pal, S. Samanta, J. Chattopadhyay, “Fear effect in prey and hunting cooperation among predators in a Leslie-Gower model,” *Mathematical Biosciences and Engineering* 16(5), 5146–5179 (2019). DOI: 10.3934/mbe.2019258.
3. D. Bai, J. Tang, “Global Dynamics of a Predator–Prey System with Cooperative Hunting,” *Applied Sciences* 13(14), 8178 (2023). DOI: 10.3390/app13148178.
