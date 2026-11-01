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

# Executable verification and scope

`fan_direct_check.cpp` builds the fan directly from its labelled adjacency lists. For each \(2\le n\le8\), it scans every integer chip assignment satisfying \(0\le c(v)<2\deg(v)\), executes two simultaneous updates and counts states with \(U^2(c)=c\ne U(c)\). Dividing by two produces the orbit counts \(6,30,128,525,2064,7915,29760\). The output file `DIRECT_CHECK.txt` gives the number of configurations scanned at each size. The finite box is exhaustive for primitive two-cycles, as proved from the required alternating firing indicators and exact height intervals; however, these tests are only a finite check of the infinite-family statement.

`fan_transfer_check.py` independently enumerates binary cut words, constructs the four-state transfer matrix and endpoint vectors, symbolically checks the rational fan generating function, and reconstructs the wheel closed-rim trace/determinant identity. It verifies exact agreement of all fan cut-word counts for \(2\le n\le15\) and checks algebraically that the ratio of the dominant constants is \(1-2/\sqrt{13}\). Its standard output is `SYMBOLIC_CHECK.txt`.

To reproduce, compile with a C++17 compiler using `g++ -O3 -std=c++17 fan_direct_check.cpp -o fan_direct_check` and run `./fan_direct_check`. With Python 3 and SymPy installed, run `python fan_transfer_check.py`. The archived outputs are observations from these programs, not replacement proofs.

The package provides a symbolic all-\(n\) argument and bounded independent computations, but no independently performed external audit, no exhaustive literature guarantee and no claim about periods other than primitive two.
