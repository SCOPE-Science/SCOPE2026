# Exact binomial-square phase transport under iterated Thue–Morse substitution

## Finding
Let \(\mu(0)=01\) and \(\mu(1)=10\). Fix any integer \(r\ge1\), any infinite binary source word \(\mathbf x=x_0x_1\cdots\), and its substituted word \(\mathbf y=\mu^r(\mathbf x)\). Let \(M\ge1\) be **any** integer. For \(s\ge0\) write \(s=q2^r+d\), with \(0\le d<2^r\), and let \(U=\mathbf y[s,s+M2^r)\), \(V=\mathbf y[s+M2^r,s+2M2^r)\). Then these adjacent windows are \(r\)-binomially equivalent exactly in the following cases:
\[
\boxed{U\sim_r V\quad\Longleftrightarrow\quad d=0\ \text{or}\ x_q=x_{q+M}=x_{q+2M}.}
\]
This is a uniform exact criterion for every substituted binary word, every substitution depth and every integer block multiplier. It says that all aligned windows are equivalent, whereas all nonaligned occurrences are controlled solely by three source letters, not the intervening word.

As a consequence, take \(\mathbf x=\mathbf t\), the binary Thue–Morse fixed point \(t_n=s_2(n)\bmod2\). For dyadic multipliers \(M=2^h\), no three corresponding source letters agree, giving the sharp position law: for all \(k\ge r\ge1\), adjacent length-\(2^k\) Thue–Morse factors are \(r\)-binomially equivalent exactly at indices divisible by \(2^r\), with density \(2^{-r}\).

## Assumptions and scope
All indices are zero-based. A scattered occurrence of \(a_1\cdots a_h\) in a finite word is an increasing choice of \(h\) positions carrying those letters. The relation \(\sim_r\) compares their multiplicities for every binary pattern of length at most \(r\). The first statement holds for **every** one-sided infinite binary source word, for each \(r\ge1\), every \(M\ge1\) and every \(s\ge0\), over ordinary integer counts. Its conclusion is independent of whether the source itself is automatic, aperiodic, or uniformly recurrent. The final Thue–Morse corollary is limited to dyadic multipliers.

## Proof
**1. Encoding scattered-subsequence counts.** Work in the finite-dimensional, associative, noncommutative algebra \(\mathcal A_r=\mathbb Q\langle X_0,X_1\rangle/(\text{monomials of degree }>r)\). For a binary word \(w\), set \(F(w)=\prod_{a\in w}(1+X_a)\), in word order. The coefficient of a monomial of degree \(h\le r\) is precisely the number of scattered copies of the corresponding binary word. Thus \(u\sim_r v\) if and only if \(F(u)=F(v)\) in \(\mathcal A_r\). Every \(F(w)\) has constant term one and is invertible.

**2. Distinguishing substituted letters.** Let \(\mu(0)=01\), \(\mu(1)=10\), and write \(A_j=\mu^j(0)\), \(B_j=\mu^j(1)\). In the unrestricted graded free algebra put \(\Delta_j=F(A_j)-F(B_j)\). Its first nonzero homogeneous component has degree exactly \(j+1\), for every \(j\ge0\). Indeed, \(\Delta_0=X_0-X_1\) and \(\Delta_1=X_0X_1-X_1X_0\). For \(j\ge1\), substitution gives \(F(A_{j+1})=F(A_j)F(B_j)\) and \(F(B_{j+1})=F(B_j)F(A_j)\); hence \(\Delta_{j+1}=\Delta_jF(B_j)-F(B_j)\Delta_j\). Since the degree-one part of \(F(B_j)\) is \(2^{j-1}(X_0+X_1)\), the leading term iterates the commutator with \(X_0+X_1\), times a nonzero scalar. Repeated commutation of \([X_0,X_1]\) with \(X_0+X_1\) is nonzero: the coefficient of \(X_0X_1^{j}\) in the leading term is nonzero (one may take the term with all added \(X_1\) on its right). Thus \(F(A_j)=F(B_j)\) modulo degrees greater than \(j\), but these expressions differ in degree \(j+1\).

A consequence used below is: if \(u,v\) are two source words of equal length with different numbers of zeros, then \(\mu^j(u)\not\sim_{j+1}\mu^j(v)\). At degree \(j+1\) the profile difference is precisely the difference in zero counts times the nonzero leading part of \(\Delta_j\), since all individual source blocks have the same lower-degree components.

**3. Separation of all proper prefixes.** Set \(L=2^r\) and, for \(0<d<L\), set \(H_a=F(\operatorname{prefix}_d\mu^r(a))\), \(a\in\{0,1\}\), in \(\mathcal A_r\). Then \(H_0\ne H_1\). To see this, write \(d=2^v e\), with \(e\) odd and \(0\le v<r\). Each prefix is the image under \(\mu^v\) of the first \(e\) letters of \(\mu^{r-v}(a)\). Those two source prefixes are complements and have different zero counts: each full length-two substituted pair contains one zero and one one, while the remaining last letters are complementary. By step 2 their \(\mu^v\)-images differ in degree \(v+1\le r\).

**4. Rigidity of adjacent misaligned blocks.** Denote the common \(r\)-profile of \(\mu^r(0)\) and \(\mu^r(1)\) by \(Q\). For a source-letter \(a\), the profile of the complementary suffix of \(\mu^r(a)\) is \(H_a^{-1}Q\). Suppose \(M\ge1\), and consider two consecutive factors of length \(ML\), each beginning at offset \(d\) from the \(L\)-block boundary. With the source letters at their three successive boundary blocks denoted \(a,b,c\), the two profiles are
\[
H_a^{-1}Q^MH_b\quad\text{and}\quad H_b^{-1}Q^MH_c.
\]
Put \(E=H_0^{-1}H_1\ne1\) and \(T=H_0^{-1}Q^MH_0\). Since \(H_a=H_0E^a\) for \(a\in\{0,1\}\), equality is equivalent to
\[
TE^{b-c}T^{-1}=E^{a-b}.
\]
If exactly one of the two exponents is zero, equality is impossible. If both are nonzero, the binary letters necessarily have \(a=c\ne b\), so the equation requires \(TET^{-1}=E^{-1}\) (or its equivalent inverse). This too is impossible. Indeed, let \(h\) be the smallest positive degree of \(E-1\); conjugation by a series with constant term one preserves its homogeneous degree-\(h\) component, whereas inversion negates that nonzero component in characteristic zero. Therefore the two adjacent profiles are equal **if and only if** \(a=b=c\).

**5. Specialization to a dyadic Thue–Morse source spacing.** For all \(q\ge0\) and \(h\ge0\), the three values \(t_q,t_{q+2^h},t_{q+2^{h+1}}\) are not identical. Write \(q=u+2^h v\), with \(0\le u<2^h\). Their values are respectively \(t_u\oplus t_v\), \(t_u\oplus t_{v+1}\), \(t_u\oplus t_{v+2}\). Three consecutive letters in the Thue–Morse word cannot all be equal, because each adjacent aligned pair \(t_{2j},t_{2j+1}\) is complementary.

**6. Conclusion.** Write \(s=Lq+d\), \(0\le d<L\), where \(L=2^r\). If \(d=0\), each length-\(ML\) window consists of \(M\) complete substituted blocks, hence both have profile \(Q^M\), independently of the source. If \(0<d<L\), step 4 proves equality precisely if the three boundary source letters \(x_q,x_{q+M},x_{q+2M}\) all agree. This establishes the main theorem for arbitrary \(\mathbf x\) and arbitrary \(M\). Applying step 5 to \(\mathbf x=\mathbf t\) with \(M=2^{k-r}\) yields the stated dyadic Thue–Morse corollary.

## Verification
The accompanying standalone `checker.py` tests the **general arbitrary-source transport identity** on a deterministic exhaustive suite of finite source patterns (all binary words through length seven, where enough boundary symbols exist), all orders \(1\le r\le4\), multipliers \(1\le M\le3\), and every possible offset in the constructed image. The checker also tests the dyadic Thue–Morse corollary at all starts \(0\le s<256\), orders \(1\le r\le5\), and exponents \(r\le k\le8\), and independently cross-checks small exact subsequence profiles by direct position combinations. Finite tests corroborate, not replace, the proof. Execute `python3 checker.py` with Python 3 and no third-party dependencies.

## Relationship to prior work
Rao, Rigo and Salimov (2015) study avoidance of binary 2-binomial powers and provide the archival motivation, rather than an exact classification for substituted arbitrary sources. Lejeune, Leroy and Rigo (2018 preprint; 2020 journal) establish the equality and next-degree separation of Thue–Morse substituted-letter blocks (their Lemma 30), as well as morphism-profile transfer. Their Theorem 48 gives an all-factor equivalence criterion specifically for the **Thue–Morse fixed point**, and therefore strongly covers the restricted fixed-point portion of this result; that portion is **not asserted as independent novelty**. The principal claim here instead classifies equivalence for \(\mu^r(\mathbf x)\) for **every binary source \(\mathbf x\)** and **every multiplier \(M\)**. The source-uniform if-and-only-if is proved by proper-prefix separation and an obstruction to conjugation to the inverse of a nontrivial unipotent series; it is not an immediate specialization of an all-factor characterization of the fixed point. The exact source-uniform statement was not located in the inspected sources, but exhaustive historical priority is not claimed.

## Limitations
The universal criterion is restricted to the specific binary substitution \(\mu(0)=01\), \(\mu(1)=10\), and window lengths divisible by \(2^r\). Other substitutions, window lengths and contiguous-factor equivalence are not classified. The Thue–Morse phase corollary is already inside the scope of a prior general factor-equivalence criterion, so its separate historical priority is not claimed. No external independent validation has been performed.

## References
1. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes*, Theoretical Computer Science 572 (2015), 83–91. Public repository record dated 26 February 2015: https://orbi.uliege.be/handle/2268/178702 .
2. M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, arXiv:1812.07330 (first posted 18 December 2018); J. Combin. Theory Ser. A 176 (2020). https://arxiv.org/abs/1812.07330 .
3. M. Rigo and P. Salimov, *Another generalization of Abelian equivalence: Binomial complexity of infinite words*, 2013. https://orbi.uliege.be/handle/2268/149313 .
