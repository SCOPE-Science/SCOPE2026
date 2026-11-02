# Infinitely many hyperbolic cubic types on one positive-entropy isentrope

## Finding
Consider the one-parameter real cubic family, with \(1\le s\le s_*\),
\[
F_s(x)=1-A_sx^3-B_sx^2,\qquad A_s=1-\frac{1}{s^2(s+1)},\quad B_s=s+\frac{1}{s^2(s+1)},
\]
where \(s_*\) is the unique root greater than one of \(s^4+s^3-3s-2=0\). There exist infinitely many parameters \(s\in(109/100,11/10)\) such that both critical points of \(F_s\) eventually enter the same superattracting orbit \(0\mapsto1\mapsto-s\mapsto0\), yet their marked critical-orbit combinatorial types are pairwise different. In fact the least entry time of the second critical point into this three-cycle is unbounded. Every selected map is postcritically finite and hyperbolic. All selected maps belong to the constant positive-entropy isentrope with \(h_{\mathrm{top}}=\log\bigl((1+\sqrt5)/2\bigr)\) and share the Artin–Mazur zeta function
\[
\zeta(t)=\frac{1}{(1-t^3)(1-t^2)(1-t-t^2)}.
\]
The constant zeta formula and Fibonacci repeller are established for this entire family in the cited source; the new conclusion is the existence of infinitely many hyperbolic marked combinatorial types with the period of the attracting critical cycle fixed at three.

## Assumptions and scope
All parameters and phase points are real. The critical points are \(0\) and \(c_s=-2B_s/(3A_s)\); the critical value at the latter point is \(v_s=1-4B_s^3/(27A_s^2)\). A marked combinatorial type records the critical points in order and their forward-orbit relations, in particular first entrance into the marked period-three critical orbit. The dynamical entropy and zeta statement concerns the compact real invariant interval associated with the bounded critical-orbit dynamics of this cubic family, as in Olivares-Vinales's Proposition 7.1.

## Proof
**1. The fixed period-three orbit and common periodic-point data.** From the formulas, \(F_s(0)=1\), \(F_s(1)=-s\), and \(F_s(-s)=0\), and \(F_s'(0)=0\). For the interval \(I=[109/100,11/10]\), one has \(I\subset(1,s_*)\). Proposition 7.1 and its proof in the cited preprint establish the common displayed zeta function and the Fibonacci symbolic repeller for all \(s\in[1,s_*]\). Their hyperbolic members have a hyperbolic repelling complement to the attracting periodic orbit and the boundary two-cycle. The Fibonacci transition matrix has Perron eigenvalue \((1+\sqrt5)/2\), giving the claimed constant positive entropy for the hyperbolic maps constructed here.

**2. A uniform inverse branch.** Let \(J=[-1/2,-3/10]\) and \(G_s=F_s^2\). For all \(s\in I\), elementary rational bounds give
\[
59/100<A_s<61/100,\quad 149/100<B_s<3/2,
\]
\[
69/100<F_s(-1/2)<71/100,\qquad 88/100<F_s(-3/10)<89/100.
\]
Since \(F_s'(x)=-3A_sx^2-2B_sx\), the derivative is strictly positive on \(J\). Writing \(x=-u\), \(3/10\le u\le1/2\), its lower bound is
\[
F_s'(x)=2B_su-3A_su^2\ge2(149/100)(3/10)-3(61/100)(3/10)^2=7293/10000.
\]
The quadratic \(2B_su-3A_su^2\) is increasing on the indicated \(u\)-interval, since its derivative is bounded below by \(2(149/100)-3(61/100)>0\). For \(y\in F_s(J)\subset(69/100,89/100)\),
\[
-F_s'(y)=3A_sy^2+2B_sy>3(59/100)(69/100)^2+2(149/100)(69/100)>289/100.
\]
Therefore \(G_s'(x)<-2\) throughout \(J\). Because \(F_s\) decreases on the positive half-line, the same rational envelopes give
\[
G_s(-1/2)>1-(61/100)(71/100)^3-(3/2)(71/100)^2>0,
\]
\[
G_s(-3/10)<1-(59/100)(88/100)^3-(149/100)(88/100)^2<-1/2.
\]
Consequently \(G_s:J\to G_s(J)\) is a decreasing diffeomorphism and \([-1/2,0]\subset G_s(J)\). Its inverse branch \(h_s:[-1/2,0]\to J\) has Lipschitz constant less than \(1/2\), uniformly in \(s\). As \(J\subset[-1/2,0]\), \(h_s\) maps \(J\) into itself and has a unique fixed point \(p_s\in J\). Moreover,
\[
q_n(s):=h_s^{n}(0)\in J,\qquad F_s^{2n}(q_n(s))=0,
\]
with \(q_n(s)\to p_s\) uniformly as \(n\to\infty\). The pair \(p_s,F_s(p_s)\) is a repelling period-two orbit because \(p_s\in J\), \(F_s(p_s)\in(69/100,89/100)\), and \(|G_s'(p_s)|>2\). It is disjoint from the attracting three-cycle.

**3. Critical-value crossing.** The second critical value \(v_s\) depends continuously on \(s\). Direct rational substitution at the endpoints, with \(R_s=G_s(v_s)-v_s\), yields
\[
-1/2<v_{109/100},v_{11/10}<-3/10,\qquad R_{109/100}>1/20,\quad R_{11/10}<-1/10.
\]
All inequalities are certified by the accompanying exact-rational program, which evaluates the defining rational expressions without floating-point arithmetic. For a strictly decreasing map \(G_s\), the function \(G_s(x)-x\) is strictly decreasing, vanishing at \(p_s\). Hence \(v_{109/100}<p_{109/100}\), while \(v_{11/10}>p_{11/10}\). Uniform convergence \(q_n\to p_s\) now gives, for all sufficiently large integers \(n\),
\[
v_{109/100}<q_n(109/100),\qquad v_{11/10}>q_n(11/10).
\]
The inverse branch depends continuously on \(s\), so the intermediate value theorem gives \(s_n\in(109/100,11/10)\) with \(v_{s_n}=q_n(s_n)\). It follows that \(F_{s_n}^{2n+1}(c_{s_n})=0\). Both critical points therefore enter the superattracting period-three cycle, and \(F_{s_n}\) is a hyperbolic, postcritically finite real polynomial.

**4. Unbounded critical capture times.** Let \(m_n\) be the first time \(F_{s_n}^{m_n}(c_{s_n})\) belongs to the marked three-cycle. If an infinite subsequence of these times were bounded, a further subsequence would have a constant entry time \(m\) and parameters converging to \(\bar s\in I\). Since \(v_{s_n}=q_n(s_n)\to p_{\bar s}\) and \(F_{s_n}^{m-1}(v_{s_n})\) lies on the three-cycle, continuity would force a forward iterate of the repelling period-two point \(p_{\bar s}\) into the disjoint period-three orbit, impossible. Thus \(m_n\to\infty\). The first entry time into the distinguished periodic critical orbit is preserved by marked critical-orbit conjugacy, proving infinitely many combinatorial types while the attracting period and entropy remain fixed.

## Verification
Execute `python3 check_exact.py` using the standard library. The script checks the parameter envelopes, the uniform inverse-branch endpoint and derivative inequalities, the exact orbit identity, and both rational critical-value crossing signs. In particular it checks exact strict residual bounds \(R_{109/100}>1/20\) and \(R_{11/10}<-1/10\). All infinite-sequence, continuity and conjugacy conclusions are proved above analytically; the finite computation is used only for explicitly stated rational inequalities.

## Relationship to prior work
Olivares-Vinales (2024 preprint, first posted 17 May; 2025 journal publication) introduced the cubic family and proved the common rational zeta function in Proposition 7.1. That paper's Theorem 2(i) obtains infinitely many hyperbolic combinatorial types by **varying the attracting critical period**; Remark 1.1 expressly distinguishes this construction from the fixed-entropy question raised by Kozlovski (2019). The new inverse-branch crossing proves infinitely many hyperbolic types **inside this specific fixed-period-three family**, without importing the earlier varying-period construction as evidence of the claim. The present argument does not claim originality of the family, its Fibonacci repeller, or its zeta formula.

## Limitations
The parameter values are produced by intermediate-value arguments, not by closed formulas, and no uniqueness or spacing of the selected parameters is claimed. Their least preperiods are proved unbounded, not necessarily equal to \(2n+1\). The exact rational checker does not certify infinitely many crossings by enumeration. Completeness of the literature comparison, especially against the inaccessible full 2025 journal revision and uncatalogued work on fixed-entropy cubic capture loci, remains a priority risk; independent mathematical validation has not been performed.

## References
1. Jorge Olivares-Vinales, *The Artin-Mazur zeta function for interval maps*, arXiv:2405.10560, version first submitted 2024-05-17, especially Remark 1.1, Theorem 2, Proposition 7.1 and Lemma 7.2, https://arxiv.org/pdf/2405.10560.
2. Jorge Olivares-Vinales, *The Artin–Mazur zeta function for interval maps*, Journal of the London Mathematical Society, 112 (2025), e70308, https://doi.org/10.1112/jlms.70308.
3. O. Kozlovski, *On the structure of isentropes of real polynomials*, Journal of the London Mathematical Society 100 (2019), 159–182, cited as Question 2 in reference 1.
