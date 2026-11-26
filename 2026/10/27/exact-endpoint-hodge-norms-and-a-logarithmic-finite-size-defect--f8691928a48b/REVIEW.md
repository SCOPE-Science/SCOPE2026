# Independent mathematical audit

## correctness

PASS

For the indicated orientations L=(3I+S+S^{-1})(2I-S-S^{-1}); periodizing q^{|j|}/sqrt(5) solves the first factor's dipole-kernel calculation (the kernel itself solves the delta source), with mass 1/5. Convolving the centered cycle path current gives the two signed current rows for each edge type. Both rows sum to zero, and passing from Q to I-Q replaces just a positive diagonal R in (0,1) by 1-R. The five selected positive long-edge entries yield A2 >= 2+2K0-32/(5n); subtracting the short-edge geometric upper bound and then 2(R2-R1) yields the stated strict cut comparison for n>=17 and strict cycle comparison for n>=36. Separately reconstructed both full columns from the grounded graph Laplacian at every n=7..35 and matched the resolvent entries exactly; the minimum margins were 12/91 and 8/91, both at 7. Replay: python3 /workspace/branches/frozen_math_recheck.py 2. For each long-edge row its two positive geometric tails have ratio r^2 and jointly contain log(n)/log(1/r)+O(1) entries above the baseline; the discarded tail mass is O(1/n). Periodization alters the centered-representative sums by at most an exponential tail in absolute mass, since positive part is 1-Lipschitz. Doubling the losses for baselines 2/(5n) and 4/(5n) gives the common coefficient 12/(5 log(1/r)); the zero-baseline mass and diagonal limit give the stated constants. Symmetry gives equality of the induced real 1 and infinity norms. The frozen script was read, not run.

## originality

PASS

On available evidence the distinct result is the simultaneous strict orbit comparison and exact absolute-current endpoint norms, including the squared-cycle logarithmic defect and coefficient. The electrical data and general projection framework are prior; related logarithmic defects on other cyclic graph families preclude a claim of novelty for the phenomenon in general.

## value

PASS

The square of a cycle is a natural first nontrivial cycle power. The diagonal correction makes cut and cycle maximizers genuinely separate tests. Proving both strict maxima for all admissible sizes, and explaining the logarithmic defect via the number of geometric entries above a moving threshold, gives an exact benchmark beyond a resistance formula or a limit alone. The scope is canonical projections, not minimal projection constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
