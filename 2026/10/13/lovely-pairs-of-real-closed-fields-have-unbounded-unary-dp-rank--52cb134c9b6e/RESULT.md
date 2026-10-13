# Lovely pairs of real closed fields have unbounded unary dp-rank
## Finding
Let \(T=\mathrm{RCF}\), and let \(T_P\) denote the complete theory of lovely pairs \(P\preccurlyeq R\) of real closed fields. For every integer \(r\ge 1\),
\[
\operatorname{dp-rk}_{T_P}(x=x)\ge r.
\]
Equivalently, the singleton partial type \(x=x\) has unbounded dp-rank in \(T_P\).

Consequently, for every integer \(k\ge 1\), let
\[
\mathcal C_k=\{S:S\text{ is a complete NIP theory and }\operatorname{dp-rk}_S(x=x)\le k\}.
\]
Then \(\mathcal C_k\notin\mathfrak D^h_{n\text{-var}}\), where \(\mathfrak D^h_{n\text{-var}}\) is the larger class of dividing lines introduced by Kim.

## Assumptions and scope
Work in a sufficiently saturated proper lovely pair \(P\preccurlyeq R\models T_P\). Because \(P\) is real closed and elementary in the real closed field \(R\), every element of \(R\) algebraic over \(P\) already lies in \(P\). Thus any \(t\in R\setminus P\) is transcendental over \(P\).

The dp-rank assertion concerns the singleton partial type \(x=x\), not a claim that one fixed complete singleton type has infinite dp-rank. This distinction is compatible with the classical theorem that dense pairs of o-minimal theories are strongly dependent.

## Proof
Fix an integer \(r\ge 1\). Choose \(t\in R\setminus P\), and put
\[
a_i=t^i\qquad(0\le i<r).
\]
The tuple \(a_0,\ldots,a_{r-1}\) is linearly independent over \(P\), since a nontrivial \(P\)-linear relation among these powers would be a polynomial equation for the transcendental element \(t\).

For each \(i<r\), define the \(P\)-linear subspace
\[
H_i=\sum_{j<r,\ j\ne i} P a_j.
\]
This set is definable in the pair language with parameters \(a_0,\ldots,a_{r-1}\): membership in \(H_i\) is expressed by existentially quantifying the coefficients over the predicate \(P\).

Choose pairwise distinct elements \(c_m\in P\) for \(m<\omega\). For each row \(i<r\), consider the formulas
\[
\varphi_i(x;m):\quad x-c_m a_i\in H_i.
\]
Two distinct formulas in the same row are inconsistent. Indeed, if both \(x-c_m a_i\in H_i\) and \(x-c_{m'}a_i\in H_i\) held with \(m\ne m'\), then
\[
(c_m-c_{m'})a_i\in H_i,
\]
contradicting the \(P\)-linear independence of \(a_0,\ldots,a_{r-1}\).

On the other hand, for every choice \(m_0,\ldots,m_{r-1}<\omega\), the element
\[
x=\sum_{i<r}c_{m_i}a_i
\]
satisfies \(\varphi_i(x;m_i)\) for every \(i<r\). Hence these rows form an inp-pattern of depth \(r\) in the single object variable \(x\). Therefore the burden of \(x=x\) is at least \(r\). Dense/lovely pairs of real closed fields are NIP, and in NIP theories burden agrees with dp-rank, so
\[
\operatorname{dp-rk}_{T_P}(x=x)\ge r.
\]
Since \(r\) was arbitrary, unary dp-rank is unbounded.

Now fix \(k\ge1\). RCF is o-minimal, hence NIP with \(\operatorname{dp-rk}(x=x)=1\), so \(\mathrm{RCF}\in\mathcal C_k\). The displayed construction gives \(T_P\notin\mathcal C_k\). Kim's Theorem 10.33 states that every dividing line in \(\mathfrak D^h_{n\text{-var}}\) is preserved both ways between a complete geometric theory and its lovely-pair expansion. RCF is geometric. Thus \(\mathcal C_k\) cannot belong to \(\mathfrak D^h_{n\text{-var}}\).

## Verification
The proof was checked at the level of each quantifier and parameter dependence. The subspaces \(H_i\) use only finitely many parameters for each fixed \(r\); the same-row inconsistency uses only \(P\)-linear independence; and every transversal is realized by an explicit finite sum. No compactness step upgrades the finite-depth constructions to one infinite-depth pattern, and no such upgrade is claimed.

Kim's arXiv record verifies first submission on 2026-09-28 and MSC 03C45. The full text states Theorem 10.33 for every \(D\in\mathfrak D^h_{n\text{-var}}\) and every geometric \(T\): membership in \(D\) is equivalent for \(T\) and \(T_P\). The same paper records the earlier preservation of NIP. Classical dense-pair work records that dense pairs of o-minimal theories are strongly dependent; this is consistent with the present claim because only unbounded finite unary rank of the partial type \(x=x\) is asserted.

## Relationship to prior work
Kim proves broad lovely-pair preservation for all dividing lines in \(\mathfrak D^h_{n\text{-var}}\), and gives distality as an example of a familiar class excluded from the smaller framework by non-preservation. The present result supplies a different obstruction for the larger framework: every fixed finite cutoff on unary dp-rank fails preservation already from RCF to its lovely pair.

Berenstein--Dolich--Onshuus prove strong dependence for dense pairs arising from o-minimal theories, but do not state a uniform finite bound on the dp-rank of the singleton partial type. Their result therefore does not imply the present finite-depth coset construction. Van den Dries develops the definable geometry of dense pairs, which supplies the standard pair setting but not this dp-rank calculation.

## Limitations
The result does not say that \(T_P\) is not strongly dependent, and it does not produce one complete singleton type of infinite dp-rank. It proves arbitrarily large finite inp-patterns for the singleton partial type \(x=x\). It also does not classify which other rank-bounded dividing lines lie outside \(\mathfrak D^h_{n\text{-var}}\).

## References
1. Joonhee Kim, “\(n\)-variable theorems for dividing lines characterized by positive consistency-inconsistency configurations, and their applications to preservation problems,” arXiv:2609.36394v2, especially Theorem 10.33 and Remark 6.8.
2. Alexander Berenstein, Alf Dolich, and Alf Onshuus, “The independence property in generalized dense pairs of structures,” Journal of Symbolic Logic 76 (2011), 391–404, DOI 10.2178/jsl/1305810754, especially Corollaries 4.10–4.11.
3. Lou van den Dries, “Dense pairs of o-minimal structures,” Fundamenta Mathematicae 157 (1998), 61–78, DOI 10.4064/fm-157-1-61-78.
