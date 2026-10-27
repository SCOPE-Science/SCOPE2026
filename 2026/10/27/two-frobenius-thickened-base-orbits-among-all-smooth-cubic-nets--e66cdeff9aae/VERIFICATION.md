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

# Verification instructions

Use Python 3 with SymPy (tested with 1.14.0). From this directory run:

```sh
python3 verify.py > checked.json
python3 -m json.tool checked.json > /dev/null
```

For the geometric-base theorem, inspect in particular the `geometric_base` entries of all eight projective orbit representatives; the other counts independently index the finite population. The output `checked.json` must agree byte-for-byte with `reference_output.json` on this Python/SymPy version; if the pretty-printer differs, compare parsed JSON objects. It reports 336 geometrically smooth cubic coefficient vectors, 5,544 all-smooth binary pencils, 864 all-smooth nets, eight projective orbits with sizes (8,8,8,168,168,168,168,168), and exactly 16 nets with nonreduced geometric base. It also lists all orbit representative coefficient masks, point-count profiles, stabilizer orders and computed affine base ideals.

For the independently implemented finite-field check, use a C++17 compiler:

```sh
g++ -O3 -std=c++17 verify_field.cpp -o verify_field
./verify_field
```

The final three lines of standard output must read:

```text
smooth_cubics=336
all_smooth_pencils=5544
all_smooth_nets=864
```

The C++ check uses the finite fields of sizes eight and sixteen to test the cubics and then reconstructs the binary subspaces. The symbolic Gröbner-basis checker is the primary exact verification of geometric smoothness; its criterion is over the algebraic closure, not merely over a finite extension. The finite-field check is corroboration. The orbit computation enumerates all 168 invertible binary coordinate matrices and verifies orbit partition and stabilizer sizes. The base-scheme calculation uses all projective charts, with no inference from rational base points alone. On the two exceptional orbits the affine coordinate quotient is the square of an irreducible cubic; on every other orbit it is the zero ring. The absence of geometric base points permits finite morphisms, and their degree nine follows from pullback of the hyperplane bundle \(\mathcal O(3)\). These computations classify the specified finite family but do not establish priority against every unpublished table.
