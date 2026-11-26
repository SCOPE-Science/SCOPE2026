# Independent mathematical audit

## correctness

PASS

Independent exact replay /workspace/replay/1.py used the symmetric difference of pairs of token states and disjointness of underlying labels to build all 45 vertices and 120 edges. All-pairs distances confirmed connectedness and counts 120,390,390,90. Inverting L+J (J the 45-by-45 all-ones matrix), with the inverse product checked, gives the exact voltage solution on zero-sum unit current vectors e_i-e_j, since J kills that subspace. The resulting 990 quadratic forms split into 17 buckets. Starting each bucket at its least pair and applying adjacent label transpositions gives exactly that bucket; each is therefore one S5 orbit. Every graph automorphism preserves resistance and the S5 action is by automorphisms, so the buckets also coincide with the full group orbits without needing the full group classification. All representatives, multiplicities, scaled numerators and distances match the frozen table; the exact Kirchhoff sum, characteristic polynomial, extrema and the graph-distance inversion agree.

## originality

PASS

The verified distinct claim is the exact pair-resistance table and equivalence of resistance equality with pair-orbit equivalence in this 45-state graph. Same-object published data overlap materially for the Laplacian polynomial and for using shortest-path geometry with S5, but do not supply an orbital inverse or the exact pair-level separation.

## value

PASS

The natural two-particle exclusion network on Petersen has only four positive graph distances; the resistance invariant instead completely resolves all 17 symmetry types of unordered vertex pairs and reverses some shortest-path comparisons. The exact values supply a reference for this network and its associated commute-time geometry, rather than just duplicating its trace or symmetry group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
