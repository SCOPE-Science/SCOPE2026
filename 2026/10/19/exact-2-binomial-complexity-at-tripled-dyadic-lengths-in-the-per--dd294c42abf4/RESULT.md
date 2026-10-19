# Exact 2-binomial complexity at tripled dyadic lengths in the period-doubling word

## Finding
For the period-doubling fixed point \(\mathbf p\), the complete 2-binomial class profile at every length three times a power of two admits a closed form. For every integer \(k\ge0\), setting \(x=2^k\), one has
\[
\boxed{b_{\mathbf p}^{(2)}(3x)=2x+k+3.}
\]
The only possible one-counts are \(x-1\), \(x\), and \(x+1\); their class counts are \(x\), \(k+3\), and \(x\), respectively. At the central one-count \(x\), the exact set of weighted one-position sums is
\[
\left\{\frac{x(3x-k-3)}2+jx:0\le j\le k+2\right\}.
\]
These lengths are not powers of two. The first values are \(5,8,13,22,39,72,137,266\) for \(k=0,1,\ldots,7\).

## Assumptions and scope
Let \(\sigma\) be the binary length-two substitution \(\sigma(0)=01\) and \(\sigma(1)=00\), and let \(\mathbf p=\lim_{r\to\infty}\sigma^r(0)=0100010101000100\cdots\). A factor is a contiguous finite subword, while a scattered subsequence can use any strictly increasing set of positions. For a finite binary word \(u\) and a binary word \(v\), write \(\binom uv\) for the number of occurrences of \(v\) as a scattered subsequence of \(u\). Words of equal length are 2-binomially equivalent when all these counts agree for \(|v|\le2\). The quantity \(b_{\mathbf p}^{(2)}(n)\) counts the corresponding classes of length-\(n\) factors, not the number of distinct factors.

For a length-\(m\) word \(u=u_0u_1\cdots u_{m-1}\), define \(t(u)=\sum_{i=0}^{m-1}u_i\) and \(J(u)=\sum_{i=0}^{m-1}i u_i\). Positions are indexed from zero. The statement ranges over every integer \(k\ge0\), with no bound on \(k\). It does not concern 2-abelian equivalence, which counts contiguous pairs.

## Proof
**Step 1: the exact binary 2-binomial signature.** For fixed length \(m\), the counts of individual digits depend only on \(t=t(u)\); counts of scattered \(00\) and \(11\) are \(\binom{m-t}{2}\) and \(\binom t2\). Since \(\binom u{01}=\sum_{i:u_i=1}(i-\text{number of earlier ones})=J(u)-\binom t2\), and \(\binom u{10}=t(m-t)-\binom u{01}\), every scattered subsequence count of length at most two is determined by \((t,J)\), and conversely these counts recover \((t,J)\). Thus 2-binomial classes of length-\(m\) factors are exactly their distinct pairs \((t,J)\).

**Step 2: all even-length factors split into two exact branches.** The fixed-point identities are \(p_{2s}=0\) and \(p_{2s+1}=1-p_s\) for every \(s\ge0\). For every length-\(m\) factor \(u\) define two length-\(2m\) words
\[
E(u)=0(1-u_0)0(1-u_1)\cdots0(1-u_{m-1}),\qquad
O(u)=(1-u_0)0(1-u_1)0\cdots(1-u_{m-1})0.
\]
Every length-\(2m\) factor begins at an even or odd index, so is respectively \(E(u)\) or \(O(u)\) for a length-\(m\) factor \(u\). Conversely, every such \(E(u)\) and \(O(u)\) occurs at the corresponding starting index of the occurrence of \(u\). Hence their union is the *whole* factor set, without any missing boundary cases.

For \(t=t(u)\) and \(J=J(u)\), both images have \(T=m-t\) ones, and direct summation of the even and odd positions gives
\[
J(E(u))=m^2-2J-t,\qquad J(O(u))=m(m-1)-2J,
\]
so \(J(E(u))-J(O(u))=T\). Both affine maps of \(J\) are injective when \(t\) is fixed.

**Step 3: induction on the tripled dyadic scale.** Write \(x=2^k\), so \(m=3x\). The induction assertion is that the possible values of \(t\) are \(x-1,x,x+1\), the corresponding numbers of distinct \(J\) are \(x,k+3,x\), and the middle set is precisely the progression
\[
\left\{A_k+jx:0\le j\le k+2\right\},\qquad A_k=\frac{x(3x-k-3)}2.
\]
For \(k=0\), the length-three factor set is \(\{000,001,010,100,101\}\). Its \((t,J)\) pairs are \((0,0),(1,2),(1,1),(1,0),(2,2)\), as required, with \(A_0=0\).

Suppose the assertion holds at \(m=3x\). At length \(2m=3(2x)\), the three old weights \(x-1,x,x+1\) become the three new weights \(2x+1,2x,2x-1\), in reverse order. For either outer old weight, the new weight \(T\) is odd. The even-start branch has \(J(E)\) of opposite parity to the odd-start branch \(J(O)\), since their difference is the odd number \(T\). Consequently the two injective branches are disjoint and each contributes all \(x\) old profiles: each new outer weight has exactly \(2x\) profiles.

For the central old weight \(t=x\), the new weight is \(T=2x\). The old central \(J\)-set is an arithmetic progression of \(k+3\) terms with spacing \(x\). The two affine image sets are therefore each arithmetic progressions of \(k+3\) terms with spacing \(2x\), and one is shifted from the other by exactly \(T=2x\). Their union is one consecutive arithmetic progression of exactly \(k+4\) terms and spacing \(2x\). Its minimum is the odd-start image of the previous maximum:
\[
A_{k+1}=m(m-1)-2\bigl(A_k+(k+2)x\bigr)
= x(6x-k-4)
=\frac{(2x)(3(2x)-(k+1)-3)}{2}.
\]
This is exactly the asserted central progression with \(k\) replaced by \(k+1\). The induction is complete. Adding the three disjoint weight-group counts gives \(x+(k+3)+x=2x+k+3\) for every \(k\ge0\). \(\square\)

## Verification
The accompanying standalone Python 3 program `verify_period_doubling.py` can be executed with `python3 verify_period_doubling.py 13`. It verifies all profile counts, three weight groups, central arithmetic progressions, and formula values for \(0\le k\le13\), i.e. up to length \(24{,}576\), and ends with `VERIFY_OK`.

The enumerator is exhaustive for each tested factor length: for \(n=3\cdot2^k\) it uses \(r=k+2\), so the length of each \(\sigma^r\)-letter block is \(L=2^r>n\). Every length-\(n\) factor lies within the images of two consecutive letters; the actual adjacent-letter pairs of \(\mathbf p\) are exactly \(00,01,10\). The verifier enumerates the profiles of every length-\(n\) window in \(\sigma^r(00)\), \(\sigma^r(01)\), and \(\sigma^r(10)\). For \(k\le10\) it separately constructs the sequence by the binary valuation formula \(p_i=\nu_2(i+1)\bmod2\) and verifies complete agreement. These finite tests corroborate the proof but are not used to infer the universal quantifier.

## Relationship to prior work
Rigo and Salimov introduced and studied binomial complexity, including exact calculations for Sturmian and Thue–Morse words [1]. Lejeune's doctoral thesis [2, §4.5, pp. 115–117] treats the same period-doubling word and its 2-binomial complexity, providing a computer graph through length \(70\) and a qualitative proposition contrasting powers of two and other lengths; it explicitly notes the lack of a precise full computation. The present theorem determines an infinite **non-power-of-two** family, with the complete three-weight profile and central weighted-position progression, so that qualitative proposition does not imply it. Rigo, Stipulanti, and Whiteland [3, §7.1] study related binomial-complexity comparisons, without the stated tripled-dyadic formula in the inspected text. A numerical coincidence with integer sequence A052968 [4] is not the same combinatorial identification or proof. These comparisons do not establish absolute priority over all unindexed prior work.

## Limitations
The conclusion applies to the single family \(n=3\cdot2^k\). It neither gives a formula for general factor lengths nor establishes global regularity or nonregularity of the complete complexity function. The computational checks end at \(k=13\), while the theorem for all \(k\ge0\) follows from the explicitly stated induction. Earlier equivalent unpublished or unindexed work cannot be excluded. There has been no independent audit of this result.

## References
[1] M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, 2013. https://orbi.uliege.be/handle/2268/149313 (repository first available 27 May 2013).

[2] M. Lejeune, *On the k-binomial equivalence of finite words and k-binomial complexity of infinite words*, doctoral thesis, 2021, §4.5, pp. 115–117. https://orbi.uliege.be/bitstream/2268/259266/1/PhDThesis_LejeuneMarie.pdf

[3] M. Rigo, M. Stipulanti and M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603v2, §7.1, 2022. https://arxiv.org/html/2201.04603v2

[4] OEIS Foundation, entry A052968, numerical sequence and references. https://oeis.org/A052968
