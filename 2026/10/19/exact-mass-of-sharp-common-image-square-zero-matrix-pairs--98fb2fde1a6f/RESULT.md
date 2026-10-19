# Exact mass of sharp common-image square-zero matrix pairs

## Finding

For a field \(k\), an integer \(r\ge1\), and a vector space \(V\) of dimension \(4r\), consider the **ordered, labeled** pairs of endomorphisms
\[
\mathcal E_r(k)=\{(A,B):A^2=B^2=0,\ \operatorname{im}(AB)=\operatorname{im}(BA),\ \operatorname{rank}(AB)=r\}.
\]
For every finite field \(k=\mathbb F_q\), their exact number is
\[
\boxed{\#\mathcal E_r(\mathbb F_q)=q^{-3r^2}\lvert\mathrm{GL}_{4r}(\mathbb F_q)\rvert.}
\]
Equivalently, fixing **any** square-zero \(A\) of rank \(2r\) on \(V\), exactly
\[
\boxed{q^{r^2}\lvert\mathrm{GL}_{2r}(\mathbb F_q)\rvert}
\]
square-zero choices of \(B\) satisfy the conditions. The formula holds in every characteristic and for every prime power \(q\). For \(r=1\), the total is \(2520\) over \(\mathbb F_2\) and \(898560\) over \(\mathbb F_3\).

The proof gives a sharp-boundary normal form. Every such pair has \(\operatorname{rank}A=\operatorname{rank}B=2r\) and
\[
\ker(AB)=\ker(BA)=\operatorname{im}A+\operatorname{im}B.
\]
Choose a decomposition \(V=U\oplus Y\oplus Z\oplus W\) into four spaces of dimension \(r\). Relative to this ordering, the pairs are exactly the simultaneous-conjugacy translates of
\[
A_0=\begin{pmatrix}0&0&I&0\\0&0&0&I\\0&0&0&0\\0&0&0&0\end{pmatrix},\qquad
B_H=\begin{pmatrix}0&H&0&0\\0&0&0&0\\0&0&0&I\\0&0&0&0\end{pmatrix},
\quad H\in\mathrm{GL}_r(k).
\]
Two parameters give conjugate ordered pairs exactly when they are similar. This normal form is used to calculate the mass formula; general string/band-module classification of pairs of square-zero operators is prior work, not claimed here as newly discovered.

## Assumptions and scope

The two operators act on the same \(4r\)-dimensional vector space; matrix pairs are ordered and labeled. They need not commute. The common-image condition concerns the two **products**, not the separate images of \(A\) and \(B\). The rank of each product is exactly \(r\), the sharp value \(\dim V/4\) allowed by the previously known image-equality bound. All assertions are field-independent until the finite-field counts are taken. The zero-rank case and nonsharp dimensions are not included.

## Proof

**1. Ranks at sharpness.** Write \(U=\operatorname{im}(AB)=\operatorname{im}(BA)\). It has dimension \(r\) and lies in both \(\operatorname{im}A\) and \(\operatorname{im}B\). Since \(A^2=B^2=0\), it also lies in \(\ker A\cap\ker B\). The map \(B\) restricts on \(\operatorname{im}A\) to a map with image \(U\), rank \(r\), and kernel containing \(U\). Thus \(\operatorname{rank}A\ge2r\). Interchanging \(A,B\) gives \(\operatorname{rank}B\ge2r\). Every square-zero endomorphism on a \(4r\)-space has rank at most \(2r\), so both ranks are \(2r\), with \(\ker A=\operatorname{im}A\) and \(\ker B=\operatorname{im}B\).

**2. The four-layer flag.** Put \(P=\operatorname{im}A\), \(Q=\operatorname{im}B\). Since \(B(P)=U\), the kernel of \(B|_P\) is \(P\cap Q\), of dimension \(2r-r=r\). It contains \(U\), so \(P\cap Q=U\) and \(\dim(P+Q)=3r\). Both products vanish on \(P+Q\): for example, \(B(P)=U\subseteq\ker A\) and \(B(Q)=0\). Similarly the other product vanishes there. Since each product has rank \(r\), its kernel is precisely \(P+Q\). Both induced maps
\[
\overline{AB},\overline{BA}:V/(P+Q)\longrightarrow U
\]
are isomorphisms. Their ratio \(H=(\overline{AB})^{-1}\overline{BA}\) is an automorphism of the \(r\)-dimensional quotient, intrinsic to the pair.

**3. Normal form and classification used in the count.** Choose a complement \(W\) to \(P+Q\), and put \(Y=A(W)\), \(Z=B(W)\). The images of \(Y\) and \(Z\) in \(P/U\) and \(Q/U\), respectively, are isomorphisms: \(A(Q)=U\), \(B(P)=U\), and each operator surjects onto its \(2r\)-dimensional image. Consequently \(V=U\oplus Y\oplus Z\oplus W\). Choose a basis of \(W\), transfer it to \(Y,Z\) via \(A,B\), and to \(U\) via \(AB\). The displayed \((A_0,B_H)\) follows. Conversely the blocks immediately satisfy the defining conditions for every invertible \(H\). Changing a basis of \(V/(P+Q)\) conjugates \(H\), and the intrinsic construction shows that no other identification is possible.

**4. Centralizer and orbit sizes.** Relative to the displayed blocks, a linear map simultaneously commuting with \(A_0,B_H\) has **exactly** the form
\[
X=\begin{pmatrix}
P_0&T&HS&R\\
0&P_0&0&S\\
0&0&P_0&T\\
0&0&0&P_0
\end{pmatrix},\qquad P_0H=HP_0,
\]
where \(S,T,R\) are arbitrary \(r\)-square blocks. Necessity follows by applying commutation to \(W\), then to \(Y=A(W)\), \(Z=B(W)\), and \(U=AB(W)\); sufficiency is direct matrix multiplication. It is invertible precisely when \(P_0\) is invertible. Thus over \(\mathbb F_q\) its invertible simultaneous centralizer has cardinality \(q^{3r^2}\lvert C_{\mathrm{GL}_r(q)}(H)\rvert\). The simultaneous-conjugacy orbit of the parameter class \([H]\) therefore has size
\[
\frac{\lvert\mathrm{GL}_{4r}(q)\rvert}{q^{3r^2}\lvert C_{\mathrm{GL}_r(q)}(H)\rvert}.
\]
Summing over similarity classes of invertible \(H\), using
\[
\sum_{[H]\subseteq\mathrm{GL}_r(q)}\frac{1}{\lvert C_{\mathrm{GL}_r(q)}(H)\rvert}=1
\]
(the ordinary conjugacy-class orbit equation), proves the asserted total.

**5. Fixed-first-factor count.** The number of square-zero rank-\(2r\) endomorphisms on a \(4r\)-space equals
\[
{4r\brack2r}_q\lvert\mathrm{GL}_{2r}(q)\rvert
=\frac{\lvert\mathrm{GL}_{4r}(q)\rvert}{q^{4r^2}\lvert\mathrm{GL}_{2r}(q)\rvert},
\]
by choosing \(\operatorname{im}A=\ker A\) and an isomorphism from its quotient to it. Transitivity of \(\mathrm{GL}_{4r}\) on this class makes the number of admissible second factors constant. Dividing the total by the displayed first-factor count gives \(q^{r^2}\lvert\mathrm{GL}_{2r}(q)\rvert\).

## Verification

The programs `verify_binary.py`, `verify_ternary.py`, and `verify_centralizer.py` are part of this package. The first enumerates all \(210\) rank-two square-zero operators over \(\mathbb F_2\), and then all \(44100\) ordered pairs; precisely \(2520\) meet the sharp common-image condition. The second enumerates all \(6240\) rank-two square-zero choices of the second factor over \(\mathbb F_3\), with a fixed first factor; precisely \(144=3\lvert\mathrm{GL}_2(3)\rvert\) qualify. The third computes the linear simultaneous centralizer of three \(8\)-dimensional canonical pairs over \(\mathbb F_3\), with two-dimensional parameters having scalar, split-distinct, and nonsemisimple Jordan types; its dimensions are \(16,14,14\), matching the formula. These are finite checks, not a proof of the unrestricted formulas. Python 3 is required; the latter two scripts additionally require NumPy.

## Relationship to prior work

Mohammadian [1] proves the sharp upper bound \(\operatorname{rank}(AB)\le\dim(V)/4\) under equality of the product images. That bound is a premise/motivation, not a new result. The current assertion is the **exact number of pairs attaining that boundary**, with a direct uniform centralizer calculation. The publisher abstract is accessible, but the full text of [1] was not available for complete overlap inspection; its potential treatment of equality cases is a material priority risk.

The general string/band-module classification in Crawley-Boevey [2, Theorems 1.2–1.3] explicitly applies to the algebra \(k\langle x,y\rangle/(x^2,y^2)\), so an abstract description of its finite-dimensional module types, including band parameters, is prior work. We do not claim that generic module parameterization as new. Its inspected theorem and construction do not directly state the prescribed common-image rank extremal locus, its simultaneous centralizer orders, or the aggregate finite-field mass, although they provide a broad framework from which these could potentially be recovered. Earlier results on jointly annihilating pairs [3] have \(AB=BA=0\), disjoint from the present positive-product-rank locus. A previously published count derived from general module classifications or an equality-case appendix remains a specific originality risk.

## Limitations

No statement is made for arbitrary product ranks, nonsaturating dimensions, or ordered triples. The theorem counts matrices, not distinct conjugacy orbits as the primary invariant, though the proof gives orbit parameters and sizes. Its closed mass formula is verified by an exact proof and small-field checks; uniqueness in the global literature is not established. Independent mathematical review has not been performed. No claim is made that a general string/band classification is new.

## References

[1] A. Mohammadian, *Sums and Products of Square-Zero Matrices*, *Communications in Algebra* **40** (2012), 4568–4574. First verified public online date: 2012-10-10. DOI: `10.1080/00927872.2011.613423`.

[2] W. Crawley-Boevey, *Classification of modules for infinite-dimensional string algebras*, arXiv:`1308.6410` (first public version 2013-08-29; revised 2016), especially the explicitly listed algebra \(k\langle x,y\rangle/(x^2,y^2)\), band modules, and Theorems 1.2–1.3.

[3] J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:`math/0211293` (2002), *Commentarii Mathematici Helvetici* **79** (2004), 396–426.
