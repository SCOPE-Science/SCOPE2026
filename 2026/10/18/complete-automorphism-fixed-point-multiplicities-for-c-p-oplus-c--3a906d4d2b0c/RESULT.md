# Complete automorphism fixed-point multiplicities for \(C_p\oplus C_{p^m}\) beyond the small-exponent tables

## Finding

Let \(p\) be any prime, \(m\ge4\) an integer, and \(G=C_{p^m}\oplus C_p\). For \(0\le j\le m+1\), let \(\Theta_{p,m}(j)\) be the number of automorphisms \(\phi\) of \(G\) satisfying \(|\ker(\phi-I)|=p^j\). Then **every fixed-point multiplicity** has the following uniform closed formula:

\[
\boxed{\Theta_{p,m}(j)=\begin{cases}
p^{m+1}(p-2)^2,&j=0,\\
p^m(p-2)(2p-1),&j=1,\\
2(p-1)^2p^{m-j+1},&2\le j\le m-2,\\
p(p-1)^2(2p+1),&j=m-1,\\
p^3-p-1,&j=m,\\
1,&j=m+1.
\end{cases}}
\]

In particular, the interior frequencies form a geometric progression with common ratio \(p^{-1}\), whereas the top two nonidentity fixed-point frequencies are independent of \(m\). These assertions hold also for \(p=2\), where the first two frequencies vanish.

For every integer \(s\ge0\), the number \(N_{p,m}(s)\) of orbits of ordered \(s\)-tuples in \(G\) under its diagonal automorphism action follows by Burnside's lemma:
\[
\boxed{N_{p,m}(s)=\frac{\sum_{j=0}^{m+1}\Theta_{p,m}(j)p^{js}}{p^{m+1}(p-1)^2}.}
\]
The individual lower layers \(j=0,1,2\) and the ordered-pair orbit problem have important antecedents; the contribution here is the **complete, all-level multiplicity distribution** for the unbounded exponent family, not the isolated previously known layers or the general Burnside identity.

## Assumptions and scope

All groups are finite and abelian; write \(G\) additively. The automorphism group has order
\[
|\operatorname{Aut}(G)|=p^{m+1}(p-1)^2.
\]
For \(p=2\), an expression such as \(p-2\) is evaluated literally; the formula does not assume odd characteristic. The theorem is stated for \(m\ge4\) because the entire cases \(m=2\) and \(m=3\) already have published fixed-point tables. The formula also agrees with the known \(m=3\) table, but that boundary case is not claimed as new.

## Proof

### Automorphism parameterization

Identify \(G\) with \((\mathbb Z/p^m\mathbb Z)\oplus(\mathbb Z/p\mathbb Z)\). Every automorphism is uniquely
\[
\phi(x,y)=\bigl(ax+p^{m-1}by\pmod{p^m},\;cx+dy\pmod p\bigr),
\]
where \(a\in(\mathbb Z/p^m\mathbb Z)^\times\), \(d\in\mathbb F_p^\times\), and \(b,c\in\mathbb F_p\). Indeed these are all endomorphisms, and the induced maps on the two distinct cyclic-exponent blocks modulo \(p\) show that invertibility is equivalent to the stated two unit conditions. Counting parameters yields \(|\operatorname{Aut}(G)|=p^{m+1}(p-1)^2\).

A fixed point solves
\[
(a-1)x+p^{m-1}by\equiv0\pmod{p^m},\qquad c(x\bmod p)+(d-1)y=0\quad\text{in }\mathbb F_p.
\]
Put \(k=\min\{v_p(a-1),m\}\), so \(k=m\) denotes \(a=1\). The numbers of available \(a\)'s are \((p-2)p^{m-1}\) for \(k=0\), \((p-1)p^{m-k-1}\) for \(1\le k\le m-1\), and one for \(k=m\).

### The lower and interior layers

For \(k=0\), the first equation determines \(x\) from \(y\), and it forces \(x\equiv0\pmod p\). Consequently \(d\ne1\) gives exactly one fixed point, while \(d=1\) gives exactly \(p\) fixed points. In either case \(b,c\) are arbitrary.

For \(1\le k\le m-2\), the first equation has exactly \(p^k\) solutions \(x\) for every \(y\); all satisfy \(x\equiv0\pmod p\), since the right side has valuation at least \(m-1\). The second equation therefore forces \(y=0\) when \(d\ne1\) and leaves \(y\) free when \(d=1\). Thus this case contributes fixed-subgroup orders \(p^k\) and \(p^{k+1}\), respectively.

For any \(2\le j\le m-2\), the disjoint contributions come from \((k,d)=(j,d\ne1)\) and \((k,d)=(j-1,d=1)\), and their sum is
\[
(p-1)p^{m-j-1}p^2(p-2)+(p-1)p^{m-j}p^2
=2(p-1)^2p^{m-j+1}.
\]
At \(j=0\) only \(k=0,d\ne1\) contributes, giving \(p^{m+1}(p-2)^2\). At \(j=1\), the contributions \(k=0,d=1\) and \(k=1,d\ne1\) add to \(p^m(p-2)(2p-1)\).

### The two upper nonidentity layers

For \(k=m-1\), write \(a-1=p^{m-1}u\), where \(u\in\mathbb F_p^\times\). Both fixed equations now depend only on \((x\bmod p,y)\):
\[
\begin{pmatrix}u&b\\c&d-1\end{pmatrix}\binom{x\bmod p}{y}=0.
\]
Every solution mod \(p\) lifts to exactly \(p^{m-1}\) values of \(x\). When \(d\ne1\), the \(2\times2\) matrix has rank one exactly when \(bc=u(d-1)\). For each nonzero \(u\) and each \(d\ne1\), precisely \(p-1\) of the \(p^2\) pairs \((b,c)\) satisfy this equation. All other pairs give rank two. When \(d=1\), the matrix has rank two exactly when \(bc\ne0\); it otherwise has rank one because \(u\ne0\).

For \(k=m\), the coefficient matrix becomes
\[
\begin{pmatrix}0&b\\c&d-1\end{pmatrix}.
\]
If \(d\ne1\), it has rank two exactly when \(bc\ne0\) and otherwise rank one. If \(d=1\), it has rank two for \(bc\ne0\), rank one when exactly one of \(b,c\) is nonzero, and rank zero exactly when \(b=c=0\). The zero-rank case is the identity automorphism and has all \(p^{m+1}\) elements fixed.

Each rank-two case has exactly \(p^{m-1}\) fixed elements, and each rank-one case exactly \(p^m\). At rank \(m-1\), include also the \(k=m-2,d=1\) contribution \(p^3(p-1)\). Direct counting of the now explicitly classified parameter cells gives
\[
\begin{split}
\Theta_{p,m}(m-1)={}&p^3(p-1)+(p-1)(p-2)(p^2-p+1)\\
&+(p-1)^3+(p-2)(p-1)^2+(p-1)^2\\
={}&p(p-1)^2(2p+1).
\end{split}
\]
The complementary rank-one counts in these upper cases give
\[
\begin{split}
\Theta_{p,m}(m)={}&(p-1)^2(p-2)+(p-1)(2p-1)\\
&+(p-2)(2p-1)+2(p-1)\\
={}&p^3-p-1.
\end{split}
\]
The remaining multiplicity is \(\Theta_{p,m}(m+1)=1\). This exhausts every automorphism, proving the stated distribution. Substitution verifies that \(\sum_j\Theta_{p,m}(j)=|\operatorname{Aut}(G)|\).

### Diagonal tuple orbits

An automorphism fixing \(p^j\) elements fixes exactly \(p^{js}\) ordered \(s\)-tuples, including the unique empty tuple for \(s=0\). Burnside's lemma therefore gives the stated formula for \(N_{p,m}(s)\). This consequence requires no assumption of semisimplicity and remains valid for all primes.

## Verification

The accompanying `verify.py` independently calculates the order of the kernel of each \(\phi-I\) using the gcd of the maximal minors of an integral presentation matrix, rather than the proof's case partition. It exhausts automorphisms for \((p,m)=(2,4),(2,5),(2,6),(3,4),(3,5),(5,4)\) and checks all proposed coefficients and total group orders. It also checks the already known boundary \(m=3\).

A second routine independently enumerates fixed elements directly for the smaller pairs \((p,m)=(2,3),(2,4),(3,3),(5,3)\). All listed tests passed with `VERIFY_OK`. These finite calculations corroborate but do not replace the uniform congruence proof.

For example, the complete six-layer frequency lists for \((p,m)=(2,4)\) and \((3,4)\) are respectively \((0,0,16,10,5,1)\) and \((243,405,216,84,23,1)\). The count \(\Theta_{p,m}(m+1)=1\) also independently follows because only the identity automorphism fixes every element.

## Relationship to prior work

Hillar and Rhea give the foundational matrix description of automorphisms of finite abelian groups. Hayat, López-Aguayo and Abbas (2018) define the fixed-point multiplicity \(\theta(G,d)\), compute its entire table for \(C_p\oplus C_{p^2}\), give the fixed-point-free count for arbitrary distinct exponent pairs and pose the wider counting problem. The 2016 paper by Hayat and Ali computes all multiplicities for \(C_p\oplus C_{p^3}\), so that case is excluded from the new claim.

Previously available separate formulae also determine the \(j=0\), \(j=1\), and \(j=2\) layers for this family. They are recovered here as required consistency checks and **are not separately claimed as new**. Their statements do not determine the remaining higher layers for unbounded \(m\).

Dutta and Prasad classify element orbits; Calvert, Dutta and Prasad develop structural descriptions of tuple orbits. Anilkumar and Prasad (2014) give an algorithm and explicit polynomials counting orbits of ordered *pairs* for any finite abelian \(p\)-group. Accordingly the ordered-pair specialization of our Burnside formula is **already covered**, and no priority is claimed for it. The value of the full distribution is that it directly counts automorphisms by fixed subgroup order and simultaneously yields the diagonal-orbit counts at every tuple length, including lengths above two. The usual Burnside formula itself is classical.

## Limitations

The theorem treats only the distinct-exponent rank-two groups \(C_p\oplus C_{p^m}\) with one cyclic factor of order \(p\), for \(m\ge4\). It does not solve the general fixed-point multiplicity problem for \(C_{p^a}\oplus C_{p^b}\) with \(a\ge2\), nor higher rank. The result is a mathematical proof with computational corroboration, not an independent certification. Despite comparison with primary literature and mathematical records, a more general or equivalent unlocated formula could already exist. The closely relevant full 2016 low-exponent paper was not available for direct complete-text inspection; its published stated scope concerns only \(m=3\).

## References

1. C. J. Hillar and D. L. Rhea, “Automorphisms of finite Abelian groups,” arXiv:math/0605185v1 (8 May 2006), *American Mathematical Monthly* 114 (2007), 917–923.
2. U. Hayat, D. López-Aguayo, and A. Abbas, “Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group,” arXiv:1801.03229, *Symmetry* 10 (2018), 238; doi:10.3390/sym10070238.
3. U. Hayat and F. Ali, “Fixed Points of Automorphisms of \(C_p\times C_{p^3}\),” *Journal of Mathematical Analysis* 7(6) (2016), 91–101.
4. K. Dutta and A. Prasad, “Degenerations and orbits in finite abelian groups,” arXiv:1005.5222 (2010), *Journal of Combinatorial Theory A* 118 (2011), 1685–1694.
5. W. Calvert, K. Dutta, and A. Prasad, “Degeneration and orbits of tuples and subgroups in an Abelian group,” arXiv:1208.4902 (2012), *Journal of Group Theory* 16 (2013), 221–233.
6. C. P. Anilkumar and A. Prasad, “Orbits of Pairs in Abelian Groups,” arXiv:1305.5328 (2013), *Séminaire Lotharingien de Combinatoire* 70 (2014), B70h.
7. F. Ali, U. Hayat, and Y. Li, “Fixed Points of Automorphisms of Certain Finite Groups,” *International Journal of Algebra* 13 (2019), 167–183.
