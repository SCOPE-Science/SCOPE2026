# Review

## Correctness
PASS. For the symmetric pair \(p_\pm=(1\pm x)/2\), the two-copy input trace distance is exactly \(x\), while the normalized-square target distance is \(2x/(1+x^2)\). The triangle inequality and CPTP contraction therefore force every deterministic channel to incur uniform error at least \(x(1-x^2)/(2(1+x^2))\). Exact differentiation gives the unique maximizer \(x^2=\sqrt5-2\). Discarding one copy has exactly the same worst-case error, proving optimality. No finite experiment is used to establish the universal statement.

## Originality
PASS. The qualitative distinction between virtual power-state estimation and physical state preparation is prior: the anchor itself separates ordinary and signed branch averages, Huggins et al. explicitly call the target virtual, and a public source-specific review already objects to a physical-state interpretation. The accepted claim is narrower and quantitative: it solves the deterministic two-copy-to-one CPTP minimax approximation problem exactly. Searches for source-specific, closest-channel, power-map, virtual-distillation, and trace-distance formulations found no equivalent theorem or stronger covering result.

## Value
PASS. A sharp state-conversion radius is materially stronger than merely observing that normalized squaring is nonlinear. It shows that the gap cannot be removed by replacing the SWAP construction with an arbitrary deterministic two-copy physical channel: a uniform error of at least \(0.1501415530\ldots\) remains even on commuting qubits, and doing nothing to one copy is already minimax optimal. This supplies an operational calibration for when signed virtual access cannot be substituted by a deterministic physical output.

## Closest literature and limitations
The closest primary source is arXiv:2603.11568v2, which supplies the exact SWAP branch identities and explicitly distinguishes the unconditional branch average from signed power-state access. The foundational virtual-distillation paper, DOI 10.1103/PhysRevX.11.041036, states that the normalized power state is used without explicitly preparing it. A public review of the anchor covers the qualitative objection but not the exact minimax constant. The theorem here is limited to one round, two copies, diagonal qubits, deterministic CPTP output, and trace distance; no claim is made for postselection, higher powers, or other metrics.

Self-review: passed. Independent audit: not yet performed.
