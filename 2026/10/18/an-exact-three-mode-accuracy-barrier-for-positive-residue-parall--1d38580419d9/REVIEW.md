# Independent mathematical audit

## correctness

PASS

For nonnegative c,w_j and positive s_j, weights proportional to the first sample r(0) form a probability distribution of u=s/(s+h) together with u=1 for c. The sample ratios obey r(h)/r(0)=E[u], r(2h)/r(0)=E[u/(2-u)]. Strict Jensen gives r(2h)>=r(0)r(h)/(2r(0)-r(h)); monotonicity in the first two samples then forces F(eps,q)=4eps^2+(3-2q+3q^2)eps-q(1-q)^2>=0. The unique positive root E(q) is attained by one positive pole with alternating errors, and the stationary q=1/3 gives E*=(2sqrt(3)-3)/9. Independent SymPy checked root, alternate errors and derivative sign; direct shifted pole s*−1/4>0 establishes SPD example cond=9. Zero approximant, c>=0, arbitrary finite m, 0<q<1 all handled. Not a claim for signed or continuous-spectrum approximants.

## originality

PASS

Best-of-knowledge originality after comparing exact mathematical implications, not titles. Prior shared-pole approximants are a different admissible set; their results neither forbid >95% accuracy for positive-residue sums on the specified triple nor identify equality cases. The Jensen lower bound and exact SPD witness are additional mathematical statements, not just a change of algorithm name.

## value

PASS

Positive-residue shifted inverses are spectrally nonnegative and form a natural parallel matrix-exponential approximation primitive, with entrywise positivity for suitable Stieltjes matrices. The sharp ~5.16% error barrier on an explicit 3-mode PSD spectrum, and ~3.92% on an SPD matrix of condition 9, is a quantitative limitation for every number of positive solves. Exact optimal one-pole and unique worst spacing are structural, not a routine numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
