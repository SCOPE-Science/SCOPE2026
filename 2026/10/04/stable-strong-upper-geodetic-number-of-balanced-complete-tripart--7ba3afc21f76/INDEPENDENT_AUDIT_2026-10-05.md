# Independent mathematical audit

## correctness

PASS

For selected counts \(s_i\), omitted demands \(t_i=n-s_i\), and same-part pair capacities \(p_i=\binom{s_i}{2}\), shortest-path coverage is exactly a three-class bipartite allocation problem. Hall reduces to \(T\le P\) and \(t_i\le P-p_i\) for all three classes, because any demand subset meeting two partite classes sees all three pair-slot classes. The displayed inequalities then prove that \((2,2,n-2)\) is minimal strong geodetic and that every larger strong set admits a one-vertex deletion; the equality argument leaves only \((2,2,n-2)\). I independently reimplemented the Hall criterion and one-vertex minimality test, recovering the stated value and exactly three maximum patterns at every tested stable-range value, including \(n=12,13,14,15,20,30,40\). The packaged max-flow verifier was read and exhaustively checks all part-count triples for \(12\le n\le30\); finite checks are corroborative only.

## originality

PASS

The defining 2021 paper introduces the strong upper geodetic number but no complete-tripartite exact formula was located. The ordinary strong-geodetic literature on complete multipartite graphs optimizes a different minimum parameter. The closest published SCOPE result solves only complete bipartite graphs; moving to three parts creates a genuinely different three-demand/three-slot Hall system. Resultary exact searches found no theorem implying the stable value, equality classification, or count.

## value

PASS

Passing from two to three partite classes changes the covering problem into a genuine three-class allocation system. The theorem gives an infinite stable exact value, a full structural classification of extremal minimal sets, and an exact count, which is a natural benchmark for the upper geodetic parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
