# A sharp logarithmic-codimension diameter law for Haar projections of regular simplices

## Finding
Fix \(c\in(0,\infty)\). For each integer \(m\ge3\), consider the Euclidean regular simplex \(S_m=\operatorname{conv}\{e_1,\dots,e_m\}\subset\mathbb R^m\), of edge length \(\sqrt2\). Discard a Haar-uniform \(k_m\)-dimensional linear subspace of its \((m-1)\)-dimensional affine direction space, where \(k_m/\log m\to c\). Write \(\Delta_m\) for the diameter of the surviving orthogonal projection. If \(s_c\) is the unique root in \((0,1)\) of \(s_c-1-\log s_c=4/c\), then
\[
\frac{m}{k_m}\left(\sqrt2-\Delta_m\right)\xrightarrow{\mathbb P}\frac{s_c}{\sqrt2}.
\]
Thus the geometrically natural logarithmic-codimension scale has an explicit nontrivial limiting diameter-loss coefficient. The root depends strictly increasingly on \(c\); its endpoints satisfy \(s_c\sim\exp(-1-4/c)\) as \(c\downarrow0\) and \(s_c\to1\) as \(c\to\infty\). These endpoint statements concern the deterministic coefficient, not a two-parameter limit with varying \(c\).

## Assumptions and scope
The affine direction space is \(H_m=\{x\in\mathbb R^m:\sum_{i=1}^m x_i=0\}\). The discarded plane \(W_m\) has Haar probability distribution on the Grassmannian of \(k_m\)-planes in \(H_m\), and the projected diameter is measured with the induced ambient Euclidean norm in \(H_m\cap W_m^\perp\). We assume integer \(1\le k_m<m-1\) and \(k_m/\log m\to c\in(0,\infty)\); hence \(k_m\to\infty\) and \(k_m=o(m)\). Every convergence statement is in probability over \(W_m\). No assertion is made for fixed discarded codimension, for codimension comparable with \(m\), or for nonorthogonal projections.

## Proof
**1. Exact Gaussian realization.** Set \(C_m=I_m-m^{-1}{\bf1}{\bf1}^{\mathsf T}\). Let \(Z\) be an \(m\times k_m\) matrix whose entries are independent standard normals, let \(A=C_mZ\), and let \(S=A^{\mathsf T}A=Z^{\mathsf T}C_mZ\). The columns of \(A\) span a Haar-uniform \(k_m\)-plane in \(H_m\) (rotational invariance of the Gaussian law). With probability one \(S\) is invertible for sufficiently large \(m\), and \(Q=AS^{-1/2}\) has orthonormal columns. If \(Z_i\in\mathbb R^{k_m}\) is row \(i\) of \(Z\), then
\[
\|P_{W_m}(e_i-e_j)\|^2=(Z_i-Z_j)^{\mathsf T}S^{-1}(Z_i-Z_j).
\]
Every diameter of a finite convex hull is attained between vertices. As each edge of \(S_m\) has squared length \(2\), orthogonal Pythagoras gives the exact identity
\[
\Delta_m^2=2-\min_{i<j}(Z_i-Z_j)^{\mathsf T}S^{-1}(Z_i-Z_j).\tag{1}
\]

**2. Simultaneous spectral normalization.** The matrix \(S\) is Wishart with \(m-1\) degrees of freedom. Its entrywise second moments yield \(\mathbb E\|S/m-I_{k_m}\|_{\mathrm F}^2=O(k_m^2/m)\to0\). Consequently \(\|S/m-I\|_{\mathrm{op}}\to0\) in probability. Hence, simultaneously for **every** pair \(i<j\), the quadratic form in (1) lies between \((1-o_{\mathbb P}(1))\|Z_i-Z_j\|^2/m\) and \((1+o_{\mathbb P}(1))\|Z_i-Z_j\|^2/m\); this follows from Loewner bounds on \(S^{-1}\) and needs no independence between \(S\) and the rows.

**3. A growing-dimensional nearest-pair theorem.** Put \(k=k_m\), \(T_m=k^{-1}\min_{i<j}\|Z_i-Z_j\|^2\), and for \(0<s<1\) write
\[
I(s)=\tfrac12(s-1-\log s),\quad p_k(s)=\Pr\{\|Z_1-Z_2\|^2\le2ks\}.
\]
Because \(\|Z_1-Z_2\|^2/2\) is \(\chi_k^2\), exponential tilting of the sum of \(k\) independent squared standard normals gives the Cramér estimate
\[
\log p_k(s)=-kI(s)+o(k),\qquad k\to\infty.\tag{2}
\]
The upper bound comes from the chi-square moment-generating function; the lower bound is obtained by tilting the coordinates to variance \(s\), restricting their average square to a vanishingly small fixed interval below \(s\), applying the law of large numbers, and then shrinking that interval. In particular (2) concerns each fixed \(s\in(0,1)\).

Let \(X_s\) count the \(\binom m2\) pairs for which the event in the definition of \(p_k(s)\) occurs. Then \(\mathbb E X_s=\binom m2p_k(s)\). If \(cI(s)>2\), (2) and Markov's inequality give \(\Pr\{X_s>0\}\to0\).

For the complementary implication, only pairs of indicators with a shared Gaussian point can be dependent. Define \(q_k(s)=\Pr\{\|Z_1-Z_2\|^2\le2ks,\ \|Z_1-Z_3\|^2\le2ks\}\). On the joint event the sum of both squared distances is at most \(4ks\). The two one-coordinate differences have covariance matrix with eigenvalues \(3\) and \(1\). The exponential Markov bound at \(\theta=(1-s)/(4s)>0\) yields
\[
q_k(s)\le\exp(-kJ(s)),\qquad
J(s)=\frac12\log[(1+6\theta)(1+2\theta)]-4s\theta.\tag{3}
\]
The crucial strict overlap estimate is
\[
4\bigl(J(s)-\tfrac32 I(s)\bigr)=H(s),\qquad
H(s)=2\log\frac{(3-s)(1+s)}4-\log s+s-1.\tag{4}
\]
Here \(H(1)=0\) and direct differentiation gives
\[
H'(s)=-\frac{(1-s)^2(s+3)}{s(3-s)(1+s)}<0
\quad(0<s<1).
\]
Thus \(J(s)>\tfrac32I(s)\). The disjoint-pair indicators are independent, so counting at most \(O(m^3)\) overlapping pairs gives
\[
\frac{\operatorname{Var}X_s}{(\mathbb EX_s)^2}
\le\frac1{\mathbb EX_s}+O\!\left(\frac{q_k(s)}{m p_k(s)^2}\right).
\]
If \(cI(s)<2\), the first term tends to zero by (2), and logarithms of the second term are bounded by
\[
-\log m+k\,[2I(s)-J(s)+o(1)]
<-\log m+\tfrac12 kI(s)+o(k)\to-\infty.
\]
Therefore \(\Pr\{X_s=0\}\to0\) by Chebyshev. The strictly decreasing continuous map \(I:(0,1)\to(0,\infty)\) has a unique root \(s_c\) with \(I(s_c)=2/c\). Applying the two preceding bounds at fixed values immediately below and above \(s_c\) proves
\[
T_m\xrightarrow{\mathbb P}2s_c.\tag{5}
\]

**4. Diameter deficit.** By (1), (5), and the simultaneous spectral bounds, \(2-\Delta_m^2=(2k_m/m)s_c(1+o_{\mathbb P}(1))\). In particular \(\Delta_m\to\sqrt2\) in probability. Divide the difference of squares by \(\sqrt2+\Delta_m\) to obtain the stated limit. Finally \(I'(s)=(1-1/s)/2<0\), so the implicit root is strictly increasing with \(c\); the endpoint formulas follow directly by expanding \(s-1-\log s=4/c\). This completes the proof.

## Verification
The standalone, standard-library-only program `verify.py` checks two independent finite representations of discarded squared edge lengths: (i) Gaussian Gram-matrix inversion and (ii) orthonormal-basis projection. It also checks the exact algebraic identity (4), the sign of its derivative, and selected numerical solutions of the rate equation. Running `python verify.py` yielded `PASS: 990 edge-identity comparisons; 10005 rate/Chernoff checks.` These are finite consistency checks; they do not prove the limiting theorem. The decisive steps are the analytic rate estimate, strict overlap exponent inequality, and second-moment argument above.

## Relationship to prior work
Baryshnikov–Vitale (1994) connects random projections of regular simplices with Gaussian samples; the present proof derives the needed Gaussian representation directly and studies a particular Euclidean metric invariant. Böröczky–Henk (1997 preprint) analyzes face counts of projected regular polytopes; face counts, and their affine-Gaussian formulations, do not imply the metric diameter deficit. Kanagawa–Mochizuki–Tanaka (1992) studies nearest-pair limit laws at **fixed** ambient dimension. Here the Gaussian ambient dimension diverges at the critical \(\log m\) scale, and the shared-endpoint dependence must be controlled quantitatively by (3)–(4). Kabluchko–Litvak–Zaporozhets (arXiv v1, 2015) studies mean width and Gaussian maxima for regular polytopes, not the near-full-dimensional projected diameter.

## Limitations
Only the logarithmic discarded-codimension regime with fixed positive limiting ratio is proved. The convergence is in probability, not an explicit finite-sample error rate or central limit theorem. Historical novelty is assessed against accessible primary texts and bibliographic material, but the complete Baryshnikov–Vitale (1994) original and Affentranger–Schneider (1992) original were unavailable to inspect, so an undiscovered equivalent high-dimensional result remains a bibliographic risk. The cited November 26, 2015 public preprint is a dated, domain-relevant archive source, not a claim about the first historical publication of the broader theory.

## References
- Kanagawa, Mochizuki and Tanaka (1992), *Limit theorems for minimum interpoint distance between any pair of iid random points in R^d*, Annals of the Institute of Statistical Mathematics 44, 121–131. Full text: https://www.ism.ac.jp/editsec/aism/pdf/044_1_0121.pdf
- Baryshnikov and Vitale (1994), *Regular Simplices and Gaussian Samples*, DOI: https://doi.org/10.1007/BF02574000 (bibliographic description inspected; full text inaccessible).
- Böröczky and Henk, *Random Projections of Regular Polytopes*, preprint dated May 1997; available at https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf
- Kabluchko, Litvak and Zaporozhets (2015), *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first posted November 26, 2015, https://arxiv.org/abs/1511.08479
