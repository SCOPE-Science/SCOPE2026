# Sparse diagonal quartic stabilization of prescribed ecological coexistence

## Finding

Consider a population model whose intrinsic growth rates and all pairwise interactions are fixed, without restrictions on their signs. **Two additional own-density coefficients per species suffice to stabilize any prescribed positive coexistence state with any requested linear decay margin.** The coefficients can always be chosen with a positive own-density quadratic contribution and a negative own-density cubic contribution to per-capita growth. All trajectories starting in the nonnegative orthant are forward complete and ultimately bounded. Among interventions restricted to powers of each species' own density of degrees two and three, two nonzero coefficients per species are also necessary in the worst case.

More precisely, for every integer \(n\ge1\), \(r\in\mathbb R^n\), \(S\in\mathbb R^{n\times n}\), \(z\in(0,\infty)^n\), and \(\gamma>0\), there exist \(\alpha_i,\beta_i>0\) so that the system
\[
\dot x_i=x_i\left(r_i+\sum_{j=1}^n S_{ij}x_j+\alpha_i x_i^2-\beta_i x_i^3\right),\qquad 1\le i\le n,
\]
has equilibrium \(z\) and every eigenvalue \(\lambda\) of its Jacobian there satisfies \(\operatorname{Re}\lambda<-\gamma\). Every solution with \(x(0)\in[0,\infty)^n\) exists for all nonnegative time and eventually enters a single bounded box that depends only on the coefficients, not on the initial state.

## Assumptions and scope

The intervention is allowed to modify only the coefficients of \(x_i^2\) and \(x_i^3\) in the per-capita growth of species \(i\); it does not change the supplied intrinsic rate \(r_i\), any original pairwise interaction \(S_{ij}\), or any coefficient involving a density belonging to another species. The upper-order terms are thus **self-density nonlinearities**, not distinct-species higher-order interactions. The target \(z\) has all components strictly positive, and the stability margin \(\gamma\) is an arbitrary strictly positive real number. No sign or nonsingularity restrictions are imposed on \(S\).

For the worst-case support assertion, interventions are restricted to polynomial sums of \(x_i^2\) and \(x_i^3\), without cross-species monomials, for each species; a coefficient counts as nonzero support if it is not zero.

## Proof

**Constructive equilibrium and stability.** Define
\[
R_i=r_i+\sum_{j=1}^n S_{ij}z_j,\qquad H_i=z_i\sum_{j\ne i}|S_{ij}|.
\]
Choose independently, for each \(i\), any real \(\beta_i\) satisfying
\[
\beta_i>\max\left\{0,\frac{R_i}{z_i^3},\frac{z_iS_{ii}-2R_i+H_i+\gamma}{z_i^3}\right\},
\qquad \alpha_i=\beta_i z_i-\frac{R_i}{z_i^2}.
\]
Then \(\alpha_i>0\), \(\beta_i>0\), and
\[
R_i+\alpha_i z_i^2-\beta_i z_i^3=0,
\]
which proves that \(z\) is an equilibrium. As the per-capita factor vanishes at \(z\), the Jacobian \(J\) has entries
\[
J_{ij}=z_iS_{ij}\quad(i\ne j),\qquad
J_{ii}=z_iS_{ii}+2\alpha_i z_i^2-3\beta_i z_i^3
=z_iS_{ii}-2R_i-\beta_i z_i^3.
\]
Our choice implies
\[
J_{ii}+\sum_{j\ne i}|J_{ij}|=z_iS_{ii}-2R_i-\beta_i z_i^3+H_i<-\gamma.
\]
Every Gershgorin disc consequently lies in the open half-plane \(\operatorname{Re}\lambda<-\gamma\), establishing strict linear asymptotic stability with the asserted spectral margin. Standard linearization at a hyperbolic sink gives local exponential convergence to \(z\).

**Global forward existence and dissipativity.** Polynomial vector fields are locally Lipschitz. Coordinate hyperplanes are invariant, and uniqueness ensures the nonnegative orthant is forward invariant. Put
\[
B=\min_i\beta_i>0,\quad U=\max_i\alpha_i,\quad
R=\max_i|r_i|,\quad L=\max_i\sum_j|S_{ij}|.
\]
For \(M(t)=\max_i x_i(t)\), every maximizer \(i\) satisfies, as long as \(M>0\),
\[
\dot x_i\le M\bigl(R+LM+UM^2-BM^3\bigr).
\]
Select any \(K>\max\{1,4R/B,4L/B,4U/B\}\). For all \(M\ge K\), each of the first three terms inside the parentheses is smaller than \(BM^3/4\), hence the parentheses are at most \(-BM^3/4<0\). The upper right Dini derivative of \(M\) is therefore negative at and above \(K\); the box \([0,K]^n\) is forward invariant, and any larger nonnegative trajectory reaches it in finite time (while above \(K\), \(D^+M\le-(B/4)M^4\)). This uniformly bounds all forward trajectories and excludes finite-time blowup, so all are globally defined.

**Sharp diagonal support requirement.** To see necessity in the worst case, take \(r_i=-1\), \(S=0\), and prescribed \(z_i=1\) for every species. Because no cross-species terms are permitted, the dynamics are decoupled. For a given species, no added own-density monomial leaves per-capita growth \(-1\), so it cannot attain the equilibrium. With only one nonzero own-density monomial \(c_i x_i^{p}\), where \(p\in\{2,3\}\), the equilibrium equation forces \(c_i=1\). The corresponding Jacobian diagonal entry at \(z_i=1\) is \(p>0\), proving instability. Thus each species needs both monomials and any universal intervention in this restricted class requires at least \(2n\) nonzero additional coefficients. The constructive part uses exactly \(2n\), proving support optimality within this class.

## Verification

The standalone script `verify.py` uses exact rational arithmetic on 1,400 deterministic test systems across one to seven species. It checks the equilibrium equations, both formulas for the Jacobian diagonal, strict row-wise Gershgorin inequalities with the requested margin, positive signs of the two feedback coefficients, and a constructive absorbing-box bound. It also checks the scalar one-monomial obstructions at both admissible degrees. It reports `PASS: 1400 exact rational systems and both one-monomial obstructions`. These are reproducibility checks; the preceding proof establishes the infinite-parameter assertions analytically.

## Relationship to prior work

Çelik, Isoldi, Portakal, and Zucal (2026, Theorem 4.2) proved that arbitrary prescribed pairwise coefficients admit stable coexistence when unconstrained quadratic and cubic per-capita tensors are added. Their construction uses the total population \(\sum_i x_i\) and mixed-species monomials. The present result imposes a stronger, self-only coefficient pattern, proves its support optimality within the self-only intervention class, prescribes an arbitrary target abundance and stability margin, and establishes dissipativity. It does not claim novelty for the broader unconstrained higher-order existence result.

Cui and collaborators (2024 preprint) derived existence and stability conditions for tensor-based higher-order Lotka–Volterra systems under sign and dominance hypotheses. Their framework addresses a different coefficient class and does not supply a universal self-only intervention for arbitrary fixed signed pairwise matrices. Classical density-dependent damping and Gershgorin stability arguments are standard; the point here is their combined sharp universal sparse realization under the fixed-data constraints.

## Limitations

The result proves local exponential stability of the designated equilibrium and boundedness of all nonnegative trajectories, **not** global attraction to that equilibrium, uniqueness of positive equilibria, exclusion of boundary attractors, or robustness under arbitrarily large coefficient perturbations. The support lower bound is only for diagonal own-density interventions of per-capita degrees two and three; no global optimality among cross-species interventions or unrestricted polynomial degrees is asserted. The construction may require very large coefficients and does not impose empirical biological plausibility constraints.

## References

1. T. Ö. Çelik, V. A. Isoldi, İ. Portakal, and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1 (first public posting 2026-09-08), especially Theorem 4.2 and its proof, https://arxiv.org/abs/2609.09286.
2. S. Cui, Q. Zhao, G. Zhang, H. Jardón-Kojakhmetov, and M. Cao, *On the analysis of a higher-order Lotka–Volterra model: an application of S-tensors and the polynomial complementarity problem*, arXiv:2405.18333 (2024), especially Corollaries 3–6, Theorem 5, and Remark 7, https://arxiv.org/abs/2405.18333.
3. B. S. Goh, *Global Stability in Many-Species Systems*, The American Naturalist 111 (1977), 135–143, DOI:10.1086/283144 (related density-dependent stability conditions).
