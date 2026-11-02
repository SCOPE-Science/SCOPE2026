# Review of the early-peak SIR jump theorem

## Correctness
PASS. The proof starts from the Euler SIR equations in the originating study and reconstructs the exact crossing manifold \(\gamma=u(1-u)r\), with \(u=\beta I_0\), \(r=S_0/I_0\). The strict descending-crossing and positivity conditions reduce precisely to \(1/2<u<1\), \(0<r<(1-u)/u^3\). The proof verifies that subsequent prevalence is decreasing and that these conditions provide a two-sided neighborhood of globally positive trajectories. Algebraic maximization establishes \(J<2/5\) and a limiting admissible family; exact rational computations independently check the concrete jump \(5992/28125\), 840 parameter pairs, and nearby peak indices. The limiting boundary is not mistaken for an admissible equality case.

## Originality
PASS under available evidence, not independent certification. The originating paper [1] explicitly explains and numerically shows peak-time attack jumps. That qualitative observation is credited, not claimed new. Its complete text does not give the first-downward-switch necessary-and-sufficient seed threshold \(1/5\), the algebraic admissibility domain, or the sharp supremum \(2/5\). Diekmann et al. [2] study a different broad renewal formulation, Lemos-Silva et al. [3] use a different discretization, and Nguyen et al. [4] bound continuous-time post-peak overshoot rather than a jump in attack at a peak-time switch. The mathematical-record and literature searches found no direct implication covering the exact extremal pair. Bibliographic incompleteness remains a genuine risk.

## Mathematical value
PASS. In contrast to merely recomputing a known numerical sawtooth, the theorem gives exact universal restrictions on the **earliest** downward peak shift: an initial infected share of at most \(20\%\) makes this specific switch impossible in an admissible epidemic, and \(40\%\) is the sharp but unattained supremum of its attack jump. These constants arise from competing prevalence-growth and susceptible-positivity inequalities, and distinguish early from later peak-switch mechanisms. This resolves a natural finite-time extremal question motivated by the originating paper's peak-time bifurcations; it does not assert any bound for later switches.

## Closest literature and limits
[1] Ozbay, Nielsen, Nguyen, arXiv:2212.06995, numerical bifurcations and qualitative peak-shift explanation. [2] Diekmann et al., PNAS 2021, general renewal formulation and peak comparison. [3] Lemos-Silva et al., arXiv:2409.09157, nonstandard discretization. [4] Nguyen et al., J. R. Soc. Interface 2023, continuous-time overshoot bound. The result does not apply to stochastic graph contagion, all Euler schemes, arbitrary initial immunity, or later peak-day transitions. Strict positivity near switching is essential. Independent literature adjudication remains pending.

Self-review: passed. Independent audit: not yet performed.
