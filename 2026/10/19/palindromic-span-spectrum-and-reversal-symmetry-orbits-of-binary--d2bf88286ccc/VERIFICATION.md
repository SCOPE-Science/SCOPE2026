---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A de Bruijn rotation class has one root at its unique 00000, and the rooted windows trace an Euler circuit on the graph of 4-bit vertices and 5-bit edges. Conversely a rooted Euler circuit gives exactly one such rotation class. The frozen feedback encoding also exhausts all classes: for a fixed 4-bit tail the two incoming 5-bit states must append opposite bits, leaving one Boolean choice. The independent rooted Euler traversal found 2048 cycles. Its span histogram was {7:200, 8:192, 9:856, 10:128, 11:392, 12:32, 13:200, 15:48}. In the same order the orbit pairs (size 2 count, size 4 count) were (14,43), (4,46), (6,211), (0,32), (6,95), (0,8), (2,49), (0,12), with no other orbit sizes. The independent test of all palindromes at lengths 14,15,16,17 removed the distinct edges of each candidate and tested the residual directed Euler-trail balance, endpoints and weak connectivity; its extendible counts were 0,6,0,0. The centered subpalindrome property rules out all longer even lengths from 14 onward and odd lengths from 17 onward, including beyond one period. The unique all-zero window is flanked by 1 on both sides, so the span cannot be less than 7. Both frozen extremizers were verified among the rooted cycles at their claimed lengths.

## originality

PASS

The de Bruijn count, the orbit-size mechanism and closely related reversal conventions have prior coverage. The span-resolved orbit census is distinct in the inspected literature. A later indexed census explicitly reproduces the entire longest-span marginal and could support a derived orbit breakdown if its stated cycle-level data are used; it is not evidence of earlier coverage, and the recorded finding inspected does not report the span-resolved orbit counts.

## value

PASS

The longest reversible factor distinguishes cycles whose order-length factor sets are identical. The span-resolved orbit census records both an exact extremal boundary and how often local palindromic structure coexists with global complement/reversal symmetry. It gives a reproducible baseline for this complete finite class rather than sampling arbitrary sequences or recounting a known total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
