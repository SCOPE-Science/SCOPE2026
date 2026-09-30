# Independent audit — 2026-09-29
- Source: `2026/09/12/034`
- Assigned/current tree SHA: `682bea928779fc61b093131187c6708a29926d65`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **repaired**

## Three-axis assessment

### Correctness

**PASSED** — The nonvanishing calculation is correct. The conductor is I=(t^2-1)B, with A/I≅F7 and B/I≅F7×F7. Quillen gives K3(F7)≅Z/48 and homotopy invariance gives K3(F7[t])≅Z/48. In the birelative Mayer–Vietoris sequence the map K3(B)⊕K3(A/I)->K3(B/I) has diagonal image (the formula may be written u-v rather than u+v depending on the sign convention). Its cokernel is Z/48, which injects through the boundary into K2(A,B,I). The literal Dennis–Stein pair t-1,t+1 is not admissible, and any map from this 48-torsion boundary class to a characteristic-7 vector-space target vanishes.

### Originality

**PASSED** — SUPPORTED NARROWLY. The mechanism is classical birelative/Milnor-square K-theory, but the audit located no source stating this exact split-node-over-F7 Z/48 worked computation. The repaired record claims only the explicit instance, not a new Mayer–Vietoris theorem.

### Scientific value

**PASSED** — The worked example is useful because it converts the conductor square into an explicit prime-to-7 boundary subgroup and also explains why the originally requested Dennis/dlog detection route cannot see that class. It is a concrete computation built from standard theory.

## Independent checks

- current main record tree exactly equals the assigned source-tree SHA
- proved A=F7+(t^2-1)F7[t] and verified the conductor criterion using f and tf at t=±1
- recomputed the CRT quotient square A/I -> B/I = diagonal F7 -> F7×F7
- recomputed coker(diag:Z/48 -> (Z/48)^2) as Z/48
- checked gcd(48,7)=1 and the inadmissibility of <t-1,t+1>

## Limitations

- This determines only a Z/48 subgroup, not the whole group K2(A,B,I).
- It does not produce a nonzero Dennis–Stein symbol or Dennis/dlog trace; the prime-to-7 boundary class cannot be detected in a characteristic-7 vector-space target.
- The originality claim is limited to this explicit worked instance because search absence is not proof of priority.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/034
- https://doi.org/10.1007/BF00538431
- https://sites.math.rutgers.edu/~weibel/papers-dir/KABI-II.pdf
- https://doi.org/10.4153/CJM-1993-018-x
- https://arxiv.org/abs/1211.1533

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
