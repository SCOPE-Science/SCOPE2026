# Empty tilt wall at beta = -1/2 for the line-ideal projection class on a Brill–Noether-general ordinary Gushel–Mukai threefold

## Result

Let X be a Brill–Noether-general ordinary Gushel–Mukai threefold with H^3=10 and tautological rank-two bundle E, and let I_L be the ideal sheaf of a line. For the left projection `pr = L_E o L_O`, the truncated Chern class of `pr(I_L)` is

`M = (-3, 2, -3)`.

It is primitive and has Euler square -2 in the genus-six Kuznetsov lattice. At beta=-1/2 there is no numerical tilt wall for this class for any alpha>0. Indeed, for every integral numerical class `(n0,n1,n2)`,

`Im Z_{alpha,-1/2} = 10 n1 + 5 n0`

is a multiple of 5, whereas `Im(M)=5`. A finite-slope Jordan–Hölder decomposition of M would require two nonzero positive imaginary parts summing to 5, which is impossible. A factor of imaginary part zero has infinite tilt slope and cannot have the same finite slope as M. Thus a tilt-semistable object of class M cannot be strictly semistable on this vertical ray.

## Numerical checks

Hirzebruch–Riemann–Roch gives `chi(O_X,I_L)=0` and `chi(E,I_L)=2`, hence `[pr(I_L)] = [I_L]-2[E]` and `(1,0,-1)-2(2,-1,1)=(-3,2,-3)` in truncated coordinates. With the genus-six Gram matrix `[[-2,-3],[-3,-5]]`, the corresponding lattice vector has square -2.

The independent audit rechecked these identities and the divisibility argument.

## Limitations

This is a numerical wall-exclusion statement on the fixed line beta=-1/2. It does not by itself prove existence of an object of class M in the tilt heart. Any transfer to a Serre-invariant Bridgeland-stable object uses the standard double-tilt construction and is conditional on the usual hypotheses. No claim is made for special/singular GM threefolds or other beta values.

## Reproducibility

From the record directory run `python3 artifacts/verify_target.py`; the script uses exact/stdlib arithmetic and prints `VERIFY_OK`.

## References

- A. Jacovskis, Z. Liu, S. Zhang, *Brill–Noether reconstruction of index one prime Fano threefolds*, arXiv:2207.01021.
- *Categorical Torelli theorems for Gushel–Mukai threefolds*, arXiv:2108.02946.
- O. Debarre, A. Kuznetsov, *Gushel–Mukai varieties: classification and birationalities*, arXiv:1510.05448.
- A. Perry, L. Pertusi, X. Zhao, *Stability conditions and moduli spaces for Kuznetsov components of Gushel–Mukai varieties*, Geom. Topol. 26 (2022).
