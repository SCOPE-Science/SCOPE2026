# Independent mathematical audit

## correctness

PASS

I independently enumerated all 2^21 labeled tournaments by exact oriented-edge masks, filtered by outdegree three, obtaining 2640. Exactly 14 cyclic triangles are flippable at each state (hence 18480 undirected edges). Explicit orbit generation under the 7! label permutations gave orbit sizes 240,720,1680, covering all 2640 states. Exact BFS from each orbit representative visited the entire graph and reproduced shell profiles: 240:(1,14,91,343,749,871,476,92,3), 720:(1,14,91,336,721,822,485,147,22,1), 1680:(1,14,91,340,739,853,483,113,6). Converse distances were 7,9,7; the sole radius-nine shell in the 720 orbit is its converse, yielding 720/2=360 antipodal unordered pairs, global diameter nine and radius eight. Independent four-subset enumeration recovered cyclic-triangle histograms (0,14,21),(7,0,28),(3,8,24), identifying the middle orbit by absence of one-cyclic-triangle four-sets. The source code checks every state; this is a genuinely complete finite proof, not sampling.

## originality

PASS

PASS, qualified best-of-knowledge: literature comparison of exact statements/implications. The graph object and moves are classical; the new claim is the complete shortest-path metric, which cannot be derived from connectivity alone. The recognized prior bounds may constrain graph diameter but do not mathematically imply these exact shell profiles; inaccessible original Brualdi–Li tables remain a priority risk.

## value

PASS

The triangle-interchange graph of the smallest interesting regular tournament score class is a canonical finite object. Its exact radius/diameter, full orbit distance distributions and intrinsic converse-antipode criterion are a meaningful complete metric classification rather than a tiny arbitrary slice, resolving a natural extremal configuration question within the 2640-state graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
