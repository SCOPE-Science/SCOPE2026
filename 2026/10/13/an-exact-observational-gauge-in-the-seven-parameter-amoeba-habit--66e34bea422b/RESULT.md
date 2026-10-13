# An exact observational gauge in the seven-parameter amoeba habituation model
## Finding
The two-compartment pressure model for \(\textit{Physarum polycephalum}\) habituation of Nishi, Tero, Nishigami and Nakagaki contains a continuous *observational equivalence* after the authors have normalized the rear generation rate to one. Consequently the seven parameters used to fit bridge-crossing observations cannot be separately identified from any amount of exact tip-position data, regardless of the switching schedule.

In the authors' seven-parameter normalization \(g_{\rm r}=1\), for every \(0<c<1\) the transformed parameters
\[
\widehat g_{\rm f}=cg_{\rm f}+1-c,\quad
\widehat g_{\rm f}^{\rm s}=cg_{\rm f}^{\rm s}+\frac{a_{\rm s}}a(1-c),\quad
\widehat\gamma=\frac\gamma c
\]
with \(a,a_{\rm s},d,r\) unchanged predict *exactly the same behavior* as the originals. The pressure states change by a simultaneous affine transformation, but the measured velocity does not. This is an unavoidable structural ambiguity under the observation scheme actually used in the paper, not a numerical near-degeneracy.

For the published supplementary seed-308 fit,
\[
(g_{\rm f},g_{\rm f}^{\rm s},a,a_{\rm s},d,\gamma,r)
=(0.001001,11.97,0.02244,0.2866,0.4909,0.005782,0.07088),
\]
choosing \(c=0.9\) produces the distinct fit
\[
(\widehat g_{\rm f},\widehat g_{\rm f}^{\rm s},\widehat\gamma)
=(0.1009009,12.050183601\ldots,0.006424444\ldots),
\]
all within the authors' reported optimization bounds. This changes the inferred unperturbed front generation rate more than one hundredfold without changing any model-predicted crossing time.

## Assumptions and scope
The parameters \(a,a_{\rm s},d,r,\gamma,g_{\rm f},g_{\rm f}^{\rm s}\) are positive, with normalized rear generation \(g_{\rm r}=1\). The input \(h(t)\in[0,1]\) is piecewise continuous; the study's binary quinine-stimulation protocol is the special case \(h(t)\in\{0,1\}\). The observed output is the modeled tip position \(\ell(t)\), its derivative, or a crossing time defined by a given tip position reaching a fixed bridge length. Initial pressure states must be transformed consistently. In particular, the published initialization at the unstimulated equilibrium satisfies this requirement automatically.

For compact notation write
\[
a_h=(1-h)a+ha_{\rm s},\qquad
g_h=(1-h)g_{\rm f}+hg_{\rm f}^{\rm s}.
\]
The model (the source's Eqs. (1)–(5)) then is
\[
\begin{aligned}
\dot p_{\rm f}&=d(p_{\rm r}-p_{\rm f})-a_h p_{\rm f}+g_h,\\
\dot p_{\rm r}&=rd(p_{\rm f}-p_{\rm r})-ap_{\rm r}+1,\\
\dot\ell&=\gamma(p_{\rm r}-p_{\rm f}).
\end{aligned}
\]

## Proof
Fix \(c\in(0,1)\), and define \(b=(1-c)/a\). Let both unobserved pressure variables change by
\[
\widehat p_{\rm f}=cp_{\rm f}+b,\qquad
\widehat p_{\rm r}=cp_{\rm r}+b.
\]
The rear reaction term transforms exactly, because
\[
-a\widehat p_{\rm r}+1
=-acp_{\rm r}-ab+1
=c(-ap_{\rm r}+1)
\]
and \(ab=1-c\). The diffusion terms transform by a factor \(c\) because they contain only differences. For the front reaction, the transformed source is
\[
\begin{aligned}
\widehat g_h
&=(1-h)(cg_{\rm f}+ab)+h(cg_{\rm f}^{\rm s}+a_{\rm s}b)\\
&=cg_h+a_hb.
\end{aligned}
\]
Therefore
\[
-a_h\widehat p_{\rm f}+\widehat g_h
=c(-a_hp_{\rm f}+g_h).
\]
The transformed pair satisfies both pressure equations for every admissible forcing schedule. All new generation rates are strictly positive because \(c\in(0,1)\) and the original parameters are positive. Positive pressure states remain positive, too.

The output identity is pointwise:
\[
\widehat\gamma(\widehat p_{\rm r}-\widehat p_{\rm f})
=\frac\gamma c\,c(p_{\rm r}-p_{\rm f})
=\gamma(p_{\rm r}-p_{\rm f}).
\]
Matching initial tip position yields \(\widehat\ell(t)=\ell(t)\) by integration. Hence every defined first-passage time of \(\ell\) to any bridge threshold is also the same. Resetting both tip-position variables to zero at the start of each day leaves the identity intact. Linear stability and uniqueness of the unstimulated equilibrium follow from the negative trace and positive determinant of the strictly dissipative two-by-two pressure matrix. Because the transformation carries the entire equilibrium equation to the new one, the required equilibrium initial states are mapped to one another automatically.

The same identity can be exhibited without latent gauge states. Set
\[
\begin{aligned}
x&=\gamma\left(p_{\rm f}-\frac1a\right),&
y&=\gamma\left(p_{\rm r}-\frac1a\right),\\
\kappa_0&=\gamma(g_{\rm f}-1),&
\kappa_1&=\gamma\left(g_{\rm f}^{\rm s}-\frac{a_{\rm s}}a\right).
\end{aligned}
\]
Direct substitution yields the exact observable normal form
\[
\begin{aligned}
\dot x&=d(y-x)-a_hx+(1-h)\kappa_0+h\kappa_1,\\
\dot y&=rd(x-y)-ay,\\
\dot\ell&=y-x.
\end{aligned}
\]
Only \((a,a_{\rm s},d,r,\kappa_0,\kappa_1)\) occur. The affine parameter transformation preserves both \(\kappa_0\) and \(\kappa_1\), so even arbitrarily rich noise-free motion data cannot select a unique original triple \((g_{\rm f},g_{\rm f}^{\rm s},\gamma)\). No assertion is made that the six reduced combinations can all be individually identified.

For any differentiable observation map formed from trajectory samples, the tangent to this observationally constant curve at \(c=1\) is
\[
\left(g_{\rm f}-1,\;g_{\rm f}^{\rm s}-a_{\rm s}/a,\;0,\;0,\;0,\;-\gamma,\;0\right).
\]
It is nonzero because \(\gamma>0\); thus the sensitivity matrix annihilates this vector, and any ordinary positive-weight sensitivity Fisher information is singular. This tangent statement does not require an assumption that the other six directions are identifiable.

## Verification
The standalone script `verification/verify.py` uses SymPy to check both full pressure-ODE conjugacy identities and their observable normal form symbolically for unrestricted symbolic parameters and stimulus indicator. It verifies preservation of the no-stimulation and stimulation equilibria, the exact null tangent, and all exact-rational transformed seed-308 coefficients. It also propagates a representative nine-day switched-input schedule using matrix exponentials to confirm the implementation-level trajectory equality. The symbolic equalities—not the finite switched experiment—prove the universal claim.

The exact published parameter values, interpreted as terminating decimals, give for \(c=9/10\):
\[
\widehat g_{\rm f}=\frac{1009009}{10^7},\qquad
\widehat g_{\rm f}^{\rm s}=\frac{6760153}{561000},\qquad
\widehat\gamma=\frac{2891}{450000}.
\]
The published Table S3 bounds include all these values and the source values. The second transformed triple is not an independent empirical fit: it is a mathematically equivalent parameterization of the same fitted trajectories.

## Relationship to prior work
General structural-identifiability theory recognizes that continuous symmetries of a state-space model can produce indistinguishable outputs; see Villaverde (2019) and Massonis, Banga, and Villaverde (2023). Their statements are methodological prior art, not claims about this particular \(\textit{Physarum}\) pressure model. The source's supplementary resource fixes \(g_{\rm r}=1\) and fits seven remaining parameters, reporting sensitivity under separate one-parameter perturbations. That scaling normalization does not remove the *additional affine gauge* exhibited here. A one-at-a-time sensitivity analysis can display large nonzero responses in each coordinate while missing a simultaneous exact null direction.

No equivalent published correction for this source or these exact seven parameters was found in the checked primary and indexed literature. Lack of a search hit alone is not proof of global novelty; the conclusion is bounded by the direct primary-source comparison and the listed residual literature-access risks.

## Limitations
The non-identifiability statement is for locomotion-derived output without independent calibrated absolute-pressure measurements. Additional observations, for example of an absolute pressure channel, can break the exhibited symmetry; whether a particular augmented observation design identifies every parameter is not analyzed.

The theorem does not assert that the model is physiologically false, that the fit does not predict behavior, or that the reduced six parameters are all globally identifiable. It also does not show identifiability among models with different functional equations. It is a source-specific mathematical observation about fitting individual mechanistic rates from movement alone.

## References
1. K. Nishi, A. Tero, Y. Nishigami, and T. Nakagaki, “Mathematical modeling for a primitive form of habituation in an amoeba,” bioRxiv preprint, first version publicly posted September 18, 2025, DOI: 10.1101/2025.09.15.675989; \(\textit{Journal of Mathematical Biology}\) 93, article 36 (2026), DOI: 10.1007/s00285-026-02438-7.
2. Nishi et al., Supplementary Information / Online Resource 1 for DOI: 10.1007/s00285-026-02438-7, Tables S3–S4 and normalization S1.1.
3. A. F. Villaverde, “Observability and Structural Identifiability of Nonlinear Biological Systems,” \(\textit{Complexity}\) (2019), DOI: 10.1155/2019/8497093.
4. G. Massonis, J. R. Banga, and A. F. Villaverde, “AutoRepar: A method to obtain identifiable and observable reparameterizations of dynamic models with mechanistic insights,” \(\textit{International Journal of Robust and Nonlinear Control}\) (2023), DOI: 10.1002/rnc.5887.
