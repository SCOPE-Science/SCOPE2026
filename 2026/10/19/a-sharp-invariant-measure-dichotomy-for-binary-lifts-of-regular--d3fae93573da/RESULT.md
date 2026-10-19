# A sharp invariant-measure dichotomy for binary lifts of regular Toeplitz words

## Finding
For each integer \(p_1\ge6\) and every sequence of integers \(q_k\ge4\), consider the regular Toeplitz words of Kang and Jäger, and the binary first-difference lift described below. This lift is minimal for every allowed parameter sequence. It is uniquely ergodic **if and only if** \(\sum_{k\ge1}q_k^{-1}=\infty\). If that sum is finite, it has **exactly two ergodic invariant probability measures** and its entire invariant-measure simplex is their closed line segment.

More precisely, put \(P_k=\prod_{j=k}^{\infty}(1-2/q_j)\), where the infinite product is interpreted as zero if it vanishes. Let \(C_{k,a}\) be the level-\(k\) odometer-aligned tower base with initial lifted symbol \(a\in\{0,1\}\). When the series converges, the two ergodic measures \(\mu_+\) and \(\mu_-\) satisfy
\[
\mu_{\pm}(C_{k,0})=\frac{1\pm P_k}{2p_k},\qquad
\mu_{\pm}(C_{k,1})=\frac{1\mp P_k}{2p_k}.
\]
For any invariant probability measure there is a parameter \(t\in[-1,1]\) such that
\[
\mu(C_{k,0})=\frac{1+tP_k}{2p_k},\qquad
\mu(C_{k,1})=\frac{1-tP_k}{2p_k}
\]
for every \(k\). The equations characterize the whole measure, not merely these marginals. The parameter \(t\) is unique when the series converges. When the series diverges, all parameters represent the same unique measure with \(\mu(C_{k,a})=1/(2p_k)\).

## Assumptions and scope
Let \(w_1=11 0^{p_1-3}\), of length \(p_1-1\). Define recursively
\[
w_{k+1}=(w_k0)^{q_k-3}\,w_k1\,w_k1\,w_k,
\qquad p_{k+1}=q_kp_k.
\]
The period-\(p_k\) skeleton is the periodic repetition of \(w_k\square\), with its final placeholder \(\square\) unfilled at level \(k\). The compatible skeletons determine the regular two-sided Toeplitz subshift \(Y\subset\{0,1\}^{\mathbb Z}\) through the standard Toeplitz orbit-closure construction. Its maximal equicontinuous factor has coordinates \(\rho_k:Y\to\mathbb Z/p_k\mathbb Z\) satisfying \(\rho_k(\sigma y)=\rho_k(y)+1\). The positive integer \(q_k\ge4\) ensures that the earlier placeholder occurs both as a zero and as a one before the next surviving placeholder, so the displayed periods form an essential nested structure.

Set
\[
X=\{x\in\{0,1\}^{\mathbb Z}:(x_{j+1}-x_j)\bmod2=y_j\text{ for some }y\in Y\}.
\]
Let \(\pi(x)_j=(x_{j+1}-x_j)\bmod2\), and define
\[
C_{k,a}=\{x\in X: \rho_k(\pi(x))=0,\ x_0=a\},\qquad a\in\{0,1\}.
\]
The level-\(k\) families \(\{\sigma^r C_{k,a}:0\le r<p_k,\ a\in\{0,1\}\}\) are finite clopen Kakutani–Rokhlin partitions (using the convention for the shift compatible with the displayed odometer equation). They are increasingly refined and generate the Borel sigma-algebra modulo every invariant probability measure. Their finitely many exceptional non-generating points have base phases at the unfilled residue for all large \(k\), a set of invariant measure zero.

## Proof
**1. Minimality and regularity.** Every skeleton has one unassigned position per period \(p_k\), hence hole density \(p_k^{-1}\to0\); consequently \(Y\) is regular, minimal and uniquely ergodic by the classical Toeplitz criterion. The word \(w_k\) has an even number of ones: the claim holds for \(w_1\) and the recursion adds two ones. Therefore a lifted phase is unchanged after \(w_k0\), is flipped after \(w_k1\), and has returned to its original value after the two exceptional ones. Since the return language contains both identity and phase-flip permutations, the two-state return action is transitive. The permutative-lift minimality criterion of Kang and Jäger (Theorem 1.5 and the proof of Theorem 6.13) then proves minimality of \(X\) for every stated sequence.

**2. Exact level-incidence calculation.** Fix a lifted symbol \(b\) at the beginning of a level-\(k+1\) block. Among the \(q_k\) successive level-\(k\) subblock beginnings, \(q_k-1\) carry symbol \(b\), and exactly one carries \(1-b\). Indeed, the repeated \(w_k0\) blocks keep phase \(b\); the first \(w_k1\) flips it at the next beginning; the second \(w_k1\) restores it. Thus the normalized incidence matrix is exactly
\[
M_k=\frac1{q_k}\begin{pmatrix}q_k-1&1\\1&q_k-1\end{pmatrix}.
\]
This is a count of actual lifted subblock starting symbols, rather than an assumption of independent random labels.

**3. All invariant measures.** Let \(\mu\) be shift invariant. Set \(v_{k,a}=p_k\mu(C_{k,a})\); then \(v_{k,0}+v_{k,1}=1\). Invariance and the tower refinement just proved give
\[
\begin{pmatrix}v_{k,0}\\v_{k,1}\end{pmatrix}
=M_k\begin{pmatrix}v_{k+1,0}\\v_{k+1,1}\end{pmatrix}.
\]
Conversely, a compatible sequence of two-component probability vectors determines consistent masses on every cell of every refined tower partition, hence an invariant Borel probability measure by compactness. The tower partitions determine it uniquely: for any fixed coordinate window, a level-\(k\) block and its starting symbol specify the lift throughout the window except when the window intersects the one unspecified symbol per \(p_k\) sites. Every invariant measure gives those exceptional phases mass at most the window length divided by \(p_k\), tending to zero. Thus no additional measures can reside in unresolved fibers.

**4. Exact dichotomy.** Put \(d_k=v_{k,0}-v_{k,1}\). The eigenvectors of \(M_k\) are \((1,1)\) with eigenvalue one and \((1,-1)\) with eigenvalue \(\beta_k=1-2/q_k\in[1/2,1)\). Therefore \(d_k=\beta_kd_{k+1}\). Since \(|d_{k+1}|\le1\), this implies \(|d_k|\le\prod_{j=k}^N\beta_j\) for all \(N\ge k\). If \(P_k=0\), every \(d_k\) vanishes and the invariant measure is unique. Otherwise \(d_k/P_k\) is independent of \(k\), and every constant \(t\in[-1,1]\) gives compatible vectors \(d_k=tP_k\). The set of all invariant probabilities is therefore affinely isomorphic to the closed interval \([-1,1]\); its two endpoints are precisely the ergodic measures. Finally, for \(q_k\ge4\), the logarithms of \(1-2/q_k\) are comparable to \(-1/q_k\); hence \(P_k>0\) precisely when \(\sum_{j\ge1}q_j^{-1}<\infty\). This proves all stated equivalences and formulas.

## Verification
The companion `verify.py` checks the exact phase distribution at successive block starts for \(p_1\in\{6,\ldots,12\}\), \(q\in\{4,\ldots,13\}\), the stochastic matrices and their nonconstant eigenvalues, and compositions of four such matrices by exact rational arithmetic. It also checks four nested word constructions. The computations are finite cross-checks only: the arbitrary-sequence result follows from the proof above. Run `python3 verify.py` with a standard Python 3 installation; no third-party packages are required.

## Relationship to prior work
Kang and Jäger, Theorem 6.13 (arXiv:2609.01140v1), introduced this Toeplitz word recursion and proved that some fast-growing period ratios give a minimal, non-uniquely-ergodic binary lift. The present theorem keeps their construction and extends the qualitative existence result to a complete parameter-by-parameter classification, with the exact measure simplex and observable tower-base masses. Their Theorem 5.4 gives a general criterion for unique ergodicity but does not state this explicit dichotomy.

Bezuglyi, Karpel and Kwiatkowski (arXiv:1709.00055v3) provide the general finite-rank Bratteli incidence-matrix theory behind measure-simplex calculations. The general matrix machinery is background, not a newly claimed method. The new identification is the rank-two stochastic incidence sequence for this specific minimal permutative Toeplitz lift and the resulting explicit sharp classification. Cortez, Drewlo, Gómez and Jäger (arXiv:2512.19921v1) construct Toeplitz systems with prescribed ergodic-measure counts in a different geometric framework.

## Limitations
This theorem applies to the displayed binary recursion with all \(q_k\ge4\); no classification of general Toeplitz subshifts, alternative filling schemes, or arbitrary permutative block codes is asserted. The exact two-ergodic-measure phase is a symbolic measure-theoretic statement, not a claim of spectral equivalence or mixing. General Bratteli theory may permit an alternate derivation. Independent originality review has not been performed.

## References
- Z. Kang and T. Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, first posted 2026-09-01; Sections 5 and 6.5, Theorem 6.13. https://arxiv.org/html/2609.01140v1
- S. Bezuglyi, O. Karpel and J. Kwiatkowski, *Exact number of ergodic invariant measures for Bratteli diagrams*, arXiv:1709.00055v3, particularly Sections 4 and 7.2. https://arxiv.org/html/1709.00055v3
- M. I. Cortez, J. Drewlo, J. Gómez and T. Jäger, *Constructing Toeplitz arrays via cut and project schemes*, arXiv:2512.19921v1. https://arxiv.org/html/2512.19921v1
