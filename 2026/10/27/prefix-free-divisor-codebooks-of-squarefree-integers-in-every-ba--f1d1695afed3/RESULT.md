# Prefix-free divisor codebooks of squarefree integers in every base

## Finding

Fix an integer base \(b\ge 2\) and an integer \(r\ge 1\). Let \(\operatorname{rep}_b(d)\) be the usual finite base-\(b\) expansion of a positive integer \(d\), without leading zeros. Let \(\mathcal P_{b,r}(X)\) be the set of integers \(n\le X\) that are squarefree, have exactly \(r\) distinct prime factors, and whose nonunit-divisor expansions
\[
 \{\operatorname{rep}_b(d): d\mid n,\ d>1\}
\]
form a prefix-free code: no such expansion is a proper initial segment of another.

**Theorem.** For each fixed pair \((b,r)\), there are constants \(c_{b,r}>0\) and \(X_{b,r}\) such that, for all real \(X\ge X_{b,r}\),
\[
 |\mathcal P_{b,r}(X)|\ge c_{b,r}\frac{X}{(\log X)^r}.
\]
In particular, for every \(r\ge1\) there are infinitely many squarefree integers with exactly \(r\) prime factors whose nontrivial divisors are pairwise prefix-free in **binary**. This proves existence for every argument of the two minimal-number problems OEIS A090335 (distinct prime factors) and A088862 (prime factors counted with multiplicity); it does not determine their minimal values.

## Assumptions and scope

The base \(b\) is an ordinary integer base at least two. Prefix means literal digit-string prefix, not divisibility, not prefix in an ordered prime-factor list, and not prefix of a concatenated code. The integer \(n\) is squarefree and has \(\omega(n)=\Omega(n)=r\), so every nonunit divisor corresponds to a unique nonempty subset of its prime factors. The counting statement is a uniform-in-\(X\) lower bound for each **fixed** \((b,r)\); no uniformity as \(r\) grows with \(X\) is claimed. The only analytic input is the prime number theorem in fixed proportional intervals.

## Proof

**1. Distinct subset-product mantissas.** Write the base as \(b=\prod_{q\mid b}q^{e_q}\) and put \(g=\gcd_{q\mid b}e_q\). Choose a prime \(\ell\ge3\) not dividing \(g\). For \(1\le i\le r\), set
\[
 t_i=\ell^{-i},\qquad u_i=b^{t_i}.
\]
For every nonempty subset \(S\subseteq\{1,\ldots,r\}\), put
\[
 t_S=\sum_{i\in S}\ell^{-i},\qquad u_S=\prod_{i\in S}u_i=b^{t_S}.
\]
Every \(t_S\) lies strictly between zero and \(1/(\ell-1)\le1/2\). The numbers \(t_S\) are pairwise distinct: their finite base-\(\ell\) expansions have digits zero or one precisely at the indexed positions in \(S\). Consequently the \(u_S\) are distinct elements of \((1,b)\).

None of the \(u_S\) is rational. Indeed, if \(j=\max S\), then \(t_S=A/\ell^j\) with \(A\) an integer coprime to \(\ell\). At least one prime \(q\mid b\) satisfies \(\ell\nmid e_q\). Were \(u_S\) rational, its \(q\)-adic valuation would be an integer, whereas the identity \(u_S^{\ell^j}=b^A\) would force that valuation to equal \(Ae_q/\ell^j\), which is not an integer. Thus the \(u_S\) never lie on a rational base-\(b\) digit-cylinder boundary.

**2. A robust family of distinct digit prefixes.** Since the collection of nonempty subsets is finite and the corresponding \(u_S\) are distinct and not base-\(b\) cylinder boundaries, there exists an integer \(K\ge1\) for which all \(u_S\) lie in pairwise distinct **open** level-\(K\) digit cylinders
\[
 \left(\frac{a_S}{b^{K-1}},\frac{a_S+1}{b^{K-1}}\right),
 \qquad a_S=\left\lfloor b^{K-1}u_S\right\rfloor.
\]
Here \(a_S\) encodes the first \(K\) base-\(b\) digits of a number in \((1,b)\). By continuity of all finitely many subset-product maps, there is a single \(\eta>0\), small enough that the \(r\) real intervals \((u_i-\eta,u_i+\eta)\) are positive and pairwise disjoint, such that for **every** choice \(y_i\in(u_i-\eta,u_i+\eta)\), all nonempty subset products \(\prod_{i\in S}y_i\) remain in the respective, pairwise different level-\(K\) cylinders. Shrinking \(\eta\) if needed also ensures each such product stays in \((1,b)\).

**3. Prime factors in the stable intervals.** Fix an integer \(L\ge K\). For each \(i\), choose an arbitrary prime \(p_i\) in
\[
 I_i(L)=\big((u_i-\eta)b^L,(u_i+\eta)b^L\big).
\]
The intervals are disjoint, so all the chosen primes are distinct. Put \(n=\prod_{i=1}^r p_i\). For a nonempty subset \(S\), the associated divisor is
\[
 d_S=\prod_{i\in S}p_i=b^{L|S|}v_S,\qquad
 v_S=\prod_{i\in S}\frac{p_i}{b^L}.
\]
By the preceding construction, \(1<v_S<b\), and \(v_S\) lies in the level-\(K\) digit cylinder assigned to \(S\). Therefore \(d_S\) has \(L|S|+1\ge K\) base-\(b\) digits, and its first \(K\) digits encode \(a_S\). These first \(K\) digits differ for every two distinct nonempty subsets \(S\). As every divisor word has at least \(K\) digits, no two divisor words can stand in a proper-prefix relation. Thus \(n\) has the claimed property, **for every possible choice of primes from the prescribed intervals**.

**4. Counting the resulting integers.** The prime number theorem gives, for each fixed \(i\),
\[
 \#\{p\text{ prime}:p\in I_i(L)\}
 = (2\eta+o(1))\frac{b^L}{L\log b}
 \quad (L\longrightarrow\infty).
\]
Since the prime intervals are disjoint, selecting one prime from each gives different products by unique factorization. Thus at least \(c'_{b,r}(b^L/L)^r\) distinct admissible squarefree integers arise for all sufficiently large \(L\), with \(c'_{b,r}>0\). Every such product is bounded above by \(Cb^{rL}\), where \(C=\prod_{i=1}^r(u_i+\eta)\).

Given a sufficiently large real \(X\), choose
\[
 L=\left\lfloor\frac{\log_b(X/C)}r\right\rfloor.
\]
Then \(L\ge K\), all products are at most \(X\), and \(b^{rL}>X/(Cb^r)\), while \(L\) is comparable to \(\log X\). The product count therefore gives
\[
 |\mathcal P_{b,r}(X)|\gg_{b,r}\frac{X}{(\log X)^r},
\]
which is the asserted bound. In base two the constructed integers witness the existence asserted in A090335. Being squarefree, they also have exactly \(r\) prime factors with multiplicity, so they witness the existence assertion in A088862. \(\square\)

## Verification

The supplied standard-library Python verifier checks literal digit-string prefix-freeness for all nonunit divisors of five explicitly constructed examples: bases \(2,3,5,8,10\), with respectively \(7,6,6,5,5\) distinct prime factors. In base two it checks \(127\) divisors of the product of the primes \(84551941,72481583,68854001,67685627,67300579,67172717,67130149\), and confirms that their initial \(13\) binary digits are pairwise different. It checks primality by trial division, without relying on a precomputed divisor table. Invoke `python3 verify.py`; successful execution prints `VERIFY_OK`. These finite witnesses are illustrative only. The quantification over all bases, all fixed prime-factor counts, and all sufficiently large bounds is supplied by the proof and the prime number theorem, not the experiment.

## Relationship to prior work

The original 2003 OEIS entry A090335 asks whether the least integer with \(r\) **distinct** prime factors and binary prefix-free nonunit divisors exists for every \(r\). OEIS A088862 asks the analogous existence question with prime factors counted with multiplicity. Both entries record finite data but not an infinite construction. OEIS A090332 is the ambient integer sequence defined by binary prefix-free divisors. The present result supplies an infinite, quantitative squarefree construction, and automatically settles both existence formulations if its proof is accepted.

Ahlswede, Khachatrian, and Sárközy (2000) also use the words *prefix-free integers*, but their definition concerns the ordered sequences of prime factors: one squarefree integer is a prefix of another when the latter's prime-factor list extends the former's list. It does **not** concern the initial digits of the ordinary base-\(b\) expansions of divisors. Their theorems therefore do not imply this claim. Likewise, an abstract prefix-code existence theorem for prescribed word lengths does not guarantee that a fixed set of actual integer divisors has those initial digit strings.

## Limitations

The constants and threshold depend on the fixed base and number of prime factors and are not optimized. This proves existence and a lower counting bound, **not** the least admissible integer for any given \(r\), nor an asymptotic equivalent for the entire set. The finite verifier does not certify the analytic prime-counting step. Literature searches and comparison with the identified primary works did not reveal equivalent coverage, but unseen or unindexed stronger results remain a scientific priority risk. Independent mathematical verification has not been performed.

## References

1. Reinhard Zumkeller, OEIS A090335, *Smallest number with exactly n distinct prime factors such that in binary representation the divisors >1 form a prefix code*, submitted November 26, 2003, https://oeis.org/A090335.
2. Reinhard Zumkeller, OEIS A088862, *Smallest number with exactly n prime factors (possibly with repetitions) such that in binary representation the divisors >1 form a prefix code*, submitted November 26, 2003, https://oeis.org/A088862.
3. Reinhard Zumkeller, OEIS A090332, *Numbers with no divisors >1 that are prefixes of other divisors in binary representation*, submitted November 26, 2003, https://oeis.org/A090332.
4. R. Ahlswede, L. H. Khachatrian and A. Sárközy, *On prefix-free and suffix-free sequences of integers*, in *Numbers, Information and Complexity* (2000), pp. 1–16, DOI 10.1007/978-1-4757-6048-4_1. Author-hosted text: https://www.math.uni-bielefeld.de/ahlswede/homepage/public/151.pdf.
5. Prime number theorem, standard fixed-interval consequence: for fixed real \(0<a<c\), the number of primes in \((aT,cT)\) is asymptotic to \((c-a)T/\log T\) as \(T\to\infty\).
