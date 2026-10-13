# Exact factorial thresholds and reversible lcm tower-height records

## Finding
For an integer \(m>1\), define its prime-factorization tower height by \(h(m)=1+\max_{p^e\parallel m}h(e)\), with \(h(1)=0\). Set \(E_1=2\) and \(E_{j+1}=2^{E_j}\), and for \(N\ge1\) let \(L(N)=\operatorname{lcm}(1,2,\ldots,N)\). For each \(k\ge1\), define the first hitting indices
\[
F_k=\min\{N\ge2:h(N!)\ge k\},\qquad
G_k=\min\{N\ge2:h(L(N))\ge k\}.
\]
Then
\[
F_1=2,\quad F_2=4,\quad F_k=E_{k-1}+2\ (k\ge3),
\qquad G_k=E_k\ (k\ge1).
\]
Furthermore, **every** integer \(k\ge3\) exhibits an exact record plateau followed by a one-level drop:
\[
h(L(N))=k\quad(E_k\le N<2E_k),\qquad
h(L(2E_k))=k-1.
\]
In particular, the factorial indices first reaching heights \(3,4,5\) are \(6,18,65538\), whereas the corresponding lcm indices are \(16,65536,2^{65536}\). Thus the lcm-height process has arbitrarily high temporary records that disappear at precisely twice their first index.

## Assumptions and scope
All variables \(N,k,j\) are positive integers, with the displayed restrictions. Each factorization exponent \(e\) in the recursion is a positive integer; allowing \(e=1\) invokes \(h(1)=0\). The notation \(p^e\parallel m\) means that \(p^e\) is the exact power of prime \(p\) dividing \(m\). No numerical cutoff or statistical hypothesis is assumed. Bertrand's postulate (a prime strictly between \(x\) and \(2x\) for real \(x\ge2\)) is used solely to guarantee a prime in an explicitly defined interval.

## Proof
**Minimal tower lemma.** For every \(j\ge1\), the least integer \(m\) with \(h(m)\ge j\) is \(E_j\). For \(j=1\), it is \(2\). If \(h(m)\ge j+1\), some prime-power exponent \(e\) of \(m\) has \(h(e)\ge j\); induction gives \(e\ge E_j\), hence \(m\ge 2^{E_j}=E_{j+1}\). Equality is attained by \(2^{E_j}\). In particular, \(h(E_j)=j\), and all integers strictly below \(E_j\) have height at most \(j-1\).

**Factorials.** Legendre's identity gives
\[
\nu_p(N!)=\sum_{r\ge1}\left\lfloor\frac{N}{p^r}\right\rfloor
\le\sum_{r\ge1}\left\lfloor\frac{N}{2^r}\right\rfloor=\nu_2(N!)
\]
for every prime \(p\le N\). For \(k\ge3\), write \(B=E_{k-1}=2^a\) with \(a=E_{k-2}\ge2\). Since \(B\) is a power of two, Legendre's formula (or the binary digit-sum identity) gives \(\nu_2(B!)=B-1\). Moreover, \(B+1\) is odd and \(\nu_2(B+2)=1\), so
\[
\nu_2((B+1)!)=B-1,\qquad \nu_2((B+2)!)=B.
\]
At all earlier factorial indices, every prime exponent is strictly below \(B\), the least integer of height at least \(k-1\); therefore \(h(N!)<k\) for \(N\le B+1\). At \(B+2\), the exponent of \(2\) is exactly \(B\), of height \(k-1\), while no exponent exceeds \(B\). Consequently \(h((B+2)!)=k\), proving \(F_k=B+2\). Direct computation gives \(h(1!)=0\), \(h(2!)=1\), \(h(3!)=1\), \(h(4!)=2\), hence \(F_1=2,F_2=4\).

**Lcm thresholds and plateaux.** For every prime \(p\le N\),
\[
\nu_p(L(N))=\max\{e\ge1:p^e\le N\}=\lfloor\log_p N\rfloor.
\]
When \(N<E_k=2^{E_{k-1}}\), each such exponent is smaller than \(E_{k-1}\), giving \(h(L(N))<k\). At \(N=E_k\), the exponent of \(2\) equals \(E_{k-1}\), hence \(h(L(E_k))=k\). This proves \(G_k=E_k\) (also for \(k=1\)). For \(k\ge3\), put \(B=E_{k-1}\ge4\). Throughout \(E_k\le N<2E_k\), the exponent of \(2\) remains exactly \(B\). Every other prime exponent is less than \(B\), because \(3^B>2^{B+1}\). By the minimal tower lemma, \(h(L(N))=k\) throughout this interval.

**The drop at twice the threshold.** Fix \(k\ge3\), write \(a=E_{k-2}\ge2\) and \(B=E_{k-1}=2^a\), and set \(N=2E_k=2^{B+1}\). Now \(\nu_2(L(N))=B+1\). The integer \(B+1\) is odd and satisfies \(B+1<3^a\). An odd integer of height at least \(k-1\) has an odd prime-power factor with exponent of height at least \(k-2\), so by the minimal tower lemma its value is at least \(3^a\). Thus \(h(B+1)\le k-2\). All exponents attached to odd primes in \(L(N)\) are strictly smaller than \(B\), so they also have height at most \(k-2\). Therefore \(h(L(N))\le k-1\).

For the reverse inequality, it suffices to find a prime \(p\) with \(\nu_p(L(N))=a\), since \(h(a)=k-2\). When \(k=3\), \(a=2,N=32\), and \(p=5\) works: \(5^2\le32<5^3\). When \(k=4\), \(a=4,N=131072\), and \(p=11\) works: \(11^4\le131072<11^5\). For \(k\ge5\), \(a\ge16\) and \(2^a+1>a(a+1)\). Put \(x=N^{1/(a+1)}\) and \(y=N^{1/a}\). Then
\[
\frac{y}{x}=2^{(2^a+1)/(a(a+1))}>2.
\]
Bertrand's postulate supplies a prime \(x<p<2x<y\). Hence \(p^a<N<p^{a+1}\), so \(\nu_p(L(N))=a\). In all cases \(h(L(N))\ge k-1\), completing the proof of the exact one-level drop.

## Verification
The standalone standard-library script `verify.py` computes exponents through exact integer divisions, factorizes only those exponents to calculate tower heights, and checks factorial first-hit boundaries at levels \(1\) through \(5\), lcm first-hit boundaries at levels \(1\) through \(4\), and the lcm plateau endpoints at levels \(3\) and \(4\). Run `python3 verify.py`. Its actual output appears in `verification_output.txt`. The finite tests are regression evidence; the proof above covers every level and every integer in each stated range.

## Relationship to prior work
De Koninck and Verreault introduce and study this exact tower-height function, deriving densities, average heights, and high consecutive runs; their Section 6 identifies the minimal height-\(k\) integer \(E_k\), which is explicitly used here as a known ingredient. Their results do not state the first factorial and lcm indices nor the exact, disappearing lcm record plateaux. In a separate paper, the same authors study numerous arithmetic functions on factorial arguments, but not this recursively defined tower height. An OEIS sequence A288636 displays the same first-height minima but defines another tower-height function via the gcd of all prime exponents, not the maximum used here. The present theorem concerns the original maximum-based height, evaluated on two specific arithmetic sequences, with a prime-existence argument for the drop.

## Limitations
This theorem does not classify the tower height at every factorial or lcm index after its first appearance, nor the pattern of later returns to a level. The first-hit values \(E_k\) for arbitrary integers were already known; the claim of new scope is confined to the factorial/lcm first hits and exact lcm record plateau-and-drop behavior. The literature comparison cannot exclude an unindexed equivalent treatment.

## References
1. J.-M. De Koninck and W. Verreault, *On the tower factorization of integers*, arXiv:2308.09149v1 (first public 2023-08-17), https://arxiv.org/abs/2308.09149; *American Mathematical Monthly* 131 (2024), 511–518, https://doi.org/10.1080/00029890.2024.2322912. Author-hosted full text: https://www.jeanmariedekoninck.mat.ulaval.ca/fileadmin/Documents/Publications/2023_on_the_tower_factorization_of_integers.pdf.
2. J.-M. De Koninck and W. Verreault, *Arithmetic functions at factorial arguments*, arXiv:2308.09761v1 (2023-08-18), https://arxiv.org/abs/2308.09761.
3. OEIS A288636, *Height of power-tower factorization of n*, https://oeis.org/A288636 (a different gcd-based height convention).
