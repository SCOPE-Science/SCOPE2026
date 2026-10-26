# Fixed-prime-support classification of non-Wieferich integers in arbitrary bases, including the dyadic exception

## Finding
Fix an integer base \(b\ge2\). For each integer \(n\ge2\) coprime to \(b\), write \(L_b(n)=\operatorname{ord}_n(b)\), and call \(n\) **non-Wieferich in base \(b\)** when
\[
\gcd\!\left(n,\frac{b^{L_b(n)}-1}{n}\right)=1.
\]
For every prescribed nonempty finite set of primes \(S\), all coprime to \(b\), the non-Wieferich integers with **exact** prime support \(S\) admit the following complete classification. No assumption about the scarcity of Wieferich primes is needed.

Put \(P=S\setminus\{2\}\). For each \(p\in P\), define
\[
t_p=\operatorname{ord}_{p}(b),\quad s_p=\nu_p(b^{t_p}-1),\quad
h_p=\max\bigl(\{0\}\cup\{\nu_p(t_q):q\in P\setminus\{p\}\}\bigr),\quad A_p=s_p+h_p.
\]
For \(n=\prod_{p\in S}p^{a_p}\) with every \(a_p\ge1\), the non-Wieferich condition at **every odd** prime holds exactly when \(a_p\ge A_p\) for all \(p\in P\). If \(2\notin S\), that is the complete criterion.

If \(2\in S\), necessarily \(b\) is odd. Set
\[
g=\max\bigl(\{0\}\cup\{\nu_2(t_q):q\in P\}\bigr),\quad
d=\nu_2(b-1),\quad e=\nu_2(b+1).
\]
The additional, **necessary and sufficient** condition on \(a_2\) is
\[
\begin{cases}
a_2\ge d+g,&b\equiv1\pmod4;\\
a_2\ge e+g,&b\equiv3\pmod4,\ g\ge1;\\
a_2=1\ \text{or}\ a_2\ge e+1,&b\equiv3\pmod4,\ g=0.
\end{cases}
\]
Thus on any fixed odd prime support the admissible exponent vectors form one translated nonnegative orthant. On a support containing \(2\) they do as well, except that the last case has one extra isolated \(2\)-exponent layer \(a_2=1\) (with freely varying admissible odd exponents). The exceptional layer is genuine: for base \(7\) and support \(\{2,3\}\), \(6\) and \(48\) are non-Wieferich, while \(12\) and \(24\) are Wieferich.

Write \(r=|S|\), and let \(N_{b,S}(X)\) count these integers at most \(X\). Then, for fixed \(b,S\),
\[
N_{b,S}(X)=\frac{(\log X)^r}{r!\prod_{p\in S}\log p}
+O_{b,S}\bigl(1+(\log X)^{r-1}\bigr)\qquad(X\to\infty).
\]
In particular, every allowable fixed prime support contains infinitely many non-Wieferich integers, including supports containing Wieferich primes for the chosen base.

## Assumptions and scope
The base \(b\) is any integer at least \(2\), and \(S\) is any nonempty finite set of primes satisfying \(p\nmid b\) for all \(p\in S\). All exponents \(a_p\) are positive integers and no primes outside \(S\) divide \(n\). A maximum over an empty collection is defined as \(0\). The valuation \(\nu_p\) is normalized by \(\nu_p(p)=1\). The order \(L_b(n)\) exists since \(\gcd(n,b)=1\). The definition extends the familiar odd-integer base-two Wieferich criterion to arbitrary coprime bases and to even integers; no claim is made that this terminology is standard for even integers.

## Proof
**1. Prime-power orders at odd primes.** For odd \(p\in S\), the order \(t_p\) divides \(p-1\) and hence \(p\nmid t_p\). By the lifting-the-exponent lemma, whenever \(t_p\mid m\),
\[
\nu_p(b^m-1)=s_p+\nu_p(m/t_p)=s_p+\nu_p(m).
\]
Consequently, the exact order modulo \(p^{a_p}\) is
\[
\operatorname{ord}_{p^{a_p}}(b)=t_p p^{\max(0,a_p-s_p)}.
\]
The global order is the least common multiple of the prime-power orders. The order modulo a power of \(2\), if present, is itself a power of \(2\). Therefore
\[
\nu_p(L_b(n))=\max\{\max(0,a_p-s_p),h_p\},
\]
and so
\[
\nu_p(b^{L_b(n)}-1)=s_p+\max\{\max(0,a_p-s_p),h_p\}
=\max\{a_p,s_p+h_p\}.
\]
Since \(n\mid b^{L_b(n)}-1\), the local coprimality condition is the equality of this valuation with \(a_p\); precisely \(a_p\ge A_p\).

**2. Prime-power orders at \(2\).** Suppose \(2\in S\); then \(b\) is odd. Write \(a=a_2\) and \(k=\nu_2(L_b(n))\). The odd-prime orders contribute exactly \(g\) to the maximum defining \(k\). Standard binary lifting gives
\[
\nu_2(b^{2^k}-1)=
\begin{cases}
d,&k=0;\\
d+e+k-1,&k\ge1.
\end{cases}
\]
If \(b\equiv1\pmod4\), then \(d\ge2\), \(e=1\), and
\[
\nu_2(\operatorname{ord}_{2^a}(b))=\max(0,a-d).
\]
Thus \(k=\max(g,0,a-d)\) and \(\nu_2(b^{L_b(n)}-1)=d+k\) (including \(k=0\)). Equality with \(a\) holds if and only if \(a\ge d+g\).

If \(b\equiv3\pmod4\), then \(d=1\) and \(e\ge2\). For \(a=1\), the order modulo \(2\) is \(1\), so \(k=g\); equality \(\nu_2(b^{L_b(n)}-1)=1\) occurs exactly when \(g=0\). For \(a\ge2\), binary lifting yields
\[
\nu_2(\operatorname{ord}_{2^a}(b))=\max(1,a-e),
\]
so \(k=\max(g,1,a-e)\) and \(\nu_2(b^{L_b(n)}-1)=e+k\). The equality \(a=e+k\) is equivalent to \(a\ge e+\max(1,g)\). Combining the \(a=1\) and \(a\ge2\) cases yields exactly the stated alternatives.

**3. Counting.** Each unrestricted exponent orthant \(a_p\ge A_p\) (and the corresponding \(2\)-adic threshold) is in bijection with lattice points \(\mathbf k\in\mathbb Z_{\ge0}^{r}\) satisfying
\[
\sum_{p\in S} k_p\log p\le\log X-C_{b,S},
\]
where the constant \(C_{b,S}\) is the logarithm of the least integer in that orthant. The right simplex has Euclidean volume \((\log X-C_{b,S})^r/(r!\prod_{p\in S}\log p)\). Unit-cube comparison gives a lattice-point discrepancy of \(O_{b,S}(1+(\log X)^{r-1})\): the inner and outer parallel simplices differ by a bounded displacement in every coordinate, changing volume by at most that order. In the exceptional \(a_2=1\) layer, the dimension drops to \(r-1\), so its contribution is \(O_{b,S}(1+(\log X)^{r-1})\). This proves the claimed asymptotic.

## Verification
The accompanying `verify.py` independently constructs the multiplicative order by factoring Euler's totient and testing modular powers; it compares the resulting prime-by-prime modular congruence with the theorem's thresholds across assorted bases, prime supports, and exponent vectors. Its checks are finite consistency tests; Steps 1–3 above establish the infinite statements without relying on enumeration. To reproduce, run `python3 verify.py` with a standard Python 3 interpreter.

## Relationship to prior work
Falk–Harrington–Jones (2026) establish prime-level generalized Wieferich congruences in their study of monogenic trinomials. Their primary MSC includes \(11A41\), and their original version appeared on July 31, 2026. Their theorems concern polynomial monogenicity and prime congruences, not a composite-integer exact-radical classification. Franco–Pomerance (1995) introduce the base-two composite Wieferich criterion and prove distributional results; their local prime obstructions provide context but not the full fixed-support exponent description. Siegel's later October 19, 2026 preprint treats the global distribution of odd base-two non-Wieferich numbers and proves a sufficient squarefree criterion. The present work includes its own exact prime-power valuation criterion, every finite support, arbitrary bases, and the even-integer exception. The later preprint is acknowledged only for its mathematical comparison; the principal recent precursor is the July 2026 study of generalized base-\(b\) Wieferich congruences.

## Limitations
The classification is restricted to numbers coprime to the fixed base. It does not count over varying supports or estimate how often base-\(b\) Wieferich primes occur. The proof uses classical lifting-the-exponent and multiplicative-order facts, and a broad uncatalogued theorem of this kind could subsume the formulation. Independent literature review and independent proof audit have not been performed.

## References
1. Amy Falk, Joshua Harrington, and Lenny Jones, *Generalized Wieferich primes and monogenic trinomials*, arXiv:2607.29329v1, publicly submitted July 31, 2026. https://arxiv.org/abs/2607.29329
2. V. Franco and C. Pomerance, *On a conjecture of Crandall concerning the \(qx+1\) problem*, 1995. https://math.dartmouth.edu/~carlp/PDF/paper101.pdf
3. Casia Siegel, *An Asymptotic for Non-Wieferich Numbers*, arXiv:2610.28685v1, submitted October 19, 2026. https://arxiv.org/abs/2610.28685
