# Same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and scientifically useful. This is not independent validation or peer review.

Same-model review: passed. Independent audit: not yet performed.

## Correctness audit

1. **Source equations and stated gap.** The full text of Cherniha–Kriukova was inspected at the porous reaction-diffusion equations, the two-positive-node construction, the concrete prey-predator system (58), and the paragraph explicitly leaving nonconstant zero-Neumann steady states beyond the paper's scope.
2. **Stationary proportionality is exact.** Under \(h_2=\alpha^2h_1\) and \(\alpha a_2+c_2=\alpha^2(a_1+\alpha c_1)\), substitution \(V=\alpha U\) makes the second stationary residual exactly \(\alpha^2\) times the first. The source paper's proportional-equilibrium constraints imply these identities.
3. **Positive periodic spatial dynamics.** Writing \(p=UU_x\) gives a two-dimensional conservative spatial system with first integral \(p^2/2-F(U)\). The lower positive reaction root is a center and the upper root a saddle. When \(U_->U_+/2\), the saddle-energy loop has a strictly positive left turning point, yielding a positive period annulus.
4. **Domain-length conclusion.** The half-period tends to \(L_c=\pi\sqrt{U_-/[b(U_+-U_-)]}\) at the center and diverges at the saddle loop. Continuity therefore gives a Neumann half-wave for every \(L>L_c\), and concatenating half-waves gives the stated multiplicity lower bound.
5. **Concrete example checked exactly.** For system (58), \(V=3U\) reduces the stationary PDE to \((UU_x)_x-3(U-1/2)(U-2/3)=0\). The first integral factors at saddle energy with positive lower turning point \((1+\sqrt7)/9\), and \(L_c=\pi\).
6. **Dispersion calculation.** Direct determinants of \(J-\mu D\) at the two homogeneous equilibria give \(3(\mu-1)^2/4\) and \((4\mu+3)^2/12\), respectively. Their traces are strictly negative for \(\mu\ge0\), so the lower equilibrium has an isolated neutral mode rather than an open Turing-unstable band.
7. **Local branch direction.** The variable \(q=U^2/2\) converts the scalar stationary equation near \(U=1/2\) to \(y_{xx}+y-14y^2+56y^3+O(y^4)=0\). The Poincare-Lindstedt period coefficient \(5a^2/12-3b_3/8\) equals \(182/3>0\), so the small-amplitude branch lies on the \(L>\pi\) side.

## Originality audit

### Existing SCOPE records

The current SCOPE archive was searched by the source title and arXiv identifier, author names, porous/density-dependent diffusion, nonconstant Neumann steady states, stationary patterns, predator-prey terminology, and degenerate/Turing resonance formulations. No prior SCOPE record covering this reduction, existence theorem, or dispersion factorization was located.

### External literature checked

- **Cherniha and Kriukova, Axioms 14 (2025), 655; arXiv:2608.11172.** The accessible full text states that its stability analysis is spatially homogeneous and that the search for nonconstant steady states satisfying zero Neumann conditions lies beyond its scope. The concrete system (58), the two positive homogeneous nodes, and the proportionality conditions were inspected. No proportional stationary reduction or domain-length theorem is given there.
- Exact-title, DOI, arXiv-ID, author-title, stationary-pattern, nonconstant-steady-state, \(V=3U\), and coefficient-specific searches were checked. No correction, comment, or follow-up containing the result above was located.
- Broader predator-prey literature contains many Turing-instability and nonconstant-steady-state results, including work with degenerate or density-dependent diffusion. These establish that the general phenomena are known, but the located papers use different systems and do not imply the model-specific proportional reduction, the \(L>\pi\) conclusion, or the perfect-square dispersion determinant for system (58).
- The original paper is openly available, so the source theorem statements and model equations relevant to this claim were inspected directly. No inaccessible paper was identified as especially likely to contain the same coefficient-specific reduction. Residual risk remains that an uncatalogued note or a differently worded treatment of the same special system exists.

The originality claim is therefore deliberately narrow: to the best of our knowledge, it concerns the exact proportional stationary family, its positive Neumann length threshold, and its relation to the degenerate dispersion touch in the cited model. Standard phase-plane, first-integral, and Turing-analysis techniques are not claimed as new.

## Value audit

The result resolves a concrete direction that the source paper explicitly leaves open for its flagship model. It shows that the parameter relations used to create two stable homogeneous states also hide a tractable nonlinear stationary sector, gives a rigorous family of positive patterns and a domain-size criterion, and distinguishes their mechanism from ordinary Turing instability. The perfect-square dispersion law and the \(L>\pi\) branch direction provide a reusable explanation for how nonconstant steady states can coexist with a homogeneous equilibrium that is linearly stable for every nonresonant Neumann mode.
