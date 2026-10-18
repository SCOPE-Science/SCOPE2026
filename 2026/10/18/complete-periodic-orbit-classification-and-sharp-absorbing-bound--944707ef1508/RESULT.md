# Complete periodic-orbit classification and sharp absorbing bound for \(\varphi(n)+3\)

## Finding
Let \(\varphi\) denote Euler's totient function with \(\varphi(1)=1\), and define \(F:\mathbb N\to\mathbb N\) by
\[
F(n)=\varphi(n)+3.
\]
For **every** positive integer \(n\), the forward orbit \(n,F(n),F^2(n),\ldots\) eventually enters the interval \(\{1,2,\ldots,25\}\) and subsequently reaches **exactly one** of these three periodic orbits:
\[
(9),\qquad(11,13,15),\qquad(23,25).
\]
They have least periods \(1\), \(3\), and \(2\), respectively; there are no other periodic points. The upper endpoint \(25\) is optimal: no initial interval \(\{1,\ldots,B\}\) with \(B<25\) eventually contains **every** forward orbit. The six periodic points also form the unique smallest (by inclusion) forward-invariant set that eventually contains every orbit.

## Assumptions and scope
The domain is all positive integers, with ordinary Euler totient and no restriction on the starting value. A periodic orbit means a finite orbit of least positive period; cyclic rotations denote the same orbit. An **absorbing initial interval** is a set \(\{1,\ldots,B\}\) into which every forward orbit eventually enters and which is forward invariant under \(F\). Nothing here concerns the distinct second-order recurrence \(x_{j+2}=\varphi(x_{j+1})+\varphi(x_j)+k\).

## Proof
**Step 1: a composite cototient bound.** Put \(c(m)=m-\varphi(m)\). If \(m\) is composite and \(p\) is its least prime divisor, then \(p\le\sqrt m\), while Euler's product formula gives
\[
\varphi(m)=m\prod_{q\mid m,\ q\text{ prime}}(1-q^{-1})\le m(1-p^{-1}).
\]
Hence
\[
c(m)\ge m/p\ge\sqrt m.\tag{1}
\]
In particular, every composite \(m\ge26\) satisfies \(F(m)=m+3-c(m)<m\).

**Step 2: prime inputs also fall below their starting value.** Let \(p\ge29\) be prime. Then \(F(p)=p+2\). If \(p+2\) is composite, (1) yields \(c(p+2)\ge\sqrt{p+2}>5\), so
\[
F^2(p)=p+5-c(p+2)<p.\tag{2}
\]
If \(p+2\) is prime, both \(p\) and \(p+2\) exceed \(3\); considering residues modulo \(3\), necessarily \(p\equiv2\pmod3\) and \(p+4\) is divisible by \(3\). As \(F^2(p)=p+4\), Euler's product formula gives
\[
F^3(p)=\varphi(p+4)+3\le\tfrac23(p+4)+3
=\frac{2p+17}{3}<p,\tag{3}
\]
where the final inequality follows from \(p>17\). Therefore **every** \(n\ge26\) has a strictly smaller positive iterate within at most three steps: composite \(n\) in one step and prime \(n\) in two or three steps.

**Step 3: global absorption.** Direct totient calculation gives the complete map on the first \(25\) positive integers:

```text
 n :  1  2  3  4  5   6  7  8  9 10  11 12 13 14 15  16 17 18 19 20  21 22 23 24 25
F(n): 4  4  5  5  7   5  9  7  9  7  13  7 15  9 11  11 19  9 21 11  15 13 25 11 23
```

Every value in the second row is at most \(25\), so the interval is forward invariant. By strong induction on the starting value \(n\), the strict-smaller-iterate result in Steps 1–2 implies that every orbit from \(n\ge26\) eventually enters that interval: the claim holds trivially when \(n\le25\); otherwise some iterate is \(m<n\), and the induction hypothesis applies to \(m\). Thus this is a **global**, not experimentally truncated, absorption proof.

**Step 4: complete cycle census inside the finite trap.** Following the arrows in the displayed complete table shows that the only cycles are \(9\mapsto9\), \(11\mapsto13\mapsto15\mapsto11\), and \(23\mapsto25\mapsto23\). More explicitly, among initial states \(1\) through \(25\), the states converging to \(9\) are
\[
\{1,2,3,4,5,6,7,8,9,10,12,14,18\};
\]
the states on the \(23\leftrightarrow25\) cycle are \(\{23,25\}\); and the remaining ten states reach \((11,13,15)\). Since all external orbits enter this interval, the three cycles exhaust **all** periodic orbits in \(\mathbb N\).

**Step 5: optimality and the minimal attracting set.** The orbit \(23\leftrightarrow25\) prevents any absorbing initial interval from having upper endpoint below \(25\). Conversely, Step 3 proves that endpoint \(25\) suffices. The union of the three cycles is forward invariant and eventually contains every forward orbit. Any forward-invariant set that eventually contains **every** orbit must contain the entirety of each cycle, by applying the requirement to an initial value on that cycle. Therefore the union of six periodic points is uniquely inclusion-minimal.

## Verification
The included standalone `verify.py` performs integer-only checks independent of numerical floating-point approximations. It checks the complete \(25\)-state map against direct trial-division totients, exercises both prime branches and composite descent for each \(26\le n<5000\), and independently calculates totients by a sieve and by prime factorization. A functional-graph census for all one million starting values from \(1\) to \(10^6\) reaches exactly the three stated cycles; the maximum observed transient length is \(46\). In this finite range the basin counts are \(13\), \(999976\), and \(11\) for the \(9\)-fixed point, \((11,13,15)\), and \((23,25)\), respectively. These computations serve as regression tests; Steps 1–5, not the census, establish the infinite statement.

Run `python3 verify.py` in a Python 3 installation; it imports only `math`. No external data, software packages, or online services are required.

## Relationship to prior work
Leonetti and Luca prove eventual periodicity of \(n\mapsto\varphi(n)+k\) for every fixed nonnegative \(k\) and bound each orbit in terms of its initial value. At \(k=3\), their theorem gives \(\sup_j x_j\le\max\{x_1,81\}+16\); it neither identifies periodic orbits nor supplies a start-independent absorbing interval of \(25\). Their proof also uses the standard inequality (1), which is used here without claiming that inequality as new.

The public result *Sharp period-size bound and extremal structure for shifted Euler cycles* proves that any least-period-\(T\) cycle of this map with \(k\ge2\) has maximum at most \([T(k-1)+1]^2\), and explicitly exhibits \(23\leftrightarrow25\) for \(k=3\). Its bound permits arbitrarily large maxima as \(T\) grows and gives no restriction to \(T\in\{1,2,3\}\). The present classification **includes** that known two-cycle, but its exclusion of all other cycles and its sharp uniform absorbing interval are not consequences of that period-sensitive inequality.

Danh and collaborators improve an upper bound for a **different**, second-order recurrence involving two preceding totients. The arithmetic-function tables for the cototient \(n-\varphi(n)\) do not by themselves classify the global iterated dynamics. No consulted statement implies this exact three-cycle spectrum or the universal absorbing endpoint \(25\).

## Limitations
The result concerns exactly the shift \(3\); it does not classify cycles for other values of \(k\) or give a closed-form test for the global basin of an arbitrary starting number without iteration. The finite verification is not an infinite proof. Although targeted searches found no equivalent classification, an unindexed or unexamined older result remains a literature risk. No independent external verification is claimed.

## References
1. P. Leonetti and F. Luca, *On the iterates of shifted Euler's function*, arXiv:2302.01783v1 (first posted 2023-02-03); journal version, *Bulletin of the Australian Mathematical Society* **109** (2024), 206–214, DOI 10.1017/S0004972723000394. Full open-access text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EA94859586A3742D43EA0E099B2630A9/S0004972723000394a.pdf/on_the_iterates_of_the_shifted_eulers_function.pdf.
2. *Sharp period-size bound and extremal structure for shifted Euler cycles*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-period-size-bound-and-extremal-structure-for-shifted-euler--02d25ffc40ae.
3. T. N. T. Danh et al., *An improvement to a theorem of Leonetti and Luca*, *Bulletin of the Australian Mathematical Society* **109** (2024), 437–442, DOI 10.1017/S0004972723000862.
4. OEIS A051953, cototient sequence \(n-\varphi(n)\), https://oeis.org/A051953.
