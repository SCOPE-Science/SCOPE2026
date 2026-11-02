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

# Verification details

The exact finite claim is the full equivalence-class table for parameters \(1\le n\le10\) and ranks \(1\le q\le5\), with cutoffs \((1,3,4,5,7)\). These are comparisons of complete recursive types, **not** comparisons of hashes or counts alone. Ordinary first-order logic ignores multiplicity of identical extension types, so sets of child types are used instead of multisets.

The C++17 file `verify_incidence_types.cpp` computes atomic adjacency/equality data and recursively interns sorted, deduplicated extension-type IDs in a global exact map. It visits 156276 memo states and constructs 2109 interned signatures on the stated input range. The independently written Python file `verify_incidence_types.py` builds immutable nested type sets directly; it also visits 156276 states. `verify_direct_small.py` evaluates every possible next vertex without symmetry reduction for index parameters one through four at rank five, obtaining identical complete root types to its separately implemented orbit recursion. Recorded outputs are `verify_cpp.out`, `verify_py.out`, and `verify_raw.out`.

To reproduce on a system with a C++17 compiler and Python 3, extract all embedded files into one directory and run `bash reproduce.sh`. The script compiles the included C++ source, replays all three computations, and compares their output byte-for-byte with the supplied records. A failed compilation, computation, assertion, or output difference exits nonzero.

The orbit-representative proof is necessary to show that the reduced finite enumeration is exhaustive. The infinite claim is justified separately by maintaining a bijection on the at-most-\(2q\) underlying indices used in a \(q\)-round game; for parameters at least \(2q\), Duplicator always has sufficient fresh indices. These two mathematical lemmas, the program paths and their results support the stated theorem. No finite test by itself asserts validity for unbounded parameters.

Independent mathematical audit: not performed. Historical priority: not exhaustively certified. No formal proof assistant or third-party certification is claimed.
