# Independent mathematical audit

## correctness

PASS

Automorphisms are independent row and column permutations. A finite base fixes precisely its r used rows and c used columns, so counting ordered potentially repeated cells involves two distinguished-block partition polynomials a_h(r),a_h(c). Inclusion–exclusion removes the m individually named cells, and signed Stirling inversion excludes repetitions among k new cells. Therefore t_k=sum_{j<=k} s(k,j) sum_{i<=j}(-1)^i C(j,i)m^i a_{j-i}(r)a_{j-i}(c). In particular t1=(r+1)(c+1)-m and t2=t1(t1-1)+(r+1)^2+(c+1)^2+1. With known m these recover product and sum of squares of r+1,c+1, hence unordered supports. Distinct shapes with (m,r,c)=(4,2,3), row-degree patterns (3,1) versus (2,2), are not isomorphic under named E,F but share all t_k. Bipartite 1,2,3-edge shapes have no distinct full-support patterns with the same ordered (r,c), proving sharpness. For two rows and n named points, a family of degree partitions produces floor((n-1)/2)+1 inequivalent bases with identical spectra. Independent Stirling–Bell computations reproduce t0..t4=(1,8,82,1067,17108). Only numerical counts are identified, not equality of complete types over named bases.

## originality

PASS

Cameron 2000 already describes oligomorphic orbit sequences, Bell-number orbit transforms, and product actions; Applegate–Cameron establishes growth bounds for orbit sequences. These are credited as the general machinery. The complete fixed-finite-base arity-two determination and sharp nonisomorphic incidence-graph collisions with an unbounded family are not given by the inspected general results. The collision is not a conclusion from equality of titles: the same stabilizer type counts are computed from the exact ordered row/column support. Risk remains that a standard orbit-profile characterization of the two-equivalence grid appears in an older model-theory thesis.

## value

PASS

The theorem precisely distinguishes what numerical type spectra can and cannot recover in a canonical omega-categorical structure: unordered support sizes are identified by arity two, but the graph of incidences inside that support is invisible even to the entire sequence, with arbitrarily many witnesses. This is a motivated model-theoretic reconstruction/collision invariant and a sharp first finite obstruction, not a one-off Bell computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
