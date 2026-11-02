# Exact two-adic quotient-set closure for every odd-parameter Lucas companion

## Finding
For **every odd integer** \(P\), define the companion Lucas sequence by
\[
V_0=2,\qquad V_1=P,\qquad V_{n+2}=PV_{n+1}+V_n\quad(n\ge0).
\]
For \(A_P=\{V_n:n\ge1\}\), form its ratio set \(R_P=\{V_m/V_n:m,n\ge1\}\subset\mathbb Q\). Then its exact closure in the two-adic field is
\[
\boxed{\overline{R_P}^{\,\mathbb Q_2}=\bigcup_{j=-2}^{2}2^j\mathbb Z_2^\times
=\{z\in\mathbb Q_2^\times:-2\le\nu_2(z)\le2\}.}
\]
In particular, **every point in all five valuation shells is approximated**, while \(0\) and every point of any other shell are excluded. A complementary exact valuation law is
\[
\nu_2(V_n)=\begin{cases}
0,&3\nmid n,\\
1,&6\mid n,\\
2,&n\equiv3\pmod6,
\end{cases}\qquad n\ge1.
\]
The uniform statement concerns every odd \(P\); the classical case \(P=1\) is already substantially implied by published Lucas-residue tables and is not claimed as a novel stand-alone case.

## Assumptions and scope
The parameter \(P\) is any odd, possibly negative, integer; indices in \(A_P\) are positive. All sequence terms are nonzero by the valuation law. The topology, units and valuation are those of \(\mathbb Q_2\), with \(\mathbb Z_2^\times=\{u\in\mathbb Z_2:\nu_2(u)=0\}\). A closure is taken in \(\mathbb Q_2\), **not** in \(\mathbb R\). No assertion is made for even \(P\) or for general second recurrence coefficient.

## Proof
**1. Matrix identities and the valuation law.** Put \(M=\begin{pmatrix}P&1\\1&0\end{pmatrix}\), so \(\det M=-1\) and the characteristic identity gives \(M^2=PM+I\). Thus \(V_n=\operatorname{tr}(M^n)\) for all \(n\ge0\), including the two prescribed initial values. Modulo \(2\), since \(P\) is odd, \(M\) is the Fibonacci companion matrix and \(M^3\equiv I\pmod2\). Consequently \(V_n\) is odd precisely when \(3\nmid n\).

Moreover \(M^3=PI+(P^2+1)M\). Since \(P^2\equiv1\pmod8\), squaring yields
\[
M^6\equiv P^2I+4PM+4M^2\equiv 5I\pmod8.
\]
Also \(V_3=P(P^2+3)\equiv4\pmod8\). For \(n\equiv3\pmod6\), write \(n=3+6t\); then
\(V_n\equiv5^tV_3\equiv4\pmod8\), whence \(\nu_2(V_n)=2\).
For positive \(n=2m\) divisible by \(6\), \(3\mid m\), hence \(V_m\) is even. The trace/determinant duplication identity
\[
V_{2m}=V_m^2-2(-1)^m
\]
then shows \(V_{2m}\equiv2\pmod4\), so its valuation is \(1\). The remaining indices have odd terms and valuation \(0\). All valuations lie in \(\{0,1,2\}\) and all three occur, at indices \(1,6,3\) respectively.

**2. A universal scalar lifting congruence.** For all integers \(k\ge2\),
\[
M^{3\cdot2^{k-1}}\equiv(1+2^k)I\pmod{2^{k+1}}.\tag{1}
\]
The case \(k=2\) is \(M^6\equiv5I\pmod8\). If the congruence holds at \(k\), write its left side as \((1+2^k)I+2^{k+1}B\) for an integral matrix \(B\). Its square equals \((1+2^k)^2I\pmod{2^{k+2}}\), since the cross term is a multiple of \(2^{k+2}\). Because \(k\ge2\), \((1+2^k)^2\equiv1+2^{k+1}\pmod{2^{k+2}}\). This proves (1) inductively.

Taking traces after multiplying (1) by \(M^n\) gives, whenever \(V_n\) is odd,
\[
V_{n+3\cdot2^{k-1}}\equiv(1+2^k)V_n
\equiv V_n+2^k\pmod{2^{k+1}}.\tag{2}
\]
Thus a positive-index odd term representing any odd residue modulo \(2^k\) has another positive-index odd term representing the **opposite next binary digit**. Both reductions retain the old residue.

**3. All two-adic units occur in the closure of odd terms.** Modulo \(4\), if \(P\equiv1\), the terms \(V_1=P\) and \(V_2=P^2+2\) yield respectively \(1\) and \(3\). If \(P\equiv3\), the terms \(V_1=P\) and \(V_5=P^5+5P^3+5P\equiv3P\pmod4\) yield respectively \(3\) and \(1\). Therefore every odd residue occurs modulo \(4\). Applying (2) inductively for \(k=2,3,\ldots\) shows that for **every** \(k\ge1\) and every odd residue \(u\pmod{2^k}\), a positive-index \(V_n\) equals \(u\) modulo \(2^k\). Hence the set of odd terms is dense in \(\mathbb Z_2^\times\).

**4. Exact closure of ratios.** The valuation law gives \(-2\le\nu_2(V_m/V_n)\le2\) for every positive \(m,n\). The union \(\bigcup_{j=-2}^2 2^j\mathbb Z_2^\times\) is a finite union of closed valuation shells in \(\mathbb Q_2\); in particular its closure still excludes \(0\).

Conversely, fix terms \(c_0=V_1\), \(c_1=V_6\), \(c_2=V_3\), of exact valuations \(0,1,2\). As odd sequence terms \(u\) vary densely through the unit group, the quotients \(c_j/u\) for \(j=0,1,2\) are dense in shells of valuations \(0,1,2\) respectively, because inversion and multiplication by a fixed nonzero scalar are homeomorphisms. Similarly \(u/c_j\), \(j=1,2\), are dense in shells of valuations \(-1,-2\). These quotients are elements of \(R_P\). Together with the closed-set upper bound, this proves the stated identity.

## Verification
The accompanying standalone `verify.py` independently computes recurrence residues modulo \(2^k\), matrix powers, and valuations. For sixteen odd parameters from \(-15\) to \(15\), it tests every odd residue for \(k=1,\ldots,11\), the scalar lifting congruence through \(k=12\), and valuation formulas for indices \(1\le n\le510\). All tests completed successfully. These finite checks are diagnostic; the proof of the infinite result is the matrix argument above.

## Relationship to prior work
Garcia, Hong, Luca, Pinsker, Sanna, Schechter and Starr (2017), Theorem 7.2(a), prove **non-density** of the classical Lucas ratio set in \(\mathbb Q_2\), using a valuation obstruction; their statement gives no complete closure and does not treat every odd parameter. Antony and Barman (2022 preprint; 2023 publication) study density criteria for linear-recurrence ratio sets, including second-order companion sequences, but their applicable statements decide density rather than the exact five-shell closure. Bundschuh and Bundschuh (2010), Theorem 2, calculate every residue frequency modulo powers of \(2\) for **the classical sequence \(P=1\)**. That result supplies a stronger prior classification of the single-parameter residue distribution and implies the classical specialization after an elementary ratio-set argument: this specialization is **not** claimed as original by itself. Carlip and Jacobson (1996), Theorem 1.1, study distributions modulo powers of \(2\) for the **first-kind sequence with initial values \(0,1\)**, not the second-kind companion \(2,P\); their indexed theorem is not a direct classification of the current ratio sets. Southwick (2014) studies complete residue systems for the classical and Gibonacci sequences; that is a distinct notion from the exact closure of ratios for every odd companion parameter. The contribution here is the **uniform all-odd-parameter exact closure**, with a direct matrix lift proving the needed unit-residue coverage.

## Limitations
The theorem does not classify even parameters, other second recurrence coefficients, or the real closure of the quotient set. A finite computation cannot prove the infinite claim. Priorities remain sensitive to unindexed descriptions of second-kind Lucas-companion residue distributions, especially possible deductions from older recurrence-distribution papers; novelty here is asserted only for the full uniform closure, not for its classical specialization.

## References
1. D. Antony and R. Barman, *p-Adic quotient sets: linear recurrence sequences*, arXiv:2207.07084v1, submitted 14 July 2022; updated 2022. https://arxiv.org/abs/2207.07084
2. S. R. Garcia, Y. X. Hong, F. Luca, E. Pinsker, C. Sanna, E. Schechter, A. Starr, *p-Adic quotient sets*, Acta Arithmetica 179 (2017), 163–184, Theorem 7.2. https://doi.org/10.4064/aa8579-4-2017
3. P. Bundschuh and R. Bundschuh, *The sequence of Lucas numbers is not stable modulo 2 and 5*, Uniform Distribution Theory 5 (2010), 113–130, Theorem 2. https://pcwww.liv.ac.uk/~karpenk/JournalUDT/vol05/no2/6Bundsch10-2.pdf
4. W. Carlip and E. Jacobson, *On the stability of certain Lucas sequences modulo powers of 2*, Fibonacci Quarterly 34 (1996), 298–305, Theorem 1.1. https://www.fq.math.ca/Scanned/34-4/carlip.pdf
5. J. T. Southwick, *The Lucas numbers and other Gibonacci sequences mod m*, arXiv:1402.0598v1 (2014). https://arxiv.org/abs/1402.0598
