# Independent mathematical audit

## correctness

PASS

For each binary circular word, length-three counts form a nonzero balanced integral circulation on the order-two de Bruijn digraph. Conversely, connected positive support gives an Euler circuit (including wraparound n=1,2). Balance forces g001=g100=t and g011=g110=u, and g010−g101=t−u, uniquely giving g010=(t−u)_++j and g101=(u−t)_++j, j≥0. The total length is a+h+3max(t,u)+min(t,u)+2j. Connectivity splits exhaustively into (t,u>0), (t>0,u=0,h=0), (t=0,u>0,a=0), (t=u=0,j>0,a=h=0), and the two pure-loop choices when t=u=j=0. The five contributions sum exactly to the supplied rational generating series. At z=1 the high-order term is (1/12)(1−z)^−5, and all other unit-circle poles have order <5, giving n^4/288+O(n^3). The zero-error capacity equality is the exact count of distinguishable profile outputs. Independently enumerated all 2^n binary words n=1..16, all balanced connected nonnegative eight-flow vectors for n=1..10, GF coefficients through n=35, and a nonconjugate n=6 collision; no finite computation is being substituted for the all-n proof. Git tree recomputed from seven real blob identities.

## originality

PASS

Best-of-knowledge PASS for the *exact* all-n binary circular trigram profile generating series and its sharp coefficient 1/288. The strongest newly inspected same-object primary source, Arnoux 2016, already proves the de Bruijn Kirchhoff constraints and the Eulerian connected-support criterion, and so these ingredients are known; it does NOT enumerate nonnegative connected integer flows at each length. Cassaigne et al. DLT 2016 gives a different exact *linear* k=3 class formula of degree six, not this cyclic degree-four count. The target five-case support census supplies nontrivial fixed-length enumeration beyond these premises. Exact-priority uncertainty remains, especially unindexed Markov-type results and the uninspected extended 2017 journal version.

## value

PASS

The natural cyclic length-three read histogram is a lossy observation channel on circular binary words. Exact attainable-output counts determine the optimal zero-error one-shot code size for each n, a complete intrinsic enumeration rather than a tiny arbitrary instance. The explicit rational series, quartic rate and coefficient 1/288, and the n=6 departure from necklace counts quantify achievable resolution. This exact integer-flow count is not a routine quoted linear-class table or merely the known Eulerian feasibility criterion; finite exact invariant of a natural infinite object family merits mathematical use independently of any later general-alphabet theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
