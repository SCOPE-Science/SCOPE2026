---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Alspach's theorem gives, for each base arc, a containing base cycle of every length \(3\le t\le c\). For any target \(\ell\), the integer intervals \([3k,ck]\), \(1\le k\le\alpha\), cover all lengths 3 through \(c\alpha\) when \(c\ge5\). Writing \(\ell=t_1+\cdots+t_k\) with each \(t_j\in[3,c]\), choose k base cycles containing the prescribed arc and lift them on distinct layer indices. Concatenating each cycle's terminal-to-u arc into the next layer gives a simple directed cycle of length \(\ell\); distinct layers prevent repeated lifted vertices. The c=3 exclusion is genuine.

## originality

PASS

Alspach proves arc-pancyclicity only in a regular tournament, while Pan--Zhang's regular multipartite result controls the number of partite sets met, not every vertex length. Xia's 2026 theorem gives all lengths from 4 upward only for arbitrary regular equal-part multipartite tournaments with at least 93 parts. The submitted theorem is an exact full-length result, including triangles, for the natural equal-blow-up subclass for every regular base order \(c\ge5\). No checked composition theorem states this lift.

## value

PASS

This gives complete arc-pancyclicity on a natural infinite subclass of regular multipartite tournaments for every admissible base order \(c\ge5\), far below the current general c>=93 range. It also includes triangles and supplies an explicit cycle construction, so it is a motivated structural special-class theorem rather than a small parameter improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
