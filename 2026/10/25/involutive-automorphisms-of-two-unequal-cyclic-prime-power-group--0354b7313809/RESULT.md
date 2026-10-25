# Involutive automorphisms of two unequal cyclic prime-power groups: a sharp exponent-gap law

## Finding
Let \(p\) be a prime, let \(1\le a<b\) be integers, put \(h=b-a\), and define
\[
G_{p;a,b}=C_{p^a}\oplus C_{p^b},\qquad
I_{p;a,b}=\#\{\varphi\in\operatorname{Aut}(G_{p;a,b}):\varphi^2=\mathrm{id}\}.
\]
The exact order-dividing-two automorphism census is
\[
\boxed{I_{p;a,b}=2+2p^{2a}\quad\text{if }p\text{ is odd}.}
\]
For \(p=2\), define the exponent-gap factor
\[
\eta(h)=\begin{cases}3,&h=1,\\4,&h=2,\\5,&h\ge3.\end{cases}
\]
Then
\[
\boxed{
I_{2;a,b}=\begin{cases}
6,&a=1,\ h=1,\\
12,&a=1,\ h=2,\\
16,&a=1,\ h\ge3,\\
4^a\eta(h),&a=2,\\
4^a\eta(h)+32,&a\ge3.
\end{cases}}
\]
Thus the count stabilizes exactly once the exponent gap reaches three in the binary case, and is independent of the larger exponent for every odd prime. The identity is included; the number of elements of *exact* order two in the automorphism group is \(I_{p;a,b}-1\).

## Assumptions and scope
All groups are finite abelian groups written additively. The primary structural hypothesis is the strict inequality \(a<b\); equal exponents are excluded. The notation \(C_{p^a}\) denotes a cyclic group of order \(p^a\). No field, characteristic-zero assumption, or extra restriction on the prime is imposed.

Every automorphism has the unique matrix form
\[
\varphi=\begin{pmatrix}u&v\\p^h w&z\end{pmatrix},\qquad
u,v,w\in\mathbb Z/p^a\mathbb Z,
\quad z\in\mathbb Z/p^b\mathbb Z,
\]
where \(u\) and \(z\) are units in their respective rings. These parameters specify the images of the two standard generators. The nonunit lower-left entry is forced by the difference of the cyclic exponents. Reducing the induced map modulo \(p\) shows that invertibility is equivalent to \(u\) and \(z\) being units.

## Proof
**1. The involution equations.** Square the generator images in the displayed matrix. Precisely the following four congruences characterize \(\varphi^2=\mathrm{id}\):
\[
\begin{aligned}
u^2+p^h vw&\equiv1\pmod{p^a},\\
z^2+p^h vw&\equiv1\pmod{p^b},\\
(u+z)v&\equiv0\pmod{p^a},\\
(u+z)w&\equiv0\pmod{p^a}.
\end{aligned}
\tag{1}
\]
All subsequent counts concern exactly these equations.

**2. Odd primes.** Assume \(p\) odd. As multiplication by \(2\) is invertible on \(G_{p;a,b}\), an involutive automorphism \(\varphi\) has canonical complementary idempotent projectors \((1+\varphi)/2\) and \((1-\varphi)/2\). Hence
\[
G_{p;a,b}=G^+\oplus G^-,\qquad \varphi|_{G^+}=+1,\quad \varphi|_{G^-}=-1.
\]
Conversely every ordered internal direct-sum decomposition gives exactly one such involution. Uniqueness of the elementary divisors of finite abelian groups implies that the two distinct cyclic direct summands \(C_{p^a}\) and \(C_{p^b}\) can be assigned independently to the plus and minus factors. There are four assignment types. The all-plus and all-minus types each give one automorphism. For either mixed type, the automorphism group acts transitively on ordered decompositions of that type, with stabilizer \(\operatorname{Aut}(C_{p^a})\times\operatorname{Aut}(C_{p^b})\). The matrix form yields
\[
|\operatorname{Aut}(G_{p;a,b})|=
\varphi(p^a)\varphi(p^b)p^{2a},
\]
where \(\varphi\) on the right denotes Euler's totient function. Each mixed orbit therefore has \(p^{2a}\) elements, proving \(I_{p;a,b}=2+2p^{2a}\).

**3. A binary square-root lemma.** Now let \(p=2\). For \(b\ge3\), an odd residue \(t\pmod{2^b}\) has exactly four square roots if \(t\equiv1\pmod8\) and none otherwise. Indeed the squaring homomorphism on the unit group modulo \(2^b\) has kernel of size four and image exactly the subgroup \(1\pmod8\). For \(b=2\), every odd square equals one modulo four and has two odd square roots.

Fix \(v,w\pmod{2^a}\), and put \(t=1-2^h vw\). The second congruence of (1) says \(z^2=t\pmod{2^b}\). For any such \(z\), the first congruence holds exactly when \(u^2=z^2\pmod{2^a}\). Since \(z\) is odd, write \(u=rz\pmod{2^a}\), with \(r^2\equiv1\pmod{2^a}\). The remaining two conditions become
\[
(1+r)v=(1+r)w=0\pmod{2^a}.\tag{2}
\]
For \(b\ge3\), the permitted ordered pairs \((v,w)\) must satisfy
\[
\begin{array}{c|c}
h & \text{square-root condition}\\\hline
1 & 4\mid vw\\
2 & 2\mid vw\\
\ge3 & \text{no restriction}.
\end{array}\tag{3}
\]
Every admissible triple \((r,v,w)\) with (2) and (3) produces exactly four choices of \(z\) and then a unique \(u\). This parameterization counts each automorphism exactly once.

**4. Binary count for \(a\ge3\).** The four solutions to \(r^2=1\pmod{2^a}\) are
\[
r\in\{-1,\,-1+2^{a-1},\,1,\,1+2^{a-1}\}\pmod{2^a}.
\]
For \(r=-1\), (2) is automatic; among all \(4^a\) ordered pairs \((v,w)\), the counts satisfying (3) for \(h=1,2,\ge3\) are, respectively,
\[
2^{2a-1},\qquad 3\cdot2^{2a-2},\qquad 2^{2a}.
\]
For \(r=-1+2^{a-1}\), condition (2) says both \(v\) and \(w\) are even. The count is \(2^{2a-2}\) in each gap regime; all such pairs satisfy (3). For either \(r=1\) or \(r=1+2^{a-1}\), condition (2) forces each of \(v,w\) to lie in \(\{0,2^{a-1}\}\). There are four ordered pairs per root, and every one meets (3). Consequently, before choosing \(z\), the three gap-regime totals are
\[
3\cdot2^{2a-2}+8,\quad 4\cdot2^{2a-2}+8,\quad5\cdot2^{2a-2}+8.
\]
Multiplying by the four choices of \(z\) gives \(3\cdot4^a+32\), \(4\cdot4^a+32\), and \(5\cdot4^a+32\).

**5. Binary boundary \(a=2\).** The roots of \(r^2=1\pmod4\) are \(r=\pm1\). For \(r=-1\), the numbers of admissible \((v,w)\) in the three gap regimes are \(8,12,16\). For \(r=1\), both \(v,w\) must be even modulo four, giving four admissible pairs in every regime. Multiplication by four square roots \(z\) yields \(48,64,80\), respectively, equal to \(4^2\eta(h)\).

**6. Binary boundary \(a=1\).** The sole root \(r^2=1\pmod2\) is \(r=1\); congruence (2) imposes no condition. If \(h=1\), then \(b=2\), and \(z^2=1-2vw\pmod4\) has two roots for exactly three of the four binary pairs \((v,w)\), giving six automorphisms. If \(h=2\), then \(b=3\), and precisely three pairs have \(vw\) even, giving twelve. If \(h\ge3\), all four pairs are permitted and each admits four roots, giving sixteen. This completes the proof.

## Verification
The accompanying `involution_verify.py` enumerates all unit diagonal entries and all off-diagonal homomorphism parameters for 27 finite instances. Instead of applying the square-root argument, it squares the images of both cyclic generators and tests identity directly. Representative predictions include
\[
I_{2;1,2}=6,\quad I_{2;2,3}=48,\quad I_{2;3,6}=352,\quad I_{3;1,2}=20,\quad I_{5;1,2}=52.
\]
All 27 tested instances agreed with the formulas; the terminal marker is `RANK_TWO_INVOLUTION_CENSUS_OK 27_cases`. The general theorem is established by the proof rather than by finite enumeration.

## Relationship to prior work
Hillar and Rhea give a general matrix description and group-order formula for automorphisms of finite abelian groups (2006). Mader develops a broader structural description of automorphism groups of finite abelian prime-power groups (2012). Neither source states an exact rank-two count of automorphisms whose square is the identity.

Hage and Harju (2007, Section 3) count involutions on *cyclic* groups; their Section 4 proves a decomposition property for involutions on direct products while explicitly observing that enumeration of involutions on a product does not follow simply from the numbers on its factors. Their report therefore motivates exactly the type of product census treated here without supplying the displayed mixed-exponent formulas.

Hayat, López-Aguayo, and Abbas (2018) count automorphisms according to the cardinalities of their fixed-point sets. That statistic does not count order-dividing-two automorphisms: an automorphism of order greater than two may have the same fixed-point cardinality as an involution, while involutions can have different fixed-point cardinalities. Previously published fixed-point layers for unequal cyclic factors likewise do not imply the present count.

## Limitations
The formula assumes unequal cyclic exponents, so it does not count involutions of the full matrix group \(\operatorname{GL}_2(\mathbb Z/p^a\mathbb Z)\) occurring when \(a=b\). It concerns rank two, and does not classify individual conjugacy classes or involution fixed-point profiles. While the closest directly relevant full papers were inspected, an equivalent formula could exist in unindexed finite-group literature or follow from a more general classification of modular representations of the cyclic group of order two.

## References
1. C. J. Hillar and D. L. Rhea, “Automorphisms of finite Abelian groups,” arXiv:math/0605185v1, first submitted 8 May 2006, https://arxiv.org/abs/math/0605185.
2. A. Mader, “The automorphism group of finite abelian p-groups,” *Annales des Sciences Mathématiques du Québec* 36 (2012), 559–575.
3. J. Hage and T. Harju, “On Involutive Anti-Automorphisms of Finite Abelian Groups,” Utrecht technical report UU-CS-2007-053 (2007), https://ics-archive.science.uu.nl/research/techreps/repo/CS-2007/2007-053.pdf.
4. U. Hayat, D. López-Aguayo, and A. Abbas, “Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group,” *Symmetry* 10 (2018), 238, DOI:10.3390/sym10070238.
