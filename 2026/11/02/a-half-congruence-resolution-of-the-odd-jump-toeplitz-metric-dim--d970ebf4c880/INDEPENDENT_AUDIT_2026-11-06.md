# Independent mathematical audit

## correctness

PASS

Reconstructed the finite-interval distance as F_b(qb+r)=q+min(ceil(r/2),1+ceil((b-r)/2)), with positive-step and overshoot-backtrack constructions respecting interval boundaries. F_b(d+b)=F_b(d)+1 and the explicit k-dependent residue pair table show injective signatures from {0,1,2k+1}, including special i=0 and 1<=i<2k+1 cases. For lower bound, all interior vertices have degree>=4, so a 2-landmark basis can only be the two degree-3 endpoints; when n=b+2 vertices 1,b collide, and when n>=b+3 six vertices at distance 2 to left endpoint have at most five second-coordinate distances. Independent separately written BFS checked 276,612 ordered graph distances across 4k+1 jumps k=3..14 and diverse n, resolution and endpoint-pair failure; infinite claim follows from the proof, not the experiment.

## originality

PASS

Nadeem–Qu–Ahmad–Azeem (2022) explicitly conjecture the odd-jump three-generator case and prove an even-jump subfamily; 2019 same-family work treats only smaller generator values, and partition dimension is not graph metric dimension. The all-length congruence b=1 mod4 solution is not directly covered by sources compared. A later 2025 broad review was not accessible in full and could contain this exact proof.

## value

PASS

Proves an infinite congruence subfamily of a specifically published open conjecture, with a uniform explicit basis and a nontrivial boundary-independent graph metric. It is neither a finite table nor a parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
