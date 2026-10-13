# Sharp reduced-residue threshold for squarefree practical numbers

## Finding

An integer \(n\ge1\) is *practical* if every integer \(t\) with \(1\le t\le n\) is a sum of distinct positive divisors of \(n\). It is *squarefree* when no prime square divides it. Let \(\omega(m)\) denote the number of distinct prime factors of \(m\), with \(\omega(1)=0\).

**Theorem.** If \(m\ge1\), \(\gcd(m,6)=1\), and \(\omega(m)\le3\), then for every residue \(b\pmod m\) satisfying \(\gcd(b,m)=1\), infinitely many squarefree practical integers \(n\) satisfy \(n\equiv b\pmod m\). In particular, this holds for every \(1\le m<5005\) coprime to \(6\). At \(m=5005=5\cdot7\cdot11\cdot13\), precisely the three integers \(1,2,6\) are both squarefree practical and coprime to \(5005\). Thus \(5005\) is the first modulus coprime to \(6\) at which the all-reduced-classes infinitude statement fails.

## Assumptions and scope

All moduli and integers are positive, except that an arbitrary residue representative \(b\) may be any integer. The term *reduced residue* means \(\gcd(b,m)=1\). No uniform asymptotic estimate as \(m\) varies is asserted. The proof uses the standard Stewart–Sierpiński practical-number criterion, Bertrand's postulate, and the prime number theorem in arithmetic progressions for each fixed modulus.

For a squarefree integer \(N=\prod_{i=1}^r p_i\) with strictly increasing primes, the Stewart–Sierpiński criterion reads: \(N=1\) or \(p_1=2\) and \(p_i\le1+\sigma(\prod_{h<i}p_h)\) for each \(i\ge2\). Here \(\sigma\) is the ordinary sum-of-divisors function. This standard characterization is stated in the cited 2022 paper.

## Proof

**1. A practical, squarefree, modulus-coprime backbone.** Fix \(m\) with \(\gcd(m,6)=1\) and \(\omega(m)\le3\). Enumerate all primes not dividing \(m\), starting at \(3\), as \(3=q_1<q_2<q_3<\cdots\). Define \(A_j=2\prod_{i=1}^j q_i\) for \(j\ge1\). Thus \(A_1=6\), and every \(A_j\) is squarefree and coprime to \(m\).

The integer \(6\) is practical since \(3\le\sigma(2)+1=4\). At most three of \(5,7,11,13\) divide \(m\), so \(q_2\le13=\sigma(6)+1\). At most three of \(5,7,11,13,17\) divide \(m\), so \(q_3\le17\le\sigma(6q_2)+1\), since \(\sigma(6q_2)=12(q_2+1)\ge72\).

For \(j\ge3\), let \(r_1<r_2<r_3<r_4\) be the first four primes exceeding \(q_j\). Four applications of Bertrand's postulate give \(r_4<16q_j\). Since at most three of these four primes divide \(m\), the next admissible prime satisfies \(q_{j+1}\le r_4<16q_j\). However, \(A_j=6q_2\cdots q_j\ge30q_j\). Therefore \(q_{j+1}<A_j\le\sigma(A_j)+1\). Applying the practical-number criterion inductively shows that every \(A_j\) is practical. The strictly increasing sequence \((A_j)\) is unbounded.

**2. Targeting every reduced residue.** Fix \(b\) with \(\gcd(b,m)=1\), and put \(X_j=\sigma(A_j)+1\). For each \(j\), the residue \(c_j\equiv bA_j^{-1}\pmod m\) is a unit modulo \(m\). The prime number theorem in arithmetic progressions, applied to the fixed modulus \(m\) and uniformly over its finitely many unit classes, guarantees that for all sufficiently large \(j\), some prime \(r_j\equiv c_j\pmod m\) lies in \((X_j/2,X_j]\). For \(j\ge3\), we have \(X_j\ge A_j\ge30q_j\), hence \(r_j>X_j/2\ge15q_j>q_j\). Thus \(r_j\) is a new prime and \(\gcd(r_j,m)=1\). Since \(r_j\le X_j=\sigma(A_j)+1\), the squarefree integer \(A_jr_j\) is practical by the same criterion. Finally, \(A_jr_j\equiv b\pmod m\), and the integers \(A_jr_j\) tend to infinity. This proves the claimed infinitude (also for \(m=1\), using the ordinary prime number theorem).

**3. The first obstruction and its minimality.** If \(N>2\) is squarefree and practical, its two smallest prime factors are necessarily \(2,3\), by the criterion: after \(2\), the next prime must be at most \(\sigma(2)+1=4\). If \(N>6\), its third prime must be at most \(\sigma(6)+1=13\), hence belongs to \(\{5,7,11,13\}\). Therefore no squarefree practical integer greater than \(6\) is coprime to \(5005\). Conversely \(1,2,6\) are squarefree practical and coprime to \(5005\), giving the exact set.

Every positive integer \(m<5005\) coprime to \(6\) has at most three distinct prime divisors, because the least possible product of four distinct primes exceeding \(3\) is \(5\cdot7\cdot11\cdot13=5005\). Part 2 applies to every such \(m\), whereas part 3 shows failure at \(5005\). Hence the threshold is sharp. \(\square\)

## Verification

The standalone checker in `squarefree_practical_verify.py` implements the squarefree Stewart–Sierpiński inequalities and verifies ten greedy backbone extensions for every \(1\le m<5005\) coprime to \(6\) (\(16680\) extensions), directly tests the complete coprime list below \(100000\) for modulus \(5005\), and constructs explicit reduced-class witnesses for moduli \(5,7,11,13,35,77,385\). All those finite checks passed. They are not used as substitutes for the unrestricted proof, and do not verify the prime number theorem.

To reproduce: run `python squarefree_practical_verify.py` with Python 3; no third-party dependencies are required.

## Relationship to prior work

Somu, Li and Kukla (2022), arXiv:2212.03673, Theorem 2.2, classify infinitude for **ordinary practical numbers** in linear progressions, with no squarefreeness condition. Their criterion gives infinitely many ordinary practical integers in reduced classes modulo \(5005\), whereas the present theorem proves that only \(1,2,6\) can be squarefree and coprime to that modulus. Thus their result does not imply the squarefree conclusion. Weingartner (2020/2021), arXiv:2011.06627, Theorem 1 and Corollary 3, give distribution statements for prime-factor-constrained sequences, notably all practical numbers; the full text does not state the squarefree-practical reduced-residue cutoff. OEIS A265501 tabulates squarefree practical numbers and discusses their global count, rather than this modulus obstruction.

## Limitations

The conclusion for moduli with more than three distinct prime factors is not classified: some such moduli also admit infinite reduced-class squarefree practical sequences, whereas \(5005\) is an obstruction. No quantitative lower bound for the number of squarefree practical integers up to \(X\) in each residue class is proved. An equivalent theorem in literature not identified by the checked searches remains possible; the result has not undergone independent mathematical audit.

## References

1. S. T. Somu, T. H. S. Li, A. Kukla, *On Some Results on Practical Numbers*, arXiv:2212.03673v1 (first public version 7 December 2022), especially §1 and Theorem 2.2. https://arxiv.org/pdf/2212.03673
2. A. Weingartner, *An Extension of the Siegel–Walfisz Theorem*, arXiv:2011.06627v2 (2021), especially Theorem 1 and Corollary 3. https://arxiv.org/pdf/2011.06627
3. OEIS A265501, *Practical numbers that are squarefree*. https://oeis.org/A265501
4. Classical Stewart–Sierpiński characterization of practical integers; standard Bertrand postulate and prime number theorem in arithmetic progressions.
