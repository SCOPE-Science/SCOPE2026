# Independent mathematical audit

## correctness

PASS

For n>=5, J>0, neutral flips admissible, consider all flip subsets of size <=3 including disconnected sets and the hub. The single-spin energy increments imply exactly the cyclic rim constraints no AA and no BBB; the hub flip remains nonnegative since m<=n/2. The exact simultaneous-flip internal-edge correction shows any two-spin flip has nonnegative cost. Exhausting connected rim triples and hub-plus-two triples leaves a negative change of -2J precisely for rim BAB with both B endpoints belonging to distinct BB runs, i.e. BBABB. Writing stable words as m blocks AB/ABB and j=n-2m long BB gaps yields count Z1=Z2=2 sum(n/m) binom(m,j)y^m; excluding adjacent long gaps yields Z3=2 sum (n/(m-j)) binom(m-j,j)y^m for 2j<=m. Transfer determinant 1-yz²-y²z⁵ and aperiodicity give log beta entropy with beta^5=beta^3+1 instead of log alpha with alpha^3=alpha+1. Independent direct evaluation of the raw Ising Hamiltonian for all 4032 spin assignments at n=5..10 and every one-, two-, three-spin flip verified classifications; at n=6 totals (10,10,4). Independently inspected packaged verify.py logic; bounded checks do not imply all n.

## originality

PASS

PASS for the exact BBABB cooperative obstruction, graded count, and distinct entropy, excluding already-known one-spin Perrin cyclic-word baseline. Newman--Stein general M-flip stability in disordered lattice models and Wacław--Burda random-bond one-spin minima do not state the homogeneous wheel three-flip formula. An unindexed special wheel or staggered-field formulation could in principle be equivalent.

## value

PASS

Homogeneous antiferromagnetic wheels are canonical frustrated graphs with a hub coupling all rim spins. Identifying exactly the first cooperative metastability obstruction, all energy-resolved surviving counts and a positive thermodynamic entropy loss is a motivated complete classification rather than routine reuse of a known one-spin word count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
