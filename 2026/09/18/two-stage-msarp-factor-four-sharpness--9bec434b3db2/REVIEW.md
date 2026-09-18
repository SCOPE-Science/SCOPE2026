# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** For a rank-two projection kernel \(K=aa^T+bb^T=I-cc^T\), conditioning on a first-stage pivot \(i\) gives the second-stage probability
\[
\Pr(j\mid i)=\frac{\det K[\{i,j\},\{i,j\}]}{K_{ii}}
=\frac{c_\ell^2}{1-c_i^2},
\]
where \(\ell\) is the omitted coordinate. Multiplication by the first-stage probability \(a_i^2\) gives the stated omission law. Its normalization follows exactly from \(r_i(1-c_i^2)=a_i^2\).

For \(A_\eta=\operatorname{diag}(2,1,\eta)[a,b,c]^T\), the oblique interpolant reproduces the \(a\)- and \(b\)-rows exactly. When \(\ell\) is omitted, the remaining residual is supported at coordinate \(\ell\) and has inner product one with \(c\), so its squared norm is \(1/c_\ell^2\). This yields the exact expected factor \(2\sum_i r_i\). The inequality \(\sum_i r_i\le2\) follows from \(1-r_i\ge b_i^2\), and the displayed one-parameter orthogonal family drives the factor to 4.

For the true orthogonal CSS projection, the scalar Schur-complement identity gives
\[
E_\ell=1/(A_\eta^TA_\eta)^{-1}_{\ell\ell}
\]
and hence the displayed exact formula. Taking \(\eta\downarrow0\) recovers the oblique factor for every fixed frame with nonzero \(c_i\). This proves sharpness of 4 because orthogonal projection is pointwise no worse than the oblique interpolant. The one-shot projection-DPP omission law is \(\Pr(L=\ell)=c_\ell^2\), giving limit 3 and the \(4/3\) separation.

The public verification artifact checks a nondegenerate full-rank rational witness and reproduces all reported finite values with exact rational arithmetic.

## Originality

**PASS, to the best of our knowledge.** The one-shot \(k+1\) ARP/volume-sampling bound and its worst-case optimality are established prior results and are not claimed as new. Grigori--Xue prove tightness of their conditional augmentation bound for a prescribed initial subset, but their current v1 does not state sharpness of the complete joint two-stage MSARP bound. Their text instead notes that the product bound is larger than the one-shot bound and reports comparable empirical performance.

Searches by the source title and arXiv identifier, MSARP/multi-stage ARP terminology, conditional projection DPPs, sequential/incremental volume sampling, factor-four sharpness, and equivalent column-subset formulations found no prior statement of the exact three-coordinate omission law, sharp factor 4 for the joint two-stage sampler, or the fact that sharpness persists for optimal orthogonal CSS projection. The source preprint is very recent, so an unindexed contemporaneous result remains a residual originality risk.

Classical volume-sampling and projection-DPP literature contains sharp one-shot bounds, and general DPP literature contains conditioning identities. Those ingredients do not by themselves state the staged worst-case result; the contribution is their exact combination for MSARP together with the sharp construction and the orthogonal-CSS separation.

## Value

**PASS.** The new MSARP paper presents the product factor as the theoretical price of incremental selection but does not determine whether that price is intrinsic. The result shows that the first nontrivial product factor is genuinely unavoidable in the stated worst-case model, and that the loss is not removed by evaluating the stronger orthogonal CSS approximation used in the experiments. It therefore identifies a real worst-case cost of preserving an earlier randomized pivot and quantitatively separates incremental from one-shot ARP.

## Scope and limitations

The sharpness family approaches rank deficiency and large condition number, so the theorem is a uniform worst-case statement rather than a claim about typical data. It treats two stages of sizes \(1+1\) only and does not establish sharpness of the general \(\prod_i(1+k_i)\) or \(2^t\) bounds. It assumes the exact dominant rank-two right singular subspace and exact arithmetic, and it does not analyze approximate subspaces, finite precision, fixed-precision stopping, or Nyström-specific structure.
