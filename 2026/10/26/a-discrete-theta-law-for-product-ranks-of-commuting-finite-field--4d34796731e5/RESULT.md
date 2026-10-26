# A discrete theta law for product ranks of commuting finite-field idempotents

## Finding

Let \(q\) be any prime power and \(m\ge 1\). Independently choose \(E,F\) uniformly among the rank-\(2m\) idempotents in \(M_{4m}(\mathbb F_q)\). Condition on \(EF=FE\), and define \(Z_m=\operatorname{rank}(EF)-m\). Put
\[
\Phi_q=\prod_{h=1}^{\infty}(1-q^{-h}),\qquad
\Theta_q=\sum_{j\in\mathbb Z}q^{-4j^2}.
\]
Then \(Z_m\) converges **in total variation** to the nondegenerate symmetric lattice distribution
\[
\Pr(Z=j)=\frac{q^{-4j^2}}{\Theta_q}\quad (j\in\mathbb Z).
\]
The unconditioned commutativity probability has the sharp asymptotic
\[
\boxed{\displaystyle\lim_{m\to\infty}q^{4m^2}\Pr(EF=FE)=\frac{\Theta_q}{\Phi_q}.}
\]
In particular, commutativity among independently sampled balanced-rank idempotents has probability asymptotic to \(q^{-4m^2}\Theta_q/\Phi_q\), yet conditional product-rank fluctuations remain nontrivial on an integer scale. For \(q=2\), the limiting probability that \(\operatorname{rank}(EF)=m\), given commutativity, is approximately \(0.8888647769\).

More generally, for every \(n\ge0\), \(0\le r,s\le n\), and \(\max(0,r+s-n)\le t\le\min(r,s)\), the number of ordered commuting idempotent pairs \((E,F)\in M_n(\mathbb F_q)^2\) with \(\operatorname{rank}E=r\), \(\operatorname{rank}F=s\), and \(\operatorname{rank}(EF)=t\) is
\[
C_{n,q}(r,s,t)=\frac{|\operatorname{GL}_n(\mathbb F_q)|}{|\operatorname{GL}_{t}(\mathbb F_q)|\,|\operatorname{GL}_{r-t}(\mathbb F_q)|\,|\operatorname{GL}_{s-t}(\mathbb F_q)|\,|\operatorname{GL}_{n-r-s+t}(\mathbb F_q)|}.
\]
Outside that range the count is zero.

## Assumptions and scope

Matrices act on an \(n\)-dimensional vector space over \(\mathbb F_q\). An idempotent satisfies \(E^2=E\), and matrix rank is ordinary linear rank. All pairs are ordered. The asymptotic keeps \(q\) fixed while \(m\) grows through positive integers. Define \(\operatorname{GL}_0(\mathbb F_q)\) to have order \(1\). Every probability is with respect to the explicitly stated uniform finite sample space; the limiting distribution is conditional on the positive-probability event \(EF=FE\).

## Proof

**Joint-eigenspace decomposition.** Since \(E^2=E\), the minimal polynomial divides \(x(x-1)\), which is separable in every characteristic. If \(EF=FE\), the four operators
\[
EF,\qquad E(I-F),\qquad (I-E)F,\qquad (I-E)(I-F)
\]
are pairwise orthogonal idempotents summing to \(I\). Thus the vector space is their direct sum of images. The dimensions, in the displayed order, are precisely \(t,r-t,s-t,n-r-s+t\). Conversely, any ordered fourfold direct sum with these dimensions specifies exactly one ordered commuting pair \((E,F)\), by making each idempotent act as its prescribed zero/one scalar on the four summands. The general linear group acts transitively on such decompositions, and a decomposition has stabilizer the product of the four general linear groups on its components. Orbit-stabilizer proves the displayed exact count, including zero-dimensional factors. In particular, the number of rank-\(r\) idempotents is \(|\operatorname{GL}_n|/(|\operatorname{GL}_r||\operatorname{GL}_{n-r}|)\), as follows either from direct image/kernel decomposition or this orbit argument.

**Balanced specialization.** For \(n=4m\), \(r=s=2m\), let \(j=t-m\). The exact count of commuting pairs in the stratum \(Z_m=j\) is
\[
A_{m,j}=\frac{|\operatorname{GL}_{4m}|}{|\operatorname{GL}_{m+j}|^2\,|\operatorname{GL}_{m-j}|^2},\qquad -m\le j\le m.
\]
Define \(\phi_k=\prod_{h=1}^{k}(1-q^{-h})\), with \(\phi_0=1\), so \(|\operatorname{GL}_k|=q^{k^2}\phi_k\). Direct substitution gives
\[
\frac{A_{m,j}}{A_{m,0}}=q^{-4j^2}\frac{\phi_m^4}{\phi_{m+j}^2\phi_{m-j}^2}.
\]
The infinite product \(\Phi_q\) is positive because \(\sum_{h\ge1}q^{-h}<\infty\). Therefore \(\Phi_q\le\phi_k\le1\). For each fixed integer \(j\), the last expression converges to \(q^{-4j^2}\), and it is uniformly at most \(\Phi_q^{-4}q^{-4j^2}\) (interpret it as zero for \(|j|>m\)). The summable majorant permits dominated convergence on \(\mathbb Z\). Hence the normalized rank distribution converges pointwise, and in total variation, to the stated theta law.

**Sharp commutativity probability.** There are
\[
B_m=\frac{|\operatorname{GL}_{4m}|}{|\operatorname{GL}_{2m}|^2}
\]
rank-\(2m\) idempotents. Independence before conditioning yields
\[
q^{4m^2}\Pr(EF=FE)=
\frac{\phi_{2m}^4}{\phi_{4m}}
\sum_{j=-m}^{m}\frac{q^{-4j^2}}{\phi_{m+j}^2\phi_{m-j}^2}.
\]
The prefactor tends to \(\Phi_q^3\); by the same summable majorant, the sum tends to \(\Theta_q/\Phi_q^4\). Their product is \(\Theta_q/\Phi_q\), proving the asymptotic. No asymptotic assertion allows \(q\) to grow with \(m\).

## Verification

The standalone Python script `check_commuting_idempotents.py` enumerates all matrices over small prime fields, detects idempotence by direct multiplication, and tests commutativity and the rank of the product for each requested rank pair. It independently compares observed counts with the four-block group formula. Cases include all rank pairs for \((n,q)=(2,2),(3,2),(2,3),(3,3)\), plus the balanced pair \((r,s)=(2,2)\) for \((n,q)=(4,2)\). These cover \(372{,}920\) ordered sampled pairs, including \(21{,}280\) commuting balanced-rank pairs when \((n,q,r,s)=(4,2,2,2)\). The exact balancing-stratum counts there are \(560,20160,560\). The script and its literal recorded output are included. The arbitrary-prime-power theorem and infinite limit are proved algebraically; the checker uses prime fields and finite dimensions only.

## Relationship to prior work

Ferraz, Polcino Milies, and Taufer [1] count single idempotent generators of fixed-rank left ideals and provide matrix representatives. Their formulas support, but do not give, a balanced-rank **commuting pair** law or its lattice limit. Edmunds [2, Corollary 6.8 and Theorem 6.9] classifies commuting idempotent endomorphism pairs up to similarity in an elementary abelian setting; the simultaneous four-eigenspace decomposition is therefore not claimed as new. That paper counts similarity classes, not the weighted balanced-rank strata and sharp conditional theta-law/commutativity asymptotic proved here. Fulman and Guralnick [3, Theorem 1.1 and Section 2] study counts and asymptotics of unrestricted commuting matrix pairs and commuting nilpotents, which do not condition both matrices to be rank-half idempotents. The original contribution assessed here is the explicit **fixed-field balanced-rank conditioned lattice law together with its sharp commutativity-probability constant**. The finite orbit-count formula is included as a proof ingredient, not claimed as a new classification.

## Limitations

A different treatment in earlier semisimple-module counting or finite-field commuting-matrix literature might implicitly yield the same conditioned limit. The searched primary sources did not identify such a result; absence from those searches cannot establish unconditional publication priority. The general asymptotic concerns \(n=4m\), \(r=s=2m\) and fixed field order; it does not assert a phase diagram for other rank densities. Small-field enumeration verifies examples, not the infinite theorem.

## References

[1] R. A. Ferraz, C. Polcino Milies, E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289, first public version 2017-11-25, https://arxiv.org/abs/1711.09289.

[2] C. C. Edmunds, *Interchange Rings*, arXiv:1402.3699, 2014, https://arxiv.org/abs/1402.3699.

[3] J. Fulman, R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499, first public version 2016-11-16, https://arxiv.org/abs/1611.05499.
