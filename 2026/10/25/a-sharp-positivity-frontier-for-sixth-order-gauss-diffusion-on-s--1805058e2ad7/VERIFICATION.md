---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The exact rational map is R(z)=(120−60z+12z²−z³)/(120+60z+12z²+z³). The strongly regular graph identity reduces R(hL) to I+b(h)L+c(h)L², whose two offdiagonal values are μ c(h) and −b(h)−(2k−λ)c(h). The proof constructs scalar divided-difference and secant inequalities using R′(z)=−24[(z²−15)²+375]/Q(z)²<0 and derivative ((R(z)−1)/z)′=2(z⁴+120z²+1200z+3600)/Q(z)²>0, forcing both values positive. Symmetry/regularity give each spectral projector constant diagonal, so F(h)=[1+fR(ah)+gR(bh)]/v has F′(h)<0, F(0)=1 and F(∞)=(2−v)/v<0; uniqueness of H_G follows. Symmetric spectral A-stability and eigenvalue 1 at zero give norm2=1 even after diagonal negativity. Exact SymPy derivatives independently vanish to residual zero; Petersen graph diagonal is 163/22231 at h=3 and −4057/82955 at h=4; finite graph checks corroborate, not prove, all-graph assertion.

## originality

PASS

The original Zappavigna–Colaneri–Kirkland–Shorten paper establishes negative general Padé positivity behavior and gives positive-systems counterexamples, but not exact all-SRG sixth-order positive off-diagonals and single diagonal zero. Blanes–Iserles–Macnamara addresses general positivity barriers and different positivity-preserving integrators. A relevant publicly recorded [2/2] Markov-chain result treats fourth-order Gauss and an eight-state directed generator, not the candidate [3/3] undirected all-parameter strongly regular transition. Standard strongly regular adjacency algebra supplies reduction, not the sign/unique-zero theorem. The originality conclusion is qualified for unindexed specialized literature and possible general complete-multipartite formulas.

## value

PASS

A-stability says nothing about entrywise physical positivity of diffusive concentrations. The exact sharp timestep on the mathematically natural infinite family of strongly regular graphs, including primitive Petersen and triangular members, is a structural classification rather than a sample-time computation. It identifies a surprising all-time strictly positive offdiagonal pattern coexisting with a single diagonal sign frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
