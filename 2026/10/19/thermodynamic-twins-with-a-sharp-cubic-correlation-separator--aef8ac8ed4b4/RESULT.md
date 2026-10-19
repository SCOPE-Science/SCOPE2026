# Thermodynamic twins with a sharp cubic correlation separator

## Finding

There are two explicit continuous, nonconjugate maps \(A,B:[0,1]\to[0,1]\) with the same periodic orbits and the same square such that the following *stronger statistical coincidence* holds: for every starting point, all finite occupation measures differ by at most one displaced atom; the maximal normalized Wasserstein discrepancy is known exactly; and the invariant-measure simplices, pressure functions for **every** continuous potential, and equilibrium-state sets coincide. Yet their stationary lag-one autocorrelations differ. On the natural central invariant probability, polynomial observables of degree at most two cannot distinguish them by this autocorrelation, but cubic observables can, with an exact coefficient.

Specifically, if \(E_n^T(x)=n^{-1}\sum_{j=0}^{n-1}\delta_{T^j(x)}\) and \(m=\lfloor n/2\rfloor\), then

\[
\sup_{x\in[0,1]} W_1(E_n^A(x),E_n^B(x))=\frac{1-3^{-m}}{4n}\quad(n\ge1).
\]

For every continuous potential \(\varphi\) one has \(P(A,\varphi)=P(B,\varphi)\), with exactly the same equilibrium measures. In contrast, writing \(q(x)=a_0+a_1x+a_2x^2+a_3x^3\), the common central stationary probability \(\mu\) satisfies

\[
\operatorname{Cov}_{\mu}(q,q\circ A)-\operatorname{Cov}_{\mu}(q,q\circ B)=-\frac{a_3(2a_2+3a_3)}{414720}.
\]

Thus this lag-one autocorrelation agrees for every quadratic polynomial but differs by \(-1/138240\) for \(q(x)=x^3\). The source already supplies the nonconjugate periodic-orbit example; novelty assessed here is solely the exact statistical and thermodynamic distinction/coincidence above.

## Assumptions and scope

All intervals have their usual Euclidean metric. Set \(a=1/4\), \(b=1/2\), \(K=[a,b]\), \(R=[b,1-a]\), and \(r(x)=1-x\). Define continuous full-branch maps

\[
 g(x)=\tfrac14|8x-1|\quad(0\le x\le a),\qquad f(x)=\tfrac14\bigl(1+\bigl||12x-4|-1\bigr|\bigr)\quad(a\le x\le b).
\]

Define \(A\) on the four successive intervals \([0,a],K,R,[1-a,1]\) by \(r\circ g,r\circ f,r,r\), respectively, and \(B\) by \(r\circ g,r,f\circ r,r\), respectively. Endpoint definitions agree, so these are continuous maps of the unit interval. These are the explicit functions displayed in Example 5.2 of Fuhrmann--Gröger--Passeggi (2026), not newly discovered maps.

Let \(\lambda_K\) and \(\lambda_R\) be normalized Lebesgue probabilities on \(K\) and \(R\). The stationary central probability is \(\mu=(\lambda_K+\lambda_R)/2\). The notation \(P(T,\varphi)\) means the variational topological pressure of a continuous interval map with continuous potential. The covariance is \(\int q(x)q(Tx)\,d\mu-[\int q\,d\mu]^2\); the mean is the same for both maps. There are no genericity assumptions on \(\varphi\).

## Proof

**1. Exact orbit coupling.** Both maps preserve the outer pair \([0,a]\cup[1-a,1]\), where they coincide. Both preserve the middle interval \(K\cup R\); on it \(A^2=B^2\), equal to \(f\) on \(K\) and \(r\circ f\circ r\) on \(R\). If \(x\in K\), even iterates coincide and equal \(f^j(x)\), whereas the odd iterates are \(r f^{j+1}(x)\) for \(A\) and \(r f^j(x)\) for \(B\). If \(x=r(y)\in R\), the respective odd iterates are \(f^j(y)\) and \(f^{j+1}(y)\). Telescoping the odd positions for \(m=\lfloor n/2\rfloor\) yields the exact signed-measure formulas

\[
 n(E_n^A(x)-E_n^B(x))=\begin{cases}
 \delta_{r f^m(x)}-\delta_{r(x)},&x\in K,\\
 \delta_y-\delta_{f^m(y)},&x=r(y)\in R,\\
 0,&x\notin K\cup R.
\end{cases}
\]

At the overlap and outer endpoints the displayed values agree, as \(f(a)=a\), \(f(b)=b\). By the Kantorovich--Rubinstein dual formula on \([0,1]\), the Wasserstein distance of two probabilities whose signed difference is \((\delta_u-\delta_v)/n\) equals \(|u-v|/n\). Thus the maximum sought is \(n^{-1}\max_{y\in K}|f^m(y)-y|\).

**2. Sharp finite-time constant.** The map \(f\) has three full affine branches, slopes \(+3,-3,+3\), each covering \(K\). Accordingly \(f^m\) has \(3^m\) monotone affine full branches on the equal mesh of size \(\ell=(b-a)3^{-m}\), with endpoints mapped to \(a\) or \(b\). The function \(f^m(y)-y\) is affine on each mesh cell, hence its maximum absolute value is at a mesh vertex. Any vertex mapped to \(b\), other than the right endpoint itself, has \(y\ge a+\ell\), hence positive displacement at most \((b-a)-\ell\). Any vertex mapped to \(a\), other than the left endpoint itself, has \(y\le b-\ell\), giving the same negative bound. The first full branch maps \(a+\ell\) to \(b\), so the bound is achieved. For \(m=0\), the identity map gives zero. Since \(b-a=1/4\), the stated equality follows for every integer \(n\ge1\). In particular \(n\sup_x W_1\to1/4\), so the uniform \(1/n\) scale and its coefficient are sharp.

**3. Stationary and thermodynamic consequences.** The signed-measure identity shows for each bounded observable \(\varphi\) that the difference of length-\(n\) orbit sums is at most the oscillation of \(\varphi\) on \([0,1]\). If \(\nu\) is \(A\)-invariant, averaging the \(B\)-pushforwards of \(\nu\) therefore converges weakly to \(\nu\); its failure to be \(B\)-invariant tends to zero, hence \(B_*\nu=\nu\). Interchange \(A\) and \(B\) to get equality of the entire invariant probability simplices. Since \(A^2=B^2\), the measure-theoretic iterate formula gives \(h_\nu(A)=\frac12h_\nu(A^2)=\frac12h_\nu(B^2)=h_\nu(B)\) on the common simplex. The variational principle now gives \(P(A,\varphi)=P(B,\varphi)\) and identity of the maximizing (equilibrium) measure sets, including whenever they are empty. This also makes the Birkhoff pointwise limit sets identical for every bounded observable, wherever the latter are defined.

**4. A stationary covariance separation.** The map \(f\) preserves \(\lambda_K\) because it has three full branches of absolute slope three. Consequently \(\mu\) is invariant under both \(A\) and \(B\). For any observable \(q\), direct change of variables using \(y\) uniform on \(K\) gives

\[
 \Delta(q):=\int q(x)q(Ax)\,d\mu-\int q(x)q(Bx)\,d\mu
 =\frac{1}{2(b-a)}\int_a^b\big[q(y)q(1-f(y))-q(1-y)q(f(y))\big]dy.
\]

The three affine pieces of \(f\) are, respectively, \(a+3(y-a)\) on \([1/4,1/3]\), \(b-3(y-1/3)\) on \([1/3,5/12]\), and \(a+3(y-5/12)\) on \([5/12,1/2]\). Exact polynomial integration yields \(\Delta(a_0+a_1y+a_2y^2+a_3y^3)=-a_3(2a_2+3a_3)/414720\). Because \(\mu\) is common, the two variances' subtracted means agree; hence \(\Delta\) equals the asserted autocovariance difference. Quadratic observables all give zero; \(q(y)=y^3\) gives \(-1/138240\). This establishes the first polynomial degree where lag-one autocorrelation detects the difference.

## Verification

The standalone `verify.py` uses only Python's standard library. It checks thousands of exact rational signed orbit-measure identities, sharp rational witnesses for the finite-time Wasserstein coefficient, and exact piecewise-polynomial integrations for the cubic covariance functional. Run `python verify.py` in a directory containing the embedded file. A finite check corroborates but does not substitute for the complete arguments above.

## Relationship to prior work

The interval maps themselves, their nonconjugacy, equality of periodic-orbit sets, and equality of squares are credited to Fuhrmann, Gröger and Passeggi, arXiv:2610.07435v1, Example 5.2 and Theorem B. Their Example 5.1 explicitly computes even and odd iterates for the underlying reflection construction. Therefore the *algebraic basis* of the telescoping argument is already in the source, and those orbit formulas are not presented as novel. Their explicit conclusions concern periodic-orbit rigidity and (unweighted) topological entropy; the exact sharp Wasserstein separation, complete all-potential thermodynamic equivalence, and minimal-degree stationary correlation separator are the findings evaluated here. General metric duality, entropy of iterates, and the variational principle are standard. Searches of relevant research records did not find these combined statistical statements but cannot establish worldwide priority.

## Limitations

The results apply to the specified explicit piecewise-linear pair, not to every pair of interval maps sharing periodic orbits. Pressure equivalence is for potentials depending on current state, not arbitrary two-time potentials; the differing correlation explicitly distinguishes two-time statistics. The coefficient is relative to the chosen Euclidean coordinate and invariant probability. The main primary paper supplies explicit iterate formulas from which the one-atom telescoping relation is readily derivable; consequently the novelty of the statistical refinement should be independently assessed. No independent expert audit or external certification has occurred.

## References

1. G. Fuhrmann, M. Gröger and A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first publicly posted 2026-10-05), especially Section 5, Example 5.2, and Theorem B.
2. Classical variational principle for topological pressure, metric entropy of iterates, and Kantorovich--Rubinstein duality (standard mathematical tools, not original claims).
