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

# Exact finite verification

The main program `cone_census.py` enumerates the entire 32,768-element parameter domain (cubic sections modulo the cone equation with nonzero vertex coefficient). It tests geometric smoothness by two exact univariate gcds, contact by restriction to all fifteen rational planes, and projective equivalence by explicit automorphisms. Its expected output is `cone_results.json` with 12,288 smooth sections, 274 smooth orbits, and maximum six proper contact planes in three 48-element orbits.

The independently coded `verify_extension.cpp` avoids the univariate gcd smoothness test: it evaluates the two-chart affine Jacobian equations over explicit finite fields of degrees one through six. The degree bound follows from the polynomial \(D\) in `RESULT.md`. A degree-at-most-six nonzero \(D\) captures every singular chart parameter; if \(D\) is zero, the factorization in the proof reduces the singular parameter candidates to factors of degree at most four. It checks plane contacts by explicit binary-form multiplication, not by the first program's bitwise sextic formula. It reproduces the full stratification recorded in `verification_counts.txt`.

The optional `verify_groebner.py` recomputes the geometric smoothness of one representative from every one of the 752 total coefficient-space orbits using Gröbner bases of the full affine Jacobian ideals over \(\mathbf F_2\). It agrees for all 752 representatives, identifying 274 smooth orbit classes. The comparison result is summarized in `groebner_agreement.txt`. This optional check requires SymPy; the first two programs require only Python 3 and a C++17 compiler.

Run from the directory containing all files:

```
python3 cone_census.py cone_results.json
g++ -O3 -std=c++17 verify_extension.cpp -o verify_extension
./verify_extension
python3 verify_groebner.py
```

These are reproducible, deterministic exact finite computations. No independent mathematical audit or external certification has been conducted. The searches of primary literature cannot establish absolute publication priority.
