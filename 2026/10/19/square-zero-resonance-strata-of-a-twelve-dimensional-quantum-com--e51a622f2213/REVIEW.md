# Independent mathematical audit

## correctness

PASS

The grading and ordered monomial basis first force the scalar and both linear coefficients to vanish on the reduced locus. Independent ordered-product collection (python3 /workspace/branches/frozen_math_replay.py 1) gives precisely the three coefficients λb²+(1+λ⁴)ac, (1+λ²)bc, and (1+λ⁴)cd+λ(1+λ)be+(1+λ⁶)af, with the other three coordinates free. Away from the zero of the last coefficient vector one linear constraint cuts out a rank-two bundle, giving L^5([B]+(L−1)[Z]). If u2u4 is nonzero, b=0 and the base is two axes; their rank-zero locus is the origin when u6 is nonzero, or the a-axis otherwise. The generic two punctured-axis closures and the origin fiber are three distinct affine six-spaces; when u6 vanishes the whole a-axis preimage is an affine seven-space containing the origin fiber and leaving one six-space. If u4=0 but u2 is nonzero, u6=1−λ² is nonzero, and b=af=0 gives two seven-spaces meeting in a six-space. For u2=0 in characteristic other than two, c≠0 solves for a,d and gives G_m×A^6; c=0 forces b=0 and gives A^7. Its closure cannot swallow the linear component because λbd−λ(1+λ)ae vanishes on the open, but not at a=e=1 and b=c=0. The open closure is geometrically integral: its coordinate ring embeds into that of the open chart and this injection persists under field extension. In characteristic two, λ=1 leaves just b²=0, and λ≠1 forces u2u4 nonzero with u6=(1+λ³)². These checks give each reported class, all component dimensions and all field cases; point counting specializes the class over finite fields, including extensions. The C source was inspected, not run; its reported finite checks agree with the scope of the calculation and do not prove the geometry.

## originality

PASS

The verified distinction is the five-case geometry and motivic class of the internal reduced square-zero locus for the asymmetric (3,4) algebra. An algebra family, an invariant of its module or cohomology categories, and a cubic analogue are not equivalent to this result. No inspected source covers the exact classification; unavailable material is identified rather than counted as negative evidence.

## value

PASS

For a standard family of finite-dimensional algebras, this is a complete exact geometric invariant in an asymmetric truncation in which three different resonance coefficients can matter. It distinguishes both component sizes and the motivic class across all characteristics, including equal motives for two different component geometries and a sharp characteristic-two dimension increase. These data are useful for comparing degeneration and counting behavior, not merely a check of a handful of parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
