# Independent mathematical audit

## correctness

PASS

Let F have degree n>=2 and finite p>2. Zhang 2026 establishes h(F,F′)<=sigma_2(F), while normalized power-mean monotonicity gives sigma_2<=sigma_p. If h=sigma_p, all inequalities are equal. Choose a p-minimizing center c_p; since sigma_2<=((sum |z_j-c_p|²)/n)^1/2 <=((sum |z_j-c_p|^p)/n)^1/p=sigma_p, strict power-mean equality for p>2 forces all distances |z_j-c_p|=R. If R=0, F=A(z-c)^n. If R>0, affine rescaling puts all zeros exactly on the unit circle and h(F,F′)=1. The finite zero set contains an extremal boundary zero with no critical point at distance <1. Phelps--Rodriguez/Rubinstein boundary rigidity forces the polynomial to be a rotated scalar (z^n-1), hence F=A(z-c)^n-B. Conversely roots of this form are a regular n-gon or all coincide, critical set is central and sigma_p=R by strict convexity/rotational symmetry. The only nontrivial inputs are the valid global p=2 bound and the already-proved boundary equality theorem; not an independent proof of these deep theorems, and Zhang full paper unavailable this run.

## originality

PASS

Khavinson--Pereira--Putinar--Saff--Shimorin 2011 primary arXiv:1010.5167 p3 Conjecture 2 explicitly asks for same equality characterization for p>1 and proves only restricted cases. Zhang arXiv:2610.02035 2026 abstract establishes all-degree p=2 inequality (with Lean formalization) and general p>=2 inequality then follows by monotonicity; its available summary does not announce finite superquadratic equality classification. Resolved Rubinstein endpoint theorem classifies special unit-boundary polynomials but requires same-radius roots, supplied here by strict p-mean equality. The exact bridge is short but a valid conjecture resolution in p>2. Full Zhang text inaccessible and could contain equality discussion not in abstract, so explicit stronger-coverage risk remains.

## value

PASS

Classifies equality for every degree and every finite p>2 in an explicitly named long-standing extremal conjecture; exact equality cases are useful even when numerical bound follows monotonically from p=2. This is a substantial gap because strictness of moment monotonicity and a boundary rigidity theorem must be linked, not only renaming a known inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
