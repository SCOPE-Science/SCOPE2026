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

The argument is analytic. Its critical checks are:

1. The upper-regime inequality is equivalent to
\[
2t<\frac{d+1}{2}n,
\qquad t=\frac{dn-m}{2},
\]
which is exactly the strict-separation condition for corner centers whose mutual Hamming distance is \((d+1)/2\).

2. A single cap is transformed by coordinate reflections to
\[
\left\{z\in[0,n]^d:\sum_i z_i<t\right\}.
\]
Inclusion-exclusion over the coordinate events \(z_i>n\) gives
\[
\frac1{d!}\sum_{k=0}^d(-1)^k\binom{d}{k}(t-kn)_+^d.
\]
After multiplying by \(2^d\) for the affine chart and substituting \(t=(dn-m)/2\), this is exactly the stated volume formula.

3. At \(m_j=(d-2j)n\), only the \(j\)-th positive-part term changes branch. Therefore all derivatives through order \(d-1\) are continuous, while the right-minus-left jump of the \(d\)-th derivative is
\[
(d+1)(-1)^{j+d}\binom{d}{j}.
\]

4. At the same parameter, the cut boundary passes through exactly the Hamming layer of radius \(j\) around each of the \(d+1\) Hadamard corners. Since \(2j<(d+1)/2\), those layers are disjoint, so their total size is exactly
\[
(d+1)\binom{d}{j}.
\]
The source's local cone shows that these are precisely the nonsimple vertices.

5. In the local cone, the extreme rays are \(e_a\) for the \(d-j\) negative-side indices and \(e_a+e_b\) for an ordered choice of one negative-side and one positive-side index. Hence the degree is
\[
(d-j)+j(d-j)=(j+1)(d-j).
\]

As a concrete consistency check, \(d=7\) has the unique internal resonance \(j=1\). The formulas give \(56\) nonsimple vertices, degree \(12\), total vertex count \(120\), and a seventh-derivative jump of magnitude \(56\).

The checks establish only the strict upper regime. They do not assert a formula when corner cuts overlap, and they do not derive normality or Ehrhart properties from the volume calculation.
