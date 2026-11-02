# Exact Hilbert distortion of centered cube–cross-polytope intersections

## Finding
For every integer \(n\ge 2\) and real parameter \(\tau>0\), put
\[
H_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\},\qquad
N_\tau(x)=\max\left\{\|x\|_\infty,\frac{\|x\|_1}{\tau}\right\}.
\]
Set \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\), \(s=\min\{\tau/2,a\}\), \(q=\lfloor s\rfloor\), and \(\rho=s-q\). The exact Banach–Mazur distance to real Euclidean space is
\[
\boxed{\displaystyle
 d_{\rm BM}\bigl((H_n,N_\tau),\ell_2^{n-1}\bigr)
 =\sqrt{2(q+\rho^2)}\,
 \max\left\{\sqrt{\frac{n-1}{n}},
 \frac{2}{\tau}\sqrt{\frac{ab}{n}}\right\}.}
\]
For \(n=2\), the distance is \(1\) for all \(\tau\); for \(n=3\), it is \(2/\sqrt3\) for all \(\tau\). For each \(n\ge4\), the distance has a **unique** minimizing parameter
\[
\boxed{\displaystyle \tau_n^*=2\sqrt{\frac{ab}{n-1}}=\begin{cases}
 n/\sqrt{n-1},& n\text{ even},\\
 \sqrt{n+1},& n\text{ odd}.
\end{cases}}
\]
The least distortion is obtained by inserting \(\tau_n^*\) into the displayed exact formula; its asymptotic scale is \(\min_{\tau>0}d_{\rm BM}\sim n^{1/4}\). The changes in extremizer support at thresholds \(\tau=2j\), for integers \(1\le j\le a\), correspond to new saturated signed coordinates of an extremal vector.

## Assumptions and scope
All vector spaces, Hilbert targets, and linear isomorphisms are **real**. Distortion is the infimum \(\|T\|\|T^{-1}\|\) over linear isomorphisms between the \((n-1)\)-dimensional normed space and \(\ell_2^{n-1}\). The ball is precisely
\[
\{x\in H_n:N_\tau(x)\le1\}=H_n\cap[-1,1]^n\cap\tau B_1^n.
\]
The statements include parameters below \(2\), endpoints where \(\tau/2\) is an integer, and the limit in which the \(\ell_1\) constraint becomes redundant.

## Proof
**1. The optimal Hilbertian pullback is Euclidean.** If a positive-definite quadratic form \(Q\) on \(H_n\) satisfies \(m^2N_\tau(x)^2\le Q(x)\le M^2N_\tau(x)^2\) for all \(x\in H_n\), average this inequality over coordinate permutations. The averaged form is invariant under the full symmetric group, and still obeys the same inequalities. Every permutation-invariant form on \(H_n\) is a scalar multiple of \(\sum_i x_i^2\): extend it by zero on the constant vectors, and note that its matrix has constant diagonal and constant off-diagonal entries. Thus the minimum over **all**, not merely invariant, Hilbertian structures equals
\[
\biggl(\sup_{\|x\|_2=1,\,x\in H_n}N_\tau(x)\biggr)
\biggl(\sup_{N_\tau(x)\le1,\,x\in H_n}\|x\|_2\biggr).
\]

**2. The sharp Euclidean-unit-sphere maximum.** The Euclidean norm of the projection of a coordinate vector onto \(H_n\) is \(\sqrt{(n-1)/n}\), so \(\sup\|x\|_\infty=\sqrt{(n-1)/n}\) on the Euclidean sphere of \(H_n\). Also, by duality of coordinate absolute values,
\[
\sup_{\|x\|_2=1,\,x\in H_n}\|x\|_1
=\max_{\varepsilon\in\{-1,1\}^n}\left\|\varepsilon-
\frac{\sum_i\varepsilon_i}{n}\mathbf1\right\|_2
=2\sqrt{\frac{ab}{n}}.
\]
The last maximum occurs for signs of the two most balanced possible multiplicities. Taking the maximum of these two coordinate constraints gives exactly the second factor in the theorem.

**3. The sharp radius of the intersected ball.** Write the total positive and negative coordinate masses of a zero-sum vector as the common number \(S\). If \(N_\tau(x)\le1\), then \(2S=\|x\|_1\le\tau\) and each coordinate has magnitude at most \(1\). Since positive and negative supports are disjoint, \(S\le\min\{\#\text{positive},\#\text{negative}\}\le a\). Hence \(S\le s\).

For nonnegative coordinates bounded by \(1\) with fixed sum \(S=j+\theta\), \(j\) an integer and \(0\le\theta<1\), the sum of their squares is at most \(j+\theta^2\): transferring positive mass from a smaller fractional coordinate to a larger one never decreases the sum of squares. Apply this separately to positive and negative coordinates. Since \(S\mapsto\lfloor S\rfloor+(S-\lfloor S\rfloor)^2\) is increasing, this gives \(\|x\|_2^2\le2(q+\rho^2)\). Equality is realized by \(q\) entries \(+1\), \(q\) entries \(-1\), and, if \(\rho>0\), one \(+\rho\) and one \(-\rho\), all other entries zero. Their number \(2\lceil s\rceil\) does not exceed \(n\). Consequently the squared Euclidean circumradius of the ball is **exactly** \(2(q+\rho^2)\). Combining steps 1–3 proves the formula.

**4. Parameter optimization.** Write \(A=\sqrt{(n-1)/n}\), \(B=2\sqrt{ab/n}\), and \(\tau^*=B/A\). For \(n\ge4\), \(2<\tau^*<2a\). The formula is \(B R(\tau)/\tau\) for \(\tau\le\tau^*\), and \(A R(\tau)\) for \(\tau\ge\tau^*\), where \(R(\tau)^2=2(\lfloor s\rfloor+(s-\lfloor s\rfloor)^2)\).

For \(0<\tau\le2\), \(R(\tau)=\tau/\sqrt2\), so the distortion is constant. For \(2<\tau\le\tau^*\), it decreases strictly. Indeed, with \(s=j+\theta>1\), \(j\ge1\) and \(0<\theta<1\), the derivative of \((j+\theta^2)/(j+\theta)^2\) has the strictly negative sign of \(j(\theta-1)\); continuity handles the integer endpoints. On \([\tau^*,2a]\) it increases strictly, because \(R\) does, and afterwards it is constant at the larger terminal value. Thus \(\tau^*\) is the unique global minimizer. When \(n=2,3\), zero-sum vectors obey \(\|x\|_1=2\|x\|_\infty\), so varying \(\tau\) only rescales the norm. Finally, \(\tau_n^*\sim\sqrt n\) and \(R(\tau_n^*)^2=\tau_n^*+O(1)\), establishing the \(n^{1/4}\) asymptotic.

## Verification
The standalone pure-Python file `checker.py` uses exact rational arithmetic. For \(2\le n\le7\), it checks the two sharp unit-sphere factor formulas and verifies the Euclidean ball radius on coordinate grids of denominator \(4\), with a total of 310,298 grid vectors and 210 exact rational assertions. It does not certify extrema over every real coordinate: those follow from the preceding mass-transfer and symmetry arguments. Running `python3 checker.py` prints the exact assertion counts and `CHECK_OK` on success.

## Relationship to prior work
Vasil'eva's 2023 study investigates Kolmogorov widths of intersections of two finite-dimensional norm balls and motivates studying sharp linear invariants of such intersections. Its theorems give width estimates, not the all-parameter Hilbert Banach–Mazur distance of the coordinate-sum-zero section here. Kobos and Varivoda's 2023 study determines Banach–Mazur phenomena for selected cube and cross-polytope pairs in small dimensions, rather than the centered sections of their intersections. These are distinct invariant and object comparisons, not novelty inferences based only on title or parameter mismatch. Related published work on quadratic mixtures of coordinate \(\ell_1\) and \(\ell_\infty\) norms, pure \(\ell_4\) zero-sum sections, and Mahler products of cube–cross-polytope intersections does not give the exact norm/max formula above. An equivalent historical formula under a different terminology remains possible and has not been independently excluded.

## Limitations
The result concerns **linear** Hilbert distortion, not nonlinear metric embeddings, and treats one common amplitude bound, one total-variation bound, and the single coordinate-sum-zero constraint. It does not classify every minimizing linear map, nor address weighted coordinates, other hyperplane normals, or complex scalars. The proof is analytical; finite checks are supporting tests. Independent scholarly priority and mathematical validation have not been established.

## References
1. A. A. Vasil'eva, *Estimates for the Kolmogorov widths of an intersection of two balls in a mixed norm*, first public arXiv version 2023-03-23, https://arxiv.org/abs/2303.13147.
2. T. Kobos and M. Varivoda, *On the Banach-Mazur Distance in Small Dimensions*, first public arXiv version 2023-05-10, https://arxiv.org/abs/2305.06427.
