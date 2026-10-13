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

The standalone `verify.py` artifact was read from its packaged path before replay.

The checker constructs the ideal-intersection graph directly from exponent pairs
\[
(i,j)
\]
using the exact rule
\[
I_{i,j}\cap I_{k,\ell}\ne0
\quad\Longleftrightarrow\quad
\max(i,k)<\alpha
\ \text{or}\
\max(j,\ell)<\beta.
\]

It verifies the three canonical class sizes and the fact that the only missing edges form the complete bipartite block between the two boundary classes.

For every small exponent pair with graph order at most \(15\), all vertex subsets are exhaustively enumerated and the full zero forcing polynomial is compared with the closed form.

The real symmetric rank-two Gram witness is checked entry-by-entry and by exact rational row reduction.

Finally, the two polynomial collisions are verified directly and shown to have different degree multisets. A finite exponent census through \(79\) corroborates that no other collisions appear there; the proof of global uniqueness uses the symbolic Diophantine argument in `RESULT.md`, not this finite scan.

Exact replay output:

```text
(1,1): N=2, polynomial={2: 1}, witness_rank=0
(1,2): N=4, polynomial={2: 5, 3: 4, 4: 1}, witness_rank=2
(1,3): N=6, polynomial={4: 11, 5: 6, 6: 1}, witness_rank=2
(1,4): N=8, polynomial={6: 19, 7: 8, 8: 1}, witness_rank=2
(2,2): N=7, polynomial={5: 16, 6: 7, 7: 1}, witness_rank=2
(2,3): N=10, polynomial={8: 31, 9: 10, 10: 1}, witness_rank=2
(2,4): N=13, polynomial={11: 50, 12: 13, 13: 1}, witness_rank=2
(3,3): N=14, polynomial={12: 57, 13: 14, 14: 1}, witness_rank=2
(3,4): N=18, predicted={16: 89, 17: 18, 18: 1}, witness_rank=2
(4,4): N=23, predicted={21: 136, 22: 23, 23: 1}, witness_rank=2
collision (1,9) ~ (3,4): polynomial={16: 89, 17: 18, 18: 1}, degree_multisets_differ
collision (1,11) ~ (2,7): polynomial={20: 131, 21: 22, 22: 1}, degree_multisets_differ
COLLISION_CENSUS_OK
VERIFY_OK
```
