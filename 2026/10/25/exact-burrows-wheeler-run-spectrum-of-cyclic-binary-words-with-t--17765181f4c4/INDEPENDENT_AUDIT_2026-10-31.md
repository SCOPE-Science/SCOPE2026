# Independent mathematical audit

## correctness

PASS

Represent each length-n word with exactly three 1s by a cyclic orbit of three nonnegative zero-gap lengths g_0,g_1,g_2 summing n-3; rotation equivalence acts by cyclic permutation, not reflection. For a rotation starting t zeros before a marker, 0≤t≤g_i, lex order prioritizes longer leading zero runs (decreasing t), then compares subsequent gaps. Its preceding BWT letter is 1 precisely for t=g_i. Exactly three marked BWT rows occur, the first transformed symbol is 1 and the last is 0 since at least one zero exists, so the total linear runs are twice the number of connected marked blocks: 2,4,6. The gap adjacency analysis distinguishes equal lengths, pairwise-distinct neighboring lengths and their cyclic orders; balanced gaps yield the unique 2-run necklace, while 4-run triples count by two equal, small-middle or middle-large adjacent marks. The resulting generating series ∑_{M≥0} C_4(M+3)z^M=z²/(1-z)²+z³/(1-z³) holds for M≥1. Burnside on three-gap cyclic compositions gives total [binom(n-1,2)+2·1_{3|n}]/3, so C_6 is the remainder, and its quadratic leading growth proves density→1. Independent code enumerated every cyclic composition orbit for every length 4..60, sorted all n cyclic rotations with multiplicities, and checked all run bins, totaling 11,419 necklaces; this independently tests the complete finite statements but the all-n proof rests on the structural lemmas and Burnside.

## originality

PASS

The sentinel-free cyclic BWT and its standard/Sturmian two-run characterization are prior knowledge; no originality is assigned to those. The exact distribution into two, four, and six linear runs among every weight-three necklace is a distinct all-length question. Simpson–Puglisi 2008 study simple BWT words (especially minimum two runs), and Mantaci–Restivo–Rosone–Russo–Sciortino 2017 fully classify BWT fixed points at low minority weight, not the run spectrum. Indeed the 2017 full primary Section 4 Proposition 4.2 explicitly classifies weight-three fixed words rather than all weight-three BWT run counts, so shared parameters do not imply coverage. No stronger all-run-spectrum theorem was found in actual searches, with possible historical gap enumeration remaining a risk.

## value

PASS

The number of equal-letter runs in the Burrows–Wheeler transform is a natural compressibility and indexing parameter. Exactly three minority markers are the first nontrivial small-weight class with three possible BWT clustering regimes; determining all three proportions and the unique maximally clustered necklace for every length is a natural complete classification, not a selected isolated small-n count. The asymptotic prevalence of six runs is an exact property of the entire fixed-content necklace ensemble.

The dated certificate retains the supplied scientific assessment, sources and limitations.
