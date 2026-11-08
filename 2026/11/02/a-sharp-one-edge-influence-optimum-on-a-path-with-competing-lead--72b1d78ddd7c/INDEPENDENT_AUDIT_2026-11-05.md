# Independent mathematical audit

## correctness

PASS

Harmonic equilibrium on a unit-resistance path with opposing fixed endpoint voltages 0 and 1 is unique by grounded Laplacian positive definiteness. For any chord a<b of length d>=2, series/parallel replacement of the segment d by d/(d+1) yields F=L(d+1)-d^2, explicit piecewise linear potentials, and total gain Delta=d^2(a+b-L)/(2F). Fixing length d makes Delta strictly increase with a, so the unrestricted optimum must have its right endpoint at leader L; the opposing-leader chord a=0 has zero gain. Maximizing f_L(a)=a(L-a)^2/[2(L+a(L-a))] is a one-variable unimodal problem: derivative sign of cubic P_L(u)=L^2-3Lu-Lu^2+u^3 has one zero alpha in (0,L), so floor/ceil alpha (clipped) give all integer optimal edges. Expansion alpha=sqrt L-1+O(L^-1/2) proves gain L/2-sqrt L+O(1) and mean 1-1/sqrt L+O(1/L). Independent exact rational grounded-Laplacian solves and all-chord optimization for L=3..29 corroborate the gain and endpoint property.

## originality

PASS

Bounded best-of-knowledge scientific comparison: The prior monotone-submodular approximation on restricted candidate sets is not an exact solution over all nonedges. Adding a chord between two followers is admissible here and must be excluded by a new monotonic-at-fixed-length argument. The source also does not state the cubic, integer maximizers or asymptotic square-root placement. The targeted Resultary query and primary works were compared on objects, hypotheses, implication and parameters, not simply titles. No decisive prior-coverage theorem identified; this is not a proof of historical priority.

## value

PASS

The equilibrium edge-addition problem is natural in harmonic opinion propagation with two competing boundary leaders. Proving that *every* unrestricted optimal new chord touches the promoting leader is a nontrivial structural insight, and exact optimal placement at distance sqrt L and near-unanimous average quantify a strong network-sensitivity phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
