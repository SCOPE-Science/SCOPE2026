# Exact parity-resolved two-step entry depths for the dyadic quadratic map

## Finding
For every integer \(k\ge1\), set \(f_k(x)=x^2+1\pmod{2^k}\) and \(g_k=f_k\circ f_k\). There is exactly one \(g_k\)-fixed residue \(u_k\) of even parity and one \(g_k\)-fixed residue \(v_k\) of odd parity. The pair \((u_k,v_k)\) is the unique periodic orbit of \(f_k\), and it has least period two, including at \(k=1\).

For parity \(p\in\{0,1\}\) and integers \(t\ge0\), let \(B_p(k,t)\) denote the number of parity-\(p\) residues satisfying \(g_k^t(x)=u_k\) for \(p=0\), or \(g_k^t(x)=v_k\) for \(p=1\). Thus \(B_p(k,t)-B_p(k,t-1)\), for \(t\ge1\), is exactly the number whose *first* arrival under the two-step map \(g_k\) occurs at step \(t\); both parity classes have one resident root at \(t=0\).

For each \(k\ge1\),
\[
B_0(k,0)=B_1(k,0)=1.
\]
For \(t\ge1\), write \(m=k-3(t-1)\). Then
\[
\boxed{B_0(k,t)=2^{k-1}\alpha(m),\qquad B_1(k,t)=2^{k-1}\beta(m),}
\]
where
\[
\alpha(m)=\begin{cases}
1,&m\le3,\\
\frac12,&4\le m\le6,\\
2^{5-m},&m\ge7,
\end{cases}
\qquad
\beta(m)=\begin{cases}
1,&m\le5,\\
2^{5-m},&m\ge6.
\end{cases}
\]
Every displayed count is an integer. Consequently the maximal two-step entry depths are \(0\) for either parity at \(k=1\), and for \(k\ge2\),
\[
\boxed{T_0(k)=\left\lceil\frac{k}{3}\right\rceil,\qquad
T_1(k)=\max\left\{1,\left\lceil\frac{k-2}{3}\right\rceil\right\}.}
\]
The full functional graph of \(f_k\) therefore consists of one directed two-cycle with incoming trees completely enumerated by parity and by the paired-step entry depth.

## Assumptions and scope
The map acts on the full residue ring \(\mathbb Z/2^k\mathbb Z\), with \(k\) an arbitrary positive integer; there are no restrictions on initial residues. Parity is invariant under \(g_k\) but swapped under \(f_k\). The quantities \(B_p(k,t)\) count arrivals after \(t\) *pairs* of iterations, not necessarily first entry after \(2t\) individual applications of \(f_k\). This distinction is essential. Valuations \(\nu_2\) in the proof are ordinary \(2\)-adic valuations, extended by \(\nu_2(0)=+\infty\).

## Proof
**Existence and uniqueness of the period-two orbit.** Over \(\mathbb Z_2\), set \(f(x)=x^2+1\) and
\[
 g(x)=f(f(x))=x^4+2x^2+2.
\]
The map \(g\) preserves parity, and for any \(x,y\),
\[
 g(x)-g(y)=(x-y)(x+y)(x^2+y^2+2).
\tag{1}
\]
When \(x,y\) are even, \(\nu_2(x^2+y^2+2)=1\) and \(\nu_2(x+y)\ge1\), so \(\nu_2(g(x)-g(y))\ge\nu_2(x-y)+2\). When both are odd, the corresponding factors have valuations \(2\) and at least \(1\), so the gain is at least \(3\). The contraction principle on each closed parity ball yields unique fixed points \(u\in2\mathbb Z_2\) and \(v\in1+2\mathbb Z_2\) for \(g\); every point of the corresponding ball converges to its unique fixed point. Since \(f\) commutes with \(g\) and swaps parity, \(f(u)=v\) and \(f(v)=u\). The reductions \(u_k,v_k\) are the unique fixed points of \(g_k\) in their parities; strict contraction rules out any additional periodic point of \(g_k\) and hence any other orbit of \(f_k\). The two elements have different parity, so their least \(f_k\)-period is exactly two.

**Sharp gain after the first pair.** Directly from \(g\), every even \(x\) satisfies \(g(x)\equiv2\pmod8\), and every odd \(x\) satisfies \(g(x)\equiv5\pmod{32}\); the same congruences hold for \(u,v\), respectively. For any \(z\equiv u\equiv2\pmod8\), equation (1) has \(\nu_2(z+u)=2\) and \(\nu_2(z^2+u^2+2)=1\). For \(z\equiv v\equiv5\pmod{32}\), the valuations are \(1\) and \(2\). In either case, if \(z\) differs from its fixed point, its distance valuation increases by *exactly three* on applying \(g\). It follows, for all \(t\ge1\), that
\[
 g^t(x)\equiv r\pmod{2^k}
\quad\Longleftrightarrow\quad
 g(x)\equiv r\pmod{2^{k-3(t-1)}},
\tag{2}
\]
where \(r=u\) on even residues and \(r=v\) on odd residues; a modulus with exponent at most zero makes the right-hand condition automatic.

**The first-pair congruences.** For any even \(x\), the factor \(x^2+u^2+2\) always has valuation \(1\), so
\[
\nu_2(g(x)-u)=1+\nu_2(x^2-u^2).
\]
Write \(x=2y\) and \(u=2a\) with odd \(a\). Then
\[
\nu_2(g(x)-u)=3+\nu_2(y^2-a^2).
\tag{3}
\]
For any odd \(x\), the factor \(x^2+v^2+2\) always has valuation \(2\), yielding
\[
\nu_2(g(x)-v)=2+\nu_2(x^2-v^2).
\tag{4}
\]
For odd \(a\), the congruence \(y^2\equiv a^2\pmod{2^h}\) has exactly four roots modulo \(2^h\) whenever \(h\ge3\), the usual four square roots of unity after multiplication by \(a^{-1}\). At \(h=1,2\) it requires only odd \(y\), with respective numbers \(1,2\) of roots. Indeed, for \(h\ge3\), the four roots of \(w^2\equiv1\pmod{2^h}\) are \(w\equiv\pm1,\pm1+2^{h-1}\pmod{2^h}\), as follows by considering the valuations of the two factors \((w-1)(w+1)\).

By (3), for a uniformly varying even \(x\), the proportion with \(g(x)\equiv u\pmod{2^m}\) is \(1\) for \(m\le3\); it is \(1/2\) for \(4\le m\le6\), because \(y\) must be odd; and for \(m\ge7\) it is \(4/2^{m-3}=2^{5-m}\). By (4), for a uniformly varying odd \(x\), the condition is automatic for \(m\le5\); for \(m\ge6\) its four roots among the \(2^{m-3}\) odd classes modulo \(2^{m-2}\) have proportion \(2^{5-m}\). Here \(m\le k\), so these proportions are valid in the complete residue ring modulo \(2^k\). Combining with (2) and multiplying by \(2^{k-1}\) residues of each parity proves the formulas for \(B_0,B_1\).

Finally the first \(t\ge1\) at which \(B_0(k,t)\) reaches \(2^{k-1}\) is the first with \(k-3(t-1)\le3\); the analogous odd threshold is \(k-3(t-1)\le5\). Together with the initial count \(B_p(k,0)=1\), these yield the claimed exact maxima, including \(k=1\) separately. \(\square\)

## Verification
The accompanying standalone `verify.py` enumerates all residues modulo \(2^k\) for \(1\le k\le17\), independently traces each two-step orbit to its parity root, and compares every cumulative entry-depth count against the formulas. It checks the unique two-cycle, both parity histograms, and boundary values. The run completed successfully with `VERIFY_OK`; the proof above, rather than finite enumeration, establishes the result for all positive \(k\).

For example, modulo \(256\) (\(k=8\)), the even-class exact-depth counts at \(t=0,1,2,3\) are \((1,15,48,64)\); the odd-class counts at \(t=0,1,2\) are \((1,15,112)\).

## Relationship to prior work
Fan and Liao proved the general \(2\)-adic quadratic minimal-decomposition theorem and specifically showed that \(f(x)=x^2-\lambda\) with \(\lambda\equiv3\pmod4\) has one attracting period-two orbit and full attraction basin (Theorem 6.1(4)); taking \(\lambda=-1\) gives this theorem's qualitative dynamical setting. That prior result **already covers** the existence, uniqueness, and global attracting behavior of the two-cycle. The new quantified assertion is the exact number of residues arriving at each paired iteration for **every** finite dyadic quotient, separately by parity, including the sharp extremal depths. The cited theorem's proof gives no such finite-depth distribution. Anashin's general \(p\)-adic ergodicity criteria address measure-preserving dynamics and do not supply this noninvertible polynomial's transient-depth distribution.

## Limitations
These are distributions in units of two applications of \(f\), not individual-step hitting-time distributions. The results concern this polynomial modulo powers of two, not arbitrary odd moduli or arbitrary quadratic coefficients. The qualitative attractor theorem was previously known. A thorough publication-priority check could reveal another exact finite-depth formula outside the inspected primary sources. Independent mathematical review remains outstanding.

## References
1. A.-H. Fan and L. Liao, *On minimal decomposition of p-adic polynomial dynamical systems*, arXiv:1010.5583v2 (first public version 27 October 2010), especially Theorem 6.1 and its proof. https://arxiv.org/html/1010.5583v2
2. V. Anashin, *Ergodic Transformations in the Space of p-adic Integers*, arXiv:math/0602083v1 (5 February 2006), particularly Section 1 and the characterizations of measure-preserving and ergodic maps. https://arxiv.org/html/math/0602083v1
