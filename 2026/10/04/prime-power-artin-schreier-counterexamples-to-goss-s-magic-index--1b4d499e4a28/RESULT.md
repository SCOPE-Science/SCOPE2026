# Prime-power Artin–Schreier counterexamples to Goss’s magic-index bound
## Finding
Let \(q=p^s\) with prime \(p\ge5\), and put \(A=\mathbb F_q[T]\). For every \(a\in\mathbb F_q^\times\), set
\[
H_a(U)=U^q-U-a.
\]
The polynomial \(H_a\) has exactly \(q/p\) distinct monic irreducible factors \(P\in A\), each of degree \(p\). For every such factor and every integer \(1\le n\le p-1\), put \(i=q^n-1\) and define
\[
D_{P,i}(X)=\sum_{m=0}^{p-1}\left(\sum_{\substack{f\in A^+\\\deg f=m}}(f\bmod P)^i\right)X^m\in(A/P)[X].
\]
Then
\[
D_{P,i}(X)=(1-X)^n.
\]
Therefore, for the mod-\(P\) Teichmüller character \(\omega_P\),
\[
\deg_X g(X,\omega_P^{q^n-1})=n-1.
\]
In particular, for every prime power \(q=p^s\) with \(p\ge5\) and every \(3\le n\le p-1\), these primes give counterexamples to Goss's magic-index degree bound. As \(a\) ranges over \(\mathbb F_q^\times\), the factor sets are disjoint, so each such index occurs on exactly \(q(q-1)/p\) distinct degree-\(p\) primes supplied by this construction.

## Assumptions and scope
The Teichmüller character and \(g(X,\omega_P^i)\) are used in the standard cyclotomic-function-field sense of Anglès. The exponent \(i=q^n-1\) is a \(q\)-magic number and satisfies \(i\equiv0\pmod{q-1}\). Because \(n\le p-1=\deg P-1\), one has \(1\le i\le q^{\deg P}-2\), so the character is nontrivial and in the usual range. The exact polynomial identity holds also for \(p=2,3\) in the indicated range, but the counterexample conclusion requires \(n\ge3\), hence \(p\ge5\).

## Proof
Fix \(a\ne0\) and a root \(\theta\) of \(H_a\). Since \(\theta^q=\theta+a\) and \(a\in\mathbb F_q\), iteration gives
\[
\theta^{q^r}=\theta+ra\qquad(0\le r\le p).
\]
For \(1\le r<p\), the difference \(ra\) is nonzero, whereas \(pa=0\). Thus the \(q\)-Frobenius orbit of every root has length exactly \(p\). Also \(H_a'(U)=-1\), so \(H_a\) is separable. Its \(q\) roots therefore split into \(q/p\) Frobenius orbits, proving that its irreducible factors are distinct and all have degree \(p\).

Fix one factor \(P\) and identify \(A/P\) with \(\mathbb F_q(\theta)\). For \(m<p\) and \(b\in\mathbb F_p a\), define
\[
T_m(b)=\sum_{\substack{f\in A^+\\\deg f=m}}\frac{f(\theta+b)}{f(\theta)}.
\]
The denominators are nonzero because \(P\) has degree \(p>m\). Clearly \(T_0(b)=1\), while for \(m\ge1\),
\[
T_m(0)=q^m=0
\]
in characteristic \(p\).

We claim that for \(1\le m\le p-1\),
\[
T_m(b+a)=T_m(b)-T_{m-1}(b).
\]
Write every monic degree-\(m\) polynomial uniquely as \(f(Y)=F_h(Y)+c\), where \(F_h(Y)=Yh(Y)\), \(h\) is monic of degree \(m-1\), and \(c\in\mathbb F_q\). Subtracting the two sums and summing first over \(c\) gives
\[
T_m(b+a)-T_m(b)
=\sum_h \bigl(F_h(\theta+b+a)-F_h(\theta+b)\bigr)
\sum_{c\in\mathbb F_q}\frac1{F_h(\theta)+c}.
\]
The finite-field identity
\[
\sum_{c\in\mathbb F_q}\frac1{z+c}=-\frac1{z^q-z}
\]
follows by logarithmic differentiation of \(z^q-z=\prod_{c\in\mathbb F_q}(z+c)\). Since \(F_h\) has coefficients in \(\mathbb F_q\),
\[
F_h(\theta)^q-F_h(\theta)=F_h(\theta+a)-F_h(\theta).
\]
Hence, with \(\Delta_aF(Y)=F(Y+a)-F(Y)\),
\[
T_m(b+a)-T_m(b)=-\sum_h\frac{\Delta_aF_h(\theta+b)}{\Delta_aF_h(\theta)}.
\]
Now \(\Delta_aF_h/(ma)\) is monic of degree \(m-1\). The map
\[
h\longmapsto \frac{\Delta_a(Yh)}{ma}
\]
is a bijection on the monic degree-\(m-1\) polynomials: if two inputs have the same image, their difference gives a polynomial \(Y(h_1-h_2)\) of degree less than \(p\) invariant under translation by \(a\); a nonconstant polynomial of degree less than \(p\) cannot be translation-invariant because its finite difference has nonzero leading coefficient. Since the polynomial also vanishes at \(0\), it is zero. Reindexing the last sum therefore proves the recursion.

Starting from \(T_m(0)\), Pascal induction gives
\[
T_m(na)=(-1)^m\binom nm
\]
for \(0\le n\le p-1\). On the other hand, for every monic \(f\) of degree less than \(p\),
\[
f(\theta)^{q^n-1}=\frac{f(\theta)^{q^n}}{f(\theta)}
=\frac{f(\theta+na)}{f(\theta)}.
\]
Thus the coefficient of \(X^m\) in \(D_{P,q^n-1}(X)\) is \((-1)^m\binom nm\), proving \(D_{P,q^n-1}(X)=(1-X)^n\).

For a nontrivial even Teichmüller character, the standard reduction identity identifies \(D_{P,i}(X)\) with the reduction of \((1-X)L(X,\omega_P^i)\). Therefore the multiplicity of \(X=1\) in \(D_{P,i}\) is one plus the number of reciprocal roots of \(L\) congruent to \(1\) at the characteristic prime, namely
\[
\operatorname{ord}_{X=1}D_{P,i}(X)=1+\deg_X g(X,\omega_P^i).
\]
The identity \(D_{P,i}=(1-X)^n\) gives \(\deg_X g=n-1\).

Finally, if a prime factor belonged to both \(H_a\) and \(H_{a'}\), any common root would give \(a=a'\). Thus the factors for distinct nonzero \(a\) are disjoint, and there are \((q-1)(q/p)=q(q-1)/p\) primes in the construction.

## Verification
The universal argument is symbolic. The accompanying verifier independently checks a genuinely non-prime base field, \(q=25\), using exact finite-field arithmetic. It constructs
\[
\mathbb F_{25}[\theta]/(\theta^5-\theta-3),
\]
verifies the five-step Frobenius orbit \(\theta^{25}=\theta+1\), checks the reciprocal-sum identity exactly at \(z=\theta\), and exhaustively verifies the normalized finite-difference bijection on every monic polynomial in the four relevant degrees. The resulting Pascal recurrence gives the coefficient vector \((1,2,3,4,0)\), exactly the coefficient vector of \((1-X)^3\) in characteristic \(5\). These finite checks corroborate the algebraic ingredients of the extension at \(q=25\); they are not used as a proof for arbitrary \(q\).

## Relationship to prior work
Anglès formulates the cyclotomic setup for a general finite field \(\mathbb F_q\), defines \(q\)-magic numbers, and records Goss's degree conjecture. Giraudin's 2026 preprint gives the first explicit infinite counterexample family by specializing throughout to the prime-field case \(q=p\): for \(P_a=T^p-T-a\) and \(i=p^n-1\), it proves the same binomial reduction and obtains \(\deg_X g=n-1\). The present result changes the base-field size from \(p\) to an arbitrary power \(q=p^s\). The polynomial \(U^q-U-a\) is no longer irreducible when \(s>1\); the Frobenius-orbit analysis and the \(\mathbb F_q\)-reciprocal-sum recursion show that all \(q/p\) degree-\(p\) factors inherit the exact reduction. Targeted searches of the current literature and published claim corpus found no statement covering this prime-power extension.

## Limitations
The theorem concerns the specific Artin–Schreier family cut out by factors of \(U^q-U-a\) and the magic indices \(q^n-1\). It does not classify all counterexamples over \(\mathbb F_q[T]\), treat magic indices with nonzero leading digit \(c\), or determine whether still larger degrees of \(g\) occur for fixed characteristic. The exact count \(q(q-1)/p\) is the count supplied by this construction, not a count of all degree-\(p\) counterexample primes.

## References
1. D. Niedbala Giraudin, *An infinite family of counterexamples to Goss's conjecture on L-functions of cyclotomic function fields*, arXiv:2609.37466v1, 2026.
2. B. Anglès, *On L-functions of cyclotomic function fields*, Journal of Number Theory 116 (2006), 247–269; arXiv:math/0502130v1; doi:10.1016/j.jnt.2005.04.007.
