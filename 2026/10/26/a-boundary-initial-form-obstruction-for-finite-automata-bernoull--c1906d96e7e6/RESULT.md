# A boundary initial-form obstruction for finite-automata Bernoulli factories

## Finding
Let \(\Delta_2=\{(p_1,p_2,p_3)\in(0,1)^3:p_1+p_2+p_3=1\}\). For every integer \(d\ge4\), define homogeneous degree-\(d\) polynomials

\[
P_d=p_1^{d-1}p_2,\qquad Q_d=p_3^{d-2}(p_1-p_2)^2+p_1^{d-1}(p_1+p_2+p_3),\qquad f_d= P_d/Q_d.
\]

Then \(f_d:\Delta_2\to(0,1)\) admits a general Bernoulli factory but admits no finite-automata Bernoulli factory. More generally, let \(P,Q\) be coprime homogeneous polynomials of the same degree, with \(Q\) nonzero on the open simplex. In a boundary chart obtained by setting one coordinate to \(1\), suppose the lowest-degree nonzero homogeneous component \(q_r\) of the dehomogenized denominator has a zero at some point \(v\) whose coordinates are all strictly positive. Then \(P/Q\) has no representation as a ratio of homogeneous polynomials with nonnegative coefficients. Whenever \(P/Q\) takes values in \((0,1)\) on the open simplex, it therefore has no finite-automata Bernoulli factory.

## Assumptions and scope
A general Bernoulli factory may use an almost-surely finite stopping rule with no finite-state restriction. A finite-automata factory is understood in the block-simulation sense used in the cited literature; its target probability must have a Bernstein-ratio representation. The simplex is open, so all three coordinates are strictly positive and sum to one. The obstruction is sufficient, not necessary: it does not classify every rational function that lacks a finite-automata implementation.

## Proof
First consider the family. On \(\Delta_2\), the identity \(p_1+p_2+p_3=1\) gives

\[
Q_d=P_d+R_d,\qquad R_d=p_3^{d-2}(p_1-p_2)^2+p_1^{d-1}(p_1+p_3).
\]

Both \(P_d\) and \(R_d\) are strictly positive on \(\Delta_2\), so \(0<f_d<1\). On the closed simplex, \(Q_d\le2\): each of its two displayed summands is at most \(1\). Consequently

\[
f_d\ge\tfrac12p_1^{d-1}p_2\ge\tfrac12(p_1p_2p_3)^d,\qquad
1-f_d=R_d/Q_d\ge\tfrac12p_1^{d-1}(p_1+p_3)\ge\tfrac12(p_1p_2p_3)^d.
\]

Thus \(\min(f_d,1-f_d)\ge\tfrac12(p_1p_2p_3)^d\). By the multivariate Bernoulli-factory criterion of Morina, as stated in the inspected 2026 note, this polynomial boundary lower bound implies that \(f_d\) has a general Bernoulli factory.

Next, \(P_d\) and \(Q_d\) are coprime. The only irreducible factors of \(P_d\) are \(p_1\) and \(p_2\); setting \(p_1=0\) in \(Q_d\) gives \(p_3^{d-2}p_2^2\), not the zero polynomial, and setting \(p_2=0\) gives \(p_3^{d-2}p_1^2+p_1^{d-1}(p_1+p_3)\), also not the zero polynomial.

Suppose a finite-automata factory existed. The Bernstein-ratio characterization gives homogeneous nonnegative-coefficient polynomials \(A,B\) representing \(f_d=A/B=P_d/Q_d\). Homogenizing to a common degree if necessary, equality on the simplex implies the polynomial identity \(AQ_d=BP_d\). Coprimality forces \(B=Q_dR\) for a nonzero polynomial \(R\).

Set \(p_3=1\) and write \(x=p_1,y=p_2\). Then

\[
q_d(x,y)=Q_d(x,y,1)=(x-y)^2+x^{d-1}(x+y+1).
\]

Because \(d\ge4\), its lowest-degree nonzero homogeneous component is \(q_2(x,y)=(x-y)^2\). Let \(r_k\) be the lowest-degree nonzero homogeneous component of \(r(x,y)=R(x,y,1)\). The lowest-degree component of \(b(x,y)=B(x,y,1)=q_d(x,y)r(x,y)\) is exactly \(q_2r_k\), which is nonzero because the polynomial ring is an integral domain. But \(B\) has nonnegative coefficients, so every homogeneous component of \(b\), including \(q_2r_k\), has nonnegative coefficients. At \(v=(1,1)\), its value is \(q_2(1,1)r_k(1,1)=0\). A polynomial with nonnegative coefficients that vanishes at a point with strictly positive coordinates must be the zero polynomial, a contradiction. Hence no Bernstein-ratio representation exists and no finite-automata factory exists.

The general obstruction is the same argument without specializing \(Q\): coprimality forces any Bernstein denominator to equal \(QR\); in the chosen boundary chart, the lowest homogeneous component of that product is \(q_r r_k\). It is nonzero in the integral domain but has nonnegative coefficients and vanishes at the positive zero of \(q_r\), which is impossible.

## Verification
The proof uses exact polynomial identities, coprimality, the integral-domain property, and the cited Bernoulli-factory characterizations; it does not infer an infinite statement from finite experiments. The condition \(d\ge4\) is essential to this proof because it ensures that the degree-two boundary term \((x-y)^2\) is the lowest-degree term of \(q_d\). The argument establishes a sufficient obstruction only. It does not prove that the criterion is necessary or characterize all finite-automata factories.

## Relationship to prior work
Paes Leme and Schneider give the degree-four instance \(d=4\) as a counterexample to the multivariable extension of the Mossel–Peres rationality claim. Their proof uses the same lowest-degree contradiction for that particular denominator. The present claim does not claim that example or its proof pattern as new: it states a general boundary-initial-form obstruction and proves the explicit family for every \(d\ge4\). Mossel–Peres's original one-variable theorem remains distinct; the multivariable claim they state is the one later shown to fail. Morina's criterion concerns general factories, not finite-state realizability.

## Limitations
The criterion is only sufficient and depends on a coprime homogeneous representation. The family proves existence of infinitely many examples, but does not describe all rational functions with this separation. The multivariate general-factory criterion is invoked as a published theorem; its original dissertation PDF was not directly accessible during this run, so that source-level dependency remains explicit. The direct abstraction from the degree-four example is a residual originality risk even though the general criterion and all-degree statement were not found in the searched records.

## References
1. R. Paes Leme and J. Schneider, “Note on Finite-Automata Bernoulli Factories for Rational Functions,” arXiv:2606.29595v1, first posted 2026-06-28, especially Sections 2–3 and Theorem 3.1.
2. E. Mossel and Y. Peres, “New Coins from Old: Computing with Unknown Bias,” arXiv:math/0304143v1, first posted 2003-04-10, especially Theorem 2.9 and the block-simulation characterization.
3. G. Morina, “Extending the Bernoulli Factory to a Dice Enterprise,” PhD thesis, University of Warwick, 2021, multivariate polynomial-bound criterion for general factories.
