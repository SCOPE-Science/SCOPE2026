# Thirteen consecutive nonprimitive nonsquares at asymptotically maximal primitive density

## Finding
For every integer \(m\ge3\) that is odd, the thirteen consecutive elements
\[
46256,46257,\ldots,46268
\]
of the prime subfield of \(\mathbb F_{65537^m}\) are simultaneously quadratic nonsquares and nonprimitive multiplicative elements. Write \(\theta_q=\varphi(q-1)/(q-1)\). Along odd prime extension degrees \(\ell\),
\[
0<\frac12-\theta_{65537^\ell}\le\frac{\ell\log 65537}{2(\ell+1)\log(\ell+1)}\longrightarrow0.
\]
Therefore for each \(3\le k\le13\), the supremum of the primitive-element density \(\theta_q\), among odd finite fields containing \(k\) consecutive non-square nonprimitive (NSNP) elements, is precisely \(1/2\), but is never attained. In particular NSNP elements can have asymptotically vanishing ambient density and still contain a fixed block of thirteen consecutive field elements.

## Assumptions and scope
The field \(\mathbb F_q\) has odd prime-power order. An element is *primitive* if it generates \(\mathbb F_q^\times\); it is *non-square* if it is not the square of any field element; NSNP means simultaneously non-square and nonprimitive. Consecutive means the additive translate set \(\{a,a+1,\ldots,a+k-1\}\), with the integer constants interpreted in the prime subfield; the explicitly constructed thirteen elements are distinct since the characteristic is \(65537>13\). The variable \(m\) ranges over all odd integers at least three for the block statement, and \(\ell\) ranges over odd rational primes for the limiting-density statement. The supremum ranges over all odd prime powers, with no bound on their characteristic or extension degree.

## Proof
**Finite base-field certificate.** The number \(p=65537=2^{16}+1\) is prime. For \(a\) in the indicated consecutive interval, exact modular exponentiation gives
\[
(a^{16384}\bmod 65537)_{a=46256}^{46268}=
(256,256,256,256,65281,256,256,256,256,256,65281,65281,256).
\]
Because \(256^2\equiv65281^2\equiv-1\pmod{65537}\), each \(a^{32768}\equiv-1\pmod{65537}\). As the order of \(\mathbb F_p^\times\) is \(65536=2^{16}\), every one of these thirteen residues has multiplicative order exactly \(65536\). The attached standalone integer-arithmetic checker reproduces every modular exponent, and the displayed thirteen-integer certificate is sufficient to check the finite step by repeated squaring.

**Odd-degree lifting.** Fix odd \(m\ge3\), set \(q=p^m\), and let \(M_m=(p^m-1)/(p-1)=\sum_{j=0}^{m-1}p^j\). Since \(p\) and \(m\) are odd, \(M_m\) is odd. Each residue \(a\) in the block belongs to the canonical prime subfield and has order exactly \(p-1<q-1\), so it is not primitive in \(\mathbb F_q^\times\). Moreover
\[
a^{(q-1)/2}=(a^{(p-1)/2})^{M_m}=(-1)^{M_m}=-1,
\]
which is the quadratic nonsquare criterion over odd finite fields. Thus the entire interval consists of NSNP elements for all odd \(m\ge3\).

**Primitive density along prime degrees.** Now let \(m=\ell\) be an odd rational prime. Because \(p-1=2^{16}\) and \(M_\ell\) is odd, every prime divisor \(r\mid M_\ell\) is odd and does not divide \(p-1\). From \(p^\ell\equiv1\pmod r\) and the primality of \(\ell\), the multiplicative order \(\operatorname{ord}_r(p)\) is either \(1\) or \(\ell\). The former would imply \(r\mid p-1\), impossible. Hence \(\operatorname{ord}_r(p)=\ell\) and \(r\equiv1\pmod\ell\), in particular \(r\ge\ell+1\). Set \(s=\omega(M_\ell)\). As the \(s\) distinct prime divisors have product at least \((\ell+1)^s\) and at most \(M_\ell<p^\ell\),
\[
s<\frac{\ell\log p}{\log(\ell+1)}.
\]
Euler's product formula and \(q-1=2^{16}M_\ell\) give
\[
\theta_q=\frac12\prod_{r\mid M_\ell}\left(1-\frac1r\right).
\]
The elementary inequality \(1-\prod_j(1-u_j)\le\sum_j u_j\) for \(u_j\in[0,1]\) implies
\[
0<\frac12-\theta_q\le\frac12\sum_{r\mid M_\ell}\frac1r
\le\frac{s}{2(\ell+1)}
<\frac{\ell\log p}{2(\ell+1)\log(\ell+1)}\to0.
\]
There are infinitely many odd primes \(\ell\), hence infinitely many such field sizes.

**Sharp supremum.** In every odd finite field, all primitive elements are nonsquares, since the multiplicative group is cyclic of even order. Therefore \(\theta_q\le1/2\). Equality means all nonsquares are primitive, so there are no NSNP elements at all; thus a field containing even one NSNP element must satisfy \(\theta_q<1/2\). The fixed thirteen-term block exists for all odd prime-degree fields constructed above, with \(\theta_q\to1/2\). Every initial subblock of length \(k\) for \(3\le k\le13\) gives the claimed supremum, and nonattainment follows.

## Verification
Run `python3 verify.py` from the extracted package. It checks primality of the Fermat base using exact trial division, re-evaluates the thirteen certified modular powers with an independent repeated-squaring implementation, verifies the congruence signs and orders, checks nonsquareness in sample odd extension degrees by the prime-subfield exponent criterion, and confirms the elementary inequality for several small prime degrees with exact rational arithmetic. The convergence argument and all-field statements follow from the proof, not from finite sampling.

## Relationship to prior work
Zhou and Wu, *Consecutive non-square non-primitive tuples in finite fields*, arXiv:2607.17267v2 (original submission 2026-07-19), prove optimal **sufficient lower-density thresholds** \(\theta_q<4/15\) for universal existence of triples and \(\theta_q<8/35\) for universal existence of four-tuples, with boundary exceptions. They also establish character-sum existence criteria for non-square odd-prime-power sets. The present theorem instead constructs explicit **high-density families** \(\theta_q\to1/2\) containing thirteen NSNP elements in one interval. Neither kind of sufficient criterion entails this sharp supremum; conversely this example does not improve their universal sufficient thresholds.

Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429v1, establishes pair-existence thresholds and studies small extension fields. The present length-thirteen and density-boundary result is not implied by a pair-existence theorem. Prior work on consecutive primitive elements in prime fields is compatible with the finite modular certificate, but does not itself establish the persistent **nonprimitive** property after odd-degree extension coupled with primitive-density convergence.

## Limitations
The result concerns existence of one explicit thirteen-term block, not the total number of such blocks, nor maximum possible NSNP block length. The density estimate is established along odd **prime** extension degrees (not all odd degrees), while the block survives every odd extension degree at least three. No assertion is made that thirteen is maximal, nor that the analytic upper-bound rate is optimal. A previous implicit use of prime-subfield lifting remains a literature-overlap risk; the finite thirteen-term certificate is reproducible but not a claim of a novel algorithm.

## References
1. J. Zhou and H. Wu, *Consecutive non-square non-primitive tuples in finite fields*, arXiv:2607.17267v2 (2026), initial submission 2026-07-19. https://arxiv.org/abs/2607.17267
2. S. D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429v1 (2026), first submitted 2026-04-23. https://arxiv.org/abs/2604.21429
3. S. D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737 (2024), on consecutive-square statistics without nonprimitivity restrictions. https://arxiv.org/abs/2402.10737
