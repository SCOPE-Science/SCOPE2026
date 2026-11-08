# Independent mathematical audit

## correctness

PASS

For even q with fixed-point-free involution, the oriented target set consists of all q² fourmers T_{a,b}=ab bar(b) bar(a). Explicit suffix-prefix overlap analysis gives q/2 special two-target modules with reciprocal cost-one transitions and q(q-1)/2 ordinary modules with reciprocal cost-two transitions. All other intermodule transition costs are >=3. In a selected cyclic Hamiltonian ordering one must leave each module, adding excess one per ordinary module and two per special module above sum of cheap outcosts 2q²-q; the result is L_cyc>=(5q²-q)/2. For linear paths, omitting the last target exit and the corresponding module penalty yields L_lin>=L_cyc+1. The proof supplies a balanced connected directed multigraph of modules (loops within complement pairs and balanced pairs between distinct complement pairs); its Euler circuit traverses each module at its cheapest internal cost and connects modules at cost exactly 3, meeting the lower bound for every even q. Cutting one intermodule overlap yields the linear optimum. Independent reconstruction checked Euler covers for q=2,4,6,8 with lengths 9,38,87,156; q=4 literal Watson–Crick 38/39-word examples were checked to contain all 16 oriented targets. This finite evidence only corroborates the symbolic module/Euler proof.

## originality

PASS

Although both have palindrome pairing and Euler tour language, universal reverse-complement representative coverage and palindrome-only shortest literal coverage are mathematically different optimization problems. A cover for all k-mer classes need not attain the palindrome-only lower bound. General approximation bounds and full de Bruijn-cycle constructions do not imply the exact length or module equality characterization. Reverse-complement pairing is an established ingredient and is credited, not claimed novel. The all-q statement is not a mere database lookup or a small q=4 numerical optimum. The explicit formula is proved for arbitrarily large even q by a module/Euler construction; lack of a database hit does not prove novelty. The pairing observation alone is insufficient to deduce the selected all-palindrome minimum tour, including the gap between cyclic and linear lengths. Matching motifs/names are insufficient; the specified coverage obligations and implications differ. Best-of-knowledge PASS with specifically identified historical-priority risks; an unsuccessful search is not proof of novelty.

## value

PASS

The shortest superstring/cover of every literal Watson–Crick reverse-complement four-palindrome is a natural constrained universal-word optimization in DNA motif design. The exact all-even-alphabet cyclic and linear formulas plus necessary extremal module structure are meaningful, not a small ad hoc enumeration; the four-letter molecular case has a concrete optimal witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
