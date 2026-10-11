---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

At \(n=6\), the law \(\operatorname{Bin}(6,1/2)\) is symmetric about three, so all three left-loadedness coefficients vanish. For \(n>6\), Simmons' binomial inequality gives \(\alpha_1>0\). Putting \(x=n-3\ge4\), fresh algebra confirms \(\Pr(X=6)/\Pr(X=0)-1=(x-3)Q(x)/(80x^5)\) with \(Q(x)=x^4+246x^3+333x^2-216x-324\), and \(Q(x)=x^4+246x^3+333(x-4)^2+2448(x-4)+4140>0\). Hence \(\Pr(X=6)>\Pr(X=0)\), so \(\alpha_3<0\). With only \(\alpha_2\) between these endpoint coefficients, either sign of \(\alpha_2\) produces exactly the \(L_1\) single-sign-change condition. This proves every integer \(n\ge6\), not merely a finite test range.

## originality

PASS

The complete 2022 primary paper explicitly proves binomial left-loadedness for means one and two and for \(4\le m\le n/3\), then states Conjecture 4.1 for all \(n\ge2m\); the displayed page therefore leaves \(m=3\) as the isolated first missing integer-mean slice. Simmons' theorem supplies only the near-mean sign \(\alpha_1>0\), not the far-tail sign needed for \(L_1\). Current Resultary and exact web searches for left-loadedness, \(\operatorname{Bin}(n,3/n)\), and Conjecture 4.1 found no later theorem covering this slice.

## value

PASS

Mean three is not an arbitrary small parameter: the motivating paper proves means one and two, then a separate range beginning at four, making three the isolated first missing integer-mean case. The argument closes that natural gap for every \(n\ge6\) with a uniform endpoint mechanism and makes the source's tail-comparison theorem available for this whole slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
