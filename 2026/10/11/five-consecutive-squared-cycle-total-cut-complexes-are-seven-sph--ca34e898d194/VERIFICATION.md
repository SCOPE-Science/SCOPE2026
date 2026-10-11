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
# Reproduction and limits

The C++17 program `verify_squared_cycle.cpp` constructs all independent \(k\)-subsets of the squared cycle \(W_{3k+3}\) and all subsets of their complementary facets for every integer \(4\le k\le8\), then implements each prescribed matching stage. The observed complete face counts were `22547, 142309, 854721, 4920705, 27332161`; independent-set facet counts were `75, 126, 196, 288, 405`. For each \(k\), precisely one unmatched face remains: integer mask `21846`, representing vertices \(\{1,2,4,6,8,10,12,14\}\), with dimension seven. In all five cases the empty simplex was matched. The program independently tests the facet enumeration formula and verifies that `faces == 2 * matched_pairs + critical_count`, with critical count one. All five reduced Euler characteristics are \(-1\).

Compile using `g++ -std=c++17 -O3 -Wall -Wextra -Wpedantic verify_squared_cycle.cpp -o verify_squared_cycle` and run `./verify_squared_cycle 4 8`. A successful run prints `VERIFY_OK` after reporting the five exact matching profiles. If a run is incomplete, the assertion is not thereby verified. The acyclicity of each complete matching follows from the sequential-element-matching theorem, not merely from runtime success. The claim covers only the five explicitly exhausted finite cases; no infinite-family proof is asserted.
