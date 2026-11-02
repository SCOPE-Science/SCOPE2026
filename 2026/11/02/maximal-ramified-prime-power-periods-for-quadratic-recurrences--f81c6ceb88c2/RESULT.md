# Maximal ramified prime-power periods for quadratic recurrences

## Finding
For every prime \(p\ge5\), every pair of integers \(P,Q\) with \(p\nmid Q\) and \(P^2-4Q\equiv0\pmod p\), and every \(k\ge1\), the normalized second-order recurrence
\[
U_0=0,\quad U_1=1,\quad U_{n+2}=PU_{n+1}-QU_n
\]
has least period
\[
\boxed{\pi_U(p^k)=m p^k},\qquad m=\operatorname{ord}_{\mathbb F_p^\times}(P/2).
\]
In particular, \(\pi_U(p^2)=p\pi_U(p)\), excluding unchanged prime-square periods in the repeated-root branch for all \(p\ge5\).

A linked exact factor obstruction holds: \(X^p-1\) in \((\mathbb Z/p^2\mathbb Z)[X]\) has no monic factor whose degree \(r\) satisfies \(2\le r\le p-2\). In particular, the double factor \((X-1)^2\) modulo \(p\) cannot lift to a monic quadratic factor modulo \(p^2\) for these primes.

The lower-prime boundary is sharp. Over \(\mathbb Z/9\mathbb Z\), \(X^2+X+1\) divides \(X^3-1\) and the associated recurrence has period \(3\) modulo both \(3\) and \(9\).

## Assumptions and scope
The variable \(p\) is prime, \(p\ge5\), and the recurrence parameters are arbitrary integers subject to the congruence and unit conditions above. Its period is the least positive integer \(T\) such that \(U_{n+T}\equiv U_n\pmod{p^k}\) for all \(n\ge0\). The residue \(P/2\) is a nonzero element of \(\mathbb F_p\), so \(m\mid p-1\).

## Proof
**Companion reduction.** Put
\[
A=\begin{pmatrix}P&-Q\\1&0\end{pmatrix}.
\]
Its determinant is a unit modulo every \(p^k\). The vectors \((1,0)^t\) and \(A(1,0)^t=(P,1)^t\) form a basis over \(\mathbb Z/p^k\mathbb Z\). Therefore the least period of \((U_n)\) is exactly the order of \(A\) in \(\mathrm{GL}_2(\mathbb Z/p^k\mathbb Z)\): if \(A^T(1,0)^t=(1,0)^t\), commuting with \(A\) forces \(A^T\) to fix a basis.

The characteristic polynomial of \(A\) reduces to \((X-\alpha)^2\) with \(\alpha=P/2\ne0\) modulo \(p\). Since \(A\) is not scalar modulo \(p\), its reduction is \(\alpha I+J\), with \(J^2=0\ne J\). By the binomial formula, \(\overline{A^m}=I+m\alpha^{-1}J=I+N\), where \(N^2=0\ne N\). It follows that \(\operatorname{ord}_p(A)=mp\): the scalar order \(m\) is prime to \(p\), and a nontrivial unipotent block has order \(p\).

**First lift.** Set \(B=A^m-I\) over the integers. Modulo \(p\), \(B\) reduces to \(N\), so \(B^2\equiv0\pmod p\) but \(B\not\equiv0\pmod p\). For every \(2\le j\le p-1\), the term \(\binom pj B^j\) is divisible by \(p^2\). Also \(B^p\equiv0\pmod{p^2}\), since \(p\ge5\) and \(B^2\) is divisible by \(p\). Thus
\[
(A^m)^p=(I+B)^p\equiv I+pB\not\equiv I\pmod{p^2}.
\]
This identifies the lift obstruction without assuming distinct roots modulo \(p\).

**Every higher lift.** The last congruence has the form \(A^{mp}=I+pC_1\) with \(C_1\equiv N\not\equiv0\pmod p\). For each \(r\ge1\), if \(A^{mp^r}=I+p^rC_r\) with \(C_r\equiv N\pmod p\), then the binomial expansion for odd \(p\) gives \(A^{mp^{r+1}}=I+p^{r+1}C_{r+1}\) with \(C_{r+1}\equiv N\pmod p\). Hence \(A^{mp^{k-1}}\not\equiv I\pmod{p^k}\) for \(k\ge2\), whereas \(A^{mp^k}\equiv I\pmod{p^k}\). Together with the order \(mp\) modulo \(p\), this proves the claimed exact period for all \(k\ge1\).

**Polynomial obstruction.** Suppose \(X^p-1=F(X)G(X)\) in \((\mathbb Z/p^2\mathbb Z)[X]\) with monic factors of degrees \(r,p-r\), both at least two. Set \(Y=X-1\). Reduction modulo \(p\) gives \(F(1+Y)\equiv Y^r\) and \(G(1+Y)\equiv Y^{p-r}\). In both factors, the constant and linear coefficients are divisible by \(p\). Consequently their product has linear coefficient divisible by \(p^2\). But
\[
(1+Y)^p-1=pY+\binom p2Y^2+\cdots+Y^p
\]
has linear coefficient exactly \(p\), nonzero modulo \(p^2\). Contradiction. For \(p\ge5\), degree two lies in the excluded range.

**Sharp exception.** The integer identity \(X^3-1=(X-1)(X^2+X+1)\) supplies a quadratic divisor when \(p=3\). The companion matrix of \(X^2+X+1\) satisfies \(A^3=I\) and \(A\ne I\), even modulo \(9\), giving period three at both levels.

## Verification
Execute `python3 verify.py` with Python 3. The script checks all residue-class coefficient pairs \((P,Q)\) modulo \(p^2\) satisfying the hypotheses for \(p=5,7,11,13\), and tests orders modulo \(p^k\) for \(k=1,2,3\) by exact modular matrix powers. This is \(3632\) coefficient pairs; the script independently verifies the \(p=3\) exceptional example. Expected output: `VERIFY_OK primes=5,7,11,13 coefficient_lifts=3632 levels=1,2,3 p3_exception=yes`. The finite checks do not prove the unrestricted theorem.

## Relationship to prior work
Shi, Wang, Zakariae, Kim and Solé (2026, Section 4.3) propose lifting the repeated quadratic factor \((X-1)^2\) of \(X^p-1\) modulo \(p\) to a quadratic factor modulo \(p^2\), in order to construct a recurrence with equal period \(p\) at the first two prime-power levels. Their stated lifting step cannot hold for \(p\ge5\); its displayed \(p=3\) example remains valid. The other distinct-root branches of their constructions are not addressed here. The older period-lifting dichotomy, attributed there to Vince (1981), allows either equality or multiplication by \(p\); the present theorem determines the branch and all higher levels in the repeated-root situation.

## Limitations
This statement is confined to invertible quadratic recurrences whose characteristic polynomial has a double nonzero root modulo \(p\), and primes \(p\ge5\). It does not classify distinct-root recurrences, primes dividing the constant coefficient, or the characteristic-three situation beyond the exhibited sharp exception. The prime-power lift argument is elementary and may have appeared implicitly in earlier recurrence-period literature; priority has not been independently established. No independent mathematical audit has been performed.

## References
1. M. Shi, X. Wang, B. Zakariae, J.-L. Kim and P. Solé, *Second order Recurrences, quadratic number fields and cyclic codes*, arXiv:2603.25343v1 (first public 2026-03-26), especially Section 4.3, https://arxiv.org/html/2603.25343v1.
2. A. Vince, *Period of a linear recurrence*, Acta Arithmetica 39 (1981), 303–311, DOI:10.4064/aa-39-4-303-311 (relevant period-lifting dichotomy as cited by [1]; complete text not reviewed here).
