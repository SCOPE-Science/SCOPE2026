# Mass-ratio phase changes for centered \(L^2\) maximal averages on weighted stars

## Finding

For a finite star with \(q\ge2\) equal-mass leaves and hub mass \(h>0\), the exact squared strong \(L^2\) norm of centered graph-ball Hardy–Littlewood maximal averaging is the maximum of only \(2\binom{q+2}{2}\) explicitly specified matrix eigenvalues, each of size at most four. This evaluates the norm for every \(q,h\), without optimizing over input functions or exponentially many radius assignments. Extremizers may always be chosen with at most three distinct absolute values on the leaves.

The hub-mass limits have distinct exact structures. Set
\[
\Phi(t)=\frac{2-t+\sqrt{t(4-3t)}}2.
\]
Then
\[
\lim_{h\downarrow0}\|M_{q,h}\|_{2,h}^2=\max_{1\le k<q}\Phi(k/q).
\]
For each fixed \(q\) there is a finite \(H_q\) such that **for every** \(h>H_q\),
\[
\|M_{q,h}\|_{2,h}^2=\Phi\bigl(q/(h+q)\bigr)
=1+\sqrt{q/h}-\frac{q}{2h}+O_q(h^{-3/2}).
\]
On that high-mass tail, every extremizer has equal absolute values on all leaves, strictly larger than its hub absolute value.

Even on the three-vertex path (\(q=2\)), hub weighting creates three rigorously distinct optimal radius patterns. At \(h=1/10\) the maximizing selector applies radius zero at the hub, radius one at one leaf, and radius two at the other leaf: every absolute-value extremizer breaks the symmetry between the equal-mass leaves. Its sharp squared norm is the largest real root of
\[
53361z^3-127281z^2+79300z-10000=0,
\]
which is \(1.448834067224\ldots\). At \(h=1\), both leaves select radius one and the squared norm is \((7+\sqrt{33})/8\) (the uniform-mass benchmark already known from the literature). At \(h=100\), the hub selects radius two, both leaves select radius zero, and the squared norm is \((101+\sqrt{201})/102\). Each named selector is strictly optimal up to interchange of the leaves, so by continuity these patterns persist on three nonempty open mass intervals; at least two changes of optimal pattern occur as mass increases. No assertion is made that these are the only changes.

## Assumptions and scope

Let the graph have vertex set \(\{o,v_1,\ldots,v_q\}\) with unit graph edges \(ov_i\) and no other edges. Equip \(o\) with measure \(h>0\), and each leaf with measure one. For an arbitrary real input \(f\), write \(a=|f(o)|\), \(b_i=|f(v_i)|\), and
\[
\mu=\frac{ha+\sum_{i=1}^q b_i}{h+q},\qquad
\nu_i=\frac{ha+b_i}{h+1}.
\]
The centered maximal operator is exactly
\[
M_{q,h}f(o)=\max\{a,\mu\},\quad
M_{q,h}f(v_i)=\max\{b_i,\nu_i,\mu\},
\]
with weighted Hilbert norm \(\|f\|_{2,h}^2=h|f(o)|^2+\sum_i|f(v_i)|^2\). The quantity called its strong norm is the optimal constant \(\sup_{f\ne0}\|M_{q,h}f\|_{2,h}/\|f\|_{2,h}\), not a linear-operator norm in the sense of additivity. All statements concern centered *graph-ball* averages, not arbitrary vertex subsets or uncentered balls.

To state the finite spectral formula, choose a hub radius selector \(r\in\{I,G\}\), standing for the singleton ball and global ball. Partition the leaves into groups selected by \(I\) (singleton), \(N\) (leaf-plus-hub), and \(G\) (global ball), of cardinalities \(k_I,k_N,k_G\ge0\), \(k_I+k_N+k_G=q\). Put \(H_I=1\), \(H_G=h/(h+q)\), and let \(\delta_{r,G}\) be one or zero according as \(r=G\) or not. Define the real matrix, with rows and columns ordered \((o,I,N,G)\),
\[
B_{r,k}=\begin{pmatrix}
 H_r & \delta_{r,G}\frac{\sqrt{h k_I}}{h+q} & \delta_{r,G}\frac{\sqrt{h k_N}}{h+q} & \delta_{r,G}\frac{\sqrt{h k_G}}{h+q}\\
 0&1&0&0\\
 \frac{\sqrt{h k_N}}{h+1}&0&\frac1{h+1}&0\\
 \frac{\sqrt{h k_G}}{h+q}&\frac{\sqrt{k_G k_I}}{h+q}&\frac{\sqrt{k_G k_N}}{h+q}&\frac{k_G}{h+q}
\end{pmatrix}.
\]
For any zero group size, delete its corresponding row **and** column. Write \(\lambda_{\max}\) for the largest eigenvalue of a real symmetric matrix. The exact formula is
\[
\boxed{\ \|M_{q,h}\|_{2,h}^2
=\max_{r\in\{I,G\}}\ \max_{k_I+k_N+k_G=q}
\lambda_{\max}\bigl(B_{r,k}^{\mathsf T}B_{r,k}\bigr).\ }
\]
Only nonnegative integer triples are used. In total, \(2\binom{q+2}{2}\) small eigenproblems suffice.

## Proof

**(1) Selector reduction.** For nonnegative inputs, each output of \(M_{q,h}\) is the maximum of two or three nonnegative *linear* averages. Squaring and summing nonnegative weighted outputs therefore commutes with the independent finite maximum over choices at each vertex. Since every selector matrix \(A\) has nonnegative entries, \(\|A|x|\|_{2,h}\ge\|Ax\|_{2,h}\) for real \(x\), so its full weighted Hilbert norm is achieved on a nonnegative vector. Interchanging the finite maximum and supremum gives the exact identity
\[
\|M_{q,h}\|_{2,h}^2=\max_{\text{all radius selectors }A}\|A\|_{2,h\to2,h}^2.
\]
The number of raw selectors is \(2\cdot3^q\).

**(2) Exact compression.** For any fixed selector, its leaf radius groups can be relabeled as three consecutive blocks of sizes \(k_I,k_N,k_G\). The positive semidefinite matrix \(A^{\mathsf T}WA\), where \(W=\operatorname{diag}(h,1,\ldots,1)\), is equivariant under independent permutations *within each group* (with the corresponding input and output permutations). A nonnegative top generalized eigenvector of \((A^{\mathsf T}WA,W)\) exists: entrywise absolute value preserves or improves the Rayleigh quotient of a maximizing vector. Averaging that nonnegative vector over within-group permutations produces a nonzero top eigenvector constant on each group. On the weighted-normalized group coordinates \(\sqrt h\,a\), \(\sqrt{k_I}\,b_I\), \(\sqrt{k_N}\,b_N\), \(\sqrt{k_G}\,b_G\), the selector acts precisely as \(B_{r,k}\). The display above follows by writing the four possible output group averages explicitly. This proves the finite formula and the existence of a maximizing absolute-value input with at most three leaf levels.

**(3) Vanishing hub mass.** Fix \(q\). The finitely many compression matrices depend continuously on \(\sqrt h\) at \(h=0\). The hub coordinate then decouples, carrying a scalar identity entry if its selector is \(I\), and zero if it is \(G\); leaf \(N\) rows become singleton rows, while \(G\) rows become the uniform average of all \(q\) leaves. Thus the limiting maximum is the squared strong norm of the complete-graph two-radius maximal operator on \(q\) equal-mass points. For any subset of \(k\) singleton rows, the other \(q-k\) rows all use the global mean. Two-level compression gives a matrix with squared-norm characteristic trace \(2-k/q\) and determinant \((1-k/q)^2\), hence larger root \(\Phi(k/q)\). Nontrivial \(1\le k<q\) give values exceeding one. Taking the finite maximum proves the limit, without an interchange of uncontrolled infinite optimizations.

**(4) Dominant-hub asymptotic and eventual exactness.** Fix \(q\), put \(\epsilon=h^{-1/2}\), and examine the finitely many matrices as \(h\to\infty\). If the hub selector is \(I\), the first-order \(\epsilon\)-perturbation of \(B_{r,k}^{\mathsf T}B_{r,k}\) restricted to its eigenvalue-one space is zero; its largest eigenvalue is \(1+O_q(\epsilon^2)\). If the hub selector is \(G\) and \(k_I>0\) singleton leaf rows are selected, that first-order perturbation on the hub/singleton-leaf subspace is exactly
\[
\epsilon\begin{pmatrix}0&\sqrt{k_I}\\\sqrt{k_I}&0\end{pmatrix},
\]
so the top eigenvalue is \(1+\sqrt{k_I}\,\epsilon+O_q(\epsilon^2)\). If \(k_I=0\), it is \(1+O_q(\epsilon^2)\). The constants are uniform over selectors for fixed \(q\), because there are finitely many. The unique largest first-order coefficient \(\sqrt q\) occurs at \(r=G\) and \((k_I,k_N,k_G)=(q,0,0)\). Therefore this selector strictly wins for all sufficiently large \(h\).

For this winning selector the compressed matrix is
\[
\begin{pmatrix}
\frac h{h+q}&\frac{\sqrt{hq}}{h+q}\\0&1
\end{pmatrix}.
\]
Its squared norm is exactly \(\Phi(q/(h+q))\); expansion at zero gives the stated two-term asymptotic. Its positive top eigenvector is unique, has equal positive leaf absolute values and a smaller positive hub absolute value. Because its selector strictly beats every other one on the large-mass tail, all maximal inputs have that radial absolute-value form (independent input signs do not matter).

**(5) Exact three-vertex symmetry certificate.** Take \(q=2\), label selectors by a three-letter word in which the first letter is hub \(I\) or \(G\) and the last two letters are leaf \(I,N,G\). There are exactly eighteen words. For the three mass values below, define \(A_{r}\) by the explicit ball averages in the assumptions, and \(W=\operatorname{diag}(h,1,1)\). The following rational thresholds \(L\) separate each winning word (up to exchanging leaves) from every other word:

| Hub mass | Winning word | \(L\) | Rational input witnessing quotient greater than \(L\) |
|---|---|---|---|
| \(1/10\) | `ING` | \(1811/1250\) | \((13,4,1)\) |
| \(1\) | `INN` | \(31/20\) | \((5,1,1)\) |
| \(100\) | `GII` | \(111/100\) | \((1,9,9)\) |

For each row, direct rational computation gives \(\|A_r f\|_{2,h}^2/\|f\|_{2,h}^2>L\) for the witness, while for *every other* radius word the symmetric matrix \(LW-A^{\mathsf T}WA\) has all three leading principal minors strictly positive. Sylvester's criterion then proves its norm squared is \(<L\). The complete finite exact certificate is implemented, without interval floating point, in `verify_weighted_star_maximal.py`. The winner eigenvalues satisfy respectively the cubic polynomial and the two radical identities in the Finding section. The winning Gram matrices have irreducible nonnegative Perron blocks, so their nonnegative maximizing rays are unique; exchanging the two leaves accounts for the only labeled alternative in the asymmetric case. All distinct active patterns remain separated on an open neighborhood of their respective mass values by continuity. This proves the asserted symmetry changes and no stronger global phase-count claim.

## Verification

Execute `python verify_weighted_star_maximal.py` with the dependencies in `requirements.txt`. It checks: exact rational Sylvester positivity against all competing three-point selectors at each indicated mass; rational Rayleigh witness lower bounds; exact characteristic-polynomial divisibility; agreement of the compressed and full-selector weighted singular values on 25 independent \((q,h)\) inputs; 2520 direct randomized maximal-function inequalities; and the two limiting laws numerically for several values of \(q\). The arbitrary-size identity and both asymptotic claims are established by the proof, **not** by these finite tests. The certificate concerns the full matrices reconstructed within the packaged checker.

## Relationship to prior work

Soria and Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs* (first public preprint 2014), introduced central finite-graph norm comparisons and the star as an extremal graph for the sublinear-exponent range. González-Riquelme and Madrid, *Sharp Inequalities for maximal operators on finite graphs* (first public preprint 2020), gave the **counting-measure** exact strong Hilbert norm for stars and complete graphs. Their sequel, *Sharp inequalities for maximal operators on finite graphs, II* (first public preprint 2020), analyzes further extremizer structure for stars, again with **counting measure**. None of these inspected norm theorems states the arbitrary positive hub mass formula, the two one-sided mass limits with eventual exact selector rigidity, or the asymmetric-leaf strong-\(L^2\) extremizer at \(h=1/10\). The equal-mass \(h=1\) three-point value in this paper is a consistency check and **not** claimed as original. The complete-graph limiting expression is also a known two-radius maximal calculation, not a standalone novelty claim.

## Limitations

All leaves have equal mass, the metric is the unit-edge star, and only the strong exponent two is classified. The exact formula is a finite eigenvalue maximization, not a closed single radical for arbitrary \(q,h\). The existence of \(H_q\) is proved but no optimal explicit threshold is claimed. The three sample mass regimes prove multiple transitions, not that there are exactly two. The work does not address arbitrary unequal leaf weights, higher-radius trees, general \(L^p\) norms, uncentered maxima or independent mathematical validation. An equivalent formulation in literature not located by the recorded searches remains an originality risk.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, first public arXiv preprint 2014-10-22, arXiv:1410.6204, https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, first public arXiv preprint 2020-05-06, arXiv:2005.03146, https://arxiv.org/abs/2005.03146.
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, first public arXiv preprint 2020-11-05, arXiv:2011.02630, https://arxiv.org/abs/2011.02630.
