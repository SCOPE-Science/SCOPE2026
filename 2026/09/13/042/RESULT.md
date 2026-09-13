# Gap-splitting equivalence for q=2 P-bundles is false: a G=0 counterexample that never splits

## Context

Let F_tor_gap be compact Kahler threefolds X with -K_X nef, irregularity q(X)=2, Albanese map a:X->T a submersion onto a 2-torus with general fibre P1. Background theorem (used as context, not claimed): each such X is P(E) for a numerically flat rank-2 bundle E up to finite etale cover. For X=P(E) with E an extension 0->L1->E->L2->0 of unitary flat line bundles with class eta, let G(X) be the fibrewise Monge-Ampere energy gap between the P(E) fibre metric and the split product reference. Target question: does some finite etale cover X' split as T'xP1 iff G(X)=0 (equivalently pullback of eta vanishes for some torus isogeny)?

## Definitions

T=C^2/Lambda, Lambda=Z[i]^2, product of two square elliptic curves. theta=sqrt(2)/2, irrational with theta^2=1/2. chi:Lambda->U(1), chi(m1,n1,m2,n2)=exp(2pi i theta m1). L->T: unitary flat line bundle for chi. E=O_T (+) L, X=P(E). eta=0 in H^1(T,L^vee). On each fibre X_t ~= P1, omega_t is the Fubini-Study metric from the flat metric on E_t, omega_ref,t the split reference; omega_t=omega_ref,t+i dbar d phi_t, E_t the Aubin-Mabuchi energy of phi_t, G(X)=int_T |E_t| dvol_T.

## Result

The if-and-only-if gap criterion is FALSE. The (<=) direction fails. X=P(O_T (+) L) lies in F_tor_gap with G(X)=0, eta=0 (hence eta-pullback vanishes for every isogeny), c1(E)=c2(E)=0, pi1-representation rho=diag(1,exp(2pi i theta m1)), yet NO finite etale cover of X splits as T'xP1.

## Proof / evidence

Lemma 1 (membership): X is compact Kahler of dimension 3; E is Hermitian-flat hence numerically flat; O_{P(E)}(1) is nef so -K_X=O(2) tensor pi*L^vee is nef; Leray gives H^1(X,O_X)~=H^1(T,O_T) so q=2 and pi is the Albanese submersion with P1 fibres. Invariants: L flat gives c1(L)=0 (real Chern form vanishes, H^2(T,Z) torsion-free), so c(E)=1, c1=c2=0; eta=0; since E is split with product flat metric, omega_t=omega_ref,t pointwise, phi_t=0, E_t=0, G(X)=0 independent of normalization. Lemma 2 (covers): pi_*:pi1(X)->pi1(T) is an isomorphism, so every connected finite etale cover is Xx_T T'=P(pi*E) for a torus isogeny pi:T'->T; disconnected covers need not be considered since T'xP1 is connected. Lemma 3 (persistence): for degree-d isogeny, dLambda subset pi_*pi1(T'), and chi(d e1)=exp(2pi i d theta)!=1 as theta is irrational, so pi*L is always nontrivial. Lemma 4 (parity obstruction): if M is nontrivial unitary flat on a torus, H^0(M)=0, so h^0(O(+)M)=1, while h^0(F(+)F)=2h^0(F) is even; since P(E1)~=P(E2) over T' iff E1~=E2 tensor F, P(O(+)M) is never T'xP1. Combining: every cover is P(O(+)pi*L) with pi*L nontrivial, hence never splits. Numerical script confirms irrationality witness, Chern classes, parity, isogeny scan to degree 50, fibrewise FS volume quadrature 0.99974 with energy 0.

## Limitations

One-direction disproof only (G=0 yet never splits); the converse (split implies G=0) and a corrected classification of which P(E) split after covers are not decided. Gap vanishing uses metric coincidence, robust to normalization, but no exhaustive scan over alternative gap normalizations is attempted. Cover classification uses the standard pi1 isomorphism for P1-bundles.

## Reproducibility

Run python3 output/artifacts/gap_counterexample.py; it validates theta irrationality, c1=c2=0, h0 parity, pullback nontriviality, and fibrewise FS/energy quadrature, writing output/artifacts/verified_results.json.

## References

Cao-Horing, Manifolds with nef anticanonical bundle (Crelle 2017); Cao, Albanese maps of projective manifolds with nef anticanonical bundles (ASENS 2019); Matsumura-Wu, Compact Kahler three-folds with nef anti-canonical bundle (arXiv:2304.03163); Naumann-Wu, Albanese map for Kahler manifolds with nef anticanonical bundle (2025); Demailly-Peternell-Schneider Hermitian-semipositive background.
