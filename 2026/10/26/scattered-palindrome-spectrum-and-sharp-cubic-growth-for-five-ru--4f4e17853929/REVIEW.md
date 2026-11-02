# Independent mathematical audit

## correctness

PASS

Every palindromic scattered subsequence string with at most five runs has one, three or five constant runs. Separate two monochromatic families, 1-0-1 with i<=min(b,d), middle zero count <=c, the five-run 0-1-0-1-0 family (outer i<=min(a,e), middle one j<=min(b,d), inner zero k<=c), and 0-1-0. For 0-1-0, i<=E permits up to b+d internal ones; larger i uses the first or second one-run exclusively, bounded by A and B. The identity min(A,B)=E makes these regions disjoint, establishing coefficients and the exact sum over distinct strings rather than embeddings. Only E*T*c is cubic; 2E+2T+c<=n yields ETc<=n^3/108 by AM-GM, with other terms O(n^2). The (m,m,2m,m,m) construction reaches the coefficient; stability of AM-GM and vanishing unused lengths establishes iff rigidity. Up to four runs cannot have five-run palindromes, hence O(n^2). Independently enumerated 243 five-tuples by actual distinct subsequence sets and verified entire length spectra. These are finite consistency tests, not the asymptotic proof.

## originality

PASS

The primary finite-word counting literature provides general scattered-palindrome bounds, reconstruction, and longest-length criteria but does not yield the five-run coefficient-by-coefficient spectrum or the first sharp cubic run-threshold with limiting shape. This is a best-of-knowledge assessment, not priority certification.

## value

PASS

Five runs is the first natural run-complexity threshold permitting three independent positive exponent choices in a palindromic subsequence, while at most four runs remains quadratic. The exact full length spectrum, cubic constant, and rigidity classify a structural extremal phenomenon; no unrelated downstream theorem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
