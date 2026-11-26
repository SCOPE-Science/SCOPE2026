# Independent mathematical audit

## correctness

PASS

The counter tracks the three exact prefix statistics modulo m. Summing i(x−i) over 1s with i preceding zeros proves z≡(x−1)y for even m. Direct composition in left-to-right word order gives C(x,y,z)=(x,y+1,z−x−1) and D(x,y,z)=(x,y,z−2); inverse letters are positive powers, so the parity obstruction is complete. Reversing suffixes gives the complete attainable set (a,b,d), and for fixed a,b the unique d that accepts the first state is feasible exactly when (x+a−1)(y+b) has parity t. For odd m all suffix statistics are possible and affine tests separate the states. For even m the feasible parity pairs first recover x,y parities. Varying a,b by two then allows only the half-modulus shifts in x,y. An odd half-modulus is prohibited by equal parities, and for even t the three feasible parity pairs test both coordinate differences individually. For 4|m and odd t there is just one feasible parity pair, so each of the four choices of even half-modulus shifts determines exactly one even shift in z and hence one reachable equivalent state. This proves the complete-DFA count for every target residue, including m=2 and t=0. Independent minimization matched all 77 cases with 2≤m≤12 (e.g. [32,8,32,8] for m=4); it corroborates the symbolic proof only.

## originality

PASS

The claim is the single-residue Myhill–Nerode index, especially the fourfold collapse for odd residues when 4 divides m. The closest catalog theorem counts the full-output Moore states, not the Boolean quotient. Other inspected results change the pattern, restrict the input words, or count a different equivalence. None gives the stated single-residue classification in the inspected material.

## value

PASS

This is a natural exact invariant of one of the simplest subsequence counters with separated identical letters. The result distinguishes acceptance complexity from the number of reachable counting states and identifies precisely when selecting a different residue on the same counter saves a factor of four. That distinction supports computing actual minimal recognizers and is not an instance-by-instance table or a corollary of the raw counter size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
