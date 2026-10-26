# Quantized half-power convergence rates for first-order properties of random finite abelian \(p\)-groups

## Finding
Fix a prime \(p\). Choose uniformly from the isomorphism classes of abelian groups of order \(p^n\), so \(G_n\cong\bigoplus_{j\ge1}(\mathbb Z/p^j\mathbb Z)^{m_j}\) corresponds to a uniformly chosen integer partition of \(n\). For every first-order sentence \(\varphi\) in the pure group language, its probability \(u_n(\varphi)\) tends to a value \(\delta_\varphi\in\{0,1\}\), and exactly one of the following alternatives holds:

1. For every fixed \(K>0\), \(|u_n(\varphi)-\delta_\varphi|=O_{\varphi,K}(n^{-K})\).
2. There exist an effectively computable integer \(r\ge1\) and a strictly positive, effectively computable integer \(A\) such that
   \[
     |u_n(\varphi)-\delta_\varphi|
     =A\left(\frac{\pi}{\sqrt6}\right)^r n^{-r/2}
        +O_\varphi(n^{-(r+1)/2}).
   \]

Every positive integer \(r\) occurs for a first-order sentence. The limiting zero-one law is classical; the contribution is the sharp universal half-power rate spectrum, its integer quantization, the superpolynomial alternative and the effective extraction of the leading rate.

## Assumptions and scope
The prime \(p\) is fixed, not allowed to vary with \(n\). The sample is uniform on **isomorphism classes** of finite abelian \(p\)-groups of *order* \(p^n\), not uniform on labelled group operations or on groups of cardinality \(n\). The pure group language uses addition, zero and inverse; scalar multiplication by any fixed integer is an abbreviation for a term. Let \(P(N)\) count integer partitions of \(N\), with \(P(N)=0\) for \(N<0\). The class has exactly \(P(n)\) objects at size parameter \(n\).

## Proof
**1. First-order reduction.** The Baur–Monk elimination of quantifiers for modules, applied to \(\mathbb Z\)-modules, says that a sentence is a Boolean combination of invariant conditions of the form \([\rho(G):\sigma(G)]\ge t\), where \(\rho\), \(\sigma\) are positive-primitive definable subgroups, \(\sigma(G)\subseteq\rho(G)\), and \(t\) is a fixed positive integer. We may replace \(t\) by a power of \(p\), since finite indices in our structures are powers of \(p\). For each cyclic summand set
\[
 e_j=\log_p[\rho(\mathbb Z/p^j\mathbb Z):\sigma(\mathbb Z/p^j\mathbb Z)]\in\mathbb N_0.
\]
Positive-primitive solution sets commute with finite direct sums, so this invariant is equivalent to \(\sum_{j\ge1}m_je_j\ge T\) for some fixed integer \(T\ge0\).

**2. Effective support dichotomy.** For a fixed pp-pair over \(\mathbb Z\), the nonnegative integer \(e_j\) is eventually affine in \(j\), with effectively decidable breakpoints and coefficients. To see this, express each pp formula as a finite integer linear system with existentially quantified unknowns; Smith normal forms of the defining matrices and of the relevant projections give the sizes of solution sets over \(\mathbb Z/p^j\mathbb Z\) as finite products of powers \(p^{\min(j,a)}\) and \(p^{\max(0,j-a)}\), with effectively computable \(p\)-adic orders \(a\). Subtracting logarithms for \(\rho\) and \(\sigma\) proves the claim. Hence \(\{j:e_j>0\}\) is either finite or cofinite, and the alternative is decidable.

**3. Infinite-support tests become almost surely true at superpolynomial speed.** If \(e_j>0\) at infinitely many \(j\), fix any \(K\) such indices \(j_1,\ldots,j_K\). Failure of \(\sum_jm_je_j\ge T\) implies \(m_{j_i}<T\) for all \(i\). Each of the finitely many exact multiplicity events has probability \(O(n^{-K/2})\) by the partition estimate in Step 4. Since \(K\) is arbitrary, the failure probability decays faster than any power of \(n\). A union bound over the finitely many pp-tests used in \(\varphi\) lets us replace every infinite-support test by true at superpolynomial probability cost.

**4. Exact finite-cylinder estimate.** Fix a finite set \(S\) of distinct positive integers and fixed nonnegative multiplicities \(a_j\) for \(j\in S\). Taking the generating function for integer partitions and forcing \(m_j=a_j\) for \(j\in S\) gives the exact identity
\[
 \Pr(m_j=a_j\ (j\in S))
  ={1\over P(n)}\sum_{U\subseteq S}(-1)^{|U|}
      P\left(n-\sum_{j\in S}ja_j-\sum_{j\in U}j\right).
\]
The first Rademacher term, a smooth function of the real argument, approximates \(P(n)\) up to an error exponentially smaller than \(P(n)\). Its logarithmic derivative is \(\pi/\sqrt{6n}+O(n^{-1})\), and its finitely many fixed-shift finite differences have the corresponding asymptotic expansions. Consequently, for \(s=|S|\),
\[
 \Pr(m_j=a_j\ (j\in S))
 =\left({\pi\over\sqrt{6n}}\right)^s\prod_{j\in S}j
  +O_{S,a}(n^{-(s+1)/2}).
\]
The leading coefficient is independent of the fixed \(a_j\), and the assertion also holds for \(S=\varnothing\), with probability one.

**5. Extracting the universal rate.** The finitely many surviving pp-tests have finite support in the index \(j\). Let \(J\) contain their union of supports, and choose a common cap \(M\ge1\), at least as large as every integer threshold. The Boolean truth value of their combination is an explicit function
\[
  f:\{0,1,\ldots,M\}^{J}\longrightarrow\{0,1\}
\]
of capped multiplicities \(\min(m_j,M)\). Let \(\delta=f(M,\ldots,M)\). By Step 4, every fixed finite collection of multiplicities exceeds \(M\) with probability tending to one; thus \(\delta\) is the limiting truth probability.

If \(f\equiv\delta\), Step 3 proves the first alternative. Otherwise define \(r\) to be the least number of coordinates at which an input to \(f\) can be below \(M\) and give the opposite truth value. It follows that \(r\ge1\). For every \(r\)-element set \(S\subseteq J\), let \(b(S)\) be the number of tuples \((a_j)_{j\in S}\in\{0,\ldots,M-1\}^{S}\) for which \(f\), with all other coordinates set to \(M\), differs from \(\delta\). The integer
\[
  A=\sum_{\substack{S\subseteq J\\|S|=r}} b(S)\prod_{j\in S}j
\]
is positive by minimality of \(r\). Sum the Step 4 estimate over these disjoint minimal-deficiency events. Restricting other coordinates to values at least \(M\) alters their joint probabilities by at most \(O(n^{-(r+1)/2})\), again by Step 4. Contributions involving \(r+1\) or more deficient coordinates have this same lower order. Step 3 contributes a superpolynomial error. Therefore \(|u_n(\varphi)-\delta|\) has the stated leading term. All constituent normal forms, support tests and finite Boolean computations are effective.

**6. Every exponent occurs.** For fixed \(r\ge1\), let \(V_j=(p^{j-1}G)[p]/(p^jG)[p]\), a pp-pair quotient of order \(p^{m_j}\). The sentence saying that at least one of \(V_1,\ldots,V_r\) is nontrivial is first-order and has generic truth value one. Failure means \(m_1=\cdots=m_r=0\); Step 4 gives
\[
  \Pr(\text{failure})
   =r!\left({\pi\over\sqrt6}\right)^r n^{-r/2}
     +O_r(n^{-(r+1)/2}).
\]
This realizes every \(r\) and finishes the proof.

## Verification
Run the self-contained program `verify_partition_speed.py` with Python 3. It enumerates small partitions, verifies the exact finite-difference multiplicity formula and pp-quotient interpretation, and checks scaled probabilities at selected large \(n\). Its successful output is `PARTITION_FO_SPEED_FINITE_OK 945 checks`. The finite computations are supporting checks only; the all-sentence and all-size statements are established by the module-normal-form and partition-asymptotic proof above.

## Relationship to prior work
The zero-one law for uniform isomorphism classes of finite abelian \(p\)-groups is not claimed as new. It follows from classical Feferman–Vaught/Compton methods and the partition asymptotic regime; see Burris–Compton–Odlyzko–Richmond (1997) and Bell–Burris (2003). Szmielew's classification and Baur–Monk elimination provide the logical structural foundation. The quantitative half-integer decay hierarchy, positive integer coefficient quantization and effective leading-rate extraction are the additional result. The recent investigations of logical limit laws for small permutation classes by Marström–Räty (2026) and finite-model questions by Koponen (2026) motivate examining finer information than existence of a limit, but use different random structures and do not establish this rate statement.

## Limitations
The law assumes a fixed prime and uniform *isomorphism classes* of order \(p^n\). No statement is made about uniform labelled groups or other group families. Computing the leading integer from a formula may require expensive elimination and finite enumeration; no polynomial-time complexity is asserted. Priority over all earlier partition-system speed results is not independently established: Burris's 2001 monograph was accessible only through publicly supplied introductory excerpts, and the full 1997 paper was not available in the accessible source consulted. The full Bell–Burris 2003 treatment was inspected and concerns sufficient criteria for the existence of logical limits rather than the present sharp rate hierarchy. The proof depends on classical Baur–Monk elimination and Rademacher's asymptotic expansion; the executable finite checker does not establish these infinite theorems.

## References
- K. J. Compton, *A logical approach to asymptotic combinatorics I–II*, Advances in Mathematics 65 (1987), 65–96; Journal of Combinatorial Theory Series A 50 (1989), 110–131.
- S. N. Burris, K. J. Compton, A. M. Odlyzko and L. B. Richmond, *Fine Spectra and Limit Laws, II: First-Order 0–1 Laws*, Canadian Journal of Mathematics 49 (1997), 641–652, doi:10.4153/CJM-1997-030-6.
- J. P. Bell and S. N. Burris, *Asymptotics for Logical Limit Laws: When the Growth of the Components Is in an RT Class*, Transactions of the AMS 355 (2003), 3777–3794.
- W. Szmielew, *Elementary properties of Abelian groups*, Fundamenta Mathematicae 41 (1955), 203–271.
- W. Baur, *Elimination of quantifiers for modules*, Israel Journal of Mathematics 25 (1976), 64–70; J. A. Monk, *On the representation theory for modules*, Journal of Symbolic Logic 36 (1971), 309–317.
- H. Rademacher, *On the partition function \(p(n)\)*, Proceedings of the London Mathematical Society 43 (1937), 241–254.
- K. Marström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1 (first public posting 2026-10-15).
- V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first public posting 2026-10-12).
