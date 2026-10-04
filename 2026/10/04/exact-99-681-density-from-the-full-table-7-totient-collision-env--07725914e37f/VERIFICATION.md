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
Run `python3 verify.py` in this package.

The checker first evaluates Euler's totient function independently and verifies
\[
(a+1)\varphi(a)=(b+1)\varphi(b)
\]
for every one of the \(28\) pairs in `pairs.json`.

For each pair it factors \(ab\) and constructs the prime-support set controlling the condition
\[
\gcd(c,ab)=1.
\]
It removes only support sets that properly contain another support set, since their coprimality events are subsets already present in the union. This leaves \(24\) irredundant events involving \(36\) primes.

The checker then counts residue classes exactly modulo the product of those \(36\) primes. At each prime \(p\), there are \(p-1\) residue classes in which \(p\) does not divide \(c\) and one in which it does. The state records which coprimality events have already been hit by a divisor of \(c\). This integer recurrence exhausts every residue class of the full squarefree modulus.

The resulting certified residue count is
\[
17851536920594151532588547718201906028355218104887683983832041343882,
\]
out of
\[
17908663449893375001554206957763965693924172368887203729748237321510.
\]
Reduction gives the fraction stated in the finding.

The verification concerns the exact finite Table-7 certificate envelope. It does not test or certify noninjectivity for parameters outside that envelope.

A successful replay prints `VERIFY_OK`.
