# Independent mathematical audit

## correctness

PASS

The smoothness boundary follows from the partial derivatives: with precisely two nonzero coordinates the corresponding parameter square is 4; with all three nonzero the symmetric linear system on their squares has diagonal 2, off-diagonals r,s,t, and determinant −2(r²+s²+t²−rst−4). When the two-coordinate minors are nonzero, a kernel vector of this matrix has all coordinates nonzero and gives a singular projective point over the algebraic closure. The known quotient isogeny has degree 8, so the 5-torsion splits, and the elliptic quartic Hasse coefficients are 2H_i. Independently the diagonal plane-quartic Hasse–Witt entries are the coefficients of X⁸Y⁴Z⁴ and its cyclic analogues in F⁴, which are 2H_i; the off-diagonal monomials have odd exponents and cannot occur. Each vanishing coefficient gives one more unit of a-number and one fewer unit of 5-rank. H_1−H_2 factors as −2(r²+1)(t²−s²) and the first nonconstant factor is invertible on the smooth locus; the signed substitutions give the two displayed linear equations for r after removing r=±2. Clearing denominators gives the stated exclusions, and the s-coordinate is a regular inverse on each graph. At a common zero all squares are q; the Hasse equation gives rst=q²+2. Squaring the product gives (q+1)²(q²+2q−1)=0. The excluded root is q=4; the two other roots are distinct and nonzero, with four admissible sign triples apiece and final discriminant −7≠0. Each triple belongs to one graph for each of the three Hasse pairs; same-pair graphs are disjoint. Substituting on a graph gives the two admissible quadratics u²±2u−2 with four distinct roots, so the graphs for different pairs do not coincide and each has four triple incidences. Independent replay: python3 /workspace/branches/check_2.py computes Hasse–Witt entries by enumerating monomials and compares all smooth F_25 parameters to the graph images. It obtains a=0,1,2,3 counts (10469,1110,96,8). Algebraic elimination, not enumeration, proves completeness over the algebraic closure.

## originality

PASS

The classical family, smoothness criterion, elliptic quotient decomposition and superspecial criterion are credited; the explicit Hasse computation specializes prior machinery. The supported distinct contribution at the frozen record's position in catalogue chronology is the full intermediate-rank geometry, not a prior superspecial isomorphism-class count. There is demonstrably equivalent geometric coverage in a separate later-dated catalogue record and arithmetic overlap in another. This is not a claim of present uniqueness or of priority based on a date alone; neither latter passage gives antecedent evidence or establishes the relationship between the records.

## value

PASS

This gives the intermediate rank degeneration, not just the smoothness boundary or the well-studied all-supersingular points, for a natural genus-three split-Jacobian family. An explicit parameter domain and component incidence in the marked space give useful test geometry for specialization and finite-field counting of rank-one parameters. It is a complete exact stratum, not merely solving for an isolated example or extrapolating the F_5 counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
