# Sharp high-index nilpotency gaps in regular Jordan lifts over truncated local rings

## Finding
Let \(k=\mathbb F_q\) be any finite field, \(e\geq3\), \(m\geq2\), and \(R=k[\varepsilon]/(\varepsilon^e)\). Let \(J_m\) have ones immediately below the main diagonal and zeros elsewhere. Consider all matrices \(A\in M_m(R)\) whose reduction modulo \(\varepsilon\) is \(J_m\). Write their characteristic polynomials uniquely as
\[
f_A(T)=T^m-\sum_{h=1}^{e-1}\varepsilon^h a_h(T),\qquad a_h(T)\in k[T],\quad \deg a_h<m.
\]
Define \(v(A)=\operatorname{ord}_T a_1(T)\), with \(v(A)=m\) when \(a_1=0\). Denote by \(\nu(A)\) the least positive integer \(N\) with \(A^N=0\). Then:

1. If \((e-1)v(A)<m\), exactly
\[
\nu(A)=em-(e-1)v(A).
\]
If \((e-1)v(A)\geq m\), then \(\nu(A)\leq(e-1)m\).
2. The possible indices strictly above \((e-1)m\) are **exactly**
\[
\{em-(e-1)v:0\leq v\leq \lfloor(m-1)/(e-1)\rfloor\}.
\]
Each listed index occurs. In particular, for \(e\geq3\) there are systematic forbidden intermediate indices in this high tail.
3. For every integer \(v\) in that displayed range, the number of matrices attaining index \(em-(e-1)v\) is
\[
(q-1)q^{(e-1)m^2-v-1}.
\]
The remaining \(q^{(e-1)m^2-\lceil m/(e-1)\rceil}\) lifts have index at most \((e-1)m\). The maximum-index proportion is therefore \(1-q^{-1}\), independently of \(m,e\).

## Assumptions and scope
The coefficient ring is the commutative truncated polynomial ring \(R=\mathbb F_q[\varepsilon]/(\varepsilon^e)\), where \(e\geq3\). No characteristic restriction is imposed. All \(q^{(e-1)m^2}\) lifts of the fixed lower-shift regular nilpotent matrix are counted individually, rather than by similarity class. The nilpotency index of the zero matrix is one. For arbitrary lifts the index lies in \([m,em]\); the theorem determines only the strict high tail \(\nu>(e-1)m\) and its complementary cardinality, not the separate lower-index multiplicities.

## Proof
**Cyclic reduction.** For each lift \(A\), the ordered vectors \(u,Au,\ldots,A^{m-1}u\), with \(u\) the first standard basis vector, reduce modulo \(\varepsilon\) to the standard basis. The matrix \(U_A\) with these columns is invertible over the local ring, lies in \(K=1+\varepsilon M_m(R)\), and conjugates \(A\) to multiplication by \(T\) in the monic companion module
\[
S_A=R[T]/(f_A(T)).
\]
The elements \(1,T,\ldots,T^{m-1}\) form an \(R\)-basis of \(S_A\). Conversely, every polynomial \(T^m-\sum_{h=1}^{e-1}\varepsilon^h a_h(T)\), with \(\deg a_h<m\), has a companion matrix reducing to \(J_m\). Thus characteristic-polynomial coefficients parameterize the \(K\)-conjugacy orbits of these lifts.

**Uniform fibers.** The kernel \(K\) of reduction \(\operatorname{GL}_m(R)\to\operatorname{GL}_m(k)\) has order \(q^{(e-1)m^2}\). Since the companion module is cyclic, its full matrix centralizer is \(S_A\) acting by multiplication; its subgroup reducing to the identity is \(1+\varepsilon S_A\), of order \(q^{(e-1)m}\). Therefore every coefficient tuple \((a_1,\ldots,a_{e-1})\) corresponds to precisely
\[
|K|/|1+\varepsilon S_A|=q^{(e-1)(m^2-m)}
\]
matrices. In particular, \(a_1\) is uniform in the \(m\)-dimensional space \(k[T]_{<m}\).

**The high-power identity.** In \(S_A\), the defining relation gives \(T^m=\varepsilon a_1(T)+\varepsilon^2a_2(T)+\cdots+\varepsilon^{e-1}a_{e-1}(T)\). Raising both sides to the \((e-1)\)-st power, each term using any factor of order at least \(\varepsilon^2\) vanishes. Hence, for every \(j\geq0\),
\[
T^{(e-1)m+j}=\varepsilon^{e-1}T^j a_1(T)^{e-1}.
\]
As \(S_A\) is a free \(R\)-module on powers \(T^0,\ldots,T^{m-1}\), reduction of the right-hand polynomial modulo \(T^m\) determines whether it vanishes: multiplication by \(\varepsilon^{e-1}\) kills all terms containing any factor \(\varepsilon\), and each remaining coefficient in \(k\) survives. The reduction modulo \(\varepsilon\) of \(S_A\) is \(k[T]/(T^m)\). Thus the right-hand side is nonzero if and only if
\[
j+(e-1)\operatorname{ord}_T(a_1)<m.
\]
When \((e-1)v<m\), the last nonzero power has degree \(em-(e-1)v-1\), proving the formula for \(\nu\); when \((e-1)v\geq m\), the power \(A^{(e-1)m}\) already vanishes. All lifts are nilpotent since \(A^m\in\varepsilon M_m(R)\), hence \(A^{em}=0\).

**Counting and sharpness.** For \(0\leq v<m\), exactly \((q-1)q^{m-v-1}\) polynomials \(a_1\in k[T]_{<m}\) have \(T\)-adic order \(v\), and the remaining \(e-2\) coefficient polynomials have \(q^{(e-2)m}\) choices. Multiplication by the uniform fiber size yields
\[
(q-1)q^{m-v-1+(e-2)m+(e-1)(m^2-m)}=(q-1)q^{(e-1)m^2-v-1}.
\]
Every \(v\) in the indicated high-tail range is realized, by choosing \(a_1=T^v\) and all other coefficient polynomials zero. The complement is characterized by the first \(\lceil m/(e-1)\rceil\) coefficients of \(a_1\) all vanishing, which happens for the stated \(q\)-power fraction of lifts. This proves every assertion.

## Verification
Run the accompanying dependency-free `verify.py` with `python3 verify.py`; its final output line is `HIGH_TAIL_OK`. It enumerates every companion polynomial in seven small prime-field instances, including ring lengths \(3,4,5\), and independently tests 750 full matrix lifts using exact truncated-coefficient multiplication. Those finite checks support the symbolic proof but do not replace it. The theorem itself holds for every prime power \(q\) and all admissible \(m,e\).

## Relationship to prior work
Avni, Onn, Prasad, and Vaserstein (arXiv:0708.1608, 2007) treat similarity over local principal ideal rings of arbitrary length, explicitly recalling that cyclic matrices admit companion forms. This is an antecedent of the cyclic-reduction step; their similarity-class and class-count statements do not supply the present high nilpotency-index valuation criterion or the sharp arithmetic-progression multiplicities for arbitrary \(e,m\). Prasad, Singla, and Spallone (arXiv:1212.6157, 2012) analyze similarity and centralizers over rings **of length two**. The published dual-number Jordan-lift distribution of 2026 also concerns \(e=2\); it gives consecutive indices, whereas the current \(e\geq3\) result shows high-tail gaps. The exact statements and the different ring-length hypotheses were compared; the elementary companion principle is not claimed as new.

## Limitations
The theorem does not determine the exact distribution of indices at or below \((e-1)m\), where the higher coefficient polynomials may affect cancellations. It concerns lifts of one regular nilpotent block and the specific equal-characteristic truncated coefficient ring, not general noncyclic reductions or mixed-characteristic rings. The exhaustive finite tests address selected small prime fields only. Literature comparison was bounded, and publication priority is not independently certified.

## References
1. Nir Avni, Uri Onn, Amritanshu Prasad, Leonid Vaserstein, *Similarity Classes of \(3\times3\) Matrices over a Local Principal Ideal Ring*, arXiv:0708.1608 (first public 2007-08-12), especially Sections 1.2 and 2.1. https://arxiv.org/abs/0708.1608
2. Amritanshu Prasad, Pooja Singla, Steven Spallone, *Similarity of Matrices over Local Rings of Length Two*, arXiv:1212.6157 (first public 2012-12-26), especially Sections 1 and 6. https://arxiv.org/abs/1212.6157
3. *Exact Nilpotency-Index Distribution for Jordan Lifts over Finite Dual Numbers*, public 2026 research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7
