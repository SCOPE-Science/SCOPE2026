# Exact prime-two orbit census and coexistence wedge for the rational Rulkov neuron map

## Finding
For the rational Rulkov map
\[
F_{\alpha,\eta,\sigma}(x,y)=\left(\frac{\alpha}{1+x^2}+y,\ y-\eta(x-\sigma)\right),\qquad \alpha>0,\quad \eta>0,\quad \sigma\in\mathbb R,
\]
there are at most two distinct real orbits of least period two. Their number is exactly classified, including all equality cases, as follows. Put
\[
k=2+\eta,\qquad A_*(\sigma)=\frac{k(1+\sigma^2)^2}{4\sigma}\quad(\sigma>0),\qquad A_{\rm sn}(\sigma)=k\sigma\quad(\sigma>1).
\]
If \(\sigma\le0\), there are no prime-two orbits. If \(0<\sigma\le1\), there are none for \(\alpha\le A_*(\sigma)\), and exactly one for \(\alpha>A_*(\sigma)\). If \(\sigma>1\), the number is zero for \(\alpha<A_{\rm sn}\), one for \(\alpha=A_{\rm sn}\), two for \(A_{\rm sn}<\alpha<A_*\), and one for \(\alpha\ge A_*\). At \(\alpha=A_*\) the smaller-amplitude branch reaches the fixed point, but the larger-amplitude prime-two orbit remains.

Every nontrivial period-two orbit is explicitly reconstructed from a positive root \(q\) of
\[
q^2+2(1-\sigma^2)q+(1+\sigma^2)^2=\frac{4\alpha\sigma}{2+\eta}.
\]
For either choice \(u\in\{-\sqrt q,\sqrt q\}\), its two points, ordered cyclically, are
\[
(x_1,y_1)=\left(\sigma+u,\ \sigma-u-\frac{\alpha}{1+(\sigma+u)^2}\right),\quad
(x_2,y_2)=\left(\sigma-u,\ \sigma+u-\frac{\alpha}{1+(\sigma-u)^2}\right).
\]
Changing the sign of \(u\) just swaps the points.

The coexistence window is genuine, not a count of unstable algebraic solutions only: at the exact parameters \((\sigma,\alpha,\eta)=(2,5,1/1000)\) the fixed point and the larger-amplitude prime-two orbit are both asymptotically stable, whereas the smaller-amplitude prime-two orbit is a hyperbolic saddle. Consequently there is an open set of parameters with this sink–sink–saddle configuration.

## Assumptions and scope
The state space is \(\mathbb R^2\); the map is smooth everywhere, though not assumed globally invertible. A prime-two orbit means a set of two distinct points exchanged by one iteration of \(F\), counted once up to cyclic permutation. The theorem assumes \(\alpha>0\) and \(\eta>0\) but places no smallness condition on \(\eta\), and counts all real prime-two orbits, whether attracting or not. The parameter \(\sigma\) here denotes the fixed-point abscissa in the later three-parameter notation; the original 2000 paper uses different parameter symbols and writes its second map component as \(y-\sigma_0x-\beta\). The coordinate identification is \(\eta=\sigma_0\), \(\sigma=-\beta/\sigma_0\) when \(\sigma_0>0\). The positive-\(\sigma\) coexistence wedge is outside that paper's displayed positive-\(\beta\) examples and is studied in later parameter maps.

## Proof
Suppose \((x_1,y_1)\mapsto(x_2,y_2)\mapsto(x_1,y_1)\) is a least-period-two orbit. Summing the two slow-variable increments yields \(x_1+x_2=2\sigma\). Therefore write \(x_1=\sigma+u\), \(x_2=\sigma-u\), where \(u\ne0\). The two fast-variable updates and one slow-variable update give
\[
(2+\eta)u=\frac{\alpha}{1+(\sigma-u)^2}-\frac{\alpha}{1+(\sigma+u)^2}
=\frac{4\alpha\sigma u}{[1+(\sigma+u)^2][1+(\sigma-u)^2]}.
\]
The denominator is positive. Dividing by \(u\), setting \(q=u^2>0\) and expanding its product proves the displayed quadratic equation. In particular, positivity forces \(\sigma>0\). Conversely, for any positive root and either sign of \(u\), the displayed \(y_1,y_2\) satisfy both fast-variable updates by definition and both slow-variable updates by the quadratic relation. Since \(u\ne0\), this is a prime-two orbit. Every orbit has been recovered, once per positive root.

Write \(P(q)=q^2+2(1-\sigma^2)q+(1+\sigma^2)^2\). If \(0<\sigma\le1\), \(P\) is strictly increasing on \(q>0\) with boundary value \(P(0)=(1+\sigma^2)^2\); equality at \(q=0\) does not create a prime-two orbit. If \(\sigma>1\), \(P\) has its unique positive minimum at \(q_0=\sigma^2-1\), with \(P(q_0)=4\sigma^2\), while \(P(0)=(1+\sigma^2)^2\). The quadratic's positive-root counts, including a double root at the minimum and one zero root at the second threshold, give every listed case. At \(\alpha=A_*\) and \(\sigma>1\), the remaining positive root is \(q=2(\sigma^2-1)\).

For stability put \(g(x)=\alpha/(1+x^2)\), \(d_i=g'(x_i)\). The one-step derivative is \(J_i=\left(\begin{smallmatrix}d_i&1\\-\eta&1\end{smallmatrix}\right)\), so the two-step multiplier polynomial is \(\lambda^2-T\lambda+D\), where
\[
T=1-2\eta+d_1d_2,\quad D=(d_1+\eta)(d_2+\eta).
\]
On a period-two orbit the defining quadratic equation gives the exact identities
\[
d_1d_2=\frac{(2+\eta)^2(\sigma^2-q)}{4\sigma^2},\quad
 d_1+d_2=-(2+\eta)\left(1-\frac{4q(q+1-\sigma^2)}{P(q)}\right),
\]
and hence
\[
1-T+D=\frac{4\eta(2+\eta)q(q+1-\sigma^2)}{P(q)}.
\]
These formulas follow by differentiating \(g\), substituting the cycle relation, and expanding; an exact symbolic reproduction is supplied.

At \((\sigma,\alpha,\eta)=(2,5,1/1000)\) the two roots are \(q_\pm=3\pm\sqrt{7984/2001}\). Exact rational squaring gives \(1997/1000<\sqrt{7984/2001}<1998/1000\). Thus \(1.002<q_-<1.003\), \(4.997<q_+<4.998\). At the lower root \(1-T+D<0\), so the multiplier polynomial is negative at \(\lambda=1\), and one multiplier is \(>1\). The above formulas also give \(0<D<1\) (for example using \(d_1d_2\in(0.74,0.76)\) and \(-3<d_1+d_2<0\)), so the other multiplier lies in \((0,1)\); this prime-two orbit is a hyperbolic saddle.

At the upper root, \(1-T+D>0\), \(-0.251<d_1d_2<0\), and \(0<d_1+d_2<3\). Consequently \(1+T+D=2-2\eta+2d_1d_2+\eta(d_1+d_2)+\eta^2>1.49\) and \(1-D=1-d_1d_2-\eta(d_1+d_2)-\eta^2>0.996\). The three real Schur inequalities \(1-T+D>0\), \(1+T+D>0\), \(1-D>0\) imply that both multipliers are strictly inside the unit disk, so this orbit is an asymptotically stable sink cycle.

The fixed point is \((\sigma,\sigma-\alpha/(1+\sigma^2))\). At the example its one-step Jacobian has trace \(1/5\) and determinant \(-799/1000\), and its Schur quantities are exactly \(1/1000\), \(401/1000\), \(1799/1000\), all positive. Thus it too is a hyperbolic sink. Hyperbolicity and the strict inequalities persist under small perturbations of the three parameters, yielding the asserted open coexistence region.

## Verification
The standalone Python/SymPy file `check_rulkov.py` verifies both maps of the reconstructed two-cycle, the exact derivative product/sum identities, the multiplier polynomial at \(\lambda=1\), the exact radical bounds, and all three Schur inequalities at the example. Run with `python check_rulkov.py` from a Python environment containing SymPy. The proof of the universal root count is elementary and does not depend on finite sampling or numerical output. The script's floating-point evaluations are diagnostic only; the stated rational interval and inequality chains constitute the strict certificates used in the proof.

## Relationship to prior work
Rulkov's 2000 preprint introduces the rational fast–slow map (in another slow-variable parameterization), and analyzes a frozen one-dimensional fast map and burst synchronization rather than an exhaustive count of prime-two points of the uncoupled full two-dimensional map. Wang and Cao (2014) analyze equilibria and bifurcation curves; Ge and Cao (2021) report period-two and higher regimes through trajectories, including an example with negative \(\alpha\), outside this theorem's \(\alpha>0\) range. Sun, Ma and Cao (2025) numerically show coexistence of fixed points and period-two regimes at parameters including \((\sigma,\alpha)=(2,5)\). This theorem determines all real prime-two solutions, including the unstable one not detected by trajectory attraction, and proves an exact open sink–sink–saddle regime. The 2025 complete article and the 2014 article were not available in full in this review, so priority relative to undisclosed details in those works remains uncertain.

## Limitations
The theorem classifies prime-two orbits only; it neither excludes cycles of higher period nor classifies global basins or chaotic invariant sets. The open coexistence conclusion is local to the certified hyperbolic example and does not assert that every parameter with two prime-two orbits has a stable one. The extended positive-\(\sigma\) regime differs from the original preprint's displayed positive-\(\beta\) cases. Publication priority relative to inaccessible full texts remains unresolved.

## References
1. N. F. Rulkov, *Regularization of Synchronized Chaotic Bursts*, arXiv:nlin/0011028v1 (first posted 2000-11-14), later *Physical Review Letters* 86 (2001), 183–186; doi:10.1103/PhysRevLett.86.183.
2. C. Wang and H. Cao, *Parameter space of the Rulkov chaotic neuron model*, *Communications in Nonlinear Science and Numerical Simulation* 19 (2014), 2060–2070; doi:10.1016/j.cnsns.2013.10.004.
3. P. Ge and H. Cao, *Intermittent evolution routes to the periodic or the chaotic orbits in Rulkov map*, *Chaos* 31 (2021), 093119; doi:10.1063/5.0060205.
4. H. Sun, Q. Ma and H. Cao, *Intrinsic properties of the chaotic Rulkov model*, *Journal of Mathematical Physics* 66 (2025), 042713; doi:10.1063/5.0244866.
