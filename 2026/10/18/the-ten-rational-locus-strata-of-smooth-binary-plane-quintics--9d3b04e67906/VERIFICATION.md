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
# Verification record

Two C++17 verification sources are included in full. Compile without external mathematical software:

```sh
g++ -O3 -std=c++17 quintic_fibers.cpp -o quintic_fibers
./quintic_fibers
g++ -O3 -std=c++17 quintic_census.cpp -o quintic_census
./quintic_census
```

The direct-fiber program loops over every one of the \(2097151\) nonzero coefficient vectors, selecting one prescribed evaluation fiber in each of the ten Fano point-set orbits. Its rational-point evaluation and row-elimination smoothness routine were written separately from the orbit program. Its output counts are \((15792,10422,7544,5000,5840,5016,4233,3350,2420,1512)\). With multiplicities \((1,7,21,7,28,7,28,21,7,1)\), these give \(688128\) smooth equations.

The projective-orbit program constructs all \(168\) invertible coordinate transformations and finds \(13055\) nonzero equation orbits. Its complete smooth/blocking totals are \(602774\) singular nonblocking, \(806249\) singular blocking, \(445802\) smooth nonblocking, and \(242326\) smooth blocking. Its smooth-orbit totals are \(2688\) nonblocking and \(1516\) blocking. Both sources were compiled and run, and their exact outputs agreed with these values.

The algebraic regular-sequence criterion for the partial derivative ideal supplies the infinite geometric smoothness justification. The finite programs prove the ten matrix-rank enumerations only once that criterion has been established. They do not independently verify external bibliographic priority. The independent-audit channel remains unperformed.
