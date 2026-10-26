# Complete weirdness criterion in a square-root prime strip

## Finding
Let \(k\ge1\), \(M=2^{k+1}-1\), and let \(M<p<q\) be odd primes. Write \(x=p-M\), suppose \((x-1)^2\le M\), and let \([t]_p\) denote the least residue of \(t\) in \(\{0,1,\ldots,p-1\}\). Then \(2^kpq\) is weird if and only if
\[
\frac{M(p+1)}{x+1}<q<\frac{Mp}{x}
\quad\text{and}\quad
1\le[x(q+1)]_p\le x-1. \tag{1}
\]
In particular, every weird number in this infinite family has abundance \(a=\sigma(2^kpq)-2^{k+1}pq\) satisfying
\[
M<a<q,\qquad
a<\frac{M(p+1)}{x+1}<\frac{(M+1)(M+2)}{3}. \tag{2}
\]
Thus Iannucci's proposed universal upper bound on abundance holds throughout the prime strip \((p-M-1)^2\le M\); statement (1) additionally gives an exact criterion with one congruence and two explicit interval inequalities.

## Assumptions and scope
An integer \(n\) is *abundant* if its divisor sum \(\sigma(n)>2n\), *semiperfect* if it is a sum of distinct proper divisors, and *weird* if abundant but not semiperfect. Here \(k\) is any positive integer, and \(p<q\) are any distinct odd primes obeying the stated gap condition. Since \(M\) is odd and \(p\) is odd, \(x=p-M\) is a positive even integer (so \(x\ge2\)). No upper bound on \(k\) or on \(q\) is assumed. The condition \((x-1)^2\le M\) is precisely sufficient for \(p>x(x-1)\), the size inequality used in the proof.

## Proof
**Divisor-sum and subset-sum reduction.** Since \(\sigma(2^k)=M\), direct multiplication gives
\[
a=M(p+1)(q+1)-(M+1)pq=M(p+1)-xq.\tag{3}\]
Consequently
\[
a=M(M+1)-x(q-M)<M(M+1)<Mp<pq.\tag{4}\]
A positive abundant integer is semiperfect exactly when its abundance is a sum of distinct proper divisors: this follows by taking the complement inside the set of proper divisors, whose total sum is \(n+a\).

Every proper divisor of \(2^kpq\) smaller than \(pq\) belongs to one of the sets \(\{2^i\}\), \(\{2^ip\}\), \(\{2^iq\}\), with \(0\le i\le k\). As \(a<pq\), any representation of \(a\) by distinct proper divisors therefore has the form
\[
a=r+sp+tq,\qquad 0\le r,s,t\le M,\tag{5}\]
where each coefficient is independently expressible as a sum of distinct powers of two in \(\{1,2,\ldots,2^k\}\). Formula (4) also ensures that if \(a-tq\ge0\), then \(0\le\lfloor(a-tq)/p\rfloor<M\). Hence a representation (5) exists exactly when some integer \(0\le t\le\lfloor a/q\rfloor\) satisfies
\[
[(a-tq)]_p\le M.\tag{6}
\]
If \(0<a\le M\), then the powers of two alone represent \(a\), so a weird number must have \(a>M\).

**The key short-gap exclusion.** Suppose that \(2^kpq\) is weird and, seeking a contradiction, that \(a\ge q\). The cases \(t=0,1\) are available in (6), so neither residue may be at most \(M\). There exist integers \(h_0,h_1\in\{1,\ldots,x-1\}\) such that
\[
[a]_p=p-h_0,\qquad [a-q]_p=p-h_1.\tag{7}
\]
Write \(\delta=h_1-h_0\), so \(|\delta|\le x-2\) and \(q\equiv\delta\pmod p\). Since \(p\) and \(q\) are distinct primes, \(\delta\ne0\). By (3), modulo \(p\),
\[
a\equiv -x(q+1)\equiv-x(\delta+1),
\quad\text{so}\quad h_0\equiv x(\delta+1)\pmod p.\tag{8}
\]
The gap hypothesis implies
\[
p=M+x\ge(x-1)^2+x=x(x-1)+1>x(x-1).\tag{9}
\]
If \(\delta\ge1\), then \(2x\le x(\delta+1)\le x(x-1)<p\), contradicting \(h_0\le x-1\). If \(\delta=-1\), the right side of (8) vanishes, again impossible. Finally, if \(\delta\le-2\), then \(x(\delta+1)\) lies between \(-x(x-3)\) and \(-x\), so its least residue is at least \(p-x(x-3)>2x>x-1\). These exhaustive cases contradict (8); hence \(a<q\).

**Exact converse.** For a weird number, \(M<a<q\) and (3) yield
\[
\frac{M(p+1)}{x+1}<q<\frac{Mp}{x}.\tag{10}
\]
With \(a<q\), only \(t=0\) can appear in (6). Its forbidden-residue condition \([a]_p>M\) is, by (8) before substituting \(\delta\), equivalent to \(1\le[x(q+1)]_p\le x-1\). This proves necessity of (1).

Conversely, if (1) holds, (3) gives \(M<a<q\). Because \([a]_p=p-[x(q+1)]_p>M\), the only possible residue in (6), with \(t=0\), is forbidden. Thus no proper-divisor subset sums to \(a\); since \(a>0\), the integer is weird. The equivalence is proved.

Lastly, \(a<q\) and (3) give \(a<M(p+1)/(x+1)\), and, because \(x\ge2\),
\[
\frac{(M+1)(M+2)}3-\frac{M(p+1)}{x+1}
=\frac{(x-2)M^2+2(x+1)}{3(x+1)}>0.
\]
This proves (2).

## Verification
Run `python3 verify.py`. This independent finite corroboration enumerates primes for \(1\le k\le9\) inside the full gap strip, tests every pair still satisfying positive abundance, and compares the new criterion with the original binary-coefficient subset-sum test. It reports `VERIFY_OK tested_prime_pairs 48596 weird_witnesses 69`, including the non-Fermat-prime example \(k=3,p=19,q=61,a=56\). The universal claim is proved above; finite enumeration is not invoked to extend its quantifiers.

## Relationship to prior work
Iannucci's 2015 work classified the bounded layers \(k\le14\), gave the general subset-sum obstruction, and conjectured \(a<(M+1)(M+2)/3\) for all weird integers of this form. A subsequent published note on this family establishes the uniform but weaker bound \(a<3M^2/4+M\), without the square-root-gap classification. The present result proves the conjectured stronger bound in a growing prime strip and reduces weirdness therein to one explicit modular residue and two inequalities. The 2016 multiple-prime-factor construction paper provides sufficient families, not this necessary-and-sufficient condition. Tables of known weird numbers verify individual examples but do not themselves imply the unbounded statement.

## Limitations
Nothing is established here for primes \(p\) beyond the given gap strip. No claim is made that there are infinitely many prime pairs in the strip, nor that the strip threshold is optimal. It remains possible that an unindexed earlier argument contains the same short-gap criterion. The verification file checks finitely many small layers; the proof gives the all-\(k\) statement.

## References
1. D. E. Iannucci, “On primitive weird numbers of the form \(2^kpq\),” arXiv:1504.02761v1, first posted 7 April 2015, https://arxiv.org/abs/1504.02761.
2. “A uniform three-quarter abundance bound for weird numbers of form \(2^kpq\),” online mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-uniform-three-quarter-abundance-bound-for-weird-numbers-of-for--b810d8b66c9f.
3. G. Amato, M. F. Hasler, G. Melfi, M. Parton, “Primitive weird numbers having more than three distinct prime factors,” Riv. Mat. Univ. Parma (2016); open manuscript https://arxiv.org/abs/1802.07178.
4. OEIS A258333, historical table of numbers of weird integers of form \(2^kpq\), https://oeis.org/A258333.
