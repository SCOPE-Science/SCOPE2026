# Exact three-halves opening of the Potts external-field cusp
## Finding
For the single-colour completely homogeneous branch of the ferromagnetic \(q\)-state Potts model with constant external field studied by Bogachev and Rozikov, fix integers \(k\ge2\) and \(q\ge2\). Put
\[
\rho=\frac{k+1}{k-1},\qquad
\theta_c=\frac{\sqrt{(q-2)^2+4(q-1)\rho^2}-(q-2)}{2}.
\]
Let \(\alpha_-(\theta)<\alpha_+(\theta)\) be the two fold fields defined by equations (2.35)--(2.41) of the source. Then, as \(\theta\downarrow\theta_c\),
\[
\alpha_+(\theta)-\alpha_-(\theta)
=C_{k,q}(\theta-\theta_c)^{3/2}+O\!\left((\theta-\theta_c)^2\right),
\]
with the explicit positive amplitude
\[
C_{k,q}=\frac{(k-1)^4}{3\sqrt{k}(k+1)^2\log\theta_c}
\left(\frac{2\theta_c+q-2}{q-1}\right)^{3/2}.
\]
Thus the source's one/three-solution boundary has an exact semicubical \(3/2\)-opening at its cusp. For \(q=2\), the source has \(\alpha_-(\theta)=-\alpha_+(\theta)\), so the individual branches satisfy
\[
\alpha_\pm(\theta)=\pm\frac{C_{k,2}}2(\theta-\theta_c)^{3/2}+O\!\left((\theta-\theta_c)^2\right).
\]

## Assumptions and scope
The parameters satisfy \(k\in\{2,3,\ldots\}\), \(q\in\{2,3,\ldots\}\), and \(\theta>\theta_c>1\). The functions \(\alpha_\pm\) are exactly the source's fold curves for the positive solutions of its scalar equation (2.32). By Theorem 2.8 of the source, that scalar equation has three positive solutions precisely for \(\alpha_-(\theta)<\alpha<\alpha_+(\theta)\), two on the folds, and one outside them. The result here quantifies only the local width of this scalar three-solution strip. It does not count solutions of the source's multi-colour system (2.33), does not determine the total number of completely homogeneous splitting Gibbs measures, and does not address extremality or thermodynamic stability.

## Proof
Write
\[
b(\theta)=\frac{\theta(\theta+q-2)}{q-1},\qquad b_c=\rho^2,
\]
so \(b(\theta_c)=b_c\). At a fold, the source's equation (2.37) can be solved for \(b\) in terms of its positive root \(x\):
\[
b=B(x):=\frac{x(x+k+1)}{(k-1)x-1}.
\]
The two fold roots coalesce at \(x=\rho\). If \(\varepsilon=b-b_c\), the exact quadratic formula gives
\[
x_\pm=\rho+\frac{k-1}{2}\varepsilon
\pm\sqrt{k\varepsilon+\frac{(k-1)^2}{4}\varepsilon^2}.
\]
Consequently,
\[
x_\pm-\rho=\pm\sqrt{k}\,\varepsilon^{1/2}
+\frac{k-1}{2}\varepsilon+O(\varepsilon^{3/2}).
\]

On the fold relation, the source's quantity \(a\) from equation (2.40) simplifies exactly to
\[
a=A(x):=\frac{((k-1)x-1)^k}{k^k x^{k+1}}.
\]
Let \(L(x)=\log A(x)\). Direct differentiation at \(x=\rho\) gives
\[
L'(\rho)=0,
\]
\[
L''(\rho)=-\frac{(k-1)^2}{k(k+1)},
\qquad
L^{(3)}(\rho)=\frac{2(k-1)^3(2k+1)}{k^2(k+1)^2}.
\]
Taylor expansion at \(\rho\), together with the preceding two-root expansion, yields
\[
L(x_+)-L(x_-)
=\frac{(k-1)^4}{3\sqrt{k}(k+1)^2}\varepsilon^{3/2}
+O(\varepsilon^2).
\]
The indexing in equation (2.41) gives
\[
\alpha_+(\theta)-\alpha_-(\theta)
=\frac{L(x_+)-L(x_-)}{\log\theta}.
\]
Finally,
\[
\varepsilon=b(\theta)-b(\theta_c)
=\frac{2\theta_c+q-2}{q-1}(\theta-\theta_c)
+O\!\left((\theta-\theta_c)^2\right),
\]
and \(\log\theta=\log\theta_c+O(\theta-\theta_c)\). Substitution proves the stated coefficient \(C_{k,q}\). It is strictly positive because \(k\ge2\), \(q\ge2\), and \(\theta_c>1\). In the case \(q=2\), Proposition 6.17 of the source gives the exact antisymmetry \(\alpha_-=-\alpha_+\), so each branch is one half of the width with the corresponding sign.

## Verification
The standalone script `verify.py` re-evaluates the source's exact formulas for \(\theta_c\), \(x_\pm\), and \(a_\pm\), checks the critical derivative signs for \(2\le k\le100\), and compares the normalized numerical fold width against \(C_{k,q}\) for eight representative pairs \((k,q)\). Its successful replay prints `VERIFY_OK`. These finite checks are corroborative only; the proof above is analytic for every integer \(k,q\ge2\).

## Relationship to prior work
Bogachev and Rozikov define \(\theta_c\), \(b(\theta)\), \(x_\pm\), \(a_\pm\), and \(\alpha_\pm\) in equations (2.35)--(2.41), and Theorem 2.8 gives the exact one/two/three-positive-solution partition for the scalar branch. Their Figure 6 explicitly calls the meeting point of \(\alpha_+\) and \(\alpha_-\) the cusp point. The source does not state the \(3/2\) opening law or its amplitude. In the especially informative case \(q=2\), Proposition 6.17 derives only \(\alpha_\pm(\theta)=o(\theta-\theta_c)\); the formula above supplies the first nonzero term. Targeted published-record searches for the source identifier, cusp aliases, fold-width asymptotics, and semicubical formulations did not locate an implication-equivalent result.

## Limitations
The asymptotic is local as \(\theta\downarrow\theta_c\). It does not prove global monotonicity of either fold curve, does not sharpen the source's conjectures concerning all completely homogeneous measures, and does not address other branches of the boundary-law system. Search non-detection is not a proof of novelty; an equivalent calculation could exist in weakly indexed literature under different variables.

## References
1. L. V. Bogachev and U. A. Rozikov, “On the uniqueness of Gibbs measure in the Potts model on a Cayley tree with external field,” arXiv:1903.11440v1 (first public 2019-03-27); Journal of Statistical Mechanics: Theory and Experiment 2019, 073205, DOI:10.1088/1742-5468/ab270b. Relevant material: equations (2.35)--(2.41), Theorem 2.8, Figure 6, Proposition 6.17.
