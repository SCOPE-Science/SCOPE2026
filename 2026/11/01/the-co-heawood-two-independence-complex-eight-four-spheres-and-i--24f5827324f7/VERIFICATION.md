---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Computational verification

Run `python3 verify.py` with a standard Python 3 interpreter in the directory containing this file. The program requires no extra packages or external data. `verification_output.txt` records one execution of that exact program.

The program constructs the fourteen-vertex co-Heawood graph from the Singer difference set \(\{0,1,3\}\) in \(\mathbb Z/7\mathbb Z\). It verifies the unique-line-pair property, degree four, and Fano nonincidence definition. Every one of the \(16384\) possible vertex masks is evaluated by two face predicates: induced maximum degree one and avoidance of all three-vertex forbidden paths.

The complete face vector including the empty face is \((1,14,91,280,420,266,42,2)\); the \(86\) facets lie in dimensions four, five and six with multiplicities \((56,28,2)\). The deterministic toggle algorithm uses \(553\) pairs. It independently constructs every nonempty-face Hasse incidence (\(4298\) in total), reverses the matched pairs, and topologically sorts the resulting \(1115\)-vertex directed graph. All vertices are visited, proving the absence of directed cycles; the unmatched cells are precisely one vertex and eight four-dimensional simplices.

The reduced mod-two chain ranks in cardinalities one through seven are \((1,13,78,202,218,40,2)\), yielding reduced mod-two Betti numbers \((0,0,0,0,8,0,0)\) in degrees zero through six. Integral wedge homotopy uses the verified discrete-Morse certificate rather than inferring integral results from mod-two data.

All \(5040\) permutations of seven points are checked, producing \(168\) point-line-preserving automorphisms. Their compositions with the specified polarity give another \(168\). Adjacency preservation is explicitly checked for each. For each of the \(336\) automorphisms, signed fixed-face Lefschetz contributions determine its action on the sole nonzero rational reduced homology group; character table multiplicities and both character sums are checked exactly. The result \(\sum_g\chi(g)^2=336\) proves absolute irreducibility, and \(\sum_g\chi(g)=0\) proves absence of invariants.

The run makes no claim about larger plane orders or independent expert certification. The named source studies concern published definitions and matching theory; novelty cannot be proved by computation alone.
