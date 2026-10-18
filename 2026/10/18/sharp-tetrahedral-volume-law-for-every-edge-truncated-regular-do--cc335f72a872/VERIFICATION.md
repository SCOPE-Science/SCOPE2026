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

# Reproducing the exact certificate

In the directory containing `verify.cpp`, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

The implementation constructs 20 exact golden-ratio dodecahedron vertices; identifies 30 edges by squared distance; produces both directions of each edge, giving 60 affine truncation paths; enumerates every unordered four-path subset; interpolates all determinants as degree-at-most-three polynomials in the ring \(\mathbb Z[\varphi]\); and checks all eight Bernstein coefficient signs bounding the determinant by \(F(t)\) in absolute value for **every** \(t\in[0,1/2]\). Sign comparisons are exact. It checks that 120 path quadruples attain the same absolute polynomial bound identically and that 40 fixed three-vertex bases have three equal-sign apex alternatives with the same original dodecahedron endpoint, certifying triangular moving-apex equality families. An explicit witness is also verified through the polynomial construction.

The checker output should begin `PASS: 487635 four-vertex configurations checked; 8 signed Bernstein inequalities each.` and include `Interior maximizing quadruples: 120` and `Movable-apex triangle families: 40`.

The proof additionally uses two independent analytic steps: (1) replacement of each tetrahedron vertex by a polytope vertex using convexity of the absolute determinant; and (2) positivity of the Bernstein basis in the interior to exclude nonidentical determinant polynomials from tying the sharp envelope. The finite exact certificate is not falsely identified with enumeration of infinitely many \(t\) values; these analytic implications close that gap.

The Archimedean uniform member has \(t=(5-\sqrt5)/10\), **not** \(t=1/3\); this follows by equating triangular and decagonal edge lengths. The classical truncated-dodecahedron body-volume formula is independently documented in the references. No formal independent audit or historical-priority certification is claimed.
