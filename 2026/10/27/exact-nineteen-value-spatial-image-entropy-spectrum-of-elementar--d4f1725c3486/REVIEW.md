# Independent mathematical audit

## correctness

PASS

For each of the 256 Wolfram radius-one binary maps, finite spatial image words are exactly labels of paths in a 4-pair-state de Bruijn transducer. Determinization from all four initial states to reachable nonempty subsets (<=15) counts every output block once, so a(n)=e_initial^T A^n 1. Accessibility and nonnegative Perron–Frobenius theory yield exp(h)=rho(A); all row sums <=2. Independent Python/SymPy exact reconstruction built all 256 matrices and characteristic polynomials, used rational Sturm root counts in 19 pairwise-disjoint intervals and exact factor divisibility to identify every Perron class. The class counts are [30,4,4,8,8,4,8,8,4,4,28,44,16,8,8,32,28,8,2]; highest proper class is rules 22,104,151,233, runner-up 37,91,164,218, zero class 0 and 255. Independent input-block enumeration agreed with deterministic counts at 1536 finite (rule,n) pairs. Actual source CSVs were independently fetched by Git blob and inspected as 20 and 257 rows, including exact rational brackets and characteristic polynomials. The infinite word-length entropy is from the matrix-growth proof, not finite samples.

## originality

PASS

Li–Packard classify ECA structural/mean-field features; Schüle–Stoop provide topological-dynamical/surjectivity classes; Kari–Taati Garden-of-Eden entropy theorem establishes full-image entropy dichotomy; Martínez et al. give Rule 22 de Bruijn/subset diagrams and forbidden patterns. None of the materially inspected results evaluates all 19 one-step spatial-image entropies with exact isolated Perron roots and global Rule-22 four-rule optimum. Older entropy rankings based on Shannon time-series or asynchronous update are different metrics. Resultary queried the all-256 one-step image problem and returned temporal automata and specific-rule dynamics rather than complete spectrum. A prior unindexed 256-rule subset-automata table remains a real novelty risk.

## value

PASS

A complete intrinsic entropy spectrum and exact rule classification for the canonical 256 elementary CA family is a natural finite classification, not an arbitrary slice. It resolves both the number and order of possible image-shift entropies, the proper-image maximizers and strict entropy gap, supplying precise topological-dynamical invariants beyond surjectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
