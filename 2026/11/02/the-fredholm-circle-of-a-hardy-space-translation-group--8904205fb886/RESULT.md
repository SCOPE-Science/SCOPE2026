# The Fredholm circle of a Hardy-space translation group

## Finding
For the bounded group \(T_\tau\) introduced by Manzur and Noor, the ordinary and Fredholm essential spectra coincide:
\[
\sigma(T_\tau)=\sigma_{\mathrm{ess}}(T_\tau)=
\begin{cases}
\{1\},&\tau=0,\\
\{\lambda\in\mathbb C:|\lambda|=1\},&\tau\in\mathbb R\setminus\{0\}.
\end{cases}
\]
Here the essential spectrum uses the Fredholm definition. For nonzero \(\tau\), every point of the circle has a weakly null unit approximate-eigenvector sequence. Therefore all points off the circle belong to the resolvent, while no point on it is Fredholm; the Fredholm index is zero at every resolvent point.

## Assumptions and scope
Work on the complex Hardy Hilbert space \(H^2(\mathbb D)\) with its orthonormal monomial basis \(e_n(z)=z^n\) for \(n\ge0\). For a real parameter \(\tau\), define \(T_\tau\) initially on polynomials by
\[
T_\tau e_0=e_0,\quad
T_\tau e_n=(n+1)^{i\tau}e_n+\big((n+1)^{i\tau}-n^{i\tau}\big)\sum_{k=0}^{n-1}e_k\quad(n\ge1),
\]
using real logarithms in complex powers. The cited primary paper establishes bounded extension, the group law \(T_\tau T_\sigma=T_{\tau+\sigma}\), and \(\|T_\tau\|\le1+2|\tau|\). Define \(\sigma_{\mathrm{ess}}(T)=\{\lambda:T-\lambda I\text{ is not Fredholm}\}\). No assumption about zeta zeros or the Riemann hypothesis enters this spectral classification.

## Proof
For every positive integer \(k\), the group law and bound imply
\[
\|T_\tau^k\|=\|T_{k\tau}\|\le1+2k|\tau|,
\qquad
\|T_\tau^{-k}\|=\|T_{-k\tau}\|\le1+2k|\tau|.
\]
Thus the spectral-radius formula gives \(r(T_\tau)\le1\) and \(r(T_\tau^{-1})\le1\). Invertibility and spectral mapping for inverses imply that every spectral value has modulus exactly one.

For \(n\ge1\), set \(\lambda_n=(n+1)^{i\tau}\). Directly from the monomial formula,
\[
\|(T_\tau-\lambda_n I)e_n\|=
\sqrt n\,\big|(n+1)^{i\tau}-n^{i\tau}\big|
\le\frac{|\tau|}{\sqrt n}.
\]
The inequality follows by \(|e^{ix}-1|\le|x|\) and \(\log(1+1/n)\le1/n\). When \(\tau\ne0\), the real sequence \(|\tau|\log(n+1)\) is increasing and unbounded, and its successive differences tend to zero. Hence its residues modulo \(2\pi\) are dense: for each angle, successive crossings of that angle plus integer multiples of \(2\pi\) approximate it with error at most one increment. It follows that \(\{\lambda_n:n\ge1\}\) is dense in the complex unit circle.

Given \(|\lambda|=1\), select strictly increasing \(n_j\) with \(\lambda_{n_j}\to\lambda\). Then
\[
\|(T_\tau-\lambda I)e_{n_j}\|
\le |\tau|/\sqrt{n_j}+|\lambda_{n_j}-\lambda|\longrightarrow0.
\]
The orthonormal sequence \(e_{n_j}\) converges weakly to zero. Were \(T_\tau-\lambda I\) Fredholm, an Atkinson left parametrix would satisfy \(B(T_\tau-\lambda I)=I-K\), where \(B\) is bounded and \(K\) compact. Applying this identity to \(e_{n_j}\), the left side tends to zero but \(\|(I-K)e_{n_j}\|\to1\), a contradiction. Thus every point on the circle lies in the Fredholm essential spectrum. Combining this with the upper spectral inclusion proves both equalities. At \(\tau=0\) the formula gives \(T_0=I\), whose ordinary and Fredholm essential spectra are both \(\{1\}\) on this infinite-dimensional space.

## Verification
The critical calculations are the published bounded group law, the polynomial estimate on powers, and the explicit column residual above. Reproduce the finite numerical checks using `python3 check.py`; they check the displayed monomial relation, elementary residual estimate and finite-section group law for sample parameters. The infinite spectral conclusions use the full mathematical arguments, not the finite computations.

## Relationship to prior work
Manzur and Noor, arXiv:2610.03568v1 (first publicly submitted October 2, 2026), construct the group to act on kernel vectors encoding zeta-zero questions. They establish its boundedness, group law, and intertwining relation but do not determine ordinary or Fredholm essential spectra. The present result uses their exact operator, proves a complete spectral classification, and separates these unconditional spectral invariants from the more delicate invariant-subspace criterion.

The compact generalized Cesàro operators studied by Albanese and coauthors in *Generalized Cesàro operators in the disc algebra and in Hardy spaces* have a discrete spectrum; those are different operator families, and their result does not imply the circle result here. The standard Hardy and Copson operators are useful background but likewise do not determine the Fredholm essential spectrum of this phase-dependent upper-triangular group.

## Limitations
This is a spectral result for the specific group on scalar complex \(H^2\); it does not prove or disprove the Riemann hypothesis, characterize invariant subspaces, or determine eigenvector completeness, the operator norm, pseudospectra, or finite-dimensional compressions. Although available searches found no equivalent formula, prior operator-group or weighted-Copson theory under different terminology remains a possible priority risk. Independent mathematical validation has not been performed.

## References
1. J. Manzur and W. Noor, *A Hardy-space operator acting on zeta-zeros*, arXiv:2610.03568v1, October 2, 2026, https://arxiv.org/html/2610.03568v1.
2. A. A. Albanese, J. Bonet, and W. J. Ricker, *Generalized Cesàro operators in the disc algebra and in Hardy spaces*, Advances in Operator Theory, published online October 22, 2024, https://link.springer.com/article/10.1007/s43036-024-00396-9.
3. G. H. Hardy, J. E. Littlewood, and G. Pólya, *Inequalities*, second edition, Cambridge University Press, 1952 (classical Hardy/Copson boundedness).
