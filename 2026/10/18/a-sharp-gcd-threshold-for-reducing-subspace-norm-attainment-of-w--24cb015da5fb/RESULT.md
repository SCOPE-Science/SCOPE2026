# A sharp gcd threshold for reducing-subspace norm attainment of weighted-shift powers

## Finding
Let \(H=\ell_2(\mathbb N_0)\). For any unilateral weighted shift \(We_j=w_je_{j+1}\) satisfying \(0<|w_j|\leq1\) and \(|w_j|\to1\), write \(P_n(W)\) for the assertion that \(W^n\) attains its norm on every nonzero closed reducing subspace. For each integer \(n\geq1\), the exact criterion is
\[
P_n(W)\quad\Longleftrightarrow\quad
\forall r\in\{0,\ldots,n-1\}\ \exists k\geq0:\ k\equiv r\pmod n,
\quad |w_k|=\cdots=|w_{k+n-1}|=1.
\]
Moreover, for **every** pair of positive integers \(m,d\), the following sharp universal implication holds across this entire weighted-shift class:
\[
\boxed{\quad [\forall W,\ P_m(W)\Longrightarrow P_d(W)]
\ \Longleftrightarrow\ m\geq2d-\gcd(m,d).\quad}
\]
Whenever the inequality fails and \(\varepsilon>0\), there is a counterexample with strictly positive real weights for which \(W-S\) is compact and \(\|W-S\|<\varepsilon\), where \(S\) denotes the unweighted unilateral shift.

For the modulus-based subclass \(\beta_0(H)=\{T:|T|\in\beta(H)\}\), where \(\beta(H)\) denotes norm attainment on all nonzero reducing subspaces, an independent sharp criterion is
\[
\boxed{\quad W^n\in\beta_0(H)\ \Longleftrightarrow\
\#\{j\geq0:|w_j|<1\}<\infty.\quad}
\]
In particular, there are arbitrarily small compact perturbations of \(S\) for which **all** positive powers are in \(\beta(H)\), yet **none** are in \(\beta_0(H)\).

## Assumptions and scope
All Hilbert spaces are complex. A subspace reduces \(T\) when it is invariant under both \(T\) and \(T^*\). Norm attainment of a restriction means that the restricted operator maps some unit vector to a vector of its operator norm. The weights are bounded contractions, nonvanishing, and asymptotically of unit modulus; no monotonicity, phase restriction, or injective-weight hypothesis is used. The norm of every positive power is one, because the finite consecutive weight products converge to one. The claim concerns norm attainment under **reducing** subspaces, not arbitrary invariant subspaces.

## Proof
**Step 1 (exact one-power characterization).** Fix \(n\geq1\) and write
\[
c_{k,n}=\prod_{i=0}^{n-1}|w_{k+i}|\in(0,1],\qquad
W^ne_k=\left(\prod_{i=0}^{n-1}w_{k+i}\right)e_{k+n}.
\]
The mutually orthogonal spaces
\[
H_r=\overline{\operatorname{span}}\{e_{r+jn}:j\geq0\},
\qquad0\leq r<n,
\]
reduce \(W^n\). Since \(c_{r+jn,n}\to1\), the restriction of \(W^n\) to each \(H_r\) has norm one. It attains this norm precisely when \(c_{k,n}=1\) for some \(k\equiv r\pmod n\): indeed, for a unit vector \(x\in H_r\),
\[
\|W^nx\|^2=\sum_{k\equiv r\;(\mathrm{mod}\;n)}c_{k,n}^2|x_k|^2,
\]
whose value can equal one only if some supported coefficient has \(c_{k,n}=1\). For a product of numbers in \((0,1]\), this is equivalent to a length-\(n\) consecutive run of unit-modulus weights. This proves necessity of the criterion.

For sufficiency put \(T=W^n\), \(A=T^*T\), and \(E=\ker(I-A)\). The hypothesis supplies some coordinate vector \(e_k\in E\cap H_r\) in every residue class. Because all weights are nonzero, iterations of \(T\) and \(T^*\) move such a vector, up to nonzero scalars, to every coordinate vector of that residue class. Consequently
\[
\overline{\operatorname{span}}\{p(T,T^*)u:
\ u\in E,\ p\text{ a noncommutative polynomial}\}=H.
\]
If a nonzero closed subspace \(M\) reduces \(T\), its orthogonal projection \(Q\) commutes with \(T,T^*\), hence with \(A\) and with its spectral projection onto \(E\). If \(M\cap E=\{0\}\), then \(QE=0\), and commuting \(Q\) past every polynomial gives \(Q=0\) on the displayed dense span, a contradiction. Hence \(M\cap E\ne\{0\}\). Every unit vector in this intersection satisfies \(\|Tx\|=1\), so \(T|_M\) attains its (necessarily unit) norm. This proves sufficiency without a classification of all reducing subspaces.

**Step 2 (universal arithmetic implication).** Fix \(m,d\geq1\), put \(g=\gcd(m,d)\), and suppose \(m\geq2d-g\). In particular \(m\geq d\), and a unit-weight run of length \(m\) contains \(L=m-d+1\) possible starting positions for a run of length \(d\). Fix a target residue \(s\pmod d\). The set of allowed residues of the original block start is
\[
F_s=\{s,s-1,\ldots,s-(L-1)\}\pmod d.
\]
Its complement has at most \(g-1\) elements, because \(L\geq d-g+1\). The \(g\) residue classes modulo \(g\) partition \(\mathbb Z/d\mathbb Z\). At least one entire class therefore lies in \(F_s\). Choose a residue \(r\pmod m\) belonging to that class modulo \(g\), and use \(P_m(W)\) to obtain a length-\(m\) all-unit block starting at \(k\equiv r\pmod m\). Its residue modulo \(d\) belongs to \(F_s\), hence one of its \(L\) length-\(d\) subblocks starts at residue \(s\pmod d\). Since \(s\) was arbitrary, Step 1 proves \(P_d(W)\).

**Step 3 (sharp compact-perturbation counterexamples).** Suppose \(m<2d-g\). If \(m<d\), take \(m\) widely separated finite runs of unit weights, each of length exactly \(m\), whose starting indices traverse all residues modulo \(m\). No length-\(d\) unit run exists. If \(m\geq d\), put \(L=m-d+1\), so \(L\leq d-g\). Fix a residue \(s\pmod d\) and the above set \(F_s\), which is a cyclic interval of \(L\) residues. Its complement contains at least \(g\) consecutive residues; hence it meets every class modulo \(g\). For each \(r\pmod m\), choose \(a_r\pmod d\) outside \(F_s\) with \(a_r\equiv r\pmod g\). The generalized Chinese remainder theorem supplies infinitely many nonnegative integers \(k_r\) with
\[
k_r\equiv r\pmod m,\qquad k_r\equiv a_r\pmod d.
\]
Select them pairwise separated by more than \(m+d\). Set the weights on each \([k_r,k_r+m-1]\) equal to one, and everywhere else set
\[
w_j=1-\frac{\eta}{j+2},\qquad0<\eta<\min\{1,\varepsilon\}.
\]
The lengths of maximal all-unit runs are exactly \(m\). Every residue modulo \(m\) is represented, so \(P_m(W)\) holds. A length-\(d\) unit run must start inside a selected block, at some \(k_r+j\) with \(0\leq j<L\). By \(a_r\notin F_s\), this start is never congruent to \(s\pmod d\). Step 1 then shows \(P_d(W)\) fails. The same off-block weight formula works in the case \(m<d\). As \(w_j\to1\), the diagonal weighted difference \(W-S\) is compact; also \(\|W-S\|\leq\eta/2<\varepsilon\). This establishes sharpness for every failing ordered pair.

**Step 4 (distinction from modulus attainment).** The positive modulus \(|W^n|\) is diagonal with entries \(c_{k,n}\leq1\), tending to one. If \(\{j:|w_j|<1\}\) is infinite, then \(\{k:c_{k,n}<1\}\) is infinite. The closed span of the corresponding coordinate vectors reduces \(|W^n|\), and the restricted positive diagonal operator has norm one without a norming vector, so \(W^n\notin\beta_0(H)\). If there are only finitely many deficient weights, \(|W^n|\) has a finite set of distinct eigenvalues and its eigenspaces span \(H\). Every nonzero reducing restriction is a direct sum of some eigenspaces and attains its largest spectral value. Hence \(W^n\in\beta_0(H)\). Finally, take deficient weights only at \(j=2^k\) for \(k\geq2\), with \(w_{2^k}=1-\eta/(2^k+2)\), and all remaining weights equal to one. The gaps between defects tend to infinity, so for each \(n\) a single run of length at least \(2n-1\) realizes a length-\(n\) unit run starting in all \(n\) residues modulo \(n\). Thus every \(P_n(W)\) holds, while infinitely many defects make every \(W^n\notin\beta_0(H)\). The perturbation from \(S\) is compact and arbitrarily small by choosing \(\eta>0\) small.

## Verification
The analytic argument proves both directions for arbitrary positive integers and arbitrarily large Hilbert-space operators. As a supplementary consistency check, the standalone `POWER_CHECK.py` exhaustively compares the arithmetic condition with the finite residue-set criterion for all \(1\leq m,d\leq30\), and verifies explicit CRT counterexample supports for all failing pairs with \(1\leq m,d\leq12\). Invoke `python POWER_CHECK.py` in an ordinary Python 3 environment; no external dependencies are required. This finite check neither establishes the infinite-dimensional reducing-subspace lemma nor substitutes for the proof above.

## Relationship to prior work
Su and Zhang (2026) introduce the perturbation framework for \(\beta(H)\), formalize \(\beta_0(H)\), and exhibit a norm-attaining weighted shift with nonattaining modulus (Example 2.7). Their paper establishes density and compact-perturbation behavior, not the ordered-pair implication threshold for powers derived here. The 2018 study of common reducing subspaces of weighted shifts by Gu is relevant background for decomposing powers of shifts; the present argument avoids classifying all those subspaces. Earlier work by Ramesh and Osaka introduced the underlying reducing-subspace norm-attainment property; the available evidence did not establish the sharp gcd threshold. No uniqueness or publication priority is asserted on the basis of database searches.

## Limitations
Nonzero weights and convergence of their moduli to one are essential hypotheses of the proved criterion; neither zero weights nor general nonconvergent weights are treated. The result concerns the specific asymptotically isometric unilateral shift class, not every bounded operator. A potentially relevant earlier Ramesh--Osaka paper was accessible at abstract level but not in complete text during comparison, so priority under alternative terminology remains uncertain. Self-review is not an independent audit.

## References
1. Z. Su and Y. Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621, originally submitted September 29, 2026; especially Example 2.7 and Section 7.
2. C. Gu, *Common reducing subspaces of several weighted shifts with operator weights*, Journal of the Mathematical Society of Japan, 2018, DOI: 10.2969/jmsj/74677467.
3. G. Ramesh and H. Osaka, *On operators which attain their norm on every reducing subspace*, DOI: 10.1007/s43034-022-00167-8; complete text not available for comparison.
