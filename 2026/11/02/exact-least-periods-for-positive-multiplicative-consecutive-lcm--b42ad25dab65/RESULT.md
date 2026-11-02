# Exact least periods for positive multiplicative consecutive-LCM quotients

## Finding
For every integer \(k\ge1\) and every positive multiplicative function \(f:\mathbb N_{>0}\to\mathbb R_{>0}\) satisfying \(f(p^j)\ne f(p^{j-1})\) for each prime \(p\) and integer \(j\ge1\), define
\[
G_{k,f}(n)=\frac{\prod_{i=0}^{k}f(n+i)}{f(\operatorname{lcm}(n,n+1,\ldots,n+k))},\qquad n\ge1.
\]
Put \(e_p=\lfloor\log_p k\rfloor\) for primes \(p\le k\). The **exact least positive period** is
\[
\boxed{T_k(f)=\prod_{\substack{p\le k\\p^{e_p}\nmid(k+1)}}p^{e_p}}.
\]
For \(k=1\) the product is empty and the quotient is identically \(1\). In particular, for every real \(\alpha\ge0\), this is the exact period when \(f=\sigma_\alpha\), where \(\sigma_\alpha(n)=\sum_{d\mid n}d^\alpha\). This includes the ordinary divisor sum \(\sigma_1\) and divisor count \(\sigma_0\). The period formula also applies to other multiplicative functions with strictly unequal adjacent prime-power values; no complete multiplicativity is required.

## Assumptions and scope
The function takes finite **positive real** values and is multiplicative on coprime arguments, with \(f(1)=1\). The adjacent prime-power inequality is assumed for every prime and positive exponent (only the exponents \(1\le j\le e_p\) matter at a given \(k\)). The input \(n\) ranges over **all** positive integers. Neither positivity nor the adjacent inequality is dispensable in this theorem without replacement assumptions: for the constant function the least period is \(1\). No general period formula is asserted for the larger arithmetic-progression parameter family.

## Proof
Fix a prime \(p\le k\). Write \(e=\lfloor\log_p k\rfloor\), \(K=k+1\), and
\[
C_j(n)=\#\{0\le i\le k:p^j\mid n+i\},\qquad r_j=\frac{f(p^j)}{f(p^{j-1})}>0.
\]
Let \(a_i=\nu_p(n+i)\) and \(M=\max_{0\le i\le k}a_i\). Multiplicativity and telescoping prime-power factors give the \(p\)-local quotient
\[
\frac{\prod_{i=0}^k f(p^{a_i})}{f(p^M)}
=\prod_{j=1}^{M}r_j^{C_j(n)-1}.
\]
Since \(p^e\le k\), every \(k+1\) consecutive positive integers include a multiple of \(p^e\); hence \(M\ge e\). Since \(p^{e+1}>k\), for every \(j>e\) at most one element of the interval is divisible by \(p^j\). In the displayed product only \(1\le j\le M\) occur, and for each \(j>e\) within that range the unique element divisible by \(p^j\) has \(C_j(n)=1\). Consequently
\[
\boxed{g_p(n)=\prod_{j=1}^{e}r_j^{C_j(n)-1}}.
\]
Each \(C_j\) depends only on \(n\pmod{p^j}\); therefore \(g_p\) has period dividing \(p^e\), and \(G_{k,f}(n)=\prod_{p\le k}g_p(n)\). Primes greater than \(k\) contribute \(1\).

Suppose \(p^e\mid K\). Then \(p^j\mid K\) for all \(j\le e\), and every length-\(K\) interval has exactly \(K/p^j\) multiples of \(p^j\). Hence every \(C_j\), and therefore \(g_p\), is constant, and the local least period is \(1\).

Now suppose \(p^e\nmid K\). Write \(K=q p^e+s\), with \(1\le s<p^e\). On a complete set of residues \(n\pmod{p^e}\), \(C_e(n)\) equals \(q+1\) on a cyclic interval of exactly \(s\) residues and equals \(q\) on the remaining residues. A nonempty proper cyclic interval of consecutive residues has no nonzero translational symmetry: it has a unique directed boundary from outside to inside. In particular, \(C_e(n+p^{e-1})\not\equiv C_e(n)\). For all \(j<e\), however, \(C_j(n+p^{e-1})=C_j(n)\). Thus
\[
\frac{g_p(n+p^{e-1})}{g_p(n)}
=r_e^{C_e(n+p^{e-1})-C_e(n)}
\]
is not identically \(1\), because \(r_e\ne1\). Since the local period divides \(p^e\), but \(p^{e-1}\) is not a period, its **least** period must be exactly \(p^e\).

It remains to show that the factors at different primes cannot cancel a missing local period. Let \(T\) be any positive integer period of the global product. The Chinese remainder theorem allows the arguments \(n\pmod{p^{e_p}}\) to vary independently for all primes \(p\le k\). Holding all other local residues fixed in
\[
\prod_{p\le k}\frac{g_p(n+T)}{g_p(n)}=1
\]
shows that each positive local ratio is a constant \(c_p\), independent of its residue. Repeated translation by \(T\) on the finite ring \(\mathbb Z/p^{e_p}\mathbb Z\) gives \(c_p^h=1\) for some positive integer \(h\). Positivity forces \(c_p=1\). Thus \(T\) is a period of each local factor and is divisible by every \(p^{e_p}\) for which \(p^{e_p}\nmid K\). Their product is itself a global period, proving the exact formula.

Finally, \(\sigma_\alpha(p^j)=1+p^\alpha+\cdots+p^{j\alpha}\) is positive and exceeds \(\sigma_\alpha(p^{j-1})\) by \(p^{j\alpha}>0\) for each \(\alpha\ge0\). This verifies the stated divisor-sum corollary without any special identities for the divisor-sum function.

## Verification
A standalone Python 3 script `verify.py` computes \(\sigma_\alpha\) by independent factorization, evaluates the original quotient directly, and compares it with the local-count product and the predicted least period. It tests \(\alpha\in\{0,1,2\}\) and \(1\le k\le10\), checking every proper divisor of the proposed period. It also tests a positive multiplicative function with prime-power values \(f(p^j)=2^{j^2}\), which is not completely multiplicative. Running `python verify.py` returned `VERIFY_OK: tested 7470 exact sigma_alpha comparisons (alpha=0,1,2), 987 non-geometric prime-power function states; all claimed periods were minimal`. These are finite corroborations, not a proof of the infinitely quantified result.

## Relationship to prior work
Qian, Tan and Hong (2012, arXiv:1201.0931v1) proved a general period bound for \(G_{k,f}\) in a more general arithmetic-progression setting and derived **exact least periods for Euler's totient**. Their concluding discussion explicitly asks for the least period when \(f=\sigma_\alpha\). The theorem above settles that stated special case for consecutive integers and extends it to an explicit positive multiplicative class. Farhi and Kane (2008, arXiv:0808.1507v1) previously determined the same formula for \(f(n)=n\). That identity case is fully covered by their theorem; the present contribution is not the numerical period formula alone but its validity for divisor sums and for the stated genuinely multiplicative (not necessarily completely multiplicative) class. The identity result does **not** directly determine \(G_{k,\sigma_\alpha}\). The accessible related statements and focused literature comparisons did not show an already-published exact period classification for these divisor-sum quotients; equivalent later or more general coverage remains possible.

## Limitations
The theorem does not classify arbitrary multiplicative functions with vanishing or repeating adjacent prime-power ratios, complex-valued functions (where cancellation may occur), nor generalized arithmetic progressions. It does not assert that every instance of the result is itself new: in particular, the identity function and its nonzero real powers inherit the earlier least-period formula. The literature comparison cannot prove global novelty, and an unlocated broader exact-period theorem may subsume the result. The Python checks cover only stated finite ranges.

## References
1. G. Qian, Q. Tan, S. Hong, *On the periodicity of a class of arithmetic functions associated with multiplicative functions*, arXiv:1201.0931v1, publicly submitted 2012-01-04. https://arxiv.org/abs/1201.0931
2. B. Farhi, D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507v1, publicly submitted 2008-08-11. https://arxiv.org/abs/0808.1507
