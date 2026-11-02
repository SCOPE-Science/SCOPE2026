# Independent mathematical audit

## correctness

PASS

For J(n,k) with n>=2k>=6, two distinct marked vertices A,B, refinement of singleton colors determines both Johnson distances by round k and hence x=|S∩A|, y=|S∩B|. Partition ground set into C=A∩B (c=k-r), P=A\B (r), Q=B\A (r), D=outside (e=n-k-r). For a vertex profile (a,b,h,d), counts of neighbors increasing or decreasing both x,y equal f=d(c-a), g=a(e-d), with f-g=c(k-x-y)+(2k-n)a. If n>2k this uniquely gives a and the entire four-block profile; if n=2k the quadratic for f gives exactly profile a and c-d, exchanged by an explicit complement-permutation automorphism fixing both markers. Four-block permutations act transitively on single profiles, so no color split beyond these orbit classes; the exhibited complement symmetry proves the balanced pairing. Feasible profile polynomial and Burnside yield exact number and size of final classes. The bound k+1 is an upper bound, not purported tight. Independent check: Independent construction of each labeled Johnson graph and simultaneous 1-WL updates checked for (n,k,r)=(6,3,1),(6,3,3),(7,3,1),(7,3,2),(8,4,1),(8,4,2),(9,4,2); independently computed 4-block profiles, balanced complement pairing and counts. The source also has two distinct verifier implementations, 91 exhaustive parameter triples and 30 group-orbit small cases, but only stated independent cases were replayed here.

## originality

PASS

Automorphism groups of Johnson graphs and the J(n,2) Tinhofer property are established. Arvind–Köbler–Rattan–Verbitsky prove an all-individualization rank-two theorem; this neither covers k>=3 nor automatically proves that exactly two markers recover stabilizer orbits in all higher ranks. The explicit balanced complementation quotient and complete class sizes are independent of rank-two statements. Older two-anchor equitable partition results might cover it; qualified priority.

## value

PASS

Higher-rank Johnson graphs are a standard association-scheme benchmark for color refinement and finite-variable counting logic. Exact two-marker orbit recovery for every n,k, the balanced exception and complete counts classify precisely what two-variable counting logic can separate, without overstating a general Tinhofer theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
