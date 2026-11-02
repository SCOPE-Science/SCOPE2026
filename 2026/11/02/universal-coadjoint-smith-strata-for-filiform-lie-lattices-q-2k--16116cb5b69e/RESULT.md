# Universal coadjoint Smith strata for filiform Lie lattices \(Q_{2k}\) over finite chain rings

## Finding

Let \(R\) be **any finite commutative chain ring** of length \(s\geq1\), with maximal ideal \((\pi)\) and residue field of size \(q\). Put \(\nu(0)=s\); for nonzero \(x\in R\), let \(\nu(x)\) be the unique \(a\in\{0,\ldots,s-1\}\) with \(x\in(\pi^a)\setminus(\pi^{a+1})\). Let \(k\geq2\), put \(n=2k\), and define the \(R\)-Lie algebra \(Q_n(R)\) with basis \(e_1,\ldots,e_n\) and independent brackets
\[
[e_1,e_i]=e_{i+1}\quad (2\leq i\leq n-1),\qquad
[e_i,e_{n+1-i}]=(-1)^{i+1}e_n\quad(2\leq i\leq k),
\]
with all other independent brackets zero. These are integral structure constants; the definition is valid in every characteristic.

For each \(R\)-linear functional \(\lambda:Q_n(R)\to R\), let \(B_\lambda(x,y)=\lambda([x,y])\). Set
\[
a=\nu(\lambda(e_n)),\quad b=\min_{3\leq i\leq n}\nu(\lambda(e_i)),\quad 0\leq b\leq a\leq s,
\]
where \(\pi^s\) denotes zero. **Every** such alternating matrix is equivalent by invertible simultaneous row/column basis changes to
\[
\boxed{\pi^b J_2\;\oplus\;(\pi^a J_2)^{\oplus(k-2)}\;\oplus\;0_2,}
\qquad J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
In particular, the kernel has cardinality \(q^{2b+2(k-2)a+2s}\) and the image has cardinality
\[
\boxed{q^{2e(a,b)}},\qquad e(a,b)=(s-b)+(k-2)(s-a).
\]
This remains true when some of the displayed blocks are zero, in residue characteristic two, and for mixed-characteristic chain rings.

Put \(r=n-3\). The **exact number of functionals** with invariants \((a,b)\) is
\[
\boxed{H_{a,b}=\begin{cases}
q^{2s}(q-1)q^{s-a-1}\bigl(q^{r(s-b)}-q^{r(s-b-1)}\bigr),&0\le b<a<s,\\[2pt]
q^{2s}(q-1)q^{s-a-1}q^{r(s-a)},&0\le b=a<s,\\[2pt]
q^{2s}\bigl(q^{r(s-b)}-q^{r(s-b-1)}\bigr),&0\le b<s,\ a=s,\\[2pt]
q^{2s},&a=b=s.
\end{cases}}
\]
Thus the entire local coadjoint-image spectrum is the explicit polynomial
\[
\boxed{\mathcal P_{k,s,q}(T)=\sum_{0\le b\le a\le s}H_{a,b}T^{e(a,b)}.}
\]
The polynomial depends only on \((k,s,q)\), not on the isomorphism type of the chain ring. In particular \(\mathcal P_{k,s,q}(1)=q^{sn}\).

There is also a representation-theoretic conclusion. If the residue characteristic \(p\) satisfies \(p>2k-1\), the Lazard/Baker–Campbell–Hausdorff group \(G=\exp(Q_n(R))\) is defined. Its number of irreducible complex characters of degree \(q^d\) is
\[
\boxed{\operatorname{ch}_{q^d}(G)=q^{-2d}\sum_{e(a,b)=d}H_{a,b}.}
\]
This counts characters, not merely possible degrees; the right side is an integer. No character-theory assertion is made outside the indicated Lazard range.

## Assumptions and scope

The ring is finite, commutative, local, and principal with totally ordered ideals; no equal-characteristic assumption is made. The integers satisfy \(k\geq2\) and \(s\geq1\). The Smith classification and point counts are statements about \(R\)-linear forms in **all** characteristics, including characteristic two. The character-degree conclusion additionally requires residue characteristic \(p>2k-1\). The theorem does not concern arbitrary filiform deformations, non-chain local rings, or indecomposable representations of the Lie algebra.

## Proof

**1. The commutator matrix.** Write \(u_i=\lambda(e_i)\), \(z=u_n\), and \(v=(u_3,\ldots,u_n)\in R^{n-2}\). Relative to the decomposition
\(Re_1\oplus\bigoplus_{i=2}^{n-1}Re_i\oplus Re_n\), the form has matrix
\[
M_\lambda=\begin{pmatrix}0&v&0\\-v^{\mathsf T}&zJ&0\\0&0&0\end{pmatrix},
\]
where \(J\) is the invertible alternating matrix on \(R^{n-2}\) induced by the pairings \(i\leftrightarrow n+1-i\). In particular, \(v\) includes the coordinate \(z\), and hence \(b\le a\).

**2. Symplectic reduction over a local principal ideal ring.** If \(b=s\), then \(v=0\) and \(z=0\), so the matrix vanishes. Otherwise, choose \(w\in R^{n-2}\) with \(v=\pi^bw\) and \(w\) primitive, i.e. with a unit coordinate. Every primitive vector in a unimodular alternating module over a local ring extends to a symplectic basis: find a vector pairing to one with \(w\), split off the resulting hyperbolic plane, and repeat on its nondegenerate orthogonal complement. This also applies to row covectors by the symplectic identification with column vectors. Hence a symplectic change of basis makes \(v=(\pi^b,0,\ldots,0)\), while keeping \(J\) standard. The matrix splits into \((k-2)\) blocks \(zJ_2\), a central zero, and the three-by-three block
\[
\begin{pmatrix}0&\pi^b&0\\-\pi^b&0&z\\0&-z&0\end{pmatrix}.
\]
Since \(b\le a\), write \(z=\pi^bc\) for some \(c\in R\). Replacing the third basis vector of this block by itself plus \(c\) times the first kills the two entries \(\pm z\), giving \(\pi^bJ_2\oplus0_1\). Each \(zJ_2\) is equivalent to \(\pi^aJ_2\) because \(z\) is an associate of \(\pi^a\) when \(a<s\), and both vanish when \(a=s\). This proves the asserted congruence and the complete elementary-divisor list. Multiplication by \(\pi^j\) on \(R\) has image cardinality \(q^{s-j}\) and kernel cardinality \(q^j\); applying this to every block proves the image and kernel formulas, including the zero blocks.

**3. Full valuation census.** The coordinates \(u_1,u_2\) contribute \(|R|^2=q^{2s}\) independently. Of the remaining coordinates, \(u_n=z\) has valuation \(a\), and the \(r=n-3\) coordinates \(u_3,\ldots,u_{n-1}\) determine \(b\) through their joint minimum with \(a\). For \(a<s\), the number of possible \(z\) is \((q-1)q^{s-a-1}\). If \(b<a\), the \(r\) coordinates have joint minimum exactly \(b\), giving \(q^{r(s-b)}-q^{r(s-b-1)}\). If \(b=a\), they are merely divisible by \(\pi^a\), giving \(q^{r(s-a)}\). If \(a=s\), then \(z=0\), and the joint minimum of those \(r\) coordinates is exactly \(b\), with the all-zero case counted separately. These disjoint cases are precisely \(H_{a,b}\). Summation with the already-proved image size gives \(\mathcal P_{k,s,q}\) and its normalization.

**4. Character degrees in the Lazard range.** Every finite commutative chain ring admits a generating additive character \(\psi:R\to\mathbb C^\times\): choose an additive character nontrivial on its socle \(\pi^{s-1}R\). Its kernel contains no nonzero ideal, since every nonzero ideal contains that socle. Consequently \(u\mapsto(x\mapsto\psi(ux))\) identifies \(R\) with its Pontryagin dual, and similarly identifies \(\operatorname{Hom}_R(Q_n(R),R)\) with the group of additive characters of \(Q_n(R)\). Under this identification the alternating form governing a character's coadjoint stabilizer has radical \(\ker M_\lambda\). For \(p>2k-1\), the finite-group orbit method for Lie rings of class less than \(p\) applies: the corresponding coadjoint orbit has size \(q^{2e(a,b)}\), and its irreducible character degree is \(q^{e(a,b)}\). Each orbit consists of exactly that many functionals. Dividing each stratum count by its orbit size proves the stated multiplicity formula. In particular, all coefficients after division are nonnegative integers.

## Verification

The standalone `check.py` builds matrices from the original bracket relations, **without applying the symplectic normal form**. For integer quotient rings it performs independent modular Smith elimination. For truncated polynomial rings it expands the matrices as linear maps over the prime field and calculates their ranks. In each case it exhaustively iterates every functional and independently compares the complete exponent distribution with the valuation formula.

The 17 exhaustive cases include \(n\in\{4,6,8\}\), rings \(\mathbb Z/2^s\mathbb Z\) through \(s=4\), \(\mathbb Z/9\mathbb Z\), \(\mathbb F_2[t]/(t^2)\), \(\mathbb F_2[t]/(t^3)\), and \(\mathbb F_3[t]/(t^2)\), and genuine extension-field arithmetic over \(\mathbb F_4[t]/(t^2)\). In particular, the computations compare nonisomorphic length-two rings with the same \((s,q)\). The checker prints `FILIFORM_Q_CHAIN_KIRILLOV_OK 17`; `CHECK_OUTPUT.txt` preserves the complete recorded output. The case \(k=3,s=2,q=2\) has
\[
\mathcal P_{3,2,2}(T)=16+112T+1024T^2+896T^3+2048T^4.
\]
These finite computations are corroboration only; the proof above handles arbitrary finite chain rings and all \(k,s\).

## Relationship to prior work

Adimi and Makhlouf, *Index of Graded Filiform and Quasi Filiform Lie Algebras* (arXiv:1212.1650v1, publicly submitted 2012-12-07), give the integral-style presentation of \(Q_{2k}\) and calculate its **generic index** over an algebraically closed characteristic-zero field (section 4.1, Proposition 13). The field-level generic-rank fact is prior work. The present statement refines it to the full Smith type of **every** coadjoint form over **every finite chain ring**, including the two interacting valuation parameters and their exact multiplicities. It is not a claim to discover the Lie family or its index.

O'Brien and Voll, *Enumerating classes and characters of \(p\)-groups* (arXiv:1203.3050v1, 2012), establish the general finite-group orbit-method framework and the character/commutator-matrix relationship (especially Theorem 3.1). That framework is prior work. Their evaluated field-rank formulas and their Theorem B's residue-vector-space hypotheses do not state the above explicit higher-length \(Q_{2k}\) Smith strata or character counts. The character formula here is the application of their general orbit mechanism to the newly evaluated chain-ring strata, not a new orbit-method theorem.

Related literature on cohomology and classification of filiform Lie algebras studies different invariants. Searches for local representation zeta formulas, chain-ring Smith invariants, coadjoint regular strata, and equivalent \(Q_{2k}\) descriptions did not identify this complete statement. Search absence is not a proof of publication priority.

## Limitations

This is a theorem about coadjoint alternating matrices and a conditional corollary about characters. It does not enumerate individual group coadjoint orbits, resolve character formulas outside the Lazard range, or treat arbitrary deformations of filiform Lie algebras. Ring-universality requires the chain-ring condition. Historical publication priority is provisional, and independent mathematical validation has not been performed.

## References

1. H. Adimi and A. Makhlouf, *Index of Graded Filiform and Quasi Filiform Lie Algebras*, arXiv:1212.1650v1 (2012-12-07), https://arxiv.org/html/1212.1650v1; especially section 4.1, Proposition 13.
2. E. A. O'Brien and C. Voll, *Enumerating classes and characters of \(p\)-groups*, arXiv:1203.3050 (2012-03-14), https://arxiv.org/abs/1203.3050; especially Theorem 3.1 and the commutator-matrix method.
3. M. Boyarchenko and M. Sabitova, *The orbit method for profinite groups and a \(p\)-adic analogue of Brown's theorem*, arXiv:math/0608126 (2006), https://arxiv.org/abs/math/0608126; background on the finite-group orbit method.
