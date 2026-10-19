# A sharp chronology threshold for directed and reciprocal epidemic contacts

## Finding

**Sharp phase-count theorem.** Consider a periodic, continuous-time susceptible–infectious–susceptible (SIS) model on \(N\geq 2\) population groups, with the same positive recovery rate in every group. Each of \(m\) prescribed nonnegative contact matrices occurs exactly once per period, for its prescribed positive duration. The disease-free invasion multiplier is independent of their chronological permutation for **every** admissible collection whenever \(m\leq 2\). If every contact matrix is symmetric (reciprocal contact), chronological invariance holds for **every** collection when \(m\leq 3\). Both bounds are sharp, already in two groups: with three **directed** phases, or with four **reciprocal** phases, permutations of the same fixed contact exposures can place one schedule strictly above and another strictly below the infection-invasion threshold. The examples below give exact crossing certificates and hold on open neighborhoods of their parameters.

Here 'sharp' refers to the minimal *number of positive-duration temporal phases*, not to the number of distinct numerical matrices; the four-phase example has repeated symmetric contact matrices, and admits arbitrarily small perturbations to four distinct symmetric matrices.

## Assumptions and scope

For each \(j\in\{1,\ldots,m\}\), choose \(Q_j\in\mathbb R_{\geq0}^{N\times N}\), duration \(\tau_j>0\), and common recovery \(\gamma>0\). During the phase with contact matrix \(Q_j\), the infected-fraction vector \(x\in[0,1]^N\) evolves according to
\[
\dot x_i=-\gamma x_i+(1-x_i)(Q_jx)_i\quad(i=1,\ldots,N).
\]
The disease-free linearization is \(\dot v=(Q_j-\gamma I)v\). For an ordering \(\pi\), let \(T=\sum_j\tau_j\) and \(F_j=\exp(\tau_jQ_j)\). With chronological order \(\pi_1,\ldots,\pi_m\) (first on the right in a matrix product), its one-period linear propagator is
\[
M_\pi=e^{-\gamma T}F_{\pi_m}\cdots F_{\pi_1}.
\]
The threshold is determined by \(\rho(M_\pi)\) being below or above one, with equality deliberately excluded from the claim. No matrix commutativity or equal durations are assumed. Symmetry means \(Q_j=Q_j^{\mathsf T}\), consistent with reciprocal, possibly weighted within- and between-group contacts; diagonal entries describe within-group transmission, not self-infection of one individual.

## Proof

**Universal impossibility with at most two phases.** The positive matrix exponentials \(F_j\) are invertible. For two phases, the two possible products \(F_2F_1\) and \(F_1F_2\) are similar: \(F_2F_1=F_2(F_1F_2)F_2^{-1}\). The common positive scalar \(e^{-\gamma T}\) does not change that fact. For one phase there is no permutation. Thus every Floquet eigenvalue is order-independent for \(m\leq2\), even for directed contacts and arbitrary dimension.

**Three reciprocal phases.** When all \(Q_j\) are symmetric, their exponentials \(F_j\) are also symmetric. For any three, the transpose of \(F_1F_2F_3\) is \(F_3F_2F_1\) and hence has the same characteristic polynomial; cyclic permutations of invertible factors have the same characteristic polynomial by similarity. The three cyclic orders together with their three reversals exhaust all six permutations. Therefore all have identical Floquet spectra, for every population dimension, and no three-phase reciprocal exposure schedule can change the invasion threshold.

**Directed three-phase sharpness.** Work in two groups, each phase of unit duration. Define
\[
Q_1=(\log2)\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
Q_2=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
Q_3=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
\gamma=\frac{\log4}{3}.
\]
Their exponentials are \(A=\operatorname{diag}(2,1)\), \(B=I+E_{12}\), and \(C=I+E_{21}\). The two products of the same three phase exposures (chronologies \(3,2,1\) versus \(2,3,1\)) are
\[
ABC=\begin{pmatrix}4&2\\1&1\end{pmatrix},\qquad
ACB=\begin{pmatrix}2&2\\1&2\end{pmatrix}.
\]
Their determinants both equal \(2\), but their traces are \(5\) and \(4\). Their Perron roots are respectively \((5+\sqrt{17})/2>4\) and \(2+\sqrt2<4\). Since \(e^{-3\gamma}=1/4\), their epidemic multipliers lie strictly on opposite sides of one. More structurally, replacing \(A\) by \(\operatorname{diag}(u,1)\), \(B\) by \(I+yE_{12}\), and \(C\) by \(I+zE_{21}\), gives the exact trace difference \(yz(u-1)>0\) for \(u>1\) and \(y,z>0\). The determinant is common and strictly positive, so the Perron root increases strictly with the trace (within this two-dimensional positive-matrix family).

**Reciprocal four-phase sharpness.** Again take two groups, with all durations one. Put
\[
Q_1=(\log2)E_{11},\quad
Q_2=Q_4=(\operatorname{arsinh}1)(E_{12}+E_{21}),\quad
Q_3=(\log2)E_{22},\qquad
\gamma=\frac{\log12}{4}.
\]
All four contacts are nonnegative and symmetric. Write \(A=\operatorname{diag}(2,1)\), \(D=\operatorname{diag}(1,2)\) and \(H=\begin{pmatrix}\sqrt2&1\\1&\sqrt2\end{pmatrix}\). Here \(\exp Q_1=A\), \(\exp Q_3=D\), \(\exp Q_2=\exp Q_4=H\), since \(\cosh(\operatorname{arsinh}1)=\sqrt2\). Two possible products are
\[
AHDH=\begin{pmatrix}8&6\sqrt2\\3\sqrt2&5\end{pmatrix},\qquad
ADHH=\begin{pmatrix}6&4\sqrt2\\4\sqrt2&6\end{pmatrix}.
\]
Both determinants are \(4\), while their traces are \(13\) and \(12\). The Perron roots are \((13+3\sqrt{17})/2>12\) and \(6+4\sqrt2<12\). Multiplying by \(e^{-4\gamma}=1/12\) proves the claimed opposite invasion verdicts. More generally let \(A=\operatorname{diag}(u,1)\), \(D=\operatorname{diag}(1,v)\), and \(H=\begin{pmatrix}\cosh h&\sinh h\\\sinh h&\cosh h\end{pmatrix}\), with \(u,v>1\) and \(h>0\). Then
\[
\operatorname{tr}(AHDH)-\operatorname{tr}(ADHH)=(u-1)(v-1)\sinh^2h>0.
\]
Both displayed threshold crossings are strict. Their continuation under sufficiently small changes of positive rates and durations follows from continuity of matrix exponentials and spectral radii, and a perturbation of \(Q_4\) distinct from \(Q_2\) therefore provides a genuinely four-distinct-contact example. The identical total contact durations and entries within each pair of schedules guarantee that the threshold difference is due solely to chronology, not changed aggregate exposure.

**Nonlinear SIS interpretation (strict cases only).** All four witness monodromy matrices have strictly positive entries. When \(\rho(M)<1\), the nonlinear flow is coordinatewise bounded above by the linear flow because \((1-x_i)(Q_jx)_i\leq(Q_jx)_i\); iteration of the period map yields extinction from every initial fraction. When \(\rho(M)>1\), the positive Perron eigenvector \(v\) gives a sufficiently small \(\epsilon v\) for which the period map strictly dominates \(\epsilon v\) (by differentiability at zero). The upper state \(\boldsymbol1\) is mapped below itself. Monotone iteration on \([0,1]^2\) supplies a strictly positive periodic SIS orbit. Consequently the two schedules have genuinely different qualitative outcomes: one allows endemic periodic persistence, while the other forces extinction. Uniqueness and global attraction of the positive orbit are not needed for this threshold-separation theorem and are not asserted here.

## Verification

Run `python verify.py` using Python 3 and SymPy. The program checks all four exact matrix products, traces, determinants and Perron roots; it evaluates the two parametric commutator/trace identities symbolically and checks permutation invariance for a separate triple of exact positive symmetric matrices. The strict inequalities are also justified analytically by the displayed radicals. The code supports—but cannot replace—the general all-dimension transpose/similarity proof. No unbounded computation or finite-search exhaustiveness assertion is used.

## Relationship to prior work

Temporal-network epidemic thresholds and propagator methods are established, including the infection and contact operators in Valdano, Colombi, Poletto and Colizza (2022 preprint; 2023 journal article). Their analyses treat richer contact and disease descriptions; they do not state this minimal phase-count dichotomy for reciprocal versus directed contacts or give the present same-exposure, opposite-invasion certificates in the inspected full text. Rocha and Masuda (2016) discuss transmission on temporally ordered contact networks; that qualitative chronology effect is not claimed new. Existing periodic SIS theory also links the linear invasion multiplier to persistence; the contribution here is the sharp universal ordering obstruction and two exact minimally phased counterexamples, not the threshold formalism itself.

## Limitations

The recovery rate is a *common scalar* and the exposure matrices are nonnegative; heterogeneous group-specific recovery or additional latent classes can invalidate transpose/similarity arguments. The reciprocal three-phase invariance concerns the **linear invasion threshold**, not necessarily trajectories or nonlinear transient outbreak sizes. The two reciprocal witness groups represent internally mixed subpopulations, including diagonal transmission. The result distinguishes strictly subcritical and supercritical schedules, not their critical equality cases. An undiscovered equivalent result in temporal positive-systems or epidemics literature remains a publication-priority risk, despite the specific comparisons documented in the accompanying review.

## References

1. E. Valdano, D. Colombi, C. Poletto, and V. Colizza, *Epidemic graph diagrams as analytics for epidemic control in the data-rich era*, medRxiv version 1, first posted 2022-10-11, DOI: 10.1101/2022.10.10.22280897; published in *Nature Communications* **14**, 8472 (2023), DOI: 10.1038/s41467-023-43856-1.
2. L. E. C. Rocha and N. Masuda, *Individual-based approach to epidemic processes on arbitrary dynamic contact networks*, *Scientific Reports* (2016), https://www.nature.com/articles/srep31456.
3. Source and reproducibility verification: the complete, self-contained `verify.py` accompanying this result.
