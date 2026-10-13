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
## Structural check
The source factorization at the third level gives, up to translation and reflection,
\[
S=B_1+d_1B_2+d_2B_3.
\]
After sorting the positive weights as \(\{1,u,v\}\), the complete subset-sum list
\[
0,1,u,v,1+u,1+v,u+v,1+u+v
\]
shows that every collision is caused by \(u=1\), \(u=v\), or \(v=u+1\). This produces exactly five entropy types.

## Curvature check
With \(h(p)=-p\log p-(1-p)\log(1-p)\) and \(s=p(1-p)\), the five formulas are
\[
3h,
\quad
3h-3s\log3,
\quad
3h-2s\log2,
\quad
(3-s)h,
\quad
(3-s)h-2s\log2.
\]
The first three have immediate negative second derivative because \(h''=-1/s\) and \(s\le1/4\). For \(G=(3-s)h\),
\[
G''=
2h+
2(2p-1)\log\frac{1-p}{p}
+1-\frac3s.
\]
The logarithmic middle term is nonpositive, \(h\le\log2\), and \(3/s\ge12\), so
\[
G''\le-11+2\log2<0.
\]
The final type adds \(4\log2\) to this curvature and still satisfies
\[
G''+4\log2\le-11+6\log2<0.
\]

## Literature check
The complete direct preprint arXiv:2609.05546 was inspected. It states the conjecture, proves only the binomial and fully non-overlapping regimes, and reports computation for other sequences. The closely related weighted-Bernoulli paper arXiv:2609.01529 was inspected through its main argument; it fixes unbiased Bernoulli variables and does not provide the varying-bias Shannon-concavity theorem.

## Limits
The verification establishes the theorem only for the third recursive level. It does not certify the conjecture for four or more Bernoulli coordinates, where multiple simultaneous subset-sum collisions can occur.
