# Exact complementary weighted-representation partitions for \((1,1,m/2)\), including translation orbits

## Finding
For every even integer \(m\ge2\), set \(h=m/2\) and let \(G=\mathbb Z/m\mathbb Z\). For any \(A\subseteq G\), let \(B=G\setminus A\), and define the **ordered** representation function
\[
R_A(n)=\#\{(x,y,z)\in A^3:x+y+hz=n\text{ in }G\}.
\]
The identity \(R_A(n)=R_B(n)\) for every \(n\in G\) has no solutions if \(m\equiv2\pmod4\). If \(4\mid m\), its complete set of solutions is the union of two explicitly defined families of \(h\)-element subsets:
\[
\begin{aligned}
\mathcal E_m&=\{A:|A\cap2G|=|A\setminus2G|=m/4\},\\
\mathcal T_m&=\{A:|A|=h,\ A+h=A\}.
\end{aligned}
\]
Here \(2G\) is the subgroup of even residues. Let \(W_m\) count **labeled** solutions. Then
\[
C_m=\begin{cases}0,&m\equiv4\pmod8,\\\binom{m/4}{m/8}^2,&8\mid m,\end{cases}
\qquad
W_m=\begin{cases}
0,&m\equiv2\pmod4,\\
\binom{m/2}{m/4}^2+\binom{m/2}{m/4}-C_m,&4\mid m.
\end{cases}
\]
Furthermore, let \(O_m\) count solution orbits under all translations of \(G\). For \(4\mid m\), define
\[
\begin{aligned}
E_m&=\sum_{\substack{d\mid m\\4\mid d}}\varphi(m/d)\binom{d/2}{d/4}^2,\\
T_m&=2\sum_{\substack{d\mid h\\2\mid d}}\varphi(h/d)\binom d{d/2},\\
J_m&=2\sum_{\substack{d\mid h\\4\mid d}}\varphi(h/d)\binom{d/2}{d/4}^2.
\end{aligned}
\]
With empty sums interpreted as zero, \(O_m=(E_m+T_m-J_m)/m\). For \(m\equiv2\pmod4\), \(O_m=0\). Thus the formulas provide an exact count of partitions up to translation, as well as of labeled solutions. The special values \((W_m,O_m)\) at \(m=4,8,12,16\) are \((6,2),(38,6),(420,38),(4934,314)\).

## Assumptions and scope
The modulus is any **even** integer at least two; the weights are the ordered triple \((1,1,m/2)\). Each coordinate lies in the **same** set \(A\), with repetitions permitted. The equality is pointwise over the entire residue group. Complementary subsets \(A,B\) are counted separately when they are different labeled sets; translation equivalence is taken only at the second counting stage. The formulas do not treat general weight triples.

## Proof
Sum the equality of representation functions over \(n\). Since each representation corresponds to exactly one ordered triple, \(|A|^3=|B|^3\), hence \(|A|=|B|=h\).

For \(j\in G\), put \(F_A(j)=\sum_{a\in A}\exp(2\pi i ja/m)\). The character transform of \(R_A\) is \(F_A(j)^2F_A(hj)\). Since \(A\) and \(B\) partition \(G\) with equal size, \(F_B(0)=F_A(0)=h\) and \(F_B(j)=-F_A(j)\) for \(j\ne0\).

For nonzero even \(j\), \(hj=0\) in \(G\), so the two transformed products agree automatically. For odd \(j\), \(hj=h\ne0\), hence the transformed equality reads \(F_A(j)^2F_A(h)=-F_A(j)^2F_A(h)\), or \(F_A(j)^2F_A(h)=0\). Therefore equality for all residues is equivalent to
\[
F_A(h)=0\quad\text{or}\quad F_A(j)=0\ \text{for every odd }j.
\]
The first alternative says \(\sum_{a\in A}(-1)^a=0\), precisely parity balance; in particular \(4\mid m\). For the second, Fourier inversion of \(F_{A+h}(j)=(-1)^jF_A(j)\) shows that all odd Fourier coefficients vanish if and only if \(A+h=A\). Such a set is a union of orbits of the fixed-point-free involution \(x\mapsto x+h\), so its size is even. Since \(|A|=h\), it exists only when \(h\) is even. This proves both the classification and the absence of solutions for \(m\equiv2\pmod4\).

Suppose \(4\mid m\). Parity-balanced sets consist of independent choices of \(m/4\) among the \(m/2\) even residues and the same number among odd residues, giving \(|\mathcal E_m|=\binom{m/2}{m/4}^2\). Translation-invariant sets are unions of precisely \(m/4\) among the \(m/2\) pairs \(\{x,x+h\}\), giving \(|\mathcal T_m|=\binom{m/2}{m/4}\). If \(m\equiv4\pmod8\), then \(h\) is even and each pair is parity-homogeneous, but a parity-balanced set would require a half-integral number of chosen pairs in each parity class: the intersection is empty. If \(8\mid m\), there are \(m/4\) pairs of each parity and exactly \(m/8\) pairs of each type must be chosen; thus \(|\mathcal E_m\cap\mathcal T_m|=\binom{m/4}{m/8}^2\). Inclusion-exclusion gives \(W_m\).

For the translation-orbit count, Burnside's lemma applies because the union \(\mathcal E_m\cup\mathcal T_m\) is translation-stable. Fix a translation by \(s\in G\). Its cyclic subgroup has \(g=\gcd(s,m)\) orbits, each of length \(m/g\). An \(s\)-fixed subset of size \(h\) is a union of \(g/2\) such orbits; it is parity-balanced precisely when \(4\mid g\), in which case the number is \(\binom{g/2}{g/4}^2\). This holds because a translation preserving an index-two parity split has even orbit length only if its generator is odd, and then no fixed subset of size \(h\) can be parity-balanced: more directly, if \(g\) is odd, \(m/g\) is divisible by four and cannot divide \(h\); if \(g\equiv2\pmod4\), \(g/2\) is odd, so no half-half selection of parity-homogeneous orbits. Thus the stated criterion covers every \(s\).

A set fixed under both translation by \(s\) and by \(h\) is constant on the cosets of the subgroup generated by \(s,h\), which has \(d=\gcd(s,h)\) orbits. Selecting half of these orbits gives \(\binom d{d/2}\) if \(2\mid d\) and none otherwise. Such a set is additionally parity-balanced exactly when \(4\mid d\), yielding \(\binom{d/2}{d/4}^2\) choices. There are \(\varphi(m/g)\) shifts with \(\gcd(s,m)=g\), and \(2\varphi(h/d)\) shifts with \(\gcd(s,h)=d\). Burnside and inclusion-exclusion give \(O_m=(E_m+T_m-J_m)/m\), as claimed.

## Verification
The standalone `verify.py` enumerates every half-sized subset for each of \(m=2,4,6,8,10,12,16\), computes all representation functions by exact triple loops, compares the full classification, then computes actual translation orbits and checks both formulas. Running `python verify.py` prints `VERIFY_OK`. This finite experiment checks only the listed moduli; the Fourier and Burnside arguments prove the infinite statement.

## Relationship to prior work
Zhenhua Qu, *Partitions of \(\mathbb Z_m\) with the Same Weighted Representation Functions*, Electronic Journal of Combinatorics 21(2) (2014), P2.55, gives a **general existence criterion** (Theorem 3), proposes determination of all sets in Problem 4, and supplies a cyclotomic criterion (Lemma 7) and a different special family in Example 5. The present result supplies a complete explicit classification and both labeled and translation-orbit enumerators for the natural order-two coefficient triple, rather than a new general existence theorem. Yang and Chen's earlier paper treats two weights; the index-two three-variable mechanism is different.

## Limitations
No claim is made about arbitrary three-term weights or uniqueness of literature coverage. Qu's general cyclotomic Lemma 7 can be specialized to derive the classification, so the contribution is the concrete two-family characterization together with its exact quantitative and orbit enumeration, **not** a novel general Fourier criterion. Later relevant studies may contain equivalent special formulas despite targeted searches. Only self-review has occurred; independent audit has not been performed.

## References
1. Z. Qu, *Partitions of \(\mathbb Z_m\) with the Same Weighted Representation Functions*, Electronic Journal of Combinatorics **21** (2014), P2.55, DOI: 10.37236/4089, first published 2014-06-27. Full article: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p55/pdf/ .
2. Q.-H. Yang and Y.-G. Chen, *Weighted representation functions on \(\mathbb Z_m\)*, arXiv:1208.4195 (2012), on the two-weight predecessor problem.
3. Z. Qu, *A remark on weighted representation functions*, Taiwanese Journal of Mathematics **18** (2014), 2014 paper on **two** weighted variables, DOI: 10.11650/tjm.18.2014.4334.
