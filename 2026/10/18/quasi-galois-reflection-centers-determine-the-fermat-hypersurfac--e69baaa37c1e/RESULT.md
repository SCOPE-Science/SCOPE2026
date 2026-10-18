# Quasi-Galois reflection centers determine the Fermat hypersurface

## Finding
Let \(r\ge3\) and \(d\ge4\) be integers, and let \(F\subset\mathbb P^{r-1}_{\mathbb C}\) be the Fermat hypersurface \(\sum_{i=1}^{r}X_i^d=0\). Denote by \(\mathcal Q\) the **non-Galois** quasi-Galois points of \(F\), i.e. those with projection-preserving group of order two. Then
\[
\operatorname{Stab}_{\operatorname{PGL}_r(\mathbb C)}(\mathcal Q)
= (\mu_d^{r}/\mu_d)\rtimes S_r,
\]
where \(\mu_d\) is embedded diagonally. In particular, \(\mathcal Q\), without including or marking any Galois point, intrinsically recovers all \(r\) outer Galois centers as intersections of its \(\binom r2\) maximally populated lines. The Fermat hypersurface is the **unique smooth degree-\(d\) hypersurface** preserved by this projective stabilizer.

## Assumptions and scope
Work throughout over \(\mathbb C\). Fix integers \(r\ge3\), \(d\ge4\). A projective automorphism preserves a hypersurface when it takes its underlying zero locus to itself. The finite set of non-Galois quasi-Galois centers is, by Miura--Takahashi (Theorem 1.8 and Remark 4.7),
\[
\mathcal Q=\left\{[e_i-\zeta e_j]:1\le i<j\le r,\;\zeta^d=1\right\}.
\]
The designated \(r\) outer Galois centers \([e_i]\) are *excluded* from \(\mathcal Q\). No claim is made for \(d=3\), for positive characteristic, or for arbitrary non-Fermat hypersurfaces.

## Proof
Write \(L_{ij}=\mathbb P(\mathbb C e_i+\mathbb C e_j)\). Each \(L_{ij}\) contains exactly \(d\) points of \(\mathcal Q\).

**Intrinsic recognition of the coordinate lines.** Let \(L\) be any other projective line, and regard its underlying vector plane as \(W\). Let \(s\) be the number of coordinate functionals that restrict nontrivially to \(W\). Necessarily \(s\ge3\), because a line with only two active coordinates would equal some \(L_{ij}\). Each of these \(s\) nonzero linear functionals has exactly one zero in \(\mathbb P(W)\). A point of \(L\cap\mathcal Q\) has exactly two nonzero coordinate values, so exactly \(s-2\) active coordinate functionals must vanish there. Distinct such points give disjoint groups of vanishing functionals. Thus the number of points in \(L\cap\mathcal Q\) is at most \(\lfloor s/(s-2)\rfloor\), which is at most \(3\) for every \(s\ge3\). Since \(d\ge4\), the \(L_{ij}\) are **exactly** the lines containing at least four points of \(\mathcal Q\), and indeed precisely the maximally populated lines.

**Recovery of Galois centers.** The intersections among the lines \(L_{ij}\) are precisely the coordinate vertices \([e_i]\), with each vertex incident to \(r-1\ge2\) such lines. This constructs the vertex set canonically from \(\mathcal Q\), even though none of these vertices belongs to \(\mathcal Q\). Consequently every projective stabilizer of \(\mathcal Q\) permutes the projectively independent vertices and is represented by a monomial matrix. After composing with a coordinate permutation, it is diagonal: \(g=\operatorname{diag}(\lambda_1,\ldots,\lambda_r)\). On \(L_{ij}\), it preserves the root-of-unity coset \(\{[e_i-\zeta e_j]:\zeta^d=1\}\) exactly when \((\lambda_j/\lambda_i)^d=1\). Requiring this for every pair gives \(\lambda_i^d=\lambda_j^d\) for all \(i,j\). Modulo a common scalar, the diagonal group is precisely \(\mu_d^{r}/\mu_d\). Conversely this diagonal group and all coordinate permutations preserve \(\mathcal Q\), proving the group formula.

**Unique smooth invariant degree-\(d\) hypersurface.** Let \(H\) be a smooth degree-\(d\) hypersurface invariant under this group, defined by a form \(f\). Since its principal defining ideal is preserved, every projective stabilizer acts on \(f\) by a scalar. Restrict to the diagonal \(\mu_d^{r}/\mu_d\). Each monomial of total degree \(d\) has weight its exponent vector modulo \(d\). Two *distinct* monomials of total degree \(d\) can carry the same weight only if they are two pure powers \(X_i^d\) and \(X_j^d\). Therefore either \(f\) is a single monomial or it is a linear combination \(\sum_i c_iX_i^d\). A monomial of degree at least four defines a non-smooth hypersurface in \(\mathbb P^{r-1}\), so only the latter case is possible. Smoothness forces every \(c_i\ne0\). A transposition of two coordinates fixes some third coordinate (as \(r\ge3\)); since it scales the defining polynomial, comparison of the fixed third coefficient shows that the scalar is one, and then \(c_i=c_j\). Thus all \(c_i\) are equal and \(H=F\). Conversely the Fermat hypersurface is smooth and invariant. This completes the proof.

## Verification
The standalone `check.py` exhaustively constructs finite-field analogues of the reflection-center configuration in six small cases with characteristic prime to \(d\), enumerates all lines spanned by pairs of centers via exact Plücker minors, and confirms that precisely \(\binom r2\) lines have \(d\) centers while all other spanned lines have at most three. These checks substantiate the incidence mechanism but the proof above, not finite enumeration, establishes the full complex infinite family. Run `python3 check.py` from the package root.

## Relationship to prior work
Miura--Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties* (arXiv:2610.09331v1), Theorem 1.8 and Remark 4.7, **already provide the exact centers and their count**; Theorem 4.1 recalls the monomial automorphism group of Fermat varieties. None of these inputs is claimed here as new. The contribution is the converse projective-rigidity result for the **unlabelled non-Galois centers alone**, plus reconstruction of excluded Galois centers and uniqueness of a smooth invariant degree-\(d\) hypersurface. Fukasawa--Miura--Takahashi, *Quasi-Galois points, II: Arrangements* (arXiv:2211.16033), treats incidence and extremal counts for plane curves, including the Fermat quartic; it does not assert the all-dimensional ambient point-set stabilizer and smooth-invariant uniqueness formulated here. The classical monomial symmetry group by itself gives only the inclusion from hypersurface symmetries into configuration symmetries, not the converse.

## Limitations
The theorem concerns the projective-linear stabilizer, not the full abstract automorphism group of a K3 surface, which may be larger. It relies on the known complete center classification for Fermat varieties. Incidence recognition fails with the same argument at \(d=3\), since noncoordinate lines can meet the center set at three points. No extension to characteristic dividing \(d\) is claimed. Although inspected sources do not state the converse rigidity, a logically equivalent observation may occur in unindexed projective-arrangement literature.

## References
1. K. Miura and T. Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331v1 (publicly submitted 2026-10-07), Theorem 1.8, Theorem 4.1, Proposition 4.5, Remark 4.7.
2. S. Fukasawa, K. Miura and T. Takahashi, *Quasi-Galois points, II: Arrangements*, arXiv:2211.16033; J. Math. Soc. Japan 77 (2025), 979--1008.
3. S. Fukasawa, K. Miura and T. Takahashi, *Quasi-Galois points, I: Automorphism groups of plane curves*, Tohoku Math. J. 71 (2019), 487--494, doi:10.2748/tmj/1576724789.
4. K. Miura and S. Taki, *Quasi-Galois points for quartic surfaces*, arXiv:2608.25445 (2026).
