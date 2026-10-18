---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For e=1 and gamma=eta, positive predator nullcline gives v=beta u/eta, and exactly h(u)=E/alpha with h=(1-u)(u+A)-beta u/[eta(1+beta u)]. Its derivative has two strictly positive distinct zeros iff beta^2>eta, h′(0)<0<h′(u_i) with u_i=((beta^2/eta)^(1/3)-1)/beta; monotonic ranges then yield iff alpha max(0,h(u_-))<E<alpha min(A,h(u_+)). Jacobian determinant is -alpha beta u^2 h′(u)/(1+beta u)^2, making the middle root a saddle, not asserting outer stability without trace. For alpha=1,A=1/5,beta=8,eta=gamma=6,e=1,E=39/200, independent SymPy reconstructed P(u)=-4800u^3+3240u^2-296u+3 and roots 0.011577...,0.094970...,0.568452..., plus trace polynomial Q(u)=960u^3-144u^2-161u+54 with global minimum Q(7/24)=335/18>0: outer equilibria hyperbolic attracting, saddle in middle, and persistence by implicit-function/hyperbolicity.

## originality

PASS

The Liu–Liang–Li–Ye–Ma 2026 article provides this differential system, cubic coexistence equation, sufficient uniqueness conditions and stability criteria, but its full text does not state this exact positive-harvesting interval or the specific certified two-sink witness. Arancibia-Ibarra et al. 2022 have related bistability in a different Leslie–Gower nullcline model; generic three-equilibrium or ecological bistability is prior art, while the sharp E-interval in this particular rational mortality/prey-harvest subfamily is a distinct parameter theorem.

## value

PASS

The critical harvest-rate interval gives a sharp, biologically motivated multiplicity threshold and exhibits two coexisting locally attracting prey-predator equilibria at the same positive harvest, clarifying alternatives beyond sufficient uniqueness results. All-positive hyperbolic witness has robust off-subfamily significance; does not overclaim basin geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
