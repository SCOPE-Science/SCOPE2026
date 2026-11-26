# Independent mathematical audit

## correctness

PASS

Token relabeling acts transitively, so the complete identity-based metric determines the diameter and common shell counts. I reproduced the full enumeration with `python3 /workspace/branches/wagner_reproduction.py`, new code using residue-based adjacency, composition on the labels, and set differences between exact frontiers. Left and right products from the identity give the same length sets by reversing each word, and expanding the current exact layer and deleting seen states proves minimality inductively. The enumeration reached exactly 40320 distinct assignments with twelve generators and returned shells [1,12,90,500,2059,5960,11124,11986,6748,1702,138], gaps [16350,18574,5322,74] and last-shell transport counts {15:48,16:90}. The underlying W distances are 0 at equality, 1 for differences ±1 or 4, and 2 for all other residues; swapping moves exactly two tokens one edge each, so the ceiling-half bound is valid. The frozen script was inspected, not run. Its docstring names verify_cube.py, a command typo; the actual file and reproducibility record correctly name verify_wagner.py.

## originality

PASS

The strongest located exact lookup is the reversible-circuit table for the cube. Its generator set has the same size but gives a different word metric, already differing at shell 3 (476 instead of 500). No Wagner match was established in the bounded comparison; the finite census is not claimed as a new enumeration method.

## value

PASS

The Wagner graph is a canonical small cubic graph with short base-graph distances but nontrivial sequential routing. The exact metric and complete transport-slack distribution quantify how poorly the natural lower bound can predict swap cost, and give a graph-specific benchmark directly comparable to the known three-cube metric. Exhaustion of all states supplies a usable baseline; the claim is not an arbitrary partial sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
