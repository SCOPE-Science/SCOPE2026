---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For every n>=3 the crown Laplacian splits into eigenvalue sectors 0,2n-2,n-2,n with multiplicities 1,1,n-1,n-1. Direct spectral projectors produce 2n*d=1+c+(n-1)(a+b), 2n*w=1+c-a-b, 2n*m=1-c+(n-1)(a-b), 2n*e=1-c-a+b with a=R(nh), b=R((n-2)h), c=R((2n-2)h), R=P/Q, P(z)=120-60z+12z^2-z^3, Q(z)=120+60z+12z^2+z^3. Independent exact symbolic polynomial multiplication using u=n-2 and positive common denominator Q(nh)Q((n-2)h)Q((2n-2)h) confirms w,m,e numerators have respectively 40,32,48 strictly positive integer monomials, beginning at powers h^2,h^3,h; this is an all-parameter identity, not sample numerics. Independently rederived R prime=-24[(z^2-15)^2+375]/Q(z)^2<0. Therefore d decreases strictly from 1 to -(n-1)/n, crossing zero exactly once H_n; all non-diagonal entries remain >0 for h>0. |R(z)|<1 for z>0, row sums 1 and Euclidean norm 1 for all h. Local uniform convergence d(x/n)->R(x) shows nH_n->the unique positive root P(rho)=0 (rho about 4.64437070925217). Independently inspected crown_verify.py with exact polynomial and rational matrix formulas; reconstructed the symbolic certificate rather than relying on a saved log.

## originality

PASS

The crown graph spectrum is known from Klee–Stamps and the [3/3] Gauss–Legendre rational stability function is classical. General SSP barriers and positive-systems results do not establish a universal exact diagonal threshold for this reversible crown family, nor do they imply all off-diagonal entries stay positive for ALL positive steps. Published Resultary [2/2] Padé examples involve a different order and different Markov generators, so their unusual positivity windows do not dominate this theorem. Best-of-knowledge PASS for the novel exact [3/3] crown positivity horizon and nH_n scaling.

## value

PASS

Entrywise positivity is essential for nonnegative diffusion states but is independent from spectral contractivity of a high-order A-stable integrator. The crown networks form a natural regular bipartite spectral family. A unique sharp positivity interval, rigorously positive off-diagonal entries outside it, and n-scaling of the horizon are meaningful stability facts rather than textbook formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
