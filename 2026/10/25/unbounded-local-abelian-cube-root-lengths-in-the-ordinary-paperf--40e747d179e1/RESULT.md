# Unbounded local Abelian-cube root lengths in the ordinary paperfolding word

## Finding
Define the binary paperfolding word \(p=p_0p_1\cdots\) by \(p_i=1\) when the odd part of \(i+1\) is \(1\pmod 4\), and \(p_i=0\) when it is \(3\pmod 4\). (Complementing every bit gives the common alternative convention.) A length-\(m\) Abelian cube at position \(i\) is a concatenation of three consecutive length-\(m\) factors starting there, all with identical Parikh vectors.

For every integer \(k\ge1\), define
\[
 i_k=\frac{2(4^k-1)}3,\qquad L_k=\frac{4^k-1}3.
\]
No Abelian cube begins at \(i_k\) with root length in
\[
 1\le m\le \left\lfloor\frac{L_k}{3}\right\rfloor
 =\left\lfloor\frac{4^k-1}{9}\right\rfloor.
\]
Thus the least possible root length of a three-block Abelian power has no uniform bound over all starting positions. If no cube begins at a position, its least root is understood to be infinite. Every Abelian power with four or more blocks begins with an Abelian cube, so the same obstruction holds for every fixed exponent at least three.

## Assumptions and scope
For any positive integer \(n\), write \(\operatorname{odd}(n)=n/2^{\nu_2(n)}\). For any odd integer \(u\), let \(\chi(u)=1\) for \(u\equiv1\pmod4\) and \(\chi(u)=-1\) for \(u\equiv3\pmod4\). The signed paperfolding word is \(2p_i-1=\chi(\operatorname{odd}(i+1))\). All indices, roots, and block lengths in the theorem are integers. The result concerns this ordinary one-sided paperfolding sequence and its bit complement; no statement is made for other folding-instruction sequences.

An Abelian cube of binary blocks is equivalent to the equality of their signed sums. This equivalence uses the requirement that all three blocks have the same length.

## Proof
**1. An auxiliary infinite word and its prefix deficit.** Set
\[
 a_j=-\chi(\operatorname{odd}(3j+1))\in\{-1,1\},\qquad
 P(n)=-\sum_{j=0}^{n-1}a_j,\qquad P(0)=0.
\]
The odd-part definition gives, for every \(n\ge0\),
\[
 a_{4n}=-1,\quad a_{4n+1}=a_n,\quad
 a_{4n+2}=1,\quad a_{4n+3}=-(-1)^n.
\]
Indeed \(3(4n+r)+1\) equals \(12n+1\), \(4(3n+1)\), \(12n+7\), and \(2(6n+5)\) for \(r=0,1,2,3\), respectively. Summing a four-symbol block therefore yields, with \(\varepsilon(n)=n\bmod2\),
\[
\begin{aligned}
P(4n)&=P(n)+\varepsilon(n),\\
P(4n+1)&=P(n)+\varepsilon(n)+1,\\
P(4n+2)&=P(n+1)+\varepsilon(n)+1,\\
P(4n+3)&=P(n+1)+\varepsilon(n).
\end{aligned}
\tag{1}
\]
These recurrences and \(P(0)=0\) imply by strong induction \(P(n)\ge1\) for every \(n\ge1\). They also show that \(P(n)=1\) precisely at
\[
 m_j=\frac{2\cdot4^j+1}{3},\qquad j\ge0.
\tag{2}
\]
For completeness: \(P(1)=1\); a larger index with \(P=1\) cannot be even, and cannot have residue \(1\pmod4\). An index \(4n+3\) has \(P=1\) exactly when \(n\) is even and \(P(n+1)=1\). Therefore successive equality indices satisfy \(m_{j+1}=4m_j-1\), which solves to (2).

**2. A threefold-scale inequality.** Put \(\delta(n)=P(n+1)-P(n)=-a_n\in\{-1,1\}\) and
\[
 Q(n)=P(3n)-2P(n).
\]
From (1), using \(\varepsilon(3n)=\varepsilon(n)\), one obtains
\[
\begin{aligned}
Q(4n)&=Q(n)-\varepsilon(n),\\
Q(4n+1)&=Q(n)+\delta(3n)-\varepsilon(n)-2,\\
Q(4n+2)&=Q(n+1)-\delta(3n+2)-3\varepsilon(n),\\
Q(4n+3)&=Q(n+1)-\delta(3n+2)+1-\varepsilon(n).
\end{aligned}
\tag{3}
\]
Crucially,
\[
 n\equiv2\pmod4\quad\Longrightarrow\quad
 \delta(3n+2)=1,
\tag{4}
\]
because then \(3n+2\) is a multiple of four and \(a_{4h}=-1\).

We prove simultaneously by strong induction
\[
 Q(n)\le
 \begin{cases}
 0,& n\equiv0,2\pmod4,\\
 -1,& n\equiv1\pmod4,\\
 1,& n\equiv3\pmod4.
 \end{cases}
\tag{5}
\]
The case \(n=0\) is immediate. For a target \(4n\), if \(n\) is even then \(Q(n)\le0\), while if \(n\) is odd then \(Q(n)\le1\) and \(\varepsilon(n)=1\); the first relation in (3) gives the required bound. For \(4n+1\), the second relation and \(\delta\le1\) give at most \(-1\), both when \(n\) is even and when \(n\) is odd. For \(4n+2\) with \(n\) odd, \(n+1\) is even, so the third relation gives at most \(0+1-3\le0\). For \(n\equiv0\pmod4\), \(Q(n+1)\le-1\) and \(-\delta\le1\), giving at most zero. For \(n\equiv2\pmod4\), (4) and \(Q(n+1)\le1\) likewise give at most zero. Finally, for \(4n+3\) and \(n\) odd the last relation gives at most \(0+1=1\); for \(n\equiv0\pmod4\), it gives at most \(-1+1+1=1\); and for \(n\equiv2\pmod4\), (4) gives at most \(1-1+1=1\). All right-hand indices in (3) are smaller than the target, except for the separately initialized index zero. Hence (5) follows. In particular,
\[
 P(3m)-2P(m)=Q(m)\le1\qquad(m\ge1).
\tag{6}
\]

**3. No Abelian cube is a prefix of \(a\).** If the first three length-\(m\) blocks of \(a\) had the same signed sum, then
\[
 P(2m)=2P(m),\qquad P(3m)=3P(m).
\]
Thus \(Q(m)=P(m)\ge1\). Inequality (6) forces \(P(m)=1\); by (2), \(m=m_j\) for some \(j\ge0\). If \(j=0\), then \(m=1\) and \(P(3)=1\ne3P(1)\). For \(j\ge1\), let \(b_j=2m_j\). Since \(b_0=2\), \(b_{j+1}=4(b_j-1)+2\), and every \(b_j-1\) is odd, equation (1) shows
\[
 P(2m_j)=P(b_j)=2j+2\ne2P(m_j)=2.
\]
This rules out every possible root length \(m\ge1\).

**4. Long prefixes reappear at explicit starting positions.** Fix \(k\ge1\) and write \(i_k=2(4^k-1)/3\), \(L_k=(4^k-1)/3\). For \(0\le j<L_k\), let \(t_j=3j+1\), so \(1\le t_j<4^k\). With \(n=i_k+j+1\), we have
\[
 3n=2\cdot4^k+t_j.
\]
Because \(\nu_2(t_j)\le2k-1\), removing the common power of two leaves the two terms with the same odd residue modulo four. Therefore
\[
 \chi(\operatorname{odd}(3n))=\chi(\operatorname{odd}(t_j)).
\]
Multiplication by the odd integer three flips \(\chi\), so
\[
 2p_{i_k+j}-1=\chi(\operatorname{odd}(n))
 =-\chi(\operatorname{odd}(t_j))=a_j.
\]
The length-\(L_k\) factor of the ordinary paperfolding word starting at \(i_k\) is consequently the length-\(L_k\) prefix of \(a\), after changing \(-1,1\) to binary symbols. If it contained an Abelian cube with root \(m\le\lfloor L_k/3\rfloor\) at its first position, the auxiliary word would have an Abelian cube prefix of the same root, contradicting step 3. Since \(L_k\to\infty\), the stated uniform-root obstruction follows. A higher Abelian power contains an Abelian cube in its first three blocks, so the same conclusion holds for every exponent at least three.

## Verification
The standalone `verify.py` implements the binary paperfolding symbols by both the odd-part formula and a separate divide-by-two recursion. It evaluates the auxiliary prefix sums directly and verifies (1), the equality cases (2), the residue-refined inequality (5), and the nonexistence of Abelian cube prefixes across all roots testable in an explicit finite range. It separately verifies the matching windows at the exact positions \(i_k\) for \(1\le k\le8\), directly comparing the three block populations for every root covered by the theorem. Running `python verify.py` requires only the Python standard library. The infinite claims are proved in steps 1–4; these finite checks are consistency tests, not substitutes for induction.

## Relationship to prior work
Holub, *Abelian powers in paper-folding words* (2012), Theorem 8, constructs Abelian powers of arbitrarily large order **somewhere** in each paperfolding word. His proof varies both starting position and root length. This does not imply that small-root cubes occur at every position, nor does it imply their impossibility at a specific sequence of starts. The present theorem demonstrates that the former uniform local assertion is false, with explicit quantitative obstructions.

Madill and Rampersad, *The abelian complexity of the paperfolding word* (2012), compute the global spectrum of Parikh vectors at each factor length and its \(2\)-regularity. Their Proposition 3 features lengths of the form \((2\cdot4^j+1)/3\), but counts **possible factors**, not consecutive equal-Parikh triples at prescribed starts. Their statement neither supplies the auxiliary inequality (5) nor rules out local cubes. Their paper uses the bit-complement convention, which does not affect Abelian cubes.

Fici and collaborators' analysis of Abelian powers at individual positions in Sturmian words (2015) supplies related motivation but concerns a different class of words and does not yield paperfolding bounds. A published paperfolding prefix-normal-defect result concerns extremal counts of ones in factors versus prefixes; that imbalance is distinct from three contiguous equal-Parikh blocks. No implication covering the present conclusion was found in the inspected statements.

## Limitations
The theorem does not say that every starting position supports an Abelian cube, nor does it determine the least root above the stated obstruction at \(i_k\). It does not apply directly to arbitrary paperfolding instruction sequences. The finite verifier cannot establish the infinite theorem by computation alone. Exhaustive historical priority cannot be certified: differently phrased or unindexed statements could exist, and independent review remains outstanding.

## References
1. Š. Holub, "Abelian powers in paper-folding words," arXiv:1207.3585 (first public version 2012-07-16), *Journal of Combinatorial Theory A* 120 (2013), 872–881. https://arxiv.org/abs/1207.3585
2. B. Madill and N. Rampersad, "The abelian complexity of the paperfolding word," arXiv:1208.2856 (first public version 2012-08-14). https://arxiv.org/abs/1208.2856
3. G. Fici, A. Langiu, T. Lecroq, A. Lefebvre, F. Mignosi, J. Peltomäki, and É. Prieur-Gaston, "Abelian powers and repetitions in Sturmian words," arXiv:1506.02797 (first public version 2015-06-09). https://arxiv.org/abs/1506.02797
4. "Unbounded prefix-normal defect of the ordinary paperfolding word," public research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-unbounded-prefix-normal-defect-of-the-ordinary-paperfolding-word--a7708413f1f3
