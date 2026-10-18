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
# Verification and limits

## Mathematical checks performed

The interval-sum lemma \(n\in\langle a,a+1,\ldots,a+k\rangle\iff\lceil n/(a+k)\rceil\le\lfloor n/a\rfloor\) was independently checked against the residue-threshold description. The parity correction to each Apéry representative is derived from \(2r\equiv j\pmod a\), not guessed from observed samples. The maxima were verified separately for odd \(t\), even \(t\) with \(q\ge2\), and even \(t\) with \(q=1\). Blockwise parity-count sums were simplified exactly for the genus formula. No step uses a finite experiment as an infinite proof.

The complete `check.py` was executed with Python 3 and reported: `PASS: 3364 parameter pairs; 844484 membership comparisons; 273586 Apéry-minimality comparisons`. It uses a direct inequality on twice the target integer for independent membership testing, derives the observed gap maximum and count by enumeration, and checks that every proposed Apéry element is minimal in its residue class. This is bounded validation over \(5\le a\le119\) with \(a\) odd and every admissible \(k\), not an exhaustive proof beyond that range.

## Scientific and access limits

The genus expression may be implied by Lee–Nam's published general genus computation and is not claimed as a new discovery. The full paper was unavailable via the available lawful pathways; a publisher preview and abstract were inspected. Related original papers by Adeniran et al. and Liu were materially read, including their scope restrictions and open-problem statements. Result database hits concerned structurally different semigroups or invariants; absence of a hit alone cannot establish novelty. The manuscript underwent self-review only; independent audit is not performed.
