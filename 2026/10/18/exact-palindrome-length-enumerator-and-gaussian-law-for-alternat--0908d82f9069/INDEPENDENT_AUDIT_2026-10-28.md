# Independent mathematical audit

## correctness

PASS

For a binary word u, earliest greedy matching into W_n=0101... has exact final position C(u)=|u|+[u_1=1]+sum_{i}[u_i=u_{i+1}], and greedy matching is optimal by induction. Each palindrome is uniquely one of the two singletons, even vv^R, or odd vcv^R. For nonempty v with length r, initial bit b and e equal-adjacent transitions, there are binom(r-1,e) such half-words and the endpoints are 2r+b+2e+1 and 2r+1+b+2e+2[c=v_r]. Summing these disjoint classes by z^C(u)t^|u|, then multiplying by 1/(1-z), gives exactly tz(1+z)(1+tz²)/((1-z)(1-t²z²(1+z²))). At n=0 the polynomial vanishes; n=1 gives t, and all words are counted once independently of embedding multiplicity. For n=2k or 2k+1, substitution v=z² gives rational series with isolated simple positive pole R(t), where t²R(t)(1+R(t))=1 and R(1)=(sqrt5-1)/2; the negative quadratic pole and pole v=1 have strictly larger modulus near t=1, while numerator amplitudes are nonzero analytic. Uniform simple-pole asymptotics of the moment generating functions show the analytic log quasi-power with h(s)=-(1/2)log(R(e^s)/R(1)), h'(0)=(1+1/sqrt5)/2 and h''(0)=2/(5sqrt5)>0. Differentiation gives the two O(1) moment errors and characteristic-function Taylor expansion proves the Gaussian weak limit. Independent exhaustive enumeration of distinct palindrome WORDS for n=1..16 and a separate formal generating-function coefficient expansion through n=100 reproduced every coefficient; symbolic differentiation reproduced alpha and beta. Finite checks are corroboration, not an infinite proof.

## originality

PASS

Best-of-knowledge originality: the complete two-variable generating function enumerates every length of a distinct scattered palindrome in the fixed alternating binary word, and its analytic dominant pole gives new explicit Gaussian length statistics. Mahalingam–Pandoh (2021) treats the SAME scattered palindrome objects, bounds SP_t and total counts, and lists short extremal words; its inspected full mathematical sections do not give the exact marked generating function or Gaussian law for this alternating family. Müllner–Ryzhikov (2019) discusses longest palindromic subsequence bounds, including alternating words of maximum length n−1, but not counts of all distinct palindrome words by length. The Flaxman–Harrow–Sorkin (2004) abstract treats distinct subsequences without palindrome restriction. Current Resultary searches find related binary subsequence work but no equivalent statement. Failure to find coverage is not proof of absolute novelty; residual risk of an unindexed earlier exact length formula or a stronger theorem persists.

## value

PASS

The infinite alternating binary word is a classical canonical comparator for distinct scattered palindrome enumeration, not an arbitrary length slice. Known total counts and inequalities on length profiles do not determine the full distribution. The exact marked rational series determines every attainable length coefficient for all prefixes, while the nontrivial positive linear variance and Gaussian weak limit quantify the typical length of a uniformly sampled DISTINCT palindromic subsequence. These are natural unknown structural invariants that a future researcher can use as an exact benchmark for broader words, counts versus occurrences, or refinement questions. It is not merely a renaming of a Fibonacci scalar total or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
