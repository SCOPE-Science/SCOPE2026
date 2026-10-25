# Independent mathematical audit

## correctness

PASS

Checked the six original cubic-coordinate formulas, their affine parametrization (u,t,v,a,b), exact F=a(u−bv²)+u²+v³ and G=t(1+b²v)+uv+bv³−ab²v² identities, with independent SymPy substitutions. On H=1+b²v nonzero eliminate t, irreducible hypersurface F gives singular support u=v=a=0, t=0. On H=0, v≠0 and explicit inverse parametrization / exact Jacobian minor gives smoothness. At any b=b0, substitutions W=u−bv², U=a+u+bv², Z=v(1+b²v)^(1/3), B=b−b0 are formally invertible, and F=UW+Z³ identically, so completed local ring is A2 surface crossed with smooth 1-parameter line. Jacobian ideal (U,W,Z²) has transversal length two. Normal/rationality are standard for Du Val A2 singularity. These local results do not contradict global nonnormality.

## originality

PASS

Han–Kwak Example 6.2 supplies the same six cubics and identifies global singular support as three lines, but the inspected original Example 6.2 does not classify transverse completed local rings or scheme lengths on the chosen affine line. The local A2 classification is a proper refinement of that singular-set computation.

## value

PASS

Exact, pointwise-uniform analytic type along an actual nontrivial singular stratum of a published degree-eight threefold; determines normal/rational local behavior and nonreduced Jacobian transverse thickness, a structural invariant rather than merely redoing singular support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
