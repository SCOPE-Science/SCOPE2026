# Sharp reflection-length positive type and isolated reciprocal islands on alternating groups

## Finding

For every integer \(n\ge 3\), let \(A_n\) be the alternating group, let \(c(g)\) count *all* cycles of a permutation, including fixed points, and let \(m=\lfloor(n-1)/2\rfloor\). Define the central kernel on \(A_n\), for \(0\le q\le 1\), by
\[
K_{n,q}(g,h)=q^{\,n-c(g^{-1}h)},\qquad 0^0:=1.
\]
Then the complete positive-semidefiniteness criterion is
\[
\boxed{K_{n,q}\succeq0\ \Longleftrightarrow\ q\in[0,1/m]\ \cup\ \{1/j:1\le j<m,\ j\in\mathbb Z\}.}
\]
The kernel is strictly positive definite for \(0\le q<1/m\). Thus the largest continuous interval of positive type doubles asymptotically relative to the symmetric-group restriction, while finitely many isolated positive-type parameters persist above it. For instance, the admissible set is \([0,1/2]\cup\{1\}\) for \(n=5,6\), and \([0,1/3]\cup\{1/2,1\}\) for \(n=7,8\).

At the boundary \(q=1/m\), the *exact* nullity is
\[
\operatorname{nullity}K_{2m+1,1/m}=\tfrac12\binom{2m}{m}^{2}\qquad(m\ge1),
\]
\[
\operatorname{nullity}K_{2m+2,1/m}
=\binom{2m+1}{m}^{2}+\tfrac12\left(\frac{2m^2}{m+1}\binom{2m}{m}\right)^2\qquad(m\ge1).
\]
More generally, at any reciprocal parameter \(q=1/j\) with \(j\ge1\), the exact rank is
\[
\boxed{\operatorname{rank}K_{n,1/j}=\frac12\sum_{\substack{\lambda\vdash n\\ \ell(\lambda)\le j\ \mathrm{or}\ \lambda_1\le j}}(f^\lambda)^2,}
\]
where \(f^\lambda\) is the dimension of the Specht module indexed by \(\lambda\); terms for self-conjugate shapes are counted once in the indicated sum. The formula is valid also when \(j\ge n\), in which case the kernel has full rank.

## Assumptions and scope

Here \(A_n\subset S_n\) consists of the even permutations. The exponent \(n-c(g)\) is the minimum number of transpositions expressing \(g\) in \(S_n\), and is even when \(g\in A_n\). Positive semidefiniteness is for the whole finite matrix indexed by all \(|A_n|=n!/2\) group elements. The parameter domain is exactly the real interval \([0,1]\); equivalently the statement extends to \([-1,1]\) with \(q\) replaced by \(|q|\), since all exponents are even. Statements about positive definiteness always mean strictly positive quadratic forms on nonzero vectors.

For a partition \(\lambda\vdash n\), the Young-diagram content of cell \((i,j)\), with zero-based indices, is \(j-i\); its conjugate partition is \(\lambda'\). Put
\[
P_\lambda(q)=\prod_{(i,j)\in\lambda}(1+q(j-i)),\qquad
Q_\lambda(q)=\tfrac12\bigl(P_\lambda(q)+P_\lambda(-q)\bigr).
\]
The notation \(f^\lambda\) and the standard partition conventions have their usual representation-theoretic meanings; the hook-length formula may be used to calculate \(f^\lambda\).

## Proof

**1. Central Fourier eigenvalues.** The classical Frobenius characteristic identity and hook-content specialization give
\[
\sum_{g\in S_n}x^{c(g)}\chi_\lambda(g)
=f^\lambda\prod_{(i,j)\in\lambda}(x+j-i).
\]
It follows by substituting \(x=q^{-1}\) and multiplying by \(q^n\) that convolution with \(q^{n-c(g)}\) on the \(\lambda\)-isotypic part of the regular representation of \(S_n\) has scalar \(P_\lambda(q)\). For restriction to \(A_n\), average with the sign character; since \(\chi_{\lambda'}=\operatorname{sgn}\chi_\lambda\), this gives scalar \(Q_\lambda(q)\) for each pair \(\{\lambda,\lambda'\}\). If \(\lambda=\lambda'\), its restriction splits into two irreducibles exchanged by conjugation by an odd permutation, and the invariant central function has the same scalar \(Q_\lambda(q)=P_\lambda(q)\) on each. Hence \(K_{n,q}\succeq0\) if and only if \(Q_\lambda(q)\ge0\) for every \(\lambda\vdash n\).

**2. Sharp continuous positivity.** Fix \(m=\lfloor(n-1)/2\rfloor\) and \(0<q<1/m\). If a Young diagram has both first row and first column of length at most \(m+1\), all contents have absolute value at most \(m\); therefore both \(P_\lambda(q)\) and \(P_\lambda(-q)\) are strictly positive.

Otherwise conjugate the diagram if necessary to arrange first-row length \(L\ge m+2\). Its number \(t=n-L\) of cells outside the first row satisfies \(t\le m\); every negative content has magnitude at most \(t\). Among these \(t\) cells, the number with negative-content magnitude at least \(k\) is at most \(t-k+1\): any such cell requires the \(k-1\) distinct cells immediately below the upper-left corner in the first column, whose negative-content magnitudes are smaller than \(k\). By matching from largest to smallest, the negative-content magnitudes can therefore be injected into \(\{1,\ldots,t\}\) so that each matched positive integer is at least the corresponding negative-content magnitude.

For \(1\le r\le m\), the ratio \(R_q(r)=(1+qr)/(1-qr)\) is strictly increasing and exceeds one. Comparing the factors associated with the injected magnitudes with the positive-content factors \(1,\ldots,t\) in the first row shows
\[
P_\lambda(q)\ge\lvert P_\lambda(-q)\rvert.
\]
Indeed, every remaining positive-content factor contributes the ratio \((1+qr)/|1-qr|>1\), including those with \(r>m\); if any denominator vanishes, \(P_\lambda(-q)=0\) and the inequality holds directly. Since \(P_\lambda(q)>0\) and the first row contains additional positive contents, the comparison is strict. Consequently \(Q_\lambda(q)>0\). At \(q=0\) the kernel is the identity; continuity gives \(Q_\lambda(1/m)\ge0\).

**3. Isolated admissible reciprocals.** At \(q=1/j\), with \(j\) a positive integer, the function \(q^{n-c(g)}=j^{-n}j^{c(g)}\) is the normalized character of the action of \(S_n\) permuting tensor factors on \((\mathbb C^j)^{\otimes n}\). Its restriction to \(A_n\) is positive definite, so all the stated reciprocal parameters are admissible.

**4. Negative intervals and sharpness.** For each integer \(1\le k<m\), embed \(A_{2k+3}\) into \(A_n\) by fixing the remaining points. The restricted exponent \(n-c(g)\) equals \((2k+3)-c_{2k+3}(g)\), so the smaller kernel is a principal submatrix. For the self-conjugate hook partition \(\lambda=(k+2,1^{k+1})\) of \(2k+3\), its Fourier scalar is
\[
Q_\lambda(q)=\prod_{r=1}^{k+1}(1-r^2q^2).
\]
This scalar is strictly negative whenever \(1/(k+1)<q<1/k\), since precisely the last factor is negative. Thus every interval between adjacent reciprocals lying above \(1/m\) is excluded. Together with steps 2 and 3, this proves the exact criterion, including \(n=3,4\) where \(m=1\) and the entire parameter interval is admissible.

**5. Exact rank and endpoint nullity.** At \(q=1/j\), the hook-content product \(P_\lambda(1/j)\) is positive exactly when \(\ell(\lambda)\le j\), and is zero otherwise; similarly \(P_\lambda(-1/j)\) is positive exactly when \(\lambda_1\le j\). Thus an alternating-group irreducible sector is missing precisely when *both* \(\ell(\lambda)>j\) and \(\lambda_1>j\). The regular-representation multiplicity rule gives the displayed rank: a pair of conjugate shapes contributes \((f^\lambda)^2\), and a self-conjugate shape splits into two sectors contributing \((f^\lambda)^2/2\) together.

When \(n=2m+1\), the unique missing shape at \(j=m\) is the self-conjugate hook \((m+1,1^m)\), of dimension \(\binom{2m}{m}\). When \(n=2m+2\), the missing diagrams are the conjugate hooks \((m+2,1^m)\), \((m+1,1^{m+1})\) of dimension \(\binom{2m+1}{m}\), and the self-conjugate \((m+1,2,1^{m-1})\) of dimension \(\frac{2m^2}{m+1}\binom{2m}{m}\). Their squares yield the stated nullities by the same multiplicity rule.

## Verification

The standalone script `verify_alt.py` uses exact rational arithmetic, enumerates all partitions of orders \(3\le n\le13\), checks the scalar positivity classifications at the threshold, strictly inside the interval, at isolated reciprocals, and in excluded intervals, and confirms endpoint multiplicity formulas. It also constructs all \(60\times60\) rational kernel matrices for \(A_5\) at five parameters and verifies their definiteness and ranks by exact symmetric elimination. Its observed result is `VERIFY_OK exact checks: 92 ; orders n=3..13, direct matrices on A5`. This finite computation supports but does not replace the proof for all \(n\).

## Relationship to prior work

The finite-group central-positive-type criterion, Schur-Weyl representation at reciprocal parameters, and hook-content Fourier scalars are classical ingredients. The work of Leinen and Puglisi concerns positive definite functions on *infinite diagonal limits* of alternating groups, not the stated finite-order threshold. Zhang reviews Schur-Weyl theory and hook-content formulas; Bożejko, Dołęga, Ejsmont and Gal discuss reflection length and the discrete parameter picture for the infinite symmetric group while studying type B/C. The theorem here classifies each **finite** alternating group, yields the exact order-dependent continuous interval together with disconnected reciprocal islands, and determines endpoint rank losses. It is not a claim that these classical tools or the infinite-group parameter results are new.

## Limitations

The theorem concerns the cycle-count/transposition-reflection-length kernel on \(A_n\) only, with \(|q|\le1\); it makes no claim about general class functions or higher-dimensional representations of other groups. Finite computational checks do not prove universal assertions. A direct full-text comparison with the 2004 diagonal-limit paper was unavailable, so the originality comparison with that paper relies on its abstract and a difference in mathematical scope; possible earlier equivalent finite-group specializations remain a substantive literature risk. The result has not received independent mathematical validation.

## References

1. F. Leinen and O. Puglisi, *Positive definite functions of diagonal limits of finite alternating groups*, Journal of the London Mathematical Society 70 (2004), 678–690, DOI: 10.1112/S0024610704005691; publicly listed online 2004-12-03.
2. Lin Zhang, *Matrix Integrals over Unitary Groups: An Application of Schur-Weyl Duality*, arXiv:1408.3782 (first version 2014-08-17; later updates).
3. M. Bożejko, M. Dołęga, W. Ejsmont and Ś. R. Gal, *Reflection length with two parameters in the asymptotic representation theory of type B/C and applications*, arXiv:2104.14530 (first version 2021-04-29).
