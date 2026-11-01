# Finite-window morphology: sharp two-input variation and a boundary-weight transition

## Finding

For integers \(n\ge2\) and \(0\le r\le n-1\), define the sliding erosion and dilation on a real signal \(f=(f_1,\ldots,f_n)\) by
\[
(E_rf)_i=\min_{\max(1,i-r)\le j\le\min(n,i+r)}f_j,
\qquad
(D_rf)_i=\max_{\max(1,i-r)\le j\le\min(n,i+r)}f_j.
\]
Both use truncated windows at the endpoints. For any strictly positive edge weights \(w_1,\ldots,w_{n-1}\), put
\[
V_w(h)=\sum_{k=1}^{n-1}w_k|h_{k+1}-h_k|.
\]
The exact two-input Lipschitz coefficient of **either** operator, in this weighted-variation seminorm, is
\[
\boxed{\mathcal L_{n,r}(w)=\max_{\substack{1\le i,k<n\\
(i>r\;\mathrm{or}\;i+r<n)\\
\max(1,i-r)\le k\le\min(n-1,i+r)}}\frac{w_i}{w_k}},
\]
where the maximum of an empty set is zero. More explicitly, for \(S=E_r\) or \(S=D_r\),
\[
\mathcal L_{n,r}(w)=\sup_{V_w(f-g)>0}\frac{V_w(Sf-Sg)}{V_w(f-g)}.
\]
Every term in the displayed finite maximum is attained exactly by a pair of real signals with arbitrarily small nonzero separation. In particular, \(\mathcal L_{n,n-1}(w)=0\).

For \(1\le r\le n-2\), define the **active edges**
\[
\mathcal A_{n,r}=\{1,\ldots,n-r-1\}\cup\{r+1,\ldots,n-1\}.
\]
Then \(\mathcal L_{n,r}(w)\le1\) if and only if every active edge has the same weight \(c>0\) and every inactive edge has weight at least \(c\). In particular, when \(n\ge2r+1\), nonexpansivity requires all weights to be equal; when \(n\le2r\), the interior band of edges \(n-r,\ldots,r\) may have any weights at least \(c\), while the two boundary bands must have equal weight \(c\). Thus a near-global window admits nonuniform contractive weights even though ordinary shorter windows do not.

For example, at \(n=6\), \(r=4\), the nonuniform weights \(w=(1,3,7,3,1)\) are contractive, while at \(r=2\) any nonuniform choice is expansive for some signal pair. This shows the effect of finite endpoint overlap rather than a generic property of heterogeneous weights.

The unweighted coefficient equals \(1\) for \(0\le r\le n-2\) and \(0\) for \(r=n-1\). Consequently **every finite composition** of sliding erosions and dilations of arbitrary radii is nonexpansive in unweighted two-input path variation, regardless of its number of stages.

## Assumptions and scope

Signals are arbitrary elements of \(\mathbb R^n\); weights are strictly positive, and the windows are the **closed, truncated, radius-\(r\) contiguous index intervals** written above. There are no periodic boundary conditions, no vertex weights, and no positivity or monotonicity restriction on signals. A quotient involving zero denominator is excluded from the supremum; translation equivariance ensures that such pairs cannot create nonzero output variation. In the degenerate radius \(r=n-1\), the output is constant in space.

## Proof

**1. Monotone selector principle.** At an input whose coordinates are pairwise distinct, a running minimum or maximum is a coordinate selector: there are indices \(p_1,\ldots,p_n\) such that \((Sf)_i=f_{p_i}\). Choose the leftmost optimizing index in each window. The sequence \((p_i)\) is nondecreasing. Indeed, consecutive windows have nondecreasing left and right endpoints. If \(p_{i+1}<p_i\), both optimizing indices belong to the intersection of the consecutive windows. Optimality in both windows forces equality of their selected values, contradicting distinctness (or contradicting leftmost tie-breaking when equality is allowed). Thus \(p_i\le p_{i+1}\).

At a generic input the operator agrees in a neighborhood with the selector matrix \((Q_ph)_i=h_{p_i}\). Let \(\Delta h_k=h_{k+1}-h_k\). Then
\[
(Q_ph)_{i+1}-(Q_ph)_i=\sum_{k=p_i}^{p_{i+1}-1}\Delta h_k.
\]
The intervals \([p_i,p_{i+1}-1]\) are pairwise disjoint (empty intervals are permitted). Consequently
\[
V_w(Q_ph)\le\sum_{k=1}^{n-1}\left(\sum_{i:p_i\le k<p_{i+1}}w_i\right)|\Delta h_k|.
\]
For each fixed \(k\), the inner sum contains at most one term. Therefore the exact variation operator norm of \(Q_p\) equals the maximum of the ratios \(w_i/w_k\) for crossings \(p_i\le k<p_{i+1}\), or zero if no crossing occurs. Equality follows by choosing a step perturbation with its only jump across edge \(k\).

**2. All and only possible crossings.** Use one-based edge indices. Consecutive windows at vertices \(i\) and \(i+1\) coincide if and only if \(i\le r\) and \(i+r\ge n\). In this case \(p_i=p_{i+1}\). Otherwise the edge is active: \(i>r\) (an old left endpoint exits), or \(i+r<n\) (a new right endpoint enters). The bounds on the two selector indices show that any crossing \(p_i\le k<p_{i+1}\) necessarily satisfies
\[
\max(1,i-r)\le k\le\min(n-1,i+r).
\]
Every listed crossing is realizable with strictly distinct coordinates. If \(i>r\), assign the unique minimum value \(0\) to vertex \(i-r\) and the unique second minimum value \(1\) to vertex \(k+1\), with all other input values distinct and greater than \(1\). The minimum selector changes from \(p_i=i-r\) to \(p_{i+1}=k+1\). If instead \(i+r<n\), assign \(0\) to vertex \(i+r+1\) and \(1\) to vertex \(k\); then the minimum selector changes from \(p_i=k\) to \(p_{i+1}=i+r+1\). This covers both possible active-edge mechanisms. Negating these signals gives the corresponding maximum-selector witnesses.

**3. Global upper bound and sharpness.** Along the segment \(f+t(g-f)\), each finite-window minimum or maximum is piecewise affine in \(t\), with finitely many breakpoints. At almost every regular parameter value its derivative is a selector map of the type described above. Thus, for \(h=g-f\),
\[
V_w\bigl(Sg-Sf\bigr)\le\int_0^1V_w\bigl(Q_{p(t)}h\bigr)\,dt
\le\mathcal L_{n,r}(w)V_w(h).
\]
Continuity removes all input-tie exceptional cases. Conversely, for each realized crossing of part 2, take its strictly ordered witness \(f\) and the perturbation \(g=f+\varepsilon h\), where \(h_j=0\) for \(j\le k\), \(h_j=1\) otherwise, and \(\varepsilon>0\) is small enough to retain the selector. Then \(V_w(g-f)=\varepsilon w_k\) and \(V_w(Sg-Sf)=\varepsilon w_i\). Every ratio in the formula is therefore attained.

**4. Classification of contraction weights.** For \(1\le r\le n-2\), the active edge set is nonempty and every pair \(i,k\) of active edges with \(|i-k|\le r\) appears in both orientations of the sharp-ratio formula. Nonexpansivity therefore forces their weights to agree. Each of the left and right active bands is contiguous; their nearest indices differ by \(2r-n+2\le r\), so the two bands also have the same weight \(c\). Every inactive edge is within distance \(r\) of the last edge of the left active band, hence its weight must be at least \(c\). Conversely, if these conditions hold, every admissible numerator has weight \(c\) and every denominator is at least \(c\); thus every listed ratio is at most \(1\). All edges are active exactly when \(n\ge2r+1\). At \(r=n-1\), all windows are identical and all output differences vanish.

**5. Compositions.** When the weights are uniform, the sharp one-stage coefficients are at most \(1\). Multiplying the Lipschitz inequalities across any finite composition of erosion and dilation operators establishes the stated two-input contraction, without any need for the composite map to be linear or idempotent.

## Verification

Run the standalone `verify.py` using a standard Python 3 interpreter; it requires no external libraries. It exhaustively enumerates strictly ordered inputs in 35 choices of path size and radius for \(2\le n\le8\); compares realized selectors with the derived crossing set; constructs exact local sharpness witnesses; tests positive weight profiles; and checks arbitrary-input inequalities using exact rational arithmetic. This checks finite cases only. The all-size theorem follows from the preceding proof.

## Relationship to prior work

Rohwer's 2002 study of LULU smoothing and the full-text 2007 treatment by Anguelov and Rohwer establish **single-input** total-variation preservation or decomposition properties for LULU operators. These do not state the **two-input weighted-variation Lipschitz coefficient** for sliding min/max maps on finite paths. The 2007 study defines lower and upper envelopes and examines their single-input variation preserving behavior. In contrast, the present result computes exact perturbation sensitivity and classifies every contractive choice of inhomogeneous edge weights, with a boundary-overlap transition. Previous results on cyclic flat dilation and on median smoothing address different boundary conventions, weight assumptions, or rank selectors. One-input variation reduction is logically insufficient to imply two-input Lipschitz contraction: running median smoothing provides a concrete counterexample to that implication.

## Limitations

No statement is made for disconnected or non-interval neighborhoods, multidimensional images, periodic boundary conditions, weighted order statistics, or spatially adaptive windows. Arbitrary finite compositions are proved contractive only in **unweighted** variation, not with arbitrary nonconstant weights unless each individual stage satisfies its own weighted criterion. The theorem does not show that an arbitrary graph morphological filter shares the same bound. The archived LULU monograph and the original 2002 paper were not fully inspectable in the present comparison, leaving a residual possibility of equivalent older coverage not visible in the accessible primary text.

## References

1. R. Anguelov and C. Rohwer, *LULU operators for functions of continuous argument*, arXiv:0711.1944v1, first submitted 13 November 2007, https://arxiv.org/html/0711.1944v1 . In particular Sections 2 and 5, including the single-input preservation identity.
2. C. H. Rohwer, *Variation reduction and LULU-smoothing*, Quaestiones Mathematicae **25** (2002), 163–176, DOI: 10.2989/16073600209486008. Bibliographic record and abstract inspected; full primary text not obtained.
3. R. Anguelov and I. Fabris-Rotelli, *LULU operators and discrete pulse transform for multidimensional arrays*, IEEE Transactions on Image Processing **19** (2010), 3012–3024. Context for the one-input variation-preserving literature.
4. C. H. Rohwer, *Nonlinear Smoothing and Multiresolution Analysis*, Birkhäuser, 2005, Chapter 7 *Variation Reduction and Shape Preservation*. Bibliographic chapter listing inspected; full chapter not obtained.
