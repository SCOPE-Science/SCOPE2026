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

The C++17 source `verify_profiles.cpp` is a complete standalone enumerator using only the standard library. Compile with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_profiles.cpp -o verify_profiles` and execute `./verify_profiles`. It enumerates all permutations of sizes 1 through 10, computes the four-quadrant masks both by direct comparisons and independent prefix/suffix minima and maxima, and asserts equality for each permutation.

It checks the size-by-size sharp type maxima 1 to 10, the complete 328 first maximal witnesses at size 10, the exact two 164-member type spectra, and orbit representatives under position reversal, value reversal and order exchange. The orbit-size profile is 10 orbits of size 4 and 36 orbits of size 8, totaling 328. The literal output of the successful replay is in `census_output.txt`.

The mathematical proof of the all-length ceiling, the complete two-spectrum classification at maximal richness and the inflation for every n above ten is contained in `RESULT.md`; checking finitely many permutations does not prove statements about infinitely many lengths. Exactness of the finite enumeration assumes the source and the compiled executable are faithfully executed. No independently performed scientific audit is claimed.
