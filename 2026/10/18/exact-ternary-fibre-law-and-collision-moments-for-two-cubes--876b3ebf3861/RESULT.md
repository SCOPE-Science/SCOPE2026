# Exact ternary fibre law and collision moments for two cubes

## Finding

For each integer \(n\geq0\), let \(R_n(a)\) count ordered pairs \((x,y)\) modulo \(3^n\) satisfying \(x^3+y^3\equiv a\pmod{3^n}\), and set \(F_n(a)=3^{-n}R_n(a)\), with \(F_0(0)=1\). Define the periodic function \(h\) modulo nine by
\[
h(a)=\begin{cases}2,&a\equiv0,1,8\pmod9,\\1,&a\equiv2,7\pmod9,\\0,&a\equiv3,4,5,6\pmod9.\end{cases}
\]
Then the representation count of **every** residue at **every** depth is given by
\[
F_1(a)=1,\qquad F_2(a)=h(a)+\mathbf1_{a\equiv0\pmod9},
\]
and, for all integers \(n\geq3\) and \(a\bmod3^n\),
\[
\boxed{F_n(a)=h(a)+3\,\mathbf1_{a\equiv0\pmod{27}}F_{n-3}(a/27).}
\]
The last quotient is evaluated modulo \(3^{n-3}\) only when the indicator is one.

For the normalized ordered collision count
\[
M_n=3^{-3n}\#\{(x,y,u,v)\bmod3^n:x^3+y^3\equiv u^3+v^3\pmod{3^n}\}
=3^{-n}\sum_{a\bmod3^n}F_n(a)^2,
\]
put \((M_0,M_1,M_2)=(1,1,19/9)\). For every \(n\geq3\),
\[
\boxed{M_n=2+\frac13M_{n-3};\qquad M_{3k+r}=3+3^{-k}(M_r-3),\quad r\in\{0,1,2\}.}
\]
In particular, \(\lim_{n\to\infty}M_n=3\).

There is an absolutely continuous pushforward law for \(X^3+Y^3\), where \(X,Y\) are independent normalized Haar-uniform elements of \(\mathbb Z_3\). Its density \(F\) is finite at every nonzero target, infinite only at target zero, and satisfies
\[
F(t)=h(t)+3\mathbf1_{t\in27\mathbb Z_3}F(t/27)\quad(t\ne0).
\]
The density is positive exactly when \(t\bmod9\in\{0,1,2,7,8\}\), a set of Haar measure \(5/9\). Its first two moments and sharp integrability boundary are
\[
\boxed{\int_{\mathbb Z_3}F(t)\,dt=1,\qquad\int_{\mathbb Z_3}F(t)^2\,dt=3,\qquad F\in L^s(\mathbb Z_3)\iff0<s<3.}
\]
Consequently \(\operatorname{Var}(F)=2\), whereas the cubic and all higher moments diverge. Moreover \(F_n\to F\) almost everywhere and in \(L^s\) for every \(0<s<3\).

## Assumptions and scope

All variables in the finite congruences range independently over complete residue systems. The convention for modulus one is \(R_0(0)=1\). For \(n\ge1\), \(F_n(a)\) is the number of ordered solutions divided by \(3^n\); it is also the density of the probability of a target congruence on that residue class relative to normalized Haar measure. The Haar measure on \(\mathbb Z_3\) gives mass \(3^{-n}\) to each residue cylinder modulo \(3^n\). The claims concern local integer residues and 3-adic integers; they do not imply global positive-integer representation formulae. The density is defined up to a Haar-null set, and its value at zero is assigned \(+\infty\) by its recursive expression.

## Proof

**1. Distribution of one unit cube.** For \(t\in\mathbb Z_3\),
\[
(1+3t)^3=1+9(t+3t^2+3t^3).
\]
The polynomial \(t+3t^2+3t^3\) is congruent to \(t\pmod3\) and has derivative \(1+6t+9t^2\equiv1\pmod3\). Hensel's lemma therefore gives precisely one solution in \(\mathbb Z_3\) of \(t+3t^2+3t^3=b\) for every \(b\in\mathbb Z_3\). Thus cubing is a measure-preserving bijection, after the natural factor-of-three rescaling, from \(1+3\mathbb Z_3\) to \(1+9\mathbb Z_3\). Replacing \(1\) by \(-1\) gives the corresponding assertion for \(-1+3\mathbb Z_3\). A Haar-uniform input therefore produces a uniform cube in \(1+9\mathbb Z_3\) with probability \(1/3\), a uniform cube in \(-1+9\mathbb Z_3\) with probability \(1/3\), or a cube divisible by \(27\) with probability \(1/3\). Conditional on the last alternative, the cube is \(27Z^3\) for Haar-uniform \(Z\in\mathbb Z_3\).

**2. Five disjoint output classes and the singular branch.** When both inputs are units, their signs modulo three are independent. Matching signs give output uniformly distributed on \(\pm2+9\mathbb Z_3\), each with probability \(1/9\); opposite signs give output uniformly distributed on \(9\mathbb Z_3\) with probability \(2/9\). If precisely one input is a unit, its sign gives output uniform on \(\pm1+9\mathbb Z_3\), each with probability \(2/9\). If both inputs are multiples of three (probability \(1/9\)), the output is \(27(Z_1^3+Z_2^3)\). A coset of \(9\mathbb Z_3\) has measure \(1/9\), and a coset of \(27\mathbb Z_3\) has measure \(1/27\). Hence the nonsingular contributions have density \(h\), while the last contribution has density \(3F(t/27)\) on \(27\mathbb Z_3\). This establishes the pushforward measure identity and its recursion.

Reducing this exact measure identity modulo \(3^n\) proves the finite recurrence for \(n\ge3\). Modulo three the map \(z\mapsto z^3\) equals \(z\), so \(F_1\equiv1\). Modulo nine the both-nonunits contribution is concentrated at zero and adds density one there, which gives the stated \(F_2\). All finite claims follow without extrapolation.

**3. Collision identity.** In the average over target residues, \(\mathbb E h^2=14/9\), since its squared values sum to \(14\) over the nine classes. On the divisible-by-\(27\) branch, \(h=2\), and \(\mathbb E F_{n-3}=1\) by counting all input pairs. Thus, for \(n\ge3\), expanding the square of the finite recurrence gives
\[
M_n=\frac{14}{9}+\frac{2\cdot2\cdot3}{27}\cdot1+\frac{9}{27}M_{n-3}
=2+\frac13M_{n-3}.
\]
Directly, \(M_0=M_1=1\); modulo nine, the nonzero values of \(F_2\) are \(3,2,2,1,1\), so \(M_2=(9+4+4+1+1)/9=19/9\). Iterating the recurrence gives the closed form and limit \(3\).

**4. Existence, support and sharp moments.** Iterating the measure identity produces a nonnegative density, for \(t\ne0\),
\[
F(t)=\sum_{j\ge0}3^j\mathbf1_{t\in27^j\mathbb Z_3}\,h(t/27^j),
\]
with only finitely many nonzero terms. Its integral is
\[
\sum_{j\ge0}3^j27^{-j}\int h=\frac89\sum_{j\ge0}9^{-j}=1.
\]
Thus no residual singular mass is omitted. Since \(h(t)>0\) on \(\{0,1,2,7,8\}\pmod9\), and \(h=0\) elsewhere with no recursive branch except at zero modulo nine, the support has measure \(5/9\) and is exactly the stated congruence set.

For \(t\ne0\), write \(k\) for the largest nonnegative integer with \(27^k\mid t\). Since \(0\le h\le2\), \(F(t)\le2\sum_{j=0}^k3^j=3^{k+1}-1\). The mass of \(27^k\mathbb Z_3\) is \(27^{-k}\), so \(F\in L^s\) for \(0<s<3\). Conversely, on every disjoint annulus \(27^k(9\mathbb Z_3\setminus27\mathbb Z_3)\), of measure \(2\cdot27^{-(k+1)}\), one has exactly \(F=3^{k+1}-1\). Their contributions to \(\int F^s\) diverge when \(s\ge3\). This also shows \(F(0)=+\infty\) is the natural limiting assignment.

The functions \(F_n\), considered as functions on \(\mathbb Z_3\) constant on cylinders, are conditional expectations of this integrable density under the increasing residue sigma-algebras. Martingale convergence gives almost-everywhere and \(L^1\) convergence. Since the stated finite recurrence and Minkowski's inequality give \(\|F_n\|_s\le\|h\|_s+3\cdot27^{-1/s}\|F_{n-3}\|_s\) for every \(1<s<3\), their \(L^s\) norms are uniformly bounded. Applying the \(L^s\) martingale convergence theorem, then the elementary embedding for smaller exponents on a probability space, proves \(L^s\) convergence throughout \(0<s<3\). In particular the second moments converge to three.

## Verification

The accompanying `verify.py` independently enumerates all cube residue multiplicities and exact ordered convolutions through modulus \(3^8\), compares every residue against the recurrence, and checks the rational collision values. It additionally checks the purely recursive identities through depth eleven. This is a finite consistency check; the infinite statements rest on Steps 1–4. Run `python3 verify.py` from the directory containing this file and the verifier; no external packages are required.

## Relationship to prior work

Brüdern and Vaughan study variance in arithmetic progressions for positive sums of two cubes and use the local congruence count \(\rho(q,a)\) in their analytic arguments. Their 2021 article does not present the exact target-by-target ternary prime-power recurrence or the limiting fibre-integrability law above. Seraj determines counts of **single** power residues modulo prime powers; those counts do not imply the ordered additive fibre multiplicities without further convolution and singular-branch analysis. Bories develops formulas for Igusa-type local zeta functions under Newton nondegeneracy hypotheses; the polynomial \(x^3+y^3\) is singular on the nonzero torus in residue characteristic three (its two partial derivatives vanish identically modulo three), so this formula cannot be directly applied at the exceptional prime. The elementary residue-support obstruction modulo nine is classical and is not claimed as a discovery.

## Limitations

The claimed new component is the assembled exact all-depth ternary fibre formula, rational collision recurrence and its sharp limiting moment law. The basic cube-residue facts and the modulo-nine obstruction are prior elementary knowledge. A more general theorem or older specialized computation could implicitly contain the exact result; independent priority has not been established. This analysis concerns ordered local residue solutions only and makes no claim about global integer solutions, singular-series convergence in an independent global problem, or external validation.

## References

1. J. Brüdern and R. C. Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes*, European Journal of Mathematics 7 (2021), 1616–1644, doi:10.1007/s40879-021-00495-4. First publicly verified appearance used here: 2021-09-20, open full article: https://link.springer.com/article/10.1007/s40879-021-00495-4.
2. S. Seraj, *Counting general power residues*, Notes on Number Theory and Discrete Mathematics 28 (2022), 730–743, doi:10.7546/nntdm.2022.28.4.730-743. https://nntdm.net/papers/nntdm-28/NNTDM-28-4-730-743.pdf.
3. B. Bories, *Igusa's p-adic local zeta function associated to a polynomial mapping and a polynomial integration measure*, arXiv:1012.5087, https://arxiv.org/abs/1012.5087. The relevant nondegeneracy condition is Definition 1.4.
