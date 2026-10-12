# Sharp angular–imbalance frontier for pointwise random-reshuffling risk on two SPD quadratics

## Finding

Two-component random reshuffling need not decrease the expected squared distance to the common minimizer **for every initial direction**, even when it strictly improves the worst-direction mean-square error. An exact angular–imbalance threshold separates these statements.

Let \(u,v\in\mathbb R^2\) be unit vectors with \(c=|u^{\mathsf T}v|\in(0,1)\), and let \(a,b\in(0,1)\). Define the two smooth, strongly convex quadratic components
\[
 f_1(x)=\tfrac12 x^{\mathsf T}(I-a uu^{\mathsf T})x,\qquad
 f_2(x)=\tfrac12 x^{\mathsf T}(I-b vv^{\mathsf T})x.
\]
Their unique common minimizer is \(0\). Starting from any deterministic \(x\in\mathbb R^2\), take two gradient steps with unit stepsize. Protocol RR chooses each of the two orders \((1,2)\) and \((2,1)\) with probability \(1/2\). Protocol IID chooses each index independently and uniformly, allowing repeated indices. Let \(L_{\rm RR}(x)\) and \(L_{\rm IID}(x)\) be the respective expected squared final Euclidean norms. Then
\[
\boxed{L_{\rm RR}(x)=\frac{a^2b^2c^2}{2}\bigl[(u^{\mathsf T}x)^2+(v^{\mathsf T}x)^2\bigr],}
\]
\[
\boxed{L_{\rm IID}(x)-L_{\rm RR}(x)
=\frac14\Bigl[(a^4-a^2b^2c^2)(u^{\mathsf T}x)^2
+(b^4-a^2b^2c^2)(v^{\mathsf T}x)^2\Bigr].}
\]
Consequently,
\[
\boxed{L_{\rm RR}(x)\le L_{\rm IID}(x)\ \text{for all }x
\quad\Longleftrightarrow\quad c\le\min\{a/b,b/a\}.}
\]
Below the boundary the inequality is strict for every nonzero initial state. At equality precisely one nontrivial initial-direction line has equality. Above the boundary there are both directions that favor RR and directions that favor IID. Nevertheless, RR **always** has a strictly smaller *worst-unit-initial-direction* risk:
\[
\sup_{\|x\|=1}L_{\rm RR}(x)
=\frac{a^2b^2c^2}{2}(1+c)
<\sup_{\|x\|=1}L_{\rm IID}(x).
\]
Finally, \(L_{\rm RR}(x)<2L_{\rm IID}(x)\) for every nonzero \(x\), and the factor \(2\) is a sharp supremum over these models and initial states. Thus a sharp per-instance directional reversal and a universal strict worst-case improvement can coexist.

An exact witness has \(a=1/4\), \(b=3/4\), \(u=(1,0)\), \(v=(3/5,4/5)\), and \(x=(-4/5,3/5)\). Then
\[
L_{\rm RR}(x)=\frac{81}{20000},\qquad
L_{\rm IID}(x)=\frac{53}{20000},\qquad
\frac{L_{\rm RR}(x)}{L_{\rm IID}(x)}=\frac{81}{53}>1.
\]

## Assumptions and scope

All computations take place in exact real arithmetic. The problem dimension and the number of components are both two. The two unit directions are linearly independent and nonorthogonal, and the attenuation parameters lie strictly between zero and one. Component Hessians \(I-a uu^{\mathsf T}\) and \(I-b vv^{\mathsf T}\) are positive definite, with eigenvalues \(1-a,1\) and \(1-b,1\), respectively. There is no gradient noise or numerical rounding. The time horizon is **exactly two component steps**, comparing one full reshuffled pass with two independent-with-replacement choices. Risks are squared Euclidean distances, not arbitrary weighted objective metrics. No statement is made about the mean iterate, more passes, or step-count-normalized wall-clock cost.

## Proof

**Exact two-step Gram operators.** The unit gradient steps have linear matrices \(A=a uu^{\mathsf T}\) and \(B=b vv^{\mathsf T}\). Since \(A^2=a^2uu^{\mathsf T}\), \(B^2=b^2vv^{\mathsf T}\), and \(u^{\mathsf T}v=\pm c\), direct multiplication gives
\[
(BA)^{\mathsf T}(BA)=a^2b^2c^2uu^{\mathsf T},\qquad
(AB)^{\mathsf T}(AB)=a^2b^2c^2vv^{\mathsf T}.
\]
The squared-error Gram matrices are therefore
\[
G_{\rm RR}=\tfrac12 a^2b^2c^2(uu^{\mathsf T}+vv^{\mathsf T}),
\]
\[
G_{\rm IID}=\tfrac14\bigl[(a^4+a^2b^2c^2)uu^{\mathsf T}
+(b^4+a^2b^2c^2)vv^{\mathsf T}\bigr].
\]
The displayed risk identities follow by taking the quadratic form in \(x\).

**Necessity, sufficiency, and directional reversal.** The vectors \(u,v\) are linearly independent, so the linear map \(x\mapsto (u^{\mathsf T}x,v^{\mathsf T}x)\) is invertible. Thus a quadratic form of the shape \(\alpha(u^{\mathsf T}x)^2+\beta(v^{\mathsf T}x)^2\) is nonnegative for all \(x\) if and only if both \(\alpha,\beta\ge0\). Here those inequalities are equivalent to \(a\ge bc\) and \(b\ge ac\), or \(c\le\min\{a/b,b/a\}\). Both coefficients are strictly positive below the threshold. On the threshold exactly one is zero: both could be zero only if \(c=1\), excluded by assumption. The invertible coordinate map then identifies a single zero-gap line. Above the threshold exactly one coefficient is negative (both cannot be negative for \(c<1\)); choosing the other linear functional to vanish gives a negative gap, and choosing the first to vanish gives a positive gap. This establishes both sides of the sharp frontier.

**Strict worst-direction advantage.** Choosing the sign of \(v\) to make \(u^{\mathsf T}v=c\) leaves both update matrices unchanged. The unit bisector \(z=(u+v)/\sqrt{2(1+c)}\) is the maximizing eigenvector of \(uu^{\mathsf T}+vv^{\mathsf T}\), whose largest eigenvalue is \(1+c\). Hence \(z^{\mathsf T}G_{\rm RR}z=a^2b^2c^2(1+c)/2\). But the difference at that very direction is
\[
z^{\mathsf T}(G_{\rm IID}-G_{\rm RR})z
=\frac{1+c}{8}\bigl[a^4+b^4-2a^2b^2c^2\bigr]
>0,
\]
where strictness follows from \(a^4+b^4\ge2a^2b^2\) and \(c<1\). Since the maximum of IID risk is at least its value at \(z\), the worst-case inequality is strict for every admissible parameter choice.

**Uniform excess factor and its sharpness.** Rewriting the IID formula gives
\[
L_{\rm IID}(x)=\tfrac12 L_{\rm RR}(x)
+\tfrac14\bigl[a^4(u^{\mathsf T}x)^2+b^4(v^{\mathsf T}x)^2\bigr]
>\tfrac12 L_{\rm RR}(x)
\]
for every nonzero \(x\), because \(u,v\) span the plane. For fixed \(c\in(0,1)\) and fixed \(b\in(0,1)\), take \(x\perp v\) and \(a\downarrow0\). Direct substitution gives
\[
\frac{L_{\rm RR}(x)}{L_{\rm IID}(x)}
=\frac{2b^2c^2}{a^2+b^2c^2}\longrightarrow2.
\]
The example follows by exact rational substitution into the two formulas. This completes the proof for all parameter values and all deterministic initial states stated above.

## Verification

The independent expressions for both sampling protocols were computed by direct matrix multiplication and by the analytical Gram formulas. The supplied standalone standard-library Python program `verify.py` performs exact rational checks for three Pythagorean pairs of directions, twenty-five attenuation pairs per direction pair, and five initial vectors per pair, plus algebraic frontier probes and an exact counterexample. Execute `python3 verify.py` to reproduce the exact identity checks. These finite tests check arithmetic and do **not** establish the continuous-parameter or universal-quantifier claims; those are proved above through the invertible-coordinate and spectral arguments.

## Relationship to prior work

Recht and Ré (2012) formulated noncommutative sampling-without-replacement comparisons and proved a two-matrix **operator-norm** comparison; an operator-norm inequality does not imply the all-initial-vector Loewner comparison classified here. De Sa (2020) provided counterexamples to other matrix-product sampling comparisons, using different product lengths and/or performance functionals. Safran and Shamir (first arXiv posting 2021-06-12) study conditioning-sensitive multi-epoch optimization bounds, emphasizing commuting quadratic terms. These do not characterize the stated noncommuting, two-step per-initialization boundary. A later anonymous metric-dependent manuscript (2026) explicitly distinguishes mean, Gram, and objective rankings, and develops large-simplex-family comparisons; the structural Gram formalism is acknowledged rather than claimed new. The present contribution is the sharp closed-form rank-one two-component angular–imbalance classification together with its opposite worst-direction ranking and the sharp universal factor-two envelope. The comparisons identify differences in statement, quantifier, model, and metric rather than inferring originality from unmatched titles. An equivalent result in unindexed specialized literature remains a priority risk.

## Limitations

This is a one-pass, two-dimensional, noiseless, exact-arithmetic classification. The result does not show that IID is better in worst-case Euclidean error, in expected optimization objective, or after an arbitrary number of epochs. The endpoints \(c=0\) and \(c=1\), and degenerate parameters \(a=0\) or \(b=0\), are outside the main classification. The sharp factor \(2\) is a supremum, not attained for admissible positive attenuations. Scientific originality has not undergone independent external audit.

## References

- B. Recht and C. Ré, “Toward a Noncommutative Arithmetic–Geometric Mean Inequality: Conjectures, Case-Studies, and Consequences,” COLT / PMLR 23 (2012), https://proceedings.mlr.press/v23/recht12.html .
- C. De Sa, “Random Reshuffling Is Not Always Better,” NeurIPS (2020), https://papers.neurips.cc/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html .
- I. Safran and O. Shamir, “Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems,” arXiv:2106.06880, initial deposit June 12, 2021, https://arxiv.org/abs/2106.06880 .
- Anonymous, “Which Sampling Scheme Is Better? Metric-Dependent Rankings in Random Reshuffling Dynamics,” publicly available version associated with doi:10.5281/zenodo.22037371 (2026); https://github.com/ipitchford/exact-low-length-recht-re-inequalities .
