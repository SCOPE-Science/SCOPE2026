# Unitary conjugacy from full-support two-sided intertwining for Cartans in a fixed non-ergodic amenable crossed product

## Context

Cartan uniqueness is settled for ergodic hyperfinite and many nonamenable settings up to automorphism or unitary conjugacy in factors. The non-ergodic (non-factor) amenable group-measure-space case, where the center is nontrivial and ergodic decomposition produces a direct integral of factors, lacked an explicit conditional unitary-rigidity statement in terms of Popa intertwining on every central cutdown.

## Definitions

Let Gamma be countable amenable acting freely, probability-measure-preservingly on a standard probability space (X,mu), ergodicity not assumed. Let M=L^infty(X) rtimes Gamma with canonical Cartan A=L^infty(X) and faithful trace tau(f u_g)=int f dmu delta_{g,e}. A Cartan B in M means maximal abelian, regular (normalizer generates M), with faithful normal conditional expectation. Popa intertwining P prec_M Q is the usual bimodule criterion via the sequential/unitary formulation. Z(M) denotes the center; Mz, Az, Bz denote cutdowns by a central projection z.

## Result

Let M, A, B be as above. Assume for every nonzero projection z in Z(M) that Az prec_{Mz} Bz and Bz prec_{Mz} Az. Then there exists u in U(M) with uAu*=B. In fact one-sided full-support intertwining already suffices; the two-sided hypothesis is more than needed.

## Proof / evidence

Decompose over Z(M)=L^infty(Y,nu): M=int_Y M_y, A=int A_y, B=int B_y with expectations disintegrating; Z(M) subset A cap B since both are MASAs, so maps are Z-modular. Fibers are free ergodic crossed products: M_y=L^infty(X_y) rtimes Gamma; for infinite Gamma a.e. fiber is the hyperfinite II1 factor R with canonical Cartan A_y by Connes-Feldman-Weiss hyperfiniteness; for finite Gamma a.e. fiber is a matrix algebra M_n(C) with diagonal MASAs. Lemma (global-to-local): failure of A_y prec B_y on a positive-measure set E yields, via Popa finite-set criterion, a Borel field of almost-orthogonal unitaries selected by Jankov-von Neumann, integrated to global unitaries tilde{u}_{m,k} in A z_E and diagonalized as w_n=tilde{u}_{n,n} to witness A z_E not prec B z_E, contradiction. Hence A_y prec B_y a.e. (and symmetrically). Fiberwise Popa Cartan-conjugacy in II1 factors (elementary MASA conjugacy in M_n) gives u_y with u_y A_y u_y*=B_y a.e. The conjugating set G defined by countable-generator tests E_{B,y}(u a_k u*)=u a_k u* and E_{A,y}(u* b_k u)=u* b_k u is Borel with nonempty a.e. fibers, so a measurable selector glues to u in U(M) with uAu*=B. Cited black boxes: Takesaki disintegration, Popa intertwining characterizations, Popa factor Cartan-conjugacy criterion, CFW amenability/hyperfiniteness, Feldman-Moore, Jankov-von Neumann selection.

## Limitations

Modulo cited standard machinery; null-set and Borel-structure details at standard direct-integral level, not re-proved. No new classification of nonamenable Cartans claimed. Conclusion is unitary conjugacy within the fixed M, not automorphism classification across algebras.

## Reproducibility

Hypotheses checkable from freeness, amenability, and Popa intertwining on central cutdowns; proof steps reference standard sources (Takesaki vol I Ch IV.8; Popa 2006 intertwining; Popa/Ioana-Peterson-Popa/Popa-Vaes conjugacy criterion; Connes-Feldman-Weiss; Jankov-von Neumann). No computation required.

## References

Connes-Feldman-Weiss 1981; Takesaki Theory of Operator Algebras I; Popa 2006 intertwining; Popa Cartan-conjugacy criterion (Ioana-Peterson-Popa, Popa-Vaes, Vaes notes); Feldman-Moore; Popa-Shlyakhtenko-Vaes 2020; Connes-Jones 1982; Popa-Vaes 2014.
