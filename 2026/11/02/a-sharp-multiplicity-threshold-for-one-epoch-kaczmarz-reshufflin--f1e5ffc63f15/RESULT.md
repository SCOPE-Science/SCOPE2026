# A sharp multiplicity threshold for one-epoch Kaczmarz reshuffling reversal

## Finding

For every integer \(m\ge 2\), consider the consistent planar linear system with \(m-1\) copies of the normalized row \(a=(1,0)\) and one normalized row \(b=(\sqrt{k},\sqrt{1-k})\), where \(0<k<1\), and zero right-hand side. Start the unrelaxed Kaczmarz iteration from \(e_0=a\). Compare, after exactly \(m\) projections, (RR) a uniformly random permutation of the \(m\) *labeled* rows and (IID) \(m\) independent uniform draws of labeled rows. Both use the same number of row projections and both systems have full column rank.

Write \(\mathcal B\) for the exceptional row type and \(\mathcal A\) for the repeated type. Conditionally on the first IID type being \(\mathcal B\), let \(N_m\) count switches between successive types in the length-\(m\) sequence. Define \(G_m(k)=\mathbb E[k^{N_m}\mid\mathcal B\text{ first}]\). With \(p=1/m\) and \(q=1-p\), its exact computable polynomial is

\[
G_m(k)=(1,0)\begin{pmatrix}p&qk\\pk&q\end{pmatrix}^{m-1}\begin{pmatrix}1\\1\end{pmatrix}.
\]

The **exact endpoint mean-squared solution errors** are

\[
R_{\mathrm{RR}}(m,k)=\frac{(1-k)k}{m},\qquad
R_{\mathrm{IID}}(m,k)=\frac{1-k}{m}G_m(k).
\]

For \(m=2\), RR is strictly better for every \(0<k<1\). For **every** \(m\ge3\), there is **exactly one** threshold \(\kappa_m\in(0,1)\), characterized by \(G_m(\kappa_m)=\kappa_m\), and

\[
R_{\mathrm{RR}}\begin{cases}<R_{\mathrm{IID}},&0<k<\kappa_m,\\=R_{\mathrm{IID}},&k=\kappa_m,\\>R_{\mathrm{IID}},&\kappa_m<k<1.\end{cases}
\]

In particular, \(\kappa_3=1/2\) and \(\kappa_4=(\sqrt{17}-4)/3\). The threshold collapses superexponentially:

\[
\kappa_m\sim \frac{m^{-(m-1)}}{1-e^{-1}}\quad (m\to\infty).
\]

For each fixed \(k\in(0,1)\), the RR-to-IID risk ratio converges to \(e^{1-k^2}\); by first taking \(m\to\infty\) and then \(k\downarrow0\), this ratio approaches \(e\).

At \(m=3\), \(b=(4/5,3/5)\), RR has risk \(48/625\) whereas IID has risk \(1179/15625\), so RR is worse by exactly \(21/15625\). The reversal is not dependent on identical rows: the three pairwise nonparallel normalized rows

\[
(1,0),\quad(312/313,25/313),\quad(4/5,3/5)
\]

with initial error \((1,0)\) have exact RR-minus-IID risk

\[
\frac{234845527130732528}{396688687243963171875}>0.
\]

By continuity, that witness lies in an open family of distinct-row systems with the same strict comparison.

## Assumptions and scope

Every row is a real unit vector, every equation has right-hand side zero, and all computations use exact unrelaxed orthogonal projection \(P_v=I-vv^\top\) onto the nullspace of its row. The unknown solution is the origin, since the two row directions are nonparallel. Rows are *labeled* even when coefficients coincide, so IID selects the repeated type with probability \((m-1)/m\), and random permutation gives the exceptional type first with probability \(1/m\). The performance criterion is the expected squared Euclidean error after one epoch of exactly \(m\) individual updates from the stated deterministic starting error, not the operator norm or a stationary rate.

## Proof

**1. Projection-word identity.** The two nullspace lines of \(a\) and \(b\) have squared cosine \(k\). If the first projection is of type \(\mathcal A\), it annihilates \(e_0=a\) forever. A first \(\mathcal B\) projection instead leaves a vector of squared norm \(1-k\). Every subsequent projection onto the same nullspace line preserves its norm, whereas a switch to the other line multiplies the squared norm by \(k\). Thus for a word starting with \(\mathcal B\), the final squared norm is exactly \((1-k)k^N\), where \(N\) is its type-switch count.

**2. Two exact risk formulas.** Under a random labeled-row permutation, only the event that the exceptional row occurs first survives; this event has probability \(1/m\), and all subsequent projections have type \(\mathcal A\). There is exactly one switch, proving the RR formula. Under IID sampling, the exceptional type is first with probability \(1/m\). Each subsequent type is independently \(\mathcal B\) with probability \(p=1/m\) and \(\mathcal A\) with probability \(q=1-p\). The weighted transition matrix, with state order \((\mathcal B,\mathcal A)\), is

\[
T_m(k)=\begin{pmatrix}p&qk\\pk&q\end{pmatrix}.
\]

The \((\mathcal B,\mathcal A)\)-initial row vector \((1,0)\) and terminal all-ones vector therefore give \(G_m(k)\) and the IID formula.

**3. Unique transition.** Set \(c_{m,j}=\Pr(N_m=j\mid\mathcal B\text{ first})\). Then \(G_m(k)=\sum_{j=0}^{m-1}c_{m,j}k^j\), with nonnegative coefficients summing to one and

\[
c_{m,0}=m^{-(m-1)}>0,\qquad
G'_m(1)=\frac{m-1}{m}+\frac{2(m-2)(m-1)}{m^2}.
\]

The derivative counts one initial transition with probability \(q\), then \(m-2\) possible later switches, each of probability \(2pq\). For every \(m\ge3\), \(G'_m(1)>1\) because \(2m^2-7m+4>0\). Moreover \(c_{m,2}>0\), hence \(h_m(k)=G_m(k)-k\) is strictly convex on \((0,1)\). Since \(h_m(0)>0\), \(h_m(1)=0\), and \(h'_m(1)>0\), there is a unique zero \(\kappa_m\in(0,1)\), with \(h_m\) positive below and negative above it. Since \(R_{\mathrm{RR}}-R_{\mathrm{IID}}=(1-k)(k-G_m(k))/m\), this proves the claimed sharp sign classification. At \(m=2\), \(G_2(k)=(1+k)/2>k\).

Direct multiplication yields

\[
G_3(k)=\frac{1+6k+2k^2}{9},\qquad
G_4(k)=\frac{1+39k+15k^2+9k^3}{64},
\]

and \(G_3(k)-k=(k-1)(2k-1)/9\), \(G_4(k)-k=(k-1)(9k^2+24k-1)/64\). These establish the displayed exact two thresholds.

**4. Sharp multiplicity asymptotic.** For \(m\ge3\), the zero- and one-switch coefficients satisfy

\[
c_{m,0}=m^{-(m-1)},\qquad
c_{m,1}=\sum_{r=1}^{m-1}p^{r-1}q^{m-r}\longrightarrow e^{-1}.
\]

The one-switch event consists precisely of an initial run of the exceptional type followed exclusively by the repeated type. Writing \(G_m(k)=c_{m,0}+c_{m,1}k+E_m(k)\), the remaining nonnegative coefficients imply \(0\le E_m(k)\le k^2\) for \(0\le k\le1\). For any fixed \(C>(1-e^{-1})^{-1}\), we have \(G_m(Cc_{m,0})-Cc_{m,0}<0\) for large \(m\). Uniqueness then implies \(\kappa_m\le Cc_{m,0}\). Inserting the threshold equation and this bound gives \(\kappa_m=c_{m,0}/(1-c_{m,1})+O(c_{m,0}^2)\), proving the asymptotic.

For fixed \(k\in(0,1)\), among the \(m-1\) IID choices following the first exceptional row, the number of exceptional choices converges in distribution to \(J\sim\mathrm{Poisson}(1)\). The probability of an exceptional choice immediately after the first, at the last position, or adjacent to another exceptional choice is \(O(1/m)\). Outside those events, the number of switches equals \(1+2J\). Boundedness of \(k^{N_m}\) then implies

\[
G_m(k)\longrightarrow k\mathbb E[k^{2J}]=k e^{k^2-1},
\]

hence the claimed limiting risk ratio.

**5. Distinct-row witness.** Apply \(P_v=I-vv^\top\) to the initial vector \((1,0)\) for each of the six permutations of the three stated rational unit vectors, and for each of the 27 length-three IID words. Their exact rational mean-squared norms differ by the strictly positive fraction displayed in the Finding. The standalone verifier performs the full enumeration without floating-point operations. The expectation difference is continuous in the row vectors, so this is an open, nonparallel-row phenomenon.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It checks probability normalization, exact switch-count coefficients and first moments through \(m=14\), the two low-dimensional polynomial identities, and exact rational projection enumeration through \(m=6\), including the explicit three-distinct-row witness. The script reports 245 exact-rational assertions passed. This finite verification supports, but is not substituted for, the general convexity and asymptotic proofs above.

## Relationship to prior work

Ferreira, Acebrón and Monteiro (arXiv:2401.02842, initially posted 2024-01-05) experimentally favor sampling without replacement for several consistent systems; this result establishes a precise initial-error exception in a deliberately redundant but full-column-rank system. Han and Xie (arXiv:2410.01140, initially posted 2024-10-02) prove linear convergence and upper bounds for random reshuffling Kaczmarz, not this one-epoch comparison. The 2026 work of Liu (arXiv:2606.32005) compares *convergence-rate guarantees* for shuffled and with-replacement stochastic gradient methods with much smaller stepsizes, not pointwise Euclidean errors at the full Kaczmarz projection step. Existing two-row finite-time comparisons cover nonduplicated two-row systems with a potentially relaxed step, but cannot imply the unique all-multiplicity threshold or its superexponential collapse. Standard exact IID MSE recurrences in randomized Kaczmarz do not by themselves identify the permutation switch law or its threshold.

## Limitations

This is an exact one-epoch, particular-start, two-dimensional family result. It does not assert that RR is worse for all initial states, all matrices, every epoch, or in worst-case complexity, nor does it contradict asymptotic convergence theorems. The main exact threshold uses repeated identical rows, although an exact all-distinct witness shows this phenomenon is robust. Published-priority uncertainty persists for specialized finite-order row-selection comparisons not located by the searches.

## References

1. I. A. Ferreira, J. A. Acebrón, J. Monteiro, *Survey of a Class of Iterative Row-Action Methods: The Kaczmarz Method*, arXiv:2401.02842, first posted 2024-01-05, https://arxiv.org/abs/2401.02842.
2. D. Han, J. Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, arXiv:2410.01140, first posted 2024-10-02, https://arxiv.org/html/2410.01140.
3. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005, first posted 2026-06-30, https://arxiv.org/abs/2606.32005.
4. A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
