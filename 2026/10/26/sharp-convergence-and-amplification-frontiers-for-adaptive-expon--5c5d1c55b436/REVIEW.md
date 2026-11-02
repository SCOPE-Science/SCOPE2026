# Independent mathematical audit

## correctness

PASS

For scalar s>0 and v with h=min(H,β/|s−1|), the log covariance u=log s obeys continuous clipped-Ricker map g(u)=u−clip(H(e^u−1),−β,β), bounded on a forward interval. Every nontrivial 2-cycle would have u>0>v and δ=u−v with δ≥log((1+δ/H)/(1−δ/H))>2δ/H≥δ for H≤2; impossible. Coppel's interval-iteration theorem therefore forces s→1. Mean multiplier 1−hs tends to 1−H, giving exact joint frontier H<2; at s0=1 it oscillates for H=2 and grows for H>2. Gain r=hs∈(0,H+β], maximum at s=1+β/H, so uniform one-step |1−r|≤1 iff H+β≤2. At H=2, g∘g(u)=u−(4/3)u³+O(u⁴), hence √n|u_n|→√3/2 absent finite capture; two-step mean multiplier 1−4u²+O(u³) yields generic |v_n|~C n^(−3/2), while s0=e^β captures s=1 after one step. Independent SymPy expansions and 119 gain/frontier cases agree; they do not prove Coppel's universal implication.

## originality

PASS

Che et al. full accessible preprint Theorem 1 restricts H≤1 and β≤1 for Gaussian convergence, while the new sharp H<2 arbitrary cap and H+β exact one-step frontier lie outside their proved domain. Coppel theory and classical Ricker constant-parameter attraction are prior lemmas; the cap and separate mean recursion require additional arguments. Resultary capped optimization examples use distinct step schemes.

## value

PASS

Identifies the maximal stable step-size regime for a motivated Gaussian variational integrator and separates transient mean amplification from ultimate convergence. At critical H=2 the covariance can settle while the mean fails, a concrete structurally relevant distinction. Sharp √n and n^(−3/2) rates quantify its flip boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
