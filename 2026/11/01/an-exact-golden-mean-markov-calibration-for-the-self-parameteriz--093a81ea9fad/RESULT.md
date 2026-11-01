# An exact golden-mean Markov calibration for the self-parameterized quadratic tent map

## Finding

For the continuous interval map of Paul, Dhungel, Sadia, Hossain and Hasan's self-parameterized tent construction,
\[
T_C(x)=\left(\frac{37}{25}+\frac C4+\frac x4\right)\min\{x,1-x\},\qquad x\in[0,1],\quad C\in[0,1],
\]
there is exactly one parameter for which the turning point \(c=1/2\) has **least period three**:
\[
C_*=\frac{100\sqrt{337}-1789}{450}=0.103902166819070955\ldots.
\]
At \(C=C_*\), put
\[
q=\frac{\sqrt{337}-7}{36},\qquad h=\frac{\sqrt{337}+11}{36},\qquad I=[q,h].
\]
The critical cycle is \(c\mapsto h\mapsto q\mapsto c\). The core \(I\) is forward invariant, and every orbit whose initial state is in \((0,1)\) enters \(I\) after finitely many steps. The endpoint \(1\) maps to the exterior fixed point \(0\).

With cells \(A=[q,c]\) and \(B=[c,h]\), the map is expanding on each monotonicity cell and has the exact covering relations \(T_{C_*}(A)=B\), \(T_{C_*}(B)=A\cup B\). Thus its core is a two-state Markov system with transition matrix
\[
M=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
For **every** integer \(n\geq1\), the number of distinct fixed points of the \(n\)-th iterate on the full interval is exactly
\[
\#\operatorname{Fix}(T_{C_*}^{n}|_{[0,1]})=1+L_n,
\]
where \(L_0=2\), \(L_1=1\), \(L_{n+2}=L_{n+1}+L_n\) are the Lucas numbers. Consequently the Artin–Mazur zeta function and full-interval topological entropy are
\[
\boxed{\zeta_{T_{C_*}}(z)=\frac{1}{(1-z)(1-z-z^2)}},\qquad
\boxed{h_{\mathrm{top}}(T_{C_*})=\log\frac{1+\sqrt5}{2}}.
\]
The core dynamics is topologically mixing. These formulas concern the ideal real-valued map, not a finite-precision implementation or cryptographic security.

## Assumptions and scope

The interval and parameter ranges are exactly those displayed above. At \(x=1/2\) the two formulas agree and equal \(h(C)\). The fixed-point count includes the exterior fixed point \(0\), which is absent from the Markov core. Fixed points of an iterate are **points**, not geometrically distinct periodic cycles; the corresponding least-period-\(n\) cycle count is
\[
\frac1n\sum_{d\mid n}\mu(n/d)(1+L_d),\qquad n\geq1,
\]
with the ordinary number-theoretic Möbius function \(\mu\). The zeta identity is an identity of formal power series (also analytic for sufficiently small \(|z|\)). The uniqueness assertion for \(C_*\) concerns critical period three in the entire physical control interval \([0,1]\), not arbitrary critical itineraries or other maps.

## Proof

**1. Critical-orbit equation and unique calibration.** Write \(a(C)=37/25+C/4\), so the left branch is \(a(C)x+x^2/4\) and the right branch is \((a(C)+x/4)(1-x)\). The critical height and its next image are
\[
h(C)=T_C(1/2)=\frac{321}{400}+\frac C8,
\qquad
q(C)=T_C(h(C))=\frac{212431}{640000}-\frac{989}{6400}C-\frac9{256}C^2.
\]
For all \(0\leq C\leq1\), one has \(1/2<h(C)<1\) and \(0<q(C)<1/2\). The second claim follows because \(q\) decreases throughout this interval and its endpoints are \(q(0)=212431/640000\) and \(q(1)=91031/640000\). Hence \(T_C^3(1/2)=q(C)(a(C)+q(C)/4)\), and exact expansion gives
\[
T_C^3(1/2)-\frac12
=\frac{(50C+121)(450C-13511)(22500C^2+178900C-18831)}{1638400000000}.
\]
The first factor is positive and the second negative throughout \([0,1]\). The quadratic factor is strictly increasing, negative at zero and positive at one; therefore it has precisely one zero there. Solving it yields the stated \(C_*\). Exact substitution gives
\[
T_{C_*}(1/2)=h,\qquad T_{C_*}(h)=q,\qquad T_{C_*}(q)=1/2,
\]
with \(0<q<1/2<h<1\). As these three values differ, the critical point has least period three.

**2. Exact Markov dynamics and global periodic-point location.** Since \(T_{C_*}\) strictly increases on \(A=[q,1/2]\) and strictly decreases on \(B=[1/2,h]\), the endpoint images prove \(T(A)=B\) and \(T(B)=I\), and in particular \(T(I)=I\). On the left branch the derivative is \(a+x/2\); on the right branch its absolute value is \(a-1/4+x/2\). Both are at least \(a>37/25>1\) on their respective branches. Thus each inverse branch on its image is a strict contraction.

For \(0<x<q\), \(T(x)=x(a+x/4)>x\), and \(T([0,q])=[0,1/2]\). A positive orbit remaining forever below \(q\) would increase to a positive fixed point in \([0,q]\), impossible because \(T(x)>x\) there. Therefore it enters \(I\) in finite time. For \(h<x<1\), the first image lies in \((0,q)\) and subsequently enters \(I\); \(T(1)=0\), while \(T(0)=0\). Thus every periodic point lies in \(I\cup\{0\}\), and \(0\notin I\).

**3. Count every periodic point without boundary overcounting.** Let \(M_{ij}=1\) exactly when \(T(J_i)\supseteq J_j\), for \(J_A=A\), \(J_B=B\). The above image relations give \(M\). For any cyclic admissible word of length \(n\), composing its \(n\) prescribed inverse branches gives a strict contraction of the first cell into itself, hence a unique point fixed by \(T^n\). Conversely, every \(n\)-periodic point in \(I\) supplies at least one admissible cyclic word. A point can have two cell symbols only at the shared endpoint \(c\). The only periodic orbit meeting \(c\) is \(c\to h\to q\to c\); at each visit to \(c\) its predecessor is \(q\), which lies in \(A\). Since \(M_{AA}=0\), a **cyclic** admissible coding must assign \(B\) to \(c\), so no periodic orbit is counted twice. This proves the bijection between periodic symbolic words and physical periodic points, with
\[
\#\operatorname{Fix}(T^n|_I)=\operatorname{tr}(M^n)=L_n.
\]
Adding the isolated fixed point zero proves the stated full count. The trace identity follows from the characteristic polynomial \(\lambda^2-\lambda-1\), which gives the Lucas initial values and recurrence.

**4. Zeta, entropy, and mixing.** The determinant identity for a finite matrix gives
\[
\exp\biggl(\sum_{n\ge1}\frac{\operatorname{tr}(M^n)z^n}{n}\biggr)=\frac1{\det(I_2-zM)}=\frac1{1-z-z^2}.
\]
The additional fixed point zero contributes the factor \((1-z)^{-1}\), proving the zeta formula. The piecewise expanding Markov partition yields the usual finite-to-one symbolic coding of the invariant core by the subshift of finite type defined by \(M\), and therefore \(h_{\mathrm{top}}(T|_I)=\log\rho(M)\). Since \(M^2\) has strictly positive entries, that core subshift is mixing, and the continuous factor on \(I\) is mixing. Points in \((0,q)\cup(h,1]\) are transient or wandering: their forward orbits enter \(I\) and never return outside \(I\), apart from the endpoint \(1\) mapping to \(0\). The nonwandering set on \([0,1]\) is precisely \(I\cup\{0\}\). The standard invariance of topological entropy under restriction to the nonwandering set then gives \(h_{\mathrm{top}}(T)=\log\rho(M)=\log((1+\sqrt5)/2)\).

## Verification

The accompanying standalone file `verify_markov.py` checks the factorization and all radical identities in exact algebraic arithmetic; proves the control-root rational bracket \(0.103902<C_*<0.103903\); verifies the Lucas trace identity; and independently constructs every cyclic admissible inverse-branch orbit of lengths one through eight at 65-decimal-digit precision. Every constructed orbit returns within prescribed error tolerance and no two codes within each period represent the same numerical point. The exact proof above, not this finite enumeration, establishes the unrestricted \(n\)-statements. The exact algebraic checks require SymPy; the numerical crosschecks require mpmath.

## Relationship to prior work

Paul et al. introduce the self-parameterized tent branch with the coefficients used here, analyze transfer curves, bifurcation diagrams, Lyapunov exponents and hardware performance, but the inspected Table 2, Sections 2–3, and concluding material do not derive a postcritically finite algebraic calibration, complete all-period census, Artin–Mazur zeta, or exact entropy. A 2021 conference precursor by the same group describes self-parameterization and remains a textual coverage risk because its complete proceedings text was not available for inspection. General unimodal symbolic-dynamics and kneading results (e.g. Alsedà–Misiurewicz–Pérez) provide the standard Markov-counting tools conditional on a Markov partition; they do not compute this map's unique algebraic control value or its global exceptional fixed point and exact count. The novelty claimed is therefore the specific **verified algebraic calibration and complete global periodic orbit classification** for this source family, not an invention of Markov or kneading theory.

## Limitations

The exact entropy and zeta formulas are asserted only at \(C=C_*\); no formula is claimed for other controls. The result is for ideal exact real arithmetic and does not validate digitized recurrence properties, random-number security or analog noise robustness. The source's full publisher PDF could not be retrieved during inspection, and the related conference paper was not materially available; this leaves a genuine bibliographic-priority risk. The algorithmic checks are finite and do not replace the proof. Independent audit has not been performed.

## References

1. P. S. Paul, A. Dhungel, M. Sadia, M. R. Hossain, and M. S. Hasan, “Self-Parameterized Chaotic Map for Low-Cost Robust Chaos,” *Journal of Low Power Electronics and Applications* **13** (2023), 18, DOI: 10.3390/jlpea13010018. Public article dated 13 February 2023; Table 2 and Sections 2–3 establish the defining formula.
2. P. S. Paul et al., “Self-Parameterized Chaotic Map: A Hardware-efficient Scheme Providing Wide Chaotic Range,” *ICECS 2021*, pp. 1–5. Earlier precursor; exact accessible publication day and full material not verified.
3. L. Alsedà, M. Misiurewicz, and R. A. Pérez, “Flexibility of Entropies for Piecewise Expanding Unimodal Maps,” arXiv:2004.01813 (2020), especially Section 2 on expanding unimodal cores and classical symbolic methods.
4. J. Milnor and W. Thurston, “On Iterated Maps of the Interval,” classical kneading theory, in *Dynamical Systems* (Lecture Notes in Mathematics 1342), 1988. Cited for background methods, not as a source of the model-specific computation.
