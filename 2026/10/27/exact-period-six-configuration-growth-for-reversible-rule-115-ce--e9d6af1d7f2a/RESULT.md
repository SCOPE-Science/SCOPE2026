# Exact period-six configuration growth for reversible rule-115 cellular automata

## Finding

Consider the reversible elementary second-order cellular automaton based on Wolfram rule 115. Let \(F\) be its map on pairs of bi-infinite binary configurations. For each integer \(n\ge0\), let \(A_n\) be the number of pairs supported in the prescribed spatial interval \(\{0,\ldots,n-1\}\) and fixed by \(F^6\); let \(B_n\) count the analogous pairs fixed by \(F^3\). Outside the interval **both initial component configurations are zero**. Positions inside the interval need not be occupied.

The complete enumeration, for every \(n\ge0\), is

\[
\sum_{n\ge0}A_nz^n=\frac{1+5z^3}{(1-z+z^2)(1-z-5z^2)},\qquad
\sum_{n\ge0}B_nz^n=\frac{1+z}{1-z-z^2}.
\]

Every finite-support periodic orbit has period divisible by three (in particular this follows here by observing the three-phase evolution outside its initial support). Thus the exact number of initial pairs of *least* temporal period six is \(A_n-B_n\). Its first values, for \(n=0,1,\ldots,9\), are \(0,0,4,16,52,152,440,1248,3532,9912\). The first nontrivial six-cycle already occurs in a two-site initial window.

Writing \(\rho=(1+\sqrt{21})/2\) and \(\delta=(1-\sqrt{21})/2\), one has

\[
A_n=\left(\frac12+\frac{13\sqrt{21}}{126}\right)\rho^n+O(|\delta|^n).
\]

Consequently the window-growth exponent for period-at-most-six configurations is exactly \(\log\rho\). Among the \(4^n\) binary initial pairs in an \(n\)-site window, the proportion of six-periodic pairs decays exponentially at rate \(\rho/4\). Within the six-periodic pairs, the fraction of least-period-six points tends to one because \(B_n\) grows only at the golden-ratio rate.

## Assumptions and scope

The two component configurations are bi-infinite maps \(m,c:\mathbb Z\to\mathbb F_2\). Write \(x_0=m\), \(x_1=c\), and for all \(t\ge1\), \(i\in\mathbb Z\), define

\[
x_{t+1}(i)=x_{t-1}(i)\oplus f(x_t(i-1),x_t(i),x_t(i+1)),
\]

where \(\oplus\) is addition modulo two and

\[
f(\ell,b,r)=\neg b\ \lor\ (\ell\land\neg r).
\]

This is precisely Wolfram rule 115 (its outputs at neighborhoods 111 through 000 are 01110011). The map \(F\) sends \((x_0,x_1)\) to \((x_1,x_2)\); it is invertible by the second-order recurrence. A pair is supported in \(\{0,\ldots,n-1\}\) when both components vanish outside that set, and the empty window \(n=0\) permits only the zero pair. We count **labeled positions**, not translation classes or spatially periodic rings. Temporal period means period under \(F\), not the shift action.

## Proof

**1. A one-column boundary shield.** With zero initial components, the constant-in-space background follows the time sequence \(0,0,1,0,0,1,\ldots\). Indeed, \(f(\ell,0,r)=1\) and \(f(\ell,1,1)=0\), irrespective of \(\ell,r\). For any pair initially zero at every site \(i\ge n\), these identities inductively force every site \(i\ge n\) to follow that background sequence forever, despite activity on its left.

At the other end, if both components initially vanish for all \(i<0\), all sites \(i\le-2\) follow the background forever, while the adjacent site \(-1\) is forced to equal one at times \(3k+2\). To check this directly, start with the fact that all sites \(i<0\) equal one at time two. Suppose the stated pattern holds through time \(3k+2\). For \(i\le-2\), its right neighbor equals one at that time; the recurrence and the two identities above give its next three values \(0,0,1\). At site \(-1\), write \(s=x_{3k+3}(-1)\), which can depend on the initial interior. Since site \(-2\) has value zero at the next two times, the recurrence gives \(x_{3k+4}(-1)=s\) and \(x_{3k+5}(-1)=s\oplus\neg s=1\). This closes the simultaneous induction. Therefore any temporally periodic finite-support trajectory has only one potentially non-background temporal column outside its initial window, at \(-1\).

**2. Temporal-column transfer.** Fix \(p\in\{3,6\}\). For a \(p\)-periodic trajectory write its length-\(p\) temporal column at site \(i\) as \(v_i=(x_0(i),\ldots,x_{p-1}(i))\in\{0,1\}^p\). Regard each column as an integer whose bit in position \(t\) is \(x_t(i)\). Let \(b_p\) denote the background column, whose bits are one precisely for \(t\equiv2\pmod3\); thus \(b_3=4\) and \(b_6=36\).

Make a directed graph with vertices all ordered pairs \((a,b)\) of temporal columns. There is an edge \((a,b)\to(b,c)\) precisely if, for *each* \(t\in\mathbb Z/p\mathbb Z\),

\[
b(t+1)\oplus b(t-1)=f(a(t),b(t),c(t)).
\]

The edge condition is exactly the cellular automaton recurrence at the middle spatial site. By the boundary shield, an initial pair supported in \(\{0,\ldots,n-1\}\) yields a path beginning at the background vertex \((b_p,b_p)\), adding a column at site \(-1\) whose first two bits vanish, adding the \(n\) freely chosen interior columns, then adding two background columns at sites \(n,n+1\), and terminating at \((b_p,b_p)\). Conversely, such a path extended by background columns at both ends yields a valid \(p\)-periodic trajectory and a unique allowed initial pair. Hence the path correspondence is a bijection, not merely an upper bound.

Retain only graph vertices both reachable from and able to reach \((b_p,b_p)\), and call the resulting adjacency matrix \(M_p\). Let the row \(u_p\) count the possible first edges obeying the two-zero-bit halo restriction. Let the column \(v_p\) count the possible two final background edges. The exact window count is therefore

\[
A_n=u_6M_6^nv_6,\qquad B_n=u_3M_3^nv_3.
\]

**3. Finite exact recurrence certificate.** An exhaustive application of the explicitly stated six-bit edge condition (at most \(64^3\) temporal-column triples) gives 27 retained vertices for \(p=6\) and three for \(p=3\). The accompanying standalone, dependency-free `verify.py` generates these graphs directly from the eight truth-table bits and checks the following scalar identities *exactly*, using arbitrary-precision integers:

\[
\begin{aligned}
B_{j+2}-B_{j+1}-B_j&=0 &&(0\le j<3),\\
A_{j+4}-2A_{j+3}-3A_{j+2}+4A_{j+1}-5A_j&=0 &&(0\le j<27).
\end{aligned}
\]

These **finite exact identities entail the recurrences for every** \(j\ge0\): each left-hand-side sequence is a scalar matrix coefficient \(u_pM_p^jP(M_p)v_p\); by Cayley–Hamilton it satisfies a recurrence of degree at most the dimension of \(M_p\). The first dimension-many zero values force every later value to vanish. This argument is an infinite proof from a finite complete certificate, not extrapolation from a table.

The same exact code checks the initial values \((B_0,B_1)=(1,2)\) and \((A_0,A_1,A_2,A_3)=(1,2,7,21)\). Summing the resulting recurrences gives the displayed rational generating functions; explicitly, the denominator for the six-period count expands to \(1-2z-3z^2+4z^3-5z^4\).

**4. Exact periods and asymptotics.** Outside the initial window the temporal background has least period three, so any period of a finite-support pair must be divisible by three. Of the divisors of six only three and six remain, giving \(A_n-B_n\) for least period six. The rational function for \(B_n\) gives \(B_n=F_{n+2}\), with Fibonacci numbers \(F_0=0,F_1=1\). The dominant simple pole of the rational function for \(A_n\) is \(z=1/\rho\), with residue coefficient \(\tfrac12+13\sqrt{21}/126\). The other poles correspond to \(\delta\) and to two unit-modulus roots; hence the stated asymptotic error. Since \(1<\frac{1+\sqrt5}{2}<\rho<4\), all growth and density conclusions follow.

## Verification

Run `python3 verify.py` (Python 3, standard library only). It constructs every legal temporal-column triple for \(p=3,6\), reduces the complete graphs to the exactly relevant vertices, computes the boundary row/column vectors, checks the initial values and the 3/27 exact recurrence identities whose validity for all subsequent terms follows by Cayley–Hamilton. As a logically separate test, it directly evolves all \(4^n\) initial pairs in windows \(0\le n\le7\), representing the infinite background by finite sets of deviations. These independently reproduce the period-three and period-six enumerations, including the first genuinely six-periodic two-site states. The direct finite tests do not replace the all-length transfer-matrix proof.

## Relationship to prior work

Formenti and Kamilya, *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115* (public preprint June 11, 2026), define the same update rule, establish periodicity for all finite initial pairs, prove the period-divisible-by-three obstruction, exhibit example periods and investigate special families of period functions. The main source's sections 2–7, including its concluding list of observed periods, do not state the present complete all-window period-three/period-six generating functions, recurrence or spatial growth exponent. Our proof independently reconstructs the needed boundary properties.

Related published mathematical results on the absence of least temporal periods nine and eighteen for finite-support rule-115 states address different iterates: they establish the implication \(F^9=\mathrm{id}\Rightarrow F^3=\mathrm{id}\) and \(F^{18}=\mathrm{id}\Rightarrow F^6=\mathrm{id}\) on finite-support configurations, but do not by those implications determine the multiplicity of six-periodic states in each finite window. General finite-state transfer-matrix methods imply rationality for fixed temporal periods; the explicit polynomial numerator, denominator, Fibonacci comparison and sharp growth constant are the specialized contribution.

## Limitations

This is a count of temporal periods dividing three and six, not of every possible period or of translation-equivalence classes. The temporal-column matrix reduction is exact but computer-assisted; all critical finite assertions and independent small-size checks are reproducible in the supplied code. The 2024 precursor *On Elementary Second Order Cellular Automata* was available only in bibliographic/abstract form during the literature comparison, so historical priority under a different formulation remains a residual risk. The mathematical proof itself does not depend on that precursor. No independent mathematical audit has been performed.

## References

1. Enrico Formenti and Supreeti Kamilya, *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115*, EPTCS 445 (2026), 95–103, arXiv:2606.13159v1, https://arxiv.org/abs/2606.13159 ; openly readable full text: https://www.researchgate.net/publication/406975127_The_Curious_Case_of_Reversible_Elementary_Second_Order_Cellular_Automaton_115 . First public posting June 11, 2026.
2. Enrico Formenti and Supreeti Kamilya, *On Elementary Second Order Cellular Automata*, Cellular Automata Technology, ASCAT 2024, 204–218, DOI:10.1007/978-3-031-56943-2_16 (bibliographic and abstract access only).
3. *Two absent finite-support periods for reversible rule-115 cellular automata*, mathematical record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-two-absent-finite-support-periods-for-reversible-rule-115-cellul--692b925dfcdf (indexed scientific statement available; complete source text not independently retrieved).
4. Cayley–Hamilton theorem and rational transfer-matrix counting (standard finite-dimensional linear algebra).
