# A divergent startup third divided difference in the LIMM error estimator

## Finding

The printed first-step initialization for the third divided difference in the adaptive linearly implicit multistep (LIMM) integrator is inconsistent with the paper’s own factorial-normalized convention. On the scalar test equation \(y'=y\), with \(y(0)=1\), the prescribed first-order LIMM starter and the formulas in Remark 7.2 give

\[
\widehat{\delta^2}=\frac{1}{2(1-h)},\qquad
\widehat{\delta^3}=\frac{2h-1}{6h(1-h)}.
\]

Hence \(h\widehat{\delta^3}\to-1/6\) as \(h\downarrow0\), so the prescribed \(\widehat{\delta^3}\) diverges like \(-1/(6h)\). By the paper’s own definition, the exact normalized third divided difference tends instead to \(y'''(0)/3!=1/6\). The order-two local-error estimate in equation (7.5) therefore has an \(h^2\) leading scale, not the expected \(h^3\) scale, whenever its order-two error coefficient is nonzero.

## Assumptions and scope

Use the paper’s order-one LIMM starter with \(\nu_0=0\), \(\alpha_{-1}=1\), \(\alpha_0=-1\), \(\beta_0=1\), \(\mu_0=-\mu_{-1}\), and \(\sigma(0)=0\). The last condition forces \(\mu_{-1}=1\), giving

\[
(I-hJ_0)(y_1-y_0)=h f_0.
\]

The test problem is smooth, its exact solution is \(y(t)=e^t\), and the step size satisfies \(0<h<1\). The claim concerns the formula printed for initializing the startup divided differences and the resulting order-two estimator. It does not assert that the full LIMM method is divergent, that the fixed-step convergence theorem is false, or that a software implementation necessarily follows the printed formula without correction.

## Proof

For \(y'=y\) at \(y_0=1\), we have \(f_0=J_0=1\). The first-order LIMM update gives \(y_1=1+h/(1-h)=1/(1-h)\). Substitution into the first formula of Remark 7.2 yields

\[
\widehat{\delta^2}
=\frac{(y_1-y_0)/h-f_0}{2h}
=\frac{1}{2(1-h)}.
\]

The same remark prescribes \(\widehat{\delta^3}=(\widehat{\delta^2}-J_0f_0)/(3h)\), so

\[
\widehat{\delta^3}
=\frac{1/(2(1-h))-1}{3h}
=\frac{2h-1}{6h(1-h)}.
\]

Multiplying by \(h\) gives \(h\widehat{\delta^3}=(2h-1)/(6(1-h))\to-1/6\). Thus \(\widehat{\delta^3}\sim-1/(6h)\). In contrast, equation (7.4) defines the normalized order-three divided difference using the factor \(3!\), so its exact small-step limit is \(y'''(0)/3!=1/6\). Finally, equation (7.5) multiplies the startup quantity by a nonzero constant and \(h^3\); the displayed divergence makes that estimate scale as \(h^2\). The included `verify.py` checks the rational identities exactly using fractions.

## Verification

The scalar update, both startup formulas, and the limiting coefficient were checked symbolically by exact rational algebra and replayed with the dependency-free script `verify.py`. This is an exact calculation, not a finite numerical experiment used as proof of a limit. The paper’s printed formulas and normalized divided-difference definition were read directly in the primary full text. No claim is made about the authors’ implementation code.

## Relationship to prior work

The primary source is Glandon, Narayanamurthi, and Sandu, “Linearly Implicit Multistep Methods for Time Integration,” especially equations (2.4), (4.2), (7.4), (7.5), and Remark 7.2. The article explicitly defines the normalized divided difference as \(y^{(k+1)}(\xi)/(k+1)!\); the startup formula is evaluated against that same convention. The decisive comparison is within the primary paper itself: equation (7.4) fixes the factorial normalization, while Remark 7.2 supplies the inconsistent startup recipe.

## Limitations

The result is limited to the published startup formula. The first-step initialization may have been corrected in software or an erratum that was not inspected. The calculation does not invalidate the fixed-step order or convergence results for LIMM, and it does not quantify the effect on a complete adaptive run after later history updates. The practical consequence is a wrong asymptotic scale for the printed startup error estimate, which can distort initial step-size or order selection.

## References

1. Ross Glandon, Mahesh Narayanamurthi, and Adrian Sandu, “Linearly Implicit Multistep Methods for Time Integration,” arXiv:2011.10685v1, first publicly available 2020-11-21; later published in *SIAM Journal on Scientific Computing* 44(6), DOI 10.1137/20M133748X.
2. The same paper, equation (7.4) and Remark 7.2, for the divided-difference normalization and startup initialization formulas.
