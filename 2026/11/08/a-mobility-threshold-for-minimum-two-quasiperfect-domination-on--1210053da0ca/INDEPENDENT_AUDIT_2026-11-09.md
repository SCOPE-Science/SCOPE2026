# Independent mathematical audit

## correctness

PASS

For outside cell (i,j), selected neighbors equal r_i+c_j; empty row+column impossible. With m<n a zero column forces exactly one selected per row, positive column loads are 1 or m, giving injections plus full columns. For m=n either all rows or columns represented, yielding permutations plus full bars. One-change edges are arrangement graph; distance t+c from mismatched rows and cyclic dependency components, with exact diameter m+floor(m/2). Independent exhaustive subset enumeration gave (3,3):12 isolates, (3,4):28 states and 36 edges with 24-component plus 4 isolates, (3,5):65 states 180 edges, (4,4):32 isolates. Read full RESULT.md and check_exhaustive.py. General proof not inferred from small boards.

## originality

PASS

The number gamma_[1,2]=m is already established via claw-free general results; n=m? arrangement graphs and their diameter are prior Day--Tripathi. New combined claim gives exact full optimizer classification including isolated columns and square-board freezing, not present in inspected abstract and no equivalent Resultary finding discovered. Full original 2013/2017 primary texts not read in this execution; risk recorded, not a default originality failure.

## value

PASS

Sharp mobility threshold for natural [1,2]-domination on line graphs of K_(m,n) identifies all optimal states, connected component and exact distances, useful for reconfiguration complexity and combinatorial placements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
