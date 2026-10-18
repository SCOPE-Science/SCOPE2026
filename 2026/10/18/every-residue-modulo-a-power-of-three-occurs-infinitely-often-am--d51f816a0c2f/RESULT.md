# Every residue modulo a power of three occurs infinitely often among Catalan numbers

## Finding
For \(n\ge0\), put \(C_n=\frac{1}{n+1}\binom{2n}{n}\). For each integer \(k\ge1\) and every residue \(r\in\mathbb Z/3^k\mathbb Z\), infinitely many \(n\ge0\) satisfy
\[
C_n\equiv r\pmod{3^k}.
\]
More strongly, for every \(k,S\ge1\), the set of residues of \(\binom{2N}{N}\) with \(N\ge1\) divisible by \(3^S\) is the full ring \(\mathbb Z/3^k\mathbb Z\), and each residue occurs infinitely many times. This answers the forbidden-residue question posed for powers of three in Rowland--Yassawi, Open Question 3.6 (2013/2015).

## Assumptions and scope
All congruences below are among ordinary integers. Set \(B(N)=\binom{2N}{N}\) for \(N\ge0\); \(v_3\) denotes the exponent of three. The theorem concerns existence and infinitude of indices, not positive natural density or an effective bound on the first index. The underlying published question concerns all prime powers of three; only those moduli are claimed here.

## Proof
**1. Separation of widely spaced ternary blocks.** Fix \(k\ge1\). For integers \(a\ge0\) and \(N\ge1\), assume \(v_3(N)\ge k+\lfloor\log_3(2a)\rfloor\), where for \(a=0\) the statement is immediate. The exact rational identity
\[
\frac{B(N+a)}{B(N)B(a)}=
\frac{\prod_{i=1}^{2a}(1+2N/i)}{\prod_{i=1}^{a}(1+N/i)^2}
\]
has every factor in \(1+3^k\mathbb Z_3\): indeed, \(v_3(i)\le\lfloor\log_3(2a)\rfloor\) for \(1\le i\le2a\). The quotient therefore lies in \(1+3^k\mathbb Z_3\). As both binomial coefficients are integers,
\[
B(N+a)\equiv B(N)B(a)\pmod{3^k}.\tag{1}
\]
This holds for arbitrarily large \(a\) provided the new block \(N\) is sufficiently more divisible by three.

**2. A supply of primitive-root factors.** For each integer \(R\ge1\), set \(b_R=B(3^R)\). Directly from the factorial ratio,
\[
b_R=2\prod_{i=1}^{3^R-1}\left(1+\frac{3^R}{i}\right).
\]
Modulo nine all factors are one except those at \(i=3^{R-1}\) and \(i=2\cdot3^{R-1}\), since the remaining factors have \(3\)-adic numerator valuation at least two. The exceptional product is \(4(1+3/2)=10\equiv1\pmod9\). Hence
\[
b_R\equiv2\pmod9\qquad(R\ge1).\tag{2}
\]
Every integer \(u\equiv2\pmod9\) has order \(2\cdot3^{k-1}\) in \((\mathbb Z/3^k\mathbb Z)^\times\), for \(k\ge1\): it has order two modulo three, and \(v_3(u^2-1)=1\) gives \(v_3(u^{2\cdot3^j}-1)=j+1\) by repeated cubing (or the lifting-the-exponent lemma). In particular every \(b_R\) generates the unit group modulo \(3^k\).

Fix \(k\). Since the infinite sequence \((b_R\bmod3^k)_{R\ge1}\) takes finitely many values, one value \(u\) occurs for infinitely many strictly increasing exponents \(R\), and this \(u\) is a generator. From that infinite set we may choose arbitrarily separated exponents.

**3. All central-binomial residue classes, with arbitrary initial zeros.** Fix also \(S\ge1\). For each \(t\in\{0,1,\dots,k\}\) choose
\[
a_t=\begin{cases}1,&t=0,\\ (3^t+1)/2,&t\ge1.\end{cases}
\]
For \(t\ge1\) the lowest \(t\) ternary digits of \(a_t\) consist of a final digit two followed by \(t-1\) ones, so adding \(a_t\) to itself creates precisely \(t\) carries. Kummer's theorem yields \(v_3(B(a_t))=t\); also \(v_3(B(a_0))=0\). Multiplication of an index by \(3^S\) merely shifts its ternary digits, hence the seed \(A_t=3^Sa_t\) satisfies
\[
v_3(B(A_t))=t.\tag{3}
\]
Choose as many exponents \(R_1<\cdots<R_j\) as desired from the infinite set in step 2, subject to \(R_1>S\) and
\[
3^{R_i}\text{ is divisible by }3^{k+\lfloor\log_3(2(A_t+\sum_{h<i}3^{R_h}))\rfloor}.
\]
These inequalities are attainable because the selected exponents are unbounded. Repeatedly applying (1) gives, for \(N_j=A_t+\sum_{i=1}^j3^{R_i}\),
\[
B(N_j)\equiv B(A_t)u^j\pmod{3^k}.\tag{4}
\]
Each \(N_j\) is divisible by \(3^S\). If \(t<k\), equation (3) implies \(B(A_t)=3^t w_t\) with \(w_t\) a unit. Because \(u\) generates the entire unit group modulo \(3^{k-t}\), varying \(j\) gives every residue of exact valuation \(t\) modulo \(3^k\). The class zero occurs using \(t=k\). The same residue occurs for infinitely many larger \(j\), by the periodicity of \(u^j\); choosing ever larger exponents also gives distinct, unbounded indices. This proves the stronger assertion.

**4. Transfer to Catalan numbers.** For every \(N\ge1\), the exact identity
\[
C_{N-1}=\frac{B(N)}{2(2N-1)}
\]
holds. Restrict the already constructed indices to multiples of \(3^S\) with \(S\ge k\). Then \(2(2N-1)\equiv-2\pmod{3^k}\), a unit independent of \(N\). Therefore
\[
C_{N-1}\equiv-\tfrac12B(N)\pmod{3^k}.
\]
Multiplication by \(-1/2\) permutes all residues, and distinct growing \(N\) yield distinct growing \(N-1\). This proves the theorem. \(\square\)

## Verification
An accompanying standalone Python checker confirms Kummer's seed valuations, the primitive-root claim for powers of three, the splitting lemma on numerous exact finite cases, and that all \(3^k\) residues for \(1\le k\le5\) occur among a finite prefix of Catalan numbers. These finite checks are diagnostic only: the infinite assertion follows from the preceding proof, including the infinite pigeonhole selection, not from enumeration.

## Relationship to prior work
Krattenthaler--Müller (arXiv:1308.2856v1, 2013), Section 12, develops power-of-three generating-function congruences for Catalan numbers; its Theorem 37 is an algorithmic expansion, and its Theorem 38/Corollary 39 give explicit reductions modulo 27 and 9. These are pointwise computation tools and do not in the inspected section assert the all-residue existence theorem. Rowland--Yassawi (arXiv:1310.8635v1, 2013), Open Question 3.6, explicitly asks whether some residue is absent modulo some power of three, after noting none had been found. Burns (arXiv:1703.02705, 2017) establishes all residues modulo primes \(p\ge5\), not powers of three. Rampersad--Shallit (Electronic Journal of Combinatorics 29(3), 2022, #P3.36) treats automata and pattern phenomena for these sequences, principally modulo primes, without a covering power-of-three surjectivity theorem in the inspected text. The present result uses a different 3-adic block-multiplication mechanism and settles the power-of-three existence question independently of automaton construction.

## Limitations
No estimates for the least witnessing index or density in individual residue classes are asserted. The proof uses an infinite-subsequence pigeonhole choice and hence is not algorithmically efficient. The novelty comparison covers accessible published texts and mathematical-results searches, not every unindexed or inaccessible paper; an earlier equivalent statement cannot be excluded without external review. Independent mathematical audit has not been performed.

## References
1. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(3^k\) behaviour of recursive sequences*, arXiv:1308.2856v1 (first posted 2013-08-13), Section 12.
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635v1 (2013-10-31), Journal de Théorie des Nombres de Bordeaux 27 (2015), 245–288, Open Question 3.6.
3. R. Burns, *The Catalan numbers have no forbidden residue modulo primes*, arXiv:1703.02705 (2017).
4. N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, Electronic Journal of Combinatorics 29(3) (2022), #P3.36, DOI 10.37236/10799.
5. E. E. Kummer, classical carry theorem for valuations of binomial coefficients (1852).
