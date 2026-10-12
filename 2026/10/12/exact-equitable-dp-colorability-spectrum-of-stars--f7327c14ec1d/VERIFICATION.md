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
# Verification

The analytic proof has two critical checks.

First, after fixing the center to a color \(\alpha\), each leaf loses at most one of its \(k\) colors. For every subset of leaves, the union of available colors therefore contains at least \(k-1\) labels. With residual capacity \(m\) on each label except capacity \(m-1\) on \(\alpha\), every such union has capacity at least \(m(k-1)-1\). The hypothesis \(m(k-1)\ge n\) makes this at least the total number \(n-1\) of leaves, which is stronger than every capacitated Hall inequality needed.

Second, when \(m(k-1)<n\) and \(k\ge2\), the plain cyclic cover using \(\tau(i)=i+1\pmod{k}\) forbids \(\tau(\alpha)\) at every leaf once the center is colored \(\alpha\). The center consumes one slot of \(\alpha\), so all leaves together have at most \(m(k-1)-1<n-1\) admissible color slots. This is a finite-capacity obstruction, not a probabilistic or computational inference. For \(k=1\), one matched edge already has no coloring.

`verify.py` independently exhausts all plain full covers for \(2\le n\le4\), \(1\le k\le4\), and directly solves the bounded-coloring problem. It also checks the arithmetic Hall and cyclic-obstruction inequalities for \(2\le n\le200\), \(1\le k\le200\). Its recorded output is in `verification_output.txt`.

Finite replay does not prove the universal quantifiers; it only stress-tests the analytic argument and the delicate boundary cases.
