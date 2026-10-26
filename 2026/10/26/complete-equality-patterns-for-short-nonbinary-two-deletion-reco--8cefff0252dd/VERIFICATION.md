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
# Verification of the finite equality-case classification

The claim is a **finite-length theorem uniform in alphabet size**. Its exhaustive proof certificate enumerates equivalence patterns, not individual words for arbitrary alphabets.

Run the three reproducible checks from the directory containing the bundled files:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic rgs_classifier.cpp -o rgs_classifier
./rgs_classifier > reproduced_rgs_output.txt
cmp rgs_output.txt reproduced_rgs_output.txt
python3 verify_direct.py > reproduced_direct_output.txt
cmp direct_output.txt reproduced_direct_output.txt
python3 verify_orbits.py rgs_output.txt > reproduced_orbit_output.txt
cmp orbit_output.txt reproduced_orbit_output.txt
```

**Exhaustive partition check.** The classifier visits respectively \(203,4140,115975,4213597\) restricted-growth partitions of \(2n\) positions at \(n=3,4,5,6\). Exactly \(133,3690,113073,4194600\) of those satisfy the disjoint-one-deletion condition. Their maxima are \(3,4,6,6\), with \(1,6,1,12\) canonical equality witnesses; the complete support multiplicities and actual witness strings are in `rgs_output.txt`. The code includes all partitions up to support \(2n\), not just the eventual maximizers.

**Independent labeled-word checks.** `verify_direct.py` uses separate Python tuple-based deletion-subsequence sets and tests every unordered labeled word pair at the specified sizes: \(q=3,4\) and lengths \(3,4,5,6\); \(q=5\) and lengths \(3,4,5\); \(q=6\) and lengths \(3,4\); plus the nonbinary-boundary diagnostic cases at \(q=2\) where the predicted support is realizable. All checks match and the output ends in `DIRECT_VERIFY_OK`.

**Symmetry check.** `verify_orbits.py` re-normalizes equality strings under center swap and simultaneous reversal. It verifies the support multiplicities and the \(1,4,1,5\) orbit counts; its output ends in `ORBIT_VERIFY_OK`.

The logic linking these finite searches to **all finite alphabets** is the proved bijection between length-\(2n\) position partitions and equality types, plus the exact \((q)_{\underline{s}}\) injection count. The direct labeled-word tests are additional assurance, not an infinite proof. These checks are reproducible but are not independent external validation or certification.
