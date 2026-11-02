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

# Finite verification

The reproduced `codewords.txt` has exactly 84 distinct 22-bit integers with minimum pairwise Hamming distance 9. Every integer from zero through 4,194,303 is examined. The C++17 verifier independently obtains the nearest-codeword distance distribution by direct Hamming comparisons and multisource breadth-first search of the 22-cube; these agree in every bucket, including zero counts beyond radius 8.

Run from the directory containing both files:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify codewords.txt
```

Expected output:

```text
VERIFY_OK SIZE 84 DISTANCE 9 RADIUS 8 DEEP 176
0 84
1 1848
2 19404
3 129360
4 614460
5 1712308
6 1566756
7 149908
8 176
TOTAL 4194304 FIRST_DEEP 78501 MEAN 21899416/4194304
```

Direct comparison uses exact integer popcounts. The BFS uses one-bit-flip edges and is therefore an independent implementation of nearest Hamming distance; its search reaches precisely the full ambient domain. The distance sum reduces to mean \(2737427/524288\). The codewords are attributed to Ota, Osa and Harada, arXiv:2610.11609v1. This is an exhaustive certificate for a finite instance; it is not an argument for a parameter family or for covering-radius optimality among all codes. Independent mathematical audit has not been performed.
