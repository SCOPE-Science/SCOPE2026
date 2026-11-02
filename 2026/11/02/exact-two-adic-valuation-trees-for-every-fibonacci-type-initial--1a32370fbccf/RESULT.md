# Exact two-adic valuation trees for every Fibonacci-type initial pair

## Finding
Let \(u,v\in\mathbb Z\) with at least one odd, and define \(U_0=u\), \(U_1=v\), and \(U_{n+2}=U_{n+1}+U_n\) for all integers \(n\ge0\). Put \(\nu_2(0)=+\infty\). Among \(r=0,1,\ldots,5\), precisely one has \(4\mid U_r\); denote it by \(r\). The index \(r+3\pmod6\) is the other even residue class, and there \(\nu_2(U_n)=1\); all four remaining classes have valuation zero.

Exactly one of the following occurs.

**Bounded case.** If \(U_r\equiv4\pmod8\), then for every integer \(t\ge0\),
\[
\nu_2(U_{6t+r})=2.
\]

**Root case.** If \(U_r\equiv0\pmod8\), there exists a unique two-adic integer \(\tau=\tau(u,v)\in\mathbb Z_2\) such that for every integer \(t\ge0\),
\[
\nu_2(U_{6t+r})=3+\nu_2(t-\tau).
\]
In particular, for every integer \(k\ge3\), exactly one residue class of \(t\pmod{2^{k-3}}\) satisfies \(2^k\mid U_{6t+r}\). These classes form a compatible nested sequence converging to \(\tau\). No such index exists in the bounded case.

Consequently, the natural densities of nonnegative indices satisfying \(2^k\mid U_n\) are \(1/3\) for \(k=1\), \(1/6\) for \(k=2\), and, for \(k\ge3\), either \(1/(6\cdot2^{k-3})\) (root case) or zero (bounded case). Of the \(48\) ordered pairs \((u,v)\pmod8\) not both even, exactly \(24\) belong to each case.

## Assumptions and scope
The statement concerns the recurrence with characteristic polynomial \(X^2-X-1\), arbitrary integer starting values, and nonnegative indices. For nonzero \((u,v)\) both even, let \(h=\min\{\nu_2(u),\nu_2(v)\}\), divide both starting values by \(2^h\), apply the classification above, and add \(h\) to each valuation. If \(u=v=0\), every valuation is infinite. Writing \(F_n\) and \(L_n\) for the standard Fibonacci and Lucas numbers, \(aF_n+bL_n\) has initial values \((2b,a+b)\), so the method applies to all integer \(a,b\).

## Proof
**1. Parity and the unique high class.** Let \(M=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). Then \(M^3=I+2M\). Modulo two, the nonzero states \((U_{n+1},U_n)\) cycle with period three; among three consecutive terms precisely one is even, and its successor is odd. Thus precisely two terms among the first six are even, at positions separated by three. For even \(U_n\), the identity \(U_{n+3}=U_n+2U_{n+1}\) shows that these two even values differ by two modulo four. Exactly one is divisible by four; call its residue \(r\). By the same identity modulo four (and \(M^6\equiv I\pmod4\)), its companion class always has valuation one, and the four remaining classes are odd.

**2. An exact two-adic isometry.** Matrix multiplication gives the stronger identity \(M^6=5I+8M\). For \(z\in\mathbb Z_2\), define the convergent function
\[
G_r(z)=\sum_{j=0}^{\infty}\binom zj\left(\frac85\right)^jU_{r+j}.
\]
The binomial coefficients are two-adic integers and the series converges uniformly because \(\nu_2(8/5)=3\). For nonnegative integer \(t\), the binomial theorem for \(M^{6t}=(5I+8M)^t\) gives the exact identity
\[
G_r(t)=5^{-t}U_{6t+r}.
\]
For any distinct \(z,w\in\mathbb Z_2\) and integer \(j\ge1\), the falling-factorial difference is divisible by \(z-w\) as a polynomial with integer coefficients, so
\[
\nu_2\!\left(\binom zj-\binom wj\right)\ge\nu_2(z-w)-\nu_2(j!).
\]
Since \(U_r\) is even and \(U_{r+1}\) odd, the \(j=1\) term in \(G_r(z)-G_r(w)\) has valuation exactly \(3+\nu_2(z-w)\). Every term with \(j\ge2\) has valuation at least \(3j-\nu_2(j!)+\nu_2(z-w)\ge5+\nu_2(z-w)\). Therefore no cancellation occurs at the leading valuation, proving
\[
\boxed{\nu_2(G_r(z)-G_r(w))=3+\nu_2(z-w)}.
\]
In particular, \(G_r(\mathbb Z_2)\subseteq U_r+8\mathbb Z_2\), and \(H(z)=(G_r(z)-U_r)/8\) is an isometry of \(\mathbb Z_2\). For every \(k\), reduction modulo \(2^k\) gives an injective self-map of a set of \(2^k\) residues, hence a bijection. Completeness implies that \(H\) is surjective onto \(\mathbb Z_2\). Thus \(G_r\) is a bijection \(\mathbb Z_2\to U_r+8\mathbb Z_2\).

**3. Exact valuations and congruence trees.** If \(U_r\equiv4\pmod8\), every element of \(U_r+8\mathbb Z_2\) has valuation two; therefore the bounded formula follows. If \(8\mid U_r\), then zero lies in \(U_r+8\mathbb Z_2\); bijectivity gives a unique \(\tau\in\mathbb Z_2\) with \(G_r(\tau)=0\). By the isometry,
\[
\nu_2(U_{6t+r})=\nu_2(G_r(t))=3+\nu_2(t-\tau),
\]
since \(5^t\) is odd. Hence, for \(k\ge3\), divisibility by \(2^k\) is exactly the congruence \(t\equiv\tau\pmod{2^{k-3}}\), proving uniqueness and all density assertions. This is an infinite theorem based on the isometry, not on finite testing.

**4. Exactly half the initial pairs.** There are \(4\cdot4\cdot3=48\) ordered pairs modulo eight with at least one odd entry. For each fixed parity pair, there are sixteen lifts modulo eight. The residue \(r\pmod6\) is determined by the initial pair modulo four. Replacing either starting value by that value plus four preserves the initial pair modulo four, hence preserves \(r\), and at least one of the two replacements changes \(U_r\) by four modulo eight: its coefficient in the linear expression for \(U_r\) must be odd, because \(M^r\) is invertible modulo two. This pairs the \(U_r\equiv0\pmod8\) and \(U_r\equiv4\pmod8\) lifts, eight of each in every parity class. The total is thus \(24\) of each kind.

## Verification
The standalone Python file `verify.py` uses only exact integers. It enumerates all \(48\) primitive initial pairs modulo eight and independently checks \(11\) successive divisibility levels, including the number and location of zero classes, as well as the low-valuation residues. It also checks \(2760\) additional signed initial pairs in the square \([-30,30]^2\), excluding even-even pairs. The observed output is:

```text
VERIFY_OK primitive_classes_mod8=48 unbounded_classes=24 modular_censuses=528 additional_integer_pairs=2760
```

Run `python3 verify.py` in the directory containing the file. These finite computations test the deductions but do not prove the two-adic isometry or its infinite consequences.

## Relationship to prior work
The standard formula for valuations of Fibonacci numbers is a special case \((u,v)=(0,1)\), with \(r=0\) and \(\tau=0\). The Lucas case \((u,v)=(2,1)\) lies in the bounded branch with \(r=3\). Medina and Rowland study the regularity of valuations of the standard Fibonacci sequence, not arbitrary initial pairs. Chavoya, Lucero, and Reynolds examine the family \(aF_n+bL_n\) and provide particular coefficient formulas, explicitly leaving other coefficient patterns unresolved. Shu and Yao study regularity of valuations of quadratic recurrences; such a characterization does not itself give this explicit unique-root index formula for every starting pair. Rowland and Yassawi provide general twisted interpolation tools, but their displayed applications concern limits and densities of attained **values** rather than the present exact divisibility-index classification. A formula covering every coefficient pair or a stronger result implied by these sources would supersede this claim; no such exact statement was located in the inspected material.

## Limitations
The recurrence coefficients are fixed at \((1,1)\), the prime is two, and no analogous formula for arbitrary second-order recurrences or other primes is asserted. The two-adic parameter \(\tau\) is specified effectively by compatible modular residues but need not have a simple rational expression. The result does not classify which pairs have an actual *integer* zero beyond the explicit condition \(\tau\in\mathbb Z_{\ge0}\); nor does it imply new results about prime factors other than two. Published-source coverage is not exhaustive, and no independent mathematical audit has been performed.

## References
1. L. A. Medina and E. Rowland, *\(p\)-regularity of the \(p\)-adic valuation of the Fibonacci sequence*, arXiv:0910.2907, first submitted 15 October 2009, later published in Fibonacci Quarterly 53 (2015), 265–271.
2. Z. Shu and J.-Y. Yao, *Analytic functions over \(\mathbb Z_p\) and \(p\)-regular sequences*, Comptes Rendus Mathématique 349 (2011), 947–952, doi:10.1016/j.crma.2011.08.001 (published online 31 August 2011).
3. J. Chavoya, A. Lucero, and S. Reynolds, *On \(p\)-adic valuations of the generalized Fibonacci sequences*, 2014 MSRI-UP Research Reports, pp. 91–99 (report dated August 2014; precise day not established).
4. E. Rowland and R. Yassawi, *\(p\)-adic asymptotic properties of constant-recursive sequences*, arXiv:1602.00176, first submitted 31 January 2016; Indagationes Mathematicae 28 (2017), 205–220.
