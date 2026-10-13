# Prime-power gcd strata of weight-two GDRS coset spectra

## Finding
Let \(q\) be any prime power and \(5\le d\le q\). Put \(M=q-1\), \(k=d-2\), and suppose \(\gcd(M,k)=p^a>1\), where \(p\) is prime and \(a\ge1\). For the normalized \([q+1,q+2-d,d]_q\) generalized doubly extended Reed–Solomon (GDRS) code, the weight-two cosets have **exactly \(a+1\) distinct complete Hamming-weight distributions**. All distributions and their exact numbers of cosets are as follows.

Fix a primitive element \(\beta\in\mathbb F_q^*\). The coset with its unique weight-two leader having nonzero symbols \(\gamma_1,\gamma_2\) has class \(s=\min(a,v_p(\lambda))\), where \(\beta^\lambda=-\gamma_2/\gamma_1\) and \(v_p(0)=\infty\); only the residue \(\lambda\pmod{p^a}\) matters. Set
\[
 A_j=(-1)^{k+k/p^j}\binom{M/p^j}{k/p^j}\quad(0\le j\le a).
\]
Then the number of words of weight \(d-2\) in a class-\(s\) coset is
\[
 F_s=\frac{A_0+\sum_{j=1}^{s}(p^j-p^{j-1})A_j-p^sA_{s+1}}{M}\quad(0\le s<a),\qquad
 F_a=\frac{A_0+\sum_{j=1}^{a}(p^j-p^{j-1})A_j}{M}.
\]
All \(F_0,\ldots,F_a\) are pairwise distinct. For \(0\le s<a\), the exact number of class-\(s\) cosets is
\[
 \binom{q+1}{2}\frac{M^2}{p^a}\bigl(p^{a-s}-p^{a-s-1}\bigr),
\]
and for class \(a\) it is \(\binom{q+1}{2}M^2/p^a\). Thus these classes partition the full \(\binom{q+1}{2}M^2\) weight-two cosets.

The entire distribution of each class follows without ambiguity from \(F_s\) using the weight enumerator in Theorem 5.1 of Davydov–Marcugini–Pambianco [1], restated under Verification. This is a strict classification of spectra, not merely an orbit upper bound. It includes the positive-gcd prime case underlying [1, Conjectures 4.12 and 5.3], while the combinatorial subset-sum formula itself is previously known [2].

## Assumptions and scope
All arithmetic is exact. The code is the normalized GDRS code of [1], with minimum distance at least five. A coset is a translate of this linear code. The weight of a coset vector is Hamming weight, and a complete coset distribution \((B_0,\ldots,B_{q+1})\) lists the numbers of vectors of each Hamming weight. The uniqueness of the weight-two leader follows from distance at least five: two distinct such vectors could otherwise differ by a nonzero codeword of weight at most four. The coefficient \(F_s=B_{d-2}\) is meaningful even for \(d=5\) (then \(d-2=3\)). We require \(1\le k<M\), which follows from \(5\le d\le q\). We make no assertion for composite \(\gcd(M,k)\) with at least two distinct prime factors.

## Proof
**(1) Exact cyclic count.** Let \(N_{M,k}(\lambda)\) be the number of unordered \(k\)-element subsets of \(\mathbb Z_M\) with sum \(\lambda\pmod M\). By character orthogonality, or directly by the already known Li–Wan–Kosters subset-sum theorem [2, Theorem 2.3],
\[
 N_{M,k}(\lambda)=\frac1M\sum_{e\mid\gcd(M,k)}(-1)^{k+k/e}\binom{M/e}{k/e}c_e(\lambda),\qquad
 c_e(\lambda)=\sum_{h\mid\gcd(e,\lambda)}h\,\mu_{\rm Mob}(e/h).
\]
This general counting identity is cited, not proposed as new. For \(e=p^j\), the Ramanujan sum \(c_e(\lambda)\) equals \(p^j-p^{j-1}\) if \(j\le v_p(\lambda)\), equals \(-p^{j-1}\) if \(j=v_p(\lambda)+1\), and is zero otherwise. The \(j=0\) term is one. Substitution gives precisely the displayed \(F_s\) formulas. By [1, Theorems 3.4 and 5.1], \(N_{M,k}(\lambda)\) equals the weight-\(d-2\) coefficient for a weight-two GDRS coset whose leader ratio has discrete logarithm \(\lambda\).

**(2) Strict separation.** For \(1\le s<a\), direct subtraction yields
\[
 F_s-F_{s-1}=\frac{p^s}{M}(A_s-A_{s+1}),\qquad F_a-F_{a-1}=\frac{p^a}{M}A_a.
\]
For any integer \(p\ge2\) and \(0<K<N\), \(\binom{pN}{pK}>\binom NK\): every \(K\)-subset of \(\{1,\ldots,N\}\) provides a distinct union of its \(p\) coordinate fibers of size \(pK\), and there are additional \(pK\)-subsets not formed from complete fibers. Hence the positive binomial magnitudes \(\lvert A_0\rvert>\cdots>\lvert A_a\rvert\).

If \(p\) is odd, all \(A_j>0\), so \(F_0<F_1<\cdots<F_a\). If \(p=2\), then \(k\) is even and \(A_j>0\) for \(j<a\). If also \(A_a>0\), the same increasing chain holds. The only other case is \(A_a<0\), equivalently \(v_2(k)=a\). If \(a=1\), then \(F_1-F_0=2A_1/M<0\). If \(a\ge2\), the first \(a\) values form the increasing chain \(F_0<\cdots<F_{a-1}\), while
\[
 F_a-F_{a-1}=\frac{2^a A_a}{M}<0,\qquad
 F_a-F_{a-2}=\frac{2^{a-1}(A_{a-1}+A_a)}M>0.
\]
The last inequality holds because \(A_{a-1}>\lvert A_a\rvert\). Therefore \(F_{a-2}<F_a<F_{a-1}\) and all \(a+1\) values are distinct in every case. As \(B_{d-2}=F_s\), distinct values imply distinct *full* distributions.

**(3) Exact multiplicities.** The class \(s<a\) contains \((M/p^a)\bigl(p^{a-s}-p^{a-s-1}\bigr)\) residues \(\lambda\pmod M\), while class \(a\) contains \(M/p^a\) residues. For each residue and each pair of support positions among \(q+1\), there are exactly \(M\) ordered nonzero leader-symbol choices realizing the specified ratio (select \(\gamma_1\ne0\), then uniquely determine \(\gamma_2\)). Distinct weight-two leaders give distinct cosets because \(d\ge5\). Multiplication gives the stated coset multiplicities and verifies their sum.

## Verification
For any class \(s\), all \(B_w\) are explicitly reconstructed from \(F_s\) by [1, Theorem 5.1]:
\[
 B_2=1,\quad B_w=0\quad(0\le w\le d-3,\ w\ne2),\quad B_{d-2}=F_s,
\]
and for \(d-1\le w\le q+1\),
\[
 B_w=A_w(C)-(-1)^{w-d}\binom{q+1}{w}\binom{w-1}{d-2}
 +(-1)^{w-d}\binom{q-1}{w-2}\binom{w-3}{d-4}
 +(-1)^{w-d}\binom{q+3-d}{q+1-w}F_s,
\]
where \(A_w(C)\) is the classical MDS codeword weight count of the code, known from its \([q+1,q+2-d,d]_q\) parameters. No full coset enumeration is asserted for arbitrary \(q\); the infinite-family conclusion follows algebraically from [1,2] and step (2).

A standalone Python 3 verifier, `verify.py`, independently enumerates all \(k\)-subsets for 33 pairs \((M,k)\) with \(5\le M\le17\), \(3\le k<M\) and prime-power \(\gcd(M,k)>1\). It compares their complete residue histograms with the character formula, valuation-class formulas and exact class multiplicities. For the first three-class example \(q=9,d=6\) (\(M=8,k=4\)), the distinct weight-four counts are \((F_0,F_1,F_2)=(8,10,9)\), with class coset multiplicities \((1440,720,720)\), totaling \(2880\). Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Davydov, Marcugini and Pambianco [1] establish the link from weight-two cosets to cyclic subset sums and tabulate finite parameter families, explicitly asking in §4.2 whether distinct orbits always yield distinct values. Their Theorem 5.1 reconstructs full coset spectra from one count, and their Conjectures 4.8, 4.12 and 5.3 supply explicit motivations. Kosters [2, Theorem 2.3], citing Li and Wan, **already proves a character formula for all finite-abelian-group subset sums**; the Fourier formula used here is not independently new. The new content is the unrestricted \(p^a\)-index strict spectrum separation, closed forms and exact numbers of code cosets in each class. Blokhuis, Pellikaan and Szőnyi [3] handle a related but different invariant, the extended coset-leader enumerator, for the distance-five twisted-cubic code; they do not give an all-\(a\) class multiplicity result.

## Limitations
The prime-power condition concerns \(\gcd(q-1,d-2)\), not necessarily \(q-1\) itself. For gcd with more than one prime divisor, the general known subset-sum formula remains available, but this statement does not assert strict distinctness for every gcd orbit. The finite verifier demonstrates reproducibility for small cases and does not replace the proof. The result is a synthesis involving two previously established major reductions; any earlier source explicitly classifying all prime-power strata would supersede its novelty. No independent mathematical audit has been performed.

## References
[1] A. A. Davydov, S. Marcugini, F. Pambianco, *Weight distributions of cosets of weight 2 of the generalized doubly extended Reed–Solomon codes*, arXiv:2605.10594v1, first posted 2026-05-11, https://arxiv.org/html/2605.10594v1.

[2] M. Kosters, *The subset sum problem for finite abelian groups*, arXiv:1112.6294v1, first posted 2011-12-29, https://arxiv.org/html/1112.6294v1 (general formula due to J. Li and D. Wan).

[3] A. Blokhuis, R. Pellikaan, T. Szőnyi, *The extended coset leader weight enumerator of a twisted cubic code*, Designs, Codes and Cryptography 90 (2022), 2223–2247, https://doi.org/10.1007/s10623-022-01060-0.
