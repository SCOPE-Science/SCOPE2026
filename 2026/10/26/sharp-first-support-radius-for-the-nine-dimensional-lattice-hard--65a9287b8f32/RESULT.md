# Sharp first support radius for the nine-dimensional lattice Hardy defect

## Finding
Let \(B_R=\{x\in\mathbb Z^9:1\le\|x\|_1\le R\}\). Extend every \(u:B_R\to\mathbb C\) by zero to all of \(\mathbb Z^9\), and set
\[
E(u)=\sum_{x\in\mathbb Z^9}\sum_{j=1}^9|u(x+e_j)-u(x)|^2,\qquad H(u)=\sum_{x\ne0}\frac{|u(x)|^2}{\|x\|_2^2}.
\]
The smallest integer \(R\ge1\) for which some nonzero \(u\), supported in \(B_R\), satisfies \(E(u)<\frac{49}{4}H(u)\) is **exactly \(R=12\)**. Indeed \(E(u)\ge\frac{49}{4}H(u)\) for every complex \(u\) supported in \(B_{11}\), whereas the attached exact integer orbit table produces a strict counterexample on \(B_{12}\).

## Assumptions and scope
The graph is the full nearest-neighbor graph on \(\mathbb Z^9\); the origin and every site outside the indicated \(\ell_1\)-ball have prescribed value zero. Every undirected edge is counted once, including edges crossing the support boundary. The weight is the inverse of *squared Euclidean length*, while support is measured in \(\ell_1\). The coefficient \(49/4\) is the dimension-nine continuum Hardy coefficient. The theorem concerns the **first finite support radius**, not the global sharp lattice Hardy constant.

## Proof
Write an orbit label \(\tau=(\tau_1,\dots,\tau_k)\) for a partition of some integer \(s\in\{1,\dots,R\}\) with \(k\le9\); it represents every lattice point whose absolute coordinate multiset is \(\tau\). Enumerate labels by increasing \(s\) and, for fixed \(s\), by the descending first-part recursion specified in `verify_hardy.py`. The labels number 191 for \(R=11\), and 264 for \(R=12\). The orbit multiplicity and squared radius are
\[
m_\tau=\frac{2^k9!}{(9-k)!\prod_{a\ge1}(\#\{i:\tau_i=a\})!},\qquad q_\tau=\sum_i\tau_i^2.
\]
Let \(N_{\tau\nu}\) count the nearest neighbors in orbit \(\nu\) of the canonical representative \((\tau_1,\dots,\tau_k,0,\dots,0)\), excluding outside sites and the origin (whose values are zero). There are 18 neighbor directions in all. Thus for an orbit-invariant function with values \(w_\tau\), the Dirichlet Laplacian is \((Lw)_\tau=18w_\tau-\sum_\nu N_{\tau\nu}w_\nu\).

**Lower-radius certificate.** The table `certificate_R11.json` lists 191 strictly positive integers \(w_\tau\), in exactly the enumeration order above. The standalone exact-arithmetic verifier checks **every** one of the 191 inequalities
\[
(72q_\tau-49)w_\tau-4q_\tau\sum_\nu N_{\tau\nu}w_\nu>0.
\]
The smallest left side is 1458. Therefore \(Lw(x)-49w(x)/(4\|x\|_2^2)>0\) at every site of \(B_{11}\). The discrete ground-state transform, for arbitrary complex \(u\) vanishing off \(B_{11}\), gives
\[
E(u)-\frac{49}{4}H(u)
=\sum_{\{x,y\}\subset B_{11},\,\|x-y\|_1=1}w_xw_y\left|\frac{u_x}{w_x}-\frac{u_y}{w_y}\right|^2
+\sum_{x\in B_{11}}\frac{(Lw)_x-49w_x/(4\|x\|_2^2)}{w_x}|u_x|^2\ge0.
\]
This identity already incorporates all boundary-edge contributions through the full 18-neighbor Laplacian. It excludes violations at every smaller radius because \(B_R\subseteq B_{11}\) for \(R\le11\).

**Upper-radius certificate.** The second table, `certificate_R12.json`, lists 264 positive integer values \(v_\tau\) defining an invariant, zero-extended function. Orbit counting and discrete summation by parts give the **exact** equality
\[
4E(v)-49H(v)=\sum_\tau\frac{m_\tau}{q_\tau}v_\tau\left[(72q_\tau-49)v_\tau-4q_\tau\sum_\nu N_{\tau\nu}v_\nu\right]
= -\frac{168023799157855578188041899511220364510317}{66816567612546192522086437300}<0.
\]
All numbers in this calculation are integers or exact rational numbers. Both certificates can be reconstructed solely from the three attached files and Python's standard library; no floating-point estimation is needed for the proof.

## Verification
Run `python verify_hardy.py` in the directory containing the two certificate JSON files. It checks the dimension and radii, enumerates 191 and 264 signed-permutation orbits, verifies integer positivity on all 191 orbits, and reproduces the displayed strictly negative exact rational value for the 264-orbit witness. The script was executed on the attached input bytes and printed `EXACT_CERTIFICATES_PASS`. This is a finite exhaustive certificate within the stated support sets; it does not determine a universal global extremizer.

## Relationship to prior work
Lizama, arXiv:2608.30831 (first posted August 31, 2026), proved the global strict inequality between the sharp nine-dimensional lattice Hardy constant and the continuum coefficient, using Gaussian Rayleigh--Ritz tests and theta estimates. Alpay, arXiv:2610.05421v1 (October 4, 2026), resolved equality with the continuum coefficient for dimensions five through eight. Neither inspected account determines the *first* \(\ell_1\) radius at which a finitely supported counterexample exists. Existing indexed work on the radius-12 correction to an **eight-dimensional reciprocal Hardy field** concerns a different dimension, a different radius convention, and the support of a proof correction rather than counterexample vectors. The present result fixes the first nine-dimensional finite Dirichlet threshold via independent exact certificates.

## Limitations
This is a certificate-based exact cutoff for dimension nine and the specified continuum coefficient, not an analytic closed form for the complete family of finite-ball eigenvalues, nor a result for other dimensions or other lattice metrics. Priority cannot be guaranteed against unindexed or inaccessible full literature; numerical exploration used to find the certificate is not part of its logical validity.

## References
- C. Lizama, *Sharp discrete Hardy constants in dimensions three and four and strict upper bounds from dimension nine*, arXiv:2608.30831, first posted 2026-08-31, https://arxiv.org/abs/2608.30831.
- N. Alpay, *Sharp discrete Hardy constants in low dimensions*, arXiv:2610.05421v1, first posted 2026-10-04, https://arxiv.org/abs/2610.05421.
