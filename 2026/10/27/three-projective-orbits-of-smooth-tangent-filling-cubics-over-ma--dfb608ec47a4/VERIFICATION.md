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
# Verification and reproducibility

The result concerns exactly the \(13\) points and lines of \(\mathbf P^2(\mathbf F_3)\), all \(59048\) nonzero homogeneous cubic forms over \(\mathbf F_3\), and rational projective coordinate changes. No external data or randomness are required.

Compile and execute `verify_incidence.cpp` using `g++ -O3 -std=c++17 verify_incidence.cpp -o incidence` followed by `./incidence > incidence.out`. It reproduces `candidate_codes.txt`, a complete strictly increasing list of the \(7488\) qualifying coefficient vectors, and reports the intermediate count \(35388\) of forms nonsingular at rational points. Compare its printed output with the embedded `incidence.out`.

Execute `python3 verify_orbits.py > orbits.out` to projectively normalize all candidates and exhaust their orbits under five explicit linear coordinate generators of \(\operatorname{GL}_3(\mathbf F_3)\). It checks closure and exact coverage by orbit sizes \(936,936,1872\), and prints the representative coefficients. Compare with the embedded `orbits.out`. Optionally execute the independent NumPy-based incidence program `python3 verify_numpy.py > numpy.out` (NumPy is its only third-party dependency) and compare the complete candidate-code sequence and counts with the two prior checks.

The proof of geometric smoothness is symbolic and applies in the algebraic closure: the first two representatives have derivative with respect to \(Y\) equal to \(Z^2\), while for the third a hypothetical common zero of the equation and its partials implies both \(Y^3=Y+1\) and \(Y=0\). Therefore the argument does not infer geometric smoothness from bounded finite-extension enumeration. The degree-two lower bound follows from a four-point conic dual failing the blocking property.

Limits: the programs certify a finite exact census for \(\mathbf F_3\), not a classification over all fields; no independent publication-priority verification or independent audit has been performed.
