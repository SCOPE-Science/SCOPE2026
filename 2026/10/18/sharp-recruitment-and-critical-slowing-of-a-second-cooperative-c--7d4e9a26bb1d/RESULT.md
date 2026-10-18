# Sharp recruitment and critical slowing of a second cooperative contagion group

## Finding

A locally persistent cooperative epidemic in one three-member group can support infection in an overlapping second group whose isolated three-member dynamics would admit no positive equilibrium. In a five-coordinate deterministic mean-field SIS model with two triangles sharing exactly one node, the **exact local recruitment threshold** is
\[
\beta_{\mathrm{rec}}(\alpha)=\frac{2}{1+\sqrt{1-4/\alpha}},\qquad \alpha>4.
\]
The equilibrium localized in the first group is exponentially stable for \(0<\beta<\beta_{\mathrm{rec}}\), has a simple center eigenvalue at equality, and has exactly one unstable eigenvalue for \(\beta>\beta_{\mathrm{rec}}\). Immediately above this threshold, a unique nearby positive coexistence equilibrium is exponentially stable. If \(u=(1+\sqrt{1-4/\alpha})/2\), its second-group prevalence is \(u(\beta-\beta_{\mathrm{rec}})+O((\beta-\beta_{\mathrm{rec}})^2)\).

At equality, let
\[
\Delta=\frac{(2u-1)(2-u)}{(1-u)^2}>0.
\]
For every sufficiently nearby physical initial state with a nonzero infection in the second group, the five-coordinate trajectory converges to the localized equilibrium and satisfies
\[
\lim_{t\to\infty}t b_j(t)=1\quad(j=1,2),\qquad
\lim_{t\to\infty}t^2(c(t)-u)=\frac1\Delta,\qquad
\lim_{t\to\infty}t^2(a_j(t)-u)=\frac{1-u}{u\Delta}\quad(j=1,2).
\]
In particular, \(\alpha=9/2\) gives \(u=2/3\), the exact recruitment threshold \(\beta_{\mathrm{rec}}=3/2\), and the critical corrections \(1/4\) at the shared node and \(1/8\) at either first-group peripheral node.

There is also a structural ordering statement for any finite sunflower of such triple groups: at a stationary state with hub prevalence \(c>0\), every nonempty peripheral pair of transmission strength \(\lambda\) has equal prevalence \(1-1/(\lambda c)\), hence requires \(\lambda c>1\). Every absent pair has two transverse eigenvalues \(-1\pm\lambda c\). Consequently, at any hyperbolically stable stationary state, the active groups must include every group stronger than an active group. This necessity does not assert existence or stability for all such supports.

## Assumptions and scope

Let \(c,a_1,a_2,b_1,b_2\in[0,1]\) denote deterministic infection-prevalence coordinates (not binary infection states). The two triples are \(\{c,a_1,a_2\}\) and \(\{c,b_1,b_2\}\). Each infected vertex recovers at rate one. A susceptible vertex is infected through a triple at rate \(\alpha\) or \(\beta\), respectively, conditional on both other vertices in that triple being infected; closure replaces pair probabilities by products of their prevalence coordinates. There is **no dyadic infection channel**. The defining polynomial ordinary differential equations are
\[
\begin{aligned}
\dot c&=-c+(1-c)(\alpha a_1a_2+\beta b_1b_2),\\
\dot a_1&=-a_1+\alpha(1-a_1)ca_2,\\
\dot a_2&=-a_2+\alpha(1-a_2)ca_1,\\
\dot b_1&=-b_1+\beta(1-b_1)cb_2,\\
\dot b_2&=-b_2+\beta(1-b_2)cb_1.
\end{aligned}
\]
All conclusions are for positive finite \(\alpha,\beta\), specifically \(\alpha>4\) in the recruitment theorem; critical asymptotics concern an open relative neighborhood of the first-group endemic state inside the physical cube, with \(b_1(0)+b_2(0)>0\). The process is the explicitly declared **deterministic mean-field ODE**, not an exact stochastic finite-population SIS process. The cube is forward invariant because vector fields point inward at zero and one.

## Proof

**Symmetry and support of equilibria.** Subtracting paired peripheral equations gives the exact identities
\[
\frac{d}{dt}(a_1-a_2)=-(1+\alpha c)(a_1-a_2),\qquad
\frac{d}{dt}(b_1-b_2)=-(1+\beta c)(b_1-b_2).
\]
Hence all stationary peripheral pairs have equal coordinates; a nonzero pair must satisfy \(a=1-1/(\alpha c)\) or \(b=1-1/(\beta c)\). At a stationary state with an absent pair \(b_1=b_2=0\), its linear block is \(\bigl(\begin{smallmatrix}-1&\beta c\\\beta c&-1\end{smallmatrix}\bigr)\), with eigenvalues \(-1\pm\beta c\). The identical calculation for any number of petals proves the ordering assertion (strict hyperbolic stability prohibits both a positive or zero transverse eigenvalue for any absent petal).

**Localized equilibrium.** On \(b_1=b_2=0\), the endemic state satisfying \(c=a_1=a_2=u\) obeys \(\alpha u(1-u)=1\). For \(\alpha>4\), its upper root \(u\in(1/2,1)\) has a stable first-group Jacobian. In the coordinates \((c,a)\), with \(a=(a_1+a_2)/2\), the symmetric linearization is
\[
J_A=\begin{pmatrix}-1/(1-u)&2\\1&-u/(1-u)\end{pmatrix},
\quad \operatorname{tr}J_A=-\frac{1+u}{1-u}<0,
\quad\det J_A=\Delta>0.
\]
The antisymmetric first-group eigenvalue equals \(-1-\alpha u<0\). The second-group eigenvalues equal \(-1\pm\beta u\); the exact local stability transition occurs at \(\beta u=1\). Above it there is exactly one unstable eigenvalue, since all first-group eigenvalues remain strictly negative at the localized equilibrium.

**Local coexistence branch.** For a nearby equilibrium, symmetry forces \(a_1=a_2=a\), \(b_1=b_2=b\). The first two equilibrium equations solve uniquely for \(c,a\) as smooth functions of \((b,\beta)\) near \((b,\beta)=(0,1/u)\), since \(J_A\) is invertible. Their first derivatives in \(b\) vanish, as the second group enters the center equation through \(\beta b^2\). Thus \(c=u+O(b^2)\), \(a=u+O(b^2)\). For \(b>0\) the final equilibrium equation divides by \(b\), giving \(\beta c(1-b)=1\). Its derivative with respect to \(b\) at the threshold is \(-1\), while its derivative with respect to \(\beta\) is \(u\). The implicit-function theorem gives one and only one nearby nonzero branch with
\[
b=u(\beta-1/u)+O((\beta-1/u)^2).
\]
It is physically positive exactly on the \(\beta>1/u\) side sufficiently close to threshold. The simple zero eigenvalue on this branch moves to \(-u(\beta-1/u)+O((\beta-1/u)^2)\); the other eigenvalues remain in the negative half-plane. This proves its local exponential stability and the transcritical exchange. The branch is not asserted to remain stable for arbitrary larger \(\beta\).

**Critical slowing.** At \(\beta=1/u\), the stable three-dimensional first-group subsystem and the stable antisymmetric second-group direction leave one center direction \(b=(b_1+b_2)/2\). A smooth local center manifold has
\[
c=u+q_c b^2+O(b^3),\qquad a_j=u+q_a b^2+O(b^3),
\]
where invariance at quadratic order gives
\[
J_A\begin{pmatrix}q_c\\q_a\end{pmatrix}+
\begin{pmatrix}(1-u)/u\\0\end{pmatrix}=0,
\quad q_c=\frac1\Delta,
\quad q_a=\frac{1-u}{u\Delta}.
\]
Along the center manifold, the remaining equation is
\[
\dot b=b[\beta c(1-b)-1]=-b^2+O(b^3).
\]
Every sufficiently nearby physical trajectory with \(b_1(0)+b_2(0)>0\) approaches this center manifold exponentially fast along its stable fibers and its positive center coordinate satisfies \(b(t)\to0\) with \(t b(t)\to1\). The pair differences decay exponentially by the exact identities above. Substituting \(b(t)\sim1/t\) in the center-manifold expressions, with exponentially small stable-fiber deviations, gives all stated \(t\)- and \(t^2\)-limits. The local physical basin can be chosen forward-invariant on the center-attracting side; trajectories with \(b_1=b_2=0\) are explicitly excluded from the nontrivial asymptotic claim.

## Verification

Execute `python check.py` with Python, SymPy, NumPy and SciPy. The checker independently differentiates the five polynomial equations, evaluates the characteristic polynomial at the exact rational threshold, verifies the quadratic center-manifold coefficients exactly, checks equilibrium and invasion identities for rational parameter families, and performs numerical local-branch and critical-trajectory diagnostics. Symbolic identities and the analytic center-manifold argument, not finite integration, establish the infinite-time limits.

## Relationship to prior work

St-Onge et al., *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, introduce general nonlinear group contagion, analyze phase transitions and mesoscopic localization using approximate master equations for random hypergraph ensembles, and distinguish influential groups from individual hubs [1]. Their ensemble-based framework does not state the exact local recruitment and critical relaxation coefficients for this fixed two-triangle deterministic cubic closure. The present equations are explicitly a particular mean-field closure; they are not the stochastic group master equations in [1].

Cisneros-Velarde and Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions* [2], treat continuous-time simplicial SIS with general matrix/tensor infection and prove sufficient conditions for bistability and endemic behavior. Their Theorem 5.1 assumes an **irreducible nonnegative pairwise matrix**, whereas this all-triple model has the pairwise matrix identically zero. In particular their sufficient conditions neither apply to its localized boundary equilibrium nor imply this exact center-manifold bifurcation or its physical critical amplitudes. 

Cui et al., *General SIS diffusion process with indirect spreading pathways on a hypergraph* [3], give a broader direct/indirect hypergraph system and endemic-stability sufficient conditions. Their abstract, model and Theorems 4.3–4.7 describe different positive/irreducible mechanisms; they do not provide a sharp threshold or critical coefficients for the two-triangle zero-dyadic pure-conjunctive flow.

Liang et al., *Discrete-time SIS Social Contagion Processes on Hypergraphs* [4], investigate a tensor-based discrete-time mean-field system with sufficient stability and domain-of-attraction conditions [4]. Their model and main propositions/theorems do not supply a sharp continuous-time two-triangle recruitment threshold or the critical coordinate asymptotics of this finding. The finite-hypergraph model and some background estimates overlap conceptually; no general priority claim for higher-order epidemic thresholds is made.

## Limitations

The result concerns a specific higher-order **mean-field** epidemic model, and does not transfer automatically to the exact five-person continuous-time stochastic Markov chain (which has an absorbing all-susceptible state). The recruitment classification is **local** to the upper isolated endemic equilibrium, not a global census of all stationary states or their basins. The bifurcating coexistence equilibrium is proved stable only sufficiently close above threshold. Critical algebraic limits require a sufficiently close initial state and a nonempty initially infected second group. Equivalence to another unindexed deterministic local-bifurcation derivation remains an originality risk. No independent audit has been conducted.

## References

[1] G. St-Onge, I. Iacopini, V. Latora, A. Barrat, G. Petri, A. Allard, L. Hébert-Dufresne, *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, Communications Physics **5**, 25 (2022), DOI: 10.1038/s42005-021-00788-w; first public arXiv version `arxiv:2105.07092v1`, 2021-05-14. Open-access full text: https://nul.repository.guildhe.ac.uk/id/eprint/1078/1/s42005-021-00788-w.pdf.

[2] P. Cisneros-Velarde and F. Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, arXiv `arxiv:2005.11404v1`, first public 2020-05-22; later IEEE Transactions on Control of Network Systems **9** (2022), 695–705. Full text: https://arxiv.org/pdf/2005.11404.

[3] S. Cui, F. Liu, H. Jardón-Kojakhmetov and M. Cao, *General SIS diffusion process with indirect spreading pathways on a hypergraph*, arXiv `arxiv:2306.00619v1` (2023). Full text: https://arxiv.org/pdf/2306.00619.

[4] L. Liang, S. Cui and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv `arxiv:2408.08602v1` (2024); full text: https://www.researchgate.net/publication/383216926_Discrete-time_SIS_Social_Contagion_Processes_on_Hypergraphs.
