# Generic single-trajectory recovery and an exact hidden-interaction leaf in triadic ecological dynamics

## Finding

Consider an ecological community of \(n\ge3\) species with *hard* triadic interactions: in the per-capita growth equation for species \(i\), each quadratic interaction contains two distinct species, neither of which is \(i\). The model is
\[
\dot x_i=x_i F_i(x),\qquad
F_i(x)=r_i+\sum_{j=1}^{n}a_{ij}x_j+
\sum_{\substack{1\le j<k\le n\\j,k\ne i}}b_{ijk}x_jx_k.
\]
All coefficients are arbitrary real numbers, and the initial abundance vector is strictly positive. Write
\[
p_n=1+n+\binom{n-1}{2}.
\]

**Exact single-trajectory criterion.** On any positive nonempty open observation-time interval, complete noiseless knowledge of all abundances and their time derivatives determines *every* coefficient uniquely among systems of the displayed form if and only if, for each species \(i\), no nonzero polynomial of the form
\[
P_i(x)=c_i+\sum_j d_{ij}x_j+
\sum_{\substack{j<k\\j,k\ne i}}e_{ijk}x_jx_k
\]
vanishes at every abundance vector visited by the observed trajectory.

**Generic finite sampling.** For every fixed strictly positive initial state, there is a nonzero polynomial in the model coefficients whose nonvanishing guarantees that a single unperturbed trajectory uniquely determines all coefficients from the abundances and instantaneous per-capita growth rates at exactly \(p_n\) sufficiently close, distinct observation times. Its nonzero set is Zariski-open and Euclidean dense. In particular, this conclusion holds for generic systems with genuinely nonzero hard triadic coefficients, not merely for pairwise systems. The required genericity does not assume stable, periodic, or bounded long-term dynamics: only a short positive solution interval is used.

**Exact exception.** Already with three strictly positive species, a nonstationary, globally bounded trajectory of a system with a nonzero hard triadic coefficient may agree *exactly at every time* with a trajectory of a purely pairwise system having different intrinsic growth rates. Thus generic structural recovery and genuine orbitwise non-identifiability both occur within this same natural model class.

## Assumptions and scope

The integer \(n\ge3\) is finite. The system is autonomous, all species are observed, derivatives are known exactly, the polynomial support indicated above is known, and the data come from one initial state \(x(0)\in(0,\infty)^n\). Coefficients are real and unconstrained unless they belong to an open sign-constrained subdomain. Existence is asserted only on a sufficiently short interval for the generic recovery theorem. By continuity and the multiplicative population equations, all coordinates remain positive on that interval. The exact criterion applies on any open interval of positive existence.

For each row \(i\), define the \(p_n\)-dimensional vector space
\[
\mathcal V_i=\operatorname{span}\bigl\{1,x_1,\ldots,x_n,
 x_jx_k:1\le j<k\le n,\ j,k\ne i\bigr\}.
\]
The supports are linearly independent as multivariate polynomials. Let \(\phi_{i1},\ldots,\phi_{ip_n}\) be the displayed monomial basis in any fixed order. A solution \(x(t)\) is **informative for row \(i\)** on \(I\) if the functions \(t\mapsto\phi_{i\ell}(x(t))\) are linearly independent over the real constants on \(I\). This is an exact structural condition, not a numerical tolerance.

## Proof

**1. Exact orbit criterion.** Because all coordinates are positive, the complete trajectory supplies
\[
g_i(t)=\dot x_i(t)/x_i(t)=F_i(x(t)).
\]
If the evaluation functions of row \(i\) are independent, these equalities have at most one coefficient vector. If every row is informative, every coefficient is uniquely determined. Conversely, suppose a nonzero \(P_i\in\mathcal V_i\) vanishes everywhere on the observed orbit. Replace only \(F_i\) by \(F_i+\eta P_i\), for a fixed \(\eta\ne0\), and leave the other per-capita rates unchanged. The observed \(x(t)\) solves the changed system as well because \(P_i(x(t))=0\). Local uniqueness for the polynomial ODE makes it the same solution from the same initial state. The coefficient vectors differ. This proves the exact equivalence, including non-identifiability rather than just a failed matrix computation.

**2. A finite polynomial jet that is generically nonsingular.** Let \(\mathcal L_\theta\) denote Lie differentiation along the polynomial vector field \(x_iF_i(x)\), with \(\theta\) the array of all its coefficients. For each \(i\), form the square matrix
\[
W_i(\theta,x^0)_{k\ell}=
 \bigl(\mathcal L_\theta^{\,k-1}\phi_{i\ell}\bigr)(x^0),
\qquad 1\le k,\ell\le p_n.
\]
Every entry is polynomial in \(\theta\) and \(x^0\), hence so is \(\det W_i\). Consider the explicit uncoupled reference system
\[
\dot x_j=2^{j-1}x_j,
\qquad x_j(t)=x_j^0e^{2^{j-1}t}.
\]
For a monomial basis element, its value along this solution is a nonzero positive constant times \(e^{\mu t}\), with \(\mu\) taken from
\[
E_i=\{0\}\cup\{2^{j-1}:1\le j\le n\}
\cup\{2^{j-1}+2^{k-1}:j<k,\ j,k\ne i\}.
\]
These \(p_n\) exponents are pairwise distinct by uniqueness of binary expansions into one or two distinct powers of two. After factoring the nonzero initial-state monomial values from columns, \(W_i\) is a classical Vandermonde matrix on \(E_i\); its determinant is
\[
\left(\prod_{\ell=1}^{p_n}\phi_{i\ell}(x^0)\right)
\prod_{u<v}(\mu_v-\mu_u)\ne0,
\]
where the exponents are ordered increasingly. This holds simultaneously for every \(i\) and every \(x^0>0\). Thus
\[
\mathcal P(\theta,x^0)=\prod_{i=1}^n\det W_i(\theta,x^0)
\]
is a nonzero polynomial, and for each fixed \(x^0>0\), \(\mathcal P(\cdot,x^0)\) is not identically zero. Its nonvanishing set is Zariski open and Euclidean dense in coefficient space, and intersects every nonempty open region of coefficients (including open sign-constrained regions). Since it is open, systems with *all* allowable hard triadic coefficients nonzero also occur in it.

**3. From the jet to exactly \(p_n\) physical-time samples.** Put \(f_{i\ell}(t)=\phi_{i\ell}(x(t))\). They are analytic locally because the ODE is polynomial. For the predetermined distinct time multipliers \(s_q=q\), \(1\le q\le p_n\), Taylor expansion gives
\[
\det[f_{i\ell}(\delta s_q)]_{q,\ell=1}^{p_n}
=\frac{\det W_i}{\prod_{k=0}^{p_n-1}k!}
\left(\prod_{q<r}(s_r-s_q)\right)
\delta^{p_n(p_n-1)/2}+o\bigl(\delta^{p_n(p_n-1)/2}\bigr).
\]
When \(\mathcal P\ne0\), every row's sample determinant is therefore nonzero for all sufficiently small positive \(\delta\), and a single choice of \(\delta\) works for the finitely many species. The linear systems
\[
(\phi_{i\ell}(x(\delta s_q)))_{q,\ell}
\,(r_i,a_{i1},\ldots,b_{ijk})^{\mathsf T}
=(g_i(\delta s_q))_q
\]
recover every row exactly. The coefficient vector on the left is understood in the same monomial-basis order, with the relevant \(b_{ijk}\) entries only. This is an identification theorem with a finite observation budget, not just asymptotic inference. With fewer than \(p_n\) independent instantaneous per-capita measurements in a row, unconstrained *row-wise linear regression* is underdetermined; this elementary statement is not extended to arbitrary additional temporal constraints.

**4. A genuine positive orbit on which triadic interactions are exactly hidden.** For \(n=3\), let the first two per-capita growth rates of *both* models be
\[
F_1=1-x_1+x_2,\qquad F_2=-1+x_1-x_2.
\]
Then \(d(x_1x_2)/dt=x_1x_2(F_1+F_2)=0\) for every solution. Start at \(x^0=(1,1,1)\), so \(x_1(t)x_2(t)=1\) forever. Compare two third-species rates:
\[
F_3^{\mathrm{HO}}=1-x_3+x_1x_2,
\qquad F_3^{\mathrm{pair}}=2-x_3.
\]
The first model has a genuine hard coefficient \(b_{312}=1\) and intrinsic growth \(r_3=1\); the second has \(b_{312}=0\) and \(r_3=2\). On the invariant leaf their vector fields agree, so both generate exactly the same full state history from \(x^0\). It is not a stationary or extinct-species artifact: initially \(\dot x(0)=(1,-1,1)\), and along the leaf
\[
\dot x_1=1+x_1-x_1^2,
\quad x_2=1/x_1,\quad
\dot x_3=x_3(2-x_3).
\]
Consequently \(1\le x_1(t)<(1+\sqrt5)/2\), \(x_2(t)>0\), and \(1\le x_3(t)<2\) for all finite positive times, with convergence to positive limits. The polynomial \(x_1x_2-1\in\mathcal V_3\) supplies the exact rank defect.

## Verification

The accompanying `verify.py` uses integer/rational determinant elimination to check every relevant uncoupled Wronskian for \(n=3,4,5,6\), comparing it to the independent exponent-difference product. It also constructs a strictly nonzero hard-triad model with \(n=3\), all three hard coefficients \(1/20\), and growth rates \((1,2,4)\); direct symbolic Lie differentiation gives nonzero row-Wronskian determinants \(635235089283/40000000\), \(249627126483/40000000\), and \(50137324083/40000000\). Finally it verifies the exact product first integral and the vector-field difference in the non-identifiable example. All executed checks passed. Finite checks are illustrations: the arbitrary-\(n\) conclusions follow from the proof.

## Relationship to prior work

Calleja-Solanas et al. (2026) demonstrate that higher-order ecological interactions can be difficult to distinguish from effective pairwise descriptions using observed attractor time series; their main-text methods, results and discussion are not an exact generic full-parameter identification theorem for hard triadic Lotka–Volterra flows. Malizia et al. (2024) describe general equation-of-motion regression to reconstruct higher-order network couplings, explicitly noting that identifiability depends on sampled trajectories; they do not provide the displayed model-specific nonvanishing polynomial and its all-\(n\) single-trajectory consequence. Brunton, Proctor and Kutz (2016) provide the general polynomial-library regression methodology rather than an ecological-specific generic jet-rank proof. Duan, Rubin and Swigon (2022) study single-trajectory parameter identification in primarily planar Lotka–Volterra systems with discrete state observations, not hard triadic coefficients or the exact criterion above. Tahmasebi and Weber (2026) analyze symmetry-assisted single-trajectory identification, principally in structured discrete-time systems, not this model's generic continuous-time ecological rank guarantee.

The elementary regression and Vandermonde ingredients are not claimed to be new. The proposed contribution is the combined exact full-parameter orbitwise dichotomy, the explicit all-dimension generic finite-jet guarantee without external excitation in the hard-triad ecological class, and the global strictly positive nonstationary blindness example. Stronger general identifiability theorems outside the inspected literature remain a possible historical-priority risk.

## Limitations

Measurements of the complete state and its exact instantaneous derivatives are assumed; the theorem gives no error/noise bounds or numerical conditioning guarantee. The Vandermonde witness uses exponentially separated rates and is not presented as an experimentally practical design. A generically nonsingular formal jet can be arbitrarily ill-conditioned at small sampling intervals, consistent with practical near-nonidentifiability. Genericity is in coefficient space for each fixed positive initial state, not a claim that every ecologically restricted manifold or invariant attractor is informative. Observation only on an equilibrium or on certain invariant algebraic leaves may cause non-identifiability. No global recovery is asserted from finitely many *state-only* snapshots without derivative information, or under unknown functional support, hidden species, model error or finite precision. The exceptional example is an exact mathematical identifiability obstruction, not a claim that every data set is ambiguous.

## References

1. V. Calleja-Solanas, S. Lamata-Otín, C. Gómez-Ambrosi, J. Gómez-Gardeñes, S. Meloni, *Higher-order interactions in ecology can be hidden in plain sight*, arXiv:2605.06301, first public 2026-05-07. https://arxiv.org/abs/2605.06301
2. F. Malizia, A. Corso, L. V. Gambuzza, G. Russo, V. Latora, M. Frasca, *Reconstructing higher-order interactions in coupled dynamical systems*, Nature Communications 15, 5184 (2024), DOI:10.1038/s41467-024-49278-x. https://www.nature.com/articles/s41467-024-49278-x
3. S. L. Brunton, J. L. Proctor, J. N. Kutz, *Discovering governing equations from data by sparse identification of nonlinear dynamical systems*, PNAS 113 (2016), 3932–3937, DOI:10.1073/pnas.1517384113. https://www.pnas.org/doi/10.1073/pnas.1517384113
4. X. Duan, J. E. Rubin, D. Swigon, *Parameter identification from single trajectory data: from linear to nonlinear*, arXiv:2209.14191 (2022). https://arxiv.org/html/2209.14191v1
5. B. Tahmasebi, M. Weber, *Adaptive Symmetry Discovery for Dynamical System Identification*, arXiv:2608.08091 (2026). https://arxiv.org/abs/2608.08091
