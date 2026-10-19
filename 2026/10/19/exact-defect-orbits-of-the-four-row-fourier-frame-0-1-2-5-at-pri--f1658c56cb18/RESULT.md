# Exact defect orbits of the four-row Fourier frame \(\{0,1,2,5\}\) at prime-power orders

## Finding
Let \(N=p^a>5\) be a prime power, \(\omega=\exp(2\pi i/N)\), and \(M=\{0,1,2,5\}\subset\mathbb Z/N\mathbb Z\). For each unordered four-element set \(C\subset\mathbb Z/N\mathbb Z\), define the unnormalized Fourier minor
\[
T_N(C)=(\omega^{rc})_{r\in M,\ c\in C}.
\]
Every such minor has rank either three or four. **All rank-three cases** are as follows; all other cases have rank four.

* If \(p=2\), necessarily \(a\ge3\), put \(h=N/8\). The four-column set is either a translate of \(\{0,2h,4h,6h\}\) or a translate of \(\{0,h,3h,4h\}\). These are disjoint translation orbits of cardinalities \(N/4\) and \(N\), respectively. Thus precisely \(5N/4\) of the \(\binom N4\) minors are singular.
* If \(p=5\), necessarily \(a\ge2\), the four-column set is a translate of \(\{0,N/5,2N/5,3N/5\}\). Equivalently, it is obtained by removing one element from a coset of the unique subgroup of order five. This orbit contains exactly \(N\) sets, hence precisely \(N\) minors are singular.
* If \(p\notin\{2,5\}\), all \(\binom N4\) minors are nonsingular.

The row pattern is a natural first quadratic case: within the family of four-row harmonic frames \(\{0,1,2,d\}\), the consecutive choice \(d=3\) has only the Vandermonde factor, while \(d=4\) has a linear Schur factor. The choice \(d=5\) is the first whose singularity is governed by a nontrivial quadratic Schur factor, allowing both fourth-root and eighth-root binary obstructions and a new fifth-torsion obstruction. Thus the result supplies a complete classification of failed four-sample reconstructions for a canonical next member of this family, including the exact number of defective column selections and their translation symmetries. The full-spark/non-full-spark dichotomy alone does not supply this information.

## Assumptions and scope
The Fourier matrix is unnormalized and has entries \(\omega^{rc}\); multiplying it by any nonzero normalization does not change rank. The row labels \(0,1,2,5\) must be distinct, which is ensured by \(N>5\). Column subsets have **four distinct** residues and are unordered. The theorem is restricted to prime-power cyclic orders; arbitrary mixed-prime moduli are not asserted to obey the same classification. The phrase rank-three means complex-linear matrix rank, not phase retrieval or a singular-value estimate.

## Proof
**1. A four-variable complete symmetric polynomial controls every minor.** Put \(z_j=\omega^{c_j}\) for the four distinct columns, and define
\[
h_2(z_1,z_2,z_3,z_4)=\sum_{1\le i\le j\le4}z_i z_j.
\]
The alternant/Vandermonde identity (or elementary interpolation) gives
\[
\det(z_j^{r})_{r\in\{0,1,2,5\},\ 1\le j\le4}
=\left(\prod_{1\le i<j\le4}(z_j-z_i)\right)h_2(z_1,z_2,z_3,z_4).
\]
Since the columns are distinct, the Vandermonde factor is nonzero. Moreover any three of the first three rows \(1,z,z^2\) on three distinct columns yield a nonzero Vandermonde determinant. Therefore vanishing of \(h_2\) is equivalent to **rank exactly three**.

**2. Only primes two and five can occur.** Consider the integer polynomial
\[
H(X)=\sum_{1\le i\le j\le4}X^{c_i+c_j}.
\]
If \(H(\omega)=0\), then the prime-power cyclotomic polynomial \(\Phi_{p^a}\) divides \(H\) in \(\mathbb Z[X]\). Since \(\Phi_{p^a}(1)=p\), the integer \(H(1)=10\) is divisible by \(p\). Thus \(p\in\{2,5\}\). This is only a necessary condition; the following two steps give the precise configurations.

**3. Binary prime powers force an antipodal pair.** Let \(p=2\). If all four roots have exponents of the same parity, divide their common root-of-unity factor and their exponent differences by two; this reduces to a smaller binary power without changing whether \(h_2=0\). Repeat until both exponent parities occur. Four distinct roots ensure that the final order is at least four. Write \(\zeta\) for the resulting primitive binary-power root. Because
\[
\mathbb Q(\zeta)=\mathbb Q(\zeta^2)\oplus\zeta\mathbb Q(\zeta^2),
\]
separate \(h_2\) into its even-exponent and odd-exponent parts. If the parity multiplicities are one and three, the odd part equals a nonzero singleton root times a sum of three binary-power roots. Such a three-term sum cannot vanish: its integer polynomial would have value three at one, contradicting divisibility by two. The same applies to multiplicities three and one. Hence there are two even and two odd roots, say \(u,v\) and \(s,t\). The odd part is
\[
(u+v)(s+t)=0.
\]
Consequently at least one pair of roots is antipodal. Undoing the common phase and power reductions preserves this antipodality.

Suppose the four roots are \(u,-u,v,w\), all of modulus one. Direct expansion yields
\[
h_2(u,-u,v,w)=u^2+v^2+vw+w^2.
\]
Set \(v/w=e^{i\theta}\). Dividing the second three terms by \(vw\) gives \(1+2\cos\theta\); as \(|u^2|=|vw|=1\), vanishing forces \(|1+2\cos\theta|=1\). Since \(v\ne w\), either \(v=-w\) or \(v/w=\pm i\). In the first case \(v^2=-u^2\), hence the four roots are a rotated copy of the fourth roots of unity. In the second case, \(vw=-u^2\), and the four roots are a rotated copy of \(\{1,e^{\pi i/4},e^{3\pi i/4},-1\}\). Conversely both shapes give \(h_2=0\) by direct substitution. Since the order is a power of two, both shapes exist at every \(N\ge8\), and these are exactly the two families in the statement.

The fourth-root coset has translation stabilizer of order four, so it has \(N/4\) translates. The second set has a unique antipodal pair and no nonzero translation stabilizer (check the four possible translations sending zero into the set), so it has exactly \(N\) translates. The two orbits are disjoint, proving \(5N/4\) rank-three minors.

**4. Fifth-power roots lie in one five-torsion coset.** Let \(p=5\) and \(a\ge2\). Write \(z_i=\zeta^{c_i}\) with \(\zeta\) primitive of order \(5^a\). The extension \(\mathbb Q(\zeta)/\mathbb Q(\zeta^5)\) has basis \(1,\zeta,\ldots,\zeta^4\). Accordingly, if \(h_2=0\), then for each residue \(r\pmod5\), the sum of all monomials \(\zeta^{c_i+c_j}\) for which \(c_i+c_j\equiv r\pmod5\) vanishes separately. After factoring \(\zeta^r\), each is a positive-coefficient sum of \(5^{a-1}\)-th roots. Its term count must be divisible by five, by the same cyclotomic evaluation-at-one argument.

Here is the needed finite residue lemma, proved without searching arbitrary integer orders: for four residues \(b_1,\ldots,b_4\in\mathbb Z/5\mathbb Z\), if every residue-class multiplicity of the ten pair sums \(b_i+b_j\) with \(i\le j\) is a multiple of five, then all four residues coincide. Indeed, if their multiplicity partition is \(3+1\), the pair-sum counts are \(6,3,1\); for \(2+2\), they are \(3,4,3\); for \(2+1+1\), no pair-sum multiplicity exceeds four; and for \(1+1+1+1\), each of the five pair-sum classes has count two. None permits all class counts divisible by five. This exhausts all nonconstant patterns.

Thus all \(c_i\) agree modulo five. Factoring their common fifth-residue phase and dividing all differences by five reduces the problem to four roots of order \(5^{a-1}\). Repeating at every level gives that all original column indices agree modulo \(5^{a-1}\). Since they are distinct, they are exactly four of the five elements of one order-five subgroup coset. Conversely, for \(\alpha\in\mu_5\) the identity
\[
\prod_{\substack{\beta\in\mu_5\\\beta\ne\alpha}}(1-\beta t)^{-1}
=\frac{1-\alpha t}{1-t^5}
\]
shows that its degree-two coefficient, namely \(h_2\) of these four fifth roots, is zero. Common rotations preserve this conclusion because \(h_2\) is homogeneous. Finally there are \(N/5\) subgroup cosets and five ways to omit one point in each; this gives exactly \(N\) singular minors. The proof is complete.

## Verification
The accompanying standalone Python program `verify.py` uses only exact integer arithmetic. For a primitive \(p^a\)-th root, it tests \(H(\omega)=0\) by checking that, for each exponent residue modulo \(N/p\), the coefficients of \(H\) at the \(p\) offsets separated by \(N/p\) are equal; this is exactly reduction modulo \(\Phi_{p^a}(X)=\sum_{j=0}^{p-1}X^{jN/p}\). It independently constructs and compares every four-column selection with the orbit classification, and exhausts the 625 possible four-tuples of residues modulo five for the finite residue and base identities.

Complete enumerations cover \(N=7,8,9,11,16,25,27,32,49,64\), with respective singular-minor counts \(0,10,0,0,20,25,0,40,0,80\). The script checks \(915{,}793\) distinct four-column minors across these orders. The finite experiments corroborate, but do not replace, the general argument above.

## Relationship to prior work
Alexeev, Cahill, and Mixon's *Full spark frames* proves the prime-power row-distribution criterion for full spark (Theorem 9). For these particular rows it predicts whether **some** singular maximal minor exists, but it neither counts them nor classifies their column sets; accordingly, the full-spark existence dichotomy is not asserted here as new. Caragea and Lee investigate principal Fourier minors, whereas the present four-row matrix has independent column selections. Hidaka and Itoh study Schur polynomials evaluated on **all primitive roots** of a fixed order; the present rank deficiency is governed by \(h_2\) on arbitrary **four-element subsets** of the prime-power roots. A related published computation handles the different row set \(\{0,1,2,4\}\), for which antipodal-pair defects follow another polynomial identity; it does not imply the two orbits for \(\{0,1,2,5\}\). A separate published full-spark criterion for \(\{0,1,3,4\}\) addresses different indices and does not count the configurations here. These are statement-level comparisons, not claims that a literature search proves absolute uniqueness.

## Limitations
The result is restricted to \(N\) a prime power and to the one prescribed four-row set. It supplies rank, not singular values or stability constants. The completeness proof relies on exact cyclotomic arithmetic and a four-residue multiplicity classification, not a finite-range extrapolation. A previously unindexed equivalent four-column census cannot be excluded without independent bibliographic review.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, first public September 15, 2024. https://arxiv.org/abs/2409.09793.
2. M. Hidaka and M. Itoh, *The Schur polynomials in all primitive nth roots of unity*, arXiv:2403.10817, first public March 16, 2024. https://arxiv.org/abs/2403.10817.
3. B. Alexeev, J. Cahill, and D. G. Mixon, *Full spark frames*, Journal of Fourier Analysis and Applications 18 (2012), 1167–1194, arXiv:1110.3548. https://arxiv.org/abs/1110.3548.
4. *Exact singular minors for the near-consecutive four-row harmonic frame*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-singular-minors-for-the-near-consecutive-four-row-harmonic--bb8a5601ae6d.
5. *Exact full-spark criterion for the four-row Fourier pattern \(\{0,1,3,4\}\)*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-full-spark-criterion-for-the-four-row-fourier-pattern-0-1--de39e0486913.
