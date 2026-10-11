# Exact forcing-induced mean skew in the periodically forced May–Leonard system
## Finding
Consider the periodically forced May–Leonard system
\[
\dot x=x((1-r)-cy+ez)+\gamma(1-x)\sin^2\theta,\qquad
\dot y=y((1-r)-cz+ex),\qquad
\dot z=z((1-r)-cx+ey),
\]
with \(r=x+y+z\), \(\dot\theta=2\omega\) on \(\mathbb R/\pi\mathbb Z\), \(0<e<c<1\), \(\omega>0\), and \(\gamma>0\). Let \(\mu\) be an invariant probability measure whose support is compactly contained in \(0<x,y,z<1\). Define
\[
X=\int x\,d\mu,\quad Y=\int y\,d\mu,\quad Z=\int z\,d\mu,
\]
and the forcing defect
\[
A=\gamma\int (x^{-1}-1)\sin^2\theta\,d\mu.
\]
Then \(A>0\), and for \(Q=c^2+ce+e^2\),
\[
Y-X=\frac{cA}{Q},\qquad X-Z=\frac{eA}{Q},\qquad X+Y+Z=\frac{3+A}{3+c-e}.
\]
In particular,
\[
Y>X>Z,\qquad \frac{Y-X}{X-Z}=\frac ce=\delta.
\]
Thus the ratio of the two finite-amplitude stationary mean gaps recovers exactly the attraction-strength parameter \(\delta\) used in the forced May–Leonard analysis. The same identities hold for every strictly positive phase-locked periodic orbit contained in the open unit cube, with the integrals replaced by period averages.

## Assumptions and scope
The statement uses the exact forced system printed by Rodrigues. The open-unit-cube hypothesis is natural for the population interpretation and is compatible with the forward-invariant closed cube: on \(x=1\), \(\dot x=-(1+c)y+(e-1)z\le0\); on \(y=1\), \(\dot y=(e-1)x-(1+c)z\le0\); on \(z=1\), \(\dot z=(e-1)y-(1+c)x\le0\), while the nonnegative coordinate faces point inward or are invariant.

For the invariant-measure formulation, compact containment in the open cube ensures that \(\log x\), \(\log y\), and \(\log z\) are legitimate bounded smooth observables on the support. The result does not assert that every SRB measure constructed in the source has this compact-interior property. For a phase-locked periodic orbit, strict positivity and containment in the open cube are sufficient directly.

## Proof
Invariance of \(\mu\) gives zero mean Lie derivative for each logarithmic coordinate. Therefore
\[
0=1-X-Y-Z-cY+eZ+A,
\]
\[
0=1-X-Y-Z-cZ+eX,
\]
\[
0=1-X-Y-Z-cX+eY.
\]
Put \(u=Y-X\) and \(v=X-Z\). Subtracting the last two unforced logarithmic balances gives
\[
cv=eu.
\]
Subtracting the first balance from the third gives
\[
A=(c+e)u+ev.
\]
Eliminating \(v\) yields
\[
u=\frac{cA}{c^2+ce+e^2},\qquad v=\frac{eA}{c^2+ce+e^2}.
\]
Adding all three logarithmic balances yields
\[
(3+c-e)(X+Y+Z)=3+A,
\]
which proves the total-mean identity.

It remains to show strict positivity of \(A\). The phase projection of any invariant probability measure for the continuous rotation \(\dot\theta=2\omega\) is Haar measure on \(\mathbb R/\pi\mathbb Z\). On the compact support, \(x<1\), so \(x^{-1}-1>0\); and \(\sin^2\theta>0\) away from two phase points of Haar measure zero. Since \(\gamma>0\), one has \(A>0\). Hence \(Y>X>Z\), and division of the two positive gap identities gives \((Y-X)/(X-Z)=c/e\).

For a phase-locked periodic orbit, integrating \(d(\log x)/dt\), \(d(\log y)/dt\), and \(d(\log z)/dt\) over one full period gives exactly the same three balances; the same algebra then applies.

## Verification
The accompanying `verify.py` symbolically reconstructs the three logarithmic balance equations, solves them, verifies the two gap identities and the total-mean identity, and checks the inward-pointing vector field on the three upper faces of the biological cube. Its recorded output is `VERIFY_OK`.

The proof itself is exact and does not rely on numerical integration, finite sampling, or small-\(\gamma\) asymptotics.

## Relationship to prior work
Rodrigues studies this exact periodically forced May–Leonard system, with \(\delta=c/e\) as the strength of attraction of the heteroclinic network, and proves abundance of rank-one strange attractors supporting SRB measures for a parameter regime. The paper's full text was inspected at the defining system, the parameter definitions, the main theorem, and its overview; searches within the full text for “mean” and “average” did not locate a species-mean identity. The source emphasizes return maps, bifurcations, periodic orbits, and SRB dynamics rather than exact finite-amplitude population averages.

Afraimovich, Hsu, and Lin study an earlier periodically perturbed May–Leonard model and derive a return map producing invariant tori, periodic behavior, and chaos. Their full text uses a different additive forcing architecture and does not state the gap law above. The present identity depends on the one-coordinate forcing \(\gamma(1-x)\sin^2\theta\) of the Rodrigues system and on the cyclic competition coefficients.

Targeted database searches for May–Leonard mean-skew, mean-ordering, logarithmic-balance, and the ratio \(c/e\) did not locate an equivalent statement. This search evidence is not a proof of bibliographic uniqueness.

## Limitations
The claim is a stationary or phase-locked-periodic balance law, not an existence theorem for periodic or chaotic attractors. It does not establish that the SRB measures constructed in the source are compactly supported away from the coordinate planes; applying the invariant-measure form to boundary-accumulating measures would require separate logarithmic-integrability and zero-log-drift justification. It also does not determine \(A\) from \(\gamma\) and \(\omega\) alone.

## References
1. A. A. P. Rodrigues, “Abundance of Strange Attractors Near an Attracting Periodically Perturbed Network,” arXiv:2010.05776v1 (2020); SIAM Journal on Applied Dynamical Systems 20 (2021), 541–570, doi:10.1137/20M1335510.
2. V. S. Afraimovich, S.-B. Hsu, and H. E. Lin, “Chaotic Behavior of Three Competing Species of May–Leonard Model under Small Periodic Perturbations,” International Journal of Bifurcation and Chaos 11 (2001), 435–447, doi:10.1142/S021812740100216X.
3. I. S. Labouriau and A. A. P. Rodrigues, “Bifurcations from an Attracting Heteroclinic Cycle under Periodic Forcing,” arXiv:1809.04006; Journal of Differential Equations 269 (2020), 4137–4174.
