# A sharp three-coexistence bound on the protection edge of a quorum public-goods game

## Finding

In the quorum-activated collective-risk evolutionary game of Li, Li, He, Shi, and Szolnoki [1], the invariant defector–protective-cooperator edge contains **at most three mixed equilibria**, counted with multiplicity. Moreover, **at most one** of these edge-interior equilibria can be locally asymptotically stable along that edge. Both bounds are sharp: three simple mixed equilibria and one stable edge-interior equilibrium already occur for the smallest possible group size \(N=4\). This is also a hyperbolic configuration of the full three-strategy replicator dynamics: its three mixed edge equilibria are, in increasing protective-cooperator frequency, a saddle, a sink, and a source. Both homogeneous defection and homogeneous ordinary cooperation are sinks as well. The three mixed equilibria persist under sufficiently small admissible parameter perturbations.

## Assumptions and scope

Consider an infinite, well-mixed population with strategy frequencies \(x,y,z\ge 0\), \(x+y+z=1\), for ordinary cooperation \(C\), defection \(D\), and protective cooperation \(S\), respectively. Interactions use independently sampled groups of size \(N\ge 3\); write \(n=N-1\). The quorum \(M\) is an integer satisfying \(2\le M\le N-1\). A contributor pays \(c>0\), the public-goods multiplier is \(1<r<N\), a protective cooperator additionally pays \(k>0\), and an unprotected group with \(j\) defectors has collective failure probability \(p(j)=1-\rho^j\), with \(0<\rho<1\). Failure incurs a shared additive loss \(L>0\). A group with at least \(M\) protective cooperators reduces the loss probability by the fraction \(\omega\in[0,1]\). These are exactly the conditional-payoff assumptions of [1], with no extra intervention rule.

The full deterministic replicator law is \(\dot x=x(P_C-\bar P)\), \(\dot y=y(P_D-\bar P)\), \(\dot z=z(P_S-\bar P)\), with \(\bar P=xP_C+yP_D+zP_S\). On the invariant edge \(x=0\), one has \(y=1-z\), and the reduced equation is \(\dot z=z(1-z)B(z)\), where \(B(z)=P_S-P_D\). The theorem concerns mixed **edge** equilibria \(0<z<1\); it makes no global enumeration of the interior \(x,y,z>0\) equilibria or of the full flow's attraction basins.

## Proof

**1. The exact conditional gain sequence.** Suppose among the \(n\) co-players of a focal individual there are exactly \(m\) protective cooperators and \(j=n-m\) defectors. Set \(a=c(r/N-1)<0\). Subtracting the two conditional payoffs in [1, Eq. (2)] gives the exact gain from choosing \(S\) instead of \(D\):

\[
b_m=a-k+L(1-\rho)\rho^{n-m}\bigl(1-\omega\mathbf1_{m\ge M}\bigr)+L\omega\bigl(1-\rho^{n-m}\bigr)\mathbf1_{m=M-1}.
\]

Indeed, choosing \(S\) instead of \(D\) increases the personal public-good share by \(rc/N\), incurs \(c+k\), prevents the additional failure increment \(p(j+1)-p(j)=(1-\rho)\rho^j\), and can itself finish the quorum precisely when \(m=M-1\). Binomial co-player sampling therefore yields the **Bernstein polynomial**

\[
 B(z)=\sum_{m=0}^{n}\binom nm b_m z^m(1-z)^{n-m}.
\]

This representation also follows independently from [1, Eqs. (7), (9), (10)].

**2. Universal sharp upper bound.** The coefficients \(b_0,\ldots,b_{M-1}\) are strictly increasing: the baseline term strictly increases with \(m\), and the pivotal quorum bonus at \(M-1\) is nonnegative. The coefficients \(b_M,\ldots,b_n\) are nondecreasing, since \(1-\omega\ge0\). Thus a **downward jump can occur only between** \(b_{M-1}\) and \(b_M\). Ignoring zero coefficients, the complete coefficient sequence has at most three sign changes, necessarily at most one from positive to negative. It cannot vanish identically because its first increasing block contains at least two distinct entries.

The bijection \(t=z/(1-z)\) from \((0,1)\) to \((0,\infty)\) gives

\[
 (1+t)^nB\!\left(\frac{t}{1+t}\right)=\sum_{m=0}^{n}\binom nm b_m t^m.
\]

Every nonzero binomial coefficient is positive, so Descartes' rule of signs bounds the number of positive roots, **counted with multiplicity**, by three. This proves the asserted upper bound, independently of group size. It is the general Bernstein sign-variation method of Peña, Lehmann, and Nöldeke [2] applied to the particular protected-risk gain sequence; neither that general method nor Descartes' rule is claimed as new.

For the stable-equilibrium bound, any edge-interior asymptotically stable isolated equilibrium requires the scalar field to point right immediately on its left and left immediately on its right, hence a positive-to-negative sign crossing of \(B\). If the initial nonzero coefficient is positive, the first increasing block cannot generate a sign change and the total coefficient variation is at most two. If it is negative, three crossings can only alternate negative–positive–negative–positive and contain at most one positive-to-negative crossing. The same conclusions hold if the initial coefficients vanish, after discarding them. Hence **at most one** edge-interior equilibrium is locally asymptotically stable along the edge. No hyperbolicity assumption is needed for this part.

**3. Exact minimal-size sharpness witness.** Let

\[
N=4,\quad M=2,\quad r=\frac{16}{5},\quad c=L=1,\quad
\rho=\frac15,\quad\omega=\frac35,\quad k=\frac7{100}.
\]

All strict parameter restrictions hold, and \(\gamma=-\log\rho=\log5>0\) in the notation of [1]. The four exact gain coefficients are

\[
(b_0,b_1,b_2,b_3)=\left(-\frac{659}{2500},\frac{169}{500},-\frac{103}{500},\frac1{20}\right),
\]

which expand to

\[
B(z)=\frac{4864z^3-8592z^2+4512z-659}{2500}.
\]

The **exact** signs are certified by

\[
B(0)=-\frac{659}{2500}<0,\qquad B\left(\frac13\right)=\frac{1903}{67500}>0,
\]
\[
B\left(\frac23\right)=-\frac{769}{67500}<0,\qquad B(1)=\frac1{20}>0.
\]

By continuity, there is one distinct mixed edge root in each of \((0,1/3)\), \((1/3,2/3)\), and \((2/3,1)\). Since the gain is cubic, there are exactly three and each is simple. A more precise rational isolation is \(z_1\in(1/5,1/4)\), \(z_2\in(3/5,2/3)\), and \(z_3\in(9/10,19/20)\). Numerical values, not used in the proof, are approximately \(0.243116863\), \(0.610504042\), \(0.912826464\). Groups of size \(N=3\) have degree at most \(n=2\) on the edge, and hence cannot have three such roots: **four is the minimal possible group size**.

**4. Full two-dimensional local stability.** In [1, Eq. (17)], the two eigenvalues at an edge root are \(A(0,z)\) in the transverse \(C\)-invasion direction and \(z(1-z)B'(z)\) in the tangential direction, where \(A=P_C-P_D\). The exact payoff identity \(B=A-k+L\omega\Psi_M\) gives, at any edge root in this example,

\[
A(0,z)=k-L\omega\Psi_2(z)=\frac7{100}-\frac{216}{125}z(1-z)^2.
\]

On the first root interval, \(z(1-z)^2>(1/5)(3/4)^2\), and on the second, \(z(1-z)^2>(3/5)(1/3)^2\); the resulting value of \(A\) is negative in both cases. On the third, \(z(1-z)^2<(1)(1/10)^2\), so \(A\) is positive. Because the cubic's three simple roots have derivative signs positive, negative, positive, respectively, the full planar equilibria are in order a hyperbolic saddle, a hyperbolic sink, and a hyperbolic source. From [1, Eqs. (14), (15)], the full-defection invasion eigenvalues are \(-121/625\) and \(-659/2500\), while the full-cooperation invasion eigenvalues are \(-3/5\) and \(-7/100\). Thus both homogeneous states are also sinks. Hyperbolic roots and their local types persist under small admissible perturbations by the implicit function theorem and eigenvalue continuity.

## Verification

The embedded standalone program `verify_quorum.py` uses only Python's standard library and exact rational arithmetic. It independently subtracts the original conditional \(S\)- and \(D\)-payoffs to recover the four gain coefficients, expands their Bernstein representation into the exact cubic, evaluates the alternating-sign certificate and the three sharper rational brackets, and checks the inequalities used for full-planar transverse stability and both homogeneous vertices. Run `python verify_quorum.py`; successful execution prints `PASS`. These checks were run successfully against the embedded program before publication. The all-size bound is analytic, not an extrapolation from finite enumeration.

## Relationship to prior work

Li et al. [1] introduce and analyze this precise three-strategy quorum-activated risk model, derive the payoff gradients and edge Jacobian, and numerically track a saddle–node pair of mixed \(D\)–\(S\) states for a different baseline parameter set with \(N=5\). Their accessible v1 main text, Appendix C.6–C.8, and Appendix D.1 describe edge equilibria through the equation \(B(0,z)=0\), but do not give a uniform three-root bound, a three-root realization, or the minimal group-size four construction. Peña, Lehmann, and Nöldeke [2] establish the general Bernstein/Descartes sign-variation machinery for arbitrary two-strategy multiplayer games, not this model's constrained gain coefficients or the exact sharp three-root example. Thus the contributed mathematics is the **model-specific coefficient shape, sharp realization, and full-planar hyperbolic classification**, not the general root-count principle.

## Limitations

This is a deterministic, infinite-population, well-mixed replicator result with independent group sampling, fixed group size, and the precise exponential failure-risk and quorum rules of [1]. It gives no global basin sizes, stochastic finite-population persistence, welfare-optimal policy, or exhaustive count of full-interior three-strategy equilibria. Root multiplicity is bounded on the \(D\)–\(S\) **edge only**. Although the closest accessible full-text works do not state this model-specific combined theorem, unindexed or later versions may contain equivalent calculations; novelty is not independently certified.

## References

[1] S. Li, X. Li, J. He, L. Shi, and A. Szolnoki, “Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection,” arXiv:2609.28132v1, first submitted 2026-09-23, https://arxiv.org/html/2609.28132 . See conditional payoffs (2), selection gradients (7)–(10), edge eigenvalues (17), §§3.1–3.2, and Appendices C–D.

[2] J. Peña, L. Lehmann, and G. Nöldeke, “Gains from switching and evolutionary stability in multi-player matrix games,” *Journal of Theoretical Biology* **346** (2014), 23–33; preprint arXiv:1310.0498, https://jorgeapenas.github.io/assets/pdf/Pena2014.pdf . See §§2–3.3 for the Bernstein gain representation and variation-diminishing bound.
