# A closed Hardy-space copy of nowhere locally Nevanlinna Dirichlet series

## Finding
Let \(\mathscr H^p\) denote the Hardy space of ordinary Dirichlet series under the Bohr transform, and put
\[\mathscr E=\bigcap_{0<p<2}\mathscr H^p,\qquad\mathscr A=\bigcap_{0<p<2}H^p(\mathbb D).\]
Equip these spaces with the cofinal Fréchet seminorms at \(p_j=2-1/j\) for integers \(j\ge2\). Let \(\mathscr E_{\rm odd}\) consist of series \(F(s)=\sum_{n\ge1}a_n n^{-s}\) whose coefficients at all even indices vanish.

**Theorem.** There is a dense \(G_\delta\) set \(\mathscr R\subset\mathscr E_{\rm odd}\) such that every \(F\in\mathscr R\) obeys, for every compact real interval \(I\) of positive length,
\[\limsup_{\varepsilon\downarrow0}\inf_{t\in I}\left|F\!\left(\frac12+\varepsilon+it\right)\right|=+\infty.\]
Fix any \(F\in\mathscr R\). Then
\[T_F:\mathscr A\longrightarrow\mathscr E,\qquad (T_FG)(s)=F(s)G(2^{-s})\]
is an injective continuous linear map with closed infinite-dimensional range. For every \(0<p<2\),
\[\|T_FG\|_{\mathscr H^p}=\|F\|_{\mathscr H^p}\|G\|_{H^p(\mathbb D)}.\]
Every nonzero \(h\in T_F(\mathscr A)\) has, on **every** nonempty real open interval \(I\),
\[\limsup_{\varepsilon\downarrow0}\int_I\log^+\left|h\!\left(\frac12+\varepsilon+it\right)\right|\,dt=+\infty.\]
Thus the set of Dirichlet series in \(\mathscr E\) which are nowhere locally in the Nevanlinna class along \(\operatorname{Re}s=1/2\), together with zero, contains a closed infinite-dimensional subspace naturally isomorphic to \(\mathscr A\).

## Assumptions and scope
For a Dirichlet polynomial \(P(s)=\sum_{n\le N}a_n n^{-s}\), write \(n=\prod_q q^{\nu_q(n)}\) and use its Bohr transform \(\mathcal BP(z)=\sum_{n\le N}a_n\prod_qz_q^{\nu_q(n)}\). The \(\mathscr H^p\) norm is the normalized Haar \(L^p\) norm of \(\mathcal BP\) on the infinite torus; completion defines \(\mathscr H^p\). The disk Hardy norm uses normalized circle Haar measure. For \(p_j=2-1/j\), \(j\ge2\), the spaces are Banach; their projective intersection is a complete Fréchet space. Since normalized Haar measures have total mass one, the \(p_j\)-norms increase with \(j\), and their intersection equals that over all \(0<p<2\). Point evaluation of a Dirichlet series is continuous on \(\operatorname{Re}s>1/2\). The closed subspace \(\mathscr E_{\rm odd}\) is the image of conditional expectation in the Bohr coordinate corresponding to the prime \(2\); odd-index Dirichlet polynomials are dense in it.

No statement is made at \(p=2\), nor does the theorem assert divergence at every fixed approach sequence: the limits are upper limits along suitable positive real approach parameters.

## Proof
**Step 1: uniform odd-block growth.** For integers \(X\ge3\), put
\[D_X(s)=\sum_{1\le n\le X}n^{-s},\qquad B_X(s)=\sum_{\substack{1\le n\le X\\n\text{ odd}}}n^{-s}=D_X(s)-2^{-s}D_{\lfloor X/2\rfloor}(s).\]
Haar integration over the first Bohr coordinate removes all even-index coefficients, so \(\|B_X\|_{\mathscr H^p}\le\|D_X\|_{\mathscr H^p}\) whenever \(p\ge1\). Harper's Steinhaus low-moment theorem gives, for each fixed \(1\le p<2\),
\[\|D_X\|_{\mathscr H^p}\le C_p\frac{\sqrt X}{(\log\log X)^{1/4}}\quad(X\text{ sufficiently large}).\]
To independently determine pointwise growth, Euler summation gives, uniformly for \(\tfrac12\le\sigma\le\tfrac34\) and \(|t|\le T\), with each fixed \(T<\infty\),
\[D_X(\sigma+it)=\frac{X^{1-\sigma-it}}{1-\sigma-it}+O_T(1).\]
The odd decomposition consequently yields
\[B_X(\sigma+it)=\frac{X^{1-\sigma-it}}{2(1-\sigma-it)}+O_T(1).\]
Indeed, the even leading term is exactly half the full leading term; replacing \(X/2\) by its integer part changes only a uniformly bounded remainder. With \(\varepsilon_X=1/\log X\), this implies
\[\inf_{|t|\le T}|B_X(\tfrac12+\varepsilon_X+it)|\ge c_T\sqrt X\]
for all large \(X\). Combining the two estimates, for each fixed \(1\le p<2\),
\[\inf_{|t|\le T}\frac{|B_X(\tfrac12+\varepsilon_X+it)|}{\|D_X\|_{\mathscr H^p}}\ge c_{p,T}(\log\log X)^{1/4}\longrightarrow\infty.\]
An imaginary translate \(B_X(s-i\tau)\) preserves all Hardy–Dirichlet norms (rotation of the prime Bohr coordinates) and still has odd support. The last estimate thus works uniformly on any prescribed compact vertical interval.

**Step 2: a simultaneous residual construction.** For each rational-ended compact interval \(I=[a,b]\) with \(a<b\), and positive integers \(k,m\), define
\[U_{I,k,m}=\bigcup_{0<\varepsilon<1/m}\left\{F\in\mathscr E_{\rm odd}:\min_{t\in I}|F(\tfrac12+\varepsilon+it)|>k\right\}.\]
Each set is open in \(\mathscr E_{\rm odd}\), because point evaluations vary continuously and uniformly on each compact vertical segment strictly to the right of the critical line. It is dense: given a basic neighborhood of \(f\), choose \(J\) such that the neighborhood is controlled by its largest seminorm \(\|\cdot\|_{\mathscr H^{p_J}}\). Approximate \(f\) in that norm by an odd Dirichlet polynomial \(P\). For any small \(\eta>0\), set
\[H_X(s)=\eta\,\frac{B_X(s-i\tau)}{\|D_X\|_{\mathscr H^{p_J}}}\]
where \(\tau\) shifts \(I\) into a fixed bounded interval. Then \(\|H_X\|_{\mathscr H^{p_J}}\le\eta\), hence every prescribed seminorm is small. But \(\min_{t\in I}|H_X(\tfrac12+\varepsilon_X+it)|\to\infty\), while the fixed polynomial \(P\) is bounded on the indicated vertical segment. Choosing \(X\) large forces \(P+H_X\in U_{I,k,m}\) while preserving the neighborhood constraint.

The Baire category theorem in the complete \(\mathscr E_{\rm odd}\) shows that
\[\mathscr R=\bigcap_{I,k,m}U_{I,k,m}\]
is dense \(G_\delta\). Given a compact interval with arbitrary real endpoints, choose a larger rational-ended compact interval. Membership in \(\mathscr R\), applied with arbitrarily large \(k,m\), proves the asserted uniform upper-limit divergence. In particular every \(F\in\mathscr R\) is nonzero.

**Step 3: a closed linear space.** Let \(G(z)=\sum_{r\ge0}b_rz^r\in\mathscr A\) be arbitrary. The coefficients of \(F\) use only primes \(3,5,7,\ldots\), while the coefficients of \(G(2^{-s})\) use only the prime \(2\). Thus the Bohr lift of their product is the tensor product of two independent variable sets. Fubini's theorem and polynomial approximation yield, for every \(0<p<2\),
\[\|F(s)G(2^{-s})\|_{\mathscr H^p}^p=\|F\|_{\mathscr H^p}^p\|G\|_{H^p(\mathbb D)}^p.\]
The map \(T_F\) is injective since \(F\not\equiv0\), and is a topological embedding between Fréchet spaces: each defining seminorm on the range is a strictly positive constant times the corresponding disk seminorm. Its range is complete, hence closed in the complete metrizable space \(\mathscr E\). Polynomials in one disk variable show that this range is infinite dimensional.

**Step 4: failure of every local logarithmic trace.** Fix nonzero \(G\in\mathscr A\) and any open interval \(I\). Because \(G\) is analytic and not identically zero, \(t\mapsto G(2^{-1/2-it})\) is not identically zero on \(I\). Select a compact subinterval \(J\subset I\) of positive length and \(c>0\) so that \(|G(2^{-1/2-it})|>2c\) for \(t\in J\). Since \(2^{-\sigma-it}\) remains strictly inside the unit disk, continuity gives \(|G(2^{-1/2-\varepsilon-it})|\ge c\) for \(t\in J\) and all sufficiently small positive \(\varepsilon\). Along a sequence \(\varepsilon_\ell\downarrow0\), Step 2 gives \(\inf_{t\in J}|F(1/2+\varepsilon_\ell+it)|\to\infty\). Consequently
\[\int_I\log^+|F(\tfrac12+\varepsilon_\ell+it)G(2^{-1/2-\varepsilon_\ell-it})|\,dt\ge |J|\log(c M_\ell)\to\infty,\]
where \(M_\ell=\inf_{t\in J}|F(1/2+\varepsilon_\ell+it)|\), and \(\ell\) is large enough that \(cM_\ell>1\). A positive harmonic majorant on any boundary rectangle would give uniform boundedness of these local logarithmic traces on smaller compact intervals, by the classical local Nevanlinna trace criterion. Such a majorant therefore cannot exist at any critical-line point. This completes the proof.

## Verification
The analytical proof uses the published Harper low-moment theorem and proves the auxiliary Euler-summation, projection, Baire and independent-coordinate steps above. The standalone file `check.py` reproduces finite odd-block identities, tests bounded Euler-summation errors on sample finite Dirichlet polynomials, and verifies the finite-variable independent-coordinate norm identity. Its passing tests are consistency checks only and do not establish the infinite-dimensional assertions.

## Relationship to prior work
Allu and Mondal (2026, arXiv:2610.25002v1, Theorem 2.1 and Lemmas 2.2–2.4) construct a counterexample in each fixed \(\mathscr H^p\), \(0<p<2\), with divergent logarithmic mass on one prescribed interval. The present conclusion simultaneously covers **every** exponent below two and **every** critical-boundary interval, and identifies a **closed** infinite-dimensional space of counterexamples. Their paper supplies the natural problem and an efficient published low-moment ingredient, but does not state the simultaneous or spaceability conclusion.

Harper (arXiv:1703.06654, Theorem 1) proves the Steinhaus low-moment bound used here. Bayart (Studia Math. 167 (2005), 161–181) establishes abstract topological and algebraic genericity for divergent series, including Dirichlet **partial sums** in different ambient spaces; an algebraically generic dense vector subspace is not the same as a closed subspace of actual functions with divergent local logarithmic trace. Olsen and Saksman (arXiv:0907.2708) study local boundary interpolation for classical and Dirichlet Hardy spaces, especially at the Hilbert exponent, not the claimed below-two closed pathological subspace. No covering implication was identified in the inspected statements; historical priority still needs external expert assessment.

## Limitations
The existence proof is nonconstructive (Baire category), with no explicit coefficient formula for \(F\). The singularity asserts divergence along selected approaches; no convergence rate, pointwise divergence at every fixed approach speed, or membership in \(\mathscr H^2\) is claimed. The proof relies on Harper's difficult published low-moment theorem; the included finite checks cannot replace it. The stated originality comparison is evidence-based and does not certify world-wide uniqueness. No independent audit has been performed.

## References
1. V. Allu and D. K. Mondal, *Local Nevanlinna embedding for Hardy space of Dirichlet series below critical exponent*, arXiv:2610.25002v1 (2026-10-18), Theorem 2.1, Lemmas 2.1–2.4, https://arxiv.org/html/2610.25002v1.
2. A. J. Harper, *Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos*, Forum Math. Pi 8 (2020), e1, Theorem 1; arXiv:1703.06654, https://arxiv.org/pdf/1703.06654.
3. F. Bayart, *Topological and algebraic genericity of divergence and universality*, Studia Math. 167 (2005), 161–181, DOI:10.4064/sm167-2-4, https://www.impan.pl/shop/en/publication/transaction/download/product/89725.
4. J.-F. Olsen and E. Saksman, *On the boundary behaviour of the Hardy spaces of Dirichlet series and a frame bound estimate*, J. Reine Angew. Math. 663 (2012), 33–66; arXiv:0907.2708, https://arxiv.org/abs/0907.2708.
