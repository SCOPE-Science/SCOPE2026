# Complete norm-gcd spectrum on primitive Gaussian lines

## Finding
Let \(a,b,c,d\in\mathbb Z\) satisfy \(c^2+d^2>0\), \(\gcd(c,d)=1\), and \(\gcd_{\mathbb Z[i]}(a+bi,c+di)=1\). Set
\[
\alpha_n=(a+cn)+(b+dn)i,\quad F(n)=N(\alpha_n)=(a+cn)^2+(b+dn)^2.
\]
Put \(A=c^2+d^2\), \(B=2(ac+bd)\), \(\Delta=ad-bc\), and let \(Q\) be the odd part of \(K=A^2+4\Delta^2\). Then for **every** \(n\in\mathbb Z\),
\[
\boxed{\gcd(F(n),F(n+1))=\gcd(Q,A(2n+1)+B).}
\]
Every prime dividing \(Q\) is congruent to \(1\pmod4\), and every positive divisor \(g\mid Q\) is attained as the gcd. For \(p^e\parallel Q\), put \(t=\nu_p(g)\). Define \(w_Q(g)\) multiplicatively by
\[
\boxed{w_Q(g)=\prod_{p^e\parallel Q}\begin{cases}(p-1)p^{e-t-1},&0\le t<e,\\1,&t=e.\end{cases}}
\]
Exactly \(w_Q(g)\) residues \(n\pmod Q\) have gcd \(g\), and hence for every \(X>0\),
\[
\#\{0\le n<X:\gcd(F(n),F(n+1))=g\}=\frac{w_Q(g)}{Q}X+O(Q).
\]
In particular, \(\gcd(F(n),F(n+1),F(n+2))=1\) for every integer \(n\).

## Assumptions and scope
The hypotheses are precisely a primitive lattice step \(\gcd(c,d)=1\), together with Gaussian coprimality of starting point and step. These are the conditions for a primitive Gaussian line with its least nonzero lattice step; the starting index need not be the minimum-norm point. The zero Gaussian integer is allowed as a term; integer gcds are nonnegative. The odd part of a positive integer is obtained by removing every factor of \(2\); here \(K\ge1\). All assertions are unconditional. This is a theorem about rational-integer norms, distinct from gcd in \(\mathbb Z[i]\).

## Proof
**No shared factor \(2\).** An integer Gaussian norm is even exactly when the Gaussian integer is divisible by \(1+i\). If both \(F(n)\) and \(F(n+1)\) were even, then \(1+i\) would divide both \(\alpha_n\) and \(\alpha_{n+1}\), hence also their difference \(\delta=c+di\) and \(\alpha_0=\alpha_n-n\delta\), contradicting Gaussian coprimality. Thus every adjacent norm gcd is odd.

**No odd prime divides both \(A\) and \(\Delta\).** Suppose an odd prime \(p\) does. Since \(\gcd(c,d)=1\), the vector \((c,d)\) is nonzero modulo \(p\). The equation \(c^2+d^2\equiv0\pmod p\) means \(p\equiv1\pmod4\). The determinant condition \(ad-bc\equiv0\pmod p\) forces \((a,b)\) to be a scalar multiple of \((c,d)\) modulo \(p\). In the split ring \(\mathbb Z[i]/p\mathbb Z[i]\simeq\mathbb F_p\times\mathbb F_p\), the nonzero zero-norm vector \((c,d)\) has a zero component, and hence \(\alpha_0\) and \(\delta\) share a Gaussian prime over \(p\), a contradiction. It follows that \(\gcd(A,\Delta)\) has no odd prime divisor. Thus every odd prime \(p\mid K\) satisfies \(p\nmid A\Delta\), and the congruence \(A^2\equiv-4\Delta^2\pmod p\) implies \(p\equiv1\pmod4\). In particular \(\gcd(A,Q)=1\).

**Exact local gcd.** Write \(D(n)=A(2n+1)+B\). Direct expansion yields
\[
F(n+1)-F(n)=D(n),\quad 4AF(n)=(D(n)-A)^2+4\Delta^2=D(n)^2-2AD(n)+K.
\]
Fix an odd prime \(p\). If \(p^e\) divides both adjacent norms, it divides \(D(n)\). If \(p\mid A\), the preceding paragraph shows \(p\nmid K\); the displayed identity then excludes any such simultaneous divisibility. When \(p\nmid A\), simultaneous divisibility by \(p^e\) is equivalent to \(p^e\mid D(n)\) and \(p^e\mid K\), by the identity and invertibility of \(4A\) modulo \(p^e\). Therefore
\[
\nu_p(\gcd(F(n),F(n+1)))=\min\{\nu_p(K),\nu_p(D(n))\}.
\]
Together with the absence of a common factor \(2\), this proves the boxed integer formula.

**Complete spectrum and exact frequencies.** For each \(p^e\parallel Q\), multiplication by \(2A\) is invertible modulo \(p^e\), so \(n\mapsto D(n)\pmod{p^e}\) permutes all residues. Exactly \((p-1)p^{e-t-1}\) residues have valuation precisely \(t<e\), and exactly one is zero modulo \(p^e\), corresponding to \(t=e\). The Chinese remainder theorem gives the product formula for \(w_Q(g)\), proves \(w_Q(g)>0\) for all \(g\mid Q\), and yields periodicity modulo \(Q\) and the stated counting error.

**Three-point rigidity.** A common prime divisor of \(F(n),F(n+1),F(n+2)\) would have to be odd. By the gcd formula it would divide both \(D(n)\) and \(D(n+1)\), hence \(2A\), contradicting \(\gcd(A,Q)=1\). The three-term gcd is therefore \(1\).

## Verification
The standalone exact-integer script `verify.py` checks the Gaussian Euclidean algorithm used to select valid primitive lines, and independently compares direct norm gcds with the formula on \(194060\) adjacent index pairs across \(6260\) primitive affine descriptions. It additionally checks the three-consecutive gcd and complete period fibers on sample lines. The test \(\alpha_n=9+ni\) gives \(Q=325\) and the exact frequency table \(w_Q(1)=240\), \(w_Q(5)=48\), \(w_Q(13)=20\), \(w_Q(25)=12\), \(w_Q(65)=4\), \(w_Q(325)=1\). The symbolic proof, not the finite tests, establishes the universal claim.

## Relationship to prior work
Magness, Nugent, and Robertson (2020 preprint; later 2021 publication) introduce primitive Gaussian lines and establish that consecutive Gaussian integers on such a line are coprime **in the ring of Gaussian integers** (their Theorem 3); their Theorems 10–11 characterize Gaussian divisors of individual line elements. Neither those results nor the inspected relevant sections compute the gcd of consecutive **rational-integer norms**, its complete divisor spectrum, or its exact periodic multiplicities. A shared rational prime can divide adjacent norms even though the Gaussian integers are coprime: \(N(1+2i)=5\) and \(N(1+3i)=10\). Classical polynomial resultant arguments bound prime support; the present primitive-line specialization determines exact gcd values and all fibers.

## Limitations
No statement is made about primes on the line, their asymptotic distribution, or general nonprimitive line descriptions. The finite verification samples are not proofs for arbitrary coefficients. Possible unindexed or more general polynomial-resultant classifications remain a bibliographic originality risk; independent mathematical review has not been performed.

## References
1. E. Magness, B. Nugent, and L. Robertson, *Walking to Infinity Along Gaussian Lines*, arXiv:2001.05018v1 (first public posting 2020-01-14), Sections 2, 4, 6; published in *Integers* 21 (2021). https://arxiv.org/pdf/2001.05018
2. Public research record: *Finite-resultant correction for coprime values of homogeneous binary forms*, published-finding corpus identifier `2026/10/4/SCOPE-finite-resultant-correction-for-coprime-values-of-homogeneous-bi--0efa4a963ad2`; distinct two-variable density setting.
