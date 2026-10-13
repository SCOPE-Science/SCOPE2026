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

# Reproduction

Compile the stand-alone C++ program `verify_cyclic_cpp.cpp` with a C++17 compiler using `g++ -O3 -std=c++17 verify_cyclic_cpp.cpp -o check_cycles`, then run `./check_cycles > reconstructed_representatives.txt`. It exhaustively lists all admissible cyclic binary words of each claimed minimum length for orders \(2\) through \(6\), tests every cyclic factor and computes every rotation/reversal orbit. It reports summary cardinalities on the error stream and prints 42 order-six canonical representatives on the output stream.

Run `python verify_cyclic_python.py` to recompute each class size and orbit partition from an independently implemented string recursion, factor-set checker and lexicographic dihedral representative. Its terminal success marker is `PYTHON_CYCLIC_ENUMERATION_VERIFIED`. The Python and C++ scripts both yield 3,6,20,102,2352 labeled words and 1,1,1,3,42 classes, respectively.

`optimal_representatives.tsv` lists 42 order-six representatives, each at length 28, under the C++ numerical bitmask canonical convention (earliest character as least significant bit), distinct from Python's lexicographic convention. Independently normalizing these 42 strings via Python's reversal/rotation action gives exactly the same 42 classes as independent exhaustive Python enumeration. Checking the 28 cyclic windows of each representative gives 21 legal factors and seven duplicated factors, each appearing exactly twice. Only orders 2–6 are exhaustively certified here. No external scientific audit has been performed.
