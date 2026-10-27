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

# Reproducibility of the distance enumerator

Execute the included standalone Python 3 scripts, requiring only the standard library:

```sh
python3 check_bfs.py
python3 check_cycles.py
```

`check_bfs.py` enumerates almost-perfect matchings as edge tuples, constructs each legal replacement, confirms regular degree and reciprocal adjacency, and computes ordinary breadth-first-search distances from a canonical vertex. It covers \(3\le2m+1\le11\).

`check_cycles.py` uses a differently ordered pairing generator. It never constructs a flip graph: it computes the symmetric-difference component statistic from every canonical pair and independently evaluates the combinatorial cycle/path recurrence for all \(1\le m\le5\). Assertions check their agreement and the full number of states.

The captured outputs `check_bfs.out` and `check_cycles.out` are byte-for-byte records of the two scripts executed with the packaged source. They confirm five sizes; they are not, by themselves, an infinite proof. The argument valid for every positive integer \(m\) is in `RESULT.md`.

No independent external audit is recorded.
