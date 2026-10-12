# Exact Liouville sign and zero locus for the quadratic Möbius-floor recurrence
## Finding
For every positive integer \(n\), define the integer sequence \(s(1)=1\) and
\[
s(n)=1-n-\sum_{d=2}^{n-1}s(d)\left\lfloor\frac nd\right\rfloor^2\qquad(n\ge2).
\]
Let \(\Omega(n)\) count prime factors with multiplicity, let \(\lambda(n)=(-1)^{\Omega(n)}\), and write \(n=2^a m\), where \(m\) is odd and \(a\ge0\). Then for every integer \(n\ge2\),
\[
\lambda(n)s(n)\ge0,\qquad
s(n)=0\ \Longleftrightarrow\ a\ge\Omega(m)+3.
\]
The first inequality is strict exactly when the displayed zero condition fails. Furthermore,
\[
s(n)\equiv\mu(n)\pmod2,\qquad
s(n)=-1\ \Longleftrightarrow\ n\text{ is prime}.
\]
In fact \(|s(n)|=1\) also holds exactly at the primes. These conclusions give a complete global sign and zero classification for the fixed quadratic specialization of the recurrence introduced in the reference.

## Assumptions and scope
The recurrence uses the ordinary floor function and is integer-valued. The notation \(\mu\) is the classical Möbius function; \(\Omega(1)=0\). The prime criterion is asserted only for \(n\ge2\), as \(s(1)=1\). All convolutions below are Dirichlet convolutions \((f*g)(n)=\sum_{d\mid n}f(d)g(n/d)\), with identity \(\delta\) supported at \(1\). Write \(u(n)=1\) and \(\operatorname{id}(n)=n\). Formal multivariate series in finitely many variables are used only coefficientwise; no analytic convergence is assumed.

## Proof
**Step 1 (exact convolution identity).** Including the \(d=1\) term in the recurrence gives, for each \(n\ge1\),
\[
\sum_{d\le n}s(d)\left\lfloor\frac nd\right\rfloor^2=n^2-n+1.
\]
Subtract the equality at \(n-1\), with the empty sum at \(n=0\) understood as zero. For fixed \(d\), the floor changes only when \(d\mid n\); at such a jump its square increases by \(2(n/d)-1\). Therefore
\[
s*(2\operatorname{id}-u)=2\operatorname{id}-2u+\delta.
\]
Euler's identity \(\operatorname{id}=u*\varphi\) gives \(2\operatorname{id}-u=u*(2\varphi-\delta)\), and \(u^{-1}=\mu\) under Dirichlet convolution. The function \(2\varphi-\delta\) has value \(1\) at \(1\), hence an inverse \(H=(2\varphi-\delta)^{-1}\). Convolving yields the exact identity
\[
s=\delta+(\mu-\delta)*H.
\tag{1}
\]

**Step 2 (a nonnegative Liouville twist).** For any finite prime set \(P\), form formal power series in variables \((x_p)_{p\in P}\), in which the coefficient of \(\prod_{p\in P}x_p^{e_p}\) is the corresponding arithmetic-function value on \(\prod p^{e_p}\). Dirichlet convolution becomes series multiplication. The series for \(u\) and \(\operatorname{id}\) are respectively \(\prod(1-x_p)^{-1}\) and \(\prod(1-px_p)^{-1}\); consequently that for \(\varphi\) is \(\prod(1-x_p)/(1-px_p)\). Replacing every \(x_p\) by \(-x_p\) twists coefficients by \(\lambda\). Thus the twisted series for \(H\) equals
\[
\frac{\prod_{p\in P}(1+px_p)}{2\prod_{p\in P}(1+x_p)-\prod_{p\in P}(1+px_p)}
=\frac{\prod_{p\in P}(1+px_p)}{1-K_P},
\]
where
\[
K_P=\sum_{\varnothing\ne S\subseteq P}\left(\prod_{p\in S}p-2\right)\prod_{p\in S}x_p.
\tag{2}
\]
Every coefficient of \(K_P\) is nonnegative: the coefficient is zero only at the singleton \(S=\{2\}\); otherwise its displayed integer is strictly positive. Since \(K_P\) has no constant term, \((1-K_P)^{-1}=\sum_{j\ge0}K_P^j\) is a well-defined formal series with nonnegative coefficients. It follows for every positive integer \(n\) that
\[
h(n):=\lambda(n)H(n)\ge0,\qquad h(1)=1.
\tag{3}
\]

**Step 3 (exact support of \(h\)).** Write \(n=2^a m\) with \(m\) odd and \(b=\Omega(m)\). The numerator in (2) supplies at most one factor \(x_2\); any factor of \(x_2\) in \(K_P\) also uses at least one odd-prime variable, because the singleton \(x_2\) coefficient vanishes. Therefore
\[
h(n)>0\ \Longrightarrow\ a\le b+1.
\]
Conversely, for \(a=0\), the positive singleton terms \((p-2)x_p\) for odd \(p\) generate every odd integer's exponent vector (and the constant term covers \(n=1\)). If \(1\le a\le b+1\), take \(2x_2\) from the numerator, use \(a-1\) of the \(b\) odd-prime occurrences to form positive \((2p-2)x_2x_p\) terms of \(K_P\), and generate every remaining odd occurrence from positive singleton \((p-2)x_p\) terms. This constructs a strictly positive monomial contribution. Hence the **exact** criterion is
\[
h(2^a m)>0\ \Longleftrightarrow\ a\le\Omega(m)+1.
\tag{4}
\]

**Step 4 (sign, zeros, parity).** For \(n>1\), equation (1) gives
\[
\lambda(n)s(n)
=\sum_{\substack{d\mid n,\ d>1\\\mu(d)\ne0}} h(n/d),
\tag{5}
\]
because \(\mu(d)=\lambda(d)\) on squarefree integers and \(\lambda\) is completely multiplicative. Every summand is nonnegative. If \(n\) is odd, choosing any prime divisor \(d\) makes \(n/d\) odd, so (4) makes the sum positive. If \(a\ge1\) and \(a\le b+2\), choosing \(d=2\) makes \(h(n/2)>0\). Finally, if \(a\ge b+3\), every squarefree divisor \(d\) can remove at most one factor of two while possibly removing odd-prime factors. Thus \(v_2(n/d)>\Omega((n/d)_{\mathrm{odd}})+1\), so (4) makes every summand zero. This proves precisely the stated sign and zero classification.

Modulo \(2\), the function \(2\varphi-\delta\) equals \(\delta\), so its inverse \(H\) is congruent to \(\delta\). By (1), \(s\equiv\mu\pmod2\).

**Step 5 (the exact prime fiber).** When \(n=p\) is prime, (5) consists only of \(h(1)=1\), and \(\lambda(p)=-1\); hence \(s(p)=-1\). Conversely, for a squarefree composite \(n\), the term \(d=n\) contributes \(1\). Choosing any prime \(p\mid n\), the distinct divisor \(d=n/p>1\) contributes \(h(p)=2(p-1)\ge2\), as is immediate from (2). Therefore \(|s(n)|\ge3\). For a nonsquarefree \(n\), every squarefree divisor \(d\) of \(n\) leaves \(n/d>1\). Here \(H(n/d)\) is even, since \(H\equiv\delta\pmod2\); thus (5) makes \(s(n)\) even and it cannot be \(-1\) or have absolute value \(1\). This completes the proof. \(\square\)

## Verification
The standalone `verify.py` directly evaluates the original floor recurrence up to \(n=700\), and separately computes all terms up to \(n=100000\) using the **proved** divisor-difference convolution. It independently constructs \(H\) by exact Dirichlet inversion of \(2\varphi-\delta\) through \(n=12000\). These independent implementations agree and check the sign theorem, exact zero-support condition, parity, and prime fiber. The reproduced numerical result is in `verification_output.txt`. No finite enumeration is used in the infinite proof; the decisive coefficientwise inequalities (2)–(5) are formal and exact.

## Relationship to prior work
Andrews, Kauffman, and Sahoo introduce the recurrence for numerical specializations \(f(t)=t^k\), and formulate the prime-only value \(-1\) as a conjecture for positive \(k\). Their stronger verbal formulation for arbitrary fixed \(f\) is not valid as written: the choice \(f\equiv1\) makes all values at \(n\ge2\) equal to \(-1\), as shown in an accessible published counterexample. This does **not** defeat the specific quadratic conjecture. The source's argument of nonidentity across **all** admissible \(f\) does not imply the numerical quadratic statement proved here. Nor does the source supply the Liouville sign law, exact two-adic zero threshold, or parity characterization. A separate recently published family of prime criteria constructed from the Dirichlet inverse of divisor powers and Jordan totients has different objects and does not imply this recurrence theorem. Source and theorem comparisons were made on their actual statements, not merely titles.

## Limitations
Only the quadratic numerical specialization \(f(t)=t^2\) is proved; no statement about all \(k\), all admissible functions, higher generality, or computational speed is asserted. The method determines signs and exact zeros, not a closed form for every nonzero magnitude. The prime fiber is a structural characterization and is not asserted to be a fast primality test. The conjectured fixed quadratic statement and the broader false fixed-function wording must not be conflated. As with all literature comparisons, an unindexed equivalent preexisting proof remains possible; no independent audit has been conducted.

## References
1. G. E. Andrews, L. H. Kauffman, and D. Sahoo, *A surprising generalization of the Möbius function*, arXiv:2609.25628v1 (first made public September 22, 2026), particularly the defining recurrence, Theorem 1, and the conjectured numerical family.
2. *A constant-function obstruction to a generalized Möbius primality criterion* (published October 2026), for the distinction between a fixed-function claim and the universal-in-functions formulation; no quadratic sign or zero classification is asserted there.
3. *Sharp parameter stability for mixed Dirichlet-inverse prime criteria* (published October 2026), for a distinct prime characterization involving divisor-power Dirichlet inverses and Jordan totients.
