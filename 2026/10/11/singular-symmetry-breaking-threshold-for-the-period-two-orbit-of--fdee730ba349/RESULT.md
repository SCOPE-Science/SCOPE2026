# Singular symmetry-breaking threshold for the period-two orbit of a replicator map

## Finding

**Theorem (unique nearby-asymmetric multiplier crossing and its scale).** Consider the two-parameter interval map
\[
f_{a,b}(x)=\frac{x}{x+(1-x)\exp(a(x-b))},\qquad 0\le x\le1,
\]
with \(a>0\) and \(0<b<1\). Write \(b=\frac12-\delta\), with \(0<\delta<\delta_0\), where \(\delta_0>0\) is a sufficiently small universal constant. Define the known fixed-point flip threshold
\[
a_0(b)=\frac{2}{b(1-b)}.
\]
For every \(a>a_0(b)\), there is exactly one primitive period-two orbit \(\{x(a),y(a)\}\) with \(0<x(a)<b<y(a)<1\). Its multiplier \(\Lambda(a,\delta)=(f_{a,b}^{2})'(x(a))\) is strictly less than \(1\) for every such \(a\).

There exists exactly one \(a_*(\delta)>a_0(b)\) at which \(\Lambda=-1\). The orbit is hyperbolically attracting for \(a_0(b)<a<a_*(\delta)\), nonhyperbolic with multiplier \(-1\) at \(a=a_*(\delta)\), and hyperbolically repelling for \(a>a_*(\delta)\). Moreover \(\partial_a\Lambda(a_*(\delta),\delta)<0\), and
\[
\boxed{\quad a_*(\delta)=\frac{1}{\delta(1-2\delta)}
+O\!\left(\delta^{-2}\exp\left(-\frac{1}{20\delta}\right)\right),\quad\delta\downarrow0.\quad}
\]
In particular \(\delta a_*(\delta)\to1\) and \(a_*(\delta)=\delta^{-1}+2+O(\delta)\). Reflection \(x\mapsto1-x\) gives the identical conclusions for \(b=\frac12+\delta\). At exact symmetry \(b=\frac12\), in contrast, the period-two orbit is hyperbolically attracting for every \(a>8\): no finite crossing occurs.

The result is a **local linear stability classification of the particular period-two orbit**, not a complete description of all coexisting attractors or a proof that a stable four-cycle is born at the neutral crossing.

## Assumptions and scope

All parameters and states are real. For the asymmetric theorem, \(0<\delta<\delta_0\), \(b=\frac12-\delta\), and \(a>a_0(b)\). The constant \(\delta_0\) is existential: the proof gives uniform small-asymmetry estimates, not a numerical optimal value. The term \(O(\cdot)\) is uniform in \(\delta\) sufficiently near zero. The local stability claims refer to iteration of \(f_{a,b}\) within its open invariant interval \((0,1)\); at multiplier \(-1\) no attraction or nonlinear period-doubling direction is claimed.

For convenient notation put
\[
h(t)=\log\frac{1-t}{t},\qquad q(t)=t(1-t),\qquad g(t)=\frac1{q(t)}.
\]
Here \(h'(t)=-g(t)\) and \(g''(t)=2/t^3+2/(1-t)^3>0\) on \((0,1)\).

## Proof

**1. Exact cycle parametrization.** Direct algebra gives the cohomological identity
\[
h(f_{a,b}(t))-h(t)=a(t-b).
\]
Summing over a two-cycle \(x\mapsto y\mapsto x\) yields \(x+y=2b\). In the ordered case \(x<y\), write \(x=b-u\), \(y=b+u\), where \(0<u<\min\{b,1-b\}\). The first cycle equation is equivalent to
\[
a=A_b(u):=\frac{h(b-u)-h(b+u)}{u}
=\frac2u\left[\operatorname{artanh}\frac{u}{b}+\operatorname{artanh}\frac{u}{1-b}\right].
\]
The power series \(\operatorname{artanh}(z)/z=\sum_{j\ge0}z^{2j}/(2j+1)\) shows that \(A_b\) is strictly increasing, with \(A_b(0+)=2/[b(1-b)]\) and \(A_b(u)\to\infty\) at the right endpoint. Hence every \(a>a_0(b)\) has one and only one nontrivial two-cycle; the second cycle equation follows from \(x+y=2b\). This reproduces a known existence-and-uniqueness conclusion independently, solely to fix the later parameterization.

**2. A global upper bound for the multiplier.** Differentiation gives
\[
f_{a,b}'(t)=\frac{q(f_{a,b}(t))}{q(t)}\bigl(1-aq(t)\bigr).
\]
The two \(q\)-ratios cancel around a cycle, giving the exact identity
\[
\Lambda(a,b)=\bigl(1-aq(x)\bigr)\bigl(1-aq(y)\bigr).
\]
Since \(a=[\int_x^y g(t)\,dt]/[(y-x)/2]\), strict convexity of \(g\) and the trapezoid inequality yield \(a<g(x)+g(y)\). Thus
\[
1-\Lambda=a\bigl[q(x)+q(y)-a q(x)q(y)\bigr]>0.
\]
Consequently, \(\Lambda<1\) along **every** nontrivial two-cycle. In particular the only possible linear-stability exit is through \(-1\).

**3. Uniform small-lower-endpoint control.** By reflection, analyze only \(b=\frac12-\delta\) with small positive \(\delta\), so that \(\frac{9}{20}\le b<\frac12\). Write \(x=x(a,\delta)\), \(y=2b-x=1-2\delta-x\). The exact cycle equation is
\[
\exp\bigl(a(b-x)\bigr)=\frac{(1-x)(2b-x)}{x(2\delta+x)}\le\frac1{x^2}.
\]
The monotone parametrization in Step 1 shows that a universal \(A\) can be chosen so that \(x\le b/2\) for every \(a\ge A\) and all \(b\in[9/20,1/2]\): indeed \(\max_b A_b(b/2)<\infty\). Hence, after increasing \(A\) if necessary,
\[
0<x(a,\delta)\le \exp(-ab/4)\le\exp(-a/10),
\qquad a\ge A.
\]
Choose \(A\) also so large that \(a\exp(-a/10)<1/4\) for all \(a\ge A\). For sufficiently small \(\delta\), also impose \(1/(2\delta)\ge A\) and \(\exp[-1/(20\delta)]<\delta\), so \(x\le\delta\) on \(a\ge1/(2\delta)\).

**4. There is no earlier loss of stability.** On each fixed compact parameter interval \(a\in[a_0(b),A]\), the cycle and its multiplier extend continuously through the flip limit \(a=a_0(b)\). At \(b=1/2\), the period-two multiplier is a nonnegative square (and equals \(1\) at the flip endpoint), so uniform continuity gives \(\Lambda>-1\) on this entire compact interval for sufficiently small \(\delta\).

For \(A\le a\le1/(2\delta)\), use \(q(x)\le x\) and \(q(y)\le1-y=2\delta+x\). The nonnegative quadratic contribution in Step 2 yields
\[
\Lambda\ge1-a\bigl[q(x)+q(y)\bigr]
\ge1-2a(\delta+x)>-\tfrac12.
\]
The last inequality uses \(2a\delta\le1\) and \(2ax<1/2\). Thus \(\Lambda>-1\) for all \(a\le1/(2\delta)\) for sufficiently small \(\delta\), including both junctions.

**5. Exactly one transverse loss thereafter.** Differentiate the exact cycle equation \(a(b-x)=h(x)-h(2b-x)\) with respect to \(a\). This gives
\[
\frac{dx}{da}=-\frac{b-x}{g(x)+g(y)-a}.
\]
Strict convexity already proved the denominator positive. For \(a\ge1/(2\delta)\), the bounds in Step 3 imply \(g(x)+g(y)-a\ge1/x-a\ge1/(2x)\), hence \(0<-dx/da\le2bx\le x\).

Since \(q(x)=O(x)\),
\[
q(y)=2\delta(1-2\delta)+O(x),
\]
and \(|dx/da|\le x\), expansion and differentiation of the exact multiplier give, uniformly for \(a\ge1/(2\delta)\),
\[
\Lambda=1-2a\delta(1-2\delta)
+O\!\left((a+a^2\delta)x\right),
\]
\[
\frac{\partial\Lambda}{\partial a}
=-2\delta(1-2\delta)
+O\!\left((1+a+a^2\delta)x\right).
\]
The implicit constants are independent of sufficiently small \(\delta\) and of this entire half-line of \(a\). Indeed the neglected \(a^2x^2\) terms are absorbed using \(x\le\delta\). Uniformly for \(a\ge1/(2\delta)\), the derivative error is bounded by a polynomial in \(\delta^{-1}\) times \(\exp[-1/(20\delta)]\), hence is \(o(\delta)\). Therefore \(\partial_a\Lambda<0\) on this half-line for all sufficiently small \(\delta\).

At \(a=1/(2\delta)\), Step 4 gives \(\Lambda>-1\). At \(a=2/\delta\), the first expansion gives \(\Lambda=1-4(1-2\delta)+o(1)<-1\). Continuity and strict decrease on the half-line, combined with Step 4, give a unique crossing \(a_*(\delta)\in(1/(2\delta),2/\delta)\) and the claimed attracting/repelling classification and transverse derivative.

**6. Sharp asymptotics and exact symmetry.** Evaluate the first expansion at \(\Lambda(a_*,\delta)=-1\). Because \(a_*\asymp\delta^{-1}\) and \(x(a_*,\delta)\le\exp[-1/(20\delta)]\), rearrangement gives
\[
a_*(\delta)=\frac1{\delta(1-2\delta)}
+O\!\left(\delta^{-2}\exp[-1/(20\delta)]\right).
\]
Its rational principal term expands as \(\delta^{-1}+2+O(\delta)\). For \(b=1/2\), \(y=1-x\), so \(\Lambda=(1-aq(x))^2\ge0\); Step 2 gives \(\Lambda<1\) for each finite \(a>8\). The conjugacy \(f_{a,1-b}(1-t)=1-f_{a,b}(t)\) transfers all conclusions to the other side of symmetry. This completes the proof.

## Verification

The included independent executable `verify.py` checks the complete cycle identities, the multiplier factorization, a sample of exact-rational polynomial identities, root brackets, direct forward-map equations, numerical attraction/repulsion signs, and finite-parameter agreement with the predicted asymptotic scale. It uses only the Python standard library and prints `VERIFY_OK; exact-rational and finite numerical checks: 421` under the tested environment. The finite checks are **not** an exhaustive proof of uniqueness, universal inequalities, or the singular limit; those follow from Steps 1–6. Floating-point limitations become severe when the small cycle coordinate is exponentially tiny; the program only compares stable quantities and uses a logarithmic coordinate to avoid underflow.

To replay: run `python3 verify.py` in the directory containing this document and the program. The included program is the exact one reviewed with the scientific claim.

## Relationship to prior work

Kryzhevich, Zhang, and Chmara (2024), arXiv:2412.16379v1, introduced the exact notation and study the two-cycle, record its known uniqueness and near-flip stability (Sec. 3.2–3.3), and demonstrate the special attracting regime for \(b=1/2\) (Sec. 3.1). They do **not** establish the unique near-symmetry multiplier crossing or its \(\delta^{-1}+2\) asymptotic. The more general published invariant-set and chaotic-dynamics results there do not imply a unique crossing as a function of \(a\).

Kryzhevich, Avrutin, and Söderbacka (2021), arXiv:2108.06739v3, analyze the smoothly conjugate sigmoid recurrence and prove two-cycle existence/uniqueness, with numerical parameter-plane period-doubling diagrams (Secs. 3–4). These describe the qualitative bifurcation landscape but not the stated singular asymptotic or a proof of unique crossing on an entire near-symmetric ray.

Chotibut and coauthors (2018), arXiv:1807.06831v1, establish the global simplicity of exactly symmetric dynamics and contrasting asymmetric chaos (Sec. 3). Kryzhevich and Zhang (2026), arXiv:2603.20685v1, review the replicator map in Sec. 5 and establish other statistical/chaotic results, not this threshold. The exact limit describes the scale at which the known symmetric/asymmetric dichotomy first manifests in the multiplier of the distinguished two-cycle.

## Limitations

The parameter restriction is \(0<|b-1/2|<\delta_0\), not the full asymmetric interval; \(\delta_0\) is not numerically optimized. At \(a=a_*\), multiplier \(-1\) alone does not establish the nonlinear criticality of a period-doubling bifurcation. Repelling refers to the existing period-two orbit and does not exclude coexisting stable or chaotic invariant sets; attracting refers to a neighborhood of that orbit, not a full basin classification. There has been no independent scientific audit. Literature search cannot exclude unpublished or unindexed equivalent theorems, and the established uniqueness/existence/symmetric-stability facts are explicitly prior results rather than new claims.

## References

1. S. Kryzhevich, Y. Zhang, M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379v1 (first public 2024-12-20), https://arxiv.org/html/2412.16379v1.
2. S. Kryzhevich, V. Avrutin, G. Söderbacka, *Bistability in a one-dimensional model of a two-predators-one-prey population dynamics system*, arXiv:2108.06739v3, https://arxiv.org/pdf/2108.06739.
3. T. Chotibut et al., *Family of chaotic maps from game theory*, arXiv:1807.06831v1, https://arxiv.org/html/1807.06831v1.
4. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1, https://arxiv.org/html/2603.20685v1.
