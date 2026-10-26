# An exact orientation-occupancy threshold for eight- and twelve-angle stacking languages

## Finding
For the manufacturing language of half-stacks on the eight- and twelve-angle alphabets, the principal-orientation occupancy threshold is exactly
\[\alpha_8=\frac{17+\sqrt{17}}{136}=0.1553169531\ldots,\qquad\alpha_{12}=\frac1{12}=0.0833333\ldots.\]
A fixed lower quota strictly below this threshold excludes an exponentially vanishing fraction of manufacturing-valid half-stacks, whereas a quota strictly above the threshold retains at most an exponentially vanishing fraction. In particular, the 10-percent rule is asymptotically almost surely satisfied on the eight-angle alphabet and exponentially restrictive on the twelve-angle alphabet.

## Assumptions and scope
For \(q\in\{8,12\}\), use the orientations
\[\Sigma_8=\{0,\pm30,\pm45,\pm60,90\},\qquad\Sigma_{12}=\{0,\pm15,\pm30,\pm45,\pm60,\pm75,90\}.\]
Angles are measured in degrees modulo \(180\), and disorientation is the smaller circular angular difference. A length-\(m\) word satisfies (M1) if adjacent disorientation is at most \(45^\circ\), and (M2) if no four adjacent orientations agree. It is a symmetric laminate half-stack if its final constant-orientation run has length one; this guarantees that its mirror concatenation satisfies (M2). Let \(U_q(m)\) count these words. For \(0\le\alpha\le1\), let \(Q_q(m,\alpha)\) count those also satisfying \(c_a(w)\ge\alpha m\) for every \(a\in\{0,45,-45,90\}\). These are half-stack versions of the original full-laminate percentage constraints, because mirroring doubles both the word length and every letter count. **Balance between opposite signed angles is not imposed in this theorem.** All asymptotics concern integer \(m\to\infty\) and fixed, noncritical \(\alpha\).

## Proof
**Run graph and Perron growth.** Let \(H_q\) be the symmetric zero-diagonal orientation adjacency matrix with \((H_q)_{ab}=1\) precisely when \(0<\delta(a,b)\le45^\circ\). A word is uniquely a sequence of constant-letter runs of lengths \(1,2,3\); successive run letters follow an edge of \(H_q\). Put \(S(z)=z+z^2+z^3\), and let \(\rho_q\) be the Perron eigenvalue of \(H_q\). The strictly positive growth constant \(\lambda_q\) is determined by \(\rho_qS(\lambda_q^{-1})=1\). The associated run-transition transfer series is \(S(z)H_q\). The one-run terminal restriction changes only its positive endpoint vector and hence does not change the exponential growth rate: \(U_q(m)=\Theta(\lambda_q^m)\). The run-state transition graph is primitive: the orientation graph is connected, and the allowed run lengths one and two yield return cycles of consecutive lengths.

**Symbol-frequency lemma.** Let \(v\) be the strictly positive Perron eigenvector of \(H_q\), normalized by \(\sum_a v_a^2=1\). For any orientation \(a\), weight each run at \(a\) of length \(r\) by \(e^{tr}\). The tilted run matrix is \(H_q\operatorname{diag}(\sum_{r=1}^3 z^r e^{tr\mathbf1_{b=a}})\). Its Perron singularity \(z(t)\) is real-analytic around zero. Differentiating its eigenvalue-one relation at \(t=0\), and using \(H_qv=\rho_qv\), gives
\[ -\frac{z'(0)}{z(0)}=v_a^2.\]
Consequently, for a uniformly random admissible half-stack, the limiting orientation fraction is exactly \(\pi_a=v_a^2\). More strongly, analytic positive-matrix perturbation and an exponential Markov bound show that for each fixed \(\epsilon>0\), there is \(c_\epsilon>0\) such that
\[\Pr\bigl(\lvert c_a(w)/m-\pi_a\rvert\ge\epsilon\bigr)=O(e^{-c_\epsilon m}).\]
Here the endpoint selection of terminal run length one is included in the positive transfer vectors and does not alter either the derivative or the exponential estimate. The proof needs no assumption of independent letters.

**Exact spectra.** In \(\Sigma_8\), partition the letters into the four principal orientations \(P=\{0,45,-45,90\}\) and four auxiliary angles \(T=\{\pm30,\pm60\}\). Every \(P\)-vertex has two neighbors in \(P\) and two in \(T\); every \(T\)-vertex has two in \(P\) and one in \(T\). Thus the equitable quotient of \(H_8\) is
\[\begin{pmatrix}2&2\\2&1\end{pmatrix},\qquad\rho_8=\frac{3+\sqrt{17}}2.\]
Its positive eigenvector has common value \(x\) on \(P\), and \(y=((\sqrt{17}-1)/4)x\) on \(T\). This is positive on every vertex, hence the Perron eigenvector. Each principal orientation therefore has limiting share
\[\pi_P=\frac{x^2}{4x^2+4y^2}=\frac{17+\sqrt{17}}{136}.\]
In \(\Sigma_{12}\), the twelve angles are equally spaced by \(15^\circ\). The orientation graph is the third power of a twelve-cycle: every vertex has six neighbors and the positive Perron eigenvector is uniform. Therefore \(\rho_{12}=6\) and \(\pi_P=1/12\) for each principal orientation.

**Sharp strict-threshold dichotomy.** If \(\alpha<\pi_P\), apply the lower-tail exponential bound to the four principal orientations and take a union bound. Then \(Q_q(m,\alpha)/U_q(m)=1-O(e^{-cm})\). If \(\alpha>\pi_P\), satisfying even one of the four quotas is an exponentially rare upper-tail event, so \(Q_q(m,\alpha)/U_q(m)=O(e^{-cm})\). In particular, \(1/12<1/10<(17+\sqrt{17})/136\), proving the eight-to-twelve contrast. The formula for \(\lambda_q\) follows upon substituting \(z=1/\lambda_q\) into the Perron root equation.

## Verification
The companion standalone verifier `verify_orientation_threshold.py` constructs both angular adjacency matrices independently, checks the eight-angle equitable partition and twelve-angle degree, independently computes Perron eigenvectors by power iteration, verifies the radical limits, computes the growth-root values, and counts all valid half-stacks with exact integer transfer arithmetic at lengths \(12,30,80\). It reproduces \(U_8(12)=102102368\) and \(U_{12}(12)=19924507008\), agreeing with the published twelve-ply half-stack count and its rounded twelve-angle counterpart. The checker prints `VERIFY_OK`. Finite checks are consistency tests, not a substitute for the Perron/concentration proof.

## Relationship to prior work
Langiu, Rubino and Canale (2026), arXiv:2610.23146v1, introduce precisely these orientation sets, local manufacturing rules, the final-run-one symmetry criterion, and a dynamic program for finite-length counts with optional percentage guidelines. Their text tabulates several finite lengths; it does not give the exact two Perron-occupancy thresholds or prove the strict subcritical/supercritical exponential dichotomy. General Perron–Frobenius and rational-language fluctuation principles are classical; the novelty claimed here is the explicit eight/twelve-alphabet comparison and its exact threshold constants, not those general tools.

## Limitations
The balance guideline between signed angles is deliberately excluded; the result does not give asymptotics for the intersection of balance and quota. At the exact thresholds \(\alpha=\alpha_q\), no polynomial prefactor or limiting acceptance probability is claimed. The above is an asymptotic counting theorem, not a numerical optimization or a statement about structural performance of laminates. Independent assessment of novelty is still required.

## References
1. A. Langiu, F. Rubino and G. Canale, *Counting and Sampling Manufacturable Stacking Sequences*, arXiv:2610.23146v1 (first public 2026-10-16), Sections 2–3 and 7–8, https://arxiv.org/html/2610.23146v1.
2. A. Bertoni, C. Choffrut, M. Goldwurm and V. Lonati, *On the number of occurrences of a symbol in words of regular languages*, Theoretical Computer Science 302 (2003), 431–456, DOI:10.1016/S0304-3975(02)00892-7 (general fluctuation background, not an eight/twelve orientation result).
