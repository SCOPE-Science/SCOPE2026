# A universal finite-horizon ordering theorem for two-species recruitment lotteries

## Finding

For the deterministic two-species territorial lottery with a **common fixed adult replacement fraction** \(0<\delta<1\), the fraction \(x\in(0,1)\) of sites occupied by the focal species responds to a season with positive relative recruit production \(r\) through
\[
F_r(x)=(1-\delta)x+\delta\frac{rx}{1+(r-1)x}.
\]
Fix any integer \(n\geq2\), a starting fraction \(0<x_0<1\), and an arbitrary multiset of \(n\) positive seasonal ratios. Across **all \(n!\) permutations** of those seasons, the focal species' **final** occupancy is maximized by the following chronological arrangement:

1. all ratios strictly below \(1\), in decreasing numerical order;
2. all ratios strictly above \(1\), also in decreasing numerical order.

The minimizing arrangement reverses this sequence: above-\(1\) ratios in increasing order, then below-\(1\) ratios in increasing order. Ratios equal to \(1\) may be inserted anywhere and repeated ratios may be interchanged. Except for those harmless exchanges, each optimum is strict. Neither arrangement depends on \(x_0\), \(\delta\), or the number of seasons. At \(\delta=1\), every ordering instead gives the same final occupancy.

## Assumptions and scope

In each discrete season the adult population occupies a fixed total number of sites. The two species experience the same season-independent adult mortality/replacement fraction \(\delta\). The remaining sites are filled immediately by recruitment in proportion to the two species' positive per-adult recruit outputs \(R_{1,j}\) and \(R_{2,j}\); define \(r_j=R_{1,j}/R_{2,j}>0\). There is no immigration, stochastic finite-site extinction, density dependence beyond the recruitment lottery, or species-specific mortality. A season's ratio is a prescribed external input independent of the current species frequencies. Objective: maximize/minimize focal-species occupancy exactly after the \(n\)-th season, not a cumulative yield, stochastic persistence probability, or long-run coexistence. Chronological composition \((a,b)\) means \(F_b(F_a(x))\).

## Proof

For \(0<\delta<1\) and \(r>0\), \(F_r\) maps \((0,1)\) strictly into itself and is strictly increasing, since
\[
F'_r(x)=1-\delta+\delta\frac{r}{[1+(r-1)x]^2}>0.
\]
For any two ratios \(a,b>0\) and \(0<x<1\), put
\[
A=1+(a-1)x,\quad B=1+(b-1)x,\quad
E=AB+\delta(a-1)(b-1)x(1-x).
\]
The common denominator factor is strictly positive: direct substitution gives
\[
E=A\{1+(b-1)F_a(x)\}
 =B\{1+(a-1)F_b(x)\}>0.
\]
Putting the two rational compositions over the positive denominator \(ABE\) and collecting terms gives the exact commutator identity
\[
F_b(F_a(x))-F_a(F_b(x))=
\frac{\delta^2(1-\delta)(a-b)(a-1)(b-1)x^2(1-x)^2}{ABE}.
\tag{1}
\]
This identity has no exceptional interior states, and its sign depends only on the two season ratios. For \(a>b\), doing \(a\) before \(b\) strictly increases final occupancy when \(a,b\) lie on the same side of \(1\); it strictly decreases final occupancy when \(b<1<a\). Swapping a neutral season \(r=1\) makes no difference, because \(F_1\) is the identity.

Consequently every strict improvement of a neighboring chronological pair moves the list toward the total order: decreasing ratios in \((0,1)\), followed by decreasing ratios in \((1,\infty)\). Importantly, the sign in (1) holds for the occupancy **arriving at that pair**, while every downstream seasonal map is strictly increasing. Therefore an improving local swap strictly improves the final occupancy even when surrounded by other seasons. The usual finite adjacent-interchange procedure removes all inversions and reaches the stated maximum; reversing every such comparison yields the minimum. Every other ordering of unequal nonneutral seasons has an inversion and a strictly improving swap, proving strict optimality modulo repeated and neutral seasons. If \(\delta=1\), each \(F_r(x)=rx/[1+(r-1)x]\) multiplies the occupancy odds by \(r\), so all maps commute and all orders tie.

## Verification

Run `python3 verify.py` using only the Python standard library. It checks (1) using exact rational arithmetic on 2,500 randomly selected parameter tuples, and exhaustively compares all permutations for 170 further randomly generated instances of lengths \(3\) through \(6\). The program verifies 12,643 exact assertions in total and checks the following rational example. With \(\delta=x_0=1/2\) and seasonal multiset \(\{1/3,2/3,3/2,3\}\), the maximum at chronological order \((2/3,1/3,3,3/2)\) equals
\[
\frac{43307611041}{83947961440},
\]
whereas the minimum at order \((3/2,3,1/3,2/3)\) equals
\[
\frac{40640350399}{83947961440}.
\]
The exact occupancy difference is \(1333630321/41973980720\), approximately \(0.0317727863\). These calculations are supplementary: arbitrary \(n\) and all real admissible parameters are handled by the proof, not by enumeration.

## Relationship to prior work

Chesson and Warner (1981) introduced the lottery explanation of fluctuation-mediated coexistence in territorial competitors; Warner and Chesson (1985) developed the storage-effect interpretation. The recurrence above is their two-species lottery rule with equal adult replacement and deterministic prescribed recruitment ratios. Cheng, Chesson and Han (2021), Section 2, explicitly write the general two-species update but study nonstationary stochastic environments through diffusion, stochastic differential equations and Fokker–Planck equations. Stump and collaborators (2022), subsection 'Model 2: The storage effect,' discuss the same recruitment fraction in trait-dependent coexistence. Those works supply the ecological model, not the finite-horizon universal permutation statement (1) and its global sorting conclusion as stated in the inspected material. Adjacent interchange is a general mathematical method; its applicability here depends on the specific factorization and its sign across \(r=1\).

## Limitations

This is a deterministic infinite-site frequency description, not a claim about stochastic finite population extinction, expected random occupancy, equilibrium coexistence, or optimal scheduling with seasonal mortality varying between periods. It assumes the same replacement fraction in every season, strictly positive recruitment, and one finite-horizon terminal-frequency objective. When \(x_0\) equals \(0\) or \(1\), all schedules tie; when \(\delta=1\), all schedules tie. The original 1981 and 1985 complete articles were not accessible for full-text comparison. Although no identical finite-horizon sorting theorem was located, an older treatment of seasonal ordering or a more general nonlinear-map rearrangement theorem could subsume the result; originality thus requires further independent literature evaluation.

## References

- P. L. Chesson and R. R. Warner, 'Environmental Variability Promotes Coexistence in Lottery Competitive Systems,' *The American Naturalist* 117 (1981), 923–943, first public article date June 1, 1981, DOI: 10.1086/283778.
- R. R. Warner and P. L. Chesson, 'Coexistence Mediated by Recruitment Fluctuations: A Field Guide to the Storage Effect,' *The American Naturalist* 125 (1985), 769–787, DOI: 10.1086/284379.
- J. Cheng, P. Chesson, and X. Han, 'The Lottery Model for Ecological Competition in NonStationary Environments,' *SIAM Journal on Applied Mathematics* 81 (2021), 2480–2502, DOI: 10.1137/20M1357858, especially Sections 2–4 and closing remarks.
- S. M. Stump, C. Song, S. Saavedra, and J. M. Levine, 'Synthesizing the effects of individual-level variation on coexistence,' *Ecological Monographs* 92 (2022), e01493, DOI: 10.1002/ecm.1493, 'Model 2: The storage effect.'
