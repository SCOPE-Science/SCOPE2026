# Complete dyadic cubic root-count recurrence and sharp extremal law

## Finding

For every integer \(k\geq1\), choose independent uniform coefficients \(a,b,c\in\mathbb Z/2^k\mathbb Z\), and put
\[
f(X)=X^3+aX^2+bX+c,\qquad R_k(f)=\#\{x\bmod2^k:f(x)\equiv0\pmod{2^k}\}.
\]
Write \(P_k(z)=\sum_fz^{R_k(f)}\); thus \(2^{-3k}P_k(z)\) is the exact probability-generating polynomial. The first three distributions are
\[
\begin{aligned}
P_1(z)&=2+4z+2z^2,\\
P_2(z)&=24+24z+8z^2+8z^3,\\
P_3(z)&=208+208z+32z^2+32z^3+16z^4+16z^5.
\end{aligned}
\]
For \(k\geq1\), define the explicitly evaluated square-root polynomial \(Q_k(z)\) as follows. For \(0\leq j\leq\lfloor(k-1)/2\rfloor\), let \(m_j=k-2j\), and set
\[
(A_j,B_j)=\begin{cases}
(1,2^j),&m_j=1,\\
(1,2^{j+1}),&m_j=2,\\
(2^{m_j-3},2^{j+2}),&m_j\geq3.
\end{cases}
\]
Then
\[
Q_k(z)=\left(2^k-1-\sum_jA_j\right)+z^{2^{\lfloor k/2\rfloor}}+\sum_jA_jz^{B_j}.
\]
This is precisely \(\sum_{d\bmod2^k}z^{\#\{y:y^2\equiv d\pmod{2^k}\}}\), including additive merging when displayed exponents coincide.

**Complete distributional recurrence.** For every \(k\geq4\),
\[
\boxed{P_k(z)=\big(2^{3k-2}+10\cdot2^{3k-6}\big)+2^{3k-2}z+2^{3k-4}z^2+2^{2k-2}zQ_k(z)+16P_{k-3}(z^4).}
\]
In particular this completely specifies every coefficient of every finite-level distribution with no finite-depth cutoff.

**Sharp extrema.** If \(k=3t+j\), where \(t\geq0\) and \(j\in\{1,2,3\}\), then
\[
\boxed{\max_f R_k(f)=\begin{cases}2\cdot4^t,&j=1,\\3\cdot4^t,&j=2,\\5\cdot4^t,&j=3,\end{cases}}
\]
and exactly
\[
\boxed{\#\{f:R_k(f)=\max_gR_k(g)\}=\begin{cases}2\cdot16^t,&j=1,\\8\cdot16^t,&j=2,\\16\cdot16^t,&j=3.\end{cases}}
\]
monic cubics attain that maximum. Every extremizer at level \(k\geq4\) is obtained uniquely by choosing \(r\in\{0,1\}\), making the substitution \(X=2Y+r\), and requiring
\[
f(2Y+r)=8g(Y),\quad g(Y)=Y^3+uY^2+vY+w,
\]
with the coefficients interpreted as congruences modulo \(2^k\), and \(g\bmod2^{k-3}\) an extremizer at level \(k-3\). The displayed equation is an identity of integer-coefficient polynomials after choosing coefficient lifts, or equivalently a coefficient congruence modulo \(2^k\). The total probability of maximum occupancy shrinks by a factor \(1/32\) for every three additional binary digits.

## Assumptions and scope

Every cubic is monic and all three lower coefficients range independently over the entire residue ring. Roots are distinct residue classes modulo \(2^k\), not multiplicities and not roots in \(\mathbb Q_2\). The theorem applies to every positive integer \(k\). It says nothing about prime moduli other than \(2\), polynomials of degree above three, or exact \(2\)-adic roots in the inverse limit.

## Proof

**1. Cubic reduction classes and simple lifts.** The eight monic cubic polynomials over \(\mathbb F_2\) have two irreducible reductions (no roots), two reductions with precisely one simple root, two with one double root and one simple root, and two with one triple root. Each fixed reduction has \(2^{3k-3}\) coefficient lifts modulo \(2^k\). The first two types contribute \(2^{3k-2}\) to the constant coefficient and \(2^{3k-2}z\), respectively, by reduction and simple Hensel lifting.

**2. The double-plus-simple class.** Fix one such reduction. Its unique simple root \(s\) lifts uniquely to an odd root modulo \(2^k\), and polynomial division gives the unique factorization
\[
f(X)=(X-s)(X^2+AX+B)\pmod{2^k},\qquad A\equiv B\equiv0\pmod2.
\]
Conversely \(s\) odd and \(A,B\) even parameterize every polynomial in this reduction class exactly once. The quadratic has only even roots, so its roots are disjoint from \(s\). Writing \(A=2u\), the substitution \(Y=X+u\) makes its equation \(Y^2\equiv u^2-B\pmod{2^k}\). Since \(B\) is even, every solution has parity \(u\), hence yields an even \(X\). For each \(d\bmod2^k\), there are exactly \(2^{k-2}\) pairs \((u,B)\) producing \(d=u^2-B\), because \(u\bmod2^{k-1}\) must have the parity of \(d\), and then \(B\) is determined. There are \(2^{k-1}\) choices of \(s\), and two reduction classes. Thus their combined contribution is
\[
2^{2k-2}zQ_k(z).
\]

**3. Evaluating the quadratic square-root law.** The residue \(d=0\) has \(2^{\lfloor k/2\rfloor}\) square roots. A nonzero square has exact valuation \(2j<k\); write \(d=2^{2j}u\) with \(u\) odd and \(m=k-2j\). The number of square roots modulo \(2^k\) is \(2^j\) times the number of odd roots of \(u\) modulo \(2^m\). For \(m=1\), this is one root for the only odd target; for \(m=2\), exactly the target \(u\equiv1\pmod4\) has two roots; for \(m\geq3\), exactly the \(2^{m-3}\) targets \(u\equiv1\pmod8\) have four. All other residues have none. This establishes \(Q_k\) above without using cubic computations.

**4. The triple class.** Shift the unique reduced root to zero: write \(f(Z+r)=Z^3+AZ^2+BZ+C\) with all three coefficients even. Only even \(Z=2Y\) can be roots. For \(k\geq4\), if \(C\equiv2\pmod4\), there are no roots. If \(B\equiv2\pmod4\) and \(4\mid C\), then
\[
f(2Y)/4=2Y^3+(A/2)\,2Y^2+(B/2)Y+C/4,
\]
whose derivative is odd modulo \(2\); it has exactly one solution modulo \(2^{k-2}\), giving exactly two distinct roots modulo \(2^k\). If \(4\mid B\) but \(C\equiv4\pmod8\), there are no roots. In the remaining case \(4\mid B\) and \(8\mid C\), one has
\[
f(2Y)=8\big(Y^3+(A/2)Y^2+(B/4)Y+C/8\big).
\]
The number of roots of \(f\bmod2^k\) is then four times the number of roots of the reduced monic cubic \(g\bmod2^{k-3}\). For each fixed \(g\bmod2^{k-3}\), there are precisely \(2^3=8\) admissible coefficient lifts for each \(r\). Counting all coefficient choices in the four branches and both \(r\) gives, respectively,
\[
\big(10\cdot2^{3k-6}\big)\,z^0,\quad \big(2^{3k-4}\big)\,z^2,\quad 16P_{k-3}(z^4),
\]
where the first term combines the two zero-root subcases. With the two simple-reduction contributions and the double-plus-simple contribution, this proves the recurrence.

**5. Initial levels, maxima, and counts.** The displayed \(P_1,P_2,P_3\) come from enumerating the eight, sixty-four, and five hundred twelve coefficient triples; the accompanying standalone verifier enumerates them independently. The largest possible number \(U_k\) of square roots of any \(d\bmod2^k\) is \(2^{k/2}\) for even \(k\), and \(2^{(k+1)/2}\) for odd \(k\geq3\), by step 3. Hence a double-plus-simple reduction has at most \(1+U_k\) roots, whereas a triple reduction has at most \(\max(2,4M_{k-3})\), where \(M_l\) is the cubic maximum at level \(l\). The base values are \(M_1=2,M_2=3,M_3=5\). Direct comparison for \(k=4,5,6\), followed by \(U_{k+3}\leq4U_k\), proves \(4M_{k-3}>1+U_k\) for every \(k\geq4\). Therefore \(M_k=4M_{k-3}\), with all maximizers arising from the scaled triple branch. Exactly sixteen cubic lifts per maximizing \(g\) are possible (including two choices of parity), so \(E_k=16E_{k-3}\), with initial \(E_1=2,E_2=8,E_3=16\). Solving both recurrences proves the stated three-phase laws.

## Verification

Run `python3 verify.py` and compile/run `verify_level7.cpp` using `c++ -O2 -std=c++17 verify_level7.cpp -o verify_level7 && ./verify_level7`. The Python program independently enumerates all \(299592\) monic cubics at moduli \(2,4,8,16,32,64\), checks every distribution coefficient, enumerates all square-root fibers at the first nine powers of two, and verifies the formal recurrence and extremizer equations through exponent \(24\). The independent C++ program exhaustively enumerates the further \(2097152\) monic cubics modulo \(128\) and checks the entire predicted histogram including the \(512\) maximizers. The expected output begins `VERIFY_OK`; no external libraries are required. Finite computations verify examples and algebraic consistency, not the infinitely quantified proof.

## Relationship to prior work

The August 1, 2026 preprint by Itamar Nir treats singular prime-power root lifting algorithmically, motivating explicit classification of finite-level lifting behavior. Cheng, Gao, Rojas and Wan develop general individual-polynomial root-count algorithms over prime-power rings; these algorithms can in principle compute any one count, but their evaluated statements do not give this all-exponent random-monic-cubic law. Jain computes finite-ring expectations and finite-field distributions, not this finite-ring cubic distribution. Bhargava, Cremona, Fisher and Gajović give the distribution of the **number of actual roots in the \(2\)-adic field**, a distinct statistic from the number of temporary solutions modulo \(2^k\), whose possible values here grow with \(k\). All these methods inform the local analysis; none of the inspected relevant statements explicitly evaluates the dyadic cubic recurrence or its extremizer count. Earlier equivalent formulas are a residual priority risk.

## Limitations

The distribution is restricted to monic degree-three polynomials over power-of-two residue rings. The recurrence uses the standard classification of square roots modulo powers of two; it does not assert that that classical component is new. The count of maximizers is for coefficient triples modulo \(2^k\), not isomorphism or affine-equivalence classes. The complete full text of the motivating root-lifting preprint was not accessible during this comparison; its abstract and verified bibliographic record were checked, and this is an originality limitation. The present self-review is not an independent audit.

## References

1. Itamar Nir, *Faster Deterministic Integer Root Finding for Integer Polynomials*, arXiv:2608.00668, first submitted August 1, 2026.
2. Qi Cheng, Shuhong Gao, J. Maurice Rojas, and Daqing Wan, *Counting Roots of Polynomials Over Prime Power Rings*, arXiv:1711.01355 (2017), Open Book Series 2 (2019), 191–205.
3. Ritik Jain, *The number of solutions of a random system of polynomials over a finite field*, arXiv:2409.06866, revised January 24, 2026.
4. Manjul Bhargava, John Cremona, Tom Fisher, and Stevan Gajović, *The density of polynomials of degree \(n\) over \(\mathbb Z_p\) having exactly \(r\) roots in \(\mathbb Q_p\)*, Proceedings of the London Mathematical Society 124 (2022), 713–736, DOI:10.1112/plms.12438.
