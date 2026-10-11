# Global rearrangement rigidity for two-weight four-cycle numerical radii on Banach \(\ell_p\)

## Finding
For every real exponent \(1<p<\infty\) and positive reals \(a>b>0\), consider weighted cyclic shifts on real or complex \(\ell_p^4\), with \((S_w x)_j=w_jx_{j+1}\) and \(x_5=x_1\). Let \(v_p\) denote the spatial numerical radius defined in the next section. For the adjacent and alternating weight patterns, respectively, write
\[
G=(a,a,b,b),\qquad A=(a,b,a,b).
\]
Then the following **strict, global rearrangement inequality** holds for all magnitudes of the contrast:
\[
\boxed{v_p(S_G)>v_p(S_A).}
\]
Every placement of the multiset of weights \(\{a,a,b,b\}\) is a cyclic rotation of one of these two patterns. Consequently the four adjacent placements are exactly the maximizing placements and the two alternating placements are exactly the minimizing placements among all six assignments. When \(a=b\), all six placements agree.

There is also a sharp scalar formula for the minimum. Let \(t=t_{p,a,b}\) be the unique maximizer over \(t>0\) of
\[
H_{p,a,b}(t)=\frac{a t^{p-1}+bt}{1+t^p}.
\]
Then
\[
\boxed{v_p(S_A)=H_{p,a,b}(t_{p,a,b})},
\]
where \(t_{p,a,b}\) is the unique positive root of
\[
a t^{p-2}((p-1)-t^p)+b(1-(p-1)t^p)=0.
\]
In particular, the maximizing ratio satisfies \(t_{p,a,b}>1\) if \(p>2\), \(t_{p,a,b}<1\) if \(1<p<2\), and \(t_{2,a,b}=1\).

The strict gap has explicit positive lower certificates:
\[
v_p(S_G)-v_p(S_A)\ge
\begin{cases}
\displaystyle\frac{(t-1)(a t^{p-1}-b)}{2(1+t^p)},&p>2,\\[5pt]
\displaystyle\frac{(1-t^{p-1})(a-bt)}{2(1+t^p)},&1<p<2.
\end{cases}
\]
At the Hilbert exponent, the exact known quadratic expression is
\[
v_2(S_A)=\frac{a+b}{2},\quad
v_2(S_G)=\sqrt{\frac{a^2+b^2}{2}},\quad
v_2(S_G)-v_2(S_A)=\frac{(a-b)^2}{4(\sqrt{(a^2+b^2)/2}+(a+b)/2)}.
\]

## Assumptions and scope
For \(1<p<\infty\), the normalized norming functional for a unit vector \(x\in\ell_p^4\) is the dual vector with coordinates \(\lvert x_j\rvert^{p-2}\overline{x_j}\), with value zero at zero coordinates. Its dual norm is one and it pairs to one with \(x\). The spatial numerical radius is
\[
v_p(S_w)=\sup_{\sum_{j=1}^4\lvert x_j\rvert^p=1}
\left\lvert\sum_{j=1}^4w_j\lvert x_j\rvert^{p-2}\overline{x_j}x_{j+1}\right\rvert.
\]
All weights are positive, and the underlying scalar field is either \(\mathbb R\) or \(\mathbb C\). The result concerns one cyclic four-coordinate shift and its six distinct placements before identifying cyclic rotations; it is not a general rearrangement theorem for arbitrary dimension, arbitrary weight multiplicities, or endpoint exponents.

## Proof
**1. Positive variational reduction and uniqueness.** The triangle inequality, followed by choosing nonnegative real coordinate phases, reduces the spatial numerical radius exactly to
\[
v_p(S_w)=\max_{s_j\ge0,\ \sum s_j=1}
\Phi_w(s),\qquad
\Phi_w(s)=\sum_{j=1}^4w_j s_j^{\alpha}s_{j+1}^{\beta},
\]
where cyclic indices are understood, \(\alpha=(p-1)/p\), and \(\beta=1/p\). Indeed \(s_j=|x_j|^p\) and every upper-bound term is simultaneously realized by nonnegative \(x_j\).

Every maximizer has strictly positive coordinates. If a maximizer had both a positive coordinate and a zero coordinate, connectedness of the four-cycle would give an edge between positive and zero masses. Transfer mass \(\epsilon>0\) from a positive coordinate to that zero coordinate. The newly activated incident term gains a positive multiple of \(\epsilon^{\beta}\) or \(\epsilon^{\alpha}\) (both exponents are smaller than one). Terms already positive change by at most \(O(\epsilon)\), and other zero-edge terms cannot decrease; thus the objective strictly increases for sufficiently small \(\epsilon\), contradiction.

The weighted geometric mean \((u,v)\mapsto u^{\alpha}v^{\beta}\) is concave on the nonnegative quadrant. For positive pairs, equality in its concavity inequality for two different arguments occurs exactly when the ordered pairs are proportional. Therefore \(\Phi_w\) is strictly concave on the interior of the probability simplex: equality for all four edges forces the two probability vectors proportional, hence equal. Thus the interior maximizer is unique.

**2. Solve the alternating pattern.** The alternating coefficients are invariant under a two-step cyclic coordinate shift. By uniqueness, the maximizing masses have \(s_1=s_3\) and \(s_2=s_4\). Taking \(x=(t,1,t,1)\) up to positive normalization gives
\[
v_p(S_A)=\max_{t>0}\frac{a t^{p-1}+bt}{1+t^p}.
\]
Strict concavity after expressing the ratio in the simplex variable \(s=t^p/(1+t^p)\in(0,1)\) proves uniqueness of \(t\). Differentiation gives the displayed root equation. Since
\[
H'_{p,a,b}(1)=\frac{(p-2)(a-b)}4,
\]
and the maximizer in the simplex variable is unique, its location is on the side of one indicated in the finding: the coordinate \(s\) increases monotonically with \(t\), so a positive derivative at one forces the maximum above one, and a negative derivative forces it below one. At \(p=2\) the maximum is attained at \(t=1\).

**3. Construct a strict better adjacent placement.** The unnormalized Rayleigh quotient for any positive vector \(x\) is
\[
Q_w(x)=\frac{\sum_{j=1}^4w_jx_j^{p-1}x_{j+1}}{\sum_{j=1}^4x_j^p}.
\]
When \(p>2\), evaluate the adjacent pattern at \(x=(t,t,1,1)\). Direct cancellation gives
\[
Q_G(t,t,1,1)-v_p(S_A)=
\frac{(t-1)(a t^{p-1}-b)}{2(1+t^p)}>0.
\]
When \(1<p<2\), evaluate at \(x=(t,1,1,t)\), obtaining
\[
Q_G(t,1,1,t)-v_p(S_A)=
\frac{(1-t^{p-1})(a-bt)}{2(1+t^p)}>0.
\]
Each test vector proves a lower bound for \(v_p(S_G)\), giving the stated quantitative certificates and strictness for every non-Hilbert exponent.

For \(p=2\), the spatial numerical radius is the top eigenvalue of the real symmetric matrix \((S_w+S_w^T)/2\). In the bipartition \(\{1,3\}\cup\{2,4\}\), the adjacent pattern has off-diagonal block with both rows equal to \((a/2,b/2)\), so its top singular value is \(\sqrt{(a^2+b^2)/2}\). The alternating pattern has block \(\begin{psmallmatrix}a/2&b/2\\b/2&a/2\end{psmallmatrix}\), with top singular value \((a+b)/2\). Their difference has the displayed strictly positive form when \(a>b\).

**4. Exhaust all assignments.** Exactly four orderings put the two copies of \(a\) on neighboring edges of the cyclic four-graph; the remaining two alternate \(a,b\). Cyclic coordinate rotation is a surjective isometry of both real and complex \(\ell_p^4\) and preserves spatial numerical radius under conjugation, so each class has one numerical-radius value. The strict comparison distinguishes the classes globally. This completes the proof.

## Verification
Run `python3 verify.py` with Python's standard library. The program fixes its random seed, performs a scalar one-dimensional numerical maximization, and checks the alternating upper bound against 15,840 positive four-vectors. It also checks 66 non-Hilbert constructive gap identities, 660 quadratic Hilbert upper bounds, and 72 parameter settings in all. The verifier prints `PASS` when its checks succeed.

For example, with \(a=3\) and \(b=1\), at \(p=4\) it finds approximately \(v_p(S_A)=2.079009579543\) and the proved adjacent *lower bound* \(2.191604738458\); the actual adjacent radius may be larger. Finite numerical checks are not proofs of universal inequalities; all quantifiers are handled by the analysis above.

## Relationship to prior work
Chang and Wang's 2012 weighted-shift permutation results characterize optimal arrangements using the classical inner-product numerical radius on complex Hilbert space. Cheung and Li's permutation study treats weighted matrix graphs and establishes powerful Hilbert-space rearrangement results, including cyclic matrices (Theorem 3.6). Those works subsume the present \(p=2\) structural comparison; this special case is not claimed as independently original. Vandanjav and Undrakh likewise study inner-product numerical ranges of weighted shift matrices and operators, not the all-exponent spatial \(\ell_p\) problem.

The theorem here compares the Banach-space spatial numerical radius globally for both non-Hilbert ranges \(1<p<2\) and \(p>2\) and every positive contrast, using a nonlinear simplex variational problem and explicit trial vectors rather than a symmetric-matrix Perron eigenvalue. No equivalent non-Hilbert all-contrast statement was identified in the examined literature. Related historical formulations could still exist.

## Limitations
The strict ordering is proved only for the two-weight multiplicity pattern on the four-cycle; the exact adjacent numerical radius outside \(p=2\) is not determined. The formula for the alternating radius is an implicit maximization/root characterization, not generally elementary radicals. The proof does not cover zero or negative weights, longer cycles, arbitrary multiplicities, or \(p=1,\infty\). The 2012 archival PDF was not accessible in full; its independently visible abstract and substantial scientific article text confirm its Hilbert-space scope, but an unlocated equivalent Banach-space theorem remains a residual originality risk.

## References
1. C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, Journal of Mathematical Analysis and Applications **394** (2012), 592–602. DOI: `10.1016/j.jmaa.2012.04.039`. First publicly available online 2012-04-30 (verified first-page publication history).
2. W.-S. Cheung and C.-K. Li, *Maximizing the numerical radii of matrices by permuting their entries*, Linear and Multilinear Algebra **62** (2014). DOI: `10.1080/03081087.2012.753594`. Author-held full text: `https://cklixx.people.wm.edu/shift-final.pdf`.
3. J. Vandanjav and N. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra and its Applications (2014). DOI: `10.1016/j.laa.2014.02.018`.
