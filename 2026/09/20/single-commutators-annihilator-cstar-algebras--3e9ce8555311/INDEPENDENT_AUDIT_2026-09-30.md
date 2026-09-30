# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/single-commutators-annihilator-cstar-algebras--3e9ce8555311`  
Assigned and audited source tree: `d3ee4bc1d62fb084b830658f381f252dfadce214`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `2ba7e840e362f93ce733972a0641ac7035e01a8b`  
Disposition: **passed**

## Correctness

**independently_supported**. The classification C_1(A)=ker tau_F follows correctly from the c0-sum structure and the two recent dimension-free commutator theorems. The extension of Liu’s separable result to arbitrary H is valid because M=closure(ran T+ran T*) is separable and reducing, while T vanishes on M^perp; if M is finite-dimensional one may enlarge by an infinite separable subspace on which T is zero. The uniform square-root block estimates then force both factors back into the c0-sum. The quotient/distance formulas follow from the norm-one section by scalar identities on finite blocks, and the bounded-trace description follows from the l1 dual and vanishing of bounded traces on infinite-dimensional K(H).

## Originality

**qualified_supported_recent_synthesis**. Liu’s September 2026 theorem supplies compact-operator commutator width one with a universal square-root bound, and Shen–Wang–Zhi supply the dimension-independent trace-zero matrix bound. The annihilator C*-algebra decomposition itself is classical. Current targeted searches did not locate the exact global kernel, distance, trace-dual, and commutator-width-one package for arbitrary annihilator C*-algebras. The contribution is therefore a timely structural synthesis unlocked by those recent bounds rather than a new elementary-block theorem.

## Scientific value

**meaningful_structural_consequence**. The result identifies the exact and only obstruction to being one commutator across arbitrary c0-sums, including unbounded matrix dimensions and nonseparable elementary blocks, and gives an exact quotient metric plus uniform factor control.

## Independent checks

- Checked the nonseparable compact-operator reduction.
- Checked c0 gluing from the square-root estimates.
- Verified the trace-dual and distance arguments.

## Literature and evidence checked

- https://arxiv.org/abs/2609.20672
- https://arxiv.org/abs/2609.09938
- https://arxiv.org/abs/1006.3934
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/single-commutators-annihilator-cstar-algebras--3e9ce8555311

## Limitations

- Restricted to annihilator/dual C*-algebras.
- Depends essentially on two very recent uniform commutator theorems.
- Older dual-C*-algebra literature may contain equivalent special cases.
