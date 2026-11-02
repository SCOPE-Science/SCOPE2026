# Short Engel probability profiles recover modular Jordan types

## Finding

Fix an odd prime \(p\ge 3\), a positive integer \(d\), and a linear operator \(N\colon V\to V\) on \(V=\mathbb F_p^d\) with \(N^p=0\). Put \(T=1+N\) and let \(G_N=V\rtimes_T C_p\). For independently uniform \(x,y\in G_N\), write \(e_1(x,y)=[x,y]=x^{-1}y^{-1}xy\) and \(e_{k+1}(x,y)=[e_k(x,y),y]\). Denote the uniform probability measure on a subspace \(W\le V\) by \(U_W\), and the point mass at zero by \(\delta_0\).

**Complete value-distribution theorem.** For every integer \(k\ge1\), all word values lie in \(V\), and
\[
\mathcal L(e_k(x,y))=
\begin{cases}
\displaystyle p^{-2}\delta_0+(1-p^{-2})U_{NV},&k=1,\\[2mm]
\displaystyle p^{-1}\delta_0+(1-p^{-1})U_{N^kV},&k\ge2.
\end{cases}
\]
In particular, if \(r_k=\operatorname{rank}_{\mathbb F_p}(N^k)\) and \(s_k=\Pr(e_k(x,y)=1_{G_N})\), then
\[
s_1=p^{-2}+(1-p^{-2})p^{-r_1},\qquad
s_k=p^{-1}+(1-p^{-1})p^{-r_k}\quad(k\ge2).
\]
All terms with \(k\ge p\) equal one.

**Inverse and optimal-length theorem.** Knowing \(p\), the group order \(|G_N|=p^{d+1}\), and only \(s_1,\ldots,s_{p-1}\) uniquely determines the full Jordan-block partition of \(N\), and thus the isomorphism class of the displayed semidirect product. This universal word-length cutoff is sharp: for each odd prime \(p\), there are two nonisomorphic groups in the family of the same order \(p^{2p-1}\) whose probabilities agree for all \(1\le k\le p-2\), but differ at \(k=p-1\).

## Assumptions and scope

All groups are finite and all probabilities use independent **uniform elements** \(x,y\), with the same \(y\) reused at each right-normed Engel step. The action of the generator of \(C_p\) is \(T=1+N\); since the characteristic is \(p\) and \(N^p=0\), \(T^p=1\). The action may be trivial or nonfaithful. The result applies for every \(d\ge1\) and every nilpotent Jordan partition with block sizes at most \(p\), without an irreducibility or Frobenius hypothesis. The prime is restricted to odd primes in order to separate the new modular family and sharp cutoff from previously studied involutive semidirect products; the probability calculation itself also works at \(p=2\).

The word convention \([x,y]=x^{-1}y^{-1}xy\) fixes all signs; changing to another standard convention does not change the identity probabilities but may alter displayed value-distribution coordinates. The subgroup \(V\) is written additively, so \(1_{G_N}\) corresponds to \(0\in V\).

## Proof

Write elements of the semidirect product as \((u,a)\), with \(u\in V\) and \(a\in\mathbb F_p\), using multiplication
\[
(u,a)(v,b)=(u+T^a v,a+b).
\]
A direct application of inverses in this multiplication gives
\[
[(u,a),(v,b)]
=\bigl(T^{-a-b}((1-T^b)u+(T^a-1)v),0\bigr).
\]
The result belongs to \(NV\), since both \(1-T^b\) and \(T^a-1\) are divisible by \(N\) as polynomials in \(N\). For any nonzero \(c\in\mathbb F_p\), the polynomial \(T^c-1\) equals \(NQ_c(N)\), where \(Q_c(0)=c\ne0\). Because \(N\) is nilpotent, \(Q_c(N)\) is invertible, and \(\operatorname{im}(T^c-1)=NV\).

Condition on the uniformly sampled exponents \((a,b)\). When \((a,b)=(0,0)\), the commutator is identically zero. Otherwise at least one of the two coefficients of the independent uniform variables \(u,v\) has image exactly \(NV\), while both coefficients have image contained in \(NV\). Consequently the first commutator is uniform on \(NV\) whenever \((a,b)\ne(0,0)\), proving the displayed formula for \(k=1\).

For any \(c\in V\), its commutator with \((v,b)\) is
\[
[(c,0),(v,b)]=((T^{-b}-1)c,0).
\]
Hence, for \(k\ge2\), the value \(e_k((u,a),(v,b))\) equals
\[
(T^{-b}-1)^{k-1}T^{-a-b}
\bigl((1-T^b)u+(T^a-1)v\bigr)
\in N^kV.
\]
When \(b=0\) this is zero. When \(b\ne0\), the coefficient of \(u\) is \(N^k\) times a product of invertible commuting polynomials in \(N\), including \(Q_{-b}(N)^{k-1}\) and \(-Q_b(N)\). Thus that coefficient maps \(V\) onto \(N^kV\). The coefficient of \(v\) also maps into \(N^kV\). As \(u,v\) are independent and uniform, their sum is uniform on \(N^kV\). The probabilities of \(b=0\) and \(b\ne0\) are \(1/p\) and \(1-1/p\), establishing every distribution above. The argument remains valid when \(N^kV=0\), in which case both measures are \(\delta_0\).

Taking the identity mass gives the formulas for \(s_k\). For \(k\ge2\), the normalized quantity
\[
\frac{s_k-p^{-1}}{1-p^{-1}}=p^{-r_k}
\]
determines the integer \(r_k\); at \(k=1\), use
\[
\frac{s_1-p^{-2}}{1-p^{-2}}=p^{-r_1}.
\]
The group order gives \(r_0=d\); the hypothesis gives \(r_p=0\). If \(m_j\) denotes the number of Jordan blocks of length \(j\), the rank identity
\[
r_k=\sum_{j=1}^{p}m_j\max(j-k,0)
\]
and its second differences yield
\[
m_j=r_{j-1}-2r_j+r_{j+1}\quad(1\le j<p),
\qquad m_p=r_{p-1}.
\]
Thus the first \(p-1\) Engel identity probabilities and the order recover every block multiplicity. Two nilpotent operators with equal block partitions are similar, hence define isomorphic displayed semidirect products.

For sharpness take \(d=2p-2\) and operators with partitions \((p,p-2)\) and \((p-1,p-1)\). Their ranks agree for \(0\le k\le p-2\), where \(r_k=2p-2-2k\), but the ranks at \(k=p-1\) are respectively one and zero. Their Engel identity probabilities therefore agree through length \(p-2\), then differ. Their corresponding groups are not isomorphic: the lower central series has \(\gamma_{j+1}(G_N)=N^jV\) for \(j\ge1\), so their nilpotency classes are respectively \(p\) and \(p-1\). This also proves that no universally shorter prefix can recover these isomorphism classes.

For example, at \(p=3\) the partitions \((3,1)\) and \((2,2)\) give groups of order \(243\) with identical \(s_1=17/81\) and different \(s_2\), respectively \(5/9\) and \(1\).

## Verification

The standalone program `CHECK_DIRECT.py` explicitly implements semidirect-product multiplication, inversion and the iterated group commutator. It enumerates **all ordered pairs** in five finite examples and checks the formula for the probability of **every individual word value**, including zero and values off the predicted image. The examples are \(p=3\) with block partitions \((3,1)\), \((2,2)\), \((2,1)\), and \(p=5\) with partitions \((3)\), \((2)\). For the largest example, the exhaustive enumeration involves \(390625\) ordered pairs; all tests print `VERIFY_OK`.

`CHECK_INVERSION.py` independently enumerates all \(411\) nilpotent Jordan partitions of total dimension at most \(11\), with parts at most \(p\), for \(p\in\{3,5,7\}\). It checks injectivity of the finite Engel-probability signature, reconstructs every partition from its probabilities, and checks all three explicit sharp cutoff pairs. It prints `VERIFY_OK`. The recorded outputs are embedded alongside the source programs. The finite tests are reproducible corroborations of, not substitutes for, the universal algebraic proof.

## Relationship to prior work

De las Heras, Toti and Vannacci (2026) study Engel probabilities in a family of modular wreath-product \(p\)-groups. Their focus on single Engel probabilities and nilpotence properties motivates the question whether a **short sequence** of probabilities can reconstruct a group action. Only the abstract and bibliographic record could be inspected; possible deeper implications of its uninspected full text remain an originality risk.

Putignano and Vannacci (2026) compare probabilities of different words in finite groups, including Engel words. Their accessible full text supplies inequalities and comparison problems, but does not state the exact all-value distribution in a unipotent elementary-abelian semidirect product or the sharp Jordan-block recovery theorem.

Cocke and Ho (2019) establish general theory about distributions of word maps on finite groups; that framework and its terminology predate this result. The present theorem fixes the specific short right-Engel sequence and computes both its complete distributions and its sharp reconstruction capacity on a natural modular family.

Previous exact classifications of Engel digraphs for abelian-kernel cyclic **Frobenius** groups treat fixed-point-free actions, whereas every nontrivial modular unipotent \(p\)-action here has nontrivial fixed points. Those Frobenius results do not imply this calculation. Earlier computations of Engel distributions for involutive elementary-by-cyclic semidirect products concern complement order two, excluded from the sharp odd-prime statement.

The rank-difference reconstruction of Jordan block sizes is standard linear algebra. The proposed contribution is its use in the complete Engel-word distribution law, the finite statistical group-recognition statement, and the universally sharp \(p-1\) cutoff; the standard linear-algebra identity is not claimed as independently new.

## Limitations

The semidirect product must split with an elementary-abelian normal subgroup and a cyclic complement of **prime order equal to the field characteristic**. The recovery theorem assumes that \(p\) and the group order are known. It does not assert that arbitrary finite groups, nonsplit extensions, non-elementary kernels, or word statistics with independently resampled second variables are reconstructible. Equality of the first \(p-2\) probabilities can occur between nonisomorphic groups of the same order. No universal novelty certification follows from the literature search, and the 2026 wreath-product paper was not fully accessible.

## References

1. M. de las Heras, N. Toti and M. Vannacci, “Engel probability in wreath products of p-groups,” arXiv:2607.11605, first public version July 13, 2026.
2. C. Putignano and M. Vannacci, “Comparing word probabilities in finite groups,” arXiv:2610.23100, first public version October 16, 2026.
3. W. Cocke and M. Ho, “The probability distribution of word maps on finite groups,” *Journal of Algebra* 518 (2019), 440–452, DOI: 10.1016/j.jalgebra.2018.10.022.
4. E. Detomi, A. Lucchini and D. Nemmi, “The Engel graph of a finite group,” arXiv:2202.13737, *Forum Mathematicum* 35 (2023), 111–122.
