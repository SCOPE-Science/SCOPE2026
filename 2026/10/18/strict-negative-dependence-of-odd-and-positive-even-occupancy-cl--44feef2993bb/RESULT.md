# Strict negative dependence of odd and positive-even occupancy classes

## Finding
For integers \(m\ge2\) and \(n\ge1\), independently allocate \(n\) labeled balls uniformly into \(m\) labeled boxes. Let \(N_i\) be the number in box \(i\), and define
\[
O=\sum_{i=1}^{m}\mathbf1\{N_i\text{ is odd}\},\qquad
E=\sum_{i=1}^{m}\mathbf1\{N_i\ge2\text{ is even}\}.
\]
Then the covariance has the complete sharp sign classification
\[
\operatorname{Cov}(O,E)=0\quad\Longleftrightarrow\quad
n=1\ \text{or}\ (m=2\text{ and }n\text{ is odd}),
\]
and it is strictly negative otherwise. Write \(a=(m-1)/m\), \(b=(m-2)/m\), \(c=(m-3)/m\), and \(d=(m-4)/m\). The exact value is
\[
\operatorname{Cov}(O,E)=\frac m4\left[
-1-(m-1)d^n+2a^n+2(m-1)c^n+mb^{2n}-2ma^nb^n
\right].
\]
Here integer powers of possibly negative \(c,d\) are intended when \(m=2,3\).

More generally, allocate independently to boxes with arbitrary positive probabilities \(p_1,\ldots,p_m\) summing to one. If \(n\ge2\) and \(p_i+p_j\le1/2\) for every distinct \(i,j\), then \(\operatorname{Cov}(O,E)<0\). This supplies a nonuniform, diffuse-mass regime of the same strict negative dependence.

For uniform allocations with \(n/m\to\lambda\in(0,\infty)\), the covariance admits the extensive limit
\[
\frac{\operatorname{Cov}(O,E)}m\longrightarrow
-\frac{(1-e^{-2\lambda})(1-e^{-\lambda})^2}{4}
-\lambda(e^{-3\lambda}-e^{-4\lambda})<0.
\]
The separate-box cross-covariance need not share the sign of the aggregate: at \(m=n=3\), it is \(1/243>0\), while \(\operatorname{Cov}(O,E)=-8/27\).

## Assumptions and scope
Allocation outcomes are independent draws from a fixed discrete distribution. The indicators in \(O\) and \(E\) partition the positive odd and positive even load classes; a zero-load box belongs to neither. No Poissonization is used. The generalization requires strictly positive probabilities and the stated pair-mass bound. The limiting formula assumes both \(m\) and \(n\) diverge, with positive finite limiting ratio.

## Proof
For uniform allocation, a fixed box has odd probability \(p_O=(1-b^n)/2\) by the parity generating function, and positive-even probability \(p_E=(1+b^n)/2-a^n\). For distinct boxes \(i,j\), the parity identity for their multinomial counts and subtraction of the zero-load event give
\[
\mathbb P(N_i\text{ odd},\ N_j\ge2\text{ even})
=\frac{1-d^n}{4}-\frac{a^n-c^n}{2}.
\]
Consequently,
\[
4\operatorname{Cov}(\mathbf1\{N_i\text{ odd}\},
\mathbf1\{N_j\ge2\text{ even}\})
=b^{2n}-d^n+2c^n-2(ab)^n.
\]
For a common box the covariance is \(-p_Op_E\), since the two events are mutually exclusive. Summing over same and distinct ordered box pairs gives the stated exact formula.

If \(m\ge4\) and \(n\ge2\), take \(x=1/m\), \(\delta=2x^2\), and \(f(t)=t^n\) on nonnegative \(t\). Observe \(b^2=d+2\delta\), \(ab=c+\delta\), and \(c=d+x\), with \(0<\delta<x\). Since \(f'\) is strictly increasing,
\[
\begin{split}
f(d+2\delta)-f(d)&=2\int_0^\delta f'(d+2u)\,du\\
&<2\int_0^\delta f'(c+u)\,du
=2[f(c+\delta)-f(c)].
\end{split}
\]
Thus every distinct-box cross-covariance is negative. The within-box covariances are strictly negative too, proving the result for \(m\ge4\).

For \(m=3\), use that \(O\) has the same parity as \(n\). If \(n\ge3\) is odd, \(O\in\{1,3\}\), and \(E=0\) on \(O=3\). Both \(\mathbb P(O=3)>0\) (counts \((n-2,1,1)\)) and \(\mathbb E[E]>0\) (counts \((n-2,2,0)\)) hold, so
\(\operatorname{Cov}(O,E)=-2\mathbb P(O=3)\mathbb E[E]<0\).
If \(n\ge2\) is even, \(O\in\{0,2\}\). Conditional on \(O=0\), at least one load is positive and even, so \(E\ge1\); conditional on \(O=2\), \(E\le1\) and \(E=0\) has positive probability (counts \((n-1,1,0)\)). Both parity states have positive probability. Negative covariance follows from the strict conditional-mean inequality.

For \(m=2\), an odd total count forces \(O=1\); if the total is even and positive, \(O\) is either zero or two, while \(E\) is positive exactly in the first case. Both cases occur. Finally, for \(n=1\), \(E=0\) identically. This exhausts all cases.

For nonuniform allocation, write \(p=p_i\), \(q=p_j\), \(d=1-2p-2q\), \(c=d+q\), \(\delta=2pq\), \(s=1-2p\), and \(t=1-2q\). Exactly as above,
\[
4\operatorname{Cov}(\mathbf1\{N_i\text{ odd}\},\mathbf1\{N_j\ge2\text{ even}\})
=(st)^n-d^n+2c^n-2[s(1-q)]^n.
\]
Under \(p+q\le1/2\), \(d\ge0\), \(st=d+2\delta\), \(s(1-q)=c+\delta\), and \(0<\delta<q\). The same strict integral comparison makes each cross-box covariance negative for \(n\ge2\). Each within-box covariance is negative, since both events have positive probability. Summation proves the nonuniform assertion.

For the limit, the one-box marginal probabilities tend respectively to \((1-e^{-2\lambda})/2\) and \((1-e^{-\lambda})^2/2\). The exact distinct-box covariance above satisfies
\[
m\operatorname{Cov}(\mathbf1\{N_i\text{ odd}\},\mathbf1\{N_j\ge2\text{ even}\})
\to-\lambda(e^{-3\lambda}-e^{-4\lambda}).
\]
This follows by expanding \((1-k/m)^n\) to first order in \(1/m\) while retaining the actual ratio \(n/m\). Summing the \(m\) diagonal and \(m(m-1)\) off-diagonal terms yields the limit.

## Verification
The accompanying `verify_parity_occupancy.py` uses only the Python standard library. It independently enumerates all allocation sequences for selected small \(m,n\) and compares their exact rational covariances with the displayed formula. Further rational-arithmetic checks verify the sharp sign cases, the individual cross-box signs, and the diffuse nonuniform pair formula. Run `python verify_parity_occupancy.py`. These are finite cross-checks of, not substitutes for, the analytic proof.

## Relationship to prior work
Ben-Hamou, Boucheron and Ohannessian (2014) develop occupancy-count concentration and urn negative-dependence methods. Dubhashi and Ranjan's balls-and-bins theory supplies negative-association principles for monotone load functions, but parity-class indicators are not monotone functions of loads; consequently ordinary negative association does not directly imply the present sign theorem. A later general exact factorial-moment treatment of occupancy gives a broad route to mixed moment calculations, without itself stating this sharp parity sign classification or the diffuse-mass extension. The contribution here is the strict sign/equality classification, its elementary convexity mechanism, the local opposite-sign phenomenon, and its nonuniform and extensive consequences, not the existence of general occupancy moment formulas.

## Limitations
This theorem establishes negative covariance, not negative association, stochastic ordering, or independence. Under arbitrary uneven probabilities the sign need not follow from this proof: only the explicitly stated pair-mass condition is asserted. The extensive limit is confined to positive finite load density. Existing general moment formulas may allow an implicit alternative derivation; mathematical priority requires independent literature review.

## References
- A. Ben-Hamou, S. Boucheron and M. I. Ohannessian, *Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications*, arXiv:1412.8652 (first public version, 2014-12-30).
- D. Dubhashi and D. Ranjan, *Balls and Bins: A Study in Negative Dependence*, BRICS Research Series RS-96-25 (1996), https://www.brics.dk/RS/96/25/BRICS-RS-96-25.pdf.
- *A Unified Exact Factorial-Moment Theory for Multi-set Allocation Occupancy (MAO) in Finite Populations*, arXiv:2608.23998 (2026).
