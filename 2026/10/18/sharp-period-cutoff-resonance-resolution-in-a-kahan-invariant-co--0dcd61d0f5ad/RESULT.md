# Sharp period-cutoff resonance resolution in a Kahan invariant-conic pencil

## Finding

The prime-period cutoff for the elliptic invariant conics of a concrete Kahan–Hirota–Kimura discretization has an **exact sharp energy-resolution threshold**. Although these periodic conics are dense, their closest pair among all prime periods at most \(P\) is uniquely the pair of period \(P\) and \(P-1\) closest to the parabolic level. The energy gap decreases as \(P^{-3}\), while the number of distinct eligible conics grows as \(P^2\). A quantitative limiting energy distribution additionally exhibits an integrable square-root concentration at the parabolic boundary.

**Theorem.** Fix \(0<\epsilon<1\) and put \(a_\epsilon=\pi^{-1}\arctan(\epsilon)\). Let \(\mathcal E_P\) denote the distinct energies of elliptic invariant conics filled by orbits of *prime period at most* the positive integer \(P\). Then

\[
\mathcal E_P=\left\{-2-\frac{\tan^2(\pi k/p)}{2\epsilon^2}:1\leq k<p\leq P,\ \gcd(k,p)=1,\ 0<k/p<a_\epsilon\right\}.
\]

Whenever \(1/(P-1)<a_\epsilon\), the set has at least two elements, and its **unique closest unordered pair** is the pair indexed by the reduced fractions \(1/P\) and \(1/(P-1)\). The exact minimum energy gap and its asymptotic are

\[
\Delta_P=\frac{\tan^2(\pi/(P-1))-\tan^2(\pi/P)}{2\epsilon^2}
=\frac{\pi^2}{\epsilon^2P^3}\bigl(1+O(P^{-1})\bigr).
\]

The number of eligible conics satisfies

\[
N_P=|\mathcal E_P|=\frac{3a_\epsilon}{\pi^2}P^2+O(P\log P).
\]

Their equally weighted empirical **energy** measures converge on \((-5/2,-2)\) to a probability law with density

\[
w_\epsilon(h)=\frac{\epsilon}{\arctan(\epsilon)\sqrt{-4-2h}\left[1+\epsilon^2(-4-2h)\right]}.
\]

For every energy interval, the empirical probability differs from that predicted by the density by \(O_\epsilon(\log P/P)\). More explicitly, for every \(0<\delta<1/2\), the limiting share of conics within energy distance \(\delta\) below the parabolic level \(-2\) equals

\[
\frac{\arctan(\epsilon\sqrt{2\delta})}{\arctan(\epsilon)}.
\]

## Assumptions and scope

The original quadratic differential equation is

\[
\dot x=x(x+y-2),\qquad \dot y=-x(2x+y-3).
\]

Its Kahan map with step parameter \(0<\epsilon<1\) is the rational map \(\Phi_\epsilon=(A/D,B/D)\), where

\[
\begin{aligned}
A={}&\epsilon(\epsilon+1)x^2+\epsilon xy+(1-2\epsilon)x,\\
B={}&\epsilon(2\epsilon-4)x^2-\epsilon(\epsilon+3)xy+6\epsilon x-\epsilon y^2+(2\epsilon+1)y,\\
D={}&2\epsilon^2x^2-\epsilon(\epsilon+1)x-\epsilon y+2\epsilon+1.
\end{aligned}
\]

By the primary reference, this map preserves the first integral

\[
V(x,y)=-\frac{(5\epsilon^2-2)x^2-2xy-y^2+6x+4y}{2\epsilon^2x^2+2}.
\]

Its level conics \(C_h=\{V=h\}\) are ellipses in the **entire** specified range \(-5/2<h<-2\), because the quadratic form has determinant \(1-\epsilon^2(5+2h)>0\). The primary reference proves that the restriction of the map to each such ellipse is conjugate to a rigid circle rotation. The theorem concerns each invariant ellipse as one geometric object; it does not count its infinitely many periodic points separately. Prime period means the least positive iterate returning every point on that ellipse to itself.

## Proof

**1. Rotation defect and exact energy parametrization.** Proposition 3 and Equation (9) of Mañosa–Pantazi give the rotation number in terms of the unit complex multiplier

\[
\xi=\frac{1-\epsilon^2u^2-2i\epsilon u}{1+\epsilon^2u^2}
=\exp[-2i\arctan(\epsilon u)],\qquad u=\sqrt{-4-2h}\in(0,1).
\]

Here the principal argument is negative. Hence \(\rho_\epsilon(h)=1-\arctan(\epsilon u)/\pi\). The defect \(r=1-\rho_\epsilon(h)\) traverses \((0,a_\epsilon)\) bijectively as the energy traverses \((-2,-5/2)\). Solving for energy yields

\[
h(r)=-2-\frac{\tan^2(\pi r)}{2\epsilon^2}.
\]

The source establishes conjugacy to rotation, so every point on the ellipse has prime period \(p\) exactly when \(r=k/p\) in lowest terms. This proves the parametrization and injectivity of \(\mathcal E_P\).

**2. Exact minimum separation and uniqueness.** Put \(g(r)=\tan^2(\pi r)/(2\epsilon^2)\). On \((0,a_\epsilon)\), \(g\) is strictly increasing and strictly convex (its second derivative is positive). Let \(r=k/p<s=l/q\) be any distinct eligible reduced fractions with \(p,q\leq P\). The smallest possible positive numerator is \(l p-k q\geq1\). If \(p\ne q\), then \(pq\leq P(P-1)\), giving \(s-r\geq1/[P(P-1)]\). If \(p=q\), the gap is at least \(1/p\), which also exceeds this lower bound. Also \(r\geq1/P\). Strict convexity and monotonicity therefore imply

\[
\begin{aligned}
g(s)-g(r)&\geq g\left(r+\frac1{P(P-1)}\right)-g(r)\\
&\geq g\left(\frac1P+\frac1{P(P-1)}\right)-g\left(\frac1P\right)\\
&=g\left(\frac1{P-1}\right)-g\left(\frac1P\right).
\end{aligned}
\]

The assumed inequality \(1/(P-1)<a_\epsilon\) ensures both endpoints occur among the eligible fractions. Equality in the second inequality requires \(r=1/P\), and equality in the first requires \(s=1/(P-1)\), so the minimizing pair is unique. Taylor expansion of \(\tan^2 z=z^2+O(z^4)\) at zero yields the stated asymptotic with its exact leading constant.

**3. A uniform rational-resonance counting estimate.** For every \(0\le t\le a_\epsilon\), let \(F_P(t)\) count reduced fractions \(k/p\) with \(p\le P\) and \(0<k/p<t\). Möbius inversion gives

\[
\begin{aligned}
F_P(t)&=\sum_{d\le P}\mu(d)\sum_{m\le P/d}\#\{j\in\mathbb Z:1\le j<tm\}\\
&=\frac{tP^2}{2}\sum_{d\le P}\frac{\mu(d)}{d^2}+O(P\log P)\\
&=\frac{3t}{\pi^2}P^2+O(P\log P).
\end{aligned}
\]

The error is uniform in \(t\), because the inner integer count differs from \(tm\) by at most one; truncating the absolutely convergent Möbius Dirichlet series contributes \(O(P)\). Taking \(t=a_\epsilon\) proves the cardinality formula (with possible strict-endpoint changes bounded by \(O(P)\)). Applying the estimate to subintervals and dividing by \(N_P\) establishes the normalized discrepancy \(O_\epsilon(\log P/P)\) and uniform limiting distribution in the rotation defect \(r\in(0,a_\epsilon)\).

**4. Pushforward to energy.** The energy map \(h(r)\) is strictly decreasing, and its inverse is

\[
r(h)=\frac1\pi\arctan\left(\epsilon\sqrt{-4-2h}\right).
\]

Pushing normalized Lebesgue measure \(dr/a_\epsilon\) forward by \(h(r)\) gives \(w_\epsilon(h)=|r'(h)|/a_\epsilon\), precisely the stated density. Its integral is one. The energy band \((-2-\delta,-2)\) corresponds to \(0<r<\arctan(\epsilon\sqrt{2\delta})/\pi\), giving the endpoint concentration formula. The density grows as a constant times \((-2-h)^{-1/2}\) near the upper energy edge, but is integrable.

## Verification

The accompanying standalone standard-library script `verify.py` checks exact rational preservation of the first integral for multiple rational map inputs, finite censuses of reduced resonances across four step sizes and six period cutoffs, the predicted unique closest pair and its exact gap, large-cutoff count estimates, and density/band identities. It reports its finite assertion count on success. These tests corroborate the formulas; the general statements are proved by the four preceding arguments, not by enumeration.

Run: `python3 verify.py`.

## Relationship to prior work

Mañosa and Pantazi, arXiv:2603.23382v1, Section 3.1 and Proposition 3, establish the invariant conic family, the explicit rotation number and the rational/irrational dichotomy. Their Corollary 5 proves density of periodic conics, and Proposition 6 shows that sufficiently large prime periods occur. Those fundamental geometric and qualitative conclusions are **not** new here. The additional statements proved above determine how many conics survive a prime-period cutoff, their **exact nearest energy spacing**, and the limiting energy distribution.

Llorens and Mañosa, arXiv:1502.03737, establish general genus-zero Möbius conjugacy and rotation-number methods for rational invariant fibrations; these do not themselves supply the sharp energy-gap or period-capped distribution for the specific Kahan pencil. Petrera and Suris, arXiv:1811.05791, study the geometric conic-pencil structure for related discretizations. The minimum-spacing argument uses standard reduced-fraction arithmetic; no new general theorem about Farey fractions is asserted.

## Limitations

The energy difference is measured in the specified conserved integral \(V\), **not** a metric distance between embedded ellipses. The cutoff is on **prime** periods, not total orbit counts or continuous time. The constants implicit in counting/discrepancy depend on the fixed step parameter where indicated. Uniform statements as \(\epsilon\to0\), persistence under nonintegrable perturbations, and observability in floating-point computations are not proved. The displayed result is a mathematical extension of an explicit prior rotation formula; a full independent bibliographic priority determination has not been completed.

## References

1. V. Mañosa and C. Pantazi, *Dynamics of Kahan-Hirota-Kimura maps with rational invariant fibrations*, arXiv:2603.23382v1, 24 March 2026, especially Section 3 and Propositions 3 and 6. https://arxiv.org/html/2603.23382v1
2. M. Llorens and V. Mañosa, *Lie Symmetries of Birational Maps Preserving Genus 0 Fibrations*, arXiv:1502.03737, 2015. https://arxiv.org/abs/1502.03737
3. M. Petrera and Y. B. Suris, *Geometry of the Kahan discretizations of planar quadratic Hamiltonian systems. II. Systems with a linear Poisson tensor*, arXiv:1811.05791, 2018 / J. Comput. Dyn. 6 (2019), 401–408. https://arxiv.org/abs/1811.05791
