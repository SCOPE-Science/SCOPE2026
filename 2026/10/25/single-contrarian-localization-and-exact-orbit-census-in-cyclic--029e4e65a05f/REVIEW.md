# Independent mathematical audit

## correctness

PASS

At each ordinary site, an equal adjacent pair is permanently frozen since each endpoint sees its own bit twice. An ordinary path initially alternating cannot keep alternating beyond two updates: odd path endpoints cannot both reverse; even-path parity forces equal neighboring ordinary bits at latest second step. Propagation from a frozen ordinary pair along the finite ordinary path makes every ordinary site eventually constant (or creates further frozen pairs). The distinguished site0 then updates by a constant map if its two ordinary neighbors agree or by complement if they differ, yielding only fixed points or 2-cycles with xor difference precisely site0. In any recurrent state the ordinary path decomposes into maximal constant runs each length≥2; these are sufficient for stability under both hub bits. With q(z)=z²/(1−z), fixed configurations A_n=2[z^{n−1}]q/(1−q²), primitive two-cycles B_n=2[z^{n−1}]q²/(1−q²), giving 2B/(A+2B)→2/3 from the common dominant simple pole (sqrt5−1)/2. Independent exhaustive dynamics over all 2^n initial states for n=3..12 reproduced counts and site0-only two-cycle differences; the frozen-pair proof covers every n≥3.

## originality

PASS

The closest primary theory for uniform radius-one majority cellular automata (Nakar–Ron 2022) and symmetric majority networks (Benjamini et al 2014, Kaaser et al 2015) excludes a single site using the complemented local rule. While period≤2 under uniform symmetric majority is classical, its hypotheses do not imply robustness under one antimonotone defect, localization of all oscillations at that defect, or these exact run-length generating functions. Best-knowledge originality PASS, subject to possible unindexed heterogeneous-majority papers.

## value

PASS

A one-defect deviation from symmetric majority is a mathematically natural robustness boundary. Complete all-cycle classification plus exact Fibonacci-type census and limiting oscillator proportion (2/3 of periodic configurations) isolates the effect of one inverted response. The theorem is structural and not merely a short finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
