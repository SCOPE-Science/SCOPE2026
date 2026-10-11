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

The verification is symbolic. For \(u^{(k)}=e_1+\cdots+e_k\), one has \(\|u^{(k)}\|_r=1\), \(u^{(k)}\uparrow\mathbf1\), and \(\|\mathbf1\|_r=r\), certifying the sharp lower bound for demicontinuity.

Every functional on \(c\) decomposes into an \(\ell_1\) coordinate functional plus a multiple of ordinary limit. The decreasing sequence \(\mathbf1-u^{(k)}\downarrow0\) eliminates the limit component from the order-continuous dual. Finite-support sign vectors show that the remaining \(\ell_1\) functional has dual norm exactly its \(\ell_1\)-norm. Hence the order-continuous norming gauge is exactly \(\|x\|_\infty\), whose worst ratio to \(\|x\|_r\) is \(r\).

In the coordinate universal completion, finite truncations of every bounded positive sequence increase to it and have \(\|\cdot\|_r\)-norm bounded by the sup norm; conversely any upward approximants bounded in \(\|\cdot\|_r\) are bounded coordinatewise by the same constant. Therefore the Lorentz norm is exactly the sup norm and its finite domain is \(\ell_\infty\).

For the extension step, a norm-one Hahn--Banach extension \(L\) of ordinary limit satisfies \(L(\mathbf1)=1\). If \(0\le x\le\mathbf1\), then \(\|\mathbf1-x\|_\infty\le1\), so \(Lx=1-L(\mathbf1-x)\ge0\); thus \(L\) is positive. The same increasing truncations have extension norm \(1\) and supremum \(\mathbf1\) of norm \(r\), while positivity yields the matching upper bound.

No computation, sampled search, or finite enumeration is used to establish any infinite assertion. The result is limited to the displayed canonical renorming family and does not determine the optimal universal constant in the general theory.
