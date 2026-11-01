# Sharp periodic-resonance staircase and neutral intervals in a fixed-point-free affine map

## Finding

For real parameters \(M>1\) and \(0<\alpha<1\), define the four-branch interval map \(F_{\alpha,M}:[-M,M]\to[-M,M]\) by
\[
F_{\alpha,M}(x)=
\begin{cases}
\alpha(x+1),&-M\le x\le-1,\\
M(x+1),&-1<x<0,\\
M(x-1),&0\le x<1,\\
\alpha(x-1),&1\le x\le M.
\end{cases}
\]
This map is fixed-point-free and is odd away from zero. The original four-piece family of García-Grimaldo and collaborators is recovered after rescaling the state by \(b_1/m_1\), with \(\alpha=m_1\) and \(M=m_2\).

Fix an integer \(k\ge1\). Study *strict one-inner-block cycles*, meaning periodic orbits having, in cyclic order, exactly \(k\) consecutive states in \((1,M)\), one state in \((0,1)\), \(k\) states in \((-M,-1)\), and one in \((-1,0)\). Define
\[
S_k=\sum_{j=0}^k\alpha^j,\qquad
q_k=\sum_{j=1}^{k-1}\alpha^{-j},\qquad
X_k=\frac{M S_k}{1+M\alpha^k},
\]
where \(q_1=0\). The following classification is exact.

**Theorem.** A strict one-inner-block orbit of least period \(2(k+1)\) exists if and only if
\[
\boxed{q_k<M-1.}
\]
In particular, such an orbit is possible only when \(k<M\), and for each integer \(2\le k<M\), it exists exactly when \(\alpha>r_k(M)\), where \(r_k(M)\) is the unique root in \((0,1)\) of \(q_k=M-1\). The case \(k=1\) exists for every admissible \(\alpha\).

If \(M\alpha^k\ne1\), there is exactly **one** orbit with this itinerary: it starts at \(X_k\), follows \(k\) positive outer branches and one positive inner branch to \(-X_k\), and then follows the reflected branches back. Its full-return multiplier is
\[
\boxed{\Lambda_k=(M\alpha^k)^2.}
\]
It is locally attracting for \(\alpha<M^{-1/k}\) and locally repelling for \(\alpha>M^{-1/k}\), always subject to the strict existence condition above.

If \(M\alpha^k=1\) **and** \(q_k<M-1\), instead the entire nonempty open interval
\[
\boxed{J_k=\left(M(S_k-1),\ M\right)}
\]
consists of points of **least** period \(2(k+1)\). The full-return map is exactly the identity on \(J_k\); the symmetric orbit starting at \(X_k=M S_k/2\) is just one member of this continuum. These cycles have neutral multiplier \(1\), not an attracting multiplier.

For the experimentally studied \(M=5\) map, only \(k=1,2,3,4\) can occur. The four strict existence regimes are \(k=1\) for all \(0<\alpha<1\); \(k=2\) for \(\alpha>1/4\); \(k=3\) for \(\alpha>(1+\sqrt{17})/8\); and \(k=4\) for \(\alpha>r_4\), where \(r_4\) is the unique root in \((0,1)\) of \(4\alpha^3-\alpha^2-\alpha-1=0\) (approximately \(0.8688768521\)). Among these itineraries, the *only* locally attracting cycles occur at the exact parameter windows
\[
\boxed{\text{least period }4:\quad 0<\alpha<\frac15,\qquad
\text{least period }6:\quad \frac14<\alpha<\frac1{\sqrt5}.}
\]
At \(\alpha=1/5\), every point of \((1,5)\) has least period four. At \(\alpha=1/\sqrt5\), every point of \((1+\sqrt5,5)\) has least period six. The strict period-eight and period-ten cycles exist only in repelling regimes. **This is an itinerary-restricted classification, not a classification of all periodic orbits, attractors, or chaotic parameter intervals.**

## Assumptions and scope

All parameters and the interval are real. Each itinerary state lies in the indicated **open** outer/inner cell; branch-boundary orbits, including those meeting zero, are excluded. The map is discontinuous at zero but continuous at \(\pm1\). The words “attracting” and “repelling” mean local asymptotic stability of a strict isolated periodic orbit, as determined by its return derivative. At an identity-return parameter there is a whole interval of neutral cycles, not a single isolated hyperbolic orbit. No conclusion is made about itineraries containing multiple inner visits in one half, nor about global basin coverage.

## Proof

**1. Exact half-return.** On the positive outer cell write \(g(x)=\alpha(x-1)\), and on the positive inner cell write \(h(x)=M(x-1)\). As long as the first \(k\) iterates follow the outer branch,
\[
g^k(x)=\alpha^k x-\sum_{j=1}^k\alpha^j.
\]
Therefore, the \((k+1)\)-step positive-to-negative half-return is the affine function
\[
G_k(x)=h(g^k(x))=a_kx-c_k,\qquad
a_k=M\alpha^k,\quad c_k=M S_k.
\]
On the corresponding negative itinerary, oddness gives the half-return \(y\mapsto a_ky+c_k\). The \(2(k+1)\)-step full return on the specified itinerary cylinder is consequently
\[
H_k(x)=a_k^2x+c_k(1-a_k).
\]

**2. Unique orbit away from neutrality.** If \(a_k\ne1\), the affine fixed-point equation \(H_k(x)=x\) has exactly one solution, \(X_k=c_k/(1+a_k)\). It satisfies \(G_k(X_k)=-X_k\), so the negative itinerary is its reflected positive itinerary. The final positive inner point is
\[
g^k(X_k)=1-X_k/M.
\]
Because \(0<\alpha<1\), the outer iterates decrease strictly while positive. The entire positive itinerary is strict precisely when \(1<X_k<M\). The first inequality follows from \(M>1\); the second is equivalent, by rearrangement, to
\[
\sum_{j=1}^{k-1}\alpha^j<(M-1)\alpha^k,
\]
which is \(q_k<M-1\). The negative itinerary then follows by symmetry. The orbit has least period \(2(k+1)\) because its full symbolic word contains exactly one visit to the positive inner cell. A smaller least period would divide \(2(k+1)\), and repetition of that shorter word at least twice would create two visits to the positive inner cell, a contradiction.

**3. Neutral interval and exhaustive alternative.** If \(a_k=1\), then \(G_k(x)=x-c_k\), and the negative half-return is \(y\mapsto y+c_k\). The identity \(H_k(x)=x\) holds throughout any strict itinerary cylinder. Such a cylinder exists if and only if \(q_k<M-1\). Indeed, at \(a_k=1\), the condition is equivalent to \(S_k<2\), and exactly the initial values in \(J_k=(M(S_k-1),M)=(c_k-M,M)\) produce positive outer iterates, one positive inner iterate, then a point in \(-J_k\). The negative half-trajectory then returns to the starting value. The same symbolic-word argument proves the least period. When \(q_k\ge M-1\), this open cylinder is empty. The return derivative equals \(a_k^2\), proving the stability assertions both inside and outside neutrality.

**4. Finiteness and the \(M=5\) phase chart.** For \(k\ge2\), the function \(q_k(\alpha)=\sum_{j=1}^{k-1}\alpha^{-j}\) decreases strictly from infinity as \(\alpha\downarrow0\) to \(k-1\) as \(\alpha\uparrow1\). Thus a strict solution exists for some \(\alpha\) precisely when \(k<M\), and the birth threshold is unique. At \(M=5\) only \(1\le k\le4\) remain. Direct algebra gives the thresholds stated in the theorem. For \(k=1,2\), the stability cutoffs are \(1/5\) and \(1/\sqrt5\). For \(k=3\), at the putative stability parameter \(\alpha=5^{-1/3}\),
\[
q_3=5^{1/3}+5^{2/3}>4,
\]
so the strict orbit does not yet exist; monotonicity places its actual birth after the stability cutoff. Likewise, for \(k=4\), at \(\alpha=5^{-1/4}\),
\[
q_4=5^{1/4}+5^{1/2}+5^{3/4}>4,
\]
and its birth again occurs after loss of stability. (The first inequality follows, for example, from \(5^{1/3}>8/5\); the second from \(5^{1/4}>7/5\).) Finally, at the two actual stability cutoffs the formula for \(J_k\) gives respectively \((1,5)\) and \((1+\sqrt5,5)\), completing the classification.

## Verification

The accompanying `checker.py` is standalone Python 3/SymPy code. Running `python checker.py` checks exact symbolic half-return and return identities for seven \(k\)-values, tests six exact-rational strict cycles and their multipliers in the \(M=5\) map, and checks multiple exact period-four and algebraic period-six points at the neutral parameters. It reported 63 successful checks. Finite checks do **not** establish the general theorem; its universal quantifiers follow from the algebraic proof above. No floating-point sampling is used to justify the existence or exclusion of any infinite family.

## Relationship to prior work

The four-branch fixed-point-free construction and its normalization are due to García-Grimaldo and Campos-Cantón (2021). García-Grimaldo, Bermudez-Marquez, Tlelo-Cuautle, and Campos-Cantón (2023, Section 3 and Figure 2) identify period-four behavior for \(0.1<\alpha<0.2\) and period-six behavior for \(0.25<\alpha<0.45\) from bifurcation diagrams and Lyapunov estimates. The theorem here derives an exact symbolic-itinerary criterion valid for all \(M>1\), the sharp period-four and period-six stability windows at \(M=5\), the finite cutoff for higher one-inner-block itineraries, and two explicit neutral periodic intervals. These precise claims do not follow from the paper's numerical plots. General border-collision and affine-return techniques are established tools; no novelty is claimed for those techniques.

## Limitations

The 2021 originating article and the 2022 comparative chapter could be examined only through abstract/preview material, not complete mathematical text. Their possible additional exact results therefore remain a priority risk. The result does not prove global attraction in either window, does not rule out coexisting periodic or chaotic invariant sets, and says nothing about cryptographic security. Boundaries and zero are excluded from the strict itinerary classification. No independent mathematical audit has been performed.

## References

1. C. García-Grimaldo and E. Campos-Cantón, “Chaotic Features of a Class of Discrete Maps without Fixed Points,” *International Journal of Bifurcation and Chaos* **31** (2021), 2150200. DOI: 10.1142/S021812742150200X.
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle, and E. Campos-Cantón, “FPGA Implementation of a Chaotic Map with No Fixed Point,” *Electronics* **12** (2023), 444, published January 14, 2023. DOI: 10.3390/electronics12020444. See particularly Sections 2–3 and Figure 2; open-access PDF at https://repositorio.ipicyt.edu.mx/handle/11627/6542.
3. C. García-Grimaldo and E. Campos-Cantón, “Comparative Analysis of Chaotic Features of Maps Without Fixed Points,” in *Complex Systems and Their Applications* (2022), pp. 151–176. DOI: 10.1007/978-3-031-02472-6_8.
4. S. J. Hogan, L. Higham, and T. C. L. Griffin, “Dynamics of a piecewise-linear map with a gap,” *Proceedings of the Royal Society A* (2007) (general discontinuous-map setting; distinct model).
