# Independent mathematical audit

## correctness

PASS

PASS: For the exact synchronous self-inclusive averaging/edge-confidence update, initial gap at edge 1-2 is 3/10>1/4 while all internal gaps are 1/5<1/4. Assuming the bridge absent, the four-path symmetric state has a0=3/10,b0=1/10 and a_{t+1}=(a_t+b_t)/2,b_{t+1}=a_t/3; internal gaps remain <=1/5 and internal confidences never decrease. The positive recurrence a_{t+2}=a_{t+1}/2+a_t/6 has roots λ=(3+sqrt33)/12 and ν=(3-sqrt33)/12. Comparison from both initial steps gives (1/4)λ^t<a_t<=(3/10)λ^t, proving nonreceptivity for delta<=lambda and first crossing for delta>lambda. Explicit positive Perron amplitude A=3/20+sqrt33/44 gives first-hit T(delta)log(delta/lambda)->log(4A). Component self-inclusive stationary weights for isolated small tree components rule out common-limit permanently cut bridge for <=4 vertices, under the restricted fixed one-cut and internal-receptive assumptions. Independent rational full-dynamics simulations for 5 delta values reproduce never-receptive examples and first-hit times 5,2,1, but infinite conclusions rely on recurrence proofs.

## originality

PASS

Same-model Li–Luo–Porter 2023/2025 treats eventual graph stabilization and reports equal-limit missing edges numerically, but does not imply this specific minimum-tree-size bridge, exact irrational rate boundary or critical delay. A different adaptive rewiring model and general seven-agent switching results do not dominate the claim.

## value

PASS

PASS: A natural question about whether common limiting opinions force a permanently missing confidence bridge is answered by a smallest connected tree witness, exact spectral race threshold, and logarithmic first-reception delay law. Its quantitative, structural result is not reducible to simulation-only observations, though initial opinion matching is codimension one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
