# Review of the three-oscillator thermal-conductance optimization

## Correctness: PASS
The claim is a sharp, quantified equality for all \(p,q>0\), \(x\ge0\), and \(T_L>T_R>0\). The positive stiffness matrix and boundary damping ensure a unique stationary covariance. Constructing the \(21\) stationary covariance equations gives two exact determinant identities; Cramer's rule derives the normalized current. Its denominator is strictly positive and quadratic in the central spring strength, so the unique constrained optimum and all boundary cases follow. The accompanying checker reconstructed the determinant identities symbolically and passed \(9,100\) independent numerical tests. The symbolic identities, not finite tests, provide the infinite analytical certificate.

## Originality: PASS, with documented historical-priority risk
published-finding corpus searches for three-site Langevin conduction, central pinning optimization, and resonance/impedance variants gave no directly equivalent claim among inspected closest findings. Established literature includes three-site cyclic heat transport (Eckmann–Zabey, 2003), long-chain conductance and boundary/substrate pinning (Roy–Dhar, 2007 and 2008), general heat-current generating functions for arbitrary networks (Saito–Dhar, 2010), and local-reservoir harmonic chains (Falasco et al., 2015). The last two are general methods that could *in principle* imply the result after specialization and nontrivial exact algebra, but do not state the sharp middle-site optimizer or asymmetry-induced boundary transition in the reviewed material. The 2008 paper studies asymptotic behavior in long disordered chains, not fixed three-site pin optimization. Earlier unpublished/less discoverable special cases could cover the result; searches cannot prove priority.

## Mathematical value: PASS
The result addresses a physically natural design question: with fixed terminal wells and heat baths, how much middle-site substrate pinning maximizes steady transport? The exact Lorentzian reduces the full continuum of design choices to an algebraic optimum, supplies a real boundary/interior phase transition, and shows quantitatively how terminal heterogeneity moves that transition. The full parameter and boundary classification is stronger than evaluating conductance at a few choices and has plausible utility for finite phononic or electromechanical toy-network design. It does not imply a general theorem for long chains or noisy experimental inference.

## Closest literature and limitations
Eckmann–Zabey, arXiv:nlin/0305006; Roy–Dhar, arXiv:0711.4318 and arXiv:0806.4693; Saito–Dhar, arXiv:1012.0622; Falasco et al., arXiv:1505.05088. They explain basic forward conduction or distinct setups. A broad search of historical three-oscillator tuning work is necessarily incomplete. No external independent review exists.

Self-review: passed. Independent audit: not yet performed.
