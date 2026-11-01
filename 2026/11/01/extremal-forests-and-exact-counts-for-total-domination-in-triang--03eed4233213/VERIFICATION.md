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

# Reproducibility

The standalone source `verification.cpp` depends only on a C++17 standard library. To rerun from a directory containing the file:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verification.cpp -o verification
./verification
```

The program constructs every two-element subset of \([n]\) as a candidate selected edge, exhausts all choices of the known optimal size for each \(n\) from four through ten, tests whether every selected edge has another selected adjacent edge and whether at most one base vertex is unused, and independently determines selected-edge component orders and cycle ranks. It rejects any valid minimum-sized selection outside the stated forest families and compares each family count with its exact integer formula.

The replayed output is:

```text
n=4 inspected=15 optimum=12 families=12,0,0 OK
n=5 inspected=120 optimum=80 families=80,0,0 OK
n=6 inspected=1365 optimum=840 families=90,750,0 OK
n=7 inspected=5985 optimum=630 families=630,0,0 OK
n=8 inspected=98280 optimum=13440 families=13440,0,0 OK
n=9 inspected=1947792 optimum=277200 families=7560,189000,80640 OK
n=10 inspected=8145060 optimum=75600 families=75600,0,0 OK
VERIFY_OK n=4..10 exhaustive, direct adjacency and exact component-classification checks
```

Only the displayed finite ranges were computationally checked. The proof for every \(n\ge4\) follows from the abstract component inequalities, the zero-cyclomatic-excess argument and Cayley's labelled-tree formula, all stated in `RESULT.md`.
