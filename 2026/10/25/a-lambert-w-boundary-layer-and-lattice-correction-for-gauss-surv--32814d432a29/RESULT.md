# A Lambert-W boundary layer and lattice correction for Gauss survivors

## Finding
Let \(T:[0,1]\to[0,1]\) be the Gauss map, \(T(0)=0\) and \(T(x)=1/x-\lfloor 1/x\rfloor\) for \(x>0\). For \(0\leq\alpha\leq1\), set
\[
E(\alpha)=\{x\in[0,1]:T^j(x)\leq\alpha\text{ for every integer }j\geq0\},\qquad d(\alpha)=\dim_H E(\alpha).
\]
For each integer \(N\geq2\), let \(s_N^-\) and \(s_N^+\) be the unique real roots in \((1/2,1)\) of, respectively,
\[
\zeta(2s,N+N^{-1})=1,\qquad \zeta(2s,N)=1,
\]
where \(\zeta(z,q)=\sum_{a=0}^\infty(a+q)^{-z}\) denotes the Hurwitz zeta function for \(z>1\). Then
\[
\boxed{s_N^-\leq d(1/N)\leq s_N^+,\qquad 0\leq s_N^+-s_N^-\leq\frac{2}{N^2\log N}.}
\]
Writing \(L=\log N\), and letting \(W\) denote the positive real Lambert function determined by \(W(t)e^{W(t)}=t\), the dimension has the asymptotic expansion
\[
\boxed{
 d(1/N)=\frac12+\frac{W(L)}{2L}
 +\frac{W(L)^2}{4NL^2(1+W(L))}
 +O\!\left(\frac{1}{N^2L}\right),\qquad N\to\infty.
}
\]
In particular the dimension approaches the discontinuity value \(1/2\) at an explicitly quantified, very slow logarithmic rate, and the first finite-digit correction is separated from the nonlinear Gauss-map distortion error. By monotonicity, the same leading-order boundary law holds for all positive real holes:
\[
\boxed{d(\alpha)-\frac12\sim\frac{W(\log(1/\alpha))}{2\log(1/\alpha)}\qquad(\alpha\downarrow0).}
\]
The value \(d(0)=0\) and the qualitative right limit \(1/2\) are prior results, not claims of novelty here.

## Assumptions and scope
The statements use the standard regular continued-fraction coding of the Gauss map and the Euclidean Hausdorff dimension on \([0,1]\). The finite-dimensional enclosures hold for **every** integer \(N\geq2\); the two-term Lambert-W formula holds as \(N\to\infty\), with an absolute implied constant. The continuous-parameter statement is a leading asymptotic, not a claim that \(d(\alpha)\) is differentiable or strictly varying: it is a devil's staircase. Rationally terminating continued fractions and the fixed point \(0\) do not affect Hausdorff dimension.

## Proof
**1. Full-shift coding and branch derivatives.** For an irrational \(x=[a_1,a_2,\ldots]\), the condition \(T^j(x)\leq1/N\) for every \(j\geq0\) is equivalent to \(a_j\geq N\) for every \(j\geq1\). Thus the irrational part of \(E(1/N)\) is the attractor of the countable conformal iterated-function system
\[
\phi_a(x)=\frac{1}{a+x},\qquad a=N,N+1,\ldots,
\]
on \(I_N=[0,1/N]\). Each branch maps \(I_N\) inside itself and the interiors of the branch images are disjoint. Throughout \(I_N\),
\[
(a+N^{-1})^{-2}\leq |\phi'_a(x)|\leq a^{-2}.
\]
This system is uniformly contracting for \(N\geq2\), has bounded distortion, and satisfies the open set condition. The standard conformal-IFS pressure/dimension principle, also used for these Gauss survivor sets in the motivating source, applies. Alternatively, apply the finite-alphabet version to each initial finite family and take an increasing union.

**2. Explicit pressure enclosures.** For every word \(\omega=(a_1,\ldots,a_k)\), the derivative of \(\phi_\omega\) is bounded above and below by the corresponding products of the scalar upper and lower factors. Consequently its geometric pressure \(P_N(s)\) satisfies
\[
\log\sum_{a=N}^\infty(a+N^{-1})^{-2s}
\leq P_N(s)\leq
\log\sum_{a=N}^\infty a^{-2s},\qquad s>\tfrac12.
\]
The unique zero of \(P_N\) is \(d(1/N)\). Both scalar sums decrease continuously from infinity to a value below one at \(s=1\); their roots \(s_N^-,s_N^+\) therefore exist uniquely in \((1/2,1)\), proving the enclosure.

To bound its width, set \(U_N(s)=\sum_{a=N}^\infty a^{-2s}\) and \(V_N(s)=\sum_{a=N}^\infty(a+N^{-1})^{-2s}\). At \(s=s_N^+\), the elementary inequality \((1+t)^{-2s}\geq1-2st\) gives
\[
0\leq1-V_N(s_N^+)\leq\frac{2s_N^+}{N}\sum_{a=N}^\infty a^{-2s_N^+-1}\leq\frac{2}{N^2}.
\]
As \(s\) varies from \(s_N^-\) to \(s_N^+\), \(V_N(s)\geq 1-2/N^2\geq1/2\); hence
\[
-V_N'(s)=2\sum_{a=N}^\infty\log(a+N^{-1})(a+N^{-1})^{-2s}\geq\log N.
\]
The mean-value theorem yields \(s_N^+-s_N^-\leq2/(N^2\log N)\).

**3. The lattice boundary layer.** Write \(s=\tfrac12+e\), \(L=\log N\). Uniformly for \(0<e\leq1/2\), the first Euler--Maclaurin terms give
\[
U_N(\tfrac12+e)=\frac{N^{-2e}}{2e}+\frac{N^{-1-2e}}2+O(N^{-2-2e}).
\]
Let \(w=W(L)\), \(e_0=w/(2L)\). Because \(we^w=L\), the integral term equals one at \(e=e_0\), and
\[
U_N(\tfrac12+e_0)=1+\frac{e_0}{N}+O(e_0/N^2).
\]
The derivative of the integral term there is exactly \(-[2L+1/e_0]\). The differentiated Euler--Maclaurin remainder is smaller by a factor of order \(N^{-1}\), and the second derivative on the relevant \(O(e_0/(NL))\) neighborhood is \(O(L^2)\). Taylor's theorem and strict monotonicity thus locate the unique upper root at
\[
s_N^+=\frac12+e_0+\frac{e_0}{N(2L+1/e_0)}+O\!\left(\frac{1}{N^2L}\right).
\]
Substituting \(e_0=w/(2L)\) turns the displayed correction into \(w^2/[4NL^2(1+w)]\). Step 2 replaces \(s_N^+\) by the true dimension at the same \(O(1/(N^2L))\) precision, completing the discrete expansion. This reasoning is asymptotic as \(N\to\infty\), where \(w\to\infty\) and \(e_0\to0\), so all derivative estimates are uniform for sufficiently large \(N\).

**4. Arbitrary small holes.** For \(N=\lfloor1/\alpha\rfloor\), monotonicity gives \(d(1/(N+1))\leq d(\alpha)\leq d(1/N)\). The leading Lambert-W terms at consecutive integers are asymptotically equivalent to that at \(\log(1/\alpha)\); squeezing proves the final displayed limit.

## Verification
The numerical checker `checker.py` (Python 3 and `mpmath` 1.3.0) computes the two Hurwitz-zeta roots by bisection for six finite values of \(N\), confirms their ordering, and compares the first two asymptotic terms to the upper root. Its complete output is in `checker_output.txt`. These computations do **not** establish the countable-alphabet dimension principle or the infinite-\(N\) asymptotic; those are supplied by the proof above. The inequalities \(N^{-1}\) versus \(N^{-2}\) and the root-to-dimension transfer are explicitly separated to avoid conflating the scalar zeta approximation with the nonlinear pressure.

## Relationship to prior work
Liu and Liao (arXiv:2610.14534v1, first public version 2026-10-10) establish the survivor-set plateau structure, a pressure characterization for dimensions, and the qualitative jump \(d(0)=0\), \(d(\alpha)\to1/2\) as \(\alpha\downarrow0\). Their Section 4 identifies \(E(1/N)\) with the minimum-digit full shift. The present theorem supplies an explicitly quantified approach to that jump and a finite-\(N\) two-sided pressure certificate with a separately resolved lattice correction, which are not statements of their main theorems.

Fang, Moreira and Zhang (arXiv:2409.00521v1) study dimensions of sets with specially located growing continued-fraction digits and related pressure laws. Their main theorems concern sparse large-digit positions and do not give a parameter-dependent expansion for the full all-positions alphabet \(\{N,N+1,\ldots\}\). Chitu, Sebe and Lascu (arXiv:2603.27635v1, Theorem 1.2) explicitly quote Good’s older lower-cutoff bounds for ordinary continued fractions and extend comparable two-sided inequalities to their \(N\)-expansion setting. Their bound \(rac12+1/[2\log(lpha+2)]\leq\dim_H F_{lpha,1}\leqrac12+\log\log(lpha-1)/[2\log(lpha-1)]\) does not determine the leading Lambert-W coefficient, the lattice correction, or the computable Hurwitz enclosure. These earlier quantitative inequalities are credited rather than claimed as new. The Mauldin--Urbański conformal-IFS framework supplies the pressure background; it is not claimed as new. Earlier restricted-digit asymptotics are a potential historical-priority risk and remain a topic for independent literature verification.

## Limitations
This theorem is specifically about the Gauss-map survivor under holes \((\alpha,1]\) and the countable alphabet with a **lower** digit cutoff. It does not treat upper bounded digits, arbitrary nonuniform digit constraints, smoothness of the devil's staircase, Hausdorff measure at the critical dimension, or escape-time distributions. The finite enclosure has a provable width, but the enclosed exact dimension is not asserted to equal either Hurwitz-zeta root. An earlier higher-order asymptotic for lower-cutoff continued fractions, if found, could cover the claimed historical novelty. Independent validation has not been performed.

## References
1. C. Liu and L. Liao, *Survivor Set of Gauss Map with a Hole at 1*, arXiv:2610.14534v1, public version dated 2026-10-10. https://arxiv.org/html/2610.14534v1
2. L. Fang, C. G. Moreira and Y. Zhang, *Fractal geometry of continued fractions with large coefficients and dimension drop problems*, arXiv:2409.00521v1 (2024). https://arxiv.org/html/2409.00521v1
3. A. C. Chitu, G. I. Sebe and D. Lascu, *Sharp Hausdorff Dimension Bounds for Sets with Bounded and Growing Digits in N-expansions*, arXiv:2603.27635v1 (2026), Theorem 1.2. https://arxiv.org/html/2603.27635v1
4. R. D. Mauldin and M. Urbański, *Dimensions and measures in infinite iterated function systems*, Proc. London Math. Soc. 73 (1996), 105--154. DOI:10.1112/plms/s3-73.1.105.
5. R. D. Mauldin and M. Urbański, *Conformal iterated function systems with applications to the geometry of continued fractions*, Trans. Amer. Math. Soc. 351 (1999), 4995--5025. DOI:10.1090/S0002-9947-99-02268-0.
