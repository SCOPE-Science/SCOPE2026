# Exact prime-power injectivity thresholds for the quadratic discriminator sequence

## Finding
For the quadratic sequence \(t_j=2j(j-1)\) introduced in a least-discriminating-modulus problem, define \(J(p,a)\) to be the first index \(j\ge2\) at which \(t_j\) repeats an earlier residue modulo \(p^a\), where \(p\) is prime and \(a\ge1\). Then
\[
J(p,a)=\begin{cases}
2,&p=2,\ a=1,\\
2^{a-2}+1,&p=2,\ a\ge2,\\
(3p^{a/2}+1)/2,&p\text{ odd},\ a\text{ even},\\
((p+2)p^{(a-1)/2}+1)/2,&p\text{ odd},\ a\text{ odd}.
\end{cases}
\]
In every case exactly one earlier index collides at this first failure. It is respectively
\[
i=\begin{cases}
1,&p=2,\ a=1,\\
2^{a-2},&p=2,\ a\ge2,\\
(p^{a/2}+1)/2,&p\text{ odd},\ a\text{ even},\\
((p-2)p^{(a-1)/2}+1)/2,&p\text{ odd},\ a\text{ odd}.
\end{cases}\]
Equivalently, the longest collision-free initial segment has exactly \(J(p,a)-1\) elements. The odd-prime formulas exhibit a sharp parity-of-exponent transition on the scale of the square root of the modulus.

## Assumptions and scope
All indices are positive integers. A repeated value is a congruence of sequence values, not a literal equality in the integers. The modulus is an **arbitrary prime power**, including powers of two. The index \(j\) is minimized over all later indices; the preceding index \(i\) is then asserted unique. Nothing is assumed about primitive roots, squarefreeness, or a bound on \(p\) or \(a\).

## Proof
For \(1\le i<j\), set \(d=j-i\) and \(s=i+j-1\). Then \(d\ge1\), \(s\ge d+1\), \(d+s=2j-1\) is odd, and
\[
t_j-t_i=2(j-i)(i+j-1)=2ds.\]
Conversely, any positive integers \(d,s\) of opposite parity with \(s>d\) yield the unique pair \(i=(s-d+1)/2\ge1\), \(j=(s+d+1)/2\). Thus minimizing \(j\) is equivalent to minimizing the odd sum \(d+s\) under prime-power divisibility of \(2ds\).

**Odd primes.** Let \(p\ge3\), and write \(u=\nu_p(d)\) and \(v=\nu_p(s)\), where \(\nu_p\) denotes prime-adic valuation. Divisibility requires \(u+v\ge a\). Put \(m=\min(u,v)\) and \(M=\max(u,v)\). Because \(d,s\) have opposite parity and all powers of an odd prime are odd,
\[
d+s\ge 2p^m+p^M\ge2p^m+p^{a-m} \quad\text{when }m\le\lfloor a/2\rfloor.\]
For \(m\ge\lceil a/2\rceil\), simply \(d+s\ge3p^m\ge3p^{\lceil a/2\rceil}\). Set \(F_a(m)=2p^m+p^{a-m}\). For integer \(m<\lfloor a/2\rfloor\),
\[
F_a(m)-F_a(m+1)=(p-1)(p^{a-m-1}-2p^m)>0;
\]
the final inequality holds since \(p\ge3\) and \(a-m-1\ge m+1\). If \(a=2k\), the minimum is therefore \(3p^k\); the \(m>k\) case is strictly larger. Equality forces \(\{d,s\}=\{p^k,2p^k\}\), hence \(d=p^k\), \(s=2p^k\), and \(i=(p^k+1)/2\), \(j=(3p^k+1)/2\). This is a genuine collision because \(p^{2k}\mid ds\), and the equality conditions make it unique.

If \(a=2k+1\), the minimum is \(F_a(k)=(p+2)p^k\). All \(m<k\) give a strictly greater value, while \(m\ge k+1\) gives at least \(3p^{k+1}>(p+2)p^k\). Equality forces \(\{d,s\}=\{2p^k,p^{k+1}\}\); since \(p\ge3\), necessarily \(d=2p^k\), \(s=p^{k+1}\). Therefore \(i=((p-2)p^k+1)/2\) and \(j=((p+2)p^k+1)/2\), again uniquely. This construction has \(p^{2k+1}\mid ds\), so the bound is attained.

**The prime two.** When \(a=1\), all \(t_j\) are even, and the first collision is \((i,j)=(1,2)\). When \(a\ge2\), the condition is \(2^{a-1}\mid ds\). Since \(d,s\) are of opposite parity, their even member is divisible by \(2^{a-1}\). If \(s\) is even, then \(d+s\ge2^{a-1}+1\), with equality uniquely at \(d=1\), \(s=2^{a-1}\). If \(d\) is even, then \(d\ge2^{a-1}\) and \(s\ge d+1\), yielding \(d+s\ge2^a+1\), strictly larger. The unique minimum is thus \(i=2^{a-2}\), \(j=2^{a-2}+1\).

In every case we have minimized the later collision index among *all* pairs, not just exhibited a pair, and the equality cases give the stated uniqueness. \(\square\)

## Verification
The accompanying dependency-free `verify.py` enumerates the residues directly, checks that every earlier index is collision-free, verifies the first colliding predecessor, and separately tests all preceding indices by integer divisibility at the predicted boundary. For the 94 tested prime powers with \(p<50\), \(1\le a\le10\), and predicted threshold at most \(15{,}000\), it reports

`VERIFY_OK prime_powers=94 residues_checked=108348 unique_first_pairs=94`

This is an independent finite check of the formulas, not an infinite proof. The preceding parity-and-valuation argument establishes the unrestricted assertion.

## Relationship to prior work
Sun introduced the sequence \(2j(j-1)\) in his least-modulus discriminator theorem. The theorem identifies the **least modulus** for which an initial segment is injective, whereas the present result fixes each prime power and determines the **maximal injective prefix length**, as well as the unique first colliding pair. A least-modulus result does not determine individual prime-power horizons; for exponent one our bound is compatible with the original prime-modulus argument.

Park studies related but different quadratic discriminators, including sequences depending on the prime-power coefficient. Sun's subsequent paper treats a broader family of polynomial sequences and least discriminating moduli, rather than this fixed-sequence first-collision classification. Existing sources are closely related, so unnoticed equivalent general coverage remains a literature risk.

## Limitations
The finding is about a specific quadratic sequence at prime-power moduli, not a formula for all composite moduli or arbitrary quadratic polynomials. It gives the first repetition and not the complete later collision distribution. Full originality is not an independently audited determination; the claim is supported by the inspected source results and the recorded searches.

## References
1. Z.-W. Sun, *On functions taking only prime values*, arXiv:1202.6589, initial preprint 2012-02-29, https://arxiv.org/abs/1202.6589.
2. S. Park, *Discriminators of quadratic polynomials*, arXiv:1308.3754, initial preprint 2013-08-17, https://arxiv.org/abs/1308.3754.
3. Z.-W. Sun, *The least modulus for which consecutive polynomial values are distinct*, arXiv:1304.5988, initial preprint 2013-04-22, https://arxiv.org/abs/1304.5988.
