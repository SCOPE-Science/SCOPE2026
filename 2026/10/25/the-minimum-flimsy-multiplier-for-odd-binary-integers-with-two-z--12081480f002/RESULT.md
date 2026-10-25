# The minimum flimsy multiplier for odd binary integers with two zeroes

## Finding
Let \(s_2(v)\) denote the number of nonzero binary digits of the positive integer \(v\). Define the *first flimsy multiplier* of \(N\) to be
\[
\mu(N)=\min\{k\ge 1:s_2(kN)<s_2(N)\},
\]
with value \(\infty\) when the set is empty.

**Theorem.** For every integer \(L\ge7\), every odd \(L\)-bit integer having exactly two zeroes has a unique expression, reading its binary bits from least significant to most significant, as
\[
1^a\,0\,1^b\,0\,1^c,\qquad a,c\ge1,\ b\ge0,\quad a+b+c+2=L.
\]
Its exact first flimsy multiplier is
\[
\mu(N)=\begin{cases}
3,&b\ge1,\ a\ge2,\\
5,&(b\ge1,\ a=1,\ c\ge2)\text{ or }(b=0,\ a\ge3,\ c\ge2),\\
7,&b=0,\ c=1,\\
9,&b=0,\ a\in\{1,2\},\\
\infty,&b\ge1,\ a=c=1.
\end{cases}
\]
These five classes are disjoint and exhaustive in the stated domain. Their respective numbers at length \(L\) are
\[
\binom{L-4}{2},\qquad 2L-11,\qquad1,\qquad2,\qquad1.
\]
Thus the answer depends only on a few local run-length conditions even as \(L\) grows.

## Assumptions and scope
The integer is odd and has a leading binary digit of one; its representation has exactly two interior zero digits. The run parameter \(b\) is allowed to vanish, but \(a\) and \(c\) are positive. The lower length bound is essential to the displayed partition: shorter words have exceptional behavior (for example, \(51\) is sturdy). A multiplier is a **positive integer**, and the minimum is in multiplier size, not in the attained digit sum.

## Proof
**1. It suffices to examine odd multipliers.** For every \(t\ge0\), \(s_2(2^tv)=s_2(v)\). If an even multiplier decreases digit sum, removing its power of two gives a smaller odd multiplier that also decreases digit sum. The multiplier \(1\) never decreases digit sum. We shall completely determine the first success among the odd multipliers \(3,5,7,9\), and independently prove that the last class has no witness at all.

**2. Four-one stability.** Fix any odd \(k\le9\). In the standard least-significant-digit-first multiplication algorithm, suppose the incoming carry is \(r\), where \(0\le r\le k-1\). For input digit \(x\in\{0,1\}\), output digit and new carry are
\[
y=(kx+r)\bmod2,\qquad r'=\left\lfloor\frac{kx+r}{2}\right\rfloor.
\]
On a run of input ones put \(e=k-1-r\). Then \(e'=\lfloor e/2\rfloor\). Since \(0\le e\le8\), at most four ones leave \(e=0\), i.e. carry \(k-1\). Every additional one thereafter produces one output bit and leaves the carry unchanged. Therefore inserting one extra one into **any run already containing four ones**, while keeping the other digits fixed, increases both \(s_2(N)\) and \(s_2(kN)\) by exactly one. The final carry bits are unchanged. Consequently \(s_2(kN)-s_2(N)\) is unchanged by capping any of the three run lengths at four, for each \(k\in\{3,5,7,9\}\).

More explicitly, let \(a'=\min(a,4)\), \(b'=\min(b,4)\), \(c'=\min(c,4)\). Since \(a,c\ge1\) and the original length is at least seven, \(a'+b'+c'+2\ge7\). Replacing the triple by its capped triple preserves all four comparisons \(s_2(kN)<s_2(N)\).

**3. Exact finite-state certificate.** There are precisely \(70\) triples
\[
1\le a'\le4,\quad0\le b'\le4,\quad1\le c'\le4,\quad a'+b'+c'+2\ge7.
\]
Each represents the explicit integer
\[
N_{a',b',c'}=(2^{a'}-1)+2^{a'+1}(2^{b'}-1)+2^{a'+b'+2}(2^{c'}-1).
\]
For each of the \(70\) triples, direct integer binary digit counts for \(k=3,5,7,9\) give exactly the first-four-multiplier classification in the theorem, except that the last class has none of those four multipliers. The class counts across the \(70\) triples are \(47,17,1,3,2\), for first multipliers \(3,5,7,9\), and none, respectively. The embedded self-contained `verify.py` enumerates the **entire** finite set and tests each digit count by two independent routes: native exact integer binary counting and an explicit bit-serial multiplication/carry algorithm. This is an exhaustive finite certificate of the stated condition, not sampling of the unbounded theorem.

By Step 2, every uncapped triple has the same four comparisons as its capped triple. In all classes where one of these multipliers succeeds, the certificate excludes every smaller odd candidate; Step 1 excludes even candidates. Thus the displayed multiplier is globally minimal.

**4. No multiplier succeeds in the last class.** For \(a=c=1\) and \(b\ge1\), elementary evaluation of the binary word gives
\[
N=3(2^{L-2}-1),\qquad s_2(N)=L-2.
\]
Every positive multiple of \(2^r-1\), for a positive integer \(r\), has at least \(r\) binary ones. To see this, take the binary expansion of any such multiple. Replace every summand \(2^j\) with \(j\ge r\) by \(2^{j-r}\), folding high digits modulo \(2^r-1\), and normalize collisions with binary carries. Each fold reduces the positive integer, while neither replacement nor binary carrying increases the number of ones. Repeating terminates at a positive integer at most \(2^r-1\) divisible by \(2^r-1\), hence exactly \(2^r-1\), whose binary weight is \(r\). Therefore every multiple has at least \(r\) ones. Taking \(r=L-2\) proves that the last class is sturdy, so its minimum is \(\infty\).

**5. Exact class counts.** The triples satisfying \(b\ge1,a\ge2\) number \(\binom{L-4}{2}\) by stars-and-bars. The two cases for multiplier five contain \(L-5\) and \(L-6\) triples. The cases for seven, nine, and sturdiness contain \(1,2,1\) triples. The total is \(\binom{L-2}{2}\), the number of choices for the two interior zero positions, so the partition is exhaustive. This proves all assertions. \(\square\)

## Verification
Run `python3 verify.py` with standard Python 3. It enumerates all \(70\) capped triples, tests all four odd multipliers using both arithmetic digit counts and an independent carry transducer, and asserts the exact classification. The package also includes a separate stress test at lengths \(7\) through \(80\); the finite-state proof, not that stress test, supplies the infinite quantifier. The verifier returned `VERIFIED` before packaging.

## Relationship to prior work
Clokie, Lidbetter, Molina Lovett, Shallit, and Witzman, *Computational Aspects of Sturdy and Flimsy Numbers* (arXiv:2002.02731, first version February 7, 2020; journal version 2022), define the minimum flimsy witness, give general algorithms for computing it, and classify which odd two-zero binary numbers are sturdy. Their preprint Theorem 15(c) establishes the sturdy exceptions, and Section 11 reports that multipliers up to nine suffice to certify the remaining cases. The conference version *Computational Fun with Sturdy and Flimsy Numbers* (2021), Theorem 16(c), gives the same sturdy/flimsy boundary. These results do not state the complete first-witness run-length partition or its exact length-by-length counts. The last sturdy class and the general idea of automata for digit multiplication are acknowledged prior knowledge; the claimed addition is the *exact first successful multiplier* uniformly across the entire natural family.

## Limitations
This classification covers **odd two-zero words of length at least seven**, not words with other zero counts or general bases. The known short exceptional case \(51\) lies outside the theorem. It proves no claim about minimum *attained digit sum*, which is a different function. The finite certificate rests on the elementary four-one reduction and its own exact arithmetic; independent external review has not been performed. An unindexed earlier first-witness table remains a possible originality risk.

## References
1. T. Clokie, T. F. Lidbetter, A. Molina Lovett, J. Shallit, and L. Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731 (first posted February 7, 2020); Theoretical Computer Science 927 (2022), 65–86. https://arxiv.org/abs/2002.02731 ; https://doi.org/10.1016/j.tcs.2022.05.029 .
2. Same authors, *Computational Fun with Sturdy and Flimsy Numbers*, FUN 2021, LIPIcs 157 (2020 publication series), article 10. https://drops.dagstuhl.de/storage/00lipics/lipics-vol157-fun2021/LIPIcs.FUN.2021.10/LIPIcs.FUN.2021.10.pdf .
