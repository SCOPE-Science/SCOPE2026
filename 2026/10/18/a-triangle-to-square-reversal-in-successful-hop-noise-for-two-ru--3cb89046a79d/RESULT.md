# A triangle-to-square reversal in successful-hop noise for two run-and-tumble particles

## Finding

Let two labeled, hard-core run-and-tumble particles occupy different sites of a periodic ring of \(n\in\{3,4\}\) vertices. Each attempts to jump one site in its current direction at rate one; the jump succeeds precisely when the target vertex is empty. Each particle independently reverses direction at rate \(a>0\). Let \(K_T\) be the total number of successful jumps by either particle up to time \(T\), started in the unique stationary distribution. Define the long-time mean rate \(\mu_n(a)=\lim_{T\to\infty}\mathbb E K_T/T\), variance rate \(\nu_n(a)=\lim_{T\to\infty}\operatorname{Var}(K_T)/T\), and Fano ratio \(F_n(a)=\nu_n(a)/\mu_n(a)\).

The exact results are
\[
\begin{aligned}
\mu_3(a)&=\frac{2a+1}{2(a+1)},&
F_3(a)&=\frac{4a^3+6a^2+5a+1}{4a(a+1)^2},\\
\mu_4(a)&=\frac{2(2a+1)^2}{6a^2+8a+3},&
F_4(a)&=\frac{40a^5+96a^4+104a^3+66a^2+22a+3}{a(6a^2+8a+3)^2}.
\end{aligned}
\]

**Noise sign changes at the first geometry admitting a nonadjacent particle pair.** On the triangle, \(F_3(a)>1\) for \(0<a<1\), \(F_3(1)=1\), and \(F_3(a)<1\) for \(a>1\). On the square, \(F_4(a)>1\) for every \(a>0\). Thus these two smallest possible hard-core rings exhibit different attainable signs of excess successful-hop counting noise.

Each Fano ratio has exactly one global minimizer at a finite positive reversal rate. The triangle's minimizing rate \(a_3\) is the unique positive zero of
\[
2a^3-4a^2-3a-1=0,
\]
while the square's minimizing rate \(a_4\) is the unique positive zero of
\[
64a^6-324a^4-432a^3-244a^2-72a-9=0.
\]
Numerically \(a_3\approx2.6399385202\), \(F_3(a_3)\approx0.9263900019\), \(a_4\approx2.8251571169\), and \(F_4(a_4)\approx1.0651120306\). Moreover, \(F_3(a)\to1\) and \(F_4(a)\to10/9\) as \(a\to\infty\), while both ratios diverge as \(a\downarrow0\).

## Assumptions and scope

The particles are distinguishable for state bookkeeping but obey identical dynamics. For \(n\in\{3,4\}\), write the relative state as \((d,u,v)\), where \(d\in\{1,\ldots,n-1\}\) is the clockwise displacement of particle two from particle one, and \(u,v\in\{-1,+1\}\) are their instantaneous directions. An orientation reversal is a genuine state transition but contributes zero to \(K_T\); a blocked attempt also contributes zero. The positive reversal rate ensures irreducibility on the finite relative-state space. The stated rates use successful jumps of either particle, not net signed displacement, the count across one selected edge, or reversal events. The stationary initial condition is convenient but does not affect long-time cumulant rates for this irreducible finite chain.

## Proof

**1. Exact reduction.** Spatial translation removes the absolute location. Reflection \((d,u,v)\mapsto(n-d,-u,-v)\) and particle exchange \((d,u,v)\mapsto(n-d,v,u)\) preserve the generator and the counted transitions. Their orbits form a strongly lumpable chain with three states for \(n=3\) and five for \(n=4\). Use the ordering obtained from orbit representatives \((1,-1,-1),(1,-1,+1),(1,+1,-1)\), and, for the square, append \((2,-1,-1),(2,-1,+1)\).

For a row generator \(Q\), let \(J\) contain only counted successful-jump off-diagonal rates, including diagonal entries when a successful jump remains inside a symmetry orbit. The tilted generator is exactly \(Q(k)=Q+(e^k-1)J\). Direct transition counting yields
\[
Q_3=\begin{pmatrix}-2a&a&a\\2a&-2a-2&2\\2a&0&-2a\end{pmatrix},\qquad
J_3=\begin{pmatrix}1&0&0\\0&0&2\\0&0&0\end{pmatrix}
\]
and
\[
Q_4=\begin{pmatrix}
-2a-1&a&a&1&0\\
2a&-2a-2&0&0&2\\
2a&0&-2a&0&0\\
2&0&0&-2a-2&2a\\
0&0&2&2a&-2a-2
\end{pmatrix},\qquad
J_4=\begin{pmatrix}
0&0&0&1&0\\
0&0&0&0&2\\
0&0&0&0&0\\
2&0&0&0&0\\
0&0&2&0&0
\end{pmatrix}.
\]
All rows of \(Q_3,Q_4\) sum to zero. Importantly, \((J_3)_{11}=1\) counts a physical jump that does not change the first orbit; omitting this term gives an incorrect triangle Fano ratio.

**2. Stationary cumulant calculation.** Let \(\pi\) be the stationary row vector, \(h=J\mathbf1\), \(\mu=\pi h\), and let \(g\) solve
\[
Qg=\mu\mathbf1-h.
\]
Differentiate the simple dominant eigenvalue of \(Q(k)\) twice at \(k=0\). This gives the exact identities
\[
\mu=\pi J\mathbf1,\qquad
\nu=\mu+2\pi Jg-2\mu\pi g.
\]
They are invariant under adding a constant to \(g\).

For the triangle, direct solution with \(g_1=0\) gives
\[
\pi_3=\left(\frac12,\frac{a}{4(a+1)},\frac{a+2}{4(a+1)}\right),\quad
g_3=\left(0,\frac{2a-1}{4a(a+1)},-\frac{2a+1}{4a(a+1)}\right)^\mathsf T.
\]
For the square put \(D=6a^2+8a+3\). Direct solution with \(g_1=0\) gives
\[
\pi_4=\frac1D\left((a+1)(2a+1),\frac{a(2a+1)}2,
\frac{(a+1)(2a+3)}2,\frac{2a^2+2a+1}2,a(a+1)\right)
\]
and
\[
g_4=\frac1D\left(0,\frac{4a^2+2a-1}{a},-
\frac{(2a+1)^2}{a},2a^2+2a+1,\frac{(a+1)(2a^2-1)}a\right)^\mathsf T.
\]
Substituting these into the two cumulant identities proves both mean and Fano formulas in the Finding for every \(a>0\).

**3. Strict Poisson-sign contrast.** Exact subtraction yields
\[
F_3(a)-1=-\frac{(a-1)(2a+1)}{4a(a+1)^2},
\]
and
\[
F_4(a)-1=\frac{(a+1)\{a^2(2a-1)^2+7a^2+10a+3\}}{a(6a^2+8a+3)^2}>0.
\]
The first identity gives the unique \(a=1\) crossing, and the second proves strict overdispersion on the square without numerical approximations.

**4. Unique finite optimizers.** Differentiation gives
\[
F_3'(a)=\frac{2a^3-4a^2-3a-1}{4a^2(a+1)^3}
\]
and
\[
F_4'(a)=\frac{64a^6-324a^4-432a^3-244a^2-72a-9}{a^2(6a^2+8a+3)^3}.
\]
Each numerator has exactly one sign change in its descending sequence of nonzero coefficients, hence exactly one positive real root by Descartes' rule together with the opposite signs at zero and infinity. The derivatives change from negative to positive at these respective roots. The explicit formulas show divergence as \(a\downarrow0\), proving that these stationary points are the unique global minima. Leading coefficients give the two stated fast-reversal limits.

## Verification

The standalone `verify_activity.py` builds both the symmetry-lumped matrices symbolically and the independent full relative-state matrices. It checks the symbolic mean and Fano formulas, the signs and derivative identities, and ten full-generator comparisons at the five exact rational rates \(a\in\{1/3,1/2,1,5/2,5\}\) for each \(n\in\{3,4\}\). Each full-generator comparison reconstructs stationary probabilities and solves a new Poisson equation. The program requires Python with SymPy as specified in `requirements.txt`; run `python verify_activity.py` from this directory. Finite samples are corroboration only; the matrix and polynomial derivations above establish the statements for all \(a>0\).

## Relationship to prior work

Slowman, Evans and Blythe obtain the stationary state of two hard-core run-and-tumble particles on a ring, including microscopic jamming and effective attraction. Mallmin, Blythe and Evans solve the un-tilted two-particle generator's spectrum and relaxation-time transitions. Chakraborty and Pradhan analyze current fluctuations and mobility, principally signed integrated transport observables and many-particle scaling. Those are substantial antecedents; none of the source portions inspected supplies the evaluated **total successful-hop counting** Fano factors, their Poisson-sign contrast between the triangle and square, or the two unique activity-noise optimizers. Exact spectral information could in principle support a subsequent derivation, and uninspected alternative counting-statistics literature might contain an equivalent result. No claim is made that the underlying model, stationary measures, general eigenvalue methods, or counting-generator differentiation are new.

## Limitations

The result classifies only the two smallest ring geometries \(n=3,4\) and exactly two hard-core walkers, with identical unit hop-attempt rates and independent symmetric positive direction-reversal rates. It does not assert that all larger rings have overdispersed total hop counts, describe full counting statistics beyond the first two cumulant rates, or establish the same behavior for other active-matter models. Independent scientific assessment and exhaustive novelty confirmation have not been performed.

## References

1. A. B. Slowman, M. R. Evans, and R. A. Blythe, *Jamming and Attraction of Interacting Run-and-Tumble Random Walkers*, arXiv:1601.00954 (first public version 2016-01-05), Phys. Rev. Lett. 116, 218101 (2016).
2. E. Mallmin, R. A. Blythe, and M. R. Evans, *Exact spectral solution of two interacting run-and-tumble particles on a ring lattice*, arXiv:1810.00813 (2018), J. Stat. Mech. 013204 (2019).
3. T. Chakraborty and P. Pradhan, *Time-dependent properties of run-and-tumble particles. II. Current fluctuations*, arXiv:2309.02896 (2023), Phys. Rev. E 109, 044135 (2024).
