# Multiplicativity of LS-category for products of capped finite spaces
## Finding
Let \(k\ge 1\). For each \(1\le i\le k\), let \(P_i\) be a nonempty noncontractible finite \(T_0\)-space, let \(m_i\ge 2\), and put
\[
X_i=P_i\oplus D_{m_i},
\]
where \(D_{m_i}\) is a discrete \(m_i\)-point space and every point of \(P_i\) is declared below every point of \(D_{m_i}\). Using unreduced Lusternik--Schnirelmann category, so that a contractible nonempty space has category \(1\), one has
\[
\operatorname{cat}\!\left(\prod_{i=1}^k X_i\right)
=
\operatorname{gcat}\!\left(\prod_{i=1}^k X_i\right)
=
\prod_{i=1}^k m_i
=
\prod_{i=1}^k\operatorname{cat}(X_i).
\]
For two factors \(X=P\oplus D_m\) and \(Y=Q\oplus D_n\), the reduced convention therefore gives
\[
\operatorname{cat}_r(X\times Y)=mn-1,
\qquad
\operatorname{cat}_r(X)=m-1,
\qquad
\operatorname{cat}_r(Y)=n-1,
\]
and hence
\[
\operatorname{cat}_r(X\times Y)-\operatorname{cat}_r(X)-\operatorname{cat}_r(Y)
=(m-1)(n-1)>0.
\]
Thus the usual reduced subadditive product estimate valid under standard separation hypotheses can fail by an arbitrarily large amount for finite non-Hausdorff spaces. The smallest member of the family is the product of two four-point crown models: each factor has reduced category \(1\), while the product has reduced category \(3\).

## Assumptions and scope
Finite \(T_0\)-spaces are identified with finite posets via the specialization order, and open sets are lower sets. For finite spaces, \(\operatorname{cat}(Z)\) denotes the least number of open subsets whose inclusions in \(Z\) are null-homotopic, while \(\operatorname{gcat}(Z)\) denotes the least number of open subsets that are contractible in themselves. Both are unreduced in the displayed theorem. The ordinal sum \(P\oplus D_m\) places all points of \(P\) below all \(m\) points of the discrete top antichain.

The assumptions that each \(P_i\) is nonempty and noncontractible and each \(m_i\ge2\) are essential to the stated obstruction. No claim is made for contractible bases or for arbitrary finite spaces not of this capped form.

## Proof
Write
\[
Z=\prod_{i=1}^k X_i
\quad\text{and}\quad
M=\prod_{i=1}^k m_i.
\]
The global maximal points of \(Z\) are exactly the \(M\) tuples whose \(i\)-th coordinate lies in the top antichain \(D_{m_i}\). For each global maximum \(a\), its principal open set
\[
U_a=\{z\in Z:z\le a\}
\]
has a maximum and is therefore contractible. These principal opens cover \(Z\). Hence
\[
\operatorname{gcat}(Z)\le M,
\qquad
\operatorname{cat}(Z)\le M.
\]

It remains to prove that no categorical open subset contains two distinct global maxima. Let \(U\subseteq Z\) be open and suppose it contains distinct global maxima \(a=(a_1,\ldots,a_k)\) and \(b=(b_1,\ldots,b_k)\). Choose an index \(j\) with \(a_j\ne b_j\). For every \(i\ne j\), choose a point \(p_i\in P_i\). Let
\[
Y_j=P_j\oplus\{a_j,b_j\}\subseteq X_j.
\]
Define an order-preserving map \(\phi:Y_j\to Z\) by varying the \(j\)-th coordinate and fixing all other coordinates at the chosen \(p_i\). Because \(U\) is a lower set containing both \(a\) and \(b\), every point of \(\phi(Y_j)\) lies in \(U\). If the inclusion \(U\hookrightarrow Z\) were null-homotopic, then after composing with \(\phi\) and the projection \(Z\to X_j\), the natural inclusion
\[
\iota:Y_j\hookrightarrow X_j
\]
would be null-homotopic.

There is an order-preserving retraction \(r:X_j\to Y_j\): it fixes \(P_j\), \(a_j\), and \(b_j\), and sends every other top point to \(a_j\). Thus \(r\circ\iota=\operatorname{id}_{Y_j}\). Consequently a null-homotopy of \(\iota\) would make \(Y_j\) contractible.

We now show that \(Y_j=P_j\oplus D_2\) is not contractible. Delete beat points from \(P_j\) until reaching a Stong core \(C_j\). The same beat-point deletions remain valid after adjoining the two new maxima, so \(C_j\oplus D_2\) is a strong deformation retract of \(P_j\oplus D_2\). Since \(P_j\) is noncontractible, \(C_j\) has more than one point and has no greatest point. The space \(C_j\oplus D_2\) has no beat points: old lower sets are unchanged; an old maximal point sees two incomparable new points above it; any old nonmaximal point retains the absence of a least strict upper point; and each new maximum has strict lower set \(C_j\), which has no greatest point. Hence \(C_j\oplus D_2\) is a nonsingleton core, so it is noncontractible. This contradiction proves that a categorical open subset of \(Z\) contains at most one global maximum.

Every categorical open cover of \(Z\) must cover all \(M\) global maxima, so it has at least \(M\) members. Therefore
\[
\operatorname{cat}(Z)\ge M.
\]
Together with the principal-open cover,
\[
\operatorname{cat}(Z)=\operatorname{gcat}(Z)=M.
\]
The same one-coordinate argument with \(k=1\) gives \(\operatorname{cat}(X_i)=m_i\), establishing the multiplicative identity. Subtracting one from unreduced category yields the displayed reduced two-factor formula and defect.

## Verification
The proof above is symbolic and applies to all quantified finite spaces; finite computation is not used as an infinite proof. A supplementary verifier in `artifacts/verify.py` checks the order-theoretic mechanism on four representative products, including a three-factor case. It verifies the number of global maxima, the principal-open cover, the coordinate-slice containment for every pair of distinct maxima, absence of beat points in the tested two-top slices, and the explicit retractions. Its recorded output is in `artifacts/verify_output.txt` and ends with `VERIFY_OK cases=4 maximal_pairs=64`.

## Relationship to prior work
Fernández-Ternero, Macías-Virgós, and Vilches develop LS-category for finite spaces and give the standard upper bound from principal opens at maximal points. Scoville and Swei prove a multiplicative upper bound for simplicial LS-category of products, but not the exact finite-space product formula above. Mosquera-Lois and Tanaka prove the one-factor identity \(\operatorname{cat}(P\oplus D_m)=m\) for noncontractible \(P\), which is recovered here as the \(k=1\) case; their inspected treatment does not state the heterogeneous product theorem.

A previously obtained result for topological complexity of \(P\oplus D_m\) entails the equal-factor twofold category value as an intermediate consequence of its inequalities. The present theorem is not inferred from that diagonal case: it treats arbitrary finite products with unrelated noncontractible bases and unrelated cap sizes, and its proof supplies a coordinate-slice obstruction that yields exact multiplicativity and the explicit two-parameter subadditivity defect.

## Limitations
The theorem concerns ordinary and geometric LS-category of capped finite \(T_0\)-spaces. It does not classify products involving contractible bases, cap size \(1\), or general finite spaces. The supplementary enumeration only checks representative small capped antichain bases and is not evidence for the universal quantifiers; those rest on the symbolic proof. Targeted literature searches and full-text inspections found no statement implying the heterogeneous product theorem, but absence from the inspected sources is not a universal novelty certificate.

## References
1. D. Fernández-Ternero, E. Macías-Virgós, and J. A. Vilches, *Lusternik-Schnirelmann category of simplicial complexes and finite spaces*, arXiv:1501.07540v1, first public version 2015-01-29.
2. N. Scoville and W. Swei, *On the Lusternik-Schnirelmann category of a simplicial map*, arXiv:1606.01205v1, 2016.
3. M. Cárdenas, R. Flores, A. Quintero, and M. T. Villar-Liñán, *Covering-based numbers related to the LS-category of finite spaces*, arXiv:2209.14739; DOI:10.33044/revuma.3601.
4. D. Mosquera-Lois and K. Tanaka, *Weak, stable, and ordinary Lusternik-Schnirelmann category of finite spaces*, arXiv:2609.39615v1, 2026.
