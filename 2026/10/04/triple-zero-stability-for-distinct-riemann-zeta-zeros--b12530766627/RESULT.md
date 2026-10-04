# Triple-zero stability for distinct Riemann zeta zeros
## Finding
Assume the energy estimate and the seven-point local inequality stated as Propositions 5 and 6 of Knausgård's arXiv:2609.33043v1 for its fixed window. Let \(N(T)\) count nontrivial zeros \(\rho\) of the Riemann zeta function with \(0<\operatorname{Im}\rho\le T\), counted with multiplicity. Let \(N_d(T)\) count those zeros distinctly, and let \(N_3(T)\) count distinct zeros on \(\operatorname{Re}s=1/2\) having multiplicity exactly three. Then
\[
\frac{N_d(T)}{N(T)}\ge q_3+\gamma_3\frac{N_3(T)}{N(T)}-o(1),
\]
where
\[
q_3=\frac{165184514109253}{197357040825000}=0.8369831317836035\ldots,
\qquad
\gamma_3=\frac{138800000}{138496169}=1.002193786313324\ldots.
\]
Equivalently, with \(a=303831/69400000\) and \(\beta=341/158232\),
\[
(2-a)N_d(T)\ge (1+H-\beta)N(T)+2N_3(T)-o(N(T)),
\qquad H=\frac{3362285207}{5000000000}.
\]
The source's unconditional distinct-zero constant is \(q=16260119298029/19426831050000\). Thus this tradeoff exceeds that numerical constant whenever \(\liminf N_3(T)/N(T)>9.7283269540\times10^{-6}\). The statement does not assert that such a positive triple-zero density exists.

## Assumptions and scope
The two imported assumptions are exactly the source statements used in its proof: (i) the smoothed pair-correlation energy satisfies \(E_\varepsilon=(C(f_\varepsilon)+o(1))N\) with \(C(f)\le 2-H\), and (ii) its seven-point local inequality holds with pressure \(1/2736\) and \(\delta=891/200000\). No stronger property of the window is assumed.

The new algebraic lemma is independent of those numerical inputs. If \(U\) is Hermitian with unit diagonal, \(D=\operatorname{diag}(d_i)\) with \(1\le d_i\le M\), \(G=D^{1/2}UD^{1/2}\), \(\tau\ge0\), and \(c\ge\max(1+\tau,M+\tau/M)\), then the source's functions \(\phi_c\) and \(\Psi_\tau\) satisfy
\[
\operatorname{tr}\phi_c(G)-\operatorname{tr}D^2\ge\operatorname{tr}\Psi_\tau(U).
\]
The number-theoretic application uses \(M=3\), \(m=347\), \(\tau=1233/1000\), and \(c=3411/1000\).

## Proof
For the matrix lemma, repeat the source's proof with \(C\) obtained from \(U-I\) by clipping eigenvalues at \(\tau\), set \(M_0=D^{-1/2}CD^{-1/2}\), and use the dual matrix \(B=2D+2M_0\). The only place the source uses \(d_i\le2\) is the bound on \(d+\tau/d\). This function is convex on \([1,M]\), hence
\[
d+\frac{\tau}d\le\max\left(1+\tau,M+\frac{\tau}M\right)\le c.
\]
Thus \(B\preceq2cI\). The rest of the argument is unchanged: \(\operatorname{tr}M_0^2\le\operatorname{tr}C^2\) because \(d_i\ge1\), and the clipped-eigenvalue identity gives the displayed Gram inequality.

Now split the on-line distinct zeros into counts \(n_1,n_2,n_3\) of multiplicities \(1,2,3\), let \(h\) count on-line distinct zeros of multiplicity at least four, and let \(k\) count off-line symmetric pairs. Put the multiplicities \(1,2,3\) into \(D\). The source's rank argument still gives at most \(h+k\) positive eigenvalues in the remainder. Comparing the resulting energy lower bound with \(3N-2N_d\), a low on-line point of multiplicity \(d\le3\) contributes the residual
\[
d^2-(3d-2)=(d-1)(d-2),
\]
which is \(0,0,2\) for \(d=1,2,3\). A high on-line point of multiplicity \(d\ge4\) contributes at least
\[
r_h=8c-10-c^2,
\]
and an off-line pair contributes at least
\[
r_k=4c-2-c^2.
\]
Therefore
\[
E_\varepsilon\ge3N-2N_d+\operatorname{tr}\Psi_\tau(U)+2n_3+r_hh+r_kk.
\]

The source's block argument applies to all \(l=n_1+n_2+n_3=N_d-h-2k\) low-multiplicity points because its local inequality and pinching step depend only on their locations and the Gram matrix. For \(m=347\),
\[
\Delta_m=\frac{303831}{200000},\qquad
a=\frac{303831}{69400000},\qquad
\beta=\frac{341}{158232}.
\]
The exact choices \(\tau=1233/1000\) and \(c=3411/1000=3+\tau/3\) satisfy
\[
\tau^2-\Delta_m=\frac{567}{500000}>0,
\]
\[
r_h-a=\frac{980049629}{173500000}>0,
\qquad
r_k-2a=\frac{112103}{347000000}>0.
\]
Using the source bound that the total spread is \(N+o(N)\), then its energy upper bound \(C(f)\le2-H\), gives
\[
(2-a)N_d\ge(1+H-\beta)N+2n_3+(r_h-a)h+(r_k-2a)k-o(N).
\]
Dropping the two nonnegative final terms proves the claim.

For the maximal-block statement within this same scheme, \(a_m=\delta(1-6/m)\) increases with \(m\), while any admissible \(\tau\) obeys \(\tau^2\ge(m-6)\delta\) and \(c\ge3+\tau/3\). At \(m=348\), \(\sqrt{\Delta_{348}}>12343/10000\). Since \(4c-2-c^2\) decreases for \(c>2\), every admissible choice at \(m\ge348\) has
\[
r_k-2a_m< -\frac{23501321}{26100000000}<0.
\]
Hence \(m=347\) is the largest feasible block length if the off-line residual is required to remain nonnegative after the block penalty.

## Verification
The file `verify.py` uses exact rational arithmetic to recompute all constants, the two parameter inequalities, the high-point and off-line residual margins, the affine coefficients \(q_3\) and \(\gamma_3\), the threshold against the source constant, and the exact \(m=348\) obstruction. Its recorded output is in `verify_output.txt`.

The verifier checks arithmetic consequences only. The infinite theorem is established by the proof above from the two explicitly stated source inputs; finite computation is not used as a substitute for that argument.

## Relationship to prior work
Knausgård, arXiv:2609.33043v1, proves a mixed-multiplicity Gram inequality only for diagonal weights \(1\le d_i\le2\), and its counting split places multiplicity at least three into the high-multiplicity remainder. The paper explicitly describes its new defect as retained for points of multiplicity one or two. The present result moves the first omitted multiplicity into the Gram block, where triple zeros contribute an additional residual \(2\) per distinct triple zero.

Wang, arXiv:2609.24167v1, refines a different finite-multiset inequality by retaining a spectral defect only on simple real points; it does not give a multiplicity-three defect term or the affine tradeoff above. Alpöge--Furman, arXiv:2608.13637v2, and Lamzouri, arXiv:2609.02882v1, establish earlier simple/distinct bounds but likewise do not imply this triple-zero-sensitive inequality.

## Limitations
The stated zeta consequence is conditional on the exact energy and seven-point local inequalities quoted from arXiv:2609.33043v1. Their underlying analytic and computer-assisted inputs are not independently re-certified here. In particular, this result does not upgrade the review status of those source computations. It also does not prove that triple zeros have positive density or even that any triple zero exists.

The \(m=347\) maximality statement is only for this specific seven-point pressure/block scheme together with the requirement \(r_k-2a\ge0\). It is not an impossibility theorem for other kernels, other local certificates, or other counting decompositions.

## References
1. K. M. Knausgård, *More than 83.69% of the zeros of the Riemann zeta function are distinct*, arXiv:2609.33043v1, 2026.
2. B. Wang, *Proportions of the non-trivial zeros of the Riemann zeta function*, arXiv:2609.24167v1, 2026.
3. L. Alpöge and R. Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637v2, 2026.
4. Y. Lamzouri, *A new proof that more than \(2/3\) of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, 2026.
5. S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, and C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376; arXiv:2306.04799.
