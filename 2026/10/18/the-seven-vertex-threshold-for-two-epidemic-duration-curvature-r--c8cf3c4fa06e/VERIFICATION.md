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

# Reproducible checks

The claim uses independent Bernoulli-open contact edges with common parameter \(p\), the root as the sole initial infection, and the last generation with new infections as the duration statistic. The general recursion and witness differentiation are proved in `RESULT.md`.

Run `python verify.py CENSUS.csv` from the directory containing the files, with Python 3.9+ and SymPy 1.10+. The program constructs all labeled trees of orders 2 through 7 from Prüfer sequences and all roots; it uses exact root-preserving canonical codes to collapse isomorphisms. Its dynamic programming computes expected duration by recursion over tail probabilities, and its independent enumerator explicitly opens every subset of edges and computes the root-component height. Their exact polynomials agree for every rooted type. Exact algebraic root counts, excluding both endpoints, give 84 rooted types with curvature-zero count frequencies: for \(n=2\), \((1,0,0)\); \(n=3\), \((2,0,0)\); \(n=4\), \((3,1,0)\); \(n=5\), \((5,4,0)\); \(n=6\), \((12,8,0)\); and \(n=7\), \((28,19,1)\), ordered as zero, one, two interior zeros. There is exactly one class with two roots, canonical code `(((()))(())())`. The executable prints `PASS` and writes `CENSUS.csv`.

The supplied `CENSUS.csv` contains all 84 exact polynomial certificates. A separate rooted-tree generator using standard nonisomorphic-tree enumeration was also checked against this census and gave the same counts. The proof of completeness uses the Prüfer bijection, not the numerical count alone. There is no claim about arbitrary larger trees. The scientific assessment reported here is not independent verification.
