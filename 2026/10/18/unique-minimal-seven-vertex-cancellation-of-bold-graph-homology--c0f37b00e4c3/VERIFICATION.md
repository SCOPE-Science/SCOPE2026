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
# Reproduction of the sharp bold-homology threshold

The classification is exact and finite. These instructions reproduce two distinct enumerations with exact \(\mathbb F_2\) linear algebra; they are not an independent mathematical audit or an infinite-family proof.

Compile and execute the labeled C implementation:

```sh
cc -O3 -std=c11 -Wall -Wextra -o census_labeled census_labeled.c
./census_labeled
```

`census_labeled.out` is the observed output. The enumeration visits all \(2^{\binom n2}\) graph masks in each order \(1\le n\le7\), testing connectivity, connected domination, Euler cancellation, and reduced boundary ranks. Every one of 252 positives on seven vertices is checked to be the cycle suspension by a graph-structural test.

Run the separate unlabeled direct cochain method:

```sh
python census_direct.py
```

Requires `networkx` and its bundled Read–Wilson graph atlas (1,253 unlabeled graphs on at most seven vertices); `census_direct.out` records the expected counts and uniquely identifies `G1212`, graph6 `Fhf~o`. The implementation constructs the **connected-dominating cochain differential**, not the complementary boundary differential of the C verifier, and checks known base families. The exact output for the positive witness must have Betti numbers in degrees 2 and 3 only, each of rank one.

Manual witness proof: the complement non-connected-dominating face complex consists of a collapsed five-cycle plus a disjoint edge. Its reduced cohomology in dimensions zero and one is one-dimensional; the degree shift by two gives bold cohomology in degrees two and three. All five free triangle–edge pairs are specified in `RESULT.md`.

Limits: absence of a graph before seven and uniqueness at seven are finite exhaustive classifications; graph orders above seven and coefficients beyond \(\mathbb F_2\) are not classified. The wider 2023 suspension theorem already covers existence and the witness groups. External independent audit has not been performed.
