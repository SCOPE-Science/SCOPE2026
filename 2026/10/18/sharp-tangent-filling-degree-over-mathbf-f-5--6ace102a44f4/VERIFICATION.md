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

# Reproduction of exact checks

Compile and execute `verify_tangent_f5.cpp` using a C++17 compiler. Its enumeration loops over all homogeneous ternary equations modulo nonzero scalars, for degrees one, two, and three. The coefficient normal form has first nonzero coordinate equal to one. Every rational zero contributes its tangent line only when the gradient is nonzero. Output:

```text
degree=1 normalized_forms=31 tangent_filling=0
degree=2 normalized_forms=3906 tangent_filling=0
degree=3 normalized_forms=2441406 tangent_filling=0
smooth_quartic_witness_rational_points=11 tangent_points=11 union_points=31
MINIMUM_DEGREE_4_VERIFIED
```

Execute `verify_witness.py` using Python 3 without third-party packages. It lists eleven rational tangent lines and confirms coverage of all thirty-one rational projective points, printing `WITNESS_VERIFIED`. Optionally run `verify_vectorized_numpy.py` with NumPy installed: it independently reconstructs all ten cubic monomials, coefficient classes, formal gradients, and line incidences, reporting `vectorized numpy census 2441406 0`.

The displayed quartic's **geometric smoothness** is not established by these finite checks; it is proved directly from its three partial derivatives in `RESULT.md`. Likewise, exhaustive checking in degrees at most three is logically distinct from infinitely many degrees or other finite fields. The C++ program and both Python scripts have been executed from the package source paths. No independent external validation has been performed.
