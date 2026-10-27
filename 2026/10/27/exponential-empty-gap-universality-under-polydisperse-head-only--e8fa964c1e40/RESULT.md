# Exponential empty-gap universality under polydisperse head-only adsorption

## Finding
Consider homogeneous irreversible deposition of oriented closed intervals on the initially uncovered real line. Proposed heads form a space-time Poisson process of intensity \(R(t)\,dx\,dt\), with a deterministic locally integrable rate \(R(t)\geq0\). Each proposal carries an independently sampled *connected* interval containing its head, with a strictly positive length lying in a fixed compact interval \([\ell_-,\ell_+]\subset(0,\infty)\); its left/right orientation and length law may depend on time but not on spatial position or prior proposals. **Accept a proposed interval exactly when its head is not covered**, even if the rest of the interval overlaps existing coverage. Accepted intervals remain covered forever.

Write \(\Lambda(t)=\int_0^t R(s)\,ds\), with \(0<\Lambda(t)<\infty\), and let \(F(t)\) be the probability that a fixed point is uncovered at time \(t\). For any \(x\geq0\), the probability that every point of a prescribed interval of length \(x\) is still uncovered is exactly
\[
P(x,t)=F(t)e^{-\Lambda(t)x}.
\]
Consequently, the intensity density of maximal uncovered gaps of length \(x>0\), per unit substrate length, is
\[
q_t(x)=F(t)\Lambda(t)^2e^{-\Lambda(t)x}.
\]
In particular, the length of an uncovered gap sampled according to **gap-count intensity**, rather than length bias, is exactly \(\operatorname{Exp}(\Lambda(t))\):
\[
\frac{q_t(x)}{\int_0^\infty q_t(y)\,dy}=\Lambda(t)e^{-\Lambda(t)x},\qquad x>0.
\]
The mean gap length is \(1/\Lambda(t)\), regardless of the deposited-length distribution or orientation bias. The expected number of gaps longer than \(a\geq0\), per unit substrate length, is \(F(t)\Lambda(t)e^{-\Lambda(t)a}\). The theorem does *not* assert that successive gap lengths are independent, or that \(F(t)\) is independent of deposited lengths.

## Assumptions and scope
The line is initially vacant; deposition proposals are spatially homogeneous and independent across disjoint sets; mark laws are independent of the past and spatially homogeneous at each time; deposited intervals are connected and have positive lengths bounded above and below. The head-point rule is distinct from ordinary hard-rod random sequential adsorption, which rejects an interval if **any** part overlaps existing coverage. All assertions concern a deterministic finite observation time with positive finite cumulative head intensity. The density \(q_t\) is a stationary *gap-count intensity measure*, not an independence claim or a limiting thermodynamic approximation.

## Proof
Fix \(x>0\) and the test interval \(I=(0,x)\). Split the marked Poisson proposal process into three independent restrictions: head locations in \(( -\infty,0)\), in \(I\), and in \((x,\infty)\). As long as \(I\) remains entirely uncovered, **every** proposal whose head lies inside \(I\) is accepted and covers a positive-length portion of \(I\). Hence survival of \(I\) requires no such proposal before time \(t\), an event with probability \(e^{-\Lambda(t)x}\).

Independently, run two killed half-line processes. The left process uses only heads strictly to the left of zero. It accepts a proposal if its head is unoccupied by previous *left-process* accepted intervals, but is killed as soon as any newly accepted connected interval touches zero or crosses into \(I\). The right process is defined symmetrically from heads strictly to the right of \(x\), and is killed as soon as an accepted interval reaches \(x\). Before either killing time, all intervals in each process are confined to its own half-line. In particular they cannot affect acceptance decisions for heads in the other half-line: a connected interval cannot reach the other side without passing through \(I\) and thus causing killing first. Therefore the two half-line survival events are independent, and their probabilities, say \(S_-(t)\) and \(S_+(t)\), do not depend on \(x\), by spatial homogeneity. Coupling each killed process to the full deposition process up to the first time \(I\) is covered proves the exact identity
\[
P(x,t)=e^{-\Lambda(t)x}S_-(t)S_+(t).
\]
The same argument for a single test point (or the limit \(x\downarrow0\)) gives \(F(t)=S_-(t)S_+(t)\). Endpoints have probability zero of coinciding with random heads; closed-versus-open interval conventions therefore do not affect the probabilities. This proves the first formula without using any monodisperse empty-interval differential equation.

Let \(q_t\) denote the expected number per unit substrate length of maximal uncovered interval components, disintegrated by their lengths. Stationarity and the mass-transport/Campbell identity give, for every \(x\geq0\),
\[
P(x,t)=\int_{(x,\infty)}(g-x)\,q_t(dg).
\]
Indeed, a gap of length \(g\) contains exactly \((g-x)_+\) possible left endpoints of fully uncovered length-\(x\) test intervals. Differentiating twice in the distributional sense on \((0,\infty)\) yields \(q_t(dg)=\Lambda(t)^2F(t)e^{-\Lambda(t)g}\,dg\). Its integral is \(\Lambda(t)F(t)\), and normalization gives the stated exponential law. Existence of the infinite-line process follows from the standard finite-ancestor graphical construction: to determine an acceptance decision in a bounded region, a backward chain of potentially blocking proposals must have successively earlier times and spatial steps at most \(\ell_+\). The expected number of such chains of length \(k\) anchored in a bounded window is bounded by \(C(2\ell_+\Lambda(t))^k/k!\) for a finite window constant \(C\). Hence infinite backward chains have probability zero. Bounded deposited lengths and finite cumulative input intensity then imply locally finite unions of accepted intervals and finite expected boundary/gap intensity. Since the probability of no proposals with heads within distance \(\ell_+\) of a fixed point is positive, \(F(t)>0\) for finite \(t\). Thus the normalization is legitimate.

## Verification
The independent `reproduce_gap_law.py` script simulates the underlying Poisson attempt process directly on an extended continuum interval; it accepts proposed segments only if the head is still vacant and maintains an exact union of accepted intervals. For deterministic mixed short/long deposited lengths and direction bias, it compares the observed **length-weighted tail ratio** \(\sum (g-x)_+/\sum g\) with the exact \(e^{-\Lambda x}\), as well as the mean count-sampled gap length with \(1/\Lambda\). The script uses fixed pseudorandom seeds and prints all comparisons. These finite Monte Carlo checks are reproducibility aids and are not the proof of the infinite-line theorem.

## Relationship to prior work
Gromenko, Privman and Glasser (arXiv:0712.3567, first public version 2007-12-20), Sections III–IV, derive \(P(x,t)=e^{-Rxt}F(t)\) and an exponential empty-gap density in their **fixed-length, orientation-symmetric** version of head-only crack deposition, using a closing empty-interval hierarchy. The present result establishes that the *normalized exponential gap distribution persists exactly even when that closed hierarchy is unavailable*: lengths may be genuinely random and the orientation law may be asymmetric and time-varying. It does not claim a new formula for their previously known monodisperse case or for the unknown heterogeneous coverage fraction.

Araújo and Cadilhe (arXiv:cond-mat/0404422, first public version 2004-04-18), Section II, analyze polydisperse **ordinary non-overlap** RSA, where attempts are rejected for whole-rod overlap. That model has a different acceptance rule and its gap statistics do not imply this head-only result. The comparison clarifies why the rule at the proposal head, not merely the mixture of deposited sizes, is decisive. A targeted check of publicly searchable mathematical records and paper titles did not reveal the stated mixed-length head-only universality theorem; this is a limited literature assessment, not a claim of exhaustive historical priority.

## Limitations
The result does not determine \(F(t)\), the number of deposited segments, correlations between different gaps, late-time behavior as \(t\to\infty\), or finite-boundary corrections. The proof relies crucially on independent spatially homogeneous Poisson proposals, pointwise-head acceptance, connected deposition intervals, an initially vacant substrate, and the absence of post-deposition motion. General marked length distributions with unbounded support are not addressed. Monte Carlo measurements are not a proof and cannot exclude undiscovered earlier coverage in literature outside the sources inspected.

## References
1. O. Gromenko, V. Privman and M. L. Glasser, *Random sequential adsorption model of damage and crack accumulation: Exact one-dimensional results*, arXiv:0712.3567, first posted 2007-12-20, https://arxiv.org/abs/0712.3567.
2. N. A. M. Araújo and A. Cadilhe, *Gap-Size Distribution Functions of a Random Sequential Adsorption Model of Segments on the Line*, arXiv:cond-mat/0404422, first posted 2004-04-18, https://arxiv.org/abs/cond-mat/0404422.
