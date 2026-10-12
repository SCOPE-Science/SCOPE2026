# Exact coprime-target fibers of finite arithmetic subderivatives
## Finding
Let \(S\) be a finite nonempty set of primes. Define
\[
P_S=\prod_{p\in S}p,
\qquad
D_S(n)=n\sum_{p\in S}\frac{\nu_p(n)}{p}
\]
for positive integers \(n\). For each nonempty subset \(T\subseteq S\), define
\[
P_T=\prod_{p\in T}p,
\qquad
H(T)=\sum_{p\in T}\frac{P_T}{p}.
\]
Then for every positive integer \(y\) satisfying \(\gcd(y,P_S)=1\), the entire inverse fiber is
\[
D_S^{-1}(y)=
\left\{\frac{P_Ty}{H(T)}:\varnothing\ne T\subseteq S,\ H(T)\mid y\right\}.
\]
Consequently,
\[
\#D_S^{-1}(y)=\#\left\{\varnothing\ne T\subseteq S:H(T)\mid y\right\}.
\]
Every singleton \(T=\{p\}\) has \(H(T)=1\), so every target in this coprime stratum has at least \(|S|\) preimages. The minimum fiber size is exactly \(|S|\), attained at \(y=1\).

Let
\[
\mathcal A_S=\left\{\varnothing\ne T\subseteq S:\gcd(H(T),P_S)=1\right\}.
\]
The maximum fiber size among all \(y\) with \(\gcd(y,P_S)=1\) is exactly \(|\mathcal A_S|\). It is attained by
\[
y_S=\operatorname{lcm}\left\{H(T):T\in\mathcal A_S\right\},
\]
which is itself coprime to \(P_S\).

For \(S=\{2,3,5\}\), the admissible subsets have \(H(T)\)-values \(1,1,1,7,31\). Thus \(y=217\) attains the maximum five-element fiber
\[
D_{\{2,3,5\}}^{-1}(217)=\{210,310,434,651,1085\}.
\]

## Assumptions and scope
The theorem concerns positive integers, a finite nonempty prime set \(S\), and targets \(y\) coprime to the squarefree product \(P_S\). The coprimality condition is structural rather than computational: it forces every prime of \(S\) that occurs in a preimage to occur to exponent exactly one. No bound is imposed on \(y\), on primes outside \(S\), or on the size of \(S\).

## Proof
Suppose \(D_S(n)=y\) and \(\gcd(y,P_S)=1\). Fix \(p\in S\). If \(\nu_p(n)\ge2\), then every summand
\[
\frac{n\nu_q(n)}{q},\qquad q\in S,
\]
is divisible by \(p\): for \(q\ne p\), the factor \(n/q\) still contains \(p^2\), while for \(q=p\), the factor \(n/p\) still contains \(p\). Hence \(p\mid D_S(n)=y\), contradicting \(\gcd(y,P_S)=1\). Therefore each active prime of \(S\) occurs in \(n\) with exponent one.

Let
\[
T=\{p\in S:p\mid n\}.
\]
Since \(y>0\), the set \(T\) is nonempty. We can write \(n=mP_T\) with \(\gcd(m,P_S)=1\). Using the preceding exponent-one conclusion,
\[
D_S(n)
=mP_T\sum_{p\in T}\frac1p
=mH(T).
\]
Thus \(H(T)\mid y\), \(m=y/H(T)\), and
\[
n=\frac{P_Ty}{H(T)}.
\]
This proves that every preimage appears in the displayed set.

Conversely, suppose \(T\ne\varnothing\) and \(H(T)\mid y\). Since \(H(T)\) divides the integer \(y\) and \(\gcd(y,P_S)=1\), one has \(\gcd(H(T),P_S)=1\). Hence
\[
m=\frac{y}{H(T)}
\]
is also coprime to \(P_S\). For \(n=mP_T\), precisely the primes in \(T\) occur from \(S\), each to exponent one. Therefore
\[
D_S(n)=mH(T)=y.
\]
So the parametrization is exact, and distinct subsets \(T\) give distinct preimages because their intersections with the prime set \(S\) are different. The fiber-count formula follows.

For a singleton \(T=\{p\}\), one has \(H(T)=1\), so the \(|S|\) singleton branches always occur. If \(|T|\ge2\), then \(H(T)>1\), and therefore at \(y=1\) only singleton branches occur. This proves the exact minimum \(|S|\).

Finally, if \(\gcd(y,P_S)=1\) and \(H(T)\mid y\), then necessarily \(T\in\mathcal A_S\), so no fiber can have more than \(|\mathcal A_S|\) elements. Conversely, all integers \(H(T)\) with \(T\in\mathcal A_S\) are coprime to \(P_S\), so their least common multiple \(y_S\) is also coprime to \(P_S\) and is divisible by every one of them. The fiber over \(y_S\) therefore has exactly \(|\mathcal A_S|\) elements.

## Verification
The symbolic proof above is the evidence for the infinite statement. A bundled regression program independently computes \(D_S\), enumerates the predicted subsets, and exhaustively compares actual and predicted fibers for all coprime targets \(y<100\) for \(S=\{2,3\}\), \(\{2,3,5\}\), \(\{3,5,7\}\), and \(\{2,5,7,11\}\). It also verifies the exact minimum and maximum formulas for those sets and the five-element example at \(S=\{2,3,5\}\), \(y=217\). The finite computation is a regression check only; it is not used to infer the theorem.

## Relationship to prior work
Merikoski, Haukkanen, and Tossavainen introduced arithmetic subderivatives for nonempty prime sets and established their basic Leibniz-additive structure. Emmons and Xiao studied inverse questions for the singleton arithmetic partial derivative and explicitly identified analogous questions for finite-set arithmetic subderivatives as a natural next step. Their singleton results do not imply the present formula because a finite-set subderivative is a sum of several prime components.

Later work on generalized arithmetic subderivatives has focused on algebraic properties, iterates, fixed points, and eigenpoint equations. The present result instead determines an entire inverse fiber on the natural target stratum \(\gcd(y,P_S)=1\), including its exact minimum and maximum branching. The checked sources did not state an equivalent finite-set inverse-fiber parametrization or a stronger theorem implying it.

## Limitations
The theorem does not classify targets divisible by primes of \(S\). On that complementary stratum, exponents at primes in \(S\) can exceed one and different exponent vectors can interact in the weighted sum \(\sum_{p\in S}\nu_p(n)/p\). The literature comparison is extensive for the directly relevant arithmetic-subderivative papers but cannot logically exclude every unindexed historical formulation.

## References
1. Brad Emmons and Xiao Xiao, “The Arithmetic Partial Derivative,” *Journal of Integer Sequences* 25 (2022), Article 22.4.7; arXiv:2201.12453.
2. Jorma K. Merikoski, Pentti Haukkanen, and Timo Tossavainen, “Arithmetic Subderivatives and Leibniz-Additive Functions,” *Annales Mathematicae et Informaticae* 50 (2019), 145–157; arXiv:1901.02216; DOI:10.33039/ami.2019.03.003.
3. Champak Talukdar and Helen K. Saikia, “Arithmetic Subderivatives Relative to Subsets of Primes,” *Communications in Mathematics and Applications* 16 (2025), 491–499; DOI:10.26713/cma.v16i2.3430.
4. Champak Talukdar and Helen K. Saikia, “Arithmetic Differential Equations Defined by Generalized Subderivatives,” *International Journal of Mathematics Trends and Technology* 72 (2026), 21–27; DOI:10.14445/22315373/IJMTT-V72I1P104.
