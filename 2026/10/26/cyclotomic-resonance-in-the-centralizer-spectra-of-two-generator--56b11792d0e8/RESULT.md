# Cyclotomic resonance in the centralizer spectra of two-generator quantum complete intersections

## Finding
Fix a prime power \(Q\ge2\), an integer \(m\ge2\), and a nonzero field element \(\zeta\in\mathbb F_Q^\times\) of multiplicative order \(d\mid Q-1\). Consider the \(2m\)-dimensional associative algebra
\[
 A_{m,\zeta}=\mathbb F_Q\langle x,y\rangle/(x^2,y^m,xy-\zeta yx).
\]
For \(a\in A_{m,\zeta}\) write \(C(a)=\{b\in A_{m,\zeta}:ab=ba\}\), an \(\mathbb F_Q\)-linear subspace. The full distribution of \(\dim C(a)\), simultaneously for every \(Q,m,\zeta\), is described as follows.

Let \(J_d=\{j\in\mathbb Z:1\le j<m,\ d\nmid j\}\). Every \(a\) is uniquely \(f(y)+xg(y)\), with \(f,g\in\mathbb F_Q[y]/(y^m)\). Let \(t\) be the least \(j\in J_d\) with \([y^j]f\ne0\), or \(m\) if there is no such \(j\). Let \(s\) be the least index of a nonzero coefficient of \(g\), or \(m\) if \(g=0\). Put
\[
 r_d(t,s)=m-t+\#\{j\in\mathbb Z:1\le j<t-s,\ d\nmid j\}.
\]
Define nonnegative integers
\[
 F_t=\begin{cases}(Q-1)Q^{m-1-\#\{j\in J_d:j<t\}},&t\in J_d,\\ Q^{m-|J_d|},&t=m,\end{cases}\qquad
 G_s=\begin{cases}(Q-1)Q^{m-s-1},&0\le s<m,\\1,&s=m.\end{cases}
\]
Then \(\dim C(a)=2m-r_d(t,s)\), and the complete rank enumerator is
\[
 \boxed{Z_{m,d}(u)=\sum_{t\in J_d\cup\{m\}}\sum_{s=0}^{m}F_tG_s u^{r_d(t,s)}.}
\]
In particular, the number of elements with \(\dim C(a)=2m-r\) is \([u^r]Z_{m,d}(u)\), and two independent uniformly sampled elements commute with probability
\[
 \boxed{\operatorname{cp}(A_{m,\zeta})=Q^{-2m}Z_{m,d}(Q^{-1}).}
\]
This distribution depends on \(\zeta\) only through its multiplicative order \(d\).

If \(d\ge m\), then \(Z_{m,d}(u)=Q^2+\sum_{r=1}^{m-1}(Q^2-1)Q^{2r}u^r\), so
\[
 \boxed{\operatorname{cp}(A_{m,\zeta})=(Q+1)Q^{-m}-Q^{1-2m}.}
\]
At the first cyclotomic resonance \(m=3,d=2\), the multiplicities of ranks \(0,1,2\) are respectively \(Q^3,(Q^2-1)Q^3,(Q-1)Q^5\), giving \(\operatorname{cp}=2Q^{-2}-Q^{-4}\). This contrasts with the generic regime \(d\ge3\), where \(\operatorname{cp}=(Q+1)Q^{-3}-Q^{-5}\). A comparison of the two twists within a single field is available whenever that field admits elements of orders \(2\) and at least \(3\) (for example \(Q=5\)).

## Assumptions and scope
The algebra is unital and finite-dimensional. All field characteristics are permitted, including characteristic two; the case \(d=1\) is automatically included and is commutative. This theorem concerns additive-algebra commuting, not conjugacy in its unit group or commuting endomorphisms of unrelated representations. The degree-two relation \(x^2=0\) is essential to the proof; no claim is made for arbitrary exponent of \(x\).

## Proof
**Normal form and commutator.** Since \(yx=\zeta^{-1}xy\), the rewriting rules reduce each monomial to either \(y^i\) or \(xy^i\), with \(0\le i<m\). The skew-polynomial quotient supplies a basis of these \(2m\) monomials, so the decomposition \(a=f+xg\) is unique. Write \(R=\mathbb F_Q[y]/(y^m)\) and \(\Delta h=h(y)-h(\zeta^{-1}y)\). For \(a=f+xg\) and \(b=h+xk\), multiplication using \(x^2=0\) gives the exact identity
\[
 [a,b]=x\bigl(g\Delta h-k\Delta f\bigr).
\]
The map \(\Delta:R\to R\) is diagonal on monomials. Its image is precisely \(W_d=\operatorname{span}\{y^j:j\in J_d\}\), because \(1-\zeta^{-j}\) vanishes exactly when \(d\mid j\). Its value on \(f\) either vanishes or is \(y^t\) times a unit, hence \((\Delta f)R=y^tR\), an \((m-t)\)-dimensional subspace.

**Rank of the commutator.** The image of \(b\mapsto[a,b]\) is \(x\bigl((\Delta f)R+gW_d\bigr)\). If \(g=0\), set \(s=m\); otherwise \(g=y^s u\) with \(u\in R^\times\). For every \(j\in J_d\) with \(j<t-s\), the element \(gy^j\) has leading degree \(s+j<t\). These elements have distinct leading degrees and are linearly independent modulo \(y^tR\): in any linear combination, the smallest leading degree with nonzero scalar coefficient cannot cancel. Every \(gy^j\) with \(j\ge t-s\) is already in \(y^tR\). Thus the image has dimension
\[
 (m-t)+\#\{1\le j<t-s:d\nmid j\}=r_d(t,s),
\]
and rank-nullity gives \(\dim C(a)=2m-r_d(t,s)\).

**Distribution.** The \(m\) coefficients of \(f\) are independent and uniform. If \(t\in J_d\), all earlier coefficients in \(J_d\) must vanish and the coefficient at \(t\) must be nonzero, while every other coefficient is free: exactly \(F_t\) choices. For \(t=m\), all coefficients in \(J_d\) vanish, leaving \(F_m\) choices. The valuation \(s\) of \(g\) similarly has exactly \(G_s\) choices. Since \(f,g\) vary independently, summing \(F_tG_s\) establishes \(Z_{m,d}\). Each rank-\(r\) element commutes with exactly \(Q^{2m-r}\) elements, because its centralizer is an \((2m-r)\)-dimensional vector space. Dividing the total by \(Q^{4m}\) gives the commuting-probability formula. The formula contains \(\zeta\) only via \(d\).

**Generic case.** When \(d\ge m\), \(J_d=\{1,\dots,m-1\}\) and \(W_d=yR\). Then the commutator image is \(y^{\min(t,s+1)}R\), so its rank is \(m-\min(t,s+1)\). For \(1\le k\le m\), the number of pairs \((f,g)\) with \(\min(t,s+1)\ge k\) equals \(Q^{2m-2(k-1)}\): precisely the \(k-1\) coefficients \([y^j]f\) for \(1\le j<k\), and the \(k-1\) coefficients \([y^j]g\) for \(0\le j<k-1\), must vanish. Taking consecutive differences gives \(Q^2\) elements of rank zero and \((Q^2-1)Q^{2r}\) elements of rank \(r\) for \(1\le r<m\). Summing the weighted centralizer sizes gives the displayed rational commuting probability.

**First resonance.** When \(m=3,d=2\), \(J_d=\{1\}\). Consequently \(t=1\) contributes rank two for every \(s\), while \(t=3\) contributes ranks one (for \(s=0,1\)) and zero (for \(s=2,3\)). Using \(F_1=(Q-1)Q^2\), \(F_3=Q^2\), and the values of \(G_s\) yields the claimed three multiplicities and probability. All formulas remain valid for arbitrary prime powers because only field linear algebra is used.

## Verification
The standalone Python program `qci_verify.py` builds the full \(2m\)-dimensional multiplication table and independently computes the rank of each inner commutator using finite-field Gaussian elimination. It exhaustively checks \(158226\) prime-field algebra elements across ten parameter triples, performs another \(6000\) direct-matrix spot checks, and exhaustively checks \(8704\) elements over the extension field \(\mathbb F_4\). It checks predicted rank and the complete histogram against the direct calculations. The accompanying file `qci_verify_output.txt` preserves the actual results. Reproduce with `python3 qci_verify.py`. These finite experiments test the formula but are not a proof for arbitrary \(m,Q\); the preceding argument proves the theorem.

## Relationship to prior work
You and Zhang (2019) study the **same two-generator quantum complete-intersection algebra family** but classify indecomposable modules of low dimension; the accessible paper abstract does not state an all-element commutator-rank census. The full text was not accessible in this review, leaving residual priority uncertainty. Erdmann and Hellstrøm-Finnsen (2017) calculate Hochschild cohomology for related equal-exponent root-of-unity algebras; in degree zero this includes centers, but it does not imply distributions of centralizers of all individual algebra elements. Bergh, Erdmann, and Jorgensen (2019) study constant Jordan types of modules, a different parameter space and invariant. Huang (2021) counts matrix solutions to quantum-plane relations in arbitrary matrix dimension, rather than pairs of elements in this fixed finite-dimensional quotient algebra. Existing finite-ring commuting-probability and class-two commutator results do not directly specialize to the present family without an identification of the algebra and its rank strata. Numerical and center-only specializations are not claimed as individually novel.

## Limitations
The theorem applies to the exponent-two generator family only, not general higher two-generator nilpotent exponents. It gives the distribution of element-centralizer **dimensions** rather than a classification of all centralizer subalgebras. An earlier equivalent description under skew triangular algebras or finite ring commuting graphs might exist; the inaccessible full text of You–Zhang and any unindexed work are residual originality risks. The verification covers finite parameter values, not the universal statement independently. No external independent validation has been performed.

## References
1. H. You and P. Zhang, “Low dimensional modules over quantum complete intersections in two variables,” *Frontiers of Mathematics in China* 14 (2019), 449–474, DOI: 10.1007/s11464-019-0764-x (published online 2019-05-14).
2. K. Erdmann and M. Hellstrøm-Finnsen, “Hochschild cohomology of some quantum complete intersections,” arXiv:1703.05962v1 (2017).
3. P. A. Bergh, K. Erdmann, and D. A. Jorgensen, “Modules of constant Jordan type over quantum complete intersections,” arXiv:1910.06714v1 (2019).
4. Y. Huang, “Counting on the variety of modules over the quantum plane,” arXiv:2110.15570v1 (2021).
