# Independent mathematical audit

## correctness

PASS

For S subset E(K_n) as a total dominating vertex set in T_n=L(K_n), open-edge incidence requires that its spanning selected graph F have at most one isolated vertex and no K2 connected component; all selected edges must meet another distinct selected edge. Inclusion minimality excludes cycles. With no isolate, every component must be P3, since removing a pendant edge from any larger tree creates one permitted isolate without leaving K2. With one isolate, every nonpendant selected edge must cut off a K2 component on one side, forcing component core of nonleaves to diameter <=2, hence a star with arms independently subdivided at most once; at least two arms. Conversely each described forest is minimal. Labeled EGF is exp(z²u³/2)-1-u + u exp(B), B=u(exp(zu+z²u²)-1-zu-z²u²)-z³u⁴/2; the P4 double-hub correction is essential. This yields gamma_t(T_n)=floor(2n/3), upper Gamma_t=2 for n3 else n-2, and the exact n mod 3 minimum-set count formulas in RESULT. Independently enumerated every candidate subset of K_n edges for n=3..6 using actual open-neighborhood total domination plus one-edge deletion minimality, reproducing M3={2:3}, M4={2:12}, M5={3:80}, M6={4:840}. Source n7 output {4:630,5:3402} was not rerun, and finite verification is not substituted for the all-n tree/spider proof.

## originality

PASS

This is inclusion-minimal total domination in the triangular graph, equivalently minimal TOTAL edge domination of K_n using open edge neighborhoods. This differs from minimal ordinary edge domination with closed neighborhoods in Kanté et al. General hypergraph-transversal algorithms, claw-free total-domination bounds, and the polynomial enumerating all (not only minimal) total dominating sets do not imply the full family-specific forest/spider classification or EGF. The full 2003 Favaron–Henning paper and a total-domination-polynomial article were inaccessible; their possible exact specializations are residual risks.

## value

PASS

Determines every inclusion-minimal total dominating set of the highly symmetric triangular graph in a reusable labeled species description and obtains complete size polynomial, min/max cardinalities, and minimum multiplicities. This natural exact invariant is not a routine deduction of generic claw-free inequalities or all-set domination counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
