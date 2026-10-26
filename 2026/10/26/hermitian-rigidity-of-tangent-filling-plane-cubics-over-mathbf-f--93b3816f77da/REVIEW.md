# Scientific assessment: tangent-filling cubics over \(\mathbf F_4\)

## Correctness — PASS
The coefficient space consists of exactly \((4^{10}-1)/3=349525\) scalar-normalized nonzero cubics; the provided finite search enumerates each. The tangent criterion evaluates the cubic, homogeneous gradient, and its tangent line at each of the 21 rational points. The factor criterion uses the fact that a degree-three form on a projective rational line cannot vanish at its five rational points unless the line divides the form. The 280 no-line candidates agree exactly with the complete 280-element projective orbit of the explicitly smooth Hermitian cubic. Independently, the Jacobian-quadrics degree-four rank criterion confirms exactly 280 geometrically smooth tangent-filling cubics. The C++ and vectorized Python incidence enumerations agree coefficient by coefficient.

## Originality — PASS, with stated bibliographic limits
The closest identified source, Asgarli–Ghioca (arXiv:2302.13420), introduces tangent-filling curves and exhibits the Hermitian construction. Its displayed main results concern large-field obstructions and examples; this does not imply that every \(\mathbf F_4\) tangent-filling cubic without a rational line component is Hermitian, nor the exact exceptional count. Classical Hermitian-unitals theory gives the 280-element orbit once the example is fixed, but does not establish exhaustion among tangent-filling cubics. Known characterizations of Hermitian curves from extremal rational point counts have different hypotheses. Relevant semantic-record and literature searches produced no equivalent rigidity statement. The remaining risk is an earlier small-field classification not indexed or not fully accessible; the source assessment does not claim that search silence proves priority.

## Value — PASS
This is an exact classification for the first nontrivial square field and the first positive-genus plane degree relevant to tangent-filling. It identifies a rigidity phenomenon under an incidence-covering hypothesis, strengthened to cover all cubics with no rational linear component, rather than merely recounting Hermitian cubics. The exclusion of all other irreducible cubics is a mathematically natural boundary case in finite-field tangent geometry.

## Scope and limits
The conclusion does not extend to arbitrary finite fields or degrees. The proof is finite and computationally exhaustive, supported by stand-alone checker source and full exact-arithmetic certificates. The literature-priority conclusion is conditional on the accessible primary literature and record searches, not independent exhaustive bibliography. The computational and scientific review is not a separate external validation.

Self-review: passed. Independent audit: not yet performed.
