# A sharp three-row reshuffling boundary for planar Kaczmarz mean-square error

## Finding

For the consistent planar system with normalized rows \(a_1=a_2=(1,0)\) and \(a_3=(c,s)\), \(c^2+s^2=1\), \(s>0\), put \(u=c^2\). One epoch means three orthogonal Kaczmarz updates. Compare a uniformly shuffled permutation of the three *labeled* rows (RRK) with three independent uniformly drawn row labels (RK). For every deterministic initial error \(e\in\mathbb R^2\), let \(R_{\mathrm{RR}}(e)\) and \(R_{\mathrm{iid}}(e)\) denote the respective expected squared Euclidean errors after the epoch.

Writing \(P=I-a_1^\top a_1\) and \(Q=I-a_3^\top a_3\), the exact comparison is
\[
R_{\mathrm{iid}}(e)-R_{\mathrm{RR}}(e)
=\frac{1-u}{27}\,e^\top\big[(8+5u)P+(1-2u)Q\big]e.
\]
Consequently, RRK is **uniformly no worse for every initial error** precisely when \(0\le u\le\tfrac12\), and is strictly better for every nonzero error when \(0\le u<\tfrac12\). At \(u=\tfrac12\) the comparison is positive semidefinite of rank one. For \(\tfrac12<u<1\), the comparison has both signs: RRK is worse on some initial errors and better on others. This is a sharp \(45^\circ\) angle/coherence boundary in the repeated-measurement family.

The worse-RRK direction can always be chosen \(e=(1,0)\). At \(c=4/5\), \(s=3/5\), with all row labels sampled uniformly,
\[
R_{\mathrm{RR}}(e)=\frac{48}{625},\qquad
R_{\mathrm{iid}}(e)=\frac{1179}{15625},\qquad
R_{\mathrm{RR}}(e)-R_{\mathrm{iid}}(e)=\frac{21}{15625}>0.
\]
This reversal persists after small distinct-row perturbations. Moreover, with only two normalized planar rows, RRK cannot be worse in expected squared error for any initial vector, so three row labels are the first possible size for a reversal of this type.

## Assumptions and scope

The coefficient matrix is the \(3\times2\) matrix with the three displayed rows, and the right-hand side is zero (equivalently, translate a consistent nonzero system by its unique solution). Since \(s>0\), the matrix has full column rank. We use the exact orthogonal-projection Kaczmarz step \(x\mapsto x-\langle a_i,x\rangle a_i\) for unit row \(a_i\), with no relaxation or momentum. The two identical rows are separate labeled observations; in iid sampling each has probability \(1/3\), so \(P\) is selected with probability \(2/3\) and \(Q\) with probability \(1/3\). Both protocols use exactly three individual projection evaluations. Statements concern exactly one epoch and expectations conditional on an arbitrary deterministic initial error; no independence between epochs is assumed or needed.

## Proof

The matrices \(P,Q\) are symmetric rank-one orthogonal projectors onto the lines perpendicular to the two distinct row directions. Their line inner-product modulus squared is \(u=c^2\). Therefore \(PQP=uP\) and \(QPQ=uQ\).

There are three equally likely locations for \(Q\) among the three reshuffled updates. If \(B\) denotes their chronological product, the three possible products are \(QP\), \(PQP\), and \(PQ\), because \(P^2=P\). Thus the exact reshuffling Gram matrix is
\[
S:=\mathbb E_{\mathrm{RR}}(B^\top B)
=\frac13\big[PQP+(PQP)^2+QPQ\big]
=\frac13\big[(u+u^2)P+uQ\big].
\]

For independent uniform draws, let the Gram-channel map be \(\mathcal L(H)=(2PHP+QHQ)/3\). Because products are formed chronologically from independent symmetric projections, their expected Gram matrix after three draws is \(T=\mathcal L^3(I)\). The identities above imply
\[
\mathcal L(P)=\frac{2P+uQ}{3},\qquad
\mathcal L(Q)=\frac{2uP+Q}{3},\qquad
\mathcal L(I)=\frac{2P+Q}{3}.
\]
Iterating on the two-dimensional span of \(P,Q\) gives
\[
T=\frac1{27}\big[(8+6u+4u^2)P+(1+6u+2u^2)Q\big].
\]
Subtracting the two exact matrices yields
\[
D:=T-S=\frac{1-u}{27}\big[(8+5u)P+(1-2u)Q\big].
\]
If \(u\le\tfrac12\), both coefficients are nonnegative. For \(u<\tfrac12\), they are positive, while the two projector ranges span \(\mathbb R^2\), hence \(D\) is positive definite. If \(u=\tfrac12\), only the \(P\) term survives. For \(\tfrac12<u<1\), the determinant has the exact value
\[
\det D=\frac{(1-u)^3(8+5u)(1-2u)}{729}<0,
\]
so \(D\) is indefinite. In particular, with \(e=(1,0)\), \(Pe=0\) and \(e^\top Qe=1-u\), whence
\[
R_{\mathrm{iid}}(e)-R_{\mathrm{RR}}(e)
=\frac{(1-u)^2(1-2u)}{27}<0.
\]
The rational example follows from \(R_{\mathrm{RR}}(e)=u(1-u)/3\) and \(R_{\mathrm{iid}}(e)=(1-u)(1+6u+2u^2)/27\), evaluated at \(u=16/25\).

The strict difference at this witness is a continuous function of the three unit-row directions; therefore, it remains positive throughout an open neighborhood, which includes systems with three pairwise distinct rows. One explicit such rational system is \(a_1=(1,0)\), \(a_2=(399/401,40/401)\), \(a_3=(4/5,3/5)\), for which direct exact-arithmetic enumeration gives a strictly positive RRK-minus-RK error gap on \(e=(1,0)\).

Finally, for any two unit planar rows with distinct projection matrices \(P,Q\) and their squared line inner-product \(u\in[0,1]\), direct enumeration of two permutations versus four independent draws gives
\[
\mathbb E_{\mathrm{iid}}(B^\top B)-\mathbb E_{\mathrm{RR}}(B^\top B)
=\frac{1-u}{4}(P+Q)\succeq0.
\]
This proves the asserted minimality in number of row labels for planar full-epoch comparisons.

## Verification

The self-contained Python 3 standard-library file `verify.py` enumerates all six labeled permutations and all 27 independent triples using exact rational matrices. It reproduces the Gram coefficients at five Pythagorean rational directions, the determinant identity, the exact \(21/15625\) reversal, a three-distinct-row rational witness, and the two-row formula. Execute `python verify.py` alongside this document. The universal continuous-angle conclusions follow from the displayed algebraic identities, not from finite sampling or the verifier alone.

## Relationship to prior work

Han and Xie [1, Algorithm 1 and Sections 3.1–3.3] formulate the actual reshuffled Kaczmarz updates and establish deterministic per-permutation linear-convergence bounds. Their comparisons with independent-sampling RK use upper bounds and experiments, not an exact fixed-initial-vector one-epoch Gram ordering on these three rows. Recht and Ré [2, Conjecture 3.1] consider spectral-operator-norm inequalities for averages of noncommutative products and motivate Kaczmarz comparison. Their low-length norm comparison does not entail positive-semidefinite ordering of the *expected Gram matrices*, which is the metric examined here. Lai and Lim [3] prove the three-factor operator-norm arithmetic–geometric mean inequality and exhibit failures at five factors; the different three-factor Gram-form ordering established here is compatible with that norm result. De Sa [4] gives higher-length failures for noncommutative matrix inequalities and learning tasks, without this rank-one projector angle classification. Oswald and Zhou [5] analyze shuffled-SOR/Kaczmarz convergence bounds rather than the exact one-epoch comparison. A later metric-aware synthesis [6] emphasizes the distinction among operator norms, mean iterates, and expected quadratic errors on other matrix families; its available summary does not supply the present three-row identity. Earlier exact mean-square analyses by Agaskar, Wang and Lu [7] and Bai and Wu [8, Theorem 2.1] already give a general Kronecker transfer formula for **independently sampled Kaczmarz** on full-column-rank consistent systems. In particular, the iid Gram matrix here can be recovered from those results. The new assertion is therefore **not** an exact-MSE formula for iid Kaczmarz in isolation: it is the comparison with the without-replacement Gram, the sharp Loewner phase boundary, its minimality, and a distinct-row reversal.

## Limitations

The all-initial-vector boundary is proved for precisely two repeated normalized planar measurements and a third distinct direction, not arbitrary three-row matrices or arbitrary dimension. The three-distinct-row result proves existence by continuity and one exact example, not a full classification for distinct rows. The reversal is for Euclidean solution-error second moments after three updates; it is not a counterexample to established three-factor *operator-norm* inequalities, nor a claim that reshuffling has a worse long-run convergence rate or larger error bound in general. No independent external audit is claimed. Potential overlap with inaccessible extended versions of relevant matrix-product literature remains possible.

## References

[1] D. Han and J. Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, arXiv:2410.01140 (first public version 2024-10-02), https://arxiv.org/abs/2410.01140; full text https://arxiv.org/pdf/2410.01140.

[2] B. Recht and C. Ré, *Toward a noncommutative arithmetic–geometric mean inequality: conjectures, case-studies, and consequences*, COLT 2012, arXiv:1202.4184, https://arxiv.org/pdf/1202.4184.

[3] Z. Lai and L.-H. Lim, *Recht–Ré noncommutative arithmetic–geometric mean conjecture is false*, ICML 2020, arXiv:2006.01510, https://arxiv.org/pdf/2006.01510.

[4] C. M. De Sa, *Random reshuffling is not always better*, NeurIPS 2020, https://proceedings.neurips.cc/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html.

[5] P. Oswald and W. Zhou, *Random reordering in SOR-type methods*, Numerische Mathematik 135 (2017), arXiv:1510.04727, https://arxiv.org/pdf/1510.04727.

[6] *Exact Low-Length Recht–Ré Inequalities and Metric-Dependent Rankings in Random Reshuffling Dynamics*, unrefereed 2026 release summary, https://evidencepress.org/releases/exact-low-length-recht-re-inequalities/. The second manuscript's PDF was not accessible during comparison.

[7] A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, IEEE GlobalSIP 2014, pp. 389–393, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b. The public abstract was inspected; the full PDF was unavailable during comparison.

[8] Z.-Z. Bai and W.-T. Wu, *On convergence rate of the randomized Kaczmarz method*, Linear Algebra and its Applications **553** (2018), 252–269, https://doi.org/10.1016/j.laa.2018.05.009. The publicly indexed full HTML text, including Theorem 2.1 and Eqs. (2.1)–(2.3), was examined.
