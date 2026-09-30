# Independent Audit — 2026/09/18/sharp-catalyst-basin-dichotomy--9f083a737492

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `127bc03b37ea81789def9738f7c1db5040b85d36`
- Disposition: **PASSED**

## Correctness

**PASS** — The global basin proof is correct. The quadratic energy for a and c is decreasing and its dissipation makes their gradient energies integrable; the source's uniform boundedness and parabolic regularity make those gradients tend to zero. Poincare-Wirtinger then reduces every omega-limit to spatial constants controlled by C(t)=int c. Because the energy converges, |C-M1/2| has a limit and hence C itself converges. The identity B'=int b(c-a) then forces either c_infty=a_infty or B_infty=0, leaving exactly the positive and boundary equilibrium branches. The mean-zero equation for b-B yields L2 convergence of b on the positive branch. If B0=0 the invariant face b=0 gives the boundary equilibrium. If B0>0 and boundary convergence were assumed, heat-semigroup smoothing upgrades a,c to uniform convergence, so eventually c-a is uniformly positive; then B'>=gamma B while B remains positive and bounded by conservation, a contradiction. The argument includes M1=M2 and correctly excludes the coalescence endpoint M1=2M2.

## Originality

**PASS** — Nguyen-Tang's open-access paper explicitly says that Lyapunov instability of the boundary equilibrium does not rule out a later return and convergence to it, and it states global attraction of the positive equilibrium as a conjecture in the coexistence mass regime. The literal conjecture also overlooks the invariant face b0=0. Targeted searches by the exact reaction terms, mass regime, title/DOI and catalyst/boundary terminology found no later proof or correction. The audited record therefore closes the source-specific global basin question and identifies the sharp positive-total-catalyst condition.

## Scientific value

**PASS** — The result upgrades local stability plus boundary instability to a complete global basin classification and fixes a genuine exception in the source conjecture. It also links global attraction to the source's local exponential theorem, giving eventual exponential convergence for every trajectory with positive catalyst mass.

## Sources

- Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria (Thi Lien Nguyen; Bao Quoc Tang): https://doi.org/10.1007/s00033-026-02847-0 — Open-access full article checked; it states the unresolved return-to-boundary issue and formulates global attraction of the positive equilibrium as a conjecture in M2<=M1<2M2.
- Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria (Thi Lien Nguyen; Bao Quoc Tang): https://arxiv.org/abs/2410.22928 — Preprint version of the primary source.

## Limitations

- The theorem is restricted to the source's catalytic system with homogeneous Neumann boundary conditions and bounded classical solutions.
- It does not cover M1=2M2, the source's second symmetric network, or provide a new explicit global exponential rate from time zero.
- The originality claim is source-specific rather than a general theorem for irreversible reaction networks.

## Independent checks

```json
{
  "primary_source_open_access_full_text_checked": true,
  "source_conjecture_verified": true,
  "proof_reconstructed": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first.
