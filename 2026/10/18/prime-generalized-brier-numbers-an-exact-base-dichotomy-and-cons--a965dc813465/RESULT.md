# Prime generalized Brier numbers: an exact base dichotomy and consecutive-prime strings

## Finding
For each integer \(b\ge2\), call a positive integer \(k\) a *generalized Brier coefficient in base* \(b\) if
\[
\gcd(k-1,b-1)=\gcd(k+1,b-1)=1
\]
and both \(kb^n-1\) and \(kb^n+1\) are composite for every integer \(n\ge1\).

**Theorem.** The following conditions on an integer \(b\ge2\) are equivalent:

1. \(b\) is even and \(3\nmid b-1\).
2. There exist infinitely many *prime* generalized Brier coefficients in base \(b\).
3. There is a fixed reduced arithmetic progression, all sufficiently large positive members of which are generalized Brier coefficients in base \(b\), and for each such member \(k\) and every \(n\ge1\), both \(kb^n-1\) and \(kb^n+1\) have at least **two distinct prime divisors**.
4. For every integer \(h\ge1\), arbitrarily long in the sense of arbitrarily large starting primes, there are \(h\) consecutive primes all of which are generalized Brier coefficients in base \(b\).

More quantitatively, in condition 1 there exist integers \(Q\ge1\) and \(r\), with \(\gcd(r,Q)=1\), such that the proportion of primes \(k\le X\) that are generalized Brier coefficients has lower limit at least \(1/\varphi(Q)>0\). For each fixed \(h\), a positive lower proportion of consecutive-prime starting indices have \(h\) consecutive generalized Brier primes (using Maynard's strengthening of Shiu's theorem).

If \(b\) is odd, its only *possible* prime generalized Brier coefficient is \(2\); if \(3\mid b-1\), its only *possible* prime generalized Brier coefficient is \(3\). These statements give at most one candidate, not existence of the exceptional candidate.

## Assumptions and scope
All integers \(b\ge2\) and all exponents \(n\ge1\) are covered. The result uses the definition with both nontriviality conditions \(\gcd(k\pm1,b-1)=1\); removing either condition changes the classification. A *reduced progression* is a residue class \(r\pmod Q\) with \(\gcd(r,Q)=1\). The phrase “consecutive primes” means consecutive in the ordered global prime sequence, not successive terms of the progression.

The new argument is a coprime-residue refinement of the explicit two-sided covering-system construction of Virbalas (2026). That construction, not the bare existence of an arithmetic progression, is the premise used. The covering-system existence and its two-distinct-factor conclusion are cited from that published construction. The prime distribution and strings-of-primes consequences use standard named prime theorems.

## Proof
**1. Exact local obstruction.** Suppose \(k\) is prime. If \(b\) is odd, then \(2\mid b-1\), and every odd prime \(k\) has \(2\mid k-1\) and \(2\mid k+1\). Hence the two required gcds cannot equal \(1\): necessarily \(k=2\). If \(3\mid b-1\), every prime \(k\ne3\) is \(1\) or \(-1\) modulo \(3\); accordingly either \(k-1\) or \(k+1\) is divisible by \(3\). Necessarily \(k=3\). Either obstruction rules out infinitely many prime coefficients. Their absence is exactly the condition that \(b\) is even and \(3\nmid b-1\).

**2. Structure of the published covering congruences.** Virbalas's two-sided construction for every integer base \(b\ge2\) supplies finite covering systems for the plus and minus families, with designated congruences on \(k\). In the construction's displayed coefficient congruences (Section 3, including (3.6)–(3.8)), the prime-power and auxiliary-prime factors used for the two coverings are pairwise coprime and have multiplicative order of \(b\) greater than \(1\) at every prime divisor. Thus no covering prime divides \(b\) or \(b-1\). The required residue on each such factor is a unit: it is of the shape \(\pm b^{-a}\), interpreted modulo the relevant prime power. There is also a coefficient congruence \(k\equiv1+b^M\pmod{b^{M+1}}\), again a unit residue, which is independent of \(b-1\). To force the two nontriviality gcds, the published proof imposes the independent condition \(k\equiv0\pmod{b-1}\). The proof of simultaneous divisibility by at least two distinct primes for each sign and each exponent only uses the covering congruences, not the particular residue \(0\pmod{b-1}\).

These properties are the only imported construction facts. In particular, the existence theorem alone would *not* imply the existence of prime coefficients: its exhibited class with \(k\equiv0\pmod{b-1}\) may fail to be reduced.

**3. A reduced simultaneous progression.** Now assume \(b\) is even and \(3\nmid b-1\). Keep every covering prime-power congruence and the coefficient congruence modulo \(b^{M+1}\), but replace the independent final congruence by
\[
k\equiv2\pmod{b-1}.
\]
When \(b=2\), this congruence is vacuous. In general \(b-1\) is odd and coprime to \(3\), so
\[
\gcd(2,b-1)=\gcd(2-1,b-1)=\gcd(2+1,b-1)=1.
\]
All retained moduli are coprime to \(b-1\), and their prescribed coefficient residues are units. By the Chinese remainder theorem there is a residue \(r\pmod Q\) simultaneously satisfying all these conditions. Its reduction modulo every prime dividing \(Q\) is nonzero; hence \(\gcd(r,Q)=1\). Moreover, the two nontriviality gcds equal \(1\) for every \(k\equiv r\pmod Q\). Every sufficiently large positive such \(k\) obeys the original two covering proofs and therefore has at least two distinct prime divisors in *both* \(kb^n-1\) and \(kb^n+1\), for every \(n\ge1\). The finitely many excluded small \(k\) can be eliminated by passing to a sufficiently large tail of the same progression. This proves condition 3.

**4. Primes and prime strings.** The prime number theorem for fixed coprime arithmetic progressions yields
\[
\#\{k\le X: k\text{ prime},\ k\equiv r\pmod Q\}
\sim\frac{\operatorname{Li}(X)}{\varphi(Q)}.
\]
Discarding the finite exceptional prefix does not change this density. Therefore the Brier-prime proportion has lower limit at least \(1/\varphi(Q)>0\), proving condition 2. Shiu's theorem on strings of primes in a fixed reduced residue class gives, for any \(h\ge1\), infinitely many blocks of \(h\) consecutive primes contained in \(r\pmod Q\), and thus all Brier coefficients after discarding an initial finite segment. Maynard's strengthening supplies positive lower density of starting prime indices for each fixed \(h\). Hence condition 4 holds. Finally, condition 4 implies condition 2, and the obstructions in step 1 imply that either condition 2, 3 or 4 forces condition 1. All four conditions are equivalent. \(\square\)

## Verification
The deduction rests on independently checkable local gcd and CRT arguments and on three cited general theorems: Virbalas's two-sided coverings with distinct prime factors, the prime number theorem in arithmetic progressions, and the Shiu--Maynard consecutive-prime results. The accompanying `verify.py` tests the exact local residue criterion and coprime CRT patch on many finite instances. It is **not** an enumeration or certificate of the infinitely many covering congruences, the primality of infinitely many coefficients, or consecutive-prime density. The universal statements follow from the proof and the cited theorems, not from finite testing.

## Relationship to prior work
Virbalas (2026) proves, for every base, the existence of an infinite progression of two-sided generalized Brier coefficients with two distinct prime divisors for each sign. Its proof chooses the residue \(0\pmod{b-1}\); that particular progression need not contain infinitely many primes. The new point is the unit-residue replacement and resulting exact across-base prime dichotomy. Filaseta--Juillerat--Luckner (2022/2023) already proved the **base-two** consecutive-prime Brier phenomenon, and indeed a stronger base-two result involving digital delicacy. That base-two case is not claimed as new. Evans--Harrington--Heiney--Wieczorek (2025/2026) construct generalized Brier coefficients of the prescribed form \(tb^t+\alpha\) in certain bases, but their assertion does not establish that the coefficients are prime or give this all-base classification. The prime-progression and consecutive-prime principles are classical and are not claimed as original.

## Limitations
No small explicit prime generalized Brier coefficient, minimal coefficient, effective value of \(Q\), or optimal progression is produced. The argument is conditional only in the ordinary sense of citing established theorems, **not** on any open conjecture. The exceptional single candidates \(k=2\) and \(k=3\) in disallowed bases are not classified individually. The mathematics does not claim the 2026 covering construction itself, the base-two phenomenon, or the Shiu--Maynard results as new. An implicit previously published coprime-residue refinement for arbitrary bases remains an originality risk.

## References
1. P. Virbalas, *On the generalized Sierpiński and Riesel numbers*, Boletín de Matemáticas 33(1) (2026), 16–26, DOI: 10.15446/bol.mat.v33n1.125921; arXiv:2610.05149.
2. M. Filaseta, J. Juillerat, and T. Luckner, *Consecutive primes which are widely digitally delicate and Brier numbers*, Integers 23 (2023); arXiv:2209.10646.
3. H. Evans, J. Harrington, K. Heiney, and M. Wieczorek, *Generalized Sierpiński and Riesel numbers of the form \(tb^t+\alpha\)*, arXiv:2508.05942 (2025).
4. D. Shiu, *Strings of congruent primes*, Journal of the London Mathematical Society 61 (2000), 359–373.
5. J. Maynard, *Dense clusters of primes in subsets*, Compositio Mathematica 152 (2016), 1517–1554.
